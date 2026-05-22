#!/usr/bin/env python3
"""
微信支付文档抓取工具
- 支持直连商户(merchant)和合作伙伴(partner)两种文档类型
- 从官方 llms.txt 获取 Markdown 文档 URL 列表和层级结构
- 从首页 HTML JSON 中提取 updateTime 变更信息
- 直接从官方 .md 路径下载 Markdown 文档
- 通过 git 跟踪所有文件变更，不再保留时间戳副本
"""

import difflib
import json
import os
import re
import time
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class WechatPayDocFetcher:
    """微信支付文档抓取器"""

    DOC_TYPES = {
        "merchant": {
            "name": "直连商户",
            "index_url": "https://pay.weixin.qq.com/doc/v3/merchant/4012062524",
            "llms_url": "https://pay.weixin.qq.com/doc/v3/merchant/llms.txt",
            "subdir": "merchant",
        },
        "partner": {
            "name": "合作伙伴",
            "index_url": "https://pay.weixin.qq.com/doc/v3/partner/4012069852",
            "llms_url": "https://pay.weixin.qq.com/doc/v3/partner/llms.txt",
            "subdir": "partner",
        },
    }

    def __init__(self, doc_type: str = "merchant", base_dir: str = "docs"):
        if doc_type not in self.DOC_TYPES:
            raise ValueError(f"不支持的文档类型: {doc_type}，支持: {list(self.DOC_TYPES.keys())}")

        self.doc_type = doc_type
        self.doc_config = self.DOC_TYPES[doc_type]
        self.base_dir = Path(base_dir) / self.doc_config["subdir"]
        self.index_url = self.doc_config["index_url"]
        self.llms_url = self.doc_config["llms_url"]
        self.diff_preview_lines = 200

        self.pages_dir = self.base_dir / "pages"
        self.pages_dir.mkdir(parents=True, exist_ok=True)

        # 单一文件路径，git 负责跟踪历史
        self.llms_file = self.base_dir / "llms.txt"
        self.index_file = self.base_dir / "index.json"
        self.report_file = self.base_dir / "report.md"

    def fetch_text(self, url: str, max_retries: int = 3) -> Optional[str]:
        """获取远端文本内容"""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

        for attempt in range(max_retries):
            try:
                request = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(request, timeout=30) as response:
                    charset = response.headers.get_content_charset() or "utf-8"
                    return response.read().decode(charset, errors="replace")
            except Exception as exc:
                print(f"  尝试 {attempt + 1}/{max_retries} 失败: {exc}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                else:
                    return None
        return None

    def parse_llms_txt(self, content: str) -> List[Dict]:
        """解析 llms.txt 获取文档列表和层级结构"""
        nodes: List[Dict] = []
        heading_stack: List[Tuple[int, str]] = []

        for line in content.splitlines():
            heading_match = re.match(r'^(#{1,6})\s+(.*)', line)
            if heading_match:
                level = len(heading_match.group(1))
                title = heading_match.group(2).strip()
                while heading_stack and heading_stack[-1][0] >= level:
                    heading_stack.pop()
                heading_stack.append((level, title))
                continue

            link_match = re.match(r'^-\s+\[([^\]]+)\]\(([^)]+\.md)\)', line)
            if link_match:
                title = link_match.group(1).strip()
                url = link_match.group(2).strip()
                if url.startswith("/"):
                    url = f"https://pay.weixin.qq.com{url}"

                doc_id_match = re.search(r'/(\d+)\.md$', url)
                doc_id = doc_id_match.group(1) if doc_id_match else ""

                path_parts = [h_title for h_level, h_title in heading_stack if h_level >= 2]
                full_path = " > ".join(path_parts) if path_parts else title

                nodes.append({
                    "docId": doc_id,
                    "title": title,
                    "url": url,
                    "updateTime": "",
                    "fullPath": full_path,
                })

        return nodes

    def extract_json_data(self, html: str) -> Optional[Dict]:
        """从 HTML 中提取 vike_pageContext JSON 数据包"""
        pattern = r'<script id="vike_pageContext" type="application/json">(.*?)</script>'
        match = re.search(pattern, html, re.DOTALL)
        if not match:
            print("  错误: 未找到 vike_pageContext 数据包")
            return None
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError as exc:
            print(f"  错误: JSON 解析失败: {exc}")
            return None

    def extract_leaf_nodes(self, data: Dict) -> List[Dict]:
        """递归提取所有叶子节点（state 为 0 的有效页面）"""
        leaf_nodes: List[Dict] = []

        def traverse(node: Dict, path: Optional[List[str]] = None):
            current_path = (path or []) + [node.get("title", "")]
            children = node.get("childrenList", []) or []
            state = node.get("state", 0)
            if state == 1:
                return
            if not children:
                leaf_nodes.append({
                    "docId": node.get("docId", ""),
                    "title": node.get("title", ""),
                    "updateTime": str(node.get("updateTime", "")),
                    "url": node.get("url", ""),
                    "fullPath": " > ".join(filter(None, current_path)),
                    "pathArray": [item["title"] for item in node.get("pathArray", []) if item.get("title")],
                })
                return
            for child in children:
                traverse(child, current_path)

        for root_node in data.get("data", {}).get("menuData", []):
            traverse(root_node)
        return leaf_nodes

    def merge_with_update_time(self, llms_nodes: List[Dict], json_nodes: List[Dict]) -> List[Dict]:
        """将 llms.txt 的 URL 信息与 JSON 的 updateTime 合并"""
        json_map = {node["docId"]: node for node in json_nodes}
        result: List[Dict] = []
        for node in llms_nodes:
            json_node = json_map.get(node["docId"])
            if json_node:
                node["updateTime"] = json_node.get("updateTime", "")
            result.append(node)
        return result

    def load_index(self) -> Dict[str, Dict]:
        """加载本地 index.json 并按 docId 返回"""
        if not self.index_file.exists():
            return {}
        try:
            with open(self.index_file, "r", encoding="utf-8") as file_obj:
                data = json.load(file_obj)
        except Exception as exc:
            print(f"  警告: 加载索引失败: {exc}")
            return {}
        return {node["docId"]: node for node in data.get("nodes", [])}

    def save_index(self, nodes: List[Dict], run_time: str):
        """覆盖写入 index.json"""
        index_data = {
            "runTime": run_time,
            "totalNodes": len(nodes),
            "docType": self.doc_type,
            "docTypeName": self.doc_config["name"],
            "nodes": nodes,
        }
        with open(self.index_file, "w", encoding="utf-8") as file_obj:
            json.dump(index_data, file_obj, ensure_ascii=False, indent=2)

    def save_llms_txt(self, content: str, run_time: str) -> Optional[str]:
        """覆盖写入 llms.txt，内容有变更时返回 unified diff"""
        previous_content = None
        if self.llms_file.exists():
            try:
                with open(self.llms_file, "r", encoding="utf-8") as file_obj:
                    previous_content = file_obj.read()
            except Exception:
                pass

        if previous_content is not None and previous_content == content:
            return None

        with open(self.llms_file, "w", encoding="utf-8") as file_obj:
            file_obj.write(content)

        if previous_content is None:
            return None

        old_lines = previous_content.splitlines()
        new_lines = content.splitlines()
        diff_lines = list(difflib.unified_diff(
            old_lines, new_lines,
            fromfile="llms_old.txt", tofile="llms.txt",
            lineterm="", n=3,
        ))
        return "\n".join(diff_lines) if diff_lines else None

    def detect_changes(
        self, new_nodes: List[Dict], old_index: Dict[str, Dict]
    ) -> Tuple[List[Dict], List[Dict], List[Dict]]:
        """检测新增、删除、修改节点"""
        new_dict = {node["docId"]: node for node in new_nodes}
        added: List[Dict] = []
        removed: List[Dict] = []
        modified: List[Dict] = []

        for doc_id, node in new_dict.items():
            if doc_id not in old_index:
                added.append(node)

        for doc_id, node in old_index.items():
            if doc_id not in new_dict:
                removed.append(node)

        for doc_id, new_node in new_dict.items():
            old_node = old_index.get(doc_id)
            if not old_node:
                continue
            if str(new_node.get("updateTime", "")) != str(old_node.get("updateTime", "")):
                modified.append({
                    "docId": doc_id,
                    "title": new_node["title"],
                    "url": new_node["url"],
                    "fullPath": new_node["fullPath"],
                    "oldUpdateTime": str(old_node.get("updateTime", "")),
                    "newUpdateTime": str(new_node.get("updateTime", "")),
                })

        return added, removed, modified

    def get_markdown_path(self, doc_id: str) -> Path:
        """返回 Markdown 文件路径: pages/{docId}.md"""
        return self.pages_dir / f"{doc_id}.md"

    def read_markdown(self, doc_id: str) -> Optional[str]:
        """读取本地 Markdown 文件"""
        path = self.get_markdown_path(doc_id)
        if not path.exists():
            return None
        with open(path, "r", encoding="utf-8") as file_obj:
            return file_obj.read()

    def save_markdown(self, node: Dict) -> Tuple[bool, bool, Optional[str]]:
        """下载并保存 Markdown 文件为 pages/{docId}.md。
        返回 (success, was_fetched, old_content_or_none)。
        old_content 用于后续 diff 生成。"""
        doc_id = node["docId"]
        markdown_url = node["url"]
        markdown_path = self.get_markdown_path(doc_id)

        old_content = self.read_markdown(doc_id)

        print(f"  拉取: {node['title']} ({doc_id})")
        markdown_content = self.fetch_text(markdown_url)
        if markdown_content is None:
            return False, True, None

        # 内容完全一致则跳过写入
        if old_content is not None and old_content == markdown_content:
            print(f"    (内容未变化，跳过写入)")
            return True, False, old_content

        with open(markdown_path, "w", encoding="utf-8") as file_obj:
            file_obj.write(markdown_content)

        return True, True, old_content

    def build_diff(self, old_content: Optional[str], new_content: str) -> Optional[str]:
        """生成 unified diff"""
        if old_content is None:
            return None
        old_lines = old_content.splitlines()
        new_lines = new_content.splitlines()
        diff_lines = list(difflib.unified_diff(
            old_lines, new_lines,
            fromfile="old.md", tofile="new.md",
            lineterm="", n=3,
        ))
        if not diff_lines:
            return "无正文差异，可能仅更新时间发生变化。"
        if len(diff_lines) > self.diff_preview_lines:
            remaining = len(diff_lines) - self.diff_preview_lines
            diff_lines = diff_lines[:self.diff_preview_lines]
            diff_lines.append(f"... 已截断其余 {remaining} 行 diff")
        return "\n".join(diff_lines)

    def format_timestamp(self, timestamp: str) -> str:
        """格式化 Unix 时间戳"""
        try:
            return datetime.fromtimestamp(int(timestamp)).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            return timestamp

    def generate_report(
        self,
        run_time: str,
        total_nodes: int,
        added: List[Dict],
        removed: List[Dict],
        modified: List[Dict],
        fetch_success: List[str],
        fetch_failed: List[str],
        diff_details: Dict[str, Optional[str]],
        all_nodes: List[Dict],
        llms_diff: Optional[str] = None,
    ) -> str:
        """生成 Markdown 差异报告"""
        report_lines = [
            f"# 微信支付文档更新报告 - {self.doc_config['name']}",
            "",
            f"**文档类型**: {self.doc_config['name']} ({self.doc_type})",
            f"**生成时间**: {run_time}",
            f"**文档总数**: {total_nodes}",
            f"**数据来源**: {self.llms_url}",
            "",
            "## 变更概览",
            "",
            f"- 新增: {len(added)} 个页面",
            f"- 删除: {len(removed)} 个页面",
            f"- 修改: {len(modified)} 个页面",
            f"- 成功拉取: {len(fetch_success)} 个页面",
            f"- 拉取失败: {len(fetch_failed)} 个页面",
            f"- llms.txt 变更: {'是' if llms_diff else '否'}",
            "",
        ]

        if llms_diff:
            report_lines.extend([
                "## llms.txt 变更",
                "",
                "```diff",
                llms_diff,
                "```",
                "",
            ])

        if added:
            report_lines.extend(["## 新增页面", ""])
            for node in added:
                report_lines.extend([
                    f"### {node['title']}",
                    f"- ID: `{node['docId']}`",
                    f"- 路径: {node['fullPath']}",
                    f"- URL: {node['url']}",
                    f"- 更新时间: {self.format_timestamp(str(node.get('updateTime', '')))}",
                    f"- 本地文件: `pages/{node['docId']}.md`",
                    "",
                ])

        if removed:
            report_lines.extend(["## 删除页面", ""])
            for node in removed:
                report_lines.extend([
                    f"- **{node['title']}** (`{node['docId']}`)",
                    f"  - 原路径: {node.get('fullPath', '')}",
                    f"  - 原 URL: {node.get('url', '')}",
                    f"  - 原更新时间: {self.format_timestamp(str(node.get('updateTime', '')))}",
                    "",
                ])

        if modified:
            report_lines.extend(["## 修改页面", ""])
            for node in modified:
                report_lines.extend([
                    f"### {node['title']}",
                    f"- ID: `{node['docId']}`",
                    f"- 路径: {node['fullPath']}",
                    f"- URL: {node['url']}",
                    f"- 更新时间变更: {self.format_timestamp(node['oldUpdateTime'])} -> {self.format_timestamp(node['newUpdateTime'])}",
                    f"- 本地文件: `pages/{node['docId']}.md`",
                    "",
                    "```diff",
                    diff_details.get(node["docId"]) or "无法生成 diff：缺少本地旧版本。",
                    "```",
                    "",
                ])

        if fetch_failed:
            report_lines.extend(["## 拉取失败", ""])
            failed_lookup = {node["docId"]: node for node in added}
            failed_lookup.update({node["docId"]: node for node in modified})
            for doc_id in fetch_failed:
                node = failed_lookup.get(doc_id)
                if node:
                    report_lines.append(f"- {node['title']} (`{doc_id}`): {node['url']}")
                    report_lines.append("")

        report_lines.extend([
            "## 附录：所有页面清单",
            "",
            f"<details>",
            f"<summary>点击查看全部 {total_nodes} 个页面</summary>",
            "",
            "| 序号 | 标题（链接） | ID | 更新时间 | 完整路径 |",
            "|------|-------------|----|----------|----------|",
        ])

        for index, node in enumerate(all_nodes, start=1):
            update_time = str(node.get("updateTime", ""))
            report_lines.append(
                f"| {index} | [{node['title']}](pages/{node['docId']}.md) | "
                f"`{node['docId']}` | {self.format_timestamp(update_time)} | {node['fullPath']} |"
            )

        report_lines.extend(["", "</details>"])
        return "\n".join(report_lines)

    def run(self, limit: Optional[int] = None):
        """运行抓取流程"""
        run_time = datetime.now().strftime("%Y%m%d_%H%M%S")

        print(f"[{run_time}] 开始抓取微信支付文档 - {self.doc_config['name']}")
        print(f"  llms.txt: {self.llms_url}")
        print(f"  首页: {self.index_url}")

        # Step 1: Fetch llms.txt
        print("\n[1/6] 获取 llms.txt...")
        llms_content = self.fetch_text(self.llms_url)
        if not llms_content:
            print("  错误: 无法获取 llms.txt")
            return
        llms_diff = self.save_llms_txt(llms_content, run_time)
        if llms_diff:
            print("  llms.txt 有变更")

        # Step 2: Parse llms.txt
        print("\n[2/6] 解析 llms.txt 获取文档 URL 和层级...")
        leaf_nodes = self.parse_llms_txt(llms_content)
        print(f"  从 llms.txt 提取到 {len(leaf_nodes)} 个文档")
        if limit and limit > 0:
            leaf_nodes = leaf_nodes[:limit]
            print(f"  测试模式：仅处理前 {limit} 个节点")

        # Step 3: Fetch JSON for updateTime
        print("\n[3/6] 获取首页 JSON（用于 updateTime）...")
        html = self.fetch_text(self.index_url)
        if html:
            json_data = self.extract_json_data(html)
            if json_data:
                json_nodes = self.extract_leaf_nodes(json_data)
                print(f"  从 JSON 提取到 {len(json_nodes)} 个节点（含 updateTime）")
                leaf_nodes = self.merge_with_update_time(leaf_nodes, json_nodes)
                matched = sum(1 for n in leaf_nodes if n.get("updateTime"))
                print(f"  成功匹配 updateTime: {matched}/{len(leaf_nodes)} 个文档")
            else:
                print("  警告: 无法解析 JSON，文档将缺少 updateTime")
        else:
            print("  警告: 无法获取首页，文档将缺少 updateTime")

        # Step 4: Detect changes
        print("\n[4/6] 检测变更...")
        old_index = self.load_index()
        is_first_run = not old_index
        if is_first_run:
            print("  首次运行：将拉取所有页面")
            added = leaf_nodes
            removed = []
            modified = []
        else:
            added, removed, modified = self.detect_changes(leaf_nodes, old_index)
            print(f"  新增: {len(added)} 个")
            print(f"  删除: {len(removed)} 个")
            print(f"  修改: {len(modified)} 个")

        # Step 5: Fetch changed pages
        nodes_to_fetch = list(added)
        modified_node_ids = {node["docId"] for node in modified}
        nodes_to_fetch.extend(node for node in leaf_nodes if node["docId"] in modified_node_ids)

        if nodes_to_fetch:
            print(f"\n[5/6] 拉取变更页面（共 {len(nodes_to_fetch)} 个）...")
        else:
            print(f"\n[5/6] 拉取变更页面...")
            print("  无页面需要拉取")

        fetch_success: List[str] = []
        fetch_failed: List[str] = []
        old_contents: Dict[str, Optional[str]] = {}

        for index, node in enumerate(nodes_to_fetch, start=1):
            print(f"  [{index}/{len(nodes_to_fetch)}] ", end="")
            success, was_fetched, old_content = self.save_markdown(node)
            if success:
                fetch_success.append(node["docId"])
                old_contents[node["docId"]] = old_content
            else:
                fetch_failed.append(node["docId"])
            if was_fetched and index < len(nodes_to_fetch):
                time.sleep(0.5)

        print(f"\n  成功: {len(fetch_success)} 个")
        print(f"  失败: {len(fetch_failed)} 个")

        has_changes = bool(added or removed or modified or llms_diff)
        if not is_first_run and not has_changes:
            print("\n[OK] 完成! 无变更，跳过保存索引和报告")
            return

        # Step 6: Generate diff for modified pages
        print("\n[6/6] 生成报告...")
        self.save_index(leaf_nodes, run_time)

        diff_details: Dict[str, Optional[str]] = {}
        for node in modified:
            doc_id = node["docId"]
            old_content = old_contents.get(doc_id) or self.read_markdown(doc_id)
            new_content = self.read_markdown(doc_id)
            if old_content and new_content:
                diff_details[doc_id] = self.build_diff(old_content, new_content)
            else:
                diff_details[doc_id] = None

        report_content = self.generate_report(
            run_time=run_time,
            total_nodes=len(leaf_nodes),
            added=added,
            removed=removed,
            modified=modified,
            fetch_success=fetch_success,
            fetch_failed=fetch_failed,
            diff_details=diff_details,
            all_nodes=leaf_nodes,
            llms_diff=llms_diff,
        )

        with open(self.report_file, "w", encoding="utf-8") as file_obj:
            file_obj.write(report_content)

        print("\n[OK] 完成!")
        print(f"   llms.txt:  {self.llms_file}")
        print(f"   index.json: {self.index_file}")
        print(f"   pages/:     {self.pages_dir}")
        print(f"   report.md:  {self.report_file}")


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(
        description="微信支付文档抓取工具 - 支持直连商户和合作伙伴文档",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 抓取直连商户文档（默认）
  python wechatpay_doc_fetcher.py

  # 抓取合作伙伴文档
  python wechatpay_doc_fetcher.py --type partner

  # 测试模式（仅前10个页面）
  python wechatpay_doc_fetcher.py --type merchant --limit 10

  # 指定输出目录
  python wechatpay_doc_fetcher.py --type partner --output ./my_docs
        """,
    )

    parser.add_argument(
        "--type", "-t",
        type=str, default="merchant",
        choices=["merchant", "partner"],
        help="文档类型：merchant(直连商户) 或 partner(合作伙伴)，默认: merchant",
    )
    parser.add_argument(
        "--limit", "-l",
        type=int, default=None,
        help="限制处理的页面数量（用于测试）",
    )
    parser.add_argument(
        "--output", "-o",
        type=str, default="docs",
        help="输出目录（默认: docs）",
    )

    args = parser.parse_args()
    fetcher = WechatPayDocFetcher(doc_type=args.type, base_dir=args.output)
    fetcher.run(limit=args.limit)


if __name__ == "__main__":
    main()

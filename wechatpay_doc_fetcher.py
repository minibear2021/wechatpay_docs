#!/usr/bin/env python3
"""
微信支付文档抓取工具
- 支持直连商户(merchant)和合作伙伴(partner)两种文档类型
- 从首页 HTML 中提取 JSON 索引数据
- 直接抓取官方 Markdown 文档
- 支持增量更新检测与 diff 报告生成
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
            "subdir": "merchant",
        },
        "partner": {
            "name": "合作伙伴",
            "index_url": "https://pay.weixin.qq.com/doc/v3/partner/4012069852",
            "subdir": "partner",
        },
    }

    def __init__(self, doc_type: str = "merchant", base_dir: str = "docs"):
        if doc_type not in self.DOC_TYPES:
            raise ValueError(f"不支持的文档类型: {doc_type}，支持: {list(self.DOC_TYPES.keys())}")

        self.doc_type = doc_type
        self.doc_config = self.DOC_TYPES[doc_type]
        self.base_dir = Path(base_dir) / self.doc_config["subdir"]
        self.base_url = "https://pay.weixin.qq.com"
        self.index_url = self.doc_config["index_url"]
        self.diff_preview_lines = 200

        self.index_dir = self.base_dir / "index"
        self.pages_dir = self.base_dir / "pages"
        self.reports_dir = self.base_dir / "reports"

        self.index_dir.mkdir(parents=True, exist_ok=True)
        self.pages_dir.mkdir(parents=True, exist_ok=True)
        self.reports_dir.mkdir(parents=True, exist_ok=True)

        self.index_file = self.index_dir / "latest.json"

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
        """递归提取所有叶子节点（只处理 state 为 0 的页面）"""
        leaf_nodes: List[Dict] = []

        def traverse(node: Dict, path: Optional[List[str]] = None):
            current_path = (path or []) + [node.get("title", "")]
            children = node.get("childrenList", []) or []
            state = node.get("state", 0)

            if state == 1:
                print(f"  跳过无效页面: {node.get('title', '')} ({node.get('docId', '')}) - state=1")
                return

            if not children:
                leaf_nodes.append(
                    {
                        "docId": node.get("docId", ""),
                        "title": node.get("title", ""),
                        "updateTime": str(node.get("updateTime", "")),
                        "url": node.get("url", ""),
                        "fullPath": " > ".join(filter(None, current_path)),
                        "pathArray": [item["title"] for item in node.get("pathArray", []) if item.get("title")],
                    }
                )
                return

            for child in children:
                traverse(child, current_path)

        for root_node in data.get("data", {}).get("menuData", []):
            traverse(root_node)

        return leaf_nodes

    def load_index(self) -> Dict[str, Dict]:
        """加载索引文件并按 docId 返回"""
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
        """保存带时间戳索引和 latest.json"""
        index_data = {
            "runTime": run_time,
            "totalNodes": len(nodes),
            "docType": self.doc_type,
            "docTypeName": self.doc_config["name"],
            "nodes": nodes,
        }

        timestamped_file = self.index_dir / f"index_{run_time}.json"
        with open(timestamped_file, "w", encoding="utf-8") as file_obj:
            json.dump(index_data, file_obj, ensure_ascii=False, indent=2)

        with open(self.index_file, "w", encoding="utf-8") as file_obj:
            json.dump(index_data, file_obj, ensure_ascii=False, indent=2)

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
            if str(new_node["updateTime"]) != str(old_node.get("updateTime", "")):
                modified.append(
                    {
                        "docId": doc_id,
                        "title": new_node["title"],
                        "url": new_node["url"],
                        "fullPath": new_node["fullPath"],
                        "oldUpdateTime": str(old_node.get("updateTime", "")),
                        "newUpdateTime": str(new_node["updateTime"]),
                    }
                )

        return added, removed, modified

    def build_source_url(self, node: Dict) -> str:
        """构建源文档 URL"""
        url = node["url"]
        return url if url.startswith("http") else f"{self.base_url}{url}"

    def build_markdown_url(self, node: Dict) -> str:
        """构建官方 Markdown URL"""
        source_url = self.build_source_url(node)
        return source_url if source_url.endswith(".md") else f"{source_url}.md"

    def get_markdown_path(self, doc_id: str, update_time: str) -> Path:
        """返回单个版本 Markdown 文件路径"""
        page_dir = self.pages_dir / doc_id
        page_dir.mkdir(parents=True, exist_ok=True)
        return page_dir / f"{doc_id}_{update_time}.md"

    def get_existing_markdown_versions(self, doc_id: str) -> List[Path]:
        """获取本地已保存的 Markdown 版本"""
        page_dir = self.pages_dir / doc_id
        if not page_dir.exists():
            return []

        def sort_key(path: Path) -> Tuple[int, str]:
            match = re.search(r"_(\d+)\.md$", path.name)
            version = int(match.group(1)) if match else -1
            return version, path.name

        return sorted(page_dir.glob(f"{doc_id}_*.md"), key=sort_key)

    def get_previous_markdown_path(self, doc_id: str, update_time: str) -> Optional[Path]:
        """获取当前版本之前的最近一个本地 Markdown 版本"""
        previous_versions = [
            path
            for path in self.get_existing_markdown_versions(doc_id)
            if path.name != f"{doc_id}_{update_time}.md"
        ]
        return previous_versions[-1] if previous_versions else None

    def save_markdown(self, node: Dict) -> Tuple[bool, bool, Optional[Path]]:
        """保存 Markdown 页面内容到本地"""
        doc_id = node["docId"]
        update_time = str(node["updateTime"])
        markdown_url = self.build_markdown_url(node)
        markdown_path = self.get_markdown_path(doc_id, update_time)

        if markdown_path.exists():
            print(f"  跳过: {node['title']} ({doc_id}) - Markdown 已存在")
            return True, False, markdown_path

        print(f"  拉取: {node['title']} ({doc_id})")
        markdown_content = self.fetch_text(markdown_url)
        if markdown_content is None:
            return False, True, None

        with open(markdown_path, "w", encoding="utf-8") as file_obj:
            file_obj.write(markdown_content)

        return True, True, markdown_path

    def read_markdown(self, path: Path) -> str:
        """读取 Markdown 文本"""
        with open(path, "r", encoding="utf-8") as file_obj:
            return file_obj.read()

    def build_diff(self, old_path: Optional[Path], new_path: Optional[Path]) -> Optional[str]:
        """生成 unified diff 文本"""
        if not old_path or not new_path or not old_path.exists() or not new_path.exists():
            return None

        old_lines = self.read_markdown(old_path).splitlines()
        new_lines = self.read_markdown(new_path).splitlines()
        diff_lines = list(
            difflib.unified_diff(
                old_lines,
                new_lines,
                fromfile=old_path.name,
                tofile=new_path.name,
                lineterm="",
                n=3,
            )
        )
        if not diff_lines:
            return "无正文差异，可能仅更新时间发生变化。"

        if len(diff_lines) > self.diff_preview_lines:
            remaining = len(diff_lines) - self.diff_preview_lines
            diff_lines = diff_lines[: self.diff_preview_lines]
            diff_lines.append(f"... 已截断其余 {remaining} 行 diff")

        return "\n".join(diff_lines)

    def create_latest_report_link(self, report_file: Path):
        """创建或覆盖最新报告链接"""
        latest_file = self.reports_dir / "latest.md"
        if latest_file.exists() or latest_file.is_symlink():
            latest_file.unlink()

        try:
            os.symlink(report_file.name, latest_file)
        except OSError:
            with open(report_file, "r", encoding="utf-8") as source_obj:
                content = source_obj.read()
            with open(latest_file, "w", encoding="utf-8") as latest_obj:
                latest_obj.write(content)

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
    ) -> str:
        """生成 Markdown 差异报告"""
        report_lines = [
            f"# 微信支付文档更新报告 - {self.doc_config['name']}",
            "",
            f"**文档类型**: {self.doc_config['name']} ({self.doc_type})",
            f"**生成时间**: {run_time}",
            f"**文档总数**: {total_nodes}",
            "",
            "## 变更概览",
            "",
            f"- 新增: {len(added)} 个页面",
            f"- 删除: {len(removed)} 个页面",
            f"- 修改: {len(modified)} 个页面",
            f"- 成功拉取: {len(fetch_success)} 个页面",
            f"- 拉取失败: {len(fetch_failed)} 个页面",
            "",
        ]

        if added:
            report_lines.extend(["## 新增页面", ""])
            for node in added:
                markdown_path = self.get_markdown_path(node["docId"], str(node["updateTime"]))
                report_lines.extend(
                    [
                        f"### {node['title']}",
                        f"- ID: `{node['docId']}`",
                        f"- 路径: {node['fullPath']}",
                        f"- URL: {self.build_markdown_url(node)}",
                        f"- 更新时间: {self.format_timestamp(str(node['updateTime']))}",
                        f"- 本地文件: `{markdown_path}`",
                        "",
                    ]
                )

        if removed:
            report_lines.extend(["## 删除页面", ""])
            for node in removed:
                report_lines.extend(
                    [
                        f"- **{node['title']}** (`{node['docId']}`)",
                        f"  - 原路径: {node.get('fullPath', '')}",
                        f"  - 原更新时间: {self.format_timestamp(str(node.get('updateTime', '')))}",
                        "",
                    ]
                )

        if modified:
            report_lines.extend(["## 修改页面", ""])
            for node in modified:
                new_markdown_path = self.get_markdown_path(node["docId"], node["newUpdateTime"])
                report_lines.extend(
                    [
                        f"### {node['title']}",
                        f"- ID: `{node['docId']}`",
                        f"- 路径: {node['fullPath']}",
                        f"- URL: {self.build_markdown_url(node)}",
                        f"- 更新时间变更: {self.format_timestamp(node['oldUpdateTime'])} -> {self.format_timestamp(node['newUpdateTime'])}",
                        f"- 新版本文件: `{new_markdown_path}`",
                        "",
                        "```diff",
                        diff_details.get(node["docId"]) or "无法生成 diff：缺少本地旧版本或新版本文件。",
                        "```",
                        "",
                    ]
                )

        if fetch_failed:
            report_lines.extend(["## 拉取失败", ""])
            failed_lookup = {node["docId"]: node for node in added}
            failed_lookup.update({node["docId"]: node for node in modified})
            for doc_id in fetch_failed:
                node = failed_lookup.get(doc_id)
                if not node:
                    continue
                report_lines.extend(
                    [
                        f"- {node['title']} (`{doc_id}`): {self.build_markdown_url(node)}",
                        "",
                    ]
                )

        report_lines.extend(
            [
                "## 附录：所有页面清单",
                "",
                f"<details>",
                f"<summary>点击查看全部 {total_nodes} 个页面</summary>",
                "",
                "| 序号 | 标题（链接） | ID | 更新时间 | 完整路径 |",
                "|------|-------------|----|----------|----------|",
            ]
        )

        for index, node in enumerate(all_nodes, start=1):
            markdown_rel_path = f"../pages/{node['docId']}/{node['docId']}_{node['updateTime']}.md"
            report_lines.append(
                f"| {index} | [{node['title']}]({markdown_rel_path}) | `{node['docId']}` | {self.format_timestamp(str(node['updateTime']))} | {node['fullPath']} |"
            )

        report_lines.extend(["", "</details>"])
        return "\n".join(report_lines)

    def run(self, limit: Optional[int] = None):
        """运行抓取流程"""
        run_time = datetime.now().strftime("%Y%m%d_%H%M%S")

        print(f"[{run_time}] 开始抓取微信支付文档 - {self.doc_config['name']}")
        print(f"  首页: {self.index_url}")

        print("\n[1/5] 获取首页数据...")
        html = self.fetch_text(self.index_url)
        if not html:
            print("  错误: 无法获取首页")
            return

        print("\n[2/5] 解析 JSON 数据包...")
        json_data = self.extract_json_data(html)
        if not json_data:
            print("  错误: 无法解析 JSON 数据")
            return

        print("\n[3/5] 提取叶子节点...")
        leaf_nodes = self.extract_leaf_nodes(json_data)
        print(f"  共找到 {len(leaf_nodes)} 个叶子节点")

        if limit and limit > 0:
            leaf_nodes = leaf_nodes[:limit]
            print(f"  测试模式：仅处理前 {limit} 个节点")

        print("\n[4/5] 检测变更...")
        old_index = self.load_index()
        is_first_run = not old_index

        if is_first_run:
            print("  首次运行：将抓取所有页面")
            added = leaf_nodes
            removed = []
            modified = []
        else:
            added, removed, modified = self.detect_changes(leaf_nodes, old_index)
            print(f"  新增: {len(added)} 个")
            print(f"  删除: {len(removed)} 个")
            print(f"  修改: {len(modified)} 个")

        print("\n[5/5] 拉取变更页面...")
        nodes_to_fetch = list(added)
        modified_node_ids = {node["docId"] for node in modified}
        nodes_to_fetch.extend(node for node in leaf_nodes if node["docId"] in modified_node_ids)

        fetch_success: List[str] = []
        fetch_failed: List[str] = []
        fetched_paths: Dict[str, Path] = {}

        for index, node in enumerate(nodes_to_fetch, start=1):
            print(f"  [{index}/{len(nodes_to_fetch)}] ", end="")
            success, was_fetched, markdown_path = self.save_markdown(node)
            if success:
                fetch_success.append(node["docId"])
                if markdown_path:
                    fetched_paths[node["docId"]] = markdown_path
            else:
                fetch_failed.append(node["docId"])

            if was_fetched and index < len(nodes_to_fetch):
                time.sleep(0.5)

        print(f"\n  成功: {len(fetch_success)} 个")
        print(f"  失败: {len(fetch_failed)} 个")

        has_changes = bool(added or removed or modified)
        if not is_first_run and not has_changes:
            print("\n✅ 完成! 无变更，跳过保存索引和报告")
            return

        self.save_index(leaf_nodes, run_time)

        diff_details: Dict[str, Optional[str]] = {}
        for node in modified:
            old_markdown_path = self.get_previous_markdown_path(node["docId"], node["newUpdateTime"])
            new_markdown_path = fetched_paths.get(node["docId"]) or self.get_markdown_path(
                node["docId"], node["newUpdateTime"]
            )
            diff_details[node["docId"]] = self.build_diff(old_markdown_path, new_markdown_path)

        print("\n[6/6] 生成差异报告...")
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
        )

        report_file = self.reports_dir / f"report_{run_time}.md"
        with open(report_file, "w", encoding="utf-8") as file_obj:
            file_obj.write(report_content)

        self.create_latest_report_link(report_file)

        timestamped_index = self.index_dir / f"index_{run_time}.json"
        print("\n✅ 完成!")
        print(f"   索引文件: {timestamped_index}")
        print(f"   最新索引: {self.index_file}")
        print(f"   Markdown 目录: {self.pages_dir}")
        print(f"   报告文件: {report_file}")
        print(f"   最新报告: {self.reports_dir / 'latest.md'}")


def main():
    """主函数"""
    import argparse

    parser = argparse.ArgumentParser(
        description="微信支付文档抓取工具 - 支持直连商户和合作伙伴文档",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 抓取直连商户文档（默认）
  python3 wechatpay_doc_fetcher.py

  # 抓取合作伙伴文档
  python3 wechatpay_doc_fetcher.py --type partner

  # 测试模式（仅前10个页面）
  python3 wechatpay_doc_fetcher.py --type merchant --limit 10

  # 指定输出目录
  python3 wechatpay_doc_fetcher.py --type partner --output ./my_docs
        """,
    )

    parser.add_argument(
        "--type",
        "-t",
        type=str,
        default="merchant",
        choices=["merchant", "partner"],
        help="文档类型：merchant(直连商户) 或 partner(合作伙伴)，默认: merchant",
    )
    parser.add_argument(
        "--limit",
        "-l",
        type=int,
        default=None,
        help="限制处理的页面数量（用于测试）",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        default="docs",
        help="输出目录（默认: docs）",
    )

    args = parser.parse_args()

    fetcher = WechatPayDocFetcher(doc_type=args.type, base_dir=args.output)
    fetcher.run(limit=args.limit)


if __name__ == "__main__":
    main()

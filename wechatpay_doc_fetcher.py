#!/usr/bin/env python3
"""
微信支付文档抓取工具
- 支持直连商户(merchant)和合作伙伴(partner)两种文档类型
- 解析首页JSON数据包
- 提取所有叶子节点
- 支持增量更新检测
- 生成Markdown差异报告
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
import urllib.request
import urllib.error
import time


class WechatPayDocFetcher:
    """微信支付文档抓取器"""
    
    # 文档类型配置
    DOC_TYPES = {
        'merchant': {
            'name': '直连商户',
            'index_url': 'https://pay.weixin.qq.com/doc/v3/merchant/4012062524',
            'subdir': 'merchant'
        },
        'partner': {
            'name': '合作伙伴',
            'index_url': 'https://pay.weixin.qq.com/doc/v3/partner/4012069852',
            'subdir': 'partner'
        }
    }
    
    def __init__(self, doc_type: str = 'merchant', base_dir: str = "docs"):
        """
        初始化抓取器
        
        Args:
            doc_type: 文档类型，'merchant' 或 'partner'
            base_dir: 基础输出目录
        """
        if doc_type not in self.DOC_TYPES:
            raise ValueError(f"不支持的文档类型: {doc_type}，支持: {list(self.DOC_TYPES.keys())}")
        
        self.doc_type = doc_type
        self.doc_config = self.DOC_TYPES[doc_type]
        self.base_dir = Path(base_dir) / self.doc_config['subdir']
        self.base_url = "https://pay.weixin.qq.com"
        self.index_url = self.doc_config['index_url']
        
        # 创建目录结构
        self.index_dir = self.base_dir / "index"
        self.pages_dir = self.base_dir / "pages"
        self.reports_dir = self.base_dir / "reports"
        
        self.index_dir.mkdir(parents=True, exist_ok=True)
        self.pages_dir.mkdir(parents=True, exist_ok=True)
        self.reports_dir.mkdir(parents=True, exist_ok=True)
        
        # 索引文件路径
        self.index_file = self.index_dir / "latest.json"
    
    def fetch_page(self, url: str, max_retries: int = 3) -> Optional[str]:
        """获取页面HTML内容"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        for attempt in range(max_retries):
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=30) as response:
                    return response.read().decode('utf-8')
            except Exception as e:
                print(f"  尝试 {attempt + 1}/{max_retries} 失败: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # 指数退避
                else:
                    return None
        return None
    
    def extract_json_data(self, html: str) -> Optional[Dict]:
        """从HTML中提取JSON数据包"""
        # 查找 vike_pageContext script 标签
        pattern = r'<script id="vike_pageContext" type="application/json">(.*?)</script>'
        match = re.search(pattern, html, re.DOTALL)
        
        if not match:
            print("  错误: 未找到 vike_pageContext 数据包")
            return None
        
        try:
            json_str = match.group(1)
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"  错误: JSON解析失败: {e}")
            return None
    
    def extract_leaf_nodes(self, data: Dict) -> List[Dict]:
        """递归提取所有叶子节点"""
        leaf_nodes = []
        
        def traverse(node: Dict, path: List[str] = None):
            if path is None:
                path = []
            
            # 获取当前节点信息
            doc_id = node.get('docId', '')
            title = node.get('title', '')
            update_time = node.get('updateTime', '')
            url = node.get('url', '')
            children = node.get('childrenList', [])
            
            current_path = path + [title]
            
            # 如果是叶子节点（无子节点）
            if not children:
                leaf_nodes.append({
                    'docId': doc_id,
                    'title': title,
                    'updateTime': update_time,
                    'url': url,
                    'fullPath': ' > '.join(current_path),
                    'pathArray': [p['title'] for p in node.get('pathArray', [])]
                })
            else:
                # 递归遍历子节点
                for child in children:
                    traverse(child, current_path)
        
        # 从 menuData 开始遍历
        menu_data = data.get('data', {}).get('menuData', [])
        for root_node in menu_data:
            traverse(root_node)
        
        return leaf_nodes
    
    def load_index(self) -> Dict[str, Dict]:
        """加载索引文件"""
        if not self.index_file.exists():
            return {}

        try:
            with open(self.index_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # 转换为以 docId 为键的字典
                return {node['docId']: node for node in data.get('nodes', [])}
        except Exception as e:
            print(f"  警告: 加载索引失败: {e}")
            return {}

    def _has_reports(self) -> bool:
        """检查reports目录是否存在报告文件"""
        if not self.reports_dir.exists():
            return False
        # 检查是否存在.md文件
        return any(self.reports_dir.glob("*.md"))
    
    def save_index(self, nodes: List[Dict], run_time: str):
        """保存索引文件（带时间戳版本 + latest.json）"""
        index_data = {
            'runTime': run_time,
            'totalNodes': len(nodes),
            'docType': self.doc_type,
            'docTypeName': self.doc_config['name'],
            'nodes': nodes
        }

        # 保存带时间戳的版本
        timestamped_file = self.index_dir / f"index_{run_time}.json"
        with open(timestamped_file, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, ensure_ascii=False, indent=2)

        # 保存/覆盖 latest.json
        with open(self.index_file, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, ensure_ascii=False, indent=2)
    
    def detect_changes(self, new_nodes: List[Dict], old_index: Dict[str, Dict]) -> Tuple[List[Dict], List[Dict], List[Dict]]:
        """
        检测变更
        返回: (新增节点, 删除节点, 修改节点)
        """
        new_dict = {node['docId']: node for node in new_nodes}
        
        # 新增节点：在新数据中存在，但在旧索引中不存在
        added = []
        for doc_id, node in new_dict.items():
            if doc_id not in old_index:
                added.append(node)
        
        # 删除节点：在旧索引中存在，但在新数据中不存在
        removed = []
        for doc_id, node in old_index.items():
            if doc_id not in new_dict:
                removed.append(node)
        
        # 修改节点：docId相同但updateTime不同
        modified = []
        for doc_id, new_node in new_dict.items():
            if doc_id in old_index:
                old_node = old_index[doc_id]
                if new_node['updateTime'] != old_node.get('updateTime', ''):
                    modified.append({
                        'docId': doc_id,
                        'title': new_node['title'],
                        'url': new_node['url'],
                        'oldUpdateTime': old_node.get('updateTime', ''),
                        'newUpdateTime': new_node['updateTime'],
                        'fullPath': new_node['fullPath']
                    })
        
        return added, removed, modified
    
    @staticmethod
    def clean_html(html: str) -> str:
        """移除 HTML 中的 JSON 数据包以减小文件大小"""
        # 匹配 vike_pageContext 脚本标签（使用非贪婪匹配）
        pattern = r'<script id="vike_pageContext" type="application/json">.*?</script>'
        return re.sub(pattern, '', html, flags=re.DOTALL)

    def save_page(self, node: Dict) -> Tuple[bool, bool]:
        """
        保存页面内容到本地（如果已存在则跳过）

        Returns:
            Tuple[bool, bool]: (是否成功, 是否实际执行了网络请求)
        """
        doc_id = node['docId']
        update_time = node['updateTime']
        url = self.base_url + node['url'] if not node['url'].startswith('http') else node['url']

        # 创建页面目录（按docId分类）
        page_dir = self.pages_dir / doc_id
        page_dir.mkdir(exist_ok=True)

        # 使用 docId_updateTime 命名文件
        html_filename = f"{doc_id}_{update_time}.html"
        json_filename = f"{doc_id}_{update_time}.json"
        html_path = page_dir / html_filename
        json_path = page_dir / json_filename

        # 检查文件是否已存在（HTML和JSON都存在才跳过）
        if html_path.exists() and json_path.exists():
            print(f"  跳过: {node['title']} ({doc_id}) - 已存在")
            return True, False  # 成功，但未执行网络请求

        print(f"  拉取: {node['title']} ({doc_id})")

        html = self.fetch_page(url)
        if html is None:
            return False, True  # 失败，但执行了网络请求

        # 清理 JSON 数据包以减小文件大小
        html = self.clean_html(html)

        # 保存页面内容
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)

        # 保存元数据
        fetch_time = datetime.now().strftime('%Y%m%d_%H%M%S')
        meta_data = {
            'docId': doc_id,
            'title': node['title'],
            'url': url,
            'fetchTime': fetch_time,
            'updateTime': update_time,
            'fullPath': node['fullPath']
        }
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(meta_data, f, ensure_ascii=False, indent=2)

        return True, True  # 成功，且执行了网络请求
    
    def generate_report(self, run_time: str, total_nodes: int, 
                       added: List[Dict], removed: List[Dict], modified: List[Dict],
                       fetch_success: List[str], fetch_failed: List[str]) -> str:
        """生成Markdown格式的差异报告"""
        
        report_lines = [
            f"# 微信支付文档更新报告 - {self.doc_config['name']}",
            "",
            f"**文档类型**: {self.doc_config['name']} ({self.doc_type})",
            f"**生成时间**: {run_time}",
            f"**文档总数**: {total_nodes}",
            "",
            "## 变更概览",
            "",
            f"- ✅ **新增**: {len(added)} 个页面",
            f"- ❌ **删除**: {len(removed)} 个页面",
            f"- 📝 **修改**: {len(modified)} 个页面",
            f"- 📥 **成功拉取**: {len(fetch_success)} 个页面",
            f"- ❗ **拉取失败**: {len(fetch_failed)} 个页面",
            "",
            "---",
            "",
        ]
        
        # 新增节点
        if added:
            report_lines.extend([
                "## 新增页面",
                "",
            ])
            for node in added:
                report_lines.append(f"### {node['title']}")
                report_lines.append(f"- **ID**: `{node['docId']}`")
                report_lines.append(f"- **路径**: {node['fullPath']}")
                report_lines.append(f"- **URL**: https://pay.weixin.qq.com{node['url']}")
                report_lines.append(f"- **更新时间**: {self.format_timestamp(node['updateTime'])}")
                report_lines.append("")
        
        # 删除节点
        if removed:
            report_lines.extend([
                "## 删除页面",
                "",
            ])
            for node in removed:
                report_lines.append(f"- **{node['title']}** (`{node['docId']}`)")
                report_lines.append(f"  - 原路径: {node['fullPath']}")
                report_lines.append("")
        
        # 修改节点
        if modified:
            report_lines.extend([
                "## 修改页面",
                "",
            ])
            for node in modified:
                report_lines.append(f"### {node['title']}")
                report_lines.append(f"- **ID**: `{node['docId']}`")
                report_lines.append(f"- **路径**: {node['fullPath']}")
                report_lines.append(f"- **URL**: https://pay.weixin.qq.com{node['url']}")
                report_lines.append(f"- **更新时间变更**: {self.format_timestamp(node['oldUpdateTime'])} → {self.format_timestamp(node['newUpdateTime'])}")
                # 添加查看链接
                page_dir = self.pages_dir / node['docId']
                if page_dir.exists():
                    filename = f"{node['docId']}_{node['newUpdateTime']}.html"
                    report_lines.append(f"- **本地文件**: `{page_dir}/{filename}`")
                report_lines.append("")
        
        # 拉取失败
        if fetch_failed:
            report_lines.extend([
                "## 拉取失败的页面",
                "",
                "| 标题 | ID | URL |",
                "|------|-----|-----|",
            ])
            for doc_id in fetch_failed:
                # 从modified中找到对应的节点
                node = None
                for m in modified:
                    if m['docId'] == doc_id:
                        node = m
                        break
                if not node:
                    for a in added:
                        if a['docId'] == doc_id:
                            node = a
                            break
                if node:
                    report_lines.append(f"| {node['title']} | `{doc_id}` | https://pay.weixin.qq.com{node['url']} |")
            report_lines.append("")
        
        # 完整页面列表
        report_lines.extend([
            "---",
            "",
            "## 附录：所有页面清单",
            "",
            "<details>",
            "<summary>点击查看全部 {total_nodes} 个页面</summary>",
            "",
            "| 序号 | 标题（链接） | ID | 更新时间 | 完整路径 |",
            "|------|-------------|-----|----------|----------|",
        ])
        
        return '\n'.join(report_lines)
    
    def format_timestamp(self, ts: str) -> str:
        """格式化Unix时间戳"""
        try:
            dt = datetime.fromtimestamp(int(ts))
            return dt.strftime('%Y-%m-%d %H:%M:%S')
        except:
            return ts
    
    def run(self, limit: Optional[int] = None):
        """
        运行抓取流程
        
        Args:
            limit: 限制处理的页面数量（用于测试）
        """
        run_time = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        print(f"[{run_time}] 开始抓取微信支付文档 - {self.doc_config['name']}")
        print(f"  首页: {self.index_url}")
        
        # 1. 获取首页HTML
        print("\n[1/5] 获取首页数据...")
        html = self.fetch_page(self.index_url)
        if not html:
            print("  错误: 无法获取首页")
            return
        
        # 2. 提取JSON数据
        print("\n[2/5] 解析JSON数据包...")
        json_data = self.extract_json_data(html)
        if not json_data:
            print("  错误: 无法解析JSON数据")
            return
        
        # 3. 提取叶子节点
        print("\n[3/5] 提取叶子节点...")
        leaf_nodes = self.extract_leaf_nodes(json_data)
        print(f"  共找到 {len(leaf_nodes)} 个叶子节点")
        
        # 应用限制（用于测试）
        if limit and limit > 0:
            leaf_nodes = leaf_nodes[:limit]
            print(f"  测试模式：仅处理前 {limit} 个节点")
        
        # 4. 加载旧索引并检测变更
        print("\n[4/5] 检测变更...")
        old_index = self.load_index()

        # 检查是否首次运行：无索引文件 或 reports目录为空
        is_first_run = not old_index or not self._has_reports()

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
        
        # 5. 拉取变更的页面
        print("\n[5/5] 拉取变更页面...")
        
        # 需要拉取的节点：新增 + 修改
        nodes_to_fetch = added.copy()
        for m in modified:
            # 从 leaf_nodes 中找到完整的节点信息
            for node in leaf_nodes:
                if node['docId'] == m['docId']:
                    nodes_to_fetch.append(node)
                    break
        
        fetch_success = []
        fetch_failed = []

        for i, node in enumerate(nodes_to_fetch, 1):
            print(f"  [{i}/{len(nodes_to_fetch)}] ", end='')
            success, was_fetched = self.save_page(node)
            if success:
                fetch_success.append(node['docId'])
            else:
                fetch_failed.append(node['docId'])
            # 只有实际执行了网络请求才添加延迟
            if was_fetched and i < len(nodes_to_fetch):
                time.sleep(0.5)
        
        print(f"\n  成功: {len(fetch_success)} 个")
        print(f"  失败: {len(fetch_failed)} 个")
        
        # 6. 保存新索引
        self.save_index(leaf_nodes, run_time)
        
        # 7. 生成报告
        print("\n[6/6] 生成差异报告...")
        report_content = self.generate_report(
            run_time, len(leaf_nodes),
            added, removed, modified,
            fetch_success, fetch_failed
        )
        
        # 添加完整清单到报告
        lines = report_content.split('\n')
        for i, line in enumerate(lines):
            if '{total_nodes}' in line:
                lines[i] = line.replace('{total_nodes}', str(len(leaf_nodes)))
        report_content = '\n'.join(lines)
        
        # 添加页面清单表格（包含完整路径和HTML文件链接）
        table_lines = []
        for idx, node in enumerate(leaf_nodes, 1):
            doc_id = node['docId']
            update_time = node['updateTime']
            # 构建HTML文件的相对路径
            html_rel_path = f"../pages/{doc_id}/{doc_id}_{update_time}.html"
            # 使用完整层级路径
            full_path = node['fullPath']
            table_lines.append(f"| {idx} | [{node['title']}]({html_rel_path}) | `{doc_id}` | {self.format_timestamp(update_time)} | {full_path} |")
        
        report_content += '\n' + '\n'.join(table_lines)
        report_content += "\n\n</details>\n"
        
        # 保存报告
        report_file = self.reports_dir / f"report_{run_time}.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_content)

        # 显示带时间戳的索引文件路径
        timestamped_index = self.index_dir / f"index_{run_time}.json"
        print(f"\n✅ 完成!")
        print(f"   索引文件: {timestamped_index}")
        print(f"   最新索引: {self.index_file}")
        print(f"   页面目录: {self.pages_dir}")
        print(f"   报告文件: {report_file}")


def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='微信支付文档抓取工具 - 支持直连商户和合作伙伴文档',
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
        """
    )
    
    parser.add_argument('--type', '-t', type=str, default='merchant',
                       choices=['merchant', 'partner'],
                       help='文档类型：merchant(直连商户) 或 partner(合作伙伴)，默认: merchant')
    parser.add_argument('--limit', '-l', type=int, default=None,
                       help='限制处理的页面数量（用于测试）')
    parser.add_argument('--output', '-o', type=str, default='docs',
                       help='输出目录（默认: docs）')
    
    args = parser.parse_args()
    
    fetcher = WechatPayDocFetcher(doc_type=args.type, base_dir=args.output)
    fetcher.run(limit=args.limit)


if __name__ == '__main__':
    main()

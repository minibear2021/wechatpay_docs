# 微信支付文档抓取工具

一个自动化抓取微信支付开发文档的工具，支持**直连商户**和**合作伙伴**两种文档类型，支持增量更新检测和 Markdown 报告生成。

## 支持的文档类型

| 类型 | 说明 | 入口地址 | 文档数量 |
|-----|------|---------|---------|
| `merchant` | 直连商户 | https://pay.weixin.qq.com/doc/v3/merchant/4012062524 | ~528 个页面 |
| `partner` | 合作伙伴 | https://pay.weixin.qq.com/doc/v3/partner/4012069852 | ~897 个页面 |

## 功能特性

- 📦 **解析 JSON 数据包**: 从微信支付文档首页提取嵌入的文档结构数据
- 🌲 **递归提取叶子节点**: 自动遍历文档树，识别所有实际文档页面
- 📝 **增量更新检测**: 通过对比 `updateTime` 识别新增、删除、修改的页面
- 📥 **智能去重**: 根据 `updateTime` 命名文件，已存在则跳过，避免重复抓取
- 📊 **Markdown 报告**: 生成包含差异对比的详细更新报告
- 📁 **类型隔离**: 不同文档类型分开存储，互不干扰

## 目录结构

```
wechatpay_docs/
├── merchant/                      # 直连商户文档
│   ├── index/
│   │   ├── leaf_nodes_index.json      # 当前索引
│   │   └── leaf_nodes_index_prev.json # 上一次索引
│   ├── pages/
│   │   └── {docId}/                   # 每个页面的独立目录
│   │       ├── {docId}_{updateTime}.html  # 页面内容（以updateTime命名）
│   │       └── {docId}_{updateTime}.json  # 元数据
│   └── reports/
│       ├── report_{timestamp}.md      # 每次运行的报告
│       └── latest.md                  # 软链接，指向最新报告
│
└── partner/                       # 合作伙伴文档
    ├── index/
    ├── pages/
    └── reports/
        └── ...
```

**文件命名规则**: `{docId}_{updateTime}.{ext}`

- 抓取前检查文件是否存在，存在则跳过
- 根据 `updateTime` 命名，可直观看到文档版本

## 使用方法

### 命令行参数

```bash
python3 wechatpay_doc_fetcher.py [选项]

选项:
  -t, --type {merchant,partner}  文档类型（默认: merchant）
  -l, --limit LIMIT              限制处理的页面数量（用于测试）
  -o, --output OUTPUT            输出目录（默认: wechatpay_docs）
  -h, --help                     显示帮助信息
```

### 示例

```bash
# 抓取直连商户文档（默认）
python3 wechatpay_doc_fetcher.py

# 抓取合作伙伴文档
python3 wechatpay_doc_fetcher.py --type partner

# 测试模式（仅前10个页面）
python3 wechatpay_doc_fetcher.py --type merchant --limit 10

# 指定输出目录
python3 wechatpay_doc_fetcher.py --type partner --output ./my_docs

# 抓取全部合作伙伴文档
python3 wechatpay_doc_fetcher.py --type partner
```

## 工作流程

1. **首次运行**: 抓取所有叶子节点页面，建立索引
2. **后续运行**: 检测变更（新增/删除/修改），仅拉取有变化的页面
3. **生成报告**: 输出 Markdown 格式的差异报告，包含文档类型标识

## 增量更新机制

工具通过对比 JSON 数据包中的 `updateTime` 字段检测变更：

| 变更类型 | 检测条件 | 处理方式 |
|---------|---------|---------|
| **新增** | docId 在新数据中存在，但在旧索引中不存在 | 拉取并保存页面 |
| **删除** | docId 在旧索引中存在，但在新数据中不存在 | 记录在报告中 |
| **修改** | docId 相同但 updateTime 不同 | 拉取新版并保存 |

## 报告内容

生成的 Markdown 报告包含：

- 文档类型标识（直连商户/合作伙伴）
- 变更概览统计
- 新增页面列表（含完整路径和URL）
- 删除页面列表
- 修改页面列表（含更新时间对比）
- 拉取失败记录
- 完整页面清单（可折叠）

## 字段说明

### 索引节点字段

| 字段名 | 说明 |
|-------|------|
| docId | 文档唯一标识 |
| title | 文档标题 |
| updateTime | Unix 时间戳，用于变更检测 |
| url | 相对路径，完整 URL 为 `https://pay.weixin.qq.com{url}` |
| fullPath | 完整层级路径 |
| pathArray | 路径数组 |

### 元数据文件字段

```json
{
  "docId": "4012062524",
  "title": "产品介绍",
  "url": "https://pay.weixin.qq.com/doc/v3/merchant/4012062524",
  "fetchTime": "20260402_113449",
  "updateTime": "1752549187",
  "fullPath": "产品文档 > 支付产品 > JSAPI支付 > 产品介绍"
}
```

## 示例输出

### 运行日志

```
[20260402_113449] 开始抓取微信支付文档 - 直连商户
  首页: https://pay.weixin.qq.com/doc/v3/merchant/4012062524

[1/5] 获取首页数据...

[2/5] 解析JSON数据包...

[3/5] 提取叶子节点...
  共找到 528 个叶子节点
  测试模式：仅处理前 3 个节点

[4/5] 检测变更...
  首次运行：将抓取所有页面

[5/5] 拉取变更页面...
  [1/3]   拉取: 产品介绍 (4012062524)
  [2/3]   拉取: 快速开始 (4015423216)
  [3/3]   拉取: 开发指引 (4012791870)
  成功: 3 个
  失败: 0 个

[6/6] 生成差异报告...

✅ 完成!
   索引文件: wechatpay_docs/merchant/index/leaf_nodes_index.json
   页面目录: wechatpay_docs/merchant/pages
   报告文件: wechatpay_docs/merchant/reports/report_20260402_113449.md
   最新报告: wechatpay_docs/merchant/reports/latest.md
```

## 依赖

- Python 3.6+
- 标准库：urllib, json, re, os, sys, datetime, pathlib, typing, time

## 注意事项

1. **请求频率**: 工具内置 0.5 秒延迟避免请求过快
2. **重试机制**: 失败请求会自动重试 3 次，使用指数退避
3. **时间戳格式**: `YYYYMMDD_HHMMSS`
4. **编码**: 所有文件使用 UTF-8 编码
5. **目录隔离**: 两种文档类型完全隔离，可以独立运行和更新

## 扩展建议

- 可添加代理支持以应对网络限制
- 可添加定时任务（cron）实现自动监控
- 可集成通知系统（邮件/钉钉/飞书）推送变更
- 可同时抓取两种类型：`python3 wechatpay_doc_fetcher.py --type merchant && python3 wechatpay_doc_fetcher.py --type partner`

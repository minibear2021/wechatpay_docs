# 微信支付文档抓取工具

一个基于官方 Markdown 输出的微信支付文档抓取工具，支持直连商户和合作伙伴两种文档类型，支持增量更新检测，并在报告中直接输出变更页的 diff。

## 支持的文档类型

| 类型 | 说明 | 入口地址 | 文档数量 |
|-----|------|---------|---------|
| `merchant` | 直连商户 | https://pay.weixin.qq.com/doc/v3/merchant/4012062524 | ~528 个页面 |
| `partner` | 合作伙伴 | https://pay.weixin.qq.com/doc/v3/partner/4012069852 | ~897 个页面 |

## 核心变化

- 首页索引从 HTML 中提取 `vike_pageContext` JSON。
- 具体文档直接访问官方 `.md` 地址，例如 `https://pay.weixin.qq.com/doc/v3/merchant/4012062524.md`。
- 本地页面仅保存 Markdown 版本文件：`{docId}_{updateTime}.md`。
- 对于修改页面，报告直接写入旧版和新版 Markdown 的 unified diff。

## 功能特性

- 解析微信支付首页中的 JSON 文档树。
- 递归提取所有叶子节点。
- 通过 `updateTime` 检测新增、删除、修改。
- 只在本地不存在对应版本 Markdown 时才落盘。
- 自动为修改页生成 diff 并写入报告。
- 为每次运行保存时间戳索引和报告，同时维护 `latest.md`。

## 目录结构

```text
wechatpay_docs/
├── docs/
│   ├── merchant/
│   │   ├── index/
│   │   │   ├── index_YYYYMMDD_HHMMSS.json
│   │   │   └── latest.json
│   │   ├── pages/
│   │   │   └── {docId}/
│   │   │       └── {docId}_{updateTime}.md
│   │   └── reports/
│   │       ├── report_YYYYMMDD_HHMMSS.md
│   │       └── latest.md
│   └── partner/
│       ├── index/
│       ├── pages/
│       └── reports/
├── README.md
└── wechatpay_doc_fetcher.py
```

## 使用方法

```bash
python3 wechatpay_doc_fetcher.py [选项]
```

### 参数

```bash
-t, --type {merchant,partner}  文档类型，默认 merchant
-l, --limit LIMIT              限制处理的页面数量，用于测试
-o, --output OUTPUT            输出目录，默认 docs
-h, --help                     显示帮助信息
```

### 示例

```bash
# 抓取直连商户文档
python3 wechatpay_doc_fetcher.py

# 抓取合作伙伴文档
python3 wechatpay_doc_fetcher.py --type partner

# 测试模式，仅处理前 10 个页面
python3 wechatpay_doc_fetcher.py --type merchant --limit 10

# 自定义输出目录
python3 wechatpay_doc_fetcher.py --type partner --output ./my_docs
```

## 工作流程

1. 获取入口页 HTML。
2. 提取 `vike_pageContext` JSON 并解析文档树。
3. 提取所有叶子节点。
4. 对比本地 `latest.json`，识别新增、删除、修改。
5. 对新增和修改页面直接抓取官方 `.md` 文本。
6. 对修改页使用 unified diff 比较本地上一版和新版本 Markdown。
7. 写入时间戳索引、更新报告，并维护最新报告链接。

## 增量更新规则

| 变更类型 | 检测条件 | 处理方式 |
|---------|---------|---------|
| 新增 | `docId` 在新索引中存在，但在旧索引中不存在 | 拉取 Markdown 并落盘 |
| 删除 | `docId` 在旧索引中存在，但在新索引中不存在 | 记录到报告 |
| 修改 | `docId` 相同但 `updateTime` 不同 | 拉取新版本 Markdown，生成 diff |

## 报告内容

报告包含以下内容：

- 变更概览统计。
- 新增页面信息。
- 删除页面信息。
- 修改页面的更新时间变化和 unified diff。
- 拉取失败页面清单。
- 全量页面清单和本地 Markdown 链接。

## 索引字段说明

| 字段名 | 说明 |
|-------|------|
| `docId` | 文档唯一标识 |
| `title` | 文档标题 |
| `updateTime` | Unix 时间戳，用于检测版本变化 |
| `url` | 相对路径，完整 URL 为 `https://pay.weixin.qq.com{url}` |
| `fullPath` | 页面完整层级路径 |
| `pathArray` | 路径数组 |

## 示例输出

```text
[20260412_101530] 开始抓取微信支付文档 - 直连商户
  首页: https://pay.weixin.qq.com/doc/v3/merchant/4012062524

[1/5] 获取首页数据...

[2/5] 解析 JSON 数据包...

[3/5] 提取叶子节点...
  共找到 528 个叶子节点
  测试模式：仅处理前 10 个节点

[4/5] 检测变更...
  新增: 0 个
  删除: 0 个
  修改: 2 个

[5/5] 拉取变更页面...
  [1/2]   拉取: 产品介绍 (4012062524)
  [2/2]   拉取: 开发指引 (4012791870)
  成功: 2 个
  失败: 0 个

[6/6] 生成差异报告...

✅ 完成!
   索引文件: docs/merchant/index/index_20260412_101530.json
   最新索引: docs/merchant/index/latest.json
   Markdown 目录: docs/merchant/pages
   报告文件: docs/merchant/reports/report_20260412_101530.md
   最新报告: docs/merchant/reports/latest.md
```

## 依赖

- Python 3.6+
- 标准库：`difflib`、`json`、`os`、`re`、`time`、`urllib`、`datetime`、`pathlib`、`typing`

## 注意事项

1. 工具内置 0.5 秒请求间隔，避免请求过快。
2. 请求失败会自动重试 3 次，并使用指数退避。
3. 若某个修改页本地不存在旧版 Markdown，报告会提示无法生成 diff。
4. 现有历史 `.html` 文件不会被自动删除，但后续新版本只会保存 `.md` 文件。

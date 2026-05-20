# 微信支付文档抓取工具

从微信支付官方 `llms.txt` 获取 Markdown 文档列表，结合 HTML 页面的 `updateTime` 变更信息，直接下载官方 `.md` 格式文档。支持直连商户和合作伙伴两种文档类型、增量更新检测和 diff 报告。

## 支持的文档类型

| 类型 | 说明 | llms.txt | 首页入口 | 文档数量 |
|-----|------|---------|---------|---------|
| `merchant` | 直连商户 | [llms.txt](https://pay.weixin.qq.com/doc/v3/merchant/llms.txt) | [首页](https://pay.weixin.qq.com/doc/v3/merchant/4012062524) | ~522 个页面 |
| `partner` | 合作伙伴 | [llms.txt](https://pay.weixin.qq.com/doc/v3/partner/llms.txt) | [首页](https://pay.weixin.qq.com/doc/v3/partner/4012069852) | ~897 个页面 |

## 核心设计

- **文档列表**：从官方 `llms.txt` 获取，包含完整的 `.md` URL 和 heading 层级结构。
- **变更检测**：仍从首页 HTML 的 `vike_pageContext` JSON 提取 `updateTime`，与 llms.txt 按 `docId` 匹配合并。
- **文档下载**：直接拉取官方 `.md` 地址（如 `https://pay.weixin.qq.com/doc/v3/merchant/4012062524.md`），不做任何格式转换。
- **版本管理**：本地文件命名 `{docId}_{updateTime}.md`，同一 docId 可保留多个版本。
- **差异报告**：修改页面直接生成新旧 Markdown 的 unified diff。

## 功能特性

- 解析 `llms.txt` 获取文档 URL 列表和层级结构。
- 从 HTML JSON 提取 `updateTime` 并与 llms.txt 按 `docId` 合并。
- 通过 `updateTime` 检测新增、删除、修改。
- 只在本地不存在对应版本 Markdown 时才下载。
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

1. 获取 `llms.txt`，解析获取所有文档的 `.md` URL 和 heading 层级。
2. 获取首页 HTML，从 `vike_pageContext` JSON 提取 `updateTime`。
3. 按 `docId` 匹配合并：URL 以 llms.txt 为准，updateTime 以 JSON 为准。
4. 对比本地 `latest.json`，识别新增、删除、修改。
5. 对新增和修改页面直接下载官方 `.md` 文件。
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
| `url` | 完整 `.md` URL，来自 llms.txt（如 `https://pay.weixin.qq.com/doc/v3/merchant/4012062524.md`） |
| `fullPath` | 页面完整层级路径 |
| `pathArray` | 路径数组 |

## 示例输出

```text
[20260520_094246] 开始抓取微信支付文档 - 直连商户
  llms.txt: https://pay.weixin.qq.com/doc/v3/merchant/llms.txt
  首页: https://pay.weixin.qq.com/doc/v3/merchant/4012062524

[1/6] 获取 llms.txt 文档列表...

[2/6] 解析 llms.txt 获取文档 URL 和层级...
  从 llms.txt 提取到 522 个文档

[3/6] 获取首页 JSON 数据（用于 updateTime）...
  从 JSON 提取到 543 个节点（含 updateTime）
  成功匹配 updateTime: 522/522 个文档

[4/6] 检测变更...
  新增: 2 个
  删除: 0 个
  修改: 1 个

[5/6] 拉取变更页面...
  [1/3]   拉取: 产品介绍 (4012062524)
  [2/3]   拉取: 开发指引 (4012791870)
  [3/3]   拉取: JSAPI/小程序下单 (4012791856)
  成功: 3 个
  失败: 0 个

[6/6] 生成差异报告...

[OK] 完成!
   索引文件: docs/merchant/index/index_20260520_094246.json
   最新索引: docs/merchant/index/latest.json
   Markdown 目录: docs/merchant/pages
   报告文件: docs/merchant/reports/report_20260520_094246.md
   最新报告: docs/merchant/reports/latest.md
```

## 依赖

- Python 3.6+
- 标准库：`difflib`、`json`、`os`、`re`、`time`、`urllib`、`datetime`、`pathlib`、`typing`

## 注意事项

1. 工具内置 0.5 秒请求间隔，避免请求过快。
2. 请求失败会自动重试 3 次，并使用指数退避。
3. 若某个修改页本地不存在旧版 Markdown，报告会提示无法生成 diff。
4. 若某文档在 llms.txt 中存在但 JSON 中找不到对应 updateTime，将以空 updateTime 保存。

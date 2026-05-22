# 微信支付文档抓取工具

从微信支付官方 `llms.txt` 获取 Markdown 文档列表，结合 HTML 页面的 `updateTime` 变更信息，直接下载官方 `.md` 格式文档。支持直连商户和合作伙伴两种文档类型、增量更新检测和 diff 报告。

## 支持的文档类型

| 类型 | 说明 | llms.txt | 首页入口 | 文档数量 |
|-----|------|---------|---------|---------|
| `merchant` | 直连商户 | [llms.txt](https://pay.weixin.qq.com/doc/v3/merchant/llms.txt) | [首页](https://pay.weixin.qq.com/doc/v3/merchant/4012062524) | ~522 个页面 |
| `partner` | 合作伙伴 | [llms.txt](https://pay.weixin.qq.com/doc/v3/partner/llms.txt) | [首页](https://pay.weixin.qq.com/doc/v3/partner/4012069852) | ~897 个页面 |

## 核心设计

- **文档列表**：从官方 `llms.txt` 获取，包含完整的 `.md` URL 和 heading 层级结构。
- **变更检测**：从首页 HTML 的 `vike_pageContext` JSON 提取 `updateTime`，与 llms.txt 按 `docId` 匹配合并。
- **文档下载**：直接拉取官方 `.md` 地址（如 `https://pay.weixin.qq.com/doc/v3/merchant/4012062524.md`），不做任何格式转换。
- **版本管理**：所有文件只保留最新版本（`pages/{docId}.md`），历史变更由 git 跟踪。
- **差异报告**：修改页面和 llms.txt 的变更内容直接输出 unified diff。

## 功能特性

- 解析 `llms.txt` 获取文档 URL 列表和层级结构，仅内容变化时更新本地文件。
- 对比本地 llms.txt，检测自身结构变动并生成 diff。
- 从 HTML JSON 提取 `updateTime` 并与 llms.txt 按 `docId` 合并。
- 通过 `updateTime` 检测新增、删除、修改。
- 内容未变化时跳过写入，避免无意义的文件变更。
- 自动为修改页生成 diff 并写入报告。
- 所有文件只保留最新版本，变更历史由 git 管理。

## 目录结构

```text
wechatpay_docs/
├── docs/
│   ├── merchant/
│   │   ├── llms.txt          # 最新 llms 内容
│   │   ├── index.json        # 最新文档索引
│   │   ├── report.md          # 最新变更报告
│   │   └── pages/
│   │       └── {docId}.md     # 各页面最新版本
│   └── partner/
│       ├── llms.txt
│       ├── index.json
│       ├── report.md
│       └── pages/
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
6. 对修改页对比本地旧内容生成 unified diff。
7. 覆盖写入 index.json 和 report.md，由 git 跟踪变更历史。

## 增量更新规则

| 变更类型 | 检测条件 | 处理方式 |
|---------|---------|---------|
| 新增 | `docId` 在新索引中存在，但在旧索引中不存在 | 拉取 Markdown 并落盘 |
| 删除 | `docId` 在旧索引中存在，但在新索引中不存在 | 记录到报告 |
| 修改 | `docId` 相同但 `updateTime` 不同 | 拉取新版本 Markdown，生成 diff |

## 报告内容

报告包含以下内容：

- 变更概览统计（含 llms.txt 自身是否变更）。
- 新增页面信息。
- 删除页面信息。
- 修改页面的更新时间变化和 unified diff。
- 拉取失败页面清单。
- llms.txt 结构变更 diff（如有）。
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
   llms.txt:  docs/merchant/llms.txt
   index.json: docs/merchant/index.json
   pages/:     docs/merchant/pages
   report.md:  docs/merchant/report.md
```

## 依赖

- Python 3.6+
- 标准库：`difflib`、`json`、`os`、`re`、`time`、`urllib`、`datetime`、`pathlib`、`typing`

## 注意事项

1. 工具内置 0.5 秒请求间隔，避免请求过快。
2. 请求失败会自动重试 3 次，并使用指数退避。
3. 若某个修改页本地不存在旧版 Markdown，报告会提示无法生成 diff。
4. 若某文档在 llms.txt 中存在但 JSON 中找不到对应 updateTime，将以空 updateTime 保存。

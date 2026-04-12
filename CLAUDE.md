# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python tool for fetching WeChat Pay (微信支付) API documentation. It supports two document types:
- `merchant` (直连商户) - ~528 pages
- `partner` (合作伙伴) - ~897 pages

## Common Commands

### Run the fetcher

```bash
# Default: fetch merchant docs
python wechatpay_doc_fetcher.py

# Fetch partner docs
python wechatpay_doc_fetcher.py --type partner

# Test mode (first 10 pages only)
python wechatpay_doc_fetcher.py --type merchant --limit 10

# Custom output directory
python wechatpay_doc_fetcher.py --type partner --output ./my_docs
```

### Fetch both document types

```bash
python wechatpay_doc_fetcher.py --type merchant && python wechatpay_doc_fetcher.py --type partner
```

## Architecture

### Single-file design

All functionality is in [`wechatpay_doc_fetcher.py`](wechatpay_doc_fetcher.py) - a self-contained Python script using only standard library modules:
- `urllib.request` for HTTP requests
- `json`/`re` for data parsing
- `difflib` for report diffs
- `pathlib` for directory management

### Data flow

1. **Fetch index page** → Extract embedded JSON from `vike_pageContext` script tag
2. **Parse menu structure** → Recursively traverse `menuData` to find leaf nodes
3. **Detect changes** → Compare `updateTime` fields against previous index
4. **Fetch changed pages** → Request the official `.md` URL for each page and save Markdown to disk (skips if already exists)
5. **Generate report** → Markdown report with add/remove/modify sections and unified diff for modified pages

### Directory structure (output)

```
wechatpay_docs/
├── merchant/                 # or partner/
│   ├── index/
│   │   ├── index_{timestamp}.json      # timestamped index snapshot
│   │   └── latest.json                 # latest index
│   ├── pages/
│   │   └── {docId}/
│   │       └── {docId}_{updateTime}.md    # page content
│   └── reports/
│       ├── report_{timestamp}.md        # each run's report
│       └── latest.md -> report_*.md     # symlink to latest
```

Files are named `{docId}_{updateTime}.{ext}` - if a file with that updateTime exists, it's skipped (incremental updates).

### Key class: WechatPayDocFetcher

- [`DOC_TYPES`](wechatpay_doc_fetcher.py:27-38): Configuration for merchant/partner endpoints
- `extract_json_data()`: Parses JSON from HTML script tag
- `extract_leaf_nodes()`: Recursively finds all document pages
- `detect_changes()`: Compares old vs new index for added/removed/modified
- `save_markdown()`: Fetches and saves individual Markdown page (with existence check)
- `build_diff()`: Generates unified diff for modified pages
- `generate_report()`: Creates Markdown diff report

### Rate limiting

- 0.5 second delay between page requests
- 3 retries with exponential backoff (2^attempt seconds)

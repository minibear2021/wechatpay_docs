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
- `pathlib` for directory management

### Data flow

1. **Fetch index page** → Extract embedded JSON from `vike_pageContext` script tag
2. **Parse menu structure** → Recursively traverse `menuData` to find leaf nodes
3. **Detect changes** → Compare `updateTime` fields against previous index
4. **Fetch changed pages** → Save HTML + metadata to disk (skips if already exists)
5. **Generate report** → Markdown diff report with all changes

### Directory structure (output)

```
wechatpay_docs/
├── merchant/                 # or partner/
│   ├── index/
│   │   ├── leaf_nodes_index.json       # current index
│   │   └── leaf_nodes_index_prev.json  # backup of previous
│   ├── pages/
│   │   └── {docId}/
│   │       ├── {docId}_{updateTime}.html  # page content
│   │       └── {docId}_{updateTime}.json  # metadata
│   └── reports/
│       ├── report_{timestamp}.md        # each run's report
│       └── latest.md -> report_*.md     # symlink to latest
```

Files are named `{docId}_{updateTime}.{ext}` - if a file with that updateTime exists, it's skipped (incremental updates).

### Key class: WechatPayDocFetcher

- [`DOC_TYPES`](wechatpay_doc_fetcher.py:27-38): Configuration for merchant/partner endpoints
- [`extract_json_data()`](wechatpay_doc_fetcher.py:89-104): Parses JSON from HTML script tag
- [`extract_leaf_nodes()`](wechatpay_doc_fetcher.py:106-143): Recursively finds all document pages
- [`detect_changes()`](wechatpay_doc_fetcher.py:177-211): Compares old vs new index for added/removed/modified
- [`save_page()`](wechatpay_doc_fetcher.py:213-257): Fetches and saves individual page (with existence check)
- [`generate_report()`](wechatpay_doc_fetcher.py:259-364): Creates Markdown diff report

### Rate limiting

- 0.5 second delay between page requests
- 3 retries with exponential backoff (2^attempt seconds)

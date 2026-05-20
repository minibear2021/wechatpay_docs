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

1. **Fetch llms.txt** → Get the official document list with `.md` URLs and hierarchy, compare with previous snapshot, save timestamped copy
2. **Fetch index page** → Extract embedded JSON from `vike_pageContext` script tag for `updateTime` metadata
3. **Merge data** → Match documents by `docId`: URLs from llms.txt, updateTime from JSON
4. **Detect changes** → Compare `updateTime` fields against previous index; also detect llms.txt structural changes
5. **Fetch changed pages** → Download Markdown directly from the official `.md` URLs listed in llms.txt (skips if already exists locally)
6. **Generate report** → Markdown report with add/remove/modify sections, llms.txt diff, and unified diff for modified pages

### Directory structure (output)

```
wechatpay_docs/
├── merchant/                 # or partner/
│   ├── llms/
│   │   ├── llms_YYYYMMDD_HHMMSS.txt          # timestamped llms.txt snapshot
│   │   └── latest.txt                    # latest llms.txt
│   ├── index/
│   │   ├── index_YYYYMMDD_HHMMSS.json      # timestamped index snapshot
│   │   └── latest.json                 # latest index
│   ├── pages/
│   │   └── {docId}/
│   │       └── {docId}_{updateTime}.md    # page content
│   └── reports/
│       ├── report_YYYYMMDD_HHMMSS.md        # each run's report
│       └── latest.md -> report_*.md     # symlink to latest
```

Files are named `{docId}_{updateTime}.{ext}` - if a file with that updateTime exists, it's skipped (incremental updates).

### Key class: WechatPayDocFetcher

- [`DOC_TYPES`](wechatpay_doc_fetcher.py:27-38): Configuration for merchant/partner endpoints (index_url + llms_url)
- `parse_llms_txt()`: Parses llms.txt markdown to extract doc URLs and heading hierarchy
- `save_llms_txt()`: Saves timestamped llms.txt snapshot, returns unified diff if changed from previous
- `extract_json_data()`: Parses JSON from HTML script tag
- `extract_leaf_nodes()`: Recursively finds all document pages with updateTime
- `merge_with_update_time()`: Merges llms.txt URLs with JSON updateTime by docId
- `detect_changes()`: Compares old vs new index for added/removed/modified
- `save_markdown()`: Fetches and saves individual Markdown page from official .md URL (with existence check)
- `build_diff()`: Generates unified diff for modified pages
- `generate_report()`: Creates Markdown diff report

### Rate limiting

- 0.5 second delay between page requests
- 3 retries with exponential backoff (2^attempt seconds)

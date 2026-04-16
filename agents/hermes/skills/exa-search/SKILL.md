---
name: exa-search
description: Web search, deep research, and content extraction via Exa.ai API. Use for searching the web, researching companies, finding LinkedIn profiles, or getting clean content from URLs. Requires EXA_API_KEY environment variable.
---

# Exa Search Skill

Search the web, research companies, and extract content using Exa.ai.

## Setup

Set your API key:
```bash
export EXA_API_KEY="your-api-key"
```

Get a free key at: https://dashboard.exa.ai/api-keys

## Usage

### Web Search
```bash
./scripts/exa.sh search "query here"
```

### Search with Content
```bash
./scripts/exa.sh search "query here" --text
```

### Get URL Content
```bash
./scripts/exa.sh crawl "https://example.com"
```

### Company Research
```bash
./scripts/exa.sh company "stripe.com"
```

### Find Similar Sites
```bash
./scripts/exa.sh similar "https://techcrunch.com"
```

## API Reference

All commands output JSON. Parse with `jq` for specific fields.

### Search Options
- `--num` - Number of results (default: 10)
- `--text` - Include page content
- `--type` - Search type: `auto`, `neural`, `keyword`

## Examples

Find finance Twitter accounts:
```bash
./scripts/exa.sh search "finance trading twitter accounts 50k-100k followers" --text --num 20
```

Research a company:
```bash
./scripts/exa.sh company "belangertrading.com"
```

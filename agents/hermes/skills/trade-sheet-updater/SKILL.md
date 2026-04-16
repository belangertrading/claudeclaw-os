---
name: trade-sheet-updater
description: "Update trade tracking Google Sheets via webhook. Use when adding trades (buy), closing trades (sell), correcting entries (delete/update), or fixing alert links. Handles all three services: Options Insider, Hot Money Trader, and 48-Hour Cashflow."
---

# Trade Sheet Updater

Updates trade tracking sheets via Google Apps Script webhooks. Three services, same mechanism.

Updating a sheet involves these steps:

1. Identify the service (Options Insider, Hot Money Trader, or 48-Hour Cashflow)
2. Load the service reference file
3. Build the payload
4. Run `scripts/update_sheet.py` (or use the curl pattern directly)
5. Verify the sheet updated correctly

## Service Reference Files

Load only the file you need:

- `references/options-insider.md` — Options Insider sheet schema + payloads
- `references/hot-money.md` — Hot Money Trader sheet schema + payloads
- `references/48hr-cashflow.md` — 48-Hour Cashflow sheet schema + payloads

## Shared curl Pattern

All three services use Google Apps Script, which redirects POST requests. Always use:

```bash
WEBHOOK_URL="https://script.google.com/macros/s/..."
PAYLOAD='{"action":"buy","ticker":"AAPL",...}'

REDIRECT=$(curl -s -w "%{redirect_url}" -o /dev/null -X POST \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD" "$WEBHOOK_URL")
curl -sL "$REDIRECT"
```

## Script

`scripts/update_sheet.py` handles all three services:

```bash
python3 scripts/update_sheet.py options-insider buy SCHW ...
python3 scripts/update_sheet.py hot-money sell STM 3.00 ...
python3 scripts/update_sheet.py 48hr buy FIG ...
```

Run with no args for full usage.

## Critical Rule

**Never update the sheet before the alert is published.** Sequence: write → draft → approve → publish → sheet.

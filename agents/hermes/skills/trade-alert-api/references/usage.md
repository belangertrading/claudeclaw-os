# Trade-Alert API — Usage Guide

## Base URL & Authentication
```
https://quant.trade-alert.com/?cmd=<COMMAND>&apikey=<KEY>&output=jsn
```

API key is stored in `/home/clawdbot/.env` as `TRADE_ALERT_API_KEY` and in the dashboard's `.env.local`.

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `cmd` | Command name (see commands.md) | Required |
| `apikey` | API key | Required |
| `output` | Format: `tsv`, `csv`, `html`, `jsn` (objects), `json` (arrays) | `tsv` |
| `symbol` | Ticker, option symbol, group, or basket | `@ALL` |
| `date` | Query date `YYYY-MM-DD` | Today / most recent trading day |
| `limit` | Number of rows | 50 |
| `fields` | Comma-separated list of fields to return | All default fields |
| `where` | Boolean filter expression | None |

### Symbol Parameter
- Single ticker: `symbol=AAPL`
- Sector group: `symbol=@FIN` (financials), `symbol=@TECH`, etc.
- All: `symbol=@ALL` (default for most commands)
- Stock only: `symbol=@STOCK`
- ETF only: `symbol=@ETF`
- Index only: `symbol=@INDEX`

### Output Formats
- `jsn` — JSON with named fields (objects). **Use this.** Each row is `{field: value, ...}`
- `json` — JSON with header + data arrays (compact but harder to use)
- `tsv` / `csv` — Tab/comma separated
- `html` — HTML table
- `glossary` — Returns field definitions for the command

### Where Filter
Boolean expression using field names. Examples:
```
where=cap=L                    # Large cap only
where=sweep=true               # Sweeps only
where=earnings=true            # Pre-earnings only
where=call=true                # Calls only
where=weekly=true              # Weekly expiry only
where=size>1000                # Size > 1000 contracts
where=premium>1000000          # Premium > $1M
where=sector=Technology        # Tech sector
where=otm=true                 # OTM options only
```

Combine with `&`: `where=cap=L&sweep=true&call=true`

### Fields Parameter
Comma-separated field names. Example:
```
fields=usymbol,size,price,strike,expiry,put_call,delta,ivol,premium,mktside,comments
```

### Glossary Access
Get field definitions for any command:
```
cmd=Top&parm=Trade&output=glossary      # Trade fields
cmd=Top&parm=Underlying&output=glossary  # Underlying fields  
cmd=Top&parm=Option&output=glossary      # Option fields
cmd=Spread&parm=Trade&output=glossary    # Spread trade fields
cmd=Moso&parm=Option&output=glossary     # Option analysis fields
cmd=Most&parm=Underlying&output=glossary # Market analysis fields
cmd=Color&parm=Note&output=glossary      # Note fields
```

## Rate Limits & Tier Info

### Our Tier (Free/Basic)
- **50 calls per day** (shared across API + web UI)
- Default 50 rows per call
- Some commands blocked during market hours (Sweep, Top confirmed blocked)
- Historical date queries (`date=YYYY-MM-DD`) return empty on free tier
- Data persists on weekends/holidays (returns last session)

### Confirmed Working (Free Tier)
- `Bullish` ✅
- `Bearish` ✅  
- `Uvol` ✅
- `Most` ✅

### Confirmed Blocked (Free Tier, Market Hours)
- `Sweep` ❌
- `Top` ❌

### Untested (Need Verification)
All other commands — test during market hours to determine access.

### Enterprise Tier
- Unlimited daily calls
- 60 calls/minute rate limit
- Per-command pricing
- Redistribution permitted

## Response Handling

### Null Bytes
The API sometimes returns null bytes (`\0`) in responses. Always strip them:
```typescript
const clean = text.replace(/\0/g, '');
```

### HTML Wrapping
Error messages are sometimes wrapped in `<h2>` tags:
```typescript
const clean = text.replace(/<\/?h2>/g, '').trim();
```

### Error Response
```json
{"error": "Reached data fetch limit of 50 calls per day"}
```

### Success Response (jsn format)
```json
{
  "data": [
    {"usymbol": "AAPL", "calls": 150000, "puts": 80000, ...},
    {"usymbol": "NVDA", "calls": 200000, "puts": 60000, ...}
  ]
}
```

## Example Queries

### Bullish flow, large cap, custom fields
```
cmd=Bullish&fields=usymbol,calls,puts,net_delta,net_vega,bullish_pct,atm_ivol,spot,spot_chg&where=cap=L&limit=20&output=jsn
```

### Most active options for a single ticker
```
cmd=Moso&symbol=NVDA&fields=usymbol,expiry,strike,put_call,volume,open_int,oichg,ask_pct,ivol&limit=20&output=jsn
```

### Unusual volume with earnings filter
```
cmd=Uvol&where=earnings=true&fields=usymbol,option_volume,adv,option_mult,atm_ivol,atm_ivol_chg,spot&limit=20&output=jsn
```

### Sweeps only (paid tier)
```
cmd=Sweep&where=size>500&fields=usymbol,size,price,strike,expiry,put_call,premium,mktside,delta,ivol&limit=30&output=jsn
```

### IV movers
```
cmd=IVGap&fields=usymbol,atm_ivol,atm_ivol_chg,atm_ivol_chg_pct,volatility20day,spot,spot_chg&limit=20&output=jsn
```

### Open interest changes
```
cmd=OIChg&fields=usymbol,expiry,strike,put_call,open_int,oichg,volume,ask_pct,ivol&limit=20&output=jsn
```

## Operating Hours
- API available: 6:15 AM – 11:45 PM ET
- Market hours: 9:30 AM – 4:00 PM ET
- Pre/post market data available during extended hours
- Weekend: returns last session data

## Support
- Email: trade-alertsupport@cboe.com
- Phone: 212-372-8020

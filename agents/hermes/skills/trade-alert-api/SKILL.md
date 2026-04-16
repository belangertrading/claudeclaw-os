---
name: trade-alert-api
description: Query the Trade-Alert (Cboe) options flow API for real-time and historical options activity data. Use when fetching options flow, unusual volume, sweeps, bullish/bearish activity, IV movers, open interest changes, spread trades, 13F holdings, or any options market data from Trade-Alert. Covers ~120 API commands across trade recaps, spread identification, security analysis, market analysis, IV analysis, and institutional data. Also use when building or modifying the Live Flow dashboard, designing flow-based alerts, or analyzing options market structure.
---

# Trade-Alert API Skill

Options flow data from Trade-Alert (Cboe subsidiary). Provides real-time and historical options trade data across all US options exchanges.

## Quick Start

```bash
# Basic query
curl "https://quant.trade-alert.com/?cmd=Bullish&apikey=${TRADE_ALERT_API_KEY}&output=jsn&limit=20"

# Custom fields + filter
curl "https://quant.trade-alert.com/?cmd=Bullish&apikey=${TRADE_ALERT_API_KEY}&output=jsn&limit=20&fields=usymbol,calls,puts,net_delta,bullish_pct,atm_ivol,spot&where=cap=L"
```

API key: stored in `/home/clawdbot/.env` as `TRADE_ALERT_API_KEY`

Always strip null bytes and HTML tags from responses:
```typescript
const clean = text.replace(/\0/g, '').replace(/<\/?h2>/g, '').trim();
```

## Rate Limit — Critical

**50 calls/day on our tier.** Shared across API calls AND web UI usage. Budget carefully.

- Use `output=jsn` (named field objects)
- Cache aggressively — each call costs 2% of daily budget
- Stagger/rotate endpoints, don't fetch all at once
- Confirmed working (free tier): `Bullish`, `Bearish`, `Uvol`, `Most`
- Confirmed blocked (market hours): `Sweep`, `Top`

## Reference Files

- **[commands.md](references/commands.md)** — Complete list of ~120 API commands organized by category (trade recaps, spreads, security analysis, market analysis, IV, 13F, other)
- **[fields.md](references/fields.md)** — All available fields for Trade, Underlying, and Option field types. Includes boolean flags usable in `where` filters. Read this when selecting columns or building filters.
- **[usage.md](references/usage.md)** — Query construction, parameters (`symbol`, `date`, `limit`, `fields`, `where`, `output`), response handling, example queries, rate limits, tier info, operating hours.

## Key Parameters

| Param | Purpose | Example |
|-------|---------|---------|
| `cmd` | Command name | `Bullish` |
| `symbol` | Ticker/group | `AAPL`, `@FIN`, `@STOCK` |
| `fields` | Select columns | `usymbol,calls,puts,net_delta` |
| `where` | Boolean filter | `cap=L`, `sweep=true`, `earnings=true` |
| `limit` | Row count | `20` |
| `date` | Historical date | `2026-03-01` (paid tier only) |
| `output` | Format | `jsn` (always use this) |

## Dashboard Integration

Live Flow page: `/home/clawdbot/clawd/apps/mission-control/app/live-flow/page.tsx`
API route: `/home/clawdbot/clawd/apps/mission-control/app/api/flow/route.ts`
Cache file: `/home/clawdbot/clawd/data/mission-control/flow-cache.json`

The API route uses per-endpoint independent caching with rotation — only the stalest endpoint gets refreshed each cycle (1 call per refresh, not all at once).

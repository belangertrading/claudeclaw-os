# Hot Money Trader Sheet

**Webhook:** `https://script.google.com/macros/s/AKfycbz4o0eF_rqmqPwERnu61Yt-mw2QI_pPOGu-Yh5to61bdzCpJOwVaudkmxrPA0v9X42t/exec`
**Sheet ID:** `12VsTbwaABgz8rLfDJQVm2n1YE-n5SzLUhFM4igpJH5o`

## Column Layout

| Col | Field |
|-----|-------|
| A | Status (Open/Closed) |
| B | Entry Date |
| C | Ticker |
| D | Stock Entry (formula) |
| E | Signal Type |
| F | Strategy |
| G | Exp. Cycle |
| H | Short Strike (spreads only) |
| I | Long Strike (single leg: strike goes here) |
| J | Type (C or P) |
| K-L | Short/Long Code (formulas) |
| M | Entry Debit |
| N | Current Value |
| O | Take Profit |
| P | Stop Loss |
| Q | Options Exit Date |
| R | Options Exit Price |
| S | Stock Exit Price (formula) |
| T-X | P/L, Return %, Win/Loss, Days Held (formulas) |
| Y | Buy Alert Link |
| Z | Sell Alert Link |

## Buy

```json
{
  "action": "buy",
  "ticker": "STM",
  "entryDate": "2/5/2026",
  "signalType": "",
  "strategy": "Long Call",
  "expCycle": "3/20/2026",
  "shortStrike": "",
  "longStrike": 30,
  "type": "C",
  "entryPrice": 1.35,
  "takeProfit": 1.89,
  "stopLoss": 0.54,
  "buyAlertLink": "https://..."
}
```

**Strike logic:**
- Spread: both `shortStrike` + `longStrike`
- Single leg: `longStrike` only (or `strike`)

`entryDate` defaults to today if omitted.

## Sell

```json
{
  "action": "sell",
  "ticker": "STM",
  "exitPrice": 3.50,
  "exitDate": "2/9/2026",
  "sellAlertLink": "https://..."
}
```

Also works on already-closed trades (updates exit fields). `expCycle` optional for disambiguation.

## Delete

```json
{
  "action": "delete",
  "ticker": "STM",
  "expCycle": "3/20/2026"
}
```

Delete only works on Open trades. To fix a closed trade, use `sell` action instead.

## Update (Fix any field)

```json
{
  "action": "update",
  "ticker": "STM",
  "sellAlertLink": "https://...",
  "exitPrice": 3.50,
  "exitDate": "2/9/2026"
}
```

Works on open or closed trades. Use to fix alert links, prices, etc.

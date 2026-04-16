# Options Insider Sheet

**Webhook:** `https://script.google.com/macros/s/AKfycby8b-gFkH_UkfIhg0nYTCmCeagXfiJzXRFU-j3movoU9HE03K7qtR07mn5_5Wi7Fc1oTw/exec`
**Sheet ID:** `1YyATKBbAanLe4xvL1C2CdLuGJFteyGnbCrYv1HjuSO8`

## Column Layout

| Col | Field |
|-----|-------|
| A | Status (Open/Closed) |
| B | Entry Date |
| C | Ticker |
| D | Stock Entry (formula — never write) |
| E | Signal Type |
| F | Strategy |
| G | Exp. Cycle |
| H | Leg 1 Strike (call for strangles, short for spreads) |
| I | Leg 2 Strike (put for strangles, long for spreads, single strike for calls/puts) |
| J | Type (C, P, or C/P) |
| K-L | Long/Short Code — **AUTO-FORMULATED. Never write to K or L.** |
| M | Entry Debit (entry price) |
| N | Current Value (formula) |
| O | Take Profit |
| P | Stop Loss |
| Q | Options Exit Date |
| R | Options Exit Price |
| S-X | P/L formulas |
| Y | Buy Alert Link |
| Z | Sell Alert Link |

## Buy

> `signalType` = pattern name (e.g. "Bull Surge", "U-Turn Velocity") — NOT "Options Insider"

```json
{
  "action": "buy",
  "ticker": "SCHW",
  "signalType": "Two-Way Trigger",
  "strategy": "Strangle",
  "expCycle": "2/27/26",
  "type": "C/P",
  "leg1Strike": 96,
  "leg2Strike": 93,
  "entryPrice": "$3.22",
  "takeProfit": "$3.86",
  "stopLoss": "10-day exit",
  "entryDate": "2/13/26",
  "buyAlertLink": "https://..."
}
```

**Strike logic:**
- Two-leg (Spread, Strangle, Straddle): `leg1Strike` + `leg2Strike`
- Single-leg (Long Call/Put): `leg2Strike` only (Leg 1 cleared, set to `""`)
- Strangles/Straddles: type = `"C/P"`

**Type field — exact values only:**
- `"C"` — calls (Long Call, Bull Call Spread)
- `"P"` — puts (Long Put, Bear Put Spread)
- `"C/P"` — both legs (Strangle, Straddle)
- Never use `"CALL"`, `"PUT"`, `"call"`, `"put"` — the sheet won't map it correctly

**Duplicate row prevention:**
After POSTing, read the sheet back immediately and count rows for that ticker + expCycle. If you see 2 rows, delete one immediately. Don't wait for Josh to catch it. The GAP webhook incident: first POST succeeded despite redirect response. Check before retrying.

## Sell

```json
{
  "action": "sell",
  "ticker": "SCHW",
  "expCycle": "2/27/26",
  "exitPrice": "$5.00",
  "exitDate": "2/20/26",
  "sellAlertLink": "https://..."
}
```

## Delete (Undo)

```json
{
  "action": "delete",
  "ticker": "SCHW",
  "expCycle": "2/27/26"
}
```

Smart: open trade → deletes row. Closed trade → clears exit fields (re-opens). `expCycle` optional.

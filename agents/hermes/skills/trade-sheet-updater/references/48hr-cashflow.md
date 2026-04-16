# 48-Hour Cashflow Sheet

**Webhook:** `https://script.google.com/macros/s/AKfycbyPMKg4GL32cBRjBziHE4zXE0u68CMRixcmSCqrSy_6wh2k_NXc9Ym-ivbIav7Om8eQ/exec`
**Sheet ID:** `1x9xQJAwWxkSY1lpkBLZlHZjhkjw2ZwAH1yybhZz_F00`

## Buy

```json
{
  "action": "buy",
  "ticker": "FIG",
  "strategy": "Put Spread",
  "expCycle": "Feb 20, 2026",
  "entryPrice": 0.10,
  "shortStrike": 21,
  "longStrike": 20.5,
  "entryDate": "2/19/2026",
  "earnings": "Y",
  "buyAlertLink": "https://..."
}
```

`entryDate` and `earnings` optional. `earnings` defaults to "N".

## Sell

```json
{
  "action": "sell",
  "ticker": "FIG",
  "exitPrice": 0,
  "exitDate": "2/20/2026",
  "sellAlertLink": "https://..."
}
```

`exitPrice` = cost to close (0 if expires worthless). `exitDate` defaults to today.

## Delete (Undo)

```json
{
  "action": "delete",
  "ticker": "FIG"
}
```

Smart: open trade → deletes row. Closed trade → clears exit fields (re-opens).

## Column Map (for manual fallback edits only)

If the webhook fails and you must edit cells directly via `gog sheets update`, verify column headers first:

```
A  Entry Date
B  Exit Date
C  Ticker
D  Strategy
E  Short Strike
F  Long Strike
G  Expiration Cycle
H  Credit Received
I  Exit Cost
J  P/L per Contract
K  Capital Required
L  Return %
M  Win/Loss
N  Days Held
O  Earnings
P  Opening Alert Link
Q  Closing Alert Link   ← col 17
R  Status               ← col 18 — AUTO-POPULATED by sheet formula. Never write to this column.
```

**⚠️ Always run `gog sheets get ... 'A1:S1'` to confirm headers before any manual cell edit.** Miscounting columns (e.g. putting the closing link in R/Status instead of Q) corrupts the row silently.

## Script

`scripts/update_sheet.py 48hr` wraps this webhook. Can also use directly via curl pattern in SKILL.md.

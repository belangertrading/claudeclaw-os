---
name: trade-cards
description: Generate branded trade card graphics for social media, journal entries, and visual content. Bloomberg dark style matching Belanger Trading charts.
---

# Trade Card Generator

Generate clean, branded trade card graphics showing key trade details at a glance.

## Use Cases

- **Social media posts** — Shareable trade visuals
- **Journal entries** — Visual record of trades
- **Content creation** — YouTube thumbnails, thread headers
- **NOT for alerts** — Alerts use pattern charts + text

## Script Location

```
scripts/generate-trade-card.py
```

## Usage

```python
from scripts.generate_trade_card import generate_trade_card

path = generate_trade_card(
    ticker="DDOG",
    strike=148,
    option_type="Call",       # 'Call' or 'Put'
    expiration="Feb 27, 2026",
    entry=6.50,
    target=9.75,
    stop=3.25,
    pattern="U-Turn Velocity",
    win_loss="5W - 1L",
    total_return="466%",
    direction="BUY"           # 'BUY' or 'SELL'
)
```

## Command Line

```bash
cd /home/clawdbot/clawd
source .venv/bin/activate
python scripts/generate-trade-card.py
```

Edit the script's `__main__` block to change parameters, or import as module.

## Output

- **Location:** `/var/www/html/charts/`
- **URL:** `https://joshbelanger.com/charts/{ticker}_trade_card_{timestamp}.png`
- **Format:** PNG, 150 DPI
- **Style:** Bloomberg dark (matches existing charts)

## Visual Elements

```
┌────────────────────────────┐
│  🟢 BUY ALERT              │  ← Direction badge (green/red)
│  DDOG $148 Call            │  ← Ticker, strike, type
│  Feb 27, 2026              │  ← Expiration
├────────────────────────────┤
│  Entry:    $6.50           │  ← Trade details
│  Target:   $9.75  (+50%)   │  ← Green for profit
│  Stop:     $3.25  (-50%)   │  ← Red for loss
├────────────────────────────┤
│  U-Turn Velocity           │  ← Pattern name
│  5W - 1L | 466% returns    │  ← Track record
└────────────────────────────┘
         BELANGER TRADING       ← Branding
```

## Future Ideas

- **SELL version** — Red badge, shows result (win/loss, %)
- **Spread version** — Shows both legs, max gain/loss
- **Animated GIF** — Entry → Target path
- **Series cards** — Multiple trades in a thread

## Dependencies

- matplotlib
- Already in `.venv/`

---

*Created: Feb 5, 2026*
*Status: Ready, waiting for use case*

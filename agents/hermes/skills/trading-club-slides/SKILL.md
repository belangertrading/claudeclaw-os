---
name: trading-club-slides
description: Create weekly Trading Club session slides — HTML presentation deck for the $15K one-time-fee Trading Club. Pull member trades from Gmail, build 6-slide deck matching existing format, deploy to mission control. Runs every Wednesday.
version: 1.0.0
tags: [trading-club, slides, presentation, weekly]
---

# Trading Club Weekly Slides

Create the weekly HTML slide deck for the Trading Club session (Wednesdays at 3:00 PM ET).

## Trigger
- Weekly Trading Club session needs presentation slides
- Henry normally handles this — Hermes is backup

## Key Lesson (April 2026)
- ALWAYS use live market data (yfinance) — never estimate or reuse last week's numbers. Josh flagged this.
- Members email their trades to Gmail — use himalaya to search/fetch from Karan, Ed, etc.
- 2022 Playbook backtests Josh wants referenced in volatile markets:
  - Absolute Return: 45 DTE @ 50% Limit (50Δ/5Δ) — 128% return, 92.3% WR, 12W/1L
  - Capital Preservation: 90 DTE @ 50% Limit (30Δ/5Δ) — 140% return, 100% WR, 0 losses
Josh says something like "need this week's Trading Club slides" or "Trading Club deck."

## Workflow

### Step 1: Get Last Week's Slides (Template)

```bash
# Slides served from mission control Next.js app on port 8888
# Reference the most recent one for format/style
curl -s http://localhost:8888/trading-club-YYYY-MM-DD.html > /tmp/trading-club-template.html
```

Previous slides live at:
- `/home/clawdbot/clawd/data/presentations/trading-club-YYYY-MM-DD.html`
- `/home/clawdbot/clawd/apps/mission-control/public/trading-club-YYYY-MM-DD.html`

### Step 2: Pull Trade Emails from Gmail

Members email their trades weekly to `support@joshbelanger.com`. Use **himalaya** (not google-workspace — that's not authenticated).

```bash
# Find this week's trade emails
himalaya envelope list "from karan and after YYYY-MM-DD" 
himalaya envelope list "from ed and after YYYY-MM-DD"

# Read the emails (use the ID from envelope list)
himalaya message read MESSAGE_ID
```

**Key people:**
- **Karan Sihota** (`karysihota@gmail.com`) — check for "Re:" replies with corrections (use the LATEST version)
- **Ed Jang** (`ed@jangfirm.com`) — often has a legal disclaimer footer, ignore it

### Step 3: Parse Trade Details & Calculate Derived Values

From each email, extract:
- Ticker, current price, company name
- Directional bias (BULLISH/BEARISH)
- Thesis bullet points (distill to 5 concise bullets)
- Trade structure (spread type)
- Expiration date
- Strike prices
- Premium/debit cost
- Allocation %
- Bailout plan

**Pull LIVE prices for all tickers (market context + trade tickers):**

```bash
/usr/bin/python3 -c "
import yfinance as yf
import warnings; warnings.filterwarnings('ignore')
for sym, name in [('SPY','SPY'), ('^VIX','VIX'), ('CL=F','Crude Oil'), ('USO','USO'), ('RKLB','RKLB'), ('XLE','XLE')]:
    t = yf.Ticker(sym)
    h = t.history(period='5d')
    if not h.empty:
        last = h['Close'].iloc[-1]
        prev = h['Close'].iloc[-2] if len(h) > 1 else last
        chg = ((last - prev) / prev) * 100
        print(f'{name}: \${last:.2f} ({chg:+.2f}%)')
"
```

Adjust the ticker list to match whatever's relevant that week. Also pull 1mo/3mo ranges for context descriptions.

**Calculate these yourself (not in the emails):**

| Metric | Formula |
|--------|---------|
| Max Reward (debit spread) | (width of strikes - debit paid) × 100 |
| Max Reward (credit spread) | credit received × 100 |
| Max Loss (debit spread) | debit paid × 100 |
| Max Loss (credit spread) | (width of strikes - credit received) × 100 |
| Breakeven (bull call spread) | long strike + debit paid |
| Breakeven (bear put spread) | long strike - debit paid |
| Breakeven (bear call spread) | short strike + credit received |
| DTE | expiration date - session date |
| Reward-to-Risk | max reward / max loss |

### Step 4: Build the 6-Slide HTML Deck

The deck is a single self-contained HTML file. Structure:

1. **Title Slide** — "BELANGER TRADING" logo, "Trading Club" heading, catchy subtitle (themed to the week's trades), date "MONTH DD, YYYY · 3:00 PM ET"
2. **Market Context** — 4 cards with key market levels (SPY, VIX, Crude Oil, + 1 relevant). Amber takeaway box summarizing the setup.
3. **Member Trade #1** — Two-column: thesis bullets (left), setup data grid + bailout box (right). Trade header with ticker, price, name, direction badge.
4. **Member Trade #2** — Same format as Trade #1.
5. **Comparison Board** — Side-by-side cards with key metrics (cost, max reward, DTE, breakeven) + summary blurb. 
6. **Discussion Points** — 5 numbered questions that contrast the two trades and provoke discussion.

**Color coding:**
- Both bullish → `green-highlight` cards on comparison board, `badge bullish`
- Both bearish → `red-highlight` cards, `badge bearish`  
- Mixed → one of each
- Debit values → `color: var(--red)`
- Credit/reward values → `color: var(--green)`
- Neutral/elevated → `color: var(--amber)`

**Title subtitle ideas by theme:**
- Both bearish → "Two Bears Walk Into a Bar"
- Both bullish → "Ignition Sequence", "Green Light"
- Mixed → "The Split", "Two Sides"
- Event-driven → reference the catalysts

### Step 5: Deploy

Copy to BOTH locations:

```bash
cp /tmp/trading-club-YYYY-MM-DD.html /home/clawdbot/clawd/data/presentations/
cp /tmp/trading-club-YYYY-MM-DD.html /home/clawdbot/clawd/apps/mission-control/public/
```

The Next.js app serves static files from `public/` automatically — no restart needed.

**Verify:** `curl -s -o /dev/null -w "%{http_code}" http://localhost:8888/trading-club-YYYY-MM-DD.html` should return 200.

Access via Tailscale: `http://100.113.44.24:8888/trading-club-YYYY-MM-DD.html`

### Step 6: Verify Visually

Navigate to the URL in the browser tool and click through all 6 slides to confirm rendering.

## Pitfalls
- **NEVER use stale/estimated market data** — Josh will catch it. Pull live prices from yfinance every time.
- If a member's trade expires the same day as the presentation, frame it as a case study, not a live trade idea.
- Note any significant price moves between when member submitted the trade and current price — flag the gap.
- Connect strategy slides (like 2022 playbook) to the member trades — don't let them float disconnected.

1. **Karan often sends corrections** — always check for "Re:" replies and use the LATEST version of the trade. In the Apr 9 session, his revised email changed the bailout level from $65 to $55.
2. **Ed's emails have legal disclaimers** — ignore the "Email Disclaimer" / confidentiality boilerplate at the bottom.
3. **himalaya search syntax** — uses `from X and after YYYY-MM-DD` format. Cannot combine with `or` — run separate queries per person.
4. **Market prices MUST be live** — Josh explicitly corrected stale/estimated prices (Apr 9 session). Pull live data via yfinance: `/usr/bin/python3 -c "import yfinance as yf; ..."`. IMPORTANT: use `/usr/bin/python3` (system Python 3.12) NOT the default `python3` (hermes venv is 3.11, yfinance installed in 3.12). For trade slides, use live prices (not email-submitted prices which may be stale by session day) and note any discrepancy.
5. **Discussion questions should contrast the two trades** — time horizon, catalyst type, structure choice, risk management approach, breakeven distance. Make them thought-provoking, not obvious. If a playbook/backtest section was added, tie Q1 back to it.
6. **The HTML template is self-contained** — all CSS inline, Google Fonts imported, JS for navigation at the bottom. No external dependencies.
7. **Slide count is flexible** — the 6-slide structure is the baseline, but Josh may request additional slides (e.g., "2022 Playbook" backtest data as slide 3). When adding slides, the JS counter auto-updates. Just make sure the initial counter text matches total (`1 / N`).
8. **When Ed's trade expires same-day or next-day** — frame it as a case study of structure/catalyst thinking rather than a live actionable idea. The group can't act on a trade that expires in 1 hour.

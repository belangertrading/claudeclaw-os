# Options Insider Alert Workflow

**Operator:** Hermes
**Service:** Options Insider (OI)
**Last updated:** 2026-04-07

This is the end-to-end operational playbook for producing OI trade alerts. Every step from Josh's signal to published alert + sheet update + activity log.

---

## North Star

Lead with what the member is feeling, connect the dots on WHY, and never pretend the market isn't happening around the trade. The voice is there. The conviction needs to come from context, not just pattern stats.

**System Language Rule:** The system is real. It's the edge. Reference it. But never let it replace the human element. System + context = conviction. System alone = mechanical.

---

## Pattern Reference

| Pattern | Direction | We Buy | TP | Exit Rule |
|---------|-----------|--------|-----|-----------|
| Bull Surge | BULLISH | CALLS | 40% gain | 60% loss |
| Bear Plunge | BEARISH | PUTS | 40% gain | 60% loss |
| U-Turn | BULLISH | CALLS | 50% gain | Exit day of expiration if TP not hit |
| U-Turn Velocity | BULLISH | CALLS | 50% gain | Exit day of expiration if TP not hit |
| Velocity | BULLISH | CALLS | 50% gain | 50% loss |
| Two-Way Trigger | NEUTRAL | CALLS + PUTS | 20% gain (combined) | Close after 10 trading days |

---

## PIPELINE

### STEP 1 — INTAKE

Josh says a pattern fired. Extract these fields (ask if missing):

| Field | Example | Required? |
|-------|---------|-----------|
| Ticker | TSLA | YES |
| Pattern | Bull Surge | YES |
| Strike(s) | $430 / $430/$450 spread | YES |
| Expiration | Feb 23, 2026 | YES |
| Strategy | Long Call / Call Spread / Strangle | YES |
| Entry price | $8.10 | YES |
| Type | C / P / C/P | YES |
| Pattern stats (W-L, total return %) | 7-1, 487% | YES |
| Last trigger + result | Nov, hit TP in 10 days | If available |
| Thesis notes / catalyst | Musk killed Model S/X | If provided |
| Spread alternative | Sell $450 call against it | If provided |

**Validation checks:**
- Pattern exists in the table above
- Direction matches: Bull Surge/U-Turn/Velocity → CALLS, Bear Plunge → PUTS, Two-Way → C/P
- TP/SL math matches pattern table (40%/60% for Bull Surge, etc.)
- Type field is C, P, or C/P (NEVER "CALL", "PUT", "call", "put")
- Entry date = today unless Josh says otherwise

### STEP 1B — READ GATE (Mandatory)

Your voice drifts between sessions. The reads are calibration.

```bash
# 1. Read voice reference
cat /home/clawdbot/clawd/skills/options-insider-alert/references/options-insider-voice.md

# 2. Read knowledge (published examples)
cat /home/clawdbot/clawd/skills/options-insider-alert/references/knowledge.md

# 3. Pull 2 most recent OI buy alerts from WordPress — NOTE: premium-post
sudo wp --path=/var/www/html --allow-root post list \
  --post_type=premium-post --posts_per_page=10 --post_status=publish \
  --tax_query='[{"taxonomy":"product-categories","field":"slug","terms":["options-insider"]}]' \
  --fields=ID,post_title --orderby=date --order=DESC
# Then read the 2 most recent BUY alerts
sudo wp --path=/var/www/html --allow-root post get <ID> --field=post_content

# 4. Read corrections log
cat /home/clawdbot/clawd/skills/options-insider-alert/data/corrections.log

# 5. Cross-reference HMT workflow for pipeline mechanics (post type, review format, etc.)
# skill_view('hmt-alert-workflow', 'references/full-workflow.md') — Steps 9-11
```

**If you haven't completed all reads in THIS session, you do not write.**

**Screenshots:** Trade screenshots are on Mac Studio at `~/Documents/Screenshots/`. Pull via SSH:
```bash
scp User@100.91.66.81:~/Documents/Screenshots/FILENAME /tmp/
sudo cp /tmp/FILENAME /var/www/html/charts/oi-TICKER-pattern-YYYYMMDD.png
sudo chown www-data:www-data /var/www/html/charts/oi-TICKER-pattern-YYYYMMDD.png
```

### STEP 2 — RESEARCH

Run these in parallel:

```bash
# Get current stock price
python3 /home/clawdbot/clawd/scripts/get_price.py TICKER

# Generate chart
python3 /home/clawdbot/clawd/scripts/generate-chart-v4.py TICKER --days 90 --sma 50,200 --annotation 'PATTERN_NAME'
```

Then research the thesis:
- What's happening with this stock RIGHT NOW?
- Why is the pattern firing at this moment?
- Find the ONE narrative that makes the timing feel inevitable
- Specific facts only: dollar amounts, dates, percentages, names
- If Bear Plunge: every sentence must describe DOWNWARD movement
- If Bull Surge/U-Turn: every sentence must describe UPWARD movement

**Check corrections log before writing:**
```bash
cat /home/clawdbot/clawd/skills/options-insider-alert/data/corrections.log
```

### STEP 3 — COMPUTE

Calculate TP and SL from entry price and pattern:

| Pattern | TP Formula | SL Formula |
|---------|-----------|-----------|
| Bull Surge | entry × 1.40 | entry × 0.40 |
| Bear Plunge | entry × 1.40 | entry × 0.40 |
| U-Turn / U-Turn Velocity | entry × 1.50 | Expiration exit |
| Velocity | entry × 1.50 | entry × 0.50 |
| Two-Way Trigger | entry × 1.20 (combined) | 10-day exit |

For spreads: verify spread width and max return calculation.

**Strike logic for the sheet:**
- Single leg: `leg2` = the strike. `leg1` = empty
- Spread: `leg1` = short strike, `leg2` = long strike
- Strangle/Straddle: `leg1` = call strike, `leg2` = put strike

### STEP 4 — DRAFT

Load these references before writing:
- Voice: `/home/clawdbot/clawd/skills/options-insider-alert/references/options-insider-voice.md`
- Knowledge: `/home/clawdbot/clawd/skills/options-insider-alert/references/knowledge.md`
- Phrase bank: `/home/clawdbot/clawd/skills/options-insider-alert/references/phrase-bank.md`
- Brand voice: `/home/clawdbot/clawd/skills/references/brand/voice.md`

Pull the 2 most recent published OI alerts of the same type (buy/sell) from WordPress:
```bash
# NOTE: post type is premium-post, not post
sudo wp --path=/var/www/html --allow-root post list --post_type=premium-post --post_status=publish --tax_query='[{"taxonomy":"product-categories","field":"slug","terms":["options-insider"]}]' --fields=ID,post_title,post_date --format=table --orderby=date --order=DESC --number=5
```

Then read them to match structure:
```bash
sudo wp --path=/var/www/html --allow-root post get POST_ID --field=post_content
```

Write the draft following the alert arc (see BUY/WIN/LOSS structures below).

### STEP 5 — QC

Run every check in `/home/clawdbot/clawd/skills/alert-qc.md`. Non-negotiable items:

- [ ] **"Why THIS ticker" is mandatory** — Silver thesis + AG trade = incomplete. The macro/sector context explains the catalyst, but the alert must also explain WHY this specific stock is the vehicle. For miners/producers: operating leverage, pure-play vs diversified, margin structure, upside to 52-week high. One dedicated paragraph. "When [commodity] moves, [ticker] moves harder" is NOT sufficient — that's a placeholder, not a thesis. (Added 2026-04-14 after Josh flagged AG alert had nothing about why AG specifically vs silver ETF or another miner.)
- [ ] **VERIFY EVERY FACTUAL CLAIM** — Do NOT invent price movements, percentages, or statistics. Pull actual data (yfinance historical, get_price.py) and confirm before writing. If you can't verify it, don't include it. This is the #1 rule. (Added 2026-04-10 after fabricating "BA down 10% in a week" when it was actually up 2.3%.)
- [ ] **QC must include price verification step** — Pull 1-week and 1-month actual price change from yfinance. Compare against any price movement claims in the draft. Flag and fix any discrepancy.
- [ ] Full contract in every trade mention (ticker, exp, strike, direction)
- [ ] Year is 2026
- [ ] Stock price verified via get_price.py
- [ ] TP/SL math correct per pattern table
- [ ] Pattern direction matches trade direction (no bullish language in PUT alerts)
- [ ] Zero em dashes anywhere
- [ ] **WP title % sign:** Use `wp eval 'wp_update_post(...)'` not `wp post update --post_title` (mangles % to %%)
- [ ] No cross-service language ("Here's what caught my attention" = HMT, NOT OI)
- [ ] "What This Trade Looks Like" present (buy alerts only)
- [ ] Custom bold headline (NOT "The Fundamentals Support the Pattern")
- [ ] Short punchy paragraphs, one thought each
- [ ] No fabricated facts
- [ ] **Self-critique before presenting:** Read the draft aloud. Kill three-item lists. Flag analyst-note phrasing. Ask "does this sound like a trader or a template?"
- [ ] **Day-of-week verification:** COMPUTE every day-of-week reference using datetime.strftime('%A'). Never guess. (Apr 14 2026: wrote "Thursday" when Apr 10 was Friday.)
- [ ] **"We" framing on ALL sell alerts:** No "you" anywhere. Same convention as HMT. Model after BP 4971, GLD 4919 gold standards.
- [ ] **Use Josh's context:** If Josh gave you macro framing, catalyst details, or positioning context (e.g. long+short divergence), it MUST be in the alert. Don't ignore the gold.
- [ ] **"Why this ticker" paragraph (commodity/miner trades):** "When silver moves, AG moves harder" is NOT sufficient. Every commodity or miner trade needs a dedicated paragraph on why this specific vehicle -- pure-play vs diversified, margin structure, operating leverage, runway to 52-week high. Generic leverage statements are not a thesis.
- [ ] **No information puke:** Each narrative beat gets its own paragraph. Opener especially -- do not cram peak price, drawdown %, geopolitical event, and macro catalyst into two sentences. Read it aloud. If you're breathless, break it up.
- [ ] **Research macro before writing commodity trades:** Pull actual supply/demand data before touching the draft. For silver: check supply deficit (Silver Institute data), solar/EV/industrial demand, gold/silver ratio. A one-line geopolitical thesis is never enough on its own.
- [ ] Structure matches most recent published alert of same type

### STEP 6 — CHART UPLOAD

```bash
# Copy chart to web-accessible directory
sudo cp /home/clawdbot/clawd/scripts/CHART_FILENAME.png /var/www/html/charts/UNIQUE_FILENAME.png
sudo chown www-data:www-data /var/www/html/charts/UNIQUE_FILENAME.png
```

Use a unique filename every time (Cloudflare caches aggressively). Format: `oi-TICKER-PATTERN-YYYYMMDD.png`

Confirm accessible: `https://yourdomain.com/charts/UNIQUE_FILENAME.png`

### STEP 7 — PRESENT TO JOSH

Send structured review message to **#trade-alerts** (channel ID: `1473066624993988739`):

```
📋 **[TICKER] OPTIONS INSIDER — DRAFT READY FOR REVIEW**

**Post:** [Alert title]
**Preview:** https://joshbelanger.com/?post_type=premium-post&p=[POST_ID]&preview=true

**Trade:** [Full action line]
**Pattern:** [Pattern name] — [W-L] — [X]% total returns
**TP:** $X (40%) | **SL:** $X (60%)

✅ to publish | ❌ to revise
```

**Do NOT dump the full alert text in Discord.** Draft lives on the site. Send the preview link.

Wait for explicit approval. Do not proceed without it.

**If Josh sends revisions:** Edit the WP draft, then run Post-Edit QC (re-read full draft, check for orphaned refs, verify all numbers consistent).

### STEP 8 — PUBLISH

**Create as DRAFT first. Never publish on create.**

**⚠️ Post type is `premium-post`, NOT `post`. All alerts use `premium-post`.**

```bash
# Write alert HTML to temp file first
cat > /tmp/oi-alert-content.html << 'ALERTEOF'
[alert HTML here]
ALERTEOF

# Create WordPress draft — NOTE: premium-post, not post
POST_ID=$(sudo wp --path=/var/www/html --allow-root post create /tmp/oi-alert-content.html \
  --post_type=premium-post --post_status=draft \
  --post_title="TRADE ALERT: TICKER Pattern Just Fired — X% Pattern" --porcelain)

# Set taxonomies
sudo wp --path=/var/www/html --allow-root post term set $POST_ID product-categories options-insider --by=slug
sudo wp --path=/var/www/html --allow-root post term set $POST_ID content-type trade-ideas-updates --by=slug

# Checkpoint
echo "{\"post_id\": $POST_ID, \"ticker\": \"TICKER\", \"service\": \"oi\", \"type\": \"buy\"}" > state/current-alert.json

# Josh approves → publish
sudo wp --path=/var/www/html --allow-root post update $POST_ID --post_status=publish
```

**Publishing triggers:** mu-plugin → n8n → email + SMS to subscribers.

**NEVER pull a published post back to draft.** That retriggers n8n and blasts subscribers again. Edits after publish get a dated correction note at the bottom.

### STEP 9 — SHEET UPDATE

After publish, update the tracking sheet.

**BUY entry:**
```bash
python3 /home/clawdbot/clawd/skills/trade-sheet-updater/scripts/update_sheet.py oi buy \
  --ticker TICKER \
  --signalType "Bull Surge" \
  --strategy "Long Call" \
  --expCycle "2/23/26" \
  --type C \
  --leg1 "" \
  --leg2 430 \
  --entryPrice "$8.10" \
  --tp "$11.34" \
  --sl "$3.24" \
  --entryDate "2/9/26" \
  --buyLink "https://site.com/POST_SLUG"
```

Or via webhook:
```bash
curl -L "https://script.google.com/macros/s/AKfycby8b-gFkH_UkfIhg0nYTCmCeagXfiJzXRFU-j3movoU9HE03K7qtR07mn5_5Wi7Fc1oTw/exec" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "buy",
    "ticker": "TSLA",
    "signalType": "Bull Surge",
    "strategy": "Long Call",
    "expCycle": "2/23/26",
    "type": "C",
    "leg1Strike": "",
    "leg2Strike": 430,
    "entryPrice": "$8.10",
    "takeProfit": "$11.34",
    "stopLoss": "$3.24",
    "entryDate": "2/9/26",
    "buyAlertLink": "https://site.com/post-slug"
  }'
```

**SELL entry:**
```bash
curl -L "https://script.google.com/macros/s/AKfycby8b-gFkH_UkfIhg0nYTCmCeagXfiJzXRFU-j3movoU9HE03K7qtR07mn5_5Wi7Fc1oTw/exec" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "sell",
    "ticker": "TSLA",
    "expCycle": "2/23/26",
    "exitPrice": "$11.34",
    "exitDate": "2/19/26",
    "sellAlertLink": "https://site.com/sell-post-slug"
  }'
```

**Duplicate prevention:** After POSTing, read the sheet back and count rows for that ticker + expCycle. If 2 rows exist, delete one immediately. The webhook can succeed on redirect responses.

**Sheet ID:** `1YyATKBbAanLe4xvL1C2CdLuGJFteyGnbCrYv1HjuSO8`

### STEP 10 — LOG ACTIVITY

```bash
./scripts/log-activity.sh
```

Log: service=oi, type=buy/sell, ticker=TICKER, post_id=POST_ID, timestamp.

---

## ALERT STRUCTURES

### BUY Alert Arc

```
HEADLINE:
TRADE ALERT: [TICKER] [Pattern] Just Fired — [X]% Pattern

OPENER (1-2 sentences):
Tension, contrast, or surprise. NOT a company description.
Find the most interesting angle for THIS specific trade.
- "Everyone's betting against [TICKER]. The [Pattern] says they're wrong."
- "This [sector] stock just triggered our [X]% pattern — for the second time."
- "The Supreme Court just handed [TICKER] a free pass."
Each alert finds its own voice. Don't copy openers across alerts.

PATTERN INTRO (2-3 sentences):
"[TICKER] is at $[PRICE] and our [Pattern] just fired — the one that catches
stocks [right before momentum takes off / right before the floor drops / etc]."

Company context sentence — match to trade type:
- Mispricing: "BAC is the second-largest bank in the U.S., and right now
  it's sitting on a classic post-earnings overreaction that's begging to snap back."
- Hidden catalyst: "MGM runs the most iconic portfolio on the Strip, and
  the market is treating it like a dead trade while BetMGM quietly turned its first profit."
- Re-trigger: Can skip intro if well-known ticker.
- Obscure ticker: Needs more company context.

PATTERN STATS (1 paragraph):
"This pattern is [X]-[Y] over the past [N] years with [X]% total returns.
Last time it triggered on [TICKER]? [Date]. [Result]."
"It just triggered again."

[CHART IMAGE — stock chart with pattern annotation]

[CUSTOM BOLD HEADLINE — the story in one line]
NOT "The Fundamentals Support the Pattern." Unique every time.
Examples: "Musk Just Killed Two Cars to Build Robots"
          "Coal to Gas — The Market Doesn't Buy It"
          "The Sell-the-News Trap"

THESIS (3-4 short paragraphs):
No bullets. One narrative thread. Specific facts, names, dollar amounts.
Find the ONE non-obvious catalyst that makes the timing feel inevitable.
First-person where it lands naturally.

TIE-IN (1 sentence):
Bridge thesis to action. Flexible per alert.
"When [Pattern] triggers with [specific fundamental factor] — that's when it delivers."

ACTION:
ACTION: Buy-to-Open [TICKER] [EXP] $[STRIKE] [Call/Put] at $[ENTRY] or better
Take Profit: $[TP] ([X]% gain)
Stop Loss: $[SL] ([X]% loss)

SPREAD ALTERNATIVE (optional):
"Want to maximize return and reduce cost? You can turn this into a [call/put]
spread by selling the [TICKER] [EXP] $[STRIKE] [Call/Put] against it."

CLOSING (2-3 sentences):
Days until expiration. Pattern conviction.
"Get in, get the [X]%, get out."

"What This Trade Looks Like"
[Options analysis screenshot]
```

### WIN Alert Arc (Result → Recall → ACTION)

**Do NOT copy verbatim. Structure is the guide — language must fit THIS trade.**

```
HEADLINE:
SELL ALERT: [TICKER] [Pattern] -- Up [X]%

RESULT (1-2 sentences):
We were right. TP triggered. Energy, not reporting.
"We were right and our take profit just triggered on [TICKER]."

RECALL (2-3 paragraphs, white space between each):
- When the pattern fired, what price, pattern record + total returns
- Why it worked ("short-term setup and the macro lined up" etc.)
- Stock move: "Right now, shares are trading around $X. Stock's up Y%."
- Options move (SEPARATE paragraph): "We bought the [contract] at $X. They're trading at $Y."
  Use "We bought" not "calls at $X" (reads like strike price)

THE NUMBER (standalone line — let it breathe):
"That's [X]% in [Y] trading days."

ACTION (bold):
ACTION: Sell-to-Close [TICKER] [EXP] $[STRIKE] [Call/Put] at $[CURRENT PRICE]
⚠️ Price = CURRENT TRADING PRICE from alert, NOT the TP target.
If calls are at $1.50, sell at $1.50 — not $1.33 or "$1.40 or better."

CLOSER:
"Great trade." (only closer for wins)
```

**Key rules for WIN sells:**
- Stock % vs options % contrast = the line members remember
- White space between every thought — let the win breathe
- Don't re-argue the thesis — just recall enough for members to remember why they got in
- Pattern record updates (was 2-0, now 3-0 with this win)
- "We" framing throughout, never "you"
- No em dashes — double dashes (--) in titles

⚠️ WIN alerts do NOT include "What This Trade Looks Like."

**Real example — UBS Bull Surge (5024, Apr 14 2026):**
We were right and our take profit just triggered on UBS.
Friday the Bull Surge fired when shares were at $41.58. A rare trigger -- 2-0 with 74% total returns over the past two years.
The short-term setup and the macro lined up.
Right now, shares are trading around $43. Stock's up 3%.
We bought the May 15, 2026 $42.50 calls at $0.95. They're trading at $1.50.
That's 58% in two trading days.
ACTION: Sell-to-Close UBS May 15, 2026 $42.50 Call at $1.50
Great trade.

### LOSS Alert Arc

```
HEADLINE:
[TICKER] — Cut This Loss
or: [TICKER] — Stop Loss Triggered
or: [TICKER] — Closing for a Loss

OPENER (1 sentence):
"Our system said [TICKER] was [about to rip higher / heading lower].
Instead, [what actually happened]."

NOTE: The improved framework says lead with feeling/context instead of
mechanical system language. System language is allowed here because it's
PAIRED WITH the honest "instead" beat. System + context = conviction.
System alone = mechanical.

CONTEXT (2-3 sentences):
What went wrong. Be specific: macro, sector, earnings, timing.
Include price at trigger, days elapsed, current price.

STOP LINE:
"Our system says to exit at [X]% loss. [Confirmation]. Time to act."

ACTION (bold):
ACTION: Sell-to-Close [TICKER] [EXP] $[STRIKE] [Call/Put] at $[PRICE] or better

MATH:
"We bought at $[ENTRY]. Now [the calls/puts] are around $[CURRENT] — down [X]%."

RECORD:
"[Pattern] is [X]-[Y] over the past [N] years with [X]% total returns.
This is the [Nth] loss."

Pull current record from the tracking sheet before writing this line.

CLOSER:
ONE honest sentence about why this specific trade failed.
"The pattern works." — ONLY if it fits. Don't force it.
"[Sector selloffs / macro reversals / etc.] don't care about patterns."
"Cut it. Clear the position. Next setup's already forming."

⚠️ LOSS alerts do NOT include "What This Trade Looks Like."
⚠️ LOSS alerts do NOT include spacer blocks between paragraphs.
⚠️ LOSS alerts do NOT include long thesis recaps or "I got this one wrong" openers.
```

---

## VOICE RULES

### OI Identity
Options Insider is a **momentum-triggered pattern service.** The pattern IS the edge. Language reflects this: momentum framing, not thesis/analysis framing.

### DO
- Reference historical pattern performance (W-L record, total returns)
- Custom bold headline for each alert's thesis section
- Direct, punchy sentences. First-person where it lands. "I'm not missing this one twice."
- End buy alerts with "Get in, get the [X]%, get out."
- Use "It just triggered again." as a signature beat
- Short paragraphs. Each beat = its own paragraph. Lines breathe.
- Offer spread alternatives after ACTION when applicable
- Rotate phrases from the phrase bank

### DON'T
- Use em dashes ( — ) anywhere in the alert. Period. Restructure the sentence.
- Use "Here's what caught my attention" (that's HMT)
- Use "The Fundamentals Support the Pattern" as a section header
- Use "The 48-Hour Window Just Opened" (that's 48HC)
- Reference dollar flow or institutional flow amounts (that's HMT)
- Use technical analysis language (support, resistance, moving averages)
- Invent facts. Every claim from Josh or a verified tool call.
- Use "Thesis dead" or "Our analysis was wrong" (we follow patterns, not theses)
- Copy openers from previous alerts. Each one finds its own angle.
- Write dense blocks. One thought per paragraph.

### Service Voice Fingerprint
These phrases are OI ONLY. Never use in HMT or 48HC:
- "What This Trade Looks Like"
- "It just triggered again."
- "Get in, get the [X]%, get out."
- Pattern names as conviction anchors (Bull Surge, Bear Plunge, U-Turn, etc.)
- "[X]-[Y] over the past [N] years with [X]% total returns"

These phrases are FORBIDDEN in OI:
- "Here's what caught my attention" (HMT)
- "The flow is…" / "$X million in flow" (HMT)
- "The 48-Hour Window Just Opened" (48HC)
- "The Fundamentals Support the Pattern" (generic, never use)

---

## REFERENCES

| Resource | Path |
|----------|------|
| Voice reference | `/home/clawdbot/clawd/skills/options-insider-alert/references/options-insider-voice.md` |
| Knowledge (published alerts) | `/home/clawdbot/clawd/skills/options-insider-alert/references/knowledge.md` |
| Phrase bank | `/home/clawdbot/clawd/skills/options-insider-alert/references/phrase-bank.md` |
| Brand voice | `/home/clawdbot/clawd/skills/references/brand/voice.md` |
| Alert QC checklist | `/home/clawdbot/clawd/skills/alert-qc.md` |
| Corrections log | `/home/clawdbot/clawd/skills/options-insider-alert/data/corrections.log` |
| Sheet updater CLI | `python3 /home/clawdbot/clawd/skills/trade-sheet-updater/scripts/update_sheet.py` |
| Sheet reference | `/home/clawdbot/clawd/skills/trade-sheet-updater/references/options-insider.md` |
| Chart generator | `python3 /home/clawdbot/clawd/scripts/generate-chart-v4.py` |
| Price checker | `python3 /home/clawdbot/clawd/scripts/get_price.py` |
| Activity logger | `./scripts/log-activity.sh` |
| Charts directory | `/var/www/html/charts/` |
| Review channel | `#trade-alerts` (ID: `1473066624993988739`) |

| Config | Value |
|--------|-------|
| WP taxonomy (product) | `options-insider` |
| WP taxonomy (content) | `trade-ideas-updates` |
| Sheet ID | `1YyATKBbAanLe4xvL1C2CdLuGJFteyGnbCrYv1HjuSO8` |
| Webhook | `AKfycby8b-gFkH_UkfIhg0nYTCmCeagXfiJzXRFU-j3movoU9HE03K7qtR07mn5_5Wi7Fc1oTw` |
| WP CLI prefix | `sudo wp --path=/var/www/html --allow-root` |
| Publish chain | mu-plugin → n8n → email + SMS |
---
name: hmt-alert-framework
description: Complete end-to-end HMT buy alert workflow — from Josh saying "we have flow" to published alert + sheet update + activity log. Covers the thinking framework (5 questions), research process, writing in WP block format, QC, publishing pipeline, and sheet webhook. Load this before writing ANY HMT alert.
tags: [trading, alerts, hmt, copywriting, belanger]
---

# HMT Alert Framework

## The North Star
Lead with what the member is feeling, connect the dots on WHY, and never pretend the market isn't happening around the trade. The voice is there. The conviction needs to come from context, not just pattern stats.

---

## Full Pipeline (11 Steps)

```
 1. INTAKE        Josh provides ticker + flow data
 2. READ GATE     voice.md + knowledge.md + 2 recent HMT buys from WP
 3. VERIFY        Live price, entry price, contract details
 4. RESEARCH      Catalyst (specific, 30-45 days out), market backdrop, sector
 5. THINK         Run 5-question framework — if any gate fails, STOP
 6. CHART         generate-chart-v4.py + flow screenshot from Josh
 7. WRITE         WP block format HTML, following narrative arc
 8. QC            alert-qc.md — every item, no skipping
 9. WORDPRESS     Create draft + set taxonomies (never publish on create)
10. REVIEW        Preview link → Josh in #trade-alerts → wait for approval
11. PUBLISH       Publish + sheet webhook + activity log
```

---

## Step 1: INTAKE

Josh provides the flow. Could be:
- Ticker + screenshot + "write this up"
- Ticker + contract details + thesis
- Just a ticker and a direction

Whatever he gives, extract: **ticker, contracts, strikes, expirations, premium, direction.**

If flow data is incomplete, check the scanner or ask. Don't guess contract counts or premium — subscribers who check will catch fabrications instantly.

---

## Step 2: READ GATE (Mandatory — No Exceptions)

Your voice drifts between sessions. You don't notice. Josh does. The reads are calibration.

```bash
# 1. Read voice reference
cat /home/clawdbot/clawd/skills/hot-money-alert/references/hot-money-voice.md

# 2. Read knowledge (published examples)
cat /home/clawdbot/clawd/skills/hot-money-alert/references/knowledge.md

# 3. Pull 2 most recent HMT buy alerts from WordPress
sudo wp --path=/var/www/html --allow-root post list \
  --post_type=premium-post --posts_per_page=10 --post_status=publish \
  --fields=ID,post_title --orderby=date --order=DESC
# Then read the 2 most recent BUY alerts
sudo wp --path=/var/www/html --allow-root post get <ID> --field=post_content
```

**If you haven't completed all 3 reads in THIS session, you do not write.**

---

## Step 3: VERIFY

Before writing a single word:

```bash
# Live stock price
python3 /home/clawdbot/clawd/scripts/get_price.py TICKER

# Entry price — Josh provides or check option chain
cd /home/clawdbot/clawd && source .venv/bin/activate && python3 -c "
import yfinance as yf
t = yf.Ticker('TICKER')
chain = t.option_chain('YYYY-MM-DD')
print(chain.calls[chain.calls['strike'] == STRIKE][['strike','lastPrice','bid','ask']])
"
```

**Required output before proceeding:**
```
VERIFIED: [TICKER] = $XXX.XX (live)
ENTRY PRICE: $X.XX (provided by Josh / live mid)
CONTRACT: [TICKER] [EXP] $[STRIKE] [Call/Put] (confirmed)
```

---

## Step 4: RESEARCH

```
1. web_search: "[TICKER] catalyst upcoming [month year]"
2. web_search: "[TICKER] earnings date" / "[TICKER] analyst upgrade"
3. web_search: "[sector] events [month year]" (conferences, product launches)
4. web_search: "market news today [date]" — what's moving the broad market
5. web_search: "[geopolitical event] stock market impact" — if relevant
6. Verify S&P/NASDAQ levels via Google Finance, not search snippets
```

**Three-Source Gate:** Every factual claim must come from (a) Josh's exact words, (b) a tool result in THIS session, or (c) a search you ran and can cite. Training data confidence is not a source. If you can't point to it, cut the sentence.

---

## Step 5: THINK — The 5-Question Framework

Every HMT buy alert must answer these in order. This is the thinking sequence — what needs to be true before you write anything.

### 1. THE FLOW — What's the unusual activity?
This is the data. Contract count, strike, expiration, average fill price, total premium. Is it in open interest? Multiple waves at the same strike = one thesis with conviction.

**Premium calculation: contracts × price × 100.** Always multiply by 100. Run the math before writing any dollar amount.

### 2. THE CATALYST — WHY are they betting NOW?
Not "AI is growing." The specific event, earnings, product launch, contract that's 30-45 days out. Competitor results that validate the thesis. Analyst upgrades with specific targets. **If you can't name it, the alert isn't ready.**

### 3. THE BACKDROP — What's the market doing TODAY?
What's the member going to see when they open their portfolio? If the world is on fire and you're telling them to buy calls, you better acknowledge the fire. Verify claims against live data — don't fabricate market stats.

### 4. THE CONTRARIAN FRAME — Connect 1, 2, and 3.
"$X million says [thesis] despite [chaos]." That's the conviction. That's what separates this from every other flow alert service. If market is calm, frame the conviction around the catalyst window.

### 5. THE LOSS FRAMEWORK — If this doesn't work, here's what broke.
Member never feels dumb. They understand the thesis so they OWN the trade. "If it doesn't work, the thesis was X and X didn't deliver." Include TP/SL with the 40%/60% framework.

---

## Step 6: CHART

```bash
cd /home/clawdbot/clawd && source .venv/bin/activate && \
python scripts/generate-chart-v4.py TICKER --days 90 --sma 50,200
```

Output URL: `https://joshbelanger.com/charts/[filename].png`

**Flow chart:** Josh saves screenshots to Mac Downloads as `OptionAlert_TICKER.jpeg`. Pull via SSH, upload to `/var/www/html/charts/`, set ownership:
```bash
sudo chown www-data:www-data /var/www/html/charts/FILENAME
```

---

## Step 7: WRITE — The Narrative Arc

**Service identity:** Hot Money Trader is a flow-following service. Lead with dollar amounts and unusual activity signals. NOT pattern-driven (that's OI).

### HMT Buy Alert Structure

**HOOK** — Flow $ + stakes. Dollar amount leads. Always.
- "$4.2 million just dropped on [TICKER] calls"
- "Someone just dropped $X million betting [TICKER] pushes higher in the next X days."
- "And if they're wrong, they lose everything." (optional)

**SETUP** — Company + price + stock chart.
- Company context: 1-2 sentences. What they do + why it matters for THIS trade.
- Price: "Shares are trading at $X"
- Stock chart image goes here.

**PIVOT** — "Here's what caught my attention:" + flow chart image.
- This line is the turn. Everything before = setup. Everything after = story.

**STORY** — Flow details + catalyst/thesis. This is where conviction lives.
- Flow details first: contracts, strikes, expirations, what makes it unusual.
- Then the WHY — the specific catalyst. This comes AFTER the flow.
- The research layer is what separates good from great. Find the ONE specific detail that makes a subscriber think "oh, that's why someone bet millions."
- 2-4 paragraphs. One idea each. Let it breathe.

**ACTION** — Bold. Full contract. TP/SL.
```
ACTION: Buy-to-Open [TICKER] [EXP] $[STRIKE] [Call/Put] at $[PRICE] or better
Take Profit: $[TARGET] (40% gain)
Stop Loss: $[STOP] (60% loss)
```

**CONVICTION CLOSE** — Reinforce the flow signal. Tie back to the contrarian frame.
- Not "the system said." Conviction from context.
- "$28.5 million in fresh premium. Single session. Single direction."

### System Language Rule
The system is real. It's the edge. Reference it — but never let it replace the human element.
- ❌ "The system said take it. We take it." — mechanical.
- ❌ "Our system said AMD was setting up for a quick drop." — system as opener, no feeling.
- ✅ "The system flagged this at $88. Oil just hit $111. We're taking the money." — system gets credit, conviction from context.
- ✅ "Bear Plunge triggered at $193.70. Semis were rolling over, export headwinds building." — system + WHY.

### WP Block Format
```html
<!-- wp:paragraph -->
<p>Alert text here</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/FILENAME" alt="Description" style="width:800px"/></figure>
<!-- /wp:image -->
```

### Voice Rules (from 30-alert corpus analysis)
- Average 9 words/sentence. 52% of sentences ≤8 words.
- 48% of paragraphs ≤15 words. Dense blocks are the exception.
- 3-5 standalone punchy lines per alert: "That money knew something." "Same direction. Same day."
- Start paragraphs with "And", "That's", "But", "When" — direct kicks.
- Use -- (double hyphens) not em dashes.
- "We" framing in body. "You" only in subscriber celebration (win alerts).

### Service Voice Fingerprint
**HMT phrases (use these):**
- "Here's what caught my attention:" (before flow chart)
- "$X million just dropped on [TICKER] calls"
- "That's a signal worth following."
- "They're not hedging. They're positioning."

**BANNED (other services):**
- ❌ "What This Trade Looks Like" (OI)
- ❌ Pattern names: Bull Surge, Bear Plunge, U-Turn (OI)
- ❌ "The 48-Hour Window Just Opened" (48HC)
- ❌ Insurance analogies (48HC)
- ❌ "Our system says to exit" (OI)

---

## Step 8: QC

Run `/home/clawdbot/clawd/skills/alert-qc.md` — every item. Not a mental check. Run the commands.

Key checks:
- [ ] Full contract specified everywhere (ticker, exp, strike, direction)
- [ ] All temporal claims verified ("overnight", "last week" — did you check?)
- [ ] Year is 2026. Expiration makes sense.
- [ ] Stock price verified via get_price.py
- [ ] TP/SL math: TP = entry × 1.40, SL = entry × 0.40
- [ ] No banned words (voice.md)
- [ ] No service voice bleed (no OI or 48HC phrases)
- [ ] No em dashes
- [ ] Premium dollar calc correct (contracts × price × 100)
- [ ] **SELL ALERTS:** Exit price is LIVE (not stale TP target)
- [ ] **SELL ALERTS:** No "you" anywhere — publishers exception, "we" framing only
- [ ] **SELL ALERTS:** Profit language is editorial ("good spot to manage profits") not directive ("locking in profits")
- [ ] **SELL ALERTS:** Title % matches body % — re-check after ANY content edit
- [ ] **SELL ALERTS:** Energy matches the win size — 100% overnight should FEEL like it

---

## Step 9: WORDPRESS

```bash
# Write alert to temp file, then create draft
POST_ID=$(sudo wp --path=/var/www/html --allow-root post create /tmp/alert-content.html \
  --post_type=premium-post --post_status=draft \
  --post_title="BUY ALERT: [TITLE]" --porcelain)

# Set taxonomies
sudo wp --path=/var/www/html --allow-root post term set $POST_ID content-type trade-ideas-updates --by=slug
sudo wp --path=/var/www/html --allow-root post term set $POST_ID product-categories hot-money-trader --by=slug
```

**Never publish on create. Always draft first.**

---

## Step 10: REVIEW

Send to Josh in `#trade-alerts` (ID: `1473066624993988739`):

```
📋 **[TICKER] HOT MONEY TRADER — DRAFT READY FOR REVIEW**

**Post:** [Alert title]
**Preview:** https://joshbelanger.com/?post_type=premium-post&p=[POST_ID]&preview=true

**Trade:** [Full action line]
**Flow:** $[X]M on [strikes/expiry] — [key signal]
**TP:** $X (40%) | **SL:** $X (60%)

✅ to publish | ❌ to revise
```

Wait for explicit approval. Do not proceed without it.

---

## Step 11: PUBLISH

On approval — publish + sheet + log. **Do NOT create a new post. The draft already exists.**

```bash
# 1. Publish
sudo wp --path=/var/www/html --allow-root post update $POST_ID --post_status=publish

# 2. Get URL
sudo wp --path=/var/www/html --allow-root post get $POST_ID --field=url

# 3. Update HMT sheet via Google Apps Script webhook
# Webhook: AKfycbz4o0eF_rqmqPwERnu61Yt-mw2QI_pPOGu-Yh5to61bdzCpJOwVaudkmxrPA0v9X42t
# Sheet: 12VsTbwaABgz8rLfDJQVm2n1YE-n5SzLUhFM4igpJH5o
#
# BUY payload:
# {
#   "action": "buy",
#   "ticker": "TICKER",
#   "entryDate": "MM/DD/YYYY",
#   "strategy": "Long Call" | "Call Spread" | etc,
#   "expCycle": "M/DD/YYYY",
#   "shortStrike": STRIKE_NUM (spread only),
#   "longStrike": STRIKE_NUM,
#   "type": "C" | "P",
#   "entryPrice": PRICE_NUM,
#   "takeProfit": TP_NUM,
#   "stopLoss": SL_NUM,
#   "buyAlertLink": "URL"
# }
#
# SELL payload:
# {"action":"sell", "ticker":"TICKER", "exitPrice":NUM, "exitDate":"MM/DD/YYYY", "sellAlertLink":"URL"}
#
# Use redirect curl pattern from trade-sheet-updater/SKILL.md
# Verify the sheet row after posting — read it back, confirm 1 row, correct fields.

# 4. Also available: CLI script
python3 /home/clawdbot/clawd/skills/trade-sheet-updater/scripts/update_sheet.py \
  hm buy TICKER "Long Call" "M/DD/YYYY" C STRIKE ENTRY_PRICE TP SL --entry-date "MM/DD/YYYY" --buy-link "URL"

# 5. Log activity
cd /home/clawdbot/clawd && ./scripts/log-activity.sh \
  "Published [TICKER] Hot Money Trader buy alert (Post [POST_ID])" "collaborative"
```

Publishing triggers mu-plugin → n8n → email + SMS to all HMT subscribers automatically.

---

## Sell/Loss Alert Framework

### The Rule: Lead with feeling, not mechanics.

❌ "Our system said [TICKER] was about to rip. Instead, it bounced."
✅ "Yesterday this trade was up 30-40%. Fifteen minutes before the bell, it needed to confirm. It slipped."

### Loss Alert Arc:
```
[THE GUT PUNCH]  — Lead with the frustrating near-miss or the pain.
[THE MARKET]     — Why today specifically. No reason IS a reason.
                   Never fabricate a reason.
[THE EXIT]       — Price, days left, distance from strike. Factual.
[ACTION]         — Bold. Sell-to-Close at $X or current prices.
[THE MATH]       — Entry → exit, % loss. One line.
[THE SETUP]      — 2-3 sentences. Why the trade made sense. No apologizing.
[HONEST CONTEXT] — Acknowledge tough stretches. Validate what they're seeing.
[CLOSE]          — Forward motion. Rotate closers from phrase-bank.md.
```

### Forbidden in Loss Alerts:
- "I got this one wrong" opener
- "Our system said X. Instead, Y." as opener
- Long thesis recap
- "That stings"
- Charts
- Fabricated stats or reasons
- "Punt it. Next setup is coming." (overused — rotate)

### Win Alert Arc:
```
[THE MOMENT]       — Put the member in the feeling. They woke up to this. Lead with the
                     stock move + what the spread did. Energy matches the win size.
                     "MU gapped to $415. The spread ripped to $26. Over 100% overnight."
[ENTRY RECALL]     — What the market felt like when we entered. Tension, uncertainty,
                     what was scary. Then the flow that cut through the noise.
                     Spell out FULL CONTRACT — "May 1st $400/$450 call spread at $11.50"
                     NOT "followed the money in at $11.50" (reader doesn't know what that means).
[THE CATALYST]     — What broke in our favor. Ceasefire, earnings, whatever moved it.
                     Be specific about timing — "last night, 11th hour" not "this morning."
[PROFIT MGMT]     — WHY we're taking the trade off. Not "don't be greedy."
                     Frame as: "in a good spot to manage profits," "earned the right to
                     take a profit." If still bullish, "manage the position by taking profits,
                     then adjust strikes or expiration." This is editorial, not directive.
[ACTION]           — Bold. Full contract. "at $XX or current prices."
                     Use LIVE spread prices, not the original TP target if price has moved past it.
[MATH + SIGNAL]    — Entry → exit, % gain. One line. Get CREATIVE with the journey
                     if the trade had a wild ride: "In at $5.90. Rode it to target,
                     watched it fall apart, and rode it back. Out at $8.26. 40%."
                     Then the WHY line: "The flow knew before the headline did."
[CLOSER]           — Short. "Great trade." can be the ONLY closer — doesn't always
                     need "More coming. Stay ready." Less is more. Vary it.
### Win Alert Arc:
```
[THE MOMENT]       — Put the member in the feeling. They woke up to this.
                     Lead with stock move + what the spread did.
                     Energy matches the win size — 100% overnight should FEEL like it.
[ENTRY RECALL]     — What the market felt like when we entered. The tension, uncertainty.
                     Then the flow that cut through the noise.
                     Spell out FULL CONTRACT — "May 1st $400/$450 call spread at $11.50"
                     NOT "followed the money in at $11.50" (vague, reader doesn't know what).
[THE CATALYST]     — What broke in our favor. Be specific about timing.
                     "Last night, 11th hour" not "this morning."
[PROFIT MGMT]      — WHY we're taking the trade off. NOT "don't be greedy."
                     "In a good spot to manage profits." "Earned the right to take a profit."
                     If still bullish: "manage the position by taking profits, then adjust
                     strikes or expiration." This is EDITORIAL, not directive.
[ACTION]           — Bold. Full contract. "at $XX or current prices."
                     Use LIVE spread price — not the original TP target if price has moved.
[MATH + SIGNAL]    — Entry → exit, % gain. One line. Get CREATIVE for wild rides:
                     "In at $5.90. Rode it to target, watched it fall apart, and rode it back.
                     Out at $8.26. 40%." Then the signal: "The flow knew before the headline did."
[CLOSER]           — "Great trade." can be the ONLY closer. Doesn't always need
                     "More coming. Stay ready." Less is more. Vary it.
```

### Win Alert Rules (Apr 8 2026 — learned through 6 rounds of MU revisions):
1. **Get LIVE spread price BEFORE writing.** MU TP was $16.10 but spread was at $20-26. Writing the stale target looks wrong to members.
2. **Energy must match the win.** Nearly 100% overnight written like a routine 40% = robotic.
3. **No "you" — publishers exception.** "We were already in" not "You positioned before the crowd."
4. **No directive profit language.** "Locking in profits" = advice. "Good spot to manage profits" = editorial.
5. **White space — let it breathe.** Each beat gets its own wp:paragraph. Dense blocks kill energy.
6. **Specifics, not assumptions.** "May 1st $400/$450 call spread at $11.50" — not "we bought at $11.50."
7. **Title must match body after edits.** If you change % or price in body, verify title matches immediately.
8. **Sheet updater syntax is POSITIONAL:** `hm sell TICKER price "date" "url"` — no flags like --exit-date.

## Cross-Service Review Findings (Apr 7 2026)

1. Loss alerts consistently bury the human moment — lead with feeling, not mechanics
2. OI buy alerts lean too hard on pattern stats, not enough on catalyst
3. "Punt it / Cut it" closers getting repetitive — rotate using phrase-bank.md
4. Market backdrop is inconsistent — should be mandatory on EVERY alert, buy or sell
5. The strongest alerts share the same DNA: backdrop → conviction → honest risk

---

## Key References

| Item | Location |
|------|----------|
| Voice reference | /home/clawdbot/clawd/skills/hot-money-alert/references/hot-money-voice.md |
| Knowledge/examples | /home/clawdbot/clawd/skills/hot-money-alert/references/knowledge.md |
| Phrase bank | /home/clawdbot/clawd/skills/hot-money-alert/references/phrase-bank.md |
| Corrections log | /home/clawdbot/clawd/skills/hot-money-alert/data/corrections.log |
| Brand voice | /home/clawdbot/clawd/skills/references/brand/voice.md |
| QC checklist | /home/clawdbot/clawd/skills/alert-qc.md |
| Price tool | /home/clawdbot/clawd/scripts/get_price.py |
| Chart tool | /home/clawdbot/clawd/scripts/generate-chart-v4.py |
| Sheet updater | /home/clawdbot/clawd/skills/trade-sheet-updater/scripts/update_sheet.py |
| WP taxonomy | hot-money-trader (product-categories), trade-ideas-updates (content-type) |
| Sheet ID | 12VsTbwaABgz8rLfDJQVm2n1YE-n5SzLUhFM4igpJH5o |
| Webhook | AKfycbz4o0eF_rqmqPwERnu61Yt-mw2QI_pPOGu-Yh5to61bdzCpJOwVaudkmxrPA0v9X42t |
| Chart dir | /var/www/html/charts/ → https://joshbelanger.com/charts/ |

## Gold Standard Examples

- **Buy**: MU $104M alert (Post 5002) — Iran/macro chaos, Computex catalyst, contrarian frame, honest risk.
- **Buy**: STM $1M alert — Back-to-back flow, chip downcycle thesis, "That's a signal worth following."
- **Buy**: TSM $8.2M + $17.5M — Short-term + long-term flow convergence, spread structure.
- **Win sell**: SCCO 100% — Flow recall, subscriber celebration, "we came for a trade, not a thesis."
- **Loss sell**: WMT (Post 5003/5004) — "Yesterday this was up 30-40%." Lead with feeling.
- **Win sell**: MU 74% overnight (Post 5005) — Gapped on ceasefire, led with the moment, specific contract recall, editorial profit mgmt framing, white space. 6 revision rounds taught: get live spread price, match energy to win size, no "you", no directive language, verify title matches body.
- **Win sell**: DELL 40% rollercoaster (Post 5006) — Hit target in 2 days, 17% drawdown over 4 sessions, ceasefire brought it back. Creative math line: "In at $5.90. Rode it to target, watched it fall apart, and rode it back. Out at $8.26. 40%." "Earned the right to take a profit." "Great trade." as sole closer.

---

## Pitfalls

1. **Don't fabricate market data.** Verify LIVE. "S&P down 10%" was wrong once — it was actually at 6,583. Use Google Finance, not search snippets.
1b. **"Down for no reason" is more honest than inventing a catalyst.** WMT sell alert (Apr 7): stock was down 3.52% with zero news. That IS the story — the market is rotating through everything. Don't fabricate a reason when there isn't one.
2. **Don't bury the catalyst.** MU v1 had $104M in flow but never said WHY.
3. **Don't ignore the macro.** If Iran is getting bombed and you're saying buy calls, acknowledge it.
4. **Generic context kills conviction.** "Samsung Q1 profit up 8x" is data. "Samsung just confirmed the supercycle — these buyers already knew" is conviction.
5. **Premium calc: contracts × price × 100.** Always multiply by 100.
6. **Don't skip the reads.** Every time reads were skipped → 3-6 revision rounds. Every time.
7. **Post-edit: re-read the FULL draft.** USO had 90% in title, 76% in body after an edit.
8. **Never publish on create.** Always draft first. Publishing triggers email blast.
9. **Don't overdramatize OR underdramatize the market.** "Market on edge" ≠ "market falling apart." Use Josh's exact characterization.
10. **Verify catalyst timing.** "11th hour last night" ≠ "this morning." Members know when the news broke.
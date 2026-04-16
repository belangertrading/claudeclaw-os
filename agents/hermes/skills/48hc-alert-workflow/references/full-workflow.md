# 48-Hour Cashflow Alert Workflow

**Operational playbook. Every step numbered. Every command copy-pasteable.**

This is the complete pipeline from "Josh provides ticker + setup" to "alert published + sheet updated + activity logged." Premium collection service — selling overpriced fear on put spreads. 48-hour holding period (typically Wednesday entry → Friday 4 PM expiration). Target: 25% return.

---

## Pipeline Overview

```
Step 0: Hard Gate — Date, Day of Week, Price, Contract
Step 1: Load Voice + References + Corrections
Step 2: Verify Price + Entry + Generate Chart
Step 3: Research (web search for current context)
Step 4: Write Alert (buy / win / loss / early exit)
Step 5: Henry QC — Structural Comparison
Step 6: Run alert-qc.md
Step 7: Create WordPress Draft + Set Taxonomies
Step 8: Post Preview to #trade-alerts
Step 9: Wait for Josh Approval
Step 10: Publish + Sheet Update + Activity Log
```

---

## Step 0: Hard Gate — Date, Day of Week, Price, Contract

48HC alerts are time-sensitive. Wrong date = subscribers enter with wrong math. This gate takes 10 seconds and prevents correction emails to thousands.

```bash
# Get current date/time
date

# Get live price
python3 /home/clawdbot/clawd/scripts/get_price.py TICKER
```

**Print this block before doing anything else:**

```
DATE/TIME: [current date/time]
TICKER:    $XXX.XX (live)
CONTRACT:  [TICKER] [EXP — WRITE THE DAY OF WEEK] $[HIGH]/$[LOW] Put Spread
```

**Example:** `CONTRACT: FLY Mar 27 (Friday) $25.50/$25.00 Put Spread`

Writing the **day of week** makes a wrong expiration date impossible to miss visually. The Mar 25 vs Mar 27 FLY error was caught this way.

**Verify the premium math immediately:**
```
Premium / Capital at Risk = 0.25
(Sell Strike - Buy Strike) - Premium = Capital at Risk
Example: Sell $21, Buy $20.50 for $0.10 → ($0.50 - $0.10) = $0.40 risk → $0.10 / $0.40 = 25% ✓
```

If the math doesn't hit 25%, flag Josh before proceeding. If Josh says to proceed anyway (e.g., wide bid-ask makes tighter strikes unfillable), write the actual return percentage throughout the alert. Use discretion framing (see Gotchas: Apr 8).

---

## Step 1: Load Voice + References + Corrections

**Read all of these. Every session. No exceptions.**

```
1. Read corrections log:
   /home/clawdbot/clawd/skills/48hr-cashflow-alert/data/corrections.log

2. Read voice reference:
   /home/clawdbot/clawd/skills/48hr-cashflow-alert/references/48hr-cashflow-voice.md

3. Read knowledge/examples:
   /home/clawdbot/clawd/skills/48hr-cashflow-alert/references/knowledge.md

4. Read phrase bank:
   /home/clawdbot/clawd/skills/48hr-cashflow-alert/references/phrase-bank.md

5. Pull 2-3 most recent published alerts of SAME TYPE from WordPress:
```

```bash
# List recent 48HC alerts
sudo wp --path=/var/www/html --allow-root post list \
  --post_type=premium-post \
  --posts_per_page=10 \
  --post_status=publish \
  --fields=ID,post_title \
  --orderby=date --order=DESC

# Read specific alert content
sudo wp --path=/var/www/html --allow-root post get <ID> --field=post_content
```

**Why this matters:** Your voice drifts toward HMT excitement between sessions. Published alerts on WordPress are the source of truth — they reflect Josh's latest edits. knowledge.md may be weeks old.

---

## Step 2: Verify Price + Entry + Generate Chart

### Live stock price
```bash
python3 /home/clawdbot/clawd/scripts/get_price.py TICKER
```

### Entry price
- If Josh provided entry price → use it: `ENTRY PRICE: $X.XX (provided by Josh)`
- If no entry price → check option chain live. A few cents changes the 25% math.

### Generate branded chart
```bash
cd /home/clawdbot/clawd && source .venv/bin/activate && python scripts/generate-chart-v4.py TICKER --days 90 --sma 50,200
```

Chart outputs to `/var/www/html/charts/` → URL: `https://joshbelanger.com/charts/[filename].png`

### Confirm output (required before writing)
```
VERIFIED: [TICKER] = $XXX.XX (live)
ENTRY PRICE: $X.XX (provided by Josh / live mid)
CHART: https://joshbelanger.com/charts/[filename].png
25% MATH: $X premium / $X risk = 25% ✓
```

**If these lines are missing, Step 2 is incomplete. Stop.**

---

## Step 3: Research — Mandatory Web Search

```
1. web_search: "[TICKER] stock news today"
2. web_search: "market news today [date]" — macro environment
3. web_search: "[any company/event you plan to reference] [date]"
```

**Three-Source Gate:** Every factual claim must come from (a) Josh's exact words, (b) a tool result in THIS session, or (c) a search you ran and can cite. Training data confidence is NOT a source.

This includes temporal claims. "Overnight," "about an hour," "last week," "futures reversed" are factual claims. If you didn't check the timestamp, don't write the time reference.

---

## Step 4: Write Alert

Output in WordPress block format (`<!-- wp:paragraph -->`).

### Alert Arc: BUY ALERT (Premium Collection Setup)

**Title:** `TRADE ALERT: [TICKER]'s [Situation] Setup – X% in 48 Hours`
(Use actual return %. Usually 25%, but may be lower on wide bid-ask names.)

**Narrative arc (not a checklist — same arc, different story every time):**

```
OPENING (3 paragraphs, 3 jobs, no overlap)
  Para 1 — What's happening with this stock right now
  Para 2 — What the market is getting wrong (system + context)
  Para 3 — What we're doing + the return

"The 48-Hour Window Just Opened" (h2 section heading)
  [Stock chart image]

COMPANY + PRICE + EXPECTED MOVE
  1-2 sentences on what they do + why it matters for THIS trade
  "Right now [TICKER] is at $X. The options market is pricing in a $X move by [day]."

THE SETUP (2-3 paragraphs, each one idea)
  Why the fear is overpriced — the research layer
  Find the ONE SPECIFIC detail that makes the mispricing obvious

ACTION BLOCK
  ACTION: Sell-to-Open [TICKER] [EXP] $[HIGH] Put / Buy the $[LOW] Put at $[CREDIT] credit
  • Premium Collected: $X per spread
  • Return: X% if [TICKER] stays above $[HIGH] through [day]

RISK (woven into narrative — NO label, NO header, NO "The Risk:", NO bullets)
  One paragraph naming the specific event that could break the trade
  Plain English. No statistical language.

CLOSING THESIS
  "X% return for 48 hours of patience and probabilities."

"What This Trade Looks Like" (h2 section heading)
  [Options analysis chart]
```

**Opening line options (match the situation):**
- Earnings: "[TICKER] reports after the close today. $X expected move on a $X stock."
- Post-crash: "[TICKER] is down X% in X days. The options market is bracing for another X% drop."
- Post-rally: "[TICKER] just ripped X% in one session. That creates mispricing."
- Mystery fear: "I can't find what they're bracing for."

**System language rule:** "48HC system flagged the puts as overpriced" is fine. System alone = mechanical. Always pair with context.

**ACTION block — INCLUDE:**
- Premium Collected: $X per spread
- Return: X% if [TICKER] stays above $X through [day]

**ACTION block — NEVER INCLUDE:**
- ~~Entry: $0.10 credit minimum~~
- ~~Capital Required: $X per spread~~
- ~~Max Loss: $X per spread~~

**Image block format:**
```html
<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/FILENAME.png" alt="Description" style="width:800px"/></figure>
<!-- /wp:image -->
```

Never upload to WP media library. Always use `/charts/` URL directly. Always `style="width:800px"`.

---

### Alert Arc: WIN UPDATE

**Title:** `TRADE UPDATE: [TICKER] – [Win Celebration from Phrase Bank]`

**Arc:** Result first → What happened → Current price → Math → "No action needed" → Record → Close.

Matter-of-fact. The system worked. Fear was overpriced. We collected.

**Creative Rules (Josh-approved Apr 11 2025):**
- **Length matches drama:** Boring hold where stock barely moved = short (4-5 lines). Wild ride with real arc = tell the story, 2+ extra sentences.
- **Repeat play callouts:** If we traded the same ticker recently, call it out: "Second time we've sold fear on this name in two weeks. Both times, the fear expired worthless."
- **Record milestones:** Frame as recovery/consistency, not first-time celebration: "Back above 80% with 64 real trades" — builds consistency narrative as the track record grows.
- **Rotate closers:** Don't use "Back Wednesday" every time. Rotate: "Wednesday. Fresh setup." / "See you Wednesday." / "Back Wednesday."

```
OPENER
  Result line. "Another one. 25% in 48 hours." or similar from phrase bank.

WHAT HAPPENED
  What the stock did. Earnings result if applicable. Brief.

CURRENT PRICE + PUTS STATUS
  "[TICKER] is at $X. Both puts expire worthless at 4 PM today. We keep every penny."
  OR "[TICKER] is at $X. Our $X puts never got touched."
  (NEVER "you keep" — sounds like individual investment advice. Always "we.")

MATH (one line)
  "$X on $X risk. 25% in 48 hours."

NO ACTION NEEDED
  "No action needed." (explicit — subscribers panic without it)

RECORD (pull LIVE from sheet — never from memory)
  "**48-Hour Cashflow Record: XX-XX (XX% win rate)**"

CLOSER
  "Questions about this trade or what I saw in the setup? Just reply — I'm here."
  Rotate closer (see Creative Rules above).
```

**Victory lap rule:** Don't over-celebrate. "Back Wednesday." Not "Another perfect read! The system keeps delivering!" The record speaks for itself.

---

### Alert Arc: LOSS UPDATE

**Title:** `TRADE UPDATE: [TICKER] — Expiration Max Loss`

**Arc:** Bad news → What we did → What went wrong → Net loss (one line) → Insurance framing → "No action needed" → Record → Close.

Short and honest. Insurance framing helps.

```
OPENER
  "Bad news..." or "Unfortunately, the market beat us this week."
  NOT "I got this one wrong."

WHAT HAPPENED
  What we did, what went wrong. Brief.

NET LOSS (one line — no bullet breakdown of legs)
  "We collected $X but lost the full $Y risk."

INSURANCE FRAMING
  "This is why we don't sell naked options. We hedge every time.
   Without that $X put, the loss would be multiples.
   The spread structure capped the damage."

NO ACTION NEEDED
  "No action needed. Your broker handles it automatically."

RECORD (pull LIVE from sheet)
  "**48-Hour Cashflow Record: XX-XX (XX% win rate)**"

TRADE TRACKER LINK

CLOSER
  "Back Wednesday with a fresh setup."
```

**Gold standard loss alerts:** FLY 4991, GAP 4927, RCAT 4982. Read before writing any loss alert.

---

### Alert Arc: EARLY EXIT

```
WHAT CHANGED
  New market conditions, catalyst shift

WHY EXIT EARLY
  Specific reason

ACTION (bold)
  BUY-TO-CLOSE [STRIKES] put spread at $[PRICE] or better

P/L CALCULATION
  Collected $X, buying back for $Y, locks in $Z profit/loss

CLOSER
  "The trade worked. Conditions changed. We adapt."
  OR "Better to take a small loss now than risk a bigger one."
```

---

## Step 5: Henry QC — Structural Comparison

Pull 2 most recent published 48HC alerts of SAME TYPE from WordPress. Read them. Compare your draft line by line.

```bash
sudo wp --path=/var/www/html --allow-root post list \
  --post_type=premium-post \
  --posts_per_page=10 \
  --post_status=publish \
  --fields=ID,post_title \
  --orderby=date --order=DESC

sudo wp --path=/var/www/html --allow-root post get <ID> --field=post_content
```

**Check against published structure:**
- [ ] Buy alert: Opening 3 paras (3 jobs, no overlap)?
- [ ] Win/loss alert: Opens with result, NOT setup recap?
- [ ] Dollar math correct?
- [ ] Win rate record matches sheet?
- [ ] "No action needed" on expiring winners/losers?
- [ ] Entry date and spread strikes correct?
- [ ] Trade Tracker link included?
- [ ] WordPress block format throughout?
- [ ] No section headers in body (anti-robot-voice)?
- [ ] Risk woven into narrative, no label?
- [ ] Em dashes: opening line OK, body FORBIDDEN?

Fix before proceeding.

---

## Step 6: Run alert-qc.md

```
Read and execute: /home/clawdbot/clawd/skills/alert-qc.md
```

**48HC-specific QC additions:**
- [ ] No HMT excitement language (aggressive conviction, flow language, "Here's what caught my attention")
- [ ] No OI pattern language (Bull Surge, Bear Plunge, U-Turn)
- [ ] No labeled risk sections ("The Risk:", "Here's The Risk")
- [ ] No bullet breakdowns in body
- [ ] No statistical/academic language ("two standard deviations", "expected move" as a term)
- [ ] No forbidden words: leverage, optimize, utilize, fascinating, robust, comprehensive
- [ ] Risk paragraph references only events BEFORE expiration (relevance filter)
- [ ] IV framed as price level ("stay above $X") NOT volatility contraction
- [ ] Em dashes absent from body paragraphs
- [ ] 25% return math verified: Premium / Capital at Risk = 0.25
- [ ] All charts saved to `/var/www/html/charts/` and URLs confirmed accessible

---

## Step 7: Create WordPress Draft + Set Taxonomies

### Write content file (use exec/shell, NOT Write tool)
```bash
cat > /tmp/alert-content.html << 'ALERTEOF'
<!-- wp:paragraph -->
<p>Your alert content here...</p>
<!-- /wp:paragraph -->
ALERTEOF
```

### Create draft
```bash
POST_ID=$(sudo wp --path=/var/www/html --allow-root post create /tmp/alert-content.html \
  --post_type=premium-post \
  --post_status=draft \
  --post_title="TRADE ALERT: [TITLE]" \
  --porcelain)
echo "Draft created: Post $POST_ID"
```

**⚠️ Always `draft`. Never `--post_status=publish` on create.**

### Set taxonomies
```bash
sudo wp --path=/var/www/html --allow-root post term set $POST_ID content-type trade-ideas-updates --by=slug
sudo wp --path=/var/www/html --allow-root post term set $POST_ID product-categories 48-hour-cashflow --by=slug
```

---

## Step 8: Post Preview to #trade-alerts

Channel: `#trade-alerts` (ID: `1473066624993988739`)

**For BUY alerts:**
```
📋 **[TICKER] 48-HOUR CASHFLOW — DRAFT READY FOR REVIEW**

**Post ID:** [POST_ID]
**Post:** [Alert title]
**Preview:** https://joshbelanger.com/?post_type=premium-post&p=[POST_ID]&preview=true

**Trade:** Sell [HIGH] Put / Buy [LOW] Put ([EXP])
**Premium:** $[X] per spread (25% return if above $[HIGH])
**Risk:** $[X] max loss if below $[LOW]

✅ to publish | ❌ to revise
```

**For WIN/LOSS/EXIT updates:**
```
📋 **[TICKER] 48-HOUR CASHFLOW UPDATE — DRAFT READY FOR REVIEW**

**Post ID:** [POST_ID]
**Post:** [Alert title]
**Preview:** https://joshbelanger.com/?post_type=premium-post&p=[POST_ID]&preview=true

**Result:** [Win/Loss/Early Exit] — [summary]
**Record:** XX-XX (XX% win rate)

✅ to publish | ❌ to revise
```

---

## Step 9: Wait for Josh Approval

**Do NOT proceed until Josh explicitly approves.**

If Josh sends revisions:
1. Make the edits
2. Run Post-Edit QC (re-read FULL draft, verify title matches body, grep for old numbers)
3. Update the existing WordPress draft (do NOT create a new post)
4. Re-send preview link

---

## Step 10: Publish + Sheet Update + Activity Log

**⚠️ CRITICAL: DO NOT create a new post. The draft ALREADY EXISTS. Publish the existing one.**

### 10a: Verify and publish
```bash
# Verify it exists as draft
sudo wp --path=/var/www/html --allow-root post get $POST_ID --fields=ID,post_status,post_title

# Publish
sudo wp --path=/var/www/html --allow-root post update $POST_ID --post_status=publish

# Get URL
sudo wp --path=/var/www/html --allow-root post get $POST_ID --field=url
```

Publishing triggers mu-plugin → n8n → email + SMS to all 48-Hour Cashflow subscribers automatically.

### 10b: Update sheet

**Sheet ID:** `1x9xQJAwWxkSY1lpkBLZlHZjhkjw2ZwAH1yybhZz_F00`
**Webhook:** `AKfycbyPMKg4GL32cBRjBziHE4zXE0u68CMRixcmSCqrSy_6wh2k_NXc9Ym-ivbIav7Om8eQ`

**BUY alert — CLI:**
```bash
# expCycle = EXPIRATION DATE (e.g. "Apr 10, 2026"), NOT "weekly"
python3 /home/clawdbot/clawd/skills/trade-sheet-updater/scripts/update_sheet.py \
  48hr buy TICKER "Put Spread" "Apr 10, 2026" 0.10 41.50 40.50 \
  "2026-04-08" "" "https://joshbelanger.com/p/..."
```

**SELL/EXIT — payload:**
```json
{
  "action": "sell",
  "ticker": "TICKER",
  "exitPrice": "X.XX",
  "exitDate": "YYYY-MM-DD",
  "sellAlertLink": "https://joshbelanger.com/..."
}
```

**⚠️ WARNING: Col R (Status) is auto-populated. NEVER write to it.**

### 10c: Verify the sheet
```bash
GOG_KEYRING_PASSWORD="***" gog sheets get 1x9xQJAwWxkSY1lpkBLZlHZjhkjw2ZwAH1yybhZz_F00 'A1:Z10' -p
```

Confirm: exactly ONE new row for this ticker, correct strikes, correct entry price. If two rows or any field wrong, fix before reporting success.

### 10d: Log activity
```bash
cd /home/clawdbot/clawd && ./scripts/log-activity.sh \
  "Published [TICKER] 48-Hour Cashflow [buy/update] alert (Post $POST_ID)" \
  "collaborative"
```

### 10e: Confirm in #trade-alerts
```
✅ **[TICKER] 48-HOUR CASHFLOW — PUBLISHED**

**Live:** [URL]
**Sheet:** Updated ✓
**Notifications:** Triggered (email + SMS)
```

---

## Voice Rules — 48HC Identity

### What 48HC sounds like
- Calm, measured, insurance-driven
- Probability language, not conviction language
- "Patience and probabilities" not "I'm extremely confident"
- Premium collection framing: collecting, selling fear, insurance
- Short declarative sentences. Let the math speak.

### Signature phrases (rotate — don't repeat consecutively)
- "25% return for 48 hours of patience and probabilities."
- "That's not how [X] works."
- "Today's fear is greater than what Friday's reality will show."
- "Pure panic selling."
- "The options market just made bank on [X]'s crash."
- "Fear was greater than reality. We got paid."

### North Star
Lead with what the member is feeling, connect the dots on WHY, and never pretend the market isn't happening around the trade.

### FORBIDDEN (cross-service bleed)
- ❌ "Here's what caught my attention" (HMT)
- ❌ "That's a signal worth following" (HMT)
- ❌ "$X million just dropped on calls" / flow language (HMT)
- ❌ Pattern names: Bull Surge, Bear Plunge, U-Turn (OI)
- ❌ Aggressive conviction / excitement tone (HMT)
- ❌ "When hot money floods in" (HMT)
- ❌ Section headers in body ("What's driving the panic:", "The Risk:")
- ❌ Bullet breakdowns of trade legs in body
- ❌ Statistical language: "two standard deviations", "expected move" as a term
- ❌ Academic language: "Pure capitulation mechanics" → "Pure panic selling"
- ❌ Math breakdowns explaining revenue translations
- ❌ Analyst mentions unless critical to setup
- ❌ Words: leverage, optimize, utilize, fascinating, robust, comprehensive
- ❌ Em dashes in body paragraphs (opening line is fine)
- ❌ Victory lap closers ("Another perfect read! The system keeps delivering!")

### REQUIRED
- ✅ Direct claims (no hedging)
- ✅ Punchy standalone lines
- ✅ Contractions (don't, can't, won't)
- ✅ Specific numbers from research only
- ✅ Conversational and immediate tone
- ✅ "The 48-Hour Window Just Opened" section heading (h2)
- ✅ "What This Trade Looks Like" closing chart heading (h2)
- ✅ Risk woven into narrative, one clean paragraph
- ✅ IV framed as price levels ("stay above $X") not volatility terms

---

## Gold Standard Examples

### BUY: FIG 4903
```
TRADE ALERT: FIG's Earnings Setup – 25% in 48 Hours

Figma reports after the close today. $3.57 expected move on a $24 stock.

That's nearly 15% in either direction. Our system flagged the puts as overpriced. We're collecting that premium.

And if we're right, that's 25% by Friday at 4 PM.

**The 48-Hour Window Just Opened**

[Trade card image]

Figma makes the design software product teams run on. After Adobe's $20 billion acquisition got blocked by regulators, the stock got hammered — down from $142 to under $25.

Right now FIG is at $24.75. The options market is pricing in a massive swing.

Most of the time — 70% — stocks stay inside that expected move at expiration. We're not betting on a good quarter. We're betting on 48 hours of calm in a stock that's already lost 80% of its value.

**ACTION: Sell-to-Open FIG Feb 20, 2026 $21 Put / Buy the $20.50 Put**

• Premium Collected: $10 per spread
• Return: 25% if FIG stays above $21 through Friday

25% return for 48 hours of patience and probabilities.

**What This Trade Looks Like**

[Options analysis chart]
```

### WIN: FIG 4904
```
Another one. 25% in 48 hours.

Figma reported Wednesday after the close. Going in, the options market was pricing a 15% swing in either direction — that's how much fear was baked in. Figma delivered $0.08 per share. Analysts expected a loss of $0.20. Revenue hit $303.8 million, up 40% from a year ago.

The stock went higher. Our $21 and $20.50 puts never got touched.

FIG is at $26.56. Both puts expire worthless at 4 PM today. You keep every penny.

That's the whole game. Fear was greater than reality. We got paid.

No action needed.

$10 on $40 risk. 25% in 48 hours.

**48-Hour Cashflow Record: 47-10 (82% win rate)**

Track every trade live in the new [Trade Tracker](https://joshbelanger.com/pc/48-hour-cashflow/).

Questions about this trade or what I saw in the setup? Just reply — I'm here.

Back Wednesday.
```

---

## Sell/Exit Math Verification (Before Writing Any Update)

1. Pull the entry row from the 48HC sheet — get ACTUAL entry price, entry date, strikes, premium collected
2. Calculate the P&L yourself if it's an early exit
3. Verify the running record (W-L count and win rate) LIVE from the sheet, not from memory
4. If referencing time elapsed, count actual calendar days

**Record miscounts destroy credibility.** If the sheet says 47-10 and you write 48-10, a subscriber who checks will never trust the number again.

---

## Post-Edit Consistency Gate

After making ANY revision to a draft:
1. Re-read the FULL draft top to bottom — not just the changed section
2. Verify title matches body numbers
3. Verify all stats, dates, percentages, and strike prices are internally consistent
4. If you changed a number anywhere, grep the entire draft for the OLD number

---

## Troubleshooting

**Subscribers didn't get notifications:**
1. Did you create as draft first, then publish? (Required for mu-plugin trigger)
2. Were taxonomies set BEFORE publishing?
3. Is n8n running? `docker ps | grep n8n`

**Sheet update failed:**
1. Did you use the redirect pattern?
2. Check response for error message
3. Verify payload JSON is valid
4. Check sheet manually — did it update?

**Wrong premium calculation:**
- Formula: (Sell Strike - Buy Strike) - Premium = Capital at Risk
- Return: Premium / Capital at Risk should = 0.25 (25%)
- Example: Sell $21, Buy $20.50 for $0.10 credit → ($0.50 - $0.10) = $0.40 risk → $0.10 / $0.40 = 25%

**Never pull a published post back to draft** — retriggers n8n and blasts subscribers again.

---

## Reference Table

| Resource | Path |
|---|---|
| Voice reference | `/home/clawdbot/clawd/skills/48hr-cashflow-alert/references/48hr-cashflow-voice.md` |
| Knowledge/examples | `/home/clawdbot/clawd/skills/48hr-cashflow-alert/references/knowledge.md` |
| Phrase bank | `/home/clawdbot/clawd/skills/48hr-cashflow-alert/references/phrase-bank.md` |
| Corrections log | `/home/clawdbot/clawd/skills/48hr-cashflow-alert/data/corrections.log` |
| Brand voice | `/home/clawdbot/clawd/skills/references/brand/voice.md` |
| Alert QC | `/home/clawdbot/clawd/skills/alert-qc.md` |
| SKILL.md (Dash's) | `/home/clawdbot/clawd/skills/48hr-cashflow-alert/SKILL.md` |
| Chart generator | `generate-chart-v4.py TICKER --days 90 --sma 50,200` |
| Price checker | `python3 /home/clawdbot/clawd/scripts/get_price.py TICKER` |
| Sheet updater | `python3 /home/clawdbot/clawd/skills/trade-sheet-updater/scripts/update_sheet.py` |
| Charts directory | `/var/www/html/charts/` → `https://joshbelanger.com/charts/` |
| Activity log | `cd /home/clawdbot/clawd && ./scripts/log-activity.sh` |
| WordPress CLI | `sudo wp --path=/var/www/html --allow-root` |
| Review channel | `#trade-alerts` (ID: `1473066624993988739`) |
| Sheet ID | `1x9xQJAwWxkSY1lpkBLZlHZjhkjw2ZwAH1yybhZz_F00` |
| Webhook | `AKfycbyPMKg4GL32cBRjBziHE4zXE0u68CMRixcmSCqrSy_6wh2k_NXc9Ym-ivbIav7Om8eQ` |

| Taxonomy | Slug |
|---|---|
| Product category | `48-hour-cashflow` |
| Content type | `trade-ideas-updates` |

---

## Gotchas (from Real Sessions)

**Mar 25 — Wrong expiration date (FLY):** Mar 25 vs Mar 27 error. Would have broken entire 48-hour framing. Fixed by adding day-of-week to Step 0 contract line.

**Mar 25 — Opening said same thing 3 ways:** "Choppy and doesn't make sense." Fix: 3 paragraphs, 3 jobs, no overlap. Para 1 = situation. Para 2 = what market gets wrong. Para 3 = what we're doing + return.

**Mar 25 — Em dash rule:** Opening line em dash is fine. Body paragraphs: forbidden. Don't restructure openings to remove them, just catch them in body during QC.

**Mar 25 — Risk paragraph had label:** "The Risk:" as a heading = wrong. Risk woven into narrative, one clean paragraph. No bullets.

**Mar 25 — Expected move missing:** Josh provided $2.00 expected move for FLY. Not included. Always include expected move in price/context paragraph when provided.

**Apr 2 — AXTI robot voice:** Wrote "What's driving the panic:" as section header. Wrote "futures reversed overnight" (fabricated). Wrote victory lap closer. Three failures from not reading published examples first.

**Apr 8 — "Our system" repetition:** Used "Our system" twice in one alert. Josh wants it once max — it provides confidence, but repeating it sounds robotic. Use "flashing" > "flagging" for system language. Second reference should just state the conclusion: "The fear is overpriced."

**Apr 8 — Sheet expCycle field:** Sent "weekly" as expCycle for 48hr buy. Should be the actual expiration date ("Apr 10, 2026"). Column I (exit price) stays blank on buy entries — only populated on follow-up sell alert.

**Apr 8 — Stale price at presentation:** Drafted at $55, presented without refreshing — stock was $53 by then. Always refresh live price immediately before presenting draft to Josh.

**Apr 8 — H2 headers are REQUIRED:** Henry flagged "The 48-Hour Window Just Opened" and "What This Trade Looks Like" as robot voice. Josh overruled — these are format, not optional. Push back if challenged.

**Apr 8 — Discretion framing:** Don't say "taking what the market gives us" as acceptance. Frame it as: this is the best trade we have, it's not ideal, size smaller or pass. The discretionary part of the system means we don't HAVE to take every trade.

**Apr 2 — Record miscounts:** Wrote wrong W-L record from memory instead of sheet. Always verify running record LIVE.

**Apr 2 — Post-expiration risk event:** Referenced risk event after contract expired. Irrelevant to 48-hour trade. Relevance filter: if after expiration, cut it.

**Apr 3 — Service voice bleed:** 48HC drifts toward HMT excitement when reads are skipped. Different services, completely different voice. If the draft sounds excited, it's wrong.

**Apr 3 — Inferred facts from Josh's output:** Josh said "DOCU held. Expired worthless." Wrote "beat estimates" — Josh never said that. Stock going up ≠ earnings beat. Inference ≠ fact.

**Ongoing — Unicode screenshot filenames:** Mac screenshots contain narrow no-break space before "PM". Breaks scp/cp. Fix: wildcard in copy command.

**Apr 8 — H2 headers are REQUIRED, don't remove them:** Henry flagged "The 48-Hour Window Just Opened" and "What This Trade Looks Like" as "robot tell." They're NOT. Every published 48HC alert (FIG, FLY, AXTI) has them. They're in the REQUIRED checklist. Don't remove even if QC says to.

**Apr 8 — Refresh price before EVERY revision:** Alert started at $55, stock moved to $53 during drafting. "$14 below" became "$11.50 below." Always re-check live price before presenting any revision, not just the initial draft.

**Apr 8 — "Our system" once per alert, max:** Josh overruled Henry on this — "our system" provides confidence and belongs in 48HC. The issue was REPETITION (used twice in one alert), not the phrase itself. Use it once in the opening where it lands hardest: "Our system is flashing that the puts are overpriced." Prefer "flashing" over "flagging" — more urgency. Second reference in body should drop the attribution: "The fear is overpriced."

**Apr 8 — White space / standalone lines:** Josh called out insufficient white space. Punchy beats need their own paragraph: "A $7 move in a $55 stock." / "The stock exploded higher today." / "We saw it last week." — standalone, not crammed into dense paragraphs.

**Apr 8 — Sub-25% return framing:** When the spread math doesn't hit 25%, don't hide it. State the actual return (11%). Frame it as: "It's the best trade we have this week, but it carries more risk per dollar of premium than we'd normally take. Size it smaller or pass entirely if that doesn't fit your comfort level." One paragraph, not two. The discretionary choice belongs to the member.

**Apr 8 — Full re-read after EVERY edit:** Josh caught "That's the best trade / That's what the market is giving us" back-to-back — two lines saying the same thing. After any patch, re-read the FULL draft top to bottom, not just the changed section. Read it as a subscriber would.

**Apr 10 — "You" is forbidden in subscriber-facing copy.** "You keep every penny" = individual investment advice framing. Always "we" — publisher's exception. "We keep every penny."

**Apr 10 — Trade Tracker line is unnecessary.** Members know where it is. Remove "Track every trade live in the Trade Tracker" from win/loss updates. Record line is enough.

**Apr 10 — Don't say "sample."** "64 real trades" is fine. "Sample keeps growing" sounds academic. Keep it plain.

**Apr 10 — White space on dramatic beats.** "The stock didn't calm down. Not even close." gets its own line. Then the details follow in the next paragraph. Let punchy standalone lines breathe.

**Apr 10 — QC before presenting.** Run the full alert-qc.md checklist AND read the draft out loud BEFORE showing Josh. He should never be the one catching day-of-week errors or choppiness. That's what the QC step is for.

**Apr 10 — Repeat play callouts.** When trading the same name again, reference it: "Second time we've sold fear on AXTI in two weeks." Builds member confidence and pattern recognition.

**Apr 10 — Record recovery framing.** When win rate recovers after losses, frame it as consistency: "Back above 80% with X real trades. The consistency keeps building." Not "first time" — members remember the dip.

**Apr 8 — Sheet updater expCycle is the EXPIRATION DATE:** `expCycle` arg must be the actual expiration date like "Apr 10, 2026", NOT "weekly" or cycle name. Correct: `48hr buy AXTI "Put Spread" "Apr 10, 2026" 0.10 41.50 40.50 "2026-04-08" "" "URL"`. Column I (exit price) stays blank on buy entries — don't pass 0.

**Apr 8 — Mac Studio screenshots:** SSH from this VPS to Mac Studio: `ssh -i /root/.ssh/id_ed25519 User@100.91.66.81`. Username is "User" (capital U). Then scp the file to `/var/www/html/charts/` for the options analysis chart.
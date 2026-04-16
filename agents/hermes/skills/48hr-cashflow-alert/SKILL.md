---
name: 48hr-cashflow-alert
description: End-to-end 48-Hour Cashflow alert pipeline. Handles buy alerts (premium collection setups), sell/exit alerts (winners, early exits, losers), WordPress publishing, sheet updates, and activity logging. Use when publishing any 48-Hour Cashflow trade alert.
---

# 48-Hour Cashflow Alert Publisher

📋 **Read `data/corrections.log` at the start of every session.** It contains the most recent corrections from Josh. If a lesson has been corrected more than once, it's a pattern — treat it as a hard rule.

⛔ **HARD RULE: Never show alert copy in chat. Never paste drafts into the conversation. The first thing Josh sees is a WordPress preview link.** No exceptions. If you're tempted to "just show a quick draft" — stop. Follow the steps below. Every revision round in chat is a failure this process exists to prevent.

⛔ **HARD RULE: Three-Source Gate.** Every factual claim in alert copy (earnings dates, price levels, market events, statistics, TIME REFERENCES) must come from one of three sources in THIS session: (a) Josh's exact words, (b) a tool result (search, price lookup, sheet data), or (c) a search you ran and can cite. If you can't point to where you got it RIGHT NOW, cut the sentence. No exceptions. Your training data confidence is not a source — it's a liability.

**This includes temporal claims.** "Overnight," "about an hour," "last week," "futures reversed" — these are factual claims. If you didn't check the timestamp, you don't write the time reference.

**Highest fabrication risk: background research color.** Analyst targets, volume comparisons, historical price stats, and industry averages you "just know" are the #1 source of unsourced claims. These feel like harmless context but they're factual claims that need [SEARCH] or [TOOL] tags. If you can't show the tag, cut the sentence. Flagged in 3/3 buy alert evals.

⛔ **HARD RULE: Read Before You Write — No Exceptions.** Before writing ANY alert (buy or sell/update), you MUST:
1. Read `references/48hr-cashflow-voice.md`
2. Read `references/knowledge.md`
3. Pull and read 2 most recent published alerts OF THE SAME TYPE (buy→buy, loss→loss, win→win) from WordPress

This is not optional prep. This is a gate. If you have not completed all three reads in THIS session, you do not write. "I remember how they sound" has been wrong every time. Your voice drifts between sessions — toward HMT excitement, toward robot structure, toward generic AI language. The reads are the only reliable calibration.

**AXTI failure:** Wrote robot-voice section headers ("What's driving the panic:") and bolted-on risk paragraphs because I hadn't read how published 48HC alerts actually flow. They weave context into narrative. They don't label sections.

⛔ **HARD RULE: Sell/Exit Math Verification.** Before writing any sell/update alert:
1. Pull the entry row from the 48HC sheet — get the ACTUAL entry price, entry date, strikes, premium collected
2. Calculate the P&L yourself if it's an early exit
3. Verify the running record (W-L count and win rate) LIVE from the sheet, not from memory
4. If referencing time elapsed, count actual calendar days

**Record miscounts destroy credibility.** If the sheet says 47-10 and you write 48-10, a subscriber who checks will never trust the number again.

⛔ **HARD RULE: Post-Edit Consistency Gate.** After making ANY revision to a draft:
1. Re-read the FULL draft top to bottom — not just the changed section
2. Verify title matches body numbers
3. Verify all stats, dates, percentages, and strike prices are internally consistent
4. If you changed a number anywhere, grep the entire draft for the OLD number

⛔ **HARD RULE: Use Josh's Context as Raw Material.** When Josh provides color or specific framing, use it. Don't flatten his words into generic market language. His conviction is the voice — not your summary of it.

⛔ **HARD RULE: Verify Josh's Numbers.** If Josh gives you a stat, verify it before using it. Pull the actual number from the sheet or run the math. If off, use the correct one and flag the discrepancy.

Publishing an alert involves these steps:

1. Read voice reference + `references/knowledge.md` examples
2. Write alert draft
3. Henry QC
4. Create WordPress draft
5. Set taxonomies
6. Send draft link to Josh
7. Josh approves
8. Spawn agent → publish + update sheet + log

## Voice & Style Reference — Why Every Step Exists

Your voice drifts between sessions. You don't notice it, but Josh does — and subscribers notice faster. The only calibration that works is reading what's actually live on the site right now. Your memory of how 48HC alerts sound is not reliable enough.

**Read before writing any alert:**
- `references/48hr-cashflow-voice.md` — Voice, tone, fear-selling model. 48HC has a distinctly different voice from HMT and OI. It's calmer, more insurance-analogy driven, more "patience and probabilities." Without reading this, you default to the HMT excitement voice, which is wrong for this service.
- `references/phrase-bank.md` — Rotation phrases. These alerts go to the same subscribers twice a week. "25% return for 48 hours of patience and probabilities" can't appear in every single one. The phrase bank prevents the repetition you won't catch yourself.
- `references/knowledge.md` — Published BUY and SELL alerts. Read them because the STRUCTURE of real published 48HC alerts is different from HMT. Shorter, math-heavier, insurance-framed. You mix up service voices without recent examples.
- **Pull 3 most recent published alerts of same TYPE (buy or sell) from WordPress.** This is the most important calibration step. Published alerts reflect Josh's latest edits. The examples in knowledge.md may be weeks old. WordPress is the source of truth for what "correct" looks like today.

48-Hour Cashflow is a **premium collection service** — selling overpriced fear on puts. 48-hour holding period.

## Service Identity

**Service:** 48-Hour Cashflow  
**Focus:** Selling overpriced fear — premium collection on put spreads  
**Trading:** Put spreads (sell higher strike, buy lower strike)  
**Target:** 25% return in 48 hours  
**Signature:** "25% return for 48 hours of patience and probabilities."

## Alert Types

### 1. BUY Alerts (Premium Collection Setups)

**Narrative Arc (not a checklist — same arc, different story every time):**

Every 48HC buy alert sells overpriced fear. The arc is always: here's what the market is bracing for → here's why it's overpriced → here's what we're collecting. But the angle changes with every trade. Read the gold standard alerts in `references/knowledge.md` before every draft.

**OPENING** — Match the situation. Each alert opens differently based on what's happening:
- Earnings: "[TICKER] reports after the close today. $X expected move on a $X stock."
- Post-crash: "[TICKER] is down X% in X days. The options market is bracing for another X% drop."
- Post-rally: "[TICKER] just ripped X% in one session. That creates mispricing."
- Mystery fear: "I can't find what they're bracing for."

**SYSTEM SIGNAL** — "Our system flagged the puts as overpriced. We're selling that fear."

**RETURN LINE** — "If they expire worthless, we collect X%." or "And if we're right, that's X% by Friday at 4 PM."

**"The 48-Hour Window Just Opened"** — Section heading (h2). Stock chart follows immediately.

**COMPANY + PRICE + EXPECTED MOVE** —
- Company: 1-2 sentences. What they do + why it matters for THIS trade.
- Price: "Right now [TICKER] is at $X. The options market is pricing in a $X move by [day]."
- Include expected move when Josh provides it — it frames the entire thesis.

**THE SETUP** — Why the fear is overpriced. This is the research layer.
- Specific, non-obvious catalysts. Not "earnings could disappoint" but "last March the stock dropped 22% on a guidance miss. This quarter they pre-announced 1,800% revenue growth. The fear is last year's fear."
- Find the ONE SPECIFIC detail that makes the mispricing obvious.
- 2-3 paragraphs. Each paragraph ONE idea. Let it breathe.

**ACTION** — Clean format. No "Capital Required", no "Max Loss", no "Entry: $X credit minimum."
```
ACTION: Sell-to-Open [TICKER] [EXP] $[HIGH] Put / Buy the $[LOW] Put at $[CREDIT] credit

• Premium Collected: $X per spread
• Return: X% if [TICKER] stays above $[HIGH] through [day]
```

**RISK** — Woven into narrative. NOT a labeled section. NOT "Here's The Risk" or "The Risk:".
One paragraph naming the specific event that could break the trade. Plain English.
- NO statistical language: "two standard deviations", "expected move" as a term
- ✅ "If earnings blow up, the stock can move way past where the options market expected."
- ✅ "If China tightens export permits further, this stock can drop fast. Size this one smaller than usual."

**CLOSING THESIS** — "X% return for 48 hours of patience and probabilities."

**"What This Trade Looks Like"** — Section heading (h2). Options analysis chart.

**Real Example Structure (FIG 4903):**

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

### 2. TRADE UPDATE Alerts — Winners

**Arc:** Result first → What happened → Current price → Math → "No action needed" → Record → Close.

Win alerts are matter-of-fact. The system worked. Fear was overpriced. We collected. Length varies — some wins are dramatic (AXTI survived a morning dip below the strike) and some are boring (FIG just held). Match the story.

**Real Example (FIG 4904):**

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

### 3. TRADE UPDATE Alerts — Losers

**Title:** `TRADE UPDATE: [TICKER] — Expiration Max Loss`

**Arc:** Bad news → What we did → What went wrong → Net loss (one line) → Insurance framing → "No action needed" → Record → Close.

Loss alerts are SHORT and honest. Insurance framing helps. The spread capped the damage — that's the point.

**Key beats:**
- **OPENER:** "Bad news..." or "Unfortunately, the market beat us this week." NOT "I got this one wrong" (old template).
- **WHAT HAPPENED:** What we did, what went wrong. Brief.
- **NET LOSS:** "We collected $X but lost the full $Y risk." ONE LINE. No bullet breakdown of legs.
- **INSURANCE FRAMING:** "This is why we don't sell naked options. We hedge every time. Without that $X put, the loss would be multiples. The spread structure capped the damage."
- **"No action needed. Your broker handles it automatically."**
- **RECORD** — REQUIRED. Pull live from sheet BEFORE writing.
- **CLOSER:** "Back [next] Wednesday with a fresh setup."

**Published gold standards:** FLY 4991, GAP 4927, RCAT 4982. Read them before writing any loss alert.

### 4. TRADE UPDATE Alerts — Early Exits

**Structure:**

```
1. WHAT CHANGED
   New market conditions, catalyst shift

2. WHY EXIT EARLY
   Specific reason

3. ACTION (bold)
   BUY-TO-CLOSE [STRIKES] put spread at $[PRICE] or better

4. P/L CALCULATION
   Collected $X, buying back for $Y, locks in $Z profit/loss

5. CLOSER
   "The trade worked. Conditions changed. We adapt."
   OR "Better to take a small loss now than risk a bigger one."
```

---

## Research Before You Write — MANDATORY

Before drafting any alert copy, search for current market context:

```
1. web_search: "[TICKER] stock news today"
2. web_search: "market news today [date]" — macro environment, what moved markets
3. web_search: "[any company/event you plan to reference] [date]" — verify BEFORE writing
```

**If you plan to reference it, you must have searched for it first. No exceptions.**
- Wrong: "Marvell reported last night" (assumed, not verified)
- Right: Search "MRVL earnings date 2026" → confirm March 5 → then write "Five days ago, Marvell reported..."

Any fact that cannot be verified by search gets cut. Omit > invent.

---

## Pre-Present QC — Why This Exists

You are not a reliable self-assessor of your own output. You consistently miss: math errors in premium calculations (the 25% return math has been wrong), incorrect expiration dates, and voice drift between services (you write 48HC alerts that sound like HMT). The QC step catches what you can't see in your own work.

Read and run `skills/alert-qc.md` before presenting any draft to Josh. If you skip this, Josh becomes the QC layer, which defeats the purpose of having you write alerts.

## Step 0: Hard Gate — Date, Time, Price

48HC alerts are time-sensitive — they're 48-hour trades with specific expiration windows. Getting the date or price wrong isn't just embarrassing, it means subscribers enter a trade with the wrong math. Running this gate takes 10 seconds and catches errors that would require a correction email to thousands of people.

Before writing a single word, run and print:

```
DATE/TIME: [session_status 🕒 line]
TICKER:    $XXX.XX (live)
CONTRACT:  [TICKER] [EXP — write the DAY OF WEEK] $[HIGH]/$[LOW] Put Spread
```

Example: `CONTRACT: FLY Mar 27 (Friday) $25.50/$25.00 Put Spread`

Writing the **day of week** makes a wrong expiration date impossible to miss visually. Josh caught a Mar 25 vs Mar 27 error on the FLY alert (Mar 25, 2026) — a same-day expiration that would have broken the entire 48-hour framing. The day of week would have caught it instantly.

Josh sees this output and can catch errors before any work is done.

---

## Step 1: Verify Before You Write — REQUIRED OUTPUT

This step produces visible proof that you checked the numbers. It's a required output — not because we don't trust you, but because you've been confidently wrong before and the only way to catch it is to make the verification visible. If the VERIFIED/ENTRY/CHART lines don't appear in your response, you skipped this step, full stop.

### 1. Verify live stock price

```bash
python3 ~/clawd/scripts/get_price.py TICKER
```
*(Tries Google Finance first (real-time), falls back to yfinance ~1-2 min)*

After running, output this line in your response:
> **VERIFIED: [TICKER] = $[result] (live)**

Do not write "Shares are trading at $X" until this line appears in your response. The reason: you've written prices from memory that were off by dollars, not cents.

### 2. Verify entry price

- **If Josh explicitly provided an entry price** → use it. Still show: `ENTRY PRICE: $X.XX (provided by Josh)`
- **If no entry price was provided** → check the option chain live before assuming any price. 48HC spreads are sensitive to premium — a few cents changes whether the 25% return math works.

### 3. Generate branded chart

```bash
cd /home/clawdbot/clawd && source .venv/bin/activate && python scripts/generate-chart-v4.py TICKER --days 90 --sma 50,200
```
The script outputs a URL at `https://joshbelanger.com/charts/...` — use this in the alert's chart section.

### 4. Confirm before proceeding

Your response must contain these lines before any alert copy:
```
VERIFIED: [TICKER] = $XXX.XX (live)
ENTRY PRICE: $X.XX (provided by Josh / live mid)
CHART: https://joshbelanger.com/charts/[filename].png
```

**If these lines are missing from your response, you did not complete Step 1. Stop and run them.** This is not bureaucracy — it's the difference between a professional alert and a correction email.

---

## Pre-Write Checklist (after Step 1 is complete)

These aren't optional prep work. Each item addresses a specific failure mode:

- [ ] Read `references/48hr-cashflow-voice.md` — because you mix up HMT's excitement voice with 48HC's calm insurance voice every time you skip this
- [ ] Pull 3 most recent published alerts of same TYPE (buy or update) from WordPress — because the live structure evolves and your memory of "what a 48HC alert looks like" drifts
- [ ] Verify current option prices (yfinance) for both legs — because premium changes fast and the numbers in your draft must match what subscribers can actually execute
- [ ] Calculate premium collected correctly (sell higher - buy lower) — because you've gotten this wrong before and bad math in a trade alert destroys credibility
- [ ] Verify 25% return math: ($premium / $capital_at_risk) = 0.25 — this is the entire service promise. If this number is wrong, nothing else matters
- [ ] Chart images saved to `/var/www/html/charts/` if using — because you've referenced chart URLs that didn't exist

---

## Publishing Pipeline

### Step 1: Write Alert

Read `references/48hr-cashflow-voice.md` and write the alert. Output in WordPress block format (`<!-- wp:paragraph -->`).

### Step 2: Henry QC — Structural Comparison

This step exists because you consistently believe your draft matches published structure when it doesn't. The only way to catch structural drift is to have the real thing open next to your draft. "I'm confident it matches" has been wrong every time you've said it.

```bash
sudo wp --path=/var/www/html --allow-root post list --post_type=premium-post --posts_per_page=10 --post_status=publish --fields=ID,post_title --orderby=date --order=DESC
sudo wp --path=/var/www/html --allow-root post get <ID> --field=post_content
```

Pull the 2 most recent published 48HC alerts of the same TYPE from WordPress. Read them. Then compare your draft against them, checking:

- [ ] For closing alerts: opens with win/loss result, not setup recap? (You default to recapping the setup first — subscribers want the result immediately)
- [ ] Dollar math correct: collected $X, buying back for $Y, locks in $Z? (Premium math errors have happened — double-check against actual numbers)
- [ ] Win rate record updated correctly? (The running record is subscriber-facing. Getting it wrong makes the service look sloppy)
- [ ] "No action needed" included on expiring winners? (Subscribers panic if there's no explicit instruction — even "do nothing" is an instruction)
- [ ] Entry date and spread strikes correct? (Verify from sheet — you've gotten dates wrong across sessions)
- [ ] Trade Tracker link included? (Subscribers use this to verify their own positions)
- [ ] WordPress block format throughout? (You sometimes drop the format mid-alert)

Fix anything before proceeding. Josh should never see a draft that hasn't passed this. If he's catching structural issues, this step failed.

### Step 3: Create WordPress Draft

**Write the HTML content file using `exec` (shell), NOT the Write tool:**
```bash
cat > /tmp/alert-content.html << 'ALERTEOF'
<!-- wp:paragraph -->
<p>Your alert content here...</p>
<!-- /wp:paragraph -->
ALERTEOF
```

Then create the draft:
```bash
POST_ID=$(sudo wp --path=/var/www/html --allow-root post create /tmp/alert-content.html \
  --post_type=premium-post \
  --post_status=draft \
  --post_title="TRADE ALERT: [TITLE]" \
  --porcelain)
echo "Draft created: Post $POST_ID"
```

**⚠️ Always `draft`. Never `--post_status=publish` on create.**
**⚠️ Use `exec` to write /tmp files, not the Write tool (which may fail on /tmp).**

### Step 4: Set Taxonomies

```bash
sudo wp --path=/var/www/html --allow-root post term set $POST_ID content-type trade-ideas-updates --by=slug
sudo wp --path=/var/www/html --allow-root post term set $POST_ID product-categories 48-hour-cashflow --by=slug
```

### Step 5: Send Draft Link to Josh

Channel: `#trade-alerts` (ID: `1473066624993988739`)

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


### Step 6: Wait for Approval

Do NOT proceed until Josh explicitly approves via Telegram.


### Step 7: On Approval — Publish Existing Draft + Sheet + Log

**⚠️ CRITICAL: DO NOT create a new post. DO NOT rewrite the alert. The draft ALREADY EXISTS from Step 3. Your ONLY job is to publish it.**

When spawning the publish agent, pass the EXACT post ID from Step 3. The agent task should be:

```
Publish existing WordPress draft Post [POST_ID] for 48-Hour Cashflow. DO NOT create a new post.

1. VERIFY the post exists and is a draft:
   sudo wp --path=/var/www/html --allow-root post get [POST_ID] --fields=ID,post_status,post_title
   If post_status is NOT "draft", STOP and report the error.

2. Publish it:
   sudo wp --path=/var/www/html --allow-root post update [POST_ID] --post_status=publish

3. Get URL:
   sudo wp --path=/var/www/html --allow-root post get [POST_ID] --field=url

4. Update sheet:
   - READ /home/clawdbot/dash/skills/trade-sheet-updater/references/48hr-cashflow.md FIRST
   - Build the payload exactly from that schema — do not guess field names or values
   - Use the curl redirect pattern from /home/clawdbot/dash/skills/trade-sheet-updater/SKILL.md

5. **Verify the sheet — required before reporting done:**
   Read back the sheet rows around the new entry:
   ```bash
   GOG_KEYRING_PASSWORD="henrybot2026" gog sheets get 1x9xQJAwWxkSY1lpkBLZlHZjhkjw2ZwAH1yybhZz_F00 'A1:Z10' -p
   ```
   Confirm exactly ONE new row for this ticker, correct strikes, correct entry price. If there are two rows or any field is wrong, fix it before reporting success.

6. Log: cd /home/clawdbot/clawd && ./scripts/log-activity.sh "Published [TICKER] 48-Hour Cashflow [buy/update] alert (Post [POST_ID])" "collaborative"
```

**The agent must NOT:**
- Create any new posts (no `wp post create`)
- Rewrite or modify the alert content
- Generate new alert copy

Publishing triggers mu-plugin → n8n → email + SMS to all 48-Hour Cashflow subscribers automatically.

---

## Voice Reminders (from 48HC reference)

**FORBIDDEN:**
- ❌ Statistical language: "two standard deviations", "expected move" as a term
- ❌ Academic language: "Pure capitulation mechanics" → say "Pure panic selling"
- ❌ Math breakdowns explaining how revenue translates
- ❌ Analyst mentions unless critical to the setup
- ❌ Words: leverage, optimize, utilize, fascinating, robust, comprehensive

**REQUIRED:**
- ✅ Direct claims (no hedging)
- ✅ Punchy standalone lines
- ✅ Use contractions (don't, can't, won't)
- ✅ Specific numbers from research only
- ✅ Conversational and immediate tone

**Signature phrases:**
- "That's not how [X] works."
- "Today's fear is greater than what Friday's reality will show."
- "Pure panic selling."
- "The options market just made bank on [X]'s crash."
- "25% return for 48 hours of patience and probabilities."

---

## Service Voice Fingerprint

**48HC phrases — YOURS (use these, they define the service):**
- "The 48-Hour Window Just Opened" (section heading)
- "25% return for 48 hours of patience and probabilities"
- Insurance framing: "like State Farm paying a claim"
- "Fear is greater than reality"
- Calm, measured, probability-driven tone
- Premium collection language: "collecting that premium," "selling overpriced fear"

**BANNED — these belong to OTHER services:**
- ❌ "Here's what caught my attention" (that's HMT)
- "What This Trade Looks Like" IS used in 48HC for the closing options analysis chart (see published AXTI 4994, FIG 4903). This heading is shared with OI. It is NOT an HMT phrase.
- ❌ "That's a signal worth following" (that's HMT)
- ❌ "$X million just dropped on calls" / flow-following language (that's HMT)
- ❌ Pattern names: Bull Surge, Bear Plunge, U-Turn (those are OI)
- ❌ Aggressive conviction / excitement tone — 48HC is calm insurance, not HMT hype
- ❌ "When hot money floods in" (that's HMT)

**If you catch any banned phrase or tone in your draft, you've got service voice bleed. Stop and re-read `references/48hr-cashflow-voice.md`.**

## 48HC-Specific Writing Rules

### Relevance Filter for Risk Paragraph
If a risk event happens AFTER the contract expires, it doesn't belong in the alert. 48HC trades expire in 48 hours. An earnings report next Tuesday is irrelevant to a Friday expiration. Only include risks that could materially impact the stock BEFORE expiration.

### Anti-Robot-Voice Rules
48HC alerts weave context into narrative. They do NOT use labeled sections or bullet breakdowns in the body.
- ❌ "What's driving the panic:" (section header = robot)
- ❌ "The Risk:" as a heading (belongs in narrative flow)
- ❌ Bullet-point breakdowns of trade legs
- ✅ Weave the driver into a sentence: "The stock dropped 8% after earnings and the puts are pricing in another 15% by Friday."
- ✅ Risk woven into paragraph: "If earnings blow up, the stock can move way past where the options market expected."

### IV Framing
48HC is about **holding a strike level**, not about volatility being lower than expected. Frame the thesis as: "We need [TICKER] to stay above $X through Friday." Not: "We expect implied volatility to contract post-earnings." Subscribers don't think in vol terms. They think in price terms.

### Victory Lap Closers
Don't over-celebrate wins. The closer should be matter-of-fact: "Back Wednesday." Not: "Another perfect read! The system keeps delivering!" The record speaks for itself.

---

## Gotchas (from Real Sessions)

**Apr 2, 2026 — AXTI robot voice + fabricated temporal claims**
Wrote "What's driving the panic:" as a section header (robot voice). Wrote "futures reversed overnight" (they hadn't — fabricated temporal claim). Wrote victory lap closer. Three failures in one alert, all from not reading published examples first.

**Apr 2, 2026 — Record miscounts**
Wrote wrong W-L record because I pulled from memory instead of the sheet. Always verify the running record LIVE before writing any update alert.

**Apr 2, 2026 — Risk paragraph included post-expiration events**
Referenced a risk event that happened after the contract expired. Irrelevant to a 48-hour trade. Relevance filter: if it's after expiration, cut it.

**Mar 25, 2026 — QC before presenting, not after Josh asks**
I presented the FLY draft to Josh before running alert-qc.md. Josh asked "Did you review that?" — that's the failure. QC is mandatory BEFORE sending the preview link. If you've written the draft and you haven't run QC, you haven't finished the draft yet.

**Mar 25, 2026 — Opening structure: 3 paragraphs, 3 jobs, no overlap**
My first FLY opening said the same thing 3 different ways. Josh called it "choppy and doesn't make sense." The structure is: Para 1 = what's happening with this stock. Para 2 = what the market is getting wrong. Para 3 = what we're doing + return. Each paragraph advances the logic. The words change every alert — the structure doesn't. It's a guide, not a script. Read `references/48hr-cashflow-voice.md` for detail.

**Mar 25, 2026 — Em dashes: opening is fine, body is not**
The em dash rule is not absolute zero. Josh approved the opening line em dash ("That kind of move creates mispricing in the options — especially the puts."). The rule applies to the body. Don't restructure opening lines to remove the em dash — just catch them in the body paragraphs during QC.

**Mar 25, 2026 — Risk paragraph: no label, no bullets, woven in**
"The Risk:" as a heading or label = wrong. Risk belongs in narrative form, one clean paragraph. No bullet breakdown of legs. No "max loss: $X." Just plain English: what specific event breaks the trade, in one paragraph.

**Mar 25, 2026 — Expected move belongs in the price context paragraph**
Josh provided a $2.00 expected move for FLY. I didn't include it — Josh had to flag it. Always ask for or include the expected move in the price/context paragraph when it's relevant to the setup framing.

**Mar 25, 2026 — Screenshot filenames with unicode characters**
Mac screenshots can contain a narrow no-break space (unicode `e2 80 af`) before "PM" in the filename. This breaks `scp` and `cp` with quoted paths. Fix: use a wildcard in the copy command. `cp /path/Screenshot\ 2026-03-25\ at\ 2.43.28*PM.png /tmp/fixed.png`

**Ongoing — Service voice bleed from HMT**
48HC drifts toward HMT excitement voice when I skip the reads. The two services feel similar (both are options trades) but the VOICE is completely different. HMT = aggressive conviction following institutional money. 48HC = calm insurance collecting premium from overpriced fear. If the draft sounds excited, it's wrong for 48HC.

**Apr 3, 2026 — Estimated context stats need source tags**
Learned from HMT eval: if you generate a stat to provide context ("normal volume runs X", "average move is Y%", "typical premium is Z"), it needs a source tag. Estimated context stats are still facts. If you don't have the number from Josh or a tool, don't write the sentence.

**Apr 3, 2026 — Live site always wins over knowledge.md**
If published alerts on WordPress differ from examples in knowledge.md, the published version is correct. Josh's preferences evolve. knowledge.md may be weeks behind. This is why "pull 2 recent published alerts" is a gate, not a suggestion.

**Apr 3, 2026 — Source tags must be VISIBLE, not just done**
Found DocuSign's $2B buyback in search results but didn't show the source tag in working notes. The data was sourced but the tag was invisible. Three-source gate requires the tag to be shown. If the grader can't see the source, it's a violation.

**Apr 3, 2026 — Don't infer facts from Josh's output**
Josh said "DOCU held. Expired worthless." I wrote "beat estimates" — Josh never said that. Stock going up doesn't mean earnings beat. Inference ≠ fact. If Josh didn't say it and you didn't search it, don't write it.

---

## Troubleshooting

**Subscribers didn't get notifications:**
1. Did you create as draft first, then publish?
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

---

## Reference

**WordPress taxonomy slug:** `48-hour-cashflow`  
**Content type slug:** `trade-ideas-updates`  
**Chart directory:** `/var/www/html/charts/` → `https://joshbelanger.com/charts/[filename]`

**Image block format — all 48HC alerts:**
```html
<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/FILENAME.png" alt="Description" style="width:800px"/></figure>
<!-- /wp:image -->
```
Never upload to WP media library. Always use `/charts/` URL directly. Always `style="width:800px"`.
**Typical expiration:** Friday 4 PM (48 hours from Wednesday entry)

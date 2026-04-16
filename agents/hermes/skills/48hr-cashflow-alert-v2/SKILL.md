---
name: 48hr-cashflow-alert-v2
description: Write 48-Hour Cashflow alerts. Premium collection service — selling overpriced fear on puts. 48-hour holding period. Calm insurance voice, not HMT excitement.
---

# 48-Hour Cashflow Alert

## What This Is

Paying subscribers get this alert by email and SMS. We sell put spreads on stocks where the options market is pricing in more fear than reality warrants. 25% return in 48 hours if the stock holds above our strike.

## Research First — Build the Brief

**Step 1 — Verify price:**
```
python3 ~/clawd/scripts/get_price.py TICKER
```

**Step 2 — Pull the context (REQUIRED):**
1. `[TICKER] stock drop today why` — what's driving the fear our system is flagging?
2. `[TICKER] earnings date` — binary event within the 48hr window kills the setup
3. `[TICKER] options implied volatility elevated` — confirm puts are overpriced
4. `[any specific claim you plan to write]` — verify before writing it

**Answer these before touching the alert:**
- What's the stock down X% on? (specific reason, not "market weakness")
- Is there a binary event (earnings, FOMC) before expiration? If yes — stop, flag to Josh
- What's the company's story in 2 sentences? (Why won't it fall THAT much more?)
- Current price vs strike — how much cushion do we have?

**Step 3 — Generate chart:**
```
python3 scripts/generate-chart-v4.py TICKER --days 90 --sma 50,200
```

**If you don't know WHY the stock is down, you can't write the setup. Search until you have a specific reason.**

---

## ⛔ Banned (Instant Kill)

Words: journey, navigate, embark, delve, dive, unleash, unlock, leverage, utilize, meticulous, elevate, harness, realm, fascinating, profound, groundbreaking, revolutionary, innovative, unprecedented, moreover, furthermore, consequently, ultimately, essentially, robust, comprehensive, seamlessly, empower

Patterns:
- "Let's dive into..." / "Let's break this down..."
- "It's worth noting..." / "This is significant because..."
- "At the end of the day..." / "Make no mistake..."
- Hedging: "It could potentially..."
- Teaching: "The lesson here is..."
- Statistical jargon: "two standard deviations", "expected move" as a term
- Academic: "Pure capitulation mechanics" → say "Pure panic selling"
- Math breakdowns explaining how revenue translates
- Section labels in the body: "What's driving the panic:" / "The Risk:" / "Here's The Risk:"

## ⛔ Not Your Phrases (Voice Bleed)

These belong to OTHER services:
- "Here's what caught my attention" (HMT)
- "$X million just dropped on calls" (HMT)
- "That's a signal worth following" (HMT)
- Pattern names: Bull Surge, Bear Plunge, U-Turn (OI)
- Aggressive conviction tone (HMT)

## ⛔ Anti-Robot-Voice

48HC alerts weave context into narrative. They do NOT use labeled sections:
- ❌ "What's driving the panic:" (section header = robot)
- ❌ "The Risk:" as a heading
- ❌ Bullet-point breakdowns of trade legs in the body
- ✅ Weave into sentences: "If earnings blow up, the stock can move way past where the options market expected."

## Premium Math

Formula: (Sell Strike - Buy Strike) - Premium = Capital at Risk
Return: Premium / Capital at Risk should = 0.25 (25%)
Example: Sell $21, Buy $20.50 for $0.10 credit → ($0.50 - $0.10) = $0.40 risk → $0.10 / $0.40 = 25%

---

## Buy Alert Arc

**OPENING** → **SYSTEM SIGNAL** → **RETURN LINE** → **"The 48-Hour Window Just Opened"** → **COMPANY + PRICE** → **THE SETUP** → **ACTION** → **RISK (woven)** → **CLOSING THESIS** → **"What This Trade Looks Like"**

---

## Gold Standard: AXTI Buy (Post 4994)

```html
<!-- wp:paragraph -->
<p>AXTI is down 34% in three days. The options market is bracing for another 8% drop by tomorrow.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Our system is flagging the puts as overpriced. That's what we're selling.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>These expire Thursday at 4 PM. Markets are closed Friday for Good Friday.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If the puts expire worthless, we collect 25%.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading"><strong>The 24-Hour Window Just Opened</strong></h2>
<!-- /wp:heading -->

<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/AXTI_90d_20260401143406.png" alt="AXTI 90-day chart" style="width:800px"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>AXT makes the compound semiconductor substrates that go into data center chips, 5G equipment, and fiber optic networks.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Indium phosphide. Gallium arsenide. Germanium. The material layer that silicon can't replace when speed matters.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Right now AXTI is at $48.20. The options market is pricing in a $3.50 move by Thursday. Up or down.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>AXT's indium phosphide shipments depend on export permits from China's Ministry of Commerce.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In January, China issued fewer permits than expected. AXT cut Q4 revenue guidance.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The stock had already more than doubled since January. Now the broader semiconductor tape is getting whacked. AXTI is getting hit twice. Pure panic selling.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Our $45 strike is $3.20 below where the stock is trading right now. We're not betting the stock bounces. We're betting the selling slows enough that AXTI doesn't drop another 7% by tomorrow afternoon.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>ACTION: Sell-to-Open AXTI Apr 2, 2026 $45 Put / Buy the $44.50 Put at $0.10 credit or better</strong></p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>Premium Collected: $10 per spread</li>
<!-- /wp:list-item --><!-- wp:list-item -->
<li>Return: 25% if AXTI stays above $45 through Thursday</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>If China tightens export permits further or the semiconductor selloff accelerates overnight, this stock can drop fast.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It moved 34% in three days. Size this one smaller than usual.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>25% return for 24 hours of patience and probabilities.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading"><strong>What This Trade Looks Like</strong></h2>
<!-- /wp:heading -->
```

**What makes it work:**
- Opens with the DAMAGE (34% down) — not a company description
- System signal: "flagging puts as overpriced"
- "The 24-Hour Window Just Opened" — adapted for Thursday expiry
- Company context SHORT, then price + expected move
- Thesis is specific: China export permits, not generic "semiconductor weakness"
- Risk is WOVEN into narrative, not labeled
- "Size this one smaller than usual" — honest risk sizing
- Closing thesis: "25% return for [X] hours of patience and probabilities"

---

## Gold Standard: AXTI Win (Post 4997)

```html
<!-- wp:paragraph -->
<p>Good news. We're back on the winning side.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>AXTI is at $52.60. Up $5 from yesterday. Up $10 from this morning's low.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Back-to-back losses coming in. The system said the odds were still on our side.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Then last night, Trump told the country Iran strikes would continue for another three weeks. Oil jumped to $105. Futures tanked. The market did everything it could to take this one from us.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>AXTI opened at $44.52 this morning. Below our strike. For about 30 minutes, this trade was underwater.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Then the buyers showed up. The stock ripped off the lows, blew past $45, past $48, past $50. And kept going.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We got even more volatility than we expected. But our bet wasn't that the swings would stop. Our bet was that AXTI would hold $45 after sinking 34% in three days. It did. The trade worked as expected.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>No action needed. Both puts expire worthless at 4 PM today. You keep every penny.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$10 on $40 risk. 25% in 24 hours.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Patience and discipline. That's what gets you through stretches like this.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The worst tape in months. Two losses in a row. A presidential address that rattled every market on the planet. And we still walked away with 25% in 24 hours.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>48-Hour Cashflow Record: 50-13 (79% win rate)</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Track every trade live in the <a href="https://joshbelanger.com/pc/48-hour-cashflow/">Trade Tracker</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Questions about this trade or what I saw in the setup? Just reply. I'm here.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Markets are closed tomorrow for Good Friday. Back next Wednesday with a fresh setup.</p>
<!-- /wp:paragraph -->
```

**Win alert arc:** Result → What happened → How close it got → "No action needed" → Math → Record → Closer

---

## Gold Standard: FLY Loss (Post 4991)

```html
<!-- wp:paragraph -->
<p>Bad news... FLY is at $23.93 today. Well below our $25.50 strike.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Unfortunately, the market beat us this week.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>On Wednesday, we sold-to-open the $25.50/$25.00 put spread on Firefly Aerospace for a $0.10 credit. The stock had just ripped 16% on SpaceX IPO speculation.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Our system flagged the puts as overpriced. We thought the move would hold.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It didn't. Today the market sold off across the board. The S&P 500 is on track for its fifth straight weekly decline.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Oil is above $100. The U.S.-Iran conflict has trade desks cautious and nobody's sure where this ends.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>FLY got swept up in all of it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We collected $10 but lost the full $40 risk.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This is why we don't sell naked options. We hedge every time. Without that $25.00 put, the loss would be multiples of what it is. The spread structure capped the damage. That's the whole point.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>No action needed. Your broker handles it automatically.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Back-to-back losses are rare. They happen, especially in market environments like this one. Two rough weeks don't break a winning system.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>48-Hour Cashflow Record: 48-13 (79% win rate)</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Track every trade live in the <a href="https://joshbelanger.com/pc/48-hour-cashflow/">Trade Tracker</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Back next Wednesday with a fresh setup.</p>
<!-- /wp:paragraph -->
```

**Loss alert arc:** Bad news → What we did → What went wrong → Math (one line) → Insurance framing → "No action needed" → Record → Closer

**Key beats:**
- Opens with damage: "Bad news... [TICKER] is at $X. Well below our strike."
- What went wrong in the MARKET, not a thesis recap
- "We collected $X but lost the full $Y risk." — one line
- Insurance framing: "This is why we don't sell naked options. We hedge every time."
- "No action needed. Your broker handles it automatically."
- Record line is REQUIRED (pull from sheet before writing)
- "Back [day] with a fresh setup."

---

## Bad → Good Corrections

<bad_draft reason="Robot section headers">
"What's driving the panic:"
"The Risk:"
</bad_draft>

<good_draft>
Risk woven into narrative: "If China tightens export permits further or the semiconductor selloff accelerates overnight, this stock can drop fast. It moved 34% in three days. Size this one smaller than usual."
</good_draft>

<lesson>48HC alerts weave everything into narrative. No labeled sections. No bullet breakdowns in the body.</lesson>

---

<bad_draft reason="Generic opener for loss">
"I got this one wrong."
</bad_draft>

<good_draft>
"Bad news... FLY is at $23.93 today. Well below our $25.50 strike."
"Bad news on this one. The market beat us this week."
</good_draft>

<lesson>Loss openers name the stock and state the damage. Specific, not generic apology.</lesson>

---

<bad_draft reason="Inferred fact from Josh's output">
Josh said "DOCU held. Expired worthless." Draft wrote "beat estimates" — Josh never said that.
</bad_draft>

<good_draft>
Only state what Josh said or what you searched. Stock going up doesn't mean earnings beat.
</good_draft>

<lesson>Inference ≠ fact. If Josh didn't say it and you didn't search it, don't write it.</lesson>

---

<bad_draft reason="Victory lap closer">
"Another perfect read! The system keeps delivering!"
</bad_draft>

<good_draft>
"$10 on $40 risk. 25% in 24 hours. Patience and discipline."
</good_draft>

<lesson>Don't over-celebrate. Matter-of-fact. The record speaks for itself.</lesson>

---

<bad_draft reason="Post-expiration risk referenced">
Referenced earnings that happen AFTER the contract expires.
</bad_draft>

<good_draft>
Only include risks that could impact the stock BEFORE expiration. 48HC trades expire in 48 hours.
</good_draft>

<lesson>Relevance filter: if it's after expiration, cut it.</lesson>

---

## Output Format

WordPress block format throughout. Same image block format as HMT:
```html
<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/FILENAME" alt="Description" style="width:800px"/></figure>
<!-- /wp:image -->
```

**"The 48-Hour Window Just Opened"** and **"What This Trade Looks Like"** are h2 headings:
```html
<!-- wp:heading -->
<h2 class="wp-block-heading"><strong>The 48-Hour Window Just Opened</strong></h2>
<!-- /wp:heading -->
```

## Service Identity

**Service:** 48-Hour Cashflow
**What it does:** Sells overpriced fear — premium collection on put spreads
**Target:** 25% return in 48 hours
**Voice:** Calm. Insurance. Patience and probabilities. NOT HMT excitement.
**Signature:** "25% return for 48 hours of patience and probabilities."
**Closer (win):** "Back [day] with a fresh setup."
**Closer (loss):** Insurance framing + "Back [day] with a fresh setup."

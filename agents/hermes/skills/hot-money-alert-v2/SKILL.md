---
name: hot-money-alert-v2
description: Write Hot Money Trader buy alerts. Flow-following service — institutional money signals the trade. Lead with dollars, tell the story, close with conviction.
---

# Hot Money Trader — Buy Alert

## What This Is

Paying subscribers get this alert by email and SMS. It tells them what to buy, why, and at what price. The flow data is the hook. The thesis explains why. The conviction makes it inevitable.

## Research First — Build the Brief

Before writing a word, assemble a catalyst brief. This is the most important step.

**Step 1 — Verify price:**
```
python3 ~/clawd/scripts/get_price.py TICKER
```

**Step 2 — Pull the catalyst (REQUIRED — this is the "why"):**
Search these in order, stop when you have a real answer:
1. `[TICKER] options flow unusual activity today` — confirm the flow is real and current
2. `[TICKER] catalyst news today` — what event tied to the flow? Earnings? Contract? Upgrade? Macro?
3. `[TICKER] stock price movement today` — price action context
4. `[any specific claim you plan to write]` — verify before writing it

**Answer these before touching the alert:**
- What was the flow? ($X million on calls/puts, how many contracts, what strike/expiry)
- What's the catalyst? (specific event — not "sector pressure" or "market conditions")
- What does the company actually do? (2 sentences, verified)
- What's the current stock price?
- Why is the catalyst believable? (Why would smart money bet here?)

**Step 3 — Generate chart:**
```
python3 scripts/generate-chart-v4.py TICKER --days 90 --sma 50,200
```

**If you can't answer "What's the catalyst?" with a specific event — stop and search more. A generic macro thesis is not a catalyst. No exceptions.**

---

## ⛔ Banned (Instant Kill)

Words: journey, navigate, embark, delve, dive, unleash, unlock, leverage, utilize, meticulous, elevate, harness, realm, fascinating, profound, groundbreaking, revolutionary, innovative, unprecedented, moreover, furthermore, consequently, ultimately, essentially, robust, comprehensive, seamlessly, empower

Patterns:
- "Let's dive into..." / "Let's break this down..."
- "It's worth noting..." / "This is significant because..."
- "At the end of the day..." / "Make no mistake..."
- Any sentence starting with "So," as transition
- Hedging: "It could potentially..."
- Teaching: "The lesson here is..."
- Performative excitement: "This is incredibly exciting!"
- Smooth transitions between paragraphs — Josh writes in CUTS

## ⛔ Not Your Phrases (Voice Bleed)

These belong to OTHER services. Using them in HMT is wrong:
- "The 48-Hour Window Just Opened" (48HC)
- "25% return for 48 hours of patience" (48HC)
- Insurance analogies (48HC)
- Pattern names: Bull Surge, Bear Plunge, U-Turn (OI)
- "Our system says to exit" (OI)

## ⛔ Premium Dollar Math

Options = 100 shares per contract. Always: **contracts × price × 100**
Example: 11,000 × $3.21 × 100 = $3.53 million (NOT $35 million)

---

## The Arc

Every HMT buy alert tells the same story in this order. The words change. The arc doesn't.

**HOOK** → **SETUP** → **PIVOT** → **STORY** → **ACTION** → **CLOSE**

---

## Gold Standard #1: USO (Post 4983)

This is what a perfect HMT buy alert looks like. Study the rhythm, not just the words.

```html
<!-- wp:paragraph -->
<p>More than 11,000 contracts just hit the $155 USO calls. All pointing to one thing: oil is going higher.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And if they're wrong, they lose everything.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>USO is the United States Oil Fund ETF. It tracks front-month WTI crude oil futures. When oil moves, USO moves with it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Under normal conditions, the ETF carries a built-in drag from rolling futures contracts. Right now conditions aren't normal. That drag has become a headwind with a potential rocket strapped to it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Shares are trading at $122.45.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/USO_90d_20260320152103.png" alt="USO Stock Chart" style="width:800px"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Here's what caught my attention:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/OptionAlert_USO_20260320.jpeg" alt="USO Options Flow" style="width:800px"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>More than 11,000 contracts on the April 17th $155 calls. Average price: $3.21. That's $3.5 million in fresh premium, all pointed at one strike.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This is the first clear upside positioning I've seen in USO in the last 10 days.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Here's the backdrop.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The US-Iran conflict is in its third week. One hour ago, reports confirmed Marines and additional warships were dispatched to the Middle East. The USS Tripoli, an amphibious assault ship carrying 2,000 Marines, was last spotted near Singapore heading toward the Strait of Hormuz.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The Strait of Hormuz is the chokepoint for roughly 20% of the world's oil supply. If that strait gets disrupted, the math on crude changes overnight.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>These buyers aren't betting on a quiet weekend. They're betting on escalation. And they're doing it going into two days with no market open to adjust.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We're structuring this as a spread to maximize the risk/reward. We're still betting oil goes vertical. The spread just puts more of the move in our favor.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>ACTION: Buy-to-Open USO April 17, 2026 $150/$180 Call Spread at $2.99 or better</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Take Profit: $4.19 (40% gain)<br>Stop Loss: $1.20 (60% loss)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Smart money doesn't drop $3.5 million on calls heading into a weekend unless they see something coming. Following the flow.</p>
<!-- /wp:paragraph -->
```

**What makes it work:**
- Opens with the dollar amount, not a company description
- "And if they're wrong, they lose everything" — optional but powerful
- Company context is SHORT (2 sentences)
- Stock price gets its own line
- Stock chart → "Here's what caught my attention:" → Flow chart (always this order)
- Flow details are SPECIFIC (11,000 contracts, $155 strike, $3.21 average, $3.5M)
- Thesis comes AFTER flow — the USS Tripoli detail, the Strait of Hormuz, 20% of world oil
- ACTION is bold, fully specified
- Closer ties back to the flow signal

---

## Gold Standard #2: DELL (Post 4985)

```html
<!-- wp:paragraph -->
<p>More than 6,400 contracts just hit the $175 DELL calls. All pointing to one thing: shares are going higher.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And if they're wrong, they lose everything.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Dell Technologies (DELL) builds the servers, storage, and PCs that power enterprise. Right now, they're one of the biggest beneficiaries of the AI infrastructure buildout.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Shares are trading at $176.62.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/DELL_90d_20260324152648.png" alt="DELL Stock Chart" style="width:800px"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Here's what caught my attention:</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/OptionAlert_DELL_20260324.jpeg" alt="DELL Options Flow" style="width:800px"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>6,400 contracts on the May 15th $175 calls. Average price: $13. That's $8.3 million in fresh premium, all pointed at one strike.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>But that's not the only upside positioning. The $180 calls traded 4,200 contracts at around $5.00. Another $2.1 million at an even higher strike. Same direction. Same day.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Last month, Dell blew out earnings and guided AI server revenue to $50 billion for fiscal 2027 — 103% growth year over year. They entered this fiscal year with a $43 billion AI server backlog. That's the story the hot money is playing. And Dell's biggest AI server rival, Super Micro Computer, just got hit with a federal indictment last week. Investors are reallocating to the compliance-first alternative with a $43 billion order book already in hand.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>DELL is up nearly 6% today — and that's before the full market share story plays out. Super Micro's indictment didn't just hurt one company. It opened a door, and Dell is the only name with a $43 billion backlog already waiting on the other side.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>With premiums elevated from market uncertainty, we're using a spread to optimize our return and improve our chances of success. We cap the upside, but we get a better entry and more room to be right.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>ACTION: Buy-to-Open Dell April 17, 2026 $180/$200 Call Spread at $5.90 or better</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Take Profit: $8.26 (40% gain)<br>Stop Loss: $2.36 (60% loss)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We need Dell to push through $180 and toward $200 by April 17th.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>$10.4 million across two strikes, same stock, same day. That's not a hedge. That's a thesis. Someone sees the backlog, the SMCI void, and $50 billion in AI revenue guidance and decided the risk of not being in is greater than the risk of being wrong. Following the flow.</p>
<!-- /wp:paragraph -->
```

**What makes it work:**
- TWO flow clusters (6,400 on $175 + 4,200 on $180) — builds the case
- Thesis: SMCI indictment opened a door, DELL is the only one standing — SPECIFIC
- Closing ties the dollar amounts back together across both strikes

---

## Bad → Good Corrections (from Josh)

These are real corrections Josh made on Dash's drafts. Study what was wrong and why.

<bad_draft reason="Missing macro context, wrong tone">
Opens with: "ANET posted a billion-dollar quarter. The Bull Surge just fired."
Body: Lists earnings numbers without market environment. No tension.
</bad_draft>

<good_draft>
Arista builds the switches that power every major AI data center in America. Three weeks ago the company posted record earnings and raised guidance. The reward? An 8% haircut because Iran spooked the tape. But today shares are already up 3%, creeping higher while nobody's watching. That window won't stay open.
</good_draft>

<lesson>The macro environment IS the story. The flow signal + what's happening in the market = why this trade makes sense RIGHT NOW. Without context, it's just a stock tip.</lesson>

---

<bad_draft reason="Run-on sentence, Josh's brainstorm used as-is">
"Arista runs the backbone of every major AI data center in America, and nervous investors have been reluctant to buy with macro headwinds dragging everything lower — three weeks after the company posted record earnings and raised guidance."
</bad_draft>

<good_draft>
Arista builds the switches that power every major AI data center in America. Three weeks ago the company posted record earnings and raised guidance. The reward? An 8% haircut because Iran spooked the tape.
</good_draft>

<lesson>When Josh gives you a brainstorm, your job is to make it SOUND GREAT. Don't paste it in. Break run-ons into punchy sentences. One idea per sentence.</lesson>

---

<bad_draft reason="Fabricated stat, no source">
"Normal daily call volume on CRWD runs around 15,000 contracts across all strikes."
</bad_draft>

<good_draft>
[Cut the sentence entirely — no source for "normal volume" claim]
</good_draft>

<lesson>If you generate a stat to provide context (normal volume, historical average, typical range), it needs a source. If you don't have the number from Josh or a tool, don't write the sentence.</lesson>

---

<bad_draft reason="Generic filler">
"The thesis played out bigger than expected."
"Fear was greater than reality."
"The setup was textbook."
</bad_draft>

<good_draft>
"Oil went from $88 to $111 in two weeks. The call spread we bought at $2.99 is now worth $5.27."
</good_draft>

<lesson>Every general statement must be replaceable with a specific fact. If it can't be, cut it.</lesson>

---

<bad_draft reason="Vague position reference">
"We followed it."
"We got in at $7.45."
</bad_draft>

<good_draft>
"We bought the CRWD May 15 $350/$370 call spread at $7.45."
</good_draft>

<lesson>Subscribers hold multiple positions. Every mention of the trade must include ticker, expiry, strike, and direction.</lesson>

---

## Output Format

WordPress block format throughout:
```html
<!-- wp:paragraph -->
<p>Text here</p>
<!-- /wp:paragraph -->
```

Image blocks:
```html
<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/FILENAME" alt="Description" style="width:800px"/></figure>
<!-- /wp:image -->
```

Never upload to WP media library. Always `/charts/` URL. Always `style="width:800px"`.

## TP/SL

Standard: 40% take profit / 60% stop loss.

---

## Win Alerts (Sell/Exit — Profitable)

Win alerts tell the story of a signal that worked. Recall the original flow, show the result, give the ACTION, celebrate the subscriber.

### Gold Standard: BP (Post 4971)

```html
<!-- wp:paragraph -->
<p>Shares of BP are hitting fresh highs.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And the call spread we bought 5 days ago is up 40%.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Five days ago, $1.2 million dropped on BP calls right before Iran started striking tankers in the Strait of Hormuz and crude exploded toward $100 a barrel.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That money knew something. We followed it.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/BP_90d_20260316114221.png" alt="BP Stock Chart" style="width:800px"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><strong>ACTION: Sell-to-Close BP APR 17 $42/$45 Call Spread at $1.30 or better</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Entry was $0.93. That is 40% in five days while the rest of the world was just waking up to what is happening in the Persian Gulf. The system said take it. We take it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That's how it's done. Onto the next one.</p>
<!-- /wp:paragraph -->
```

### Gold Standard: USO Win (Post 4998)

```html
<!-- wp:paragraph -->
<p>Oil just hit $111.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>And the call spread we bought two weeks ago is up 76%.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Two weeks ago, $3.5 million dropped on USO calls right before the Strait of Hormuz went dark. Marines were heading to the Persian Gulf. Crude was at $88.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That money knew something. We bought the $150/$180 call spread at $2.99.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Now we're finally getting the move those big players were looking for. WTI front-month futures surging on the back of Trump's address. Three-day weekend ahead. And the president just told the country he's going to keep bombing Iran for another three weeks.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Last night Trump addressed the nation. Strikes on Iran continuing for another two to three weeks. No exit strategy. WTI ripped 12% today to $111.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The oil thesis is working. But this tape is vicious. Volatility cuts both ways. We're sitting on 76% heading into a three-day weekend with expiration approaching. Lock it in and reposition later if oil still has legs.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>ACTION: Sell-to-Close USO April 17, 2026 $150/$180 Call Spread at $5.27 or current prices</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Entry was $2.99. That's 76% in two weeks while the rest of the market was getting whipped around by headlines. The system said take it. We take it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That's how it's done. Onto the next one.</p>
<!-- /wp:paragraph -->
```

**Win alert arc:** Result → Entry recall (with flow details) → What's happening now → ACTION → Math → Closer

**Key beats:**
- Open with current price + gain. "Oil just hit $111. And the call spread we bought two weeks ago is up 76%."
- Recall the original flow signal with specific details
- "We targeted X%. We got Y%." — Clean. Punchy.
- ACTION is bold, fully specified with Sell-to-Close
- Body uses "we" throughout. "You" only in celebration paragraph if any.
- Closer: "That's how it's done. Onto the next one." (vary it — don't copy verbatim every time)

---

## Loss Alerts (Sell/Exit — Losers)

Loss alerts are SHORT. Bad news immediately. What happened. ACTION early. Math. Brief honest explanation. Move on.

### Gold Standard: TECK (Post 4968)

```html
<!-- wp:paragraph -->
<p>Bad news. We're cutting TECK for a loss.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Ten days ago, $9.6 million dropped on TECK calls at 35x normal volume. We followed the bet.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The macro backdrop for copper is still bullish. But right now, the Iran war has markets in full risk-off. Industrial metals aren't running in this environment.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Maybe those buyers thought the conflict wouldn't last this long or cause this much of an issue. Hard to know. What we do know is they're still in the trade. Their bet doesn't expire until April 17.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Ours isn't working. We're cutting it loose.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>ACTION: Sell-to-Close TECK Apr 17, 2026 $60/$65 Call Spread at $0.40 or current prices</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We bought at $1.20. The spread is around $0.40 now. That's the loss.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Cut it.</p>
<!-- /wp:paragraph -->
```

### Gold Standard: NVDA Loss (Post 4981)

```html
<!-- wp:paragraph -->
<p>Bad news. We're cutting NVDA for a loss.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Seventeen days ago, a big player dropped $28.5 million into NVDA calls in a single session. 95,000 contracts on one strike, smart money paying up to get filled.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The setup made sense. The Iran-US war had dragged the stock down on fear that had nothing to do with NVIDIA's business. Earnings came in blowout. Jensen Huang took the GTC stage and laid out the next generation of AI infrastructure.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Smart money was betting the stock would finally catch a bid.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It never did.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The war headlines faded. Earnings were forgotten. GTC came and went. NVDA sat in the mud through all of it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Yesterday was the final signal. The Fed held rates. The market sold off anyway. Then Micron reported a record quarter: $23.9 billion in revenue, up 196% year over year, record margins, raised guidance. The whole semiconductor sector opened lower this morning.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This market is not rewarding good news right now. Our 60% stop triggered. Time to salvage what we can.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>ACTION: Sell-to-Close NVDA April 2, 2026 $190/$205 Call Spread at $0.94 or current prices</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We paid $4.05. We're getting out around $0.94. That's the loss.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Cut it. Onto the next one.</p>
<!-- /wp:paragraph -->
```

**Loss alert arc:** Bad news → Original signal recall → What went wrong → ACTION (early) → Math (one line) → Closer

**Key beats:**
- "Bad news. We're cutting [TICKER] for a loss." — opens every loss.
- Recall the original flow signal with specific dollar amounts
- 2-3 sentences on what went wrong. No excuses, no apology
- ACTION bold, early — don't bury it
- Math in one line: "We paid $X. Getting out at $Y. That's the loss."
- "Cut it." or "Cut it. Onto the next one."

**Never include:**
- Long thesis recaps
- "I got this one wrong" (old template)
- Charts (loss alerts don't need visuals)
- Excuses or blame

---

## Bad → Good: Win/Loss Corrections

<bad_draft reason="Loss opener too generic">
"I got this one wrong."
</bad_draft>

<good_draft>
"Bad news. We're cutting TECK for a loss."
"Bad news... FLY is at $23.93 today. Well below our $25.50 strike."
</good_draft>

<lesson>Loss openers name the stock and state the damage. Not generic apology.</lesson>

---

<bad_draft reason="Win alert uses stale numbers">
"Up 90%" in title, "76%" in body after editing
</bad_draft>

<good_draft>
After ANY edit, re-read the FULL draft. Verify title matches body numbers. Grep for the OLD number.
</good_draft>

<lesson>Post-edit consistency. If you change a number anywhere, check the ENTIRE draft for the old number.</lesson>

---

## Service Identity

**Service:** Hot Money Trader
**What it does:** Follows institutional options flow — someone bet millions, we follow
**Voice:** Aggressive conviction. Specific numbers. Short declarative sentences. The flow is the evidence, the thesis explains the evidence.
**Closer (buy):** "That's a signal worth following." or tie flow dollars back to thesis.
**Closer (win):** "That's how it's done. Onto the next one." (vary it)
**Closer (loss):** "Cut it." or "Cut it. Onto the next one."

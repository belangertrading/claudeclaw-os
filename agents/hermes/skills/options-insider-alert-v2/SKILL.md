---
name: options-insider-alert-v2
description: Write Options Insider alerts. Pattern-triggered momentum service — Bull Surge, Bear Plunge, U-Turn, Two-Way Trigger. Lead with the pattern, tell the story, close with conviction.
---

# Options Insider Alert

## What This Is

Paying subscribers get this alert by email and SMS. Our system identifies momentum patterns (Bull Surge, Bear Plunge, U-Turn, Two-Way Trigger). When one fires, we trade it.

## Research First — Build the Brief

**Step 1 — Verify price:**
```
python3 ~/clawd/scripts/get_price.py TICKER
```

**Step 2 — Pull the catalyst (REQUIRED):**
1. `[TICKER] stock news today` — what's driving price action when pattern fired?
2. `[TICKER] [pattern name] sector catalyst` — macro context tying to the pattern
3. `[TICKER] earnings upcoming` — if earnings are imminent, note it in the alert
4. `[any specific claim you plan to write]` — verify before writing it

**Answer these before touching the alert:**
- What's the narrative context? (Why is this stock moving NOW — specific event, not "sector pressure")
- Pattern stats: W-L record on this ticker, total returns (from Josh or skip if unknown)
- What does the company actually do? (2 sentences max, verified)
- Current price and entry price

**Step 3 — Generate chart:**
```
python3 scripts/generate-chart-v4.py TICKER --days 90 --sma 50,200 --annotation "PATTERN_NAME"
```

**The catalyst is what makes the alert readable. "Pattern fired" alone is not a thesis. You need the story context WHY smart money should believe the pattern plays out here.**

---

## ⛔ Banned (Instant Kill)

Words: journey, navigate, embark, delve, dive, unleash, unlock, leverage, utilize, meticulous, elevate, harness, realm, fascinating, profound, groundbreaking, revolutionary, innovative, unprecedented, moreover, furthermore, consequently, ultimately, essentially, robust, comprehensive, seamlessly, empower

Patterns:
- "Let's dive into..." / "Let's break this down..."
- "It's worth noting..." / "This is significant because..."
- "At the end of the day..." / "Make no mistake..."
- Hedging: "It could potentially..."
- Teaching: "The lesson here is..."
- Performative excitement: "This is incredibly exciting!"
- Smooth transitions between paragraphs — Josh writes in CUTS

## ⛔ Not Your Phrases (Voice Bleed)

These belong to OTHER services:
- "Here's what caught my attention" (HMT)
- "$X million just dropped on calls" / flow-following language (HMT)
- "That's a signal worth following" (HMT)
- "The 48-Hour Window Just Opened" (48HC)
- Insurance analogies (48HC)
- "25% return for 48 hours of patience" (48HC)

## ⛔ Pattern Direction (Non-Negotiable)

| Pattern | Direction | We Buy |
|---------|-----------|--------|
| Bull Surge | BULLISH | CALLS |
| U-Turn / U-Turn Velocity | BULLISH (reversing up) | CALLS |
| Bear Plunge | BEARISH | PUTS |
| Two-Way Trigger | NEUTRAL | CALLS + PUTS |

**Bear Plunge = stock DROPPING = we buy PUTS.** If your draft describes Bear Plunge as "buying a dip" or "looking for shares to rip higher," you have it backwards.

## Pattern TP/SL

| Pattern | Take Profit | Stop Loss |
|---------|-------------|-----------|
| Bull Surge | 40% gain | 60% loss |
| Bear Plunge | 40% gain | 60% loss |
| U-Turn Velocity | 50% gain | 50% loss |
| U-Turn Standard | 50% gain | Exit day of expiration |
| Two-Way Trigger | 20% gain (combined) | Close after 10 trading days |

**Always look up the pattern before writing TP/SL. Never from memory.**

---

## Buy Alert Arc

**OPENER (tension)** → **PATTERN INTRO** → **"It just triggered again."** → **STOCK CHART** → **BOLD STORY HEADLINE** → **NARRATIVE (2-4 paras)** → **ACTION + TP/SL** → **CLOSER** → **"What This Trade Looks Like"** → **OPTIONS CHART**

---

## Gold Standard: AMD Bear Plunge (Post 4993)

```html
<!-- wp:paragraph -->
<p>AMD ripped 6.8% last Wednesday on reports that it plans to raise CPU prices 10% to 15%.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Then the last few trading sessions, it's giving it back. Down nearly 10% from Wednesday's high. The Bear Plunge just triggered.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>AMD is at $193.70. The pattern is 2-0 on AMD over the past two years with 148% total returns. The last trigger was August 2024. Hit the profit target 11 days later.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>It just triggered again.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/AMD_90d_20260330153647.png" alt="AMD 90-day chart" style="width:800px"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p><strong>The Sell-the-News Trap</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>AMD builds the CPUs and GPUs that power data centers and AI infrastructure. Q4 revenue hit a record $10.3 billion, up 34% year over year. Data center revenue surged 39%. Q1 2026 guidance came in at $9.8 billion, above what Wall Street expected.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The fundamentals didn't change. The tape did.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The semiconductor sector is under pressure from multiple angles. Export licensing for AMD's MI325X chips to China now requires case-by-case government review. Geopolitical instability is weighing on the whole group. And after a 6.8% single-day rip on pricing news, today's reversal looks like classic sell-the-news.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The Bear Plunge signals when a stock is setting up for a quick drop. AMD surged on pricing headlines Wednesday. Now the reversal is accelerating. Sell-the-news, macro pressure, export headwinds. The tape is pointing lower.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>ACTION: Buy-to-Open AMD April 10, 2026 $190 Put at $6.70 or better</strong><br>Take Profit: $9.38 (40% gain)<br>Stop Loss: $2.68 (60% loss)</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading"><strong>What This Trade Looks Like</strong></h2>
<!-- /wp:heading -->

<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/AMD_options_analysis_20260330.png" alt="AMD Options Analysis" style="width:800px"/></figure>
<!-- /wp:image -->
```

**What makes it work:**
- Opens with TENSION: ripped 6.8%, now giving it back
- Pattern + stats + "It just triggered again." — three beats, three paragraphs
- Stock chart AFTER "It just triggered again."
- Bold custom headline captures the thesis: "The Sell-the-News Trap"
- Narrative is 2-4 paragraphs, ONE idea each
- Bear Plunge correctly described as stock dropping, buying puts
- ACTION with TP/SL
- "What This Trade Looks Like" + options analysis chart at the end

---

## Gold Standard: WMT Bull Surge (Post 4996) — Opening

```
Oil is above $100. The Strait of Hormuz is the chokepoint for roughly 20% of the world's oil supply...

Food prices are climbing. Anyone at the grocery store already knows this. When food prices rise, consumers trade down.

They don't stop buying groceries. They stop buying them at the expensive place.

That's been Walmart's playbook for decades...
```

**What makes it work:** Macro environment → consumer impact → why THIS stock benefits. Not a company description first.

---

## Gold Standard: ABNB Loss (Post 4992)

```html
<!-- wp:paragraph -->
<p>Our system said ABNB was about to rip. Instead, it sank on an upgrade.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Shares were at $131.81 when the U-Turn Velocity triggered on March 25th.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The thesis was clean. Hotels get crushed by high oil and a rate-cut drought. Travelers trade down to Airbnb. Earnings backed it up. Revenue beat. 12% bookings growth. Guidance above expectations.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Two days later, Truist upgraded ABNB from Sell to Hold and raised the price target to $129.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That should have been a catalyst. The stock opened at $129 and is now trading at $122.74.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Good news isn't landing in this market right now.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Five straight weeks of S&P losses. Oil above $100. Macro uncertainty grinding everything down.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Our 50% stop triggered. Time to act.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>ACTION: Sell-to-Close ABNB April 17, 2026 $135 Call at $1.33 or current prices</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>We bought at $3.80. The exit is around $1.33. That's a 65% loss on this trade.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Punt it. Next setup is coming.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The U-Turn Velocity is now 6-1 on ABNB with 398% total returns over the past two years.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>One bad trigger in a rough market doesn't erase that record. But it counts.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Options Insider since inception: 50 wins, 34 losses (59% win rate), average gain of 67% on winners.</p>
<!-- /wp:paragraph -->
```

**Loss alert arc:** System said X, instead Y → Entry context → What went wrong → ACTION (early) → Math → Pattern record → Performance stats → Closer

**Key beats:**
- Opens with contrast: what system said vs what happened
- Entry context: price + date + pattern
- What went wrong: macro environment, specific events
- ACTION bold, early
- Math one line: "We bought at $X. Exit around $Y. That's Z% loss."
- Pattern record post-loss (REQUIRED)
- Performance stats from sheet (REQUIRED for OI losses): "Since inception: X wins, average gain of Y%"
- "Punt it. Next setup is coming." or "Cut it."

**Never include in OI losses:**
- "I got this one wrong"
- Long thesis recaps
- "What This Trade Looks Like" section
- Charts

---

## Win Alert Structure

- Open with the result + what moved
- Entry recall with pattern details
- "We targeted X%. We got Y%."
- ACTION: Sell-to-Close / Buy-to-Close (bold)
- Could it run more? Maybe. But "Get in, get the X%, get out."
- Pattern record update

---

## Bad → Good Corrections

<bad_draft reason="Bear Plunge described backwards">
"The Bear Plunge catches stocks that have been hit harder than the move warrants. Looking for shares to rip higher."
</bad_draft>

<good_draft>
"The Bear Plunge signals when a stock is setting up for a quick drop. AMD surged on pricing headlines Wednesday. Now the reversal is accelerating."
</good_draft>

<lesson>Bear Plunge = BEARISH = stock dropping = we buy PUTS. Before writing ANY pattern description, answer: "What position? What direction?" If they don't match, stop.</lesson>

---

<bad_draft reason="Dense paragraphs">
"ABNB is at $132 and our U-Turn Velocity just fired. The one that catches stocks right as they flip from pressure to momentum. Airbnb runs the largest short-term rental marketplace in the world. Pattern is 6-0 with 463% total returns. It just triggered again."
</bad_draft>

<good_draft>
"Two weeks ago, the ABNB Bear Plunge fired."

"Now the U-Turn Velocity just fired. Looking for shares to rip higher."

"ABNB is at $132.03. The pattern is 6-0 on ABNB over the past two years with 463% total returns."

"It just triggered again."
</good_draft>

<lesson>Opening needs breathing room. Each beat is its own paragraph. One thought per paragraph.</lesson>

---

<bad_draft reason="Paraphrased Josh's thesis">
"Low debt, high sensitivity to economic growth."
</bad_draft>

<good_draft>
"People don't stop traveling. They trade down from hotels to Airbnb."
</good_draft>

<lesson>When Josh gives you the thesis, use it. Don't translate his insight into generic market language.</lesson>

---

<bad_draft reason="HMT voice in OI alert">
"Here's what caught my attention:" before options screenshot
</bad_draft>

<good_draft>
"What This Trade Looks Like" before options screenshot (OI's phrase)
</good_draft>

<lesson>Service voices are not interchangeable. OI uses "What This Trade Looks Like." HMT uses "Here's what caught my attention."</lesson>

---

<bad_draft reason="Fabricated pattern stats">
Invented a W-L record that didn't exist.
</bad_draft>

<good_draft>
If you don't have the number, omit the line entirely. Omit > invent.
</good_draft>

<lesson>Never fabricate pattern stats. The SCHW incident happened because stats were invented. If Josh didn't provide it, don't write it.</lesson>

---

## Output Format

WordPress block format. Same image block format as other services:
```html
<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/FILENAME" alt="Description" style="width:800px"/></figure>
<!-- /wp:image -->
```

**"What This Trade Looks Like"** is an h2 heading:
```html
<!-- wp:heading -->
<h2 class="wp-block-heading"><strong>What This Trade Looks Like</strong></h2>
<!-- /wp:heading -->
```

## Service Identity

**Service:** Options Insider
**What it does:** Pattern-triggered momentum trading — system identifies, we execute
**Voice:** Conviction driven by pattern history. Specific numbers. "It just triggered again."
**Phrases:** "Get in, get the X%, get out." / "It just triggered again." / Pattern names
**Closer (buy):** Days to expiration + pattern conviction + "Get in, get the X%, get out."
**Closer (win):** Pattern record + move on
**Closer (loss):** "Punt it." or "Cut it." + performance stats

---
name: hot-money-alert
description: End-to-end Hot Money Trader alert pipeline. Handles buy alerts (unusual flow), sell/exit alerts (winners and losers), WordPress publishing, sheet updates, and activity logging. Use when publishing any Hot Money Trader trade alert.
---

# Hot Money Trader Alert Publisher

⛔ **HARD RULE: Never show alert copy in chat. Never paste drafts into the conversation. The first thing Josh sees is a WordPress preview link.** No exceptions. Follow the steps below — the skill exists to prevent revision rounds in chat.

⛔ **HARD RULE: Three-Source Gate.** Every factual claim in alert copy (earnings dates, price levels, market events, statistics, TIME REFERENCES) must come from one of three sources in THIS session: (a) Josh's exact words, (b) a tool result (search, price lookup, sheet data), or (c) a search you ran and can cite. If you can't point to where you got it RIGHT NOW, cut the sentence. No exceptions. Your training data confidence is not a source — it's a liability.

**This includes temporal claims.** "Overnight," "about an hour," "last week," "two days ago," "futures reversed" — these are factual claims. If you didn't check the timestamp, you don't write the time reference.

**Highest fabrication risk: background research color.** Analyst targets, volume comparisons, historical price stats, and industry averages you "just know" are the #1 source of unsourced claims. These feel like harmless context but they're factual claims that need [SEARCH] or [TOOL] tags. If you can't show the tag, cut the sentence. This was flagged in 3 out of 3 buy alert evals (HMT: "normal volume runs 15,000", OI: "Benchmark initiated at $190", 48HC: "$2B buyback").

⛔ **HARD RULE: Read Before You Write — No Exceptions.** Before writing ANY alert (buy or sell), you MUST:
1. Read `references/hot-money-voice.md`
2. Read `references/knowledge.md`
3. Pull and read 2 most recent published alerts OF THE SAME TYPE (buy→buy, loss→loss, win→win) from WordPress

This is not optional prep. This is a gate. If you have not completed all three reads in THIS session, you do not write. "I remember how they sound" has been wrong every time it was tested. Your voice drifts between sessions and you don't notice. The reads are the calibration — skip them and the draft will need 3-4 revision rounds instead of 0-1.

**Mar 27-Apr 2 failures:** USO sell alert took 6+ revision rounds. ABNB draft used wrong energy. Every time I skipped the reads and drafted from memory, it cost 3-4 extra rounds minimum.

⛔ **HARD RULE: Sell/Exit Math Verification.** Before writing any sell/exit alert:
1. Pull the entry row from the HMT sheet — get the ACTUAL entry price, entry date, contract details
2. Calculate the P&L math yourself: `(exit - entry) / entry × 100`
3. Verify every number in the copy matches the sheet, not your memory
4. If referencing prior trades or running record, pull that number LIVE from the sheet — do not reuse a number from a previous session
5. If referencing time elapsed ("three days ago," "last week"), count the actual calendar days from entry date to today

**USO failure:** Used stale gain percentage without rechecking. Title said 90% after body was updated to 76%. Both numbers came from memory, not the sheet.

⛔ **HARD RULE: Post-Edit Consistency Gate.** After making ANY revision to a draft (Josh's feedback, your own catch, anything):
1. Re-read the FULL draft top to bottom — not just the changed section
2. Verify title matches body numbers
3. Verify all stats, dates, and percentages are internally consistent
4. If you changed a number anywhere, grep the entire draft for the OLD number

**USO failure:** Updated body gain from 90% to 76% but left the title saying 90%. A full re-read would have caught this in 5 seconds.

⛔ **HARD RULE: Specify the Position.** Never use vague position references. Every mention of the trade must include WHAT was traded.
- ❌ "We followed it" — followed WHAT?
- ❌ "We got in at $X" — got in on WHAT contract?
- ❌ "The trade is up X%" — WHICH trade? State the contract.
- ✅ "The TSM $380/$410 call spread is up 50%"
- ✅ "We bought the SCCO Feb 20 $180/$190 call spread at $2.00"

Subscribers hold multiple positions. "We followed it" means nothing to someone with 3 open trades.

⛔ **HARD RULE: Use Josh's Context as Raw Material.** When Josh provides color, energy, or specific framing for a trade — use it. Don't translate his thesis into generic market language. Don't soften his conviction. His words are raw material for the draft, not suggestions to be paraphrased into something blander.
- Josh says "someone with deep pockets knows the chip downcycle is over" → write THAT, not "institutional investors see potential upside"
- Josh provides urgency/energy about a specific flow → the draft must carry that energy, not flatten it into a summary

⛔ **HARD RULE: Verify Josh's Numbers.** If Josh gives you a stat ("up 90%", "3 winners in a row"), verify it before using it. His back-of-napkin estimates are sometimes approximate. Pull the actual number from the sheet or run the math yourself. If Josh's number is off, use the correct one and flag the discrepancy.

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

Your voice drifts between sessions. You don't notice it, but Josh does — and subscribers notice faster. The only calibration that works is reading what's actually live on the site right now. Your memory of Josh's voice is not reliable enough.

**Read before writing any alert:**
- `references/hot-money-voice.md` — Voice, tone, flow analysis framework. This grounds your sentence structure and word choice. Without it, you default to your own patterns, which read like AI.
- `references/phrase-bank.md` — Rotation phrases. Alerts go to the same subscribers repeatedly. If you reuse "Outstanding trade. Onto the next one." three times in a row, it reads robotic. The phrase bank exists to prevent repetition you won't catch yourself.
- `references/knowledge.md` — Published BUY and SELL alerts. These are the gold standard. Read them because the STRUCTURE of real published alerts is different from what you'll produce from memory. You consistently get ACTION placement, flow detail density, and paragraph rhythm wrong without a recent reference.
- **Pull 3 most recent published alerts of same TYPE (buy or sell) from WordPress.** This is the most important calibration step. Published alerts reflect Josh's latest edits and preferences, which evolve. The examples in knowledge.md may be weeks old. WordPress is the source of truth for what "correct" looks like today.

Hot Money Trader is a **flow-following service**. Lead with dollar amounts and unusual activity signals.

### Voice Rules — From Corpus Extraction (30 Published Alerts)

These rules were extracted from analyzing every published HMT alert. They're not suggestions — they're what Josh actually writes. Full extraction data in `references/voice-extraction.md`.

**Sentence rhythm:** Average 9 words/sentence. 52% of sentences are ≤8 words. Only 6% exceed 18 words. If your draft has sentences averaging 15+ words, you're writing too long. Cut or split.

**Paragraph rhythm:** 48% of paragraphs are ≤15 words. Average 2.2 sentences per paragraph. Dense blocks (41+ words) are only 9% of paragraphs — they're the exception, used for thesis sections with specific numbers.

**Standalone punchy lines:** Every alert has 3-5 lines of ≤5 words sprinkled through the body. "That money knew something." "Same direction. Same day." "That's a thesis." "Cut it." These create the breathing room Josh keeps asking for.

**Paragraph openers:** Start with "And", "That's", "But", "When", "Here's" — direct kicks, not subordinate clauses. Not "While the market was selling off..." but "The market sold off."

**"a single" emphasis:** Josh uses "single strike", "single session", "single day" to hammer concentration. Use it when describing flow.

---

## Anti-AI Language Rules — MANDATORY

These alerts go to paying subscribers. If it reads like ChatGPT wrote it, trust is destroyed.

### Forbidden Words (LLM Filler — Instant Kill)
Never use: journey, navigate, embark, delve, dive, unleash, unlock, leverage, utilize, meticulous, elevate, harness, realm, fascinating, profound, groundbreaking, revolutionary, innovative, disruptive, tapestry, craft, blueprint, transform, paradigm, unprecedented, beacon, moreover, furthermore, consequently, ultimately, essentially, simply, arguably, firstly, secondly, thirdly, in conclusion, in summary, optimize, drive results, implement, seamlessly, effortlessly, streamline, robust, comprehensive, cutting-edge, state-of-the-art, empower

### Banned Patterns
- ❌ "Let's dive into..." / "Let's break this down..."
- ❌ "Here's the thing:" (overused AI crutch)
- ❌ "It's worth noting that..."
- ❌ "This is significant because..."
- ❌ "What this means is..."
- ❌ "In other words..."
- ❌ "To put this in perspective..."
- ❌ "The bottom line is..."
- ❌ "Make no mistake..."
- ❌ "At the end of the day..."
- ❌ Any sentence starting with "So," as a transition
- ❌ Triple adjective stacks ("massive, unprecedented, historic")
- ❌ Explaining what you're about to do ("Let me explain why this matters")

### Voice Killers
- ❌ Hedging: "It could potentially..." — either it is or it isn't
- ❌ Filler transitions: "With that being said..." / "Having said that..."
- ❌ Performative excitement: "This is incredibly exciting!"
- ❌ Teaching tone: "The lesson here is..." / "The key takeaway..."
- ❌ Formal attribution: "According to market analysts..."
- ❌ Smooth transitions between paragraphs — Josh writes in CUTS, not flows

### What Josh Actually Sounds Like
- Short declarative sentences mixed with longer ones
- Em dashes for mid-thought asides — not semicolons
- Specific numbers ($29 million, 55,000 contracts, 2.1% move)
- States facts flat, no emotional performance
- "That's a signal worth following." not "This incredible opportunity shouldn't be missed!"
- Casual but professional — no slang overdose, no corporate polish
- Dismissal pivots: "Doesn't matter." / "That's trading." — then moves on

### Premium Dollar Calculation — ALWAYS MULTIPLY BY 100
Options contracts represent 100 shares each. The dollar figure in copy is:
**contracts × price × 100**
Example: 11,000 contracts × $3.21 × 100 = $3.53 million (NOT $35 million)
Run this math before writing any premium dollar amount. Do not skip.

### Accuracy Rule — ZERO TOLERANCE FOR FABRICATION
- **NEVER make up statistics** — P/E ratios, pullback percentages, earnings numbers, market caps, growth rates
- **If you don't have the number, don't write it.** Leave it out entirely rather than guess.
- **Every factual claim must be either:**
  1. Provided directly by Josh in the trade brief, OR
  2. Verified via a tool call (yfinance, web search, etc.) in this session
- **Before writing any market stat**, run the lookup. Example: "NVDA down 50% from highs" — did you check? If not, delete it.
- **Speculation is allowed** ("Maybe they're betting on the next product cycle") — but it must be clearly framed as speculation, not stated as fact
- This rule exists because we wrote "50% pullback" when it was actually 14%. That kind of error destroys subscriber trust instantly.

### The Test
Read it out loud. Does it sound like a trader talking to his room? Or does it sound like an AI writing a blog post about trading? If the second — rewrite the whole thing.

---

## Service Identity

**Service:** Hot Money Trader  
**Focus:** Unusual options flow — following institutional money  
**Trading:** Single-leg options (calls/puts) and spreads  
**TP/SL:** 40% target, 60% stop

## Alert Types

### 1. BUY Alerts (Unusual Flow Triggers)

**Narrative Arc (not a checklist — each beat raises the stakes):**

Every HMT buy alert tells a story. The flow data is the hook. The thesis explains WHY. The conviction makes it inevitable. Read the gold standard alerts in `references/knowledge.md` before every draft.

**HOOK** — Flow $ + stakes. Dollar amount leads. Always.
- "$4.2 million just dropped on [TICKER] calls"
- "Someone just dropped $X million betting [TICKER] pushes higher in the next X days."
- "And if they're wrong, they lose everything." (optional — ~60% of published alerts use this)

**SETUP** — Company + price + stock chart.
- Company context: 1-2 sentences. What they do + why it matters for THIS trade.
- Price line: "Shares are trading at $X" — can combine with options activity ("...and options activity is screaming: [numbers]") or keep separate. Match the rhythm of the story.
- Stock chart goes right after the price line.

**PIVOT** — "Here's what caught my attention:" + flow chart.
- This line is the turn. Everything before it is setup. Everything after it is the story.
- Flow chart image follows immediately.
- **Flow chart source:** Josh saves screenshots to Mac Downloads as `OptionAlert_TICKER.jpeg`. Pull via SSH, upload to `/var/www/html/charts/`, set `www-data:www-data` ownership.

**STORY** — Flow details + catalyst/thesis. This is where conviction lives.
- Flow details first: contracts, strikes, expirations, what makes it unusual. Specific numbers. "8,500 contracts. Single strike. $4.2 million."
- Then the WHY — the specific, non-obvious catalyst that makes this trade feel inevitable. This comes AFTER the flow, not before. The flow is the evidence. The thesis explains the evidence.
- **The research layer is what separates good from great.** Generic catalysts ("AI is growing", "geopolitical tensions") don't create urgency. Find the ONE SPECIFIC detail that makes a subscriber think "oh, that's why someone just bet millions." Examples from published gold standards:
  - USO: Not "Iran conflict" → "USS Tripoli carrying Marines last reported outside Singapore heading toward the Strait of Hormuz" (specific warship, specific chokepoint, 20% of world oil supply)
  - DELL: Not "AI servers growing" → "Super Micro got hit with a federal indictment. Dell is the compliance-first alternative with a $43B backlog already in hand" (competitor eliminated, DELL only one standing)
  - TSM: Not "big call volume" → "I monitored open interest overnight. 103,000 contracts weren't there before. This is newly opened money" (verified new positioning, not rolling)
- This section is 2-4 paragraphs. Each paragraph has ONE idea. Let it breathe.
- Energy and conviction come from specificity and stakes, not adjectives.

**ACTION** — Bold. Full contract. TP/SL.
```
ACTION: Buy-to-Open [TICKER] [EXP] $[STRIKE] [Call/Put] at $[PRICE] or better
OR: Buy-to-Open [TICKER] [EXP] $[STRIKE]/$[STRIKE] [Call/Put] Spread at $[PRICE] or better

Take Profit: $[TARGET] ([X]% gain)
Stop Loss: $[STOP] ([X]% loss)
```
- Spread rationale after ACTION if applicable: "The spread caps the risk while giving full exposure to a move through $X."

**CONVICTION CLOSE** — Reinforce the flow signal. One paragraph.
- "That's a signal worth following."
- OR tie the closing back to the specific flow: "$28.5 million in fresh premium. Single session. Single direction."
- The close should feel like the final piece of evidence that makes the trade obvious.

**Image block format (all HMT alerts):**
```html
<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/FILENAME" alt="Description" style="width:800px"/></figure>
<!-- /wp:image -->
```
Never upload to WP media library. Always use `/charts/` URL directly. Always `style="width:800px"`.

**Chart order:** Stock chart after price paragraph → "Here's what caught my attention" → Options flow chart.

**Real Example Structure (STM 4833):**

```
BUY ALERT: $1 Million Bet on STM — Chip Maker Ready to Rip

Someone just dropped $1 million on STMicroelectronics calls — betting shares rip higher in the next 43 days.

And if they're wrong, they lose everything.

STMicroelectronics (STM) makes the chips that power everything from cars to iPhones.

Last week, the company delivered a one-two punch: Q4 earnings beat expectations (marking the "return to year-over-year growth" according to the CEO) — and three days ago, they closed their acquisition of NXP's MEMS sensor business, expanding their grip on automotive and industrial markets.

The chip downcycle is over. And someone with deep pockets knows it.

Shares are trading at $29 and options activity is screaming: 11,000 calls traded vs just 700 puts. That's 2x the normal expected volume.

Here's what caught my attention:

[Flow chart image]

This is back-to-back days of aggressive call buying.

Yesterday, buyers paid $1.55 for the March 20 $30 calls and added 5,000 contracts to open interest. Today? They're back — 7,000 more contracts traded at $1.44. That's $1 million in premium on a single strike.

When buyers show up two days in a row at similar prices, they're not hedging. They're building a position.

**ACTION: Buy-to-Open STM March 20, 2026 $30 Call at $1.35 or better**

Take Profit: $1.89 (40% gain)
Stop Loss: $0.54 (60% loss)

Earnings catalyst behind them. Acquisition complete. Hot money piling in while the rest of the market bleeds.

That's a signal worth following.
```

**Real Example Structure (TSM 4879 — spread):**

```
Someone just dropped $8.2 million betting TSM pushes higher in the next 38 days.

And someone with even deeper pockets? They put $17.5 million on the same bet — but gave themselves until January 2027 to be right.

Two different trades. Same stock. Same direction. Same day.

Taiwan Semiconductor (TSM) manufactures every cutting-edge AI chip on the planet — NVIDIA, AMD, Apple, all of them. When AI spending accelerates, TSM's foundries are where the money lands.

Shares are trading around $215, and the Smart Money is showing up in size.

Here's what caught my eye:

[Flow chart]

The March 20 $370 calls saw more than 4,300 contracts trade today. One buyer alone paid $2.4 million for 1,500 contracts in a single clip. In total, about $8.2 million in premium — all opening buyers, all betting shares continue higher.

That's the short-term money talking.

But here's what takes this from interesting to hard-to-ignore: 5,000 contracts traded in the January 2027 $450 calls — $17.5 million in a single strike. That's someone betting shares nearly double from here over the next year. That's not a trade. That's a thesis.

When short-term flow and long-term conviction line up on the same name, same day — that's Wall Street telling you something.

We followed similar activity in TSM back on January 16th and got caught in the market downturn. The difference? That trade had 7 days of life. This one gives us 38.

More time means more room to be right.

**ACTION: Buy-to-Open TSM March 20, 2026 $380/$410 Call Spread at $7.45 or better**

Take Profit: $11.18 (50% gain)
Stop Loss: $2.98 (60% loss)

The spread structure caps the risk while giving us full exposure to a move higher. We need shares to push through $380 and toward $410 over the next 38 days.

Big Money showed their hand twice today — the fast money says now, the deep pockets say it's just getting started. That's a signal worth following.
```

### 2. SELL/EXIT Alerts — Winners

**Narrative Arc:** Result → Entry recall (with flow details) → ACTION → Forward spec + dismiss → Celebration → Close.

Every win alert tells the story of a signal that worked. The flow details from the original buy alert get recalled. The subscriber gets credit. Length varies by story — BP was 4 paragraphs, USO was 11. Match the complexity of what happened.

**Before writing:** Pull the ORIGINAL buy alert from WordPress and recall the specific flow details. Search for WHY the stock is moving today. Both go into the draft.

**Key beats:**
- **OPENER:** Current price + gain. One line. "Shares of [TICKER] are at $X and our trade is up X%."
- **ENTRY RECALL:** What the flow signal was, with specific details. "[X] days ago we spotted $XM dropping on [TICKER] calls right after [catalyst]." Include the detail that made it interesting (routing, urgency, concentration).
- **"We targeted X%. We got Y%."** — Clean. Punchy.
- **ACTION:** Full contract. Bold. "Sell-to-Close [CONTRACT] at $[PRICE] or better"
- **FORWARD SPEC + DISMISS:** "Could [TICKER] keep running? Maybe. But we came for a trade, not a thesis." Today's news/catalyst goes here.
- **SUBSCRIBER CELEBRATION:** "You spotted... You positioned... Now you're banking X%." The subscriber is the hero.
- **CLOSER:** "Outstanding trade. Onto the next one." (vary it — don't copy this verbatim every time)

**Voice note:** Published alerts use both "we" and "you." Body narrative is "we" ("we targeted," "we got"). Celebration paragraph switches to "you." Don't force one framing throughout — match the published alerts.

**Urgency variant (TSM 4890):** When the trade hit target but is pulling back fast, lead with urgency: "The spread hit $11.60 yesterday. It's now at $8.40. Take what you have now." ACTION comes immediately.

**Chart in sell alerts:** Usually no chart. Exception: when the stock moved dramatically and the visual adds value (USO 4998 included a chart because oil went from $88 to $111).

**Real Example (SCCO 4686 — 100% winner):**

```
Shares of SCCO are at $176.51 and our trade is up 100%.

Three days ago we spotted $200K dropping on SCCO calls right after copper ripped 6%.

Someone bought 860 contracts at a single strike — and they used sophisticated routing to pay up at $2.30 when the market was only 2.15x2.30. That urgency meant something, and you acted on it.

We targeted 50%. We got 100%.

**ACTION: Sell-to-Close SCCO FEB 20 $180/$190 call spread at $4.00 or better**

That $200K buyer might be playing for something bigger. Maybe copper's got another leg up.

Maybe there's news coming on China demand or supply disruptions. Doesn't matter — we came for a trade, not a thesis. The spread's at max efficiency right here.

You spotted hot money chasing copper momentum. You positioned before the crowd caught on. Now you're banking 100% while they're still reading headlines about commodity cycles.

Outstanding trade. Onto the next one.
```

**Real Example (TSM 4890 — partial winner, urgency version):**

Note: This is the "take profit NOW before it evaporates" variant. Use when the trade hit target but is pulling back fast.

```
The TSM $380/$410 call spread hit $11.60 yesterday — 56% gain. It touched $11.25 this morning. It's now at $8.40.

If you took profit at the 50% target ($11.18) — you already banked the win.

If you're still holding, markets are rolling over and the spread is giving back gains fast. Take what you have now.

**ACTION: Sell-to-Close TSM MAR 20 $380/$410 Call Spread at $11.18 or current prices**

We came for 50%. The spread delivered. Don't let a winner turn into a loser.

Outstanding trade. Onto the next one.
```

### 3. SELL/EXIT Alerts — Losers

**Narrative Arc:** Bad news immediately → What happened → ACTION (early) → Math → Brief honest explanation → Cut it.

Loss alerts are SHORT. No excuses, no thesis recaps, no sugarcoating. The subscriber needs to know: what happened, what to do, and that you're moving on.

**Key beats:**
- **OPENER:** Bad news first. Every published loss alert opens with the damage.
  - "Bad news. We're cutting [TICKER] for a loss." (TECK, NVDA)
  - "[TICKER] isn't getting to $X this week." (HMY, AR)
  - "[TICKER] didn't follow the flow." (general)
- **WHAT HAPPENED:** 2-3 sentences. What the signal was, what went wrong instead. Recall the original flow, then say what broke.
- **ACTION:** Bold. Early (paragraph 4-5, not buried at the bottom). "Sell-to-Close [CONTRACT] at $[PRICE] or current prices"
- **MATH:** "We paid $X. Getting out at $Y. That's the loss." One line. No bullet breakdown.
- **HONEST EXPLANATION:** 1-2 sentences on why. "The flow was real. The tape didn't cooperate." / "The signal was right on direction. These strikes needed a bigger breakout." / "This market is not rewarding good news right now."
- **CLOSER:** "Cut it. Next setup's already forming." / "Clear it out. Onto the next one."

**Length varies:** Most losses are 8 paragraphs. NVDA 4981 was 11 because 17 days of macro events needed explaining. Match the complexity.

**Never include in loss alerts:**
- Long thesis recaps
- "I got this one wrong" (old template, not current voice)
- Excuses or blame
- Charts (loss alerts don't need visuals)

5. NO EXCUSES
   Short explanation if needed, but don't dwell

6. CLOSER
   "We can cut this one and move onto the next trade."
   OR "Next setup's already forming."
```

**Keep it SHORT. Losses don't need long explanations.**

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

You are not a reliable self-assessor of your own output. This is not an insult — it's a measured observation based on repeated failures. You consistently miss: charts in sell alerts that shouldn't have them, ACTION placement that doesn't match published examples, missing subscriber celebration language, and structural drift from what's actually live on WordPress. The QC step catches what you can't see in your own work.

Read and run `skills/alert-qc.md` before presenting any draft to Josh. If you skip this, Josh becomes the QC layer, which defeats the purpose of having you write alerts.

## Step 0: Hard Gate — Date, Time, Price

These three values are wrong more often than you think. Options prices move fast, dates get confused across sessions, and you've written alerts with yesterday's price more than once. Running this gate takes 10 seconds and has caught real errors that would have gone to thousands of subscribers.

Before writing a single word, run and print:

```
DATE/TIME: [session_status 🕒 line]
TICKER:    $XXX.XX (live)
CONTRACT:  [TICKER] [EXP] $[STRIKE] [Call/Put]
```

Josh sees this output and can catch errors before any work is done. A correction email to subscribers is always worse than 10 seconds of verification.

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
- **If no entry price was provided** → check the option chain:

```bash
cd /home/clawdbot/clawd && source .venv/bin/activate && python3 -c "
import yfinance as yf
t = yf.Ticker('TICKER')
chain = t.option_chain('YYYY-MM-DD')
print(chain.calls[chain.calls['strike'] == STRIKE][['strike','lastPrice','bid','ask']])
"
```

After running, output: `ENTRY PRICE: $X.XX (live mid)`

### 3. Generate branded chart

Every HMT alert needs a stock chart. Subscribers expect a consistent visual format. The chart also forces you to look at the actual price action, which sometimes contradicts the narrative you're about to write.

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

- [ ] Read `references/hot-money-voice.md` — because your voice drifts every session and you don't notice
- [ ] Pull 2 most recent published HMT alerts of same TYPE from WordPress and read them — because the structure on the live site may differ from what's in knowledge.md, and Josh's preferences evolve
- [ ] Verify flow data is accurate — because you've fabricated contract counts and premium totals when you didn't have real numbers, and a subscriber who checks will destroy trust instantly
- [ ] Chart image saved to `/var/www/html/charts/` and referenced in alert — because you've referenced chart URLs that didn't exist

---

## Publishing Pipeline

### Step 1: Write Alert

Read `references/hot-money-voice.md` and write the alert. Output in WordPress block format (`<!-- wp:paragraph -->`).

### Step 2: Henry QC — Structural Comparison

This step exists because you consistently believe your draft matches published structure when it doesn't. The only way to catch structural drift is to have the real thing open next to your draft. "I'm confident it matches" has been wrong every time you've said it.

```bash
sudo wp --path=/var/www/html --allow-root post list --post_type=premium-post --posts_per_page=5 --post_status=publish --fields=ID,post_title --orderby=date --order=DESC
sudo wp --path=/var/www/html --allow-root post get <ID> --field=post_content
```

Pull the 2 most recent published HMT alerts of the same TYPE from WordPress. Read them. Then compare your draft against them, checking:

- [ ] Opens with dollar amount of institutional flow — not hype? (You default to hype openers when you skip this)
- [ ] Specific flow numbers included (contracts, volume vs normal, call/put ratio)? (You round or estimate when you should use exact figures)
- [ ] Entry date and price correct? (verify from sheet — you've gotten dates wrong)
- [ ] Current stock price verified via yfinance? (This is a cross-check against Step 1)
- [ ] WordPress block format throughout? (You sometimes drop the format mid-alert)
- [ ] For sell alerts: ACTION early, math simple, closer punchy? (You consistently bury ACTION too low in sell alerts — the BP alert was the latest example)

Fix anything before proceeding. Josh should never see a draft that hasn't passed this. If he's catching structural issues, this step failed.

### Step 3: Create WordPress Draft

```bash
POST_ID=$(sudo wp --path=/var/www/html --allow-root post create /tmp/alert-content.html \
  --post_type=premium-post \
  --post_status=draft \
  --post_title="BUY ALERT: [TITLE]" \
  --porcelain)
echo "Draft created: Post $POST_ID"
```

**⚠️ Always `draft`. Never `--post_status=publish` on create.**

### Step 4: Set Taxonomies

```bash
sudo wp --path=/var/www/html --allow-root post term set $POST_ID content-type trade-ideas-updates --by=slug
sudo wp --path=/var/www/html --allow-root post term set $POST_ID product-categories hot-money-trader --by=slug
```

### Step 5: Send Draft Link to Josh

Channel: `#trade-alerts` (ID: `1473066624993988739`)

```
📋 **[TICKER] HOT MONEY TRADER — DRAFT READY FOR REVIEW**

**Post:** [Alert title]
**Preview:** https://joshbelanger.com/?post_type=premium-post&p=[POST_ID]&preview=true

**Trade:** [Full action line]
**Flow:** $[X]M on [strikes/expiry] — [key signal]
**TP:** $X (X%) | **SL:** $X (X%)        ← BUY
**Entry:** $X | **Exit:** ~$X | **P/L:** ~X%  ← SELL

✅ to publish | ❌ to revise
```

### Step 6: Wait for Approval

Do NOT proceed until Josh explicitly approves via Telegram.

### Step 7: On Approval — Publish Existing Draft + Sheet + Log

**⚠️ CRITICAL: DO NOT create a new post. DO NOT rewrite the alert. The draft ALREADY EXISTS from Step 3. Your ONLY job is to publish it.**

When spawning the publish agent, pass the EXACT post ID from Step 3. The agent task should be:

```
Publish existing WordPress draft Post [POST_ID] for Hot Money Trader. DO NOT create a new post.

1. VERIFY the post exists and is a draft:
   sudo wp --path=/var/www/html --allow-root post get [POST_ID] --fields=ID,post_status,post_title
   If post_status is NOT "draft", STOP and report the error.

2. Publish it:
   sudo wp --path=/var/www/html --allow-root post update [POST_ID] --post_status=publish

3. Get URL:
   sudo wp --path=/var/www/html --allow-root post get [POST_ID] --field=url

4. Update sheet — read skills/trade-sheet-updater/references/hot-money.md for the exact schema BEFORE building the payload. Do not guess field values from memory.

   BUY payload (exact field values required — do not deviate):
   {
     "action": "buy",
     "ticker": "[TICKER]",
     "entryDate": "[today MM/DD/YYYY]",
     "signalType": "",
     "strategy": "Call Spread",
     "expCycle": "[expiry M/DD/YYYY]",
     "shortStrike": "[short strike number]",
     "longStrike": "[long strike number]",
     "type": "C",
     "entryPrice": [price as number],
     "takeProfit": [tp as number],
     "stopLoss": [sl as number],
     "buyAlertLink": "[published URL]"
   }

   SELL payload:
   {"action":"sell", "ticker":"[TICKER]", "exitPrice":[price], "exitDate":"[date]", "sellAlertLink":"[URL]"}

   Use the redirect curl pattern from trade-sheet-updater/SKILL.md. After posting, verify the row in the sheet before reporting success.

5. Log: cd /home/clawdbot/clawd && ./scripts/log-activity.sh "Published [TICKER] Hot Money Trader [buy/sell] alert (Post [POST_ID])" "collaborative"
```

**The agent must NOT:**
- Create any new posts (no `wp post create`)
- Rewrite or modify the alert content
- Generate new alert copy

Publishing triggers mu-plugin → n8n → email + SMS to all Hot Money Trader subscribers automatically.

---

## Service Voice Fingerprint

**HMT phrases — YOURS (use these, they define the service):**
- "Here's what caught my attention:" (before flow chart)
- "$X million just dropped on [TICKER] calls"
- "That's a signal worth following."
- "When this much money floods into one strike..."
- "They're not hedging. They're positioning."
- Dollar amounts and contract counts leading every beat
- **"We" framing in the body** — "We targeted 40%. We got it." / "We followed the flow." The subscriber celebration at the end can use "you" sparingly ("You positioned before the crowd") but the body narrative is "we." Check published alerts on the live site — they use "we" predominantly. If your draft has more "you" than "we" in the body, fix it.

**BANNED — these belong to OTHER services:**
- ❌ "What This Trade Looks Like" (that's OI)
- ❌ "The 48-Hour Window Just Opened" (that's 48HC)
- ❌ Pattern names: Bull Surge, Bear Plunge, U-Turn, Two-Way Trigger (those are OI)
- ❌ Insurance analogies: "like State Farm paying a claim" (that's 48HC)
- ❌ "25% return for 48 hours of patience and probabilities" (that's 48HC)
- ❌ "Our system says to exit" (that's OI)
- ❌ Calm/insurance tone — HMT is aggressive conviction, not measured patience

**If you catch any banned phrase in your draft, you've got service voice bleed. Stop and re-read `references/hot-money-voice.md`.**

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

---

## Gotchas (from Real Sessions)

**Mar 27-Apr 2 — USO title/body number mismatch**
Updated body gain percentage but left the old number in the title. Post-edit consistency gate now exists to prevent this. After ANY edit, re-read the FULL draft.

**Mar 27-Apr 2 — "Thesis played out bigger than expected" = lazy**
Generic filler that says nothing. What SPECIFICALLY played out? What moved? By how much? Replace every generic statement with the specific fact it's supposed to represent.

**Mar 27-Apr 2 — Not elaborating on Josh's energy/context**
Josh provided specific color about a trade and the draft flattened it into generic market language. His words are raw material. Use them.

**Mar 27-Apr 2 — Vague position references**
"We followed it" without stating what contract was traded. Subscribers need specifics: ticker, expiration, strike, direction. Every mention of the trade must be fully specified.

**Mar 27-Apr 2 — 6+ revision rounds on single alerts**
Root cause every time: skipped the mandatory reads. Drafted from memory. Memory was wrong on structure, voice, and energy. The reads take 2 minutes. Skipping them costs 30+ minutes in revisions.

**Apr 3, 2026 — Fabricated volume stat in eval**
Wrote "Normal daily call volume on CRWD runs around 15,000 contracts across all strikes" — completely made up. No source, no tag. The three-source gate caught it on review but not during drafting. **If you're generating a stat to provide context (normal volume, historical average, typical range), it needs a source tag just like any other fact. If you don't have the number from Josh or a tool, don't write the sentence. Estimated context stats are still facts.**

**Apr 3, 2026 — "You" vs "We" framing**
Used "You spotted... You positioned... Now you're banking" throughout the win alert body. Published HMT alerts use "we" in the body. "You" is for the subscriber celebration paragraph at the end, used sparingly. The body narrative is "we" — we're in this trade together. Checked against SCCO gold standard in knowledge.md (which uses "you") but the live site has evolved. **Live site always wins over knowledge.md examples.**

---

## Reference

**WordPress taxonomy slug:** `hot-money-trader`  
**Content type slug:** `trade-ideas-updates`  
**Chart directory:** `/var/www/html/charts/` → `https://joshbelanger.com/charts/[filename]`

**Image block format -- all HMT alerts:**
```html
<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/FILENAME.png" alt="Description" style="width:800px"/></figure>
<!-- /wp:image -->
```
Never upload to WP media library. Always use `/charts/` URL directly. Always `style="width:800px"`.

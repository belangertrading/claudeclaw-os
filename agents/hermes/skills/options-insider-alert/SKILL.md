---
name: options-insider-alert
description: End-to-end Options Insider trade alert pipeline. Handles buy alerts (pattern triggers), sell/exit alerts (winners and losers), WordPress publishing, sheet updates, and activity logging. Use when publishing any Options Insider trade alert.
---

# Options Insider Alert Publisher

📋 **Read `data/corrections.log` at the start of every session.** It contains the most recent corrections from Josh. If a lesson has been corrected more than once, it's a pattern — treat it as a hard rule.

⛔ **HARD RULE: Never show alert copy in chat. Never paste drafts into the conversation. The first thing Josh sees is a WordPress preview link.** No exceptions. Follow the pipeline below.

⛔ **HARD RULE: QC before preview link, every time.** Run `skills/alert-qc.md` BEFORE sending the preview URL to Josh. If Josh has to ask "did you review this?" — you failed. The QC step is not optional and not a mental check. Run the commands.

⛔ **HARD RULE: TP/SL comes from the pattern table, not memory.** Before writing the ACTION block, look up the pattern in the Pattern Reference table at the bottom of this skill. U-Turn Velocity ≠ U-Turn Standard ≠ Bull Surge. Getting this wrong sends subscribers the wrong exit levels. Check the table every single time.

⛔ **HARD RULE: Three-Source Gate.** Every factual claim in alert copy (earnings dates, price levels, market events, statistics, TIME REFERENCES) must come from one of three sources in THIS session: (a) Josh's exact words, (b) a tool result (search, price lookup, sheet data), or (c) a search you ran and can cite. If you can't point to where you got it RIGHT NOW, cut the sentence. No exceptions. Your training data confidence is not a source — it's a liability.

**This includes temporal claims.** "Overnight," "about an hour," "last week," "two days ago" — these are factual claims. If you didn't check the timestamp, you don't write the time reference.

**Highest fabrication risk: background research color.** Analyst targets, volume comparisons, historical price stats, and industry averages you "just know" are the #1 source of unsourced claims. These feel like harmless context but they're factual claims that need [SEARCH] or [TOOL] tags. If you can't show the tag, cut the sentence. Flagged in 3/3 buy alert evals.

⛔ **HARD RULE: Post-Edit Consistency Gate.** After making ANY revision to a draft:
1. Re-read the FULL draft top to bottom — not just the changed section
2. Verify title matches body numbers
3. Verify all stats, dates, and percentages are internally consistent
4. If you changed a number anywhere, grep the entire draft for the OLD number

⛔ **HARD RULE: Use Josh's Context as Raw Material.** When Josh provides a specific thesis, energy, or framing — use it. Don't translate his words into softer, more generic language. His thesis is the draft's thesis.
- Josh says "people don't stop traveling, they trade down from hotels to Airbnb" → write THAT
- ❌ "low debt, high sensitivity to economic growth" (your paraphrase that strips Josh's insight)

⛔ **HARD RULE: Read Before You Write — No Exceptions.** Before writing ANY alert (buy or sell), you MUST:
1. Read `references/options-insider-voice.md`
2. Read `references/knowledge.md`
3. Pull and read 2 most recent published alerts OF THE SAME TYPE (buy→buy, loss→loss, win→win) from WordPress

This is not optional prep. This is a gate. If you have not completed all three reads in THIS session, you do not write. "I remember how they sound" has been wrong every time it was tested. Your voice drifts between sessions and you don't notice. The reads are the calibration — skip them and the draft will need 3-4 revision rounds instead of 0-1.

**Mar 30, 2026 failure:** AMD OI buy alert took 4 revision rounds because Dash skipped the read step, drafted from memory, and used HMT structure ("Here's what caught my attention") in an OI alert. The read step would have caught this in 30 seconds.

⛔ **HARD RULE: Know Your Patterns — Direction Is Non-Negotiable.**

| Pattern | Direction | What It Means | We Buy |
|---------|-----------|---------------|--------|
| Bull Surge | BULLISH | Stock about to rip higher | CALLS |
| U-Turn / U-Turn Velocity / U-Turn Standard | BULLISH | Stock reversing from down to up | CALLS |
| Bear Plunge | BEARISH | Stock about to drop | PUTS |
| Two-Way Trigger | NEUTRAL | Could go either way | CALLS + PUTS |

**Bear Plunge = we are betting the stock DROPS. We buy PUTS.** If your draft describes a Bear Plunge as "buying a dip" or "looking for shares to rip higher," you have the pattern backwards. Stop and re-read the table.

**Mar 30, 2026 failure:** AMD Bear Plunge alert described the pattern as buying a dip — the exact opposite of what Bear Plunge means. The pattern signals a DROP and we buy PUTS.

⛔ **HARD RULE: Math Verification on Sell/Exit Alerts.** Before presenting any sell alert:
1. Pull the entry row from the OI sheet — get the ACTUAL entry price, entry date, TP%, SL%
2. Calculate the P&L math yourself: `(exit - entry) / entry × 100`
3. Verify every number in the copy matches the sheet, not your memory
4. If referencing prior trades in the opener (e.g., "463% total returns"), pull that number LIVE from the sheet — do not reuse a number from a previous session
5. If referencing time elapsed ("one rough week"), count the actual calendar days from entry date to today

**Mar 30, 2026 failures:** ABNB alert used stale "463% total returns" without checking if the number changed after recent losses. Also wrote "one rough week" when it had been two weeks since entry. Both would have been caught by checking the sheet.

## Pipeline

1. **Step 0:** Verify trade details (price, contract, cross-check inputs)
2. **Step 1:** Read voice references + knowledge.md + pull 3 recent alerts from WordPress
3. **Step 2:** Write alert draft in WordPress block format
4. **Step 3:** Henry QC (run commands, not mental checks)
5. **Step 4:** Create WordPress draft + set taxonomies
6. **Step 5:** Send draft link to Josh
7. **Step 6:** Josh approves → ACT IMMEDIATELY
8. **Step 7:** Publish + update sheet + log activity

## Voice & Style — Why Every Read Matters

Your voice drifts between sessions. You don't notice it, but Josh does — and subscribers notice faster. The only calibration that works is reading what's actually live on the site right now. Your memory of how OI alerts sound is not reliable enough.

Read ALL THREE before writing any alert. If a path fails, SEARCH for it — do not skip.

- `references/options-insider-voice.md` — Voice, tone, structure, patterns, TP/SL rules. OI has a pattern-driven voice that's different from HMT (flow-driven) and 48HC (fear-selling). Without reading this, you blend the service voices. Subscribers can tell.
- `references/phrase-bank.md` — Rotation phrases. Alerts go to the same subscribers repeatedly. If you reuse "Get in, get the X%, get out" in every alert, it reads robotic. The phrase bank prevents repetition you won't catch yourself.
- `references/knowledge.md` — Published BUY, WIN, and LOSS examples. Study the structure, not the words. Your default structure consistently differs from what's actually published — especially in loss alerts, where you add forbidden elements (thesis recaps, "that stings," total returns %) without realizing it.

Then pull 3 most recent published alerts of same TYPE from WordPress. This is the most important calibration step — published alerts reflect Josh's latest edits, which evolve. Knowledge.md may be weeks behind.

```bash
sudo wp --path=/var/www/html --allow-root post list --post_type=premium-post --posts_per_page=10 --post_status=publish --fields=ID,post_title --orderby=date --order=DESC
```
Read the content of the 3 most relevant. Compare structure line by line against what you write.

Options Insider is a **momentum-triggered pattern service**. Language must reflect this.

---

## Research Before You Write — MANDATORY

Before drafting any alert copy, search for current market context. This applies to BOTH buy and sell alerts.

**For SELL/EXIT alerts especially — the exit reason must be rooted in what's actually happening, not assumed.**

```
1. web_search: "[TICKER] stock news today"
2. web_search: "market news today [date]" — macro environment, what moved markets in the last 2-3 days
3. web_search: "[sector] stocks [date]" — if the trade is sector-driven (travel, energy, banks), check if the sector shifted
4. web_search: "[any company/event you plan to reference] [date]" — verify BEFORE writing
```

**Market environment context is required for exit alerts.** The reason the trade isn't working is almost always a market or sector shift. Find it, verify it, use it in the copy. This makes the exit feel honest and grounded — not like a random stop loss.

Examples of what to look for:
- Sector reversal: "oil pulled back, travel stocks caught a bid" → that's the exit reason
- Macro shift: "risk-off unwound, the whole market ripped" → that context belongs in the alert
- Individual catalyst: "earnings beat, short squeeze, upgrade" → explain what hit you

**If you plan to reference it, you must have searched for it first. No exceptions.**
- Wrong: "Marvell reported last night" (assumed, not verified)
- Right: Search "MRVL earnings date 2026" → confirm March 5 → then write "Five days ago, Marvell reported..."

Any fact that cannot be verified by search gets cut. Omit > invent.

---

## Pre-Present QC — Why This Exists

You are not a reliable self-assessor of your own output. This is a measured observation: you consistently miss structural drift from published examples, forbidden elements in loss alerts, and pattern stat fabrication (the SCHW incident where you invented a W-L record). The QC step catches what you can't see in your own work.

Read and run `skills/alert-qc.md` before presenting any draft to Josh. If you skip this, Josh becomes the QC layer, which defeats the purpose of having you write alerts.

## Step 0: Hard Gate — Date, Time, Price

These three values are wrong more often than you think. Options have specific expirations, and writing an alert with the wrong strike or date means subscribers enter the wrong trade. The SCHW correction email happened because contract details weren't cross-checked. Running this gate takes 10 seconds.

Before writing a single word, run and print:

```
DATE/TIME: [session_status 🕒 line]
TICKER:    $XXX.XX (live)
CONTRACT:  [TICKER] [EXP] $[STRIKE] [Call/Put]
```

Josh sees this output and can catch errors before any work is done. A correction email to subscribers is always worse than 10 seconds of verification.

---

## Step 1: Verify Before You Write

**Required output — show these lines before writing any alert copy:**

### 1. Verify live stock price
```bash
python3 /home/clawdbot/clawd/scripts/get_price.py TICKER
```
Fallback:
```bash
cd /home/clawdbot/clawd && source .venv/bin/activate && python3 -c "import yfinance as yf; print(yf.Ticker('TICKER').fast_info['lastPrice'])"
```

### 2. Verify entry price
- Josh provided a price → use it: `ENTRY PRICE: $X.XX (provided by Josh)`
- No price given → check option chain live

### 3. Cross-check contract details
**⚠️ If Josh provides screenshots AND text, cross-check expiration, strikes, and strategy.**
**If there's a discrepancy, ASK Josh immediately. Do not assume either is correct.**
A correction email to thousands of subscribers is always worse than one clarifying question.

### 4. Generate branded chart
```bash
cd /home/clawdbot/clawd && source .venv/bin/activate && python scripts/generate-chart-v4.py TICKER --days 90 --sma 50,200 --annotation "SIGNAL_TYPE"
```
Replace SIGNAL_TYPE with the OI signal (Bull Surge, U-Turn, Bear Plunge). The script outputs a URL at `https://joshbelanger.com/charts/...` — use this in the "What This Trade Looks Like" section of the alert.

### 5. Required output before proceeding
```
VERIFIED: [TICKER] = $XXX.XX (live)
ENTRY PRICE: $X.XX (provided by Josh / live mid)
CONTRACT: [TICKER] [EXP] $[STRIKE] [Call/Put] (confirmed)
CHART: https://joshbelanger.com/charts/[filename].png
```

---

## Alert Structures

### Format Rules (Apply to Every Alert, Every Time)

**Opening — short, punchy, breathing room:**
Each sentence is its own paragraph. No compound sentences crammed together. The opening establishes what happened, why the pattern fired, and the record. That's three separate beats — three separate paragraphs minimum.

Wrong:
> "ABNB is at $132 and our U-Turn Velocity just fired. The one that catches stocks right as they flip from pressure to momentum. Airbnb runs the largest short-term rental marketplace in the world. Pattern is 6-0 with 463% total returns. It just triggered again."

Right:
> "Two weeks ago, the ABNB Bear Plunge fired."
>
> "Now the U-Turn Velocity just fired. Looking for shares to rip higher."
>
> "ABNB is at $132.03. The pattern is 6-0 on ABNB over the past two years with 463% total returns."
>
> "It just triggered again."

**Body — one thought per paragraph:**
Every paragraph does exactly one job. If you can split a paragraph into two separate ideas, split it. Dense blocks of connected sentences = wrong. Each new idea = new paragraph. Read the draft and ask: does every paragraph have one point? If not, break it.

**The test before you submit:** Read it out loud. If you run out of breath, the paragraph is too long.

### BUY Alerts

**Narrative Arc (not a checklist — same arc, different story every time):**

Every OI buy alert tells a pattern story. The pattern fires, the fundamentals explain why NOW, the conviction makes the trade obvious. Read the gold standard alerts in `references/knowledge.md` before every draft.

**HEADLINE:** `TRADE ALERT: [TICKER] [Pattern] Just Fired — [X]% Pattern`

**OPENER** — Tension, contrast, or surprise. NOT a company description. Each alert finds its own angle.

**PATTERN INTRO** — Price + pattern + company context + stats + "It just triggered again."
- Company context: 1-2 sentences that fit THIS trade (mispricing / hidden catalyst / re-trigger / obscure ticker)

4. [CUSTOM BOLD HEADLINE — the story in one line]
   2-4 short paragraphs, no bullets. ONE narrative thread.
   150-250 words. Do NOT try to cover everything.
   ✅ One clear story with specific facts
   ❌ Listing every business segment
   ❌ Rehashing what subscribers already know

5. TIE-IN (1 sentence bridging research to ACTION)

6. ACTION (bold) + TP/SL + optional spread alternative

7. CLOSING — Days to exp, pattern conviction, "Get in, get the X%, get out."

8. "What This Trade Looks Like" + chart image
```

**Company context sentence — NOT a template:**
Each trade is different. Don't force a formula.
- **Mispricing** (BAC): "second-largest bank...sitting on a post-earnings overreaction"
- **Hidden catalyst** (MGM): "most iconic portfolio on the Strip...market treating it like a dead trade"
- **Re-trigger** (TSLA): Skip the intro — subscribers know Tesla. Lead with the pattern re-firing.
- **Obscure ticker** (HNRG): Needs more context — subscribers may not know it.

### SELL/EXIT — Winners

See `references/knowledge.md` for full examples. Structure:
```
1. OPENER (varies — "You caught a quick one" / "This one made you earn it")
2. Current price + context vs entry
3. Trade recap + what happened
4. Dollar math (entry → exit, % gain)
5. ACTION: Buy-to-Close / Sell-to-Close
6. Pattern record (X-Y)
7. Closer (varies)
```

### SELL/EXIT — Losers

See `references/knowledge.md` for full examples. Structure:
```
1. OPENER: Price + % down. "[TICKER] is at $X and our options trade is down X%." Lead with the damage.
2. ENTRY CONTEXT: "Shares were at $X when the [Pattern] triggered on [Month Xth]. X days later, [what reversed the trade]."
3. STOP CONFIRMATION: "Our system says to exit at the X% stop loss. With [time context], this one isn't working."
4. ACTION (comes EARLY — bold)
5. MATH: Entry price → exit price, % loss. One sentence.
6. SETUP RECAP (2-3 sentences): Why the trade made sense. What actually happened. No apologizing, no "I got this wrong."
7. CONTEXT CLOSER: Acknowledge the stretch honestly if it's been a tough run. Short, direct.
8. PERFORMANCE STATS: "Since inception: X winners, average gain of X%." Pull live from sheet before writing. Do NOT fabricate.
9. CLOSER: "Cut it. Next setup is coming." (vary slightly each time)
```

**FORBIDDEN in loss exits:** "I got this one wrong" opener, long thesis recap, "That stings", "What This Trade Looks Like" section, spacer blocks, any fabricated stats.

**REQUIRED in loss exits:** Performance stats pulled live from the sheet (post-loss). Query the OI sheet before writing. Format: "Since inception: X winners, average gain of X%." This is now standard for all OI loss alerts — it grounds the subscriber in the long-term record during a losing trade.

**⚠️ SCHW lesson (Feb 24):** Never fabricate pattern stats. If W-L record was not explicitly provided, omit that line entirely. Omit > invent.

---

## Pre-Write Checklist

These aren't optional prep work. Each item addresses a specific failure mode:

- [ ] Read `references/options-insider-voice.md` — because your voice drifts every session and you blend service voices without noticing
- [ ] Read `references/knowledge.md` — because your default alert structure differs from published examples in ways you don't catch
- [ ] Pull 3 most recent published alerts of same TYPE from WordPress — because Josh's preferences evolve and knowledge.md may be weeks behind what's live
- [ ] Compare structure line by line — because "I'm confident it matches" has been wrong before (BP sell alert is the latest example)
- [ ] Verify pattern stats — the SCHW incident happened because you fabricated a W-L record. If you don't have the number, omit it. Omit > invent.
- [ ] Verify current option price — because prices move fast and a stale price in a trade alert means subscribers can't execute
- [ ] Verify entry date — because you've gotten dates wrong across sessions, especially when compaction has hit

---

## Publishing Pipeline

### Create WordPress Draft
```bash
POST_ID=$(sudo wp --path=/var/www/html --allow-root post create /tmp/alert-content.html \
  --post_type=premium-post --post_status=draft \
  --post_title="TRADE ALERT: [TITLE]" --porcelain)
```
**⚠️ Always `draft`. Never `--post_status=publish` on create.**

### Set Taxonomies
```bash
sudo wp --path=/var/www/html --allow-root post term set $POST_ID content-type trade-ideas-updates --by=slug
sudo wp --path=/var/www/html --allow-root post term set $POST_ID product-categories options-insider --by=slug
```

### Henry QC — Structural Comparison

This step exists because you consistently believe your draft matches published structure when it doesn't. The only way to catch structural drift is to have the real thing open next to your draft.

```bash
sudo wp --path=/var/www/html --allow-root post get $POST_ID --field=post_content
```
Compare your draft against recently published OI alerts of the same type:
- [ ] Opens with tension/conflict, not a company description? (You default to explaining the company first — subscribers don't need that, they need the trade setup)
- [ ] Contract details match Step 0 verification (expiration, strike, price)? (Cross-check catches copy/paste errors from prior alerts)
- [ ] Pattern name and record correct? (Fabricated stats destroyed trust once — verify or omit)
- [ ] WordPress block format throughout? (You drop format mid-alert when you're focused on copy)
- [ ] For LOSS exits: no forbidden elements? (You add "I got this one wrong" openers, thesis recaps, and "What This Trade Looks Like" sections to loss alerts — all explicitly forbidden. Check every time.)

### Send Draft Link to Josh
Channel: `#trade-alerts` (ID: `1473066624993988739`)
```
📋 **[TICKER] OPTIONS INSIDER — DRAFT READY FOR REVIEW**

**Post:** [Alert title]
**Preview:** https://joshbelanger.com/?post_type=premium-post&p=[POST_ID]&preview=true

**Trade:** [Full action line]
**TP/SL or Entry/Exit/P&L**
**Pattern:** [Name] — X-Y record

✅ to publish | ❌ to revise
```

### Wait for Approval
- Telegram: "publish", "go", "approved", "send it", ✅, or similar
- Josh approves via Telegram.
- **⚠️ When Josh approves, ACT IMMEDIATELY. Do not lose the approval in conversation.**

### Publish Existing Draft + Sheet + Log

**⚠️ CRITICAL: DO NOT create a new post. DO NOT rewrite the alert. The draft ALREADY EXISTS. Your ONLY job is to publish it.**

When spawning the publish agent, pass the EXACT post ID. The agent task should be:

```
Publish existing WordPress draft Post [POST_ID] for Options Insider. DO NOT create a new post.

1. VERIFY the post exists and is a draft:
   sudo wp --path=/var/www/html --allow-root post get [POST_ID] --fields=ID,post_status,post_title
   If post_status is NOT "draft", STOP and report the error.

2. Publish it:
   sudo wp --path=/var/www/html --allow-root post update [POST_ID] --post_status=publish

3. Get URL:
   sudo wp --path=/var/www/html --allow-root post get [POST_ID] --field=url

4. Update sheet:
   - READ /home/clawdbot/dash/skills/trade-sheet-updater/references/options-insider.md FIRST
   - Build the payload exactly from that schema — do not guess field names or values
   - Use the curl redirect pattern from /home/clawdbot/dash/skills/trade-sheet-updater/SKILL.md

5. **Verify the sheet — required before reporting done:**
   Read back the sheet rows around the new entry:
   ```bash
   GOG_KEYRING_PASSWORD="henrybot2026" gog sheets get 1YyATKBbAanLe4xvL1C2CdLuGJFteyGnbCrYv1HjuSO8 'A83:P90' -p
   ```
   Confirm:
   - Exactly ONE new row for this ticker + expCycle
   - Type field = "C", "P", or "C/P" (not "CALL", "PUT", etc.)
   - Strike in correct column (single leg = leg2/col I; spread = both cols)
   - Entry price, TP, SL all populated correctly
   If anything is wrong, fix it before reporting success. Josh should never have to check the sheet.

6. Log: ./scripts/log-activity.sh "Published [TICKER] OI [buy/sell] alert (Post [POST_ID])" "collaborative"
```

**The agent must NOT:**
- Create any new posts (no `wp post create`)
- Rewrite or modify the alert content
- Generate new alert copy

Publishing triggers mu-plugin → n8n → email + SMS automatically.

---

## Gotchas (from Real Sessions)

**Mar 30, 2026 — Drafted from memory, skipped mandatory reads**
AMD OI buy alert. Skipped reading published OI alerts, drafted from memory, used HMT voice ("Here's what caught my attention") in an OI alert. Took 4 revision rounds. The read step is a GATE, not optional prep. This is why the hard rule exists at the top of this file.

**Mar 30, 2026 — Bear Plunge pattern described backwards**
Wrote the Bear Plunge as if we were buying a dip (bullish). Bear Plunge = BEARISH = stock dropping = we buy PUTS. Pattern direction table is now a hard rule at the top.

**Mar 30, 2026 — Stale numbers from prior sessions**
Used "463% total returns" for ABNB without re-checking the sheet (number may have changed after losses). Used "one rough week" when entry was two weeks ago. Every number and time reference must be verified against live data in THIS session.

**Mar 30, 2026 — Research section contradicted opener**
Price and timing in the body didn't match what was stated in the opening. Cross-check all numbers between sections before presenting.

**Mar 25, 2026 — Dense body paragraphs, every session**
This is a recurring failure. I write dense multi-sentence paragraphs in the body even after being corrected. The rule is structural: one thought = one paragraph. No exceptions. Read the draft out loud before submitting. If you run out of breath, break it up.

**Mar 25, 2026 — Opening not broken into short punchy lines**
The opening needs breathing room. Each beat (what happened, pattern stats, "it just triggered again") is its own paragraph. Cramming them together makes it choppy and hard to read. This has been corrected multiple sessions in a row — it must become the default, not the correction.

**Mar 25, 2026 — Presenting draft before QC**
Draft written, preview link sent, Josh asked "did you review this?" — that's the failure. QC runs BEFORE the preview link. Every time. No exceptions. If the preview link is sent and QC hasn't run, the process failed.

**Mar 25, 2026 — U-Turn Velocity TP/SL wrong**
Used "exit at expiration" (regular U-Turn rule) for a U-Turn Velocity alert. U-Turn Velocity = 50% TP / 50% SL. Always look up the pattern in the Pattern Reference table. Never write TP/SL from memory.

**Mar 25, 2026 — "Tough Long" framing — never talk subscribers out of a trade**
Wrote a section header "This Is a Tough Long. Here's Why Buyers Are Showing Up Anyway." Josh: "It's not our job to convince them not to take the trade." The alert sells the thesis. It does not present the counterargument. Cut any language that creates doubt about the trade.

**Mar 25, 2026 — Paraphrasing Josh's thesis into generic language**
Josh provided the hotel-swap thesis explicitly: people don't stop traveling, they trade down from hotels to Airbnb. I wrote "low debt, high sensitivity to economic growth" instead. When Josh gives you the thesis, use it. Don't translate it into softer language.

**Mar 25, 2026 — "Made the Bear Plunge work" when it got stopped out**
The prior ABNB Bear Plunge alert was stopped out. I wrote "the same macro that made the Bear Plunge work." Never describe a stopped-out trade as "working." Accurate: "the Bear Plunge fired" or "the Bear Plunge got stopped out."

## Correction Workflow

When a published alert has an error (wrong expiration, strike, price):

1. **Fix the live post** — update WordPress content immediately
2. **Send correction** — use the shared script:
```bash
python3 /home/clawdbot/clawd/scripts/send-correction.py \
  --post-id POST_ID \
  --service "Options Insider" \
  --subject "CORRECTION: TICKER — What Changed" \
  --correction-html "<p>Quick correction...</p><p>Corrected trade: ...</p>" \
  --sms-text "Hi __NAME__, OPTIONS INSIDER CORRECTION: brief correction. Reply STOP to unsubscribe" \
  --link "https://joshbelanger.com/p/slug/"
```
3. **Log it** — `./scripts/log-activity.sh "Sent correction for [TICKER] Post [ID]" "support"`

**Prevention > Correction.** Step 0's cross-check exists to catch these before publishing.

---

## Pattern Reference

| Pattern | Take Profit | Exit Rule |
|---------|-------------|-----------|
| Bull Surge | 40% gain | 60% loss |
| Bear Plunge | 40% gain | 60% loss |
| U-Turn / U-Turn Velocity / U-Turn Standard | 50% gain | Exit day of expiration if TP not hit |
| Two-Way Trigger | 20% gain (combined) | Close after 10 trading days if TP not hit |
| Velocity | 50% gain | 50% loss |

---

## Quick Reference

| Item | Value |
|------|-------|
| WordPress taxonomy | `options-insider` |
| Content type slug | `trade-ideas-updates` |

| Chart directory | `/var/www/html/charts/` → `https://joshbelanger.com/charts/` |
| Image block format | Always use `/charts/` URL directly. Never upload to WP media library. Always set `style="width:800px"` on the img tag. See block format below. |

**Standard image block (all services):**
```html
<!-- wp:image {"sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://joshbelanger.com/charts/FILENAME.png" alt="Description" style="width:800px"/></figure>
<!-- /wp:image -->
```
| n8n webhook | `http://localhost:5678/webhook/alert-notify` (corrections only) |
| Sheet ID | `1YyATKBbAanLe4xvL1C2CdLuGJFteyGnbCrYv1HjuSO8` |

**Mar 30, 2026 — Bear Plunge thesis inverted**
Described the Bear Plunge as catching stocks "hit harder than the move warrants" — bullish dip-buying language in a PUT alert. Had the entire thesis backwards. Bear Plunge = stock dropping = we buy puts. Every sentence about the pattern must describe DOWNWARD movement. Before writing any pattern description, answer: "What position? What direction?" If they don't match, stop.

**Mar 30, 2026 — HMT voice in OI alert**
Used "Here's what caught my attention" in an OI alert. That's HMT flow language. OI uses "What This Trade Looks Like" before the options screenshot. Service voices are NOT interchangeable. Read the voice reference for the correct service BEFORE writing.

**Mar 30, 2026 — Partial QC presented as done**
Said "I checked em dashes and math" and called it QC. That's 2 out of 15+ items on the checklist. Full QC means every item in alert-qc.md. Partial QC = no QC.

**Mar 25, 2026 — WMT opener was a status update, not a hook**
Opened with where the stock is now instead of tension/conflict. The opening must create a reason to keep reading. "WMT is at $X" is not a hook. "Two weeks ago the Bear Plunge fired and shares haven't stopped falling" is.

**Ongoing — Generic filler phrases**
These appear in drafts when I'm not being specific enough:
- ❌ "Fear > reality" (means nothing without the specific numbers)
- ❌ "Thesis played out bigger than expected" (WHAT played out? By HOW MUCH?)
- ❌ "The setup was textbook" (lazy — describe what actually happened)
- ❌ "Conditions aligned perfectly" (which conditions? be specific)
Every general statement must be replaceable with a specific fact. If it can't be, cut it.

## Service Voice Fingerprint

**OI phrases — YOURS (use these, they define the service):**
- "What This Trade Looks Like" (section heading before chart — NOTE: 48HC also uses this heading for the closing chart. It's shared, not exclusive to OI)
- Pattern names: Bull Surge, Bear Plunge, U-Turn, Two-Way Trigger
- "X-Y record with X% total returns"
- "It just triggered again."
- "Get in, get the X%, get out."
- Pattern-driven thesis language: "The pattern fires when..."

**BANNED — these belong to OTHER services:**
- ❌ "Here's what caught my attention" (that's HMT)
- ❌ "$X million just dropped on calls" / flow-following language (that's HMT)
- ❌ "That's a signal worth following" (that's HMT)
- ❌ "The 48-Hour Window Just Opened" (that's 48HC)
- ❌ Insurance analogies (that's 48HC)
- ❌ "25% return for 48 hours of patience" (that's 48HC)
- ❌ "When hot money floods in" (that's HMT)

**If you catch any banned phrase in your draft, you've got service voice bleed. Stop and re-read `references/options-insider-voice.md`.**

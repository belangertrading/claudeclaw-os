---
name: x-playbook
description: X/Twitter content playbook for Josh Belanger — the full platform execution system. Replies, quote tweets, original posts, scanner, QC. Two modes. REPLY MODE — Josh drops a link and says "write me a reply" or "what should I say to this" or agent surfaces a trending post with angles. SCANNER MODE — cron surfaces 3-5 trending posts with reply angles. Use when writing any X content, drafting replies, finding reply opportunities, or when someone asks about X strategy. Also triggers on "trending posts", "what's moving on X", "write a tweet", "reply to this", "quote tweet this", "x playbook". NOT for posting — Josh posts manually. Agent produces ready-to-copy plain text only.
---

# X Playbook

Write X/Twitter content for @BelangerTrading. Replies, quote tweets, original posts. Josh posts manually — agent produces ready-to-copy plain text.

Read `references/strategy.md` on first use for full context. Read `references/citadel-case-study.md` for the only fully approved example so far.

## ⚠️ HARD RULES

1. **NEVER fabricate credentials or experience Josh doesn't have.** He traded equities and options, not energy derivatives, not crypto, not forex. If you don't know whether Josh has the experience, don't claim it. The story must be REAL.
2. **NEVER sell, pitch, or CTA on social.** Social = authority. Paid = conversion. Separate. No "check out my service," no "link in bio," no bridging.
3. **NEVER announce credentials.** Not "22 years on Wall Street taught me..." — let the story prove the experience. If it could come from any account, kill it.
4. **Content is about MARKETS, not options.** Options is the instrument Josh uses. The topic is what's moving, why, and what people are missing.
5. **Output is plain text.** No markdown, no formatting. Paste-and-post to X. No hashtags unless Josh specifically asks.
6. **Josh posts manually.** Never attempt to post via API or automation.
7. **Hook / Body / Punch on everything.** No exceptions. If the punch is "we'll see how it plays out" — kill it and rewrite.

## THE SUPREME RULE

**It is better to be a complete and utter asshole than boring.** (Finn's Rule #1)

Every draft gets tested against this. Safe, generic, inoffensive = dead content. Polarizing, specific, conviction-driven = engagement. If you're not making SOMEONE uncomfortable, you're not doing it right.

## The 6 Mindset Ingredients (Quality Filter)

Every piece of content must have at least 3 of these. If it has fewer than 3, kill it and rewrite:

1. **Authenticity** — Real stories, real numbers, real opinions. Not performative vulnerability.
2. **Conviction** — Pick a side. "I think maybe" = death. "This will" = life.
   - **Finn's example:** "I think X is pretty cool" = LOW conviction. Passive, forgettable, no one engages. "X will change how every retail trader manages risk in 2026" = HIGH conviction. Specific, debatable, makes people reply. If your take could be a shoulder shrug, it's not a take.
3. **Humor / Personality** — Not jokes. The natural wit of someone who's seen it all.
4. **Value** — The reader leaves knowing something they didn't before.
5. **Polarity** — You WILL piss people off. That's the game. If everyone agrees, it's boring.
6. **DON'T BE BORING** — This overrides everything. A wrong take with personality beats a right take that reads like a textbook.

## Voice

The "rich uncle who's been through it" (Charlie Light). Not teaching. Not lecturing. Not flexing. The guy at the party who's already done it and says it out loud.

**Default posture: ATTACK.** We go on the attack — not waiting for someone to prompt us. See something wrong? Swing at it. See a consensus forming? Go contrarian. The default is aggressive, not reactive.

**What makes it Josh:**
- Conviction. Pick a side. No hedging.
- Specificity from experience — details nobody else knows
- Stories surface from context, not from a script
- If a 25-year-old influencer could say it, it's wrong
- **Be early, double down.** If you spot a take before the crowd, post it. If it turns out right, post again. Own the call.
- **Conviction without ego.** Josh has a take and defends it with facts, but never pretends to know it all. It's a debate, not a lecture. When someone pushes back, Josh treats it like two people who care about the same thing seeing it differently. Never defensive. Never dismissive. Never "I'm right and you're an idiot." Josh is not pretending to be the authority on everything — he's sharing what 22 years taught him and letting people decide.
- **Never punch down.** Small accounts challenging Josh get respect, not ridicule. The rich uncle doesn't embarrass the nephew — he drops the facts and lets the audience decide.
- **Spot flash bangs.** When someone keeps changing the argument (misleading → straw man → DCA → Buffett quotes), they're throwing flash bangs to pull you off your original point. Don't chase. Stay on the original take or walk away. The second you follow them into their new topic, you lost the frame. Know when the debate is over — Josh doesn't need the last word.

Read `references/voice-dna.md` for the full brand voice.

## Formatting Rules

- **No text blocks.** Walls of text with no line breaks = nobody reads it.
- **Vary line lengths.** Short line. Then a medium one that builds. Then short again. Same-length lines feel monotonous.
- **One full thought per line break.** Not one word per line (that's TikTok caption energy). Not five sentences per block (that's an essay).
- **Show More button (long-form only):** 90% of long-form performance depends on where the Show More button falls. Place it at a cliffhanger — right after "Here's what happened next." or "Best thing that ever happened to me." See x-content-creation skill for full Show More guide.

## Banned Phrases

These kill engagement. Cut them on sight:

**Hedge language (no conviction):**
- "We'll see how it plays out"
- "Time will tell"
- "It remains to be seen"
- "Only time will tell"
- "It's hard to say"
- "There are arguments on both sides"

**ChatGPT energy (Finn's term — generic AI slop):**
- "Here's the thing..."
- "Let me break this down"
- "What most people don't realize is..."
- "In my experience as a trader..."
- "As someone who's been in markets for X years..."
- Any sentence starting with "Look,"
- Any sentence starting with "Listen,"

**Credential announcing:**
- "22 years on Wall Street..." — WRONG. It's 22 years in the MARKETS, not on Wall Street. Wall Street was the start, not the whole career.
- "As an ex-Wall Street trader..." — only if varied. Never the same phrasing twice in a week.
- "In my decades of experience..."
- Leading with the resume instead of the story
- Using the same credential phrasing repeatedly — rotate: "ex-Wall Street guy," "ex-Wall Street trader," "someone who worked on Wall Street with 22 years in the markets," "started in the pits at 19." If it sounds robotic, it IS robotic.

**Structural bans:**
- Bullet points in tweets
- Numbered lists in tweets
- Thread format unless explicitly requested
- "1/" or "🧵" unless Josh asks for a thread
- Hashtags (unless Josh explicitly asks)
- Emojis as section breaks

**Testing rules:**
1. Read the draft out loud. Does it sound like a person talking or a press release?
2. Could a 25-year-old finance bro post this? If yes, kill it.
3. Is there a real story or specific detail? If no, it's generic.
4. Does the punch leave an emotion or just trail off? Trailing off = rewrite.

## Reply Mode

When Josh drops a link or says "write me a reply":

### Step 1: Read the Post (FULL CONTEXT)
Read the ACTUAL post, not just the search snippet. Use XMCP `getPostsById` or Puppeteer for X Articles. Understand:
- WHO is saying this? (Current official? Ex-official? Pundit? Data account?)
- WHY are they saying it? (Defending their record? Breaking news? Pushing an agenda?)
- WHAT is the current reality? (Is this claim accurate right now? What's changed since?)
- WHAT is the real conversation underneath? (Citadel example: surface = electricity pricing, real = institutional bullying.)

If you can't answer all four, you don't understand the post well enough to draft a reply.

### Step 2: Find Josh's Angle
What does Josh know about this from personal experience? Check:
- Story bank: `/home/clawdbot/sloane/x-story-bank.md`
- Does this trigger a memory Josh has shared before?
- What's the insider take that nobody else in the replies will have?

If no personal story exists: use Josh's market expertise to add a take nobody else is saying. Still needs conviction and specificity.

### Step 3: Draft (Hook / Body / Punch)
- **Hook** (first line): Stops the scroll. Personal, unexpected, or provocative. 0.1 seconds to win.
- **Body** (middle): Back up the hook. Story, specificity, insider knowledge.
- **Punch** (last line): Leaves an emotion. Determines whether they engage. If it's weak, the whole reply dies.

### Step 4: Self-Check
Run these checks IN ORDER. If any fail, rewrite before presenting:
1. **Context check** — Does the reply show you actually understand what the post is about? Who said it, why, and what's happening right now? If the reply could be written by someone who only read the headline, it fails.
2. **Fabrication check** — Does the reply claim any experience Josh doesn't have?
3. **Banned phrases check** — Any banned words or patterns?
4. **Testing rules** — Read it out loud. Could a 25-year-old post this? Real story or specific detail? Punch leaves an emotion?

### Step 5: Present to Josh
Post in X Content thread (topic 3050) or wherever Josh asked. Plain text, ready to copy. If you have multiple angles, present 2 max — not 5 options.

### Rejection Diagnostic
If Josh rejects a draft, diagnose WHY before rewriting:
- **"Too generic"** → Missing personal story or specific detail. Find one.
- **"Sounds like AI"** → Check banned phrases. Read it out loud.
- **"Wrong angle"** → You misread what the post is really about. Re-read Step 1.
- **"Too long"** → Replies should be 2-4 sentences max unless it's a quote tweet.
- **"I wouldn't say this"** → You fabricated experience or voice. Strip it back to what Josh actually knows.

- **"You're making stuff up"** → Fabrication. Different from wrong voice. You invented a detail, stat, or experience. Strip it entirely — don't rephrase, remove.
- **"We don't talk about ourselves"** → Self-promotional or brand-focused. Content is about markets, not about BT.

Every rejection = a gotcha. Add it immediately.

## Scanner Mode (Cron)

Surfaces 3-5 posts worth replying to. Runs twice daily: 7 AM ET (pre-market) and 12 PM ET (midday).

### What to Scan
1. New posts from hunting list accounts (see `references/hunting-list.md`)
2. Trending finance/markets posts with high velocity (500+ likes OR 100+ replies in <2 hours)
3. Breaking market news crossing into X
4. Viral finance posts crossing over from general X

### Filter Criteria
- **Relevance:** Markets, trading, institutional moves, finance industry drama
- **Reply opportunity:** Active reply section, not already 500+ replies deep
- **Audience overlap:** The people engaging are Matt or Matt-adjacent (25-34, trades, has money in the game)
- **Josh can add value:** There's an angle from experience, not just commentary

### Output Format (to Telegram topic 3050)
```
🎯 [number]. [one-line summary]
[link]
📊 [likes]/[replies]/[reposts] in [time]
💡 Angle: [one sentence — why Josh should swing at this]
```

Surface top 3-5 reply/QT opportunities. For each, note whether it works better as a reply or a quote tweet.

Additionally, draft 1-2 original tweet ideas based on what's trending in the market today. These don't need another post as context — they come from Josh's perspective on the day's action. Use the same Hook/Story/Punch structure from the x-content-creation skill. Pull open positions from the trade sheets if relevant.

If nothing qualifies for replies, say "Nothing worth swinging at this morning/afternoon." Original content ideas should still be attempted regardless.

## Quote Tweets

Same as replies but longer format allowed (up to ~280 chars). Quote tweets work when:
- Josh has a strong counter-take to the original post
- The original post needs context the audience doesn't have
- Josh's experience directly contradicts the consensus

Quote tweets do NOT work when:
- It's just agreeing with the post (that's a reply or a repost)
- The take is lukewarm ("This is interesting because...")

## Original Posts

Less frequent than replies. Used for:
- Josh has a market take that doesn't need someone else's post as context
- A trade played out and there's a lesson
- Something happened that only Josh would notice from his position

Same Hook/Body/Punch structure. Same banned phrases. Same self-check.

## Story Bank

`/home/clawdbot/sloane/x-story-bank.md`

When Josh shares a personal story during ANY interaction — log it immediately. Stories surface from context (a post jogs a memory), not from interviews. If you hear a new one, append it to the file before doing anything else.

Format:
```
## [Short title]
**Source:** [where it came from — which conversation, which post triggered it]
**Story:** [the details as Josh told them]
**Use when:** [what kind of posts this reply to]
```

## Audience

**Matt. 31. Austin.** Full persona in `references/strategy.md` Part 2. The content is for Matt — but good content bleeds up to older demographics. Build for 25-34, the 45-year-olds find it through the same content.

## Start at Zero

Every scanner run, every draft, every day — start at zero. No coasting on yesterday's output.

- **No recycled drafts.** If it didn't get posted, it's dead. Markets moved, context shifted, the post is buried.
- **No template reliance.** Hook/Body/Punch is the structure, not the formula. Some days it's a one-liner. Some days it's a story. Some days it's a question. If every draft sounds the same, the structure became a crutch.
- **Fresh market pulse every time.** Check current prices before referencing any ticker. Don't write "XHB is overpriced" without knowing where XHB opened today.
- **No rollover inventory.** Tomorrow we find new posts, write new takes, run new QC. Yesterday's work doesn't carry over.

## Gotchas

1. **Mar 21: Read the actual post, not just the search snippet.** Biden "strongest economy" draft missed that Biden is the EX-president defending his record, not making a current policy claim. The search snippet had enough context — I skimmed instead of reading. Always understand WHO is saying it, WHY they're saying it, and WHAT the current situation actually is before drafting.
2. **Mar 19: Citadel reply took 7 attempts.** Failed modes: dismissive, commentator, generic, fabricated credentials, announcing credentials, missing the real story. See `references/citadel-case-study.md` for the full breakdown. Every new approved example gets its own case study file.
2. **Mar 19: "Options" is too niche.** Josh corrected "options trading content" to "markets content." Options is the tool. Markets is the topic. Always frame around markets.
3. **Mar 19: Stories come from context, not prompts.** Don't ask Josh to "tell me a story about X." Wait for a post to jog a memory. When it happens, capture it immediately.
4. **Mar 19: Don't be a commentator.** "The video is solid but the framing is engagement bait" is media criticism, not value. Josh is a trader, not a content reviewer.
5. **Mar 21: QC stamps were rubber stamps.** Scanner output got ✅ without running through Finn properly. Fix: every draft runs a 5-gate checklist BEFORE getting a pass — (1) 25-year-old test, (2) teaching tone check, (3) punch test (last line alone — emotion or trail-off?), (4) conviction check (any hedge language?), (5) day trader lens (does it reflect current market reality, not theory?). (6) clarity — would Matt in Austin understand this without Googling anything? No jargon, no talking over people's heads. (7) Josh's actual take — does this reflect what Josh actually believes, not what gets easy engagement? If it can't pass all 7, rewrite before presenting. If it still can't pass, cut it from the batch entirely. No more QC theater.
6. **Mar 22: Don't skip posts because the topic looks "political" or "geopolitical."** If Josh can find a market angle, it belongs in the batch. ICE at airports isn't an immigration post — it's a travel/leisure short catalyst when combined with jet fuel costs and weak demand. The filter isn't "is this about markets?" — it's "can Josh connect this to a trade?" If yes, draft it. If no, skip it.
7. **Mar 21: Josh's actual positions matter more than easy engagement.** Two locked opinions: (a) AGAINST "index and chill" — BT sells active management, passive investing posts are swing opportunities. (b) Congress trading ISN'T illegal and some of them have great picks — Josh's angle is "look at the results, not the narrative." Contrarian to populist rage. NOT "burn it down." Don't draft the easy outrage take — draft Josh's actual take or skip the post. Easy populist outrage, but not his position. Don't draft replies on Pelositracker-type posts that frame congressional trading as illegal. If there's no angle Josh actually holds on a post, skip the post entirely.

# Alert QC Checklist

**Load this file and run every check before presenting any draft to Josh.**

This checklist exists because you skip steps when you're confident in your output. That confidence has been wrong repeatedly — wrong dates, wrong prices, fabricated stats, structural drift from published examples, charts that don't exist. Josh should never be the one catching these errors. That's what this file is for.

## Pre-Present QC

Run through every item. If anything fails or is uncertain, flag it explicitly before proceeding.

### Trade Fully Specified
- [ ] Every mention of the trade includes the FULL contract: ticker, expiration, strike, direction. No "we followed it" or "we got in" without the contract details.
- [ ] If the alert references a prior trade, that trade is also fully specified.

### Temporal Claims Verified
- [ ] Every time reference ("overnight," "about an hour," "last week," "two days ago") has been verified with a tool or search. If you didn't check the timestamp, cut the time reference.
- [ ] No fabricated sequence claims ("futures reversed" without checking if they actually did).

### Dates & Expiration
- [ ] Year is correct — today is 2026. Flag anything showing 2025 or 2027.
- [ ] Expiration date makes sense relative to today. If Josh said "Mar 13" but it's already past Mar 13, ask.
- [ ] Entry date matches today's date.

### Numbers & Stats
- [ ] Stock price verified via `get_price.py` — not assumed, not from memory.
- [ ] Entry price is from Josh or verified via option chain. Flagged as "(provided by Josh)" or "(live mid)".
- [ ] TP/SL math correct: TP = entry x 1.40, SL = entry x 0.40 (HMT). 25% return check for 48HC.
- [ ] Spread width and return calculation verified.
- [ ] Any market stat from a search result (oil price, earnings move, sector %) flagged to Josh before it goes in print. Do not publish unverified search numbers.

### Pattern Thesis (OI ONLY — CRITICAL)
- [ ] **Position direction matches pattern direction.** If buying PUTS, every sentence about the pattern must describe DOWNWARD movement. If buying CALLS, every sentence must describe UPWARD movement. Read the pattern table in `knowledge/options-insider/alert-structure.md`.
- [ ] **No bullish language in bearish trades.** Grep for: "rip higher", "looking for upside", "momentum taking off", "about to move higher", "undervalued", "beaten down unfairly", "hit harder than the move warrants". If found in a PUT alert, the thesis is BACKWARDS. Fix immediately.
- [ ] **No bearish language in bullish trades.** Grep for: "setting up for a drop", "pointing lower", "reversal accelerating downward". If found in a CALL alert, fix.

### Service Voice (ALL SERVICES — CRITICAL)
- [ ] **No cross-service language.** Each service has its own vocabulary:
  - OI: "What This Trade Looks Like" (NOT "Here's what caught my attention" — that's HMT)
  - HMT: "Here's what caught my attention" (NOT "What This Trade Looks Like" — that's OI)
  - 48HC: "The 48-Hour Window Just Opened" (unique to 48HC)
- [ ] **Pulled 2+ recent published alerts of the SAME service and TYPE before writing.** Not from memory — from WordPress. If you didn't pull them, this QC fails. Go back and pull them now.

### Structural Match
- [ ] **Compare structure against the most recent published alert of same type.** Section order, heading placement, chart position. Line by line. If the structure doesn't match, fix before presenting.
- [ ] **Opening is broken into short punchy lines.** Each beat = its own paragraph. No dense openers.
- [ ] **Body paragraphs: one thought each.** If a paragraph has two ideas, split it.

### Copy
- [ ] Zero em dashes (— or --) anywhere in the alert body or title. Read every sentence.
- [ ] Short paragraphs. No dense blocks. Lines breathe.
- [ ] No fabricated facts. Every claim is from Josh or a verified tool call.
- [ ] No forbidden words (see voice reference for each service).
- [ ] No contradictions (e.g., saying "the pattern fired" in past tense after saying it triggered today).

### Images
- [ ] Image files uploaded to `/var/www/html/charts/` BEFORE the URL appears in any post content.
- [ ] Unique filename used — never overwrite an existing file (Cloudflare caches aggressively).
- [ ] Ownership set: `sudo chown www-data:www-data /var/www/html/charts/FILENAME`
- [ ] Image URLs confirmed accessible in browser before draft is presented.

### WordPress
- [ ] Post created as `draft` — never published on create.
- [ ] Taxonomies set before presenting to Josh.
- [ ] Post ID checkpointed to `state/current-alert.json`.

### Service Voice Fingerprint
- [ ] **No cross-service phrases.** Check against the Service Voice Fingerprint section in the skill for this service.
- [ ] OI draft contains NO HMT phrases ("Here's what caught my attention", flow $ language)
- [ ] HMT draft contains NO OI phrases ("What This Trade Looks Like" as intro, pattern names)
- [ ] 48HC draft contains NO HMT phrases (excitement tone, flow language, aggressive conviction)
- [ ] 48HC draft contains NO section-header robot voice ("What's driving the panic:", "The Risk:")

### Post-Publish Rules
- [ ] Never pull a published post back to draft — retriggers n8n and blasts subscribers again.
- [ ] Any edit made after publish gets a dated correction note at the bottom of the alert.

---

## Post-Edit QC (Run After ANY Revision)

This section is triggered when Josh sends feedback and you edit the draft. The initial QC caught the first-draft issues. This catches the errors introduced BY the edit.

- [ ] Re-read the FULL draft top to bottom — not just the section you changed
- [ ] Title still matches body numbers (the USO failure: title said 90% after body was updated to 76%)
- [ ] All stats, dates, and percentages are internally consistent across the entire draft
- [ ] If you changed a number, grep the draft for the OLD number — it may appear elsewhere
- [ ] No orphaned references (removed a section but another paragraph still refers to it)
- [ ] The edit didn't introduce new forbidden elements or service voice bleed
- [ ] Read the draft out loud. Does it still flow, or did the edit create a jarring transition?

## How to Flag Issues

Don't bury flags in the message. Call them out at the top:

```
⚠️ QC FLAGS:
- Expiration says "Mar 13, 2025" — did you mean 2026?
- Crude oil price ($X) pulled from search, not verified — please confirm before I finalize.
```

Then wait for Josh to confirm before proceeding.

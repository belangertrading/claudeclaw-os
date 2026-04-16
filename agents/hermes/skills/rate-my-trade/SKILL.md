---
name: rate-my-trade
description: Prepare and run Rate My Trade sessions for Titans Zoom calls. Builds the pre-call brief from member submissions, structures Josh's live evaluation framework (Pass/Fail/Pivot), and archives each session as a searchable case study in the Vault. Use when prepping a Titans call, processing trade submissions, building the call agenda, or archiving a completed session. Also triggers on "rate my trade", "titans call prep", "trade submissions", "vault", "pass fail pivot".
---

# Rate My Trade — Titans Zoom Format

Members submit trades. Josh evaluates live. Every session becomes a case study.

## Framework: Pass / Fail / Pivot

| Verdict | Meaning |
|---------|---------|
| **Pass** | Trade is sound. Risk defined, thesis clear, setup present. Go. |
| **Fail** | Trade has a fatal flaw — bad risk/reward, no edge, chasing. Don't take it. |
| **Pivot** | Right idea, wrong execution. Josh restructures — different strike, spread, timing, or approach. |

> **For recorded sessions:** Use "No Trade" instead of "Fail" — softer on replay, same message.

## Pre-Call Prep Workflow

1. **Collect submissions** — Members submit via the 13-field template (see below). Submissions come in via email or Discord.
2. **Build the brief** — For each submission, create a one-page summary:
   - Ticker + current price (use `python3 ~/clawd/scripts/get_price.py TICKER`)
   - Member's thesis (1-2 sentences, their words)
   - The trade details (strike, expiry, entry, size)
   - Red flags I spot (things Josh will likely catch)
   - Quick chart context (trend, key levels, earnings date if relevant)
3. **Cap at 3-4 trades per call** — Deep breakdowns > surface coverage. If more submitted, pick the most educational variety (mix of Pass/Fail/Pivot candidates).
4. **Order strategically** — Start with a strong Pass or interesting Pivot. Don't lead with a Fail.
5. **Send brief to Josh** — At least 1 hour before call. Gmail draft or Telegram, whatever's faster.

## Submission Template (13 Fields)

Members fill this out when submitting a trade for review:

1. **Ticker**
2. **Direction** (Bullish / Bearish / Neutral)
3. **Strategy** (Long Call, Put Spread, Iron Condor, etc.)
4. **Strike(s)**
5. **Expiration**
6. **Entry Price** (or target entry)
7. **Position Size** (% of portfolio or dollar amount)
8. **Take Profit Target**
9. **Stop Loss**
10. **Thesis** (Why this trade? What's the catalyst?)
11. **What kills this trade?** (The bear case they see)
12. **Bailout Plan** (If it goes against you, what do you do?)
13. **Timeframe** (How long are you giving this to work?)

## Post-Session Archive (The Vault)

Every completed session gets archived as a searchable case study.

1. **Pull the Zoom transcript** (same flow as trading-club-recap skill)
2. **For each trade reviewed, create a case entry:**
   ```
   ## [TICKER] — [Verdict: Pass/Fail/Pivot]
   **Date:** YYYY-MM-DD
   **Member Thesis:** [their reasoning]
   **Josh's Evaluation:** [key points from transcript]
   **Verdict Reasoning:** [why Pass/Fail/Pivot]
   **Teaching Moment:** [the generalizable lesson]
   **If Pivot — New Structure:** [Josh's alternative]
   ```
3. **Tag each entry** with: ticker, strategy type, verdict, lesson category
4. **Save to** `data/rate-my-trade/vault/YYYY-MM-DD.md`
5. **Update index** at `data/rate-my-trade/vault/index.md` with new entries

## Compliance

Every session recording and vault entry must include at top:
> ⚠️ **For educational purposes only. Not financial advice. Past performance does not guarantee future results.**

## Gotchas

1. **Piloted Mar 12, 2026.** First send used service="Titans" which didn't exist in the N8N sheet — likely went nowhere. Had to resend as "Alliance." Check N8N workflow service mapping before sending member communications.

2. **N8N has "Alliance" hardcoded** as an OR condition in the webhook workflow. Sending to "Alliance" hits ALL Alliance members, not just Titans. TODO: Fix this in the N8N workflow.

3. **`__NAME__` placeholder doesn't work in email body** — N8N only replaces names in SMS. Use "Hey Trader," for emails.

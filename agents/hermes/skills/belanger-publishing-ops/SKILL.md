---
name: belanger-publishing-ops
description: Operating model for Belanger Trading's publishing operation. Hermes is the operator — does the thinking, research, QC, and publishing mechanics. Subagents write drafts. Covers the content tier system, shared reference architecture, and how to approach any new content type. Load this when Josh asks about the business broadly, assigns a new content type, or when planning cross-service work.
tags: [belanger, publishing, operations, architecture]
---

# Belanger Trading Publishing Operations

## Role
Hermes is the operator, not the writer. I do the thinking (5-question framework, catalyst research, market backdrop), spawn subagents to write drafts with the right voice refs + research brief, QC the output, and handle publishing mechanics (WordPress, sheets, logging). This scales — one more content type is one more workflow skill, not a new operation.

## Content Tiers

### Tier 1 — Paid Alerts (time-sensitive, subscriber-facing)
| Service | Skill | Voice | Sheet |
|---------|-------|-------|-------|
| Hot Money Trader | `hmt-alert-workflow` | Flow-driven, aggressive conviction | 12VsTbwa... |
| Options Insider | `oi-alert-workflow` | Pattern-driven momentum | 1YyATKBb... |
| 48-Hour Cashflow | `48hc-alert-workflow` | Calm insurance, premium collection | 1x9xQJAw... |

### Tier 2 — Reports & Analysis (longer form, paid subscribers)
- Alliance reports (`alliance-report/` in Dash skills)
- Member memos (`member-memo/`)
- Weekly damage reports (`weekly-damage-report/`)
- Earnings analysis (`fin-earnings-analysis/`, `fin-earnings-preview/`)
- Same voice, different structure — more research depth, less urgency

### Tier 3 — Free Content / Top of Funnel
- **Trading Journal on Substack** — joshbelanger.substack.com (327K+ subs), RSS: /feed
  - Hermes skill: `journal-writing` at `/root/.hermes/skills/journal-writing/` (built Apr 2026, fresh — not Dash's old v1/v2)
  - Josh's rawest voice. Private journal that happens to be public. Jesse Livermore lineage.
  - Key balance: not bragging, not wallowing. Transparency like Buffett's annual letters.
  - Titles like "Right thesis. Wrong timing. -$8,300." — dollar amounts, self-deprecation, unresolved endings
  - Cadence: ~2-4x/month (gap since Mar 4 — needs to be more consistent)
  - Iterative process: raw material → find tension → draft → feedback → revise → publish
  - Loss entries always free (trust-building). Win entries can be gated.
- **JoshBelanger.com** blog / SEO content
  - SEO pillar #1: "Unusual Options Activity" at /options-trading/
- **X/Twitter** — x-content-creation/, x-cowriter/, x-playbook/ in Dash skills
- **TikTok, YouTube** — to be built

### Tier 4 — Operational Support
- Email replies (`email-reply/`)
- Trade cards (`trade-cards/`)
- Troll responses (`troll-response/`)
- Trade recaps (`trading-club-recap/`)

## Shared Reference Architecture
All content types share Josh's voice. The plan is a single reference library:

```
/root/.hermes/belanger/
├── voice/           brand-voice.md, alert-qc.md, phrase-bank.md, corrections.log
├── services/        hmt/, oi/, 48hc/ (service-specific voice + knowledge)
├── sheets/          update_sheet.py, webhook URLs, per-service schemas
└── substack/        Journal voice samples, RSS feed URL
```

Workflow skills are lightweight pointers to this library. New content type = new workflow skill + reference subdir if needed.

## The North Star (All Content Types)
Lead with what the member is feeling, connect the dots on WHY, and never pretend the market isn't happening around the trade. Conviction comes from context, not just pattern stats or system output.

## System Language Rule (All Content Types)
The system is real — it's the edge, it's credibility. Reference it. But never let it replace the human element.
- ❌ "The system said take it. We take it." — mechanical, system doing all the talking
- ✅ "The system flagged this at $88. Oil just hit $111. We're taking the money." — system gets credit, conviction from context

## How to Approach a New Content Type
1. Read Dash's existing skill for it (if any) — extract the operational details (webhooks, schemas, WP taxonomies)
2. Read 3-5 recent published examples of that content type
3. Read brand-voice.md for the universal rules
4. Build a workflow skill with the same structure: numbered pipeline steps, writing arc, voice rules, references table
5. The workflow should be executable end-to-end, not theoretical

## Key Operational Details
- WordPress: /var/www/html, --allow-root, post_type=premium-post for alerts
- WP taxonomies: product-categories (service slug), content-type (trade-ideas-updates)
- Charts: /var/www/html/charts/ → https://joshbelanger.com/charts/
- Price tool: python3 /home/clawdbot/clawd/scripts/get_price.py TICKER
- Chart tool: python3 /home/clawdbot/clawd/scripts/generate-chart-v4.py TICKER --days 90 --sma 50,200
- Activity log: ./scripts/log-activity.sh "description" "type"
- Publishing triggers: mu-plugin → n8n → email + SMS
- Never publish on create. Always draft first.
- Never pull published back to draft (retriggers n8n blast).
- Review channel: #trade-alerts (Discord ID: 1473066624993988739)

## Dash's Skills (Legacy Reference)
Located at /home/clawdbot/clawd/skills/. These contain reference files (voice.md, knowledge.md, phrase-bank.md, corrections.log) that my workflows currently depend on by path. Plan: migrate reference files into /root/.hermes/belanger/, then Dash's alert skills (6 total: v1+v2 × 3 services) can be deleted. Other Dash skills (alliance-report, x-content-creation, etc.) remain as reference until I build replacement workflows. Journal-writing has been replaced — new skill at `/root/.hermes/skills/journal-writing/` (Dash's journal-writing, journal-writing-v2, and journal-editing are now legacy reference only).

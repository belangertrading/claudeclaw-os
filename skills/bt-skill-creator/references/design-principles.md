# Skill Design Principles

**Source:** "Lessons from Building Claude Code" by Thariq Shihipar (Anthropic), March 2026
**Full article:** `/home/clawdbot/clawd/references/skill-best-practices-thariq.md`
**BT additions:** From 6 months of skill building, ~43 skills, and hundreds of corrections.

---

## 1. Gotchas Section = Highest-Signal Content

The most valuable part of any skill. Built from real failures — times the agent got it wrong and the human corrected it.

**How to build it:**
- Start with known failure modes from the interview
- Add every human correction immediately (same turn, not later)
- Be specific: not "write concisely" but "Josh's replies are 2-4 sentences. Never open with 'I appreciate you taking the time.'"
- Date every gotcha so you can see the evolution

**"Most of ours began as a few lines and a single gotcha, and got better because people kept adding to them as new edge cases appear."** — Thariq

**BT pattern:** Gotchas live in SKILL.md, not a separate file. They're the last section, numbered, dated. Every agent reads them every invocation. When a skill has 15+ gotchas, consider promoting patterns into the main workflow and archiving resolved ones.

## 2. Don't State the Obvious

Claude already knows a lot. Focus the skill on where Claude's defaults are wrong.

**The test:** Remove a line. Would Claude still do the same thing? If yes, cut it.

**Example:** Anthropic's frontend-design skill doesn't teach HTML — it breaks Claude's habit of reaching for Inter font and purple gradients. Our alert skills don't teach how to write — they enforce voice patterns, ban specific phrases, and gate factual claims.

## 3. Skills Store Data

Skills can maintain state across sessions:
- **data/config.json** — Setup info (if missing, skill asks the user)
- **data/corrections.log** — Running list of human corrections (append-only)
- **data/history.log** — What the skill has done (prevents repeating mistakes)

Pattern: the skill reads its own history before acting. It gets smarter over time.

**BT example:** The x-story-bank is skill state — captured stories that persist across sessions and grow from real conversations, not interviews.

## 4. Start Small, Grow From Failures

Don't write the perfect skill upfront. Ship the minimum:
- Core workflow (few lines)
- 1-2 gotchas from known failures
- Reference files it needs

Use it. When it fails, add the correction as a gotcha. The skill grows from real usage, not imagined scenarios.

**The trap:** Over-engineering a skill before it's been used once. The trading-club-recap skill had 9 gotchas after one night of real testing. None of those gotchas were predictable in advance — they all came from Josh's corrections on actual output.

## 5. Nine Skill Categories

Know what type before building — it changes what you emphasize:

| Category | Emphasize |
|----------|-----------|
| Library & API Reference | Examples, edge cases, correct usage |
| Product Verification | Test steps, pass/fail criteria |
| Data Fetching & Analysis | Connections, transforms, caching |
| Business Process Automation | Workflow steps, gotchas, error handling |
| Code Scaffolding | Templates, conventions, boilerplate |
| Code Quality & Review | Standards, anti-patterns, review checklists |
| CI/CD & Deployment | Pipelines, rollback procedures |
| Runbooks | Symptom → investigation → structured report |
| Infrastructure Operations | Guardrails, maintenance routines |

Most BT skills are **Business Process Automation** (alerts, recaps, memos) or **Data Fetching & Analysis** (trade-alert-api, equity-research).

## 6. On-Demand Hooks

Skills can include session hooks activated only when the skill is triggered:
- `/careful` — blocks destructive commands
- `/freeze` — blocks edits outside a directory

**BT application:** Alert skills have a hard gate (no copy in chat, three-source gate) that functions like an always-on hook. Any subscriber-facing skill should have equivalent protection.

## 7. Progressive Disclosure (BT Addition)

Three levels of loading:
1. **Metadata** (~100 words) — Always in context. Trigger description.
2. **SKILL.md** (<500 lines) — Loaded when triggered. Core workflow + gotchas.
3. **References** (unlimited) — Read on demand. Voice DNA, examples, API docs.

The skill TELLS the agent what reference files exist and WHEN to read them. Example: "Read `references/voice-dna.md` before drafting any email." The agent only loads it when it's actually writing.

## 8. Symlinked References (BT Addition)

Voice skills share reference files. Don't duplicate — symlink:
```bash
ln -sf /home/clawdbot/clawd/references/email-voice/voice-dna.md references/voice-dna.md
```

One source of truth. Update the original, all skills get the update. Currently used by: email-reply, trading-club-recap, journal-writing-v2, x-cowriter, head-of-x.

## 9. The Three-Source Gate (BT Addition)

Any skill producing content for paying subscribers must include:

> Every factual claim must come from: (a) Josh's exact words this session, (b) a tool result this session, or (c) a search you ran this session. Can't cite it? Cut it.

This exists because an agent wrote "Marvell reported last night" in alert copy — completely false, stated with full confidence. Process rules ("search before writing") fail because the agent doesn't recognize its own blind spots. The structural fix: require proof for every claim. No proof, no sentence.

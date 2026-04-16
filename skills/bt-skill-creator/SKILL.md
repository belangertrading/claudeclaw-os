---
name: bt-skill-creator
description: Create new skills, modify and improve existing skills, and measure skill performance for Belanger Trading. Use when users want to create a skill from scratch, update or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy. Also triggers on "build a skill", "turn this into a skill", "make a skill for", "improve this skill", "the skill needs fixing", or any request to codify a workflow into a reusable skill.
---

# BT Skill Creator

Build, test, and improve skills for the Belanger Trading agent team. Forked from Anthropic's skill-creator with Thariq's design philosophy baked in and BT-specific patterns added.

**Read `references/design-principles.md` before writing any skill.** It covers the philosophy that determines whether a skill is useful or ignored.

## Philosophy (Thariq — Non-Negotiable)

These aren't suggestions. They're how good skills work.

1. **Gotchas are the highest-signal content.** Built from real failures, not imagined ones. A skill with 3 gotchas and 10 lines of instructions beats a skill with 200 lines of instructions and no gotchas.

2. **Don't state the obvious.** Claude already knows how to write HTML, draft emails, call APIs. The skill exists to override Claude's DEFAULTS — where it goes wrong without guidance. The test: remove a line. Would Claude still do the same thing? If yes, cut it.

3. **Start small, grow from failures.** Ship the minimum: core workflow + 1-2 gotchas + reference files. Use it. When it fails, add the correction as a gotcha. The skill grows from real usage, not imagined scenarios.

4. **Avoid railroading.** Skills are reusable across many prompts. Over-specific instructions break in edge cases. Give Claude information and flexibility, not rigid step-by-step scripts it can't deviate from.

5. **The description is a trigger, not a summary.** Write it for the AI scanning `available_skills`. Be slightly pushy — Claude undertriggers skills. Include specific phrases, contexts, and adjacent use cases.

## Two Tracks

Not every skill needs the full eval suite. Pick the right track:

### Track 1: Ship & Iterate (Default)
For most skills. Especially new workflows, internal tools, process automation.

1. **Capture intent** — What should this skill do? When should it trigger? What's the output?
2. **Write the SKILL.md** — Core workflow, 1-2 known gotchas, reference file pointers
3. **Use it** — Run it on a real task
4. **Correct it** — Every human correction = a gotcha, added in the same turn
5. **Repeat** — The skill gets better from real usage

This is Thariq's model. Most Anthropic skills started as "a few lines and a single gotcha." Ours should too.

### Track 2: Full Eval Suite (High-Stakes)
For skills where bad output has real consequences: alert pipelines, subscriber-facing emails, voice writing, anything touching money or member communications.

1. **Capture intent** (same as Track 1)
2. **Write the SKILL.md** (same as Track 1)
3. **Write 2-3 test cases** → `evals/evals.json`
4. **Spawn with-skill and baseline sub-agents** in the same turn
5. **Draft assertions** while runs are in progress
6. **Grade, aggregate, launch eval viewer** for human review
7. **Read feedback, improve, repeat**

Full eval process details are in `references/eval-process.md`.

**When to use Track 2:**
- Alert skills (48hr, HMT, OI) — bad copy goes to paying subscribers
- Voice writing skills (journal, email-reply, recap) — voice drift is invisible to the agent
- Any skill where output goes to external humans
- When a skill has failed multiple times and you need to verify the fix works

## Anatomy of a BT Skill

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description)
│   ├── Hard rules (if subscriber-facing)
│   ├── Core workflow
│   ├── Gotchas (grows over time — this is the most important section)
│   └── Error handling
├── references/ (read on demand, not loaded by default)
│   ├── voice-dna.md (symlink for voice skills)
│   ├── knowledge.md (published examples)
│   └── domain-specific docs
├── scripts/ (helper scripts — deterministic/repetitive tasks)
├── evals/ (test cases — Track 2 only)
│   └── evals.json
└── data/ (skill state — optional)
    ├── corrections.log (append-only human corrections)
    └── history.log (what the skill has done)
```

### Progressive Disclosure (Three Levels)

1. **Metadata** (name + description) — Always in context (~100 words). This is the trigger.
2. **SKILL.md body** — Loaded when skill triggers (<500 lines ideal)
3. **References** — Read on demand (unlimited size, loaded only when needed)

Keep SKILL.md under 500 lines. If approaching the limit, split into references with clear pointers.

## Writing the SKILL.md

### Capture Intent

Before writing anything:
1. What should this skill enable Claude to do?
2. When should it trigger? (specific phrases, not generic)
3. What's the output format?
4. What category is it? (determines what to emphasize)

**Nine categories** — know the type before building:
1. **Library & API Reference** → examples + edge cases
2. **Product Verification** → test steps + pass/fail criteria
3. **Data Fetching & Analysis** → connections + transforms
4. **Business Process Automation** → workflow steps + gotchas
5. **Code Scaffolding** → templates + conventions
6. **Code Quality & Review** → standards + anti-patterns
7. **CI/CD & Deployment** → pipelines + rollback
8. **Runbooks** → symptom → investigation → report
9. **Infrastructure Operations** → guardrails + maintenance

### Writing Patterns

**Explain the why, not just the what.** Today's LLMs are smart. If you find yourself writing ALWAYS or NEVER in all caps, reframe: explain the reasoning so the model understands WHY the constraint exists. That's more powerful and more durable than rigid rules.

Exception: hard rules for subscriber-facing output (three-source gate, no copy in chat) stay rigid because the consequences of violation are real.

**Use the imperative form.** "Read the voice DNA file before drafting" not "You should consider reading the voice DNA file."

**Include examples.**
```
## Commit message format
Example 1:
Input: Added user authentication with JWT tokens
Output: feat(auth): implement JWT-based authentication
```

### The "Remove a Line" Test

After writing a draft, review every line:
- Would Claude do this anyway without the instruction? **Cut it.**
- Does this override a Claude default that's wrong for this context? **Keep it.**
- Is this a gotcha from a real failure? **Keep it — it's the most valuable content.**

## BT-Specific Patterns

### Gotchas on Correction (AGENTS.md Rule)

When Josh (or any human) corrects output produced by a skill, the correction becomes a gotcha **in that skill, in the same turn.** Not later. Not "I'll add it next session." Same turn.

Format: Include the date, what was wrong, and what's correct.
```
7. **Mar 19: Don't call people out** — "Ed finally showed up" is useless to someone
   who missed the session. Write for the absent reader.
```

### Three-Source Gate (Subscriber-Facing Skills)

Any skill that produces output for paying subscribers gets this hard rule:

> Every factual claim must come from one of three sources in THIS session:
> (a) Josh's exact words, (b) a tool result, or (c) a search you ran and can cite.
> Can't cite it? Cut the sentence.

Add this as a `⛔ HARD RULE` at the top of the skill, same level as "never show copy in chat."

### Symlinked References

Voice skills share reference files. Don't copy — symlink:
```bash
ln -sf /home/clawdbot/clawd/references/email-voice/voice-dna.md references/voice-dna.md
ln -sf /home/clawdbot/clawd/references/email-voice/gold-standard.md references/gold-examples.md
```

One source of truth. Updates propagate to all skills automatically.

### Model Routing

Skills that spawn sub-agents should specify the model:
- **Opus** — Voice writing only (journal, X posts, email copy, alerts). The output IS the voice.
- **Sonnet** — Everything else (research, data, building, organizing)
- **Haiku** — Simple extraction, formatting, quick lookups

### Cron Integration

Skills that run on schedule need a cron job. Define it in the skill:
```
## Cron
Schedule: Thursdays 6 PM ET
Model: sonnet
Session: isolated
Delivery: announce
```

### Data Storage

Skills can store state:
- `data/corrections.log` — Append-only human corrections. Read on every invocation.
- `data/history.log` — What the skill has done (prevents repeating mistakes)
- `data/config.json` — Setup info (if missing, skill asks the user)

Pattern: the skill reads its own history before acting. It gets smarter over time.

## Improving a Skill

When a skill needs improvement, the approach depends on the problem:

**Single correction from Josh** → Add gotcha immediately, same turn. Done. This is maintenance, not a rebuild.

**Pattern of failures** (3+ similar corrections) → The gotchas aren't enough. Read the skill fresh, identify the structural issue, rewrite the relevant section. Then add a gotcha explaining the pattern.

**Full rebuild needed** → Use Track 2 (eval suite). Snapshot the current skill, write test cases, run with-skill vs old-skill comparisons, iterate with human review.

## Description Optimization

After a skill is stable, optimize the description for triggering accuracy. Full process in the skill-creator eval tooling:

1. Generate 20 trigger eval queries (10 should-trigger, 10 should-not-trigger)
2. Review with user via `assets/eval_review.html`
3. Run optimization loop: `python -m scripts.run_loop --eval-set <path> --skill-path <path> --model <model-id> --max-iterations 5`
4. Apply `best_description` to SKILL.md frontmatter

## Eval Process (Track 2 Only)

Full eval details: `references/eval-process.md`

Quick version:
1. Save test cases to `evals/evals.json` (see `references/schemas.md`)
2. Spawn with-skill + baseline sub-agents per test case
3. Grade assertions → `grading.json` (see `agents/grader.md`)
4. Aggregate → `benchmark.json` (run `scripts/aggregate_benchmark.py`)
5. Launch viewer → `eval-viewer/generate_review.py`
6. Read feedback, improve, repeat

## Reference Files

- `references/design-principles.md` — Thariq's philosophy (read before writing any skill)
- `references/eval-process.md` — Full Track 2 eval process (from Anthropic's skill-creator)
- `references/schemas.md` — JSON structures for evals, grading, benchmarks
- `agents/grader.md` — How to evaluate assertions against outputs
- `agents/comparator.md` — Blind A/B comparison between two outputs
- `agents/analyzer.md` — Analyze benchmark results and surface patterns

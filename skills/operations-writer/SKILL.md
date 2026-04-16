---
name: operations-writer
description: "Build or update Belanger Trading Operations Manual documents from Josh's raw notes. Use when Josh provides new notes, context, or input to expand the operations manual - including updating the Operations Manual (operations/operations-manual.md), creating new SOPs, or converting operational knowledge into self-contained Skills. Handles the full pipeline: collect notes, build conceptual map, spawn Opus writer, QA, save. Trigger phrases include: add this to the manual, build an SOP for, update the brand bible, here are my notes on, create a skill for this process."
---

# Operations Writer

Turns Josh's raw notes and input into polished Operations Manual documents using a rigorous write → QA pipeline. The same process that produced Operations Manual.

## Key Files

- **Current Operations Manual:** `operations/operations-manual.md` (924 lines, ~9,500 words)
- **Josh's Notes (source of truth):** `operations/belangers-notes.md`
- **Conceptual Mapping (idea inventory):** `operations/brand-bible-mapping.md`
- **New input:** Ask Josh for the file path or paste inline

## What You Can Build

| Task | Output |
|---|---|
| Update Operations Manual with new notes | Updated `operations-manual.md` (or new version) |
| New SOP | `operations/sops/[name].md` |
| New Skill from process knowledge | `skills/[name]/` via skill-creator |

## Process

### Step 1 — Collect Source Material
Gather all inputs before writing anything:
- Josh's new notes (file path or inline)
- Existing document to update (if updating)
- Read `references/process.md` for QA standards

### Step 2 — Build Conceptual Map
Before writing, create a flat inventory of every distinct idea in Josh's notes:
- One bullet per idea, no grouping yet
- This becomes the QA checklist
- Save as a temp file: `operations/mapping-[doc-name].md`

If updating an existing doc: cross-reference new ideas against existing content first — avoid duplication.

### Step 3 — Spawn Opus Writer
Spawn an Opus sub-agent with:
1. Josh's notes (source of truth — use verbatim language when possible)
2. Existing document structure (as template)
3. Conceptual map (every idea that must appear)

**Task instruction to agent:** "Read all three files completely before writing a single word. Use the structure as template. Every idea in the conceptual map must find a home in the document. Use Josh's exact language and examples — do not paraphrase or sanitize. One pass. Do it right."

### Step 4 — Conceptual Mapping QA
After agent completes, run paragraph-by-paragraph QA:
- Read the new document section by section
- Check each item in the conceptual map — does it have a home?
- **Not keyword search** — check if the concept is expressed, even in different words
- Flag anything missing; spawn a fix agent for gaps

See `references/process.md` for QA checklist and common failure modes.

### Step 5 — Save and Log
- Save output to appropriate file
- Log activity: `./scripts/log-activity.sh "Built [doc name] from Josh's notes" "collaborative"`
- Update WORKQUEUE.md if part of a larger project

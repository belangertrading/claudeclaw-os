---
name: project-manager
description: Create and manage Belanger Trading projects. Use when Josh says "create a project for this", "make this a project", "spin up a project", or when any work needs structured tracking. Handles Ops Dashboard project entry and activity logging. Single source of truth is always the Ops Dashboard.
---

# Project Manager

## Create a Project

When Josh says to create a project (or when work clearly needs one):

### 1. Gather Details

From conversation context, determine:
- **Title** — short, clear project name
- **Vision** — one sentence on what success looks like
- **Priority** — high / medium / low
- **Checklist** — break the work into concrete steps (done: true/false)
- **Technical notes** — file paths, IDs, references needed to do the work
- **Next steps** — what happens immediately after setup

If anything is unclear, ask ONE focused question. Don't interrogate.

### 2. Create Ops Dashboard Entry

Add project to `data/mission-control/projects.json`:

```python
import json
from datetime import datetime, timezone

with open('/home/clawdbot/clawd/data/mission-control/projects.json') as f:
    d = json.load(f)

project = {
    "id": "project-slug",
    "title": "Project Title",
    "vision": "What success looks like in one sentence.",
    "status": "in-progress",
    "priority": "high",
    "eta": "Month Year",
    "checklist": [
        {"text": "First concrete step", "done": False},
        {"text": "Second concrete step", "done": False}
    ],
    "technicalNotes": [
        "Key file paths, sheet IDs, references"
    ],
    "nextSteps": "What happens right after setup."
}

d['projects'].append(project)
d['lastUpdated'] = datetime.now(timezone.utc).isoformat()

with open('/home/clawdbot/clawd/data/mission-control/projects.json', 'w') as f:
    json.dump(d, f, indent=2)
```

### 3. Log It

```bash
./scripts/log-activity.sh "Created project: [Title] — Ops Dashboard entry" "build"
```

### 4. Confirm to Josh

Brief confirmation: project name, what's first on the checklist.

---

## Where Things Live

| What | Where | Purpose |
|------|-------|---------|
| Project details, checklist, status | Ops Dashboard (`projects.json`) | Single source of truth |
| Project chat / iteration | Ops Dashboard project chat (Max) | Built-in agent workspace |
| Working notes (complex projects) | `memory/project-<slug>.md` | Agent context recovery (optional) |
| "We did this" | Activity log (`log-activity.sh`) | Audit trail |
| "We worked on X today" | Daily memory (`memory/YYYY-MM-DD.md`) | Breadcrumb only — no project details |

**Rules:**
- Ops Dashboard owns project status and checklist — no duplication elsewhere
- No WORKQUEUE entries for projects — Ops Dashboard is the tracker
- Project chat lives in the dashboard, not Discord

## Context Recovery (How the Agent Picks Up Stale Projects)

**Default:** Read project chat history from the dashboard.
Chat history stored at: `data/mission-control/chat-history/{projectId}.json`

**Complex projects:** If the project involves dense technical decisions, file changes across multiple sessions, or things that broke and got fixed — create `memory/project-<slug>.md` as working notes. This is NOT a copy of the dashboard. It's what the agent needs to resume work: current approach, what was tried, what failed, key decisions made.

**When to create the project .md:**
- Multiple sessions of iteration with technical depth
- Lots of file paths, code changes, or architectural decisions to track
- Chat history alone wouldn't give the agent enough to resume confidently

**When chat history is enough:**
- Straightforward projects (build a page, write copy, research a topic)
- Short-lived projects (done in 1-2 sessions)

Delete `memory/project-<slug>.md` when the project closes.

---

## Update a Project

When work progresses, update the Ops Dashboard entry directly:
- Check off completed items in the checklist
- Update `nextSteps`
- Change `status` when appropriate: `in-progress` → `complete`

---

## Close a Project

When a project is done:
1. Set `status: "complete"` and `completedDate` in `projects.json`
2. Log: `./scripts/log-activity.sh "Completed project: [Title]" "build"`

---

## Reference

| Item | Value |
|------|-------|
| Ops Dashboard | `http://100.113.44.24:8888` |
| Projects data | `data/mission-control/projects.json` |
| Chat history | `data/mission-control/chat-history/` |

# BT Ops — System Architecture

*Last updated: April 16, 2026 — 3:00 AM EDT*

## Overview

Belanger Trading runs an autonomous agent operating system built on [ClaudeClaw](https://github.com/earlyaidopters/claudeclaw-os) — a TypeScript wrapper around Anthropic's Claude Agent SDK that turns Claude Code into a persistent Telegram bot with multi-agent orchestration, scheduled tasks, and tool access.

**This is the primary system.** OpenClaw is being sunset.

## Version Matrix

| Component | Version | Notes |
|-----------|---------|-------|
| ClaudeClaw | 1.1.0 | `/home/clawdbot/lean-stack` |
| Claude Agent SDK | 0.2.110 | `@anthropic-ai/claude-agent-sdk` |
| Claude Code CLI | 2.1.110 | Auth via OAuth (`~/.claude/`) |
| Node.js | 22.22.2 | Engine requirement: >=20 |
| OS | Ubuntu 24.04 | Linux 6.8.0-107-generic (x64) |

## Agent Roster

| Agent | Role | Model | Delivery |
|-------|------|-------|----------|
| **Henry** 🎩 | COO / Main | claude-opus-4-6 | Telegram DM |
| **Hermes** 🔱 | Trading Analyst & Research | claude-opus-4-6 | Telegram (delegated) |
| **Kyle** ✍️ | Head of Marketing | claude-sonnet-4-6 | Telegram (delegated) |
| **Sloane** 🪞 | Head of Content | claude-sonnet-4-6 | Telegram (delegated) |

## Architecture

```
┌─────────────────────────────────────────────────┐
│                   Telegram                       │
│              (Josh's phone)                      │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│           ClaudeClaw (bt-ops.service)            │
│  TypeScript bot → Claude Agent SDK → Claude Code │
│  Port 3141 (dashboard)                           │
│                                                  │
│  ┌─────────┐ ┌─────────┐ ┌────────┐ ┌────────┐ │
│  │ Henry   │ │ Hermes  │ │ Kyle   │ │ Sloane │ │
│  │ (main)  │ │ (agent) │ │(agent) │ │(agent) │ │
│  └─────────┘ └─────────┘ └────────┘ └────────┘ │
│                                                  │
│  Cron Scheduler (30 jobs)                        │
│  Hive Mind (SQLite shared state)                 │
│  Model Fallback: Opus → Sonnet → Haiku           │
│  Gemini API (embeddings + voice)                 │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│              Ubuntu VPS (belangertrading)         │
│                                                  │
│  XMCP (Twitter API, :8000)                       │
│  Ops Dashboard (:8888)                           │
│  BT Ops Dashboard (:3141)                        │
└─────────────────────────────────────────────────┘
```

## Services

| Service | Type | Command |
|---------|------|---------|
| bt-ops | systemd | `sudo systemctl {start|stop|restart|status} bt-ops` |
| xmcp | systemd | Port 8000, Twitter MCP |

## Model Fallback Chain

Configured via `MODEL_FALLBACK_CHAIN` in `.env`:

```
Opus (primary) → Sonnet → Haiku
```

On overload/billing errors, automatically cascades. User gets notified which model it switched to.

## Cron Jobs (30 total)

Managed by ClaudeClaw's built-in scheduler (not system cron).

**Trading Hours (M-F):**
- 9:00 AM — Morning Brief
- 10:00 / 12:00 / 4:00 PM — Flow Scans
- 8:00 AM — Daily Content Draft

**Daily:**
- 7:00 AM / 12:00 PM — X Scanner
- 7:00 AM — Analytics Collect, Competitor Email Ingest
- 8:00 AM — Competitor Intel Report

Full list: `cat /home/clawdbot/lean-stack/cron/jobs.json`

## Skills

**Main (Henry):** 14 skills in `skills/`
**Hermes:** 28 skills in `agents/hermes/skills/`
**Sloane:** 11 skills in `agents/sloane/skills/`
**Kyle:** 5 skills in `agents/kyle/skills/`

Skills are loaded by the SDK via `.claude/settings.json` and each agent's `CLAUDE.md`.

## Key Files

| Path | Purpose |
|------|---------|
| `/home/clawdbot/lean-stack/` | Project root |
| `src/agent.ts` | Core agent loop (SDK query wrapper) |
| `src/bot.ts` | Telegram bot handlers |
| `src/orchestrator.ts` | Sub-agent delegation |
| `src/scheduler.ts` | Cron job runner |
| `src/gemini.ts` | Gemini API (embeddings, text gen) |
| `cron/jobs.json` | Scheduled job definitions |
| `agents/*/CLAUDE.md` | Agent souls + system prompts |
| `skills/*/SKILL.md` | Skill definitions |
| `store/claudeclaw.db` | Session state + hive mind |
| `.env` | All secrets (gitignored) |
| `.claude/settings.json` | Tool permissions |
| `CLAUDE.md` | Henry's system prompt (gitignored) |

## GitHub

- **Upstream:** [earlyaidopters/claudeclaw-os](https://github.com/earlyaidopters/claudeclaw-os) (public, read-only for jmbel13)
- **Fork:** [belangertrading/claudeclaw-os](https://github.com/belangertrading/claudeclaw-os) (push access, issues enabled)
- **Issues:** <https://github.com/belangertrading/claudeclaw-os/issues>
- **Gitignored:** `.env`, `CLAUDE.md`, `agents/*/agent.yaml`, `agents/*/CLAUDE.md`, `store/`, `dist/`

## Auth

Claude Code authenticates via OAuth stored in `~/.claude/.credentials.json`. The service runs as `clawdbot` user.

**Known issue:** clawdbot's OAuth token can expire independently of root's. If the bot gets 401 errors, sync credentials:
```bash
sudo cp /root/.claude/.credentials.json /home/clawdbot/.claude/.credentials.json
sudo chown clawdbot:clawdbot /home/clawdbot/.claude/.credentials.json
sudo chmod 600 /home/clawdbot/.claude/.credentials.json
sudo systemctl restart bt-ops
```

## Permissions

Tool permissions are managed via `.claude/settings.json` (NOT `--dangerously-skip-permissions`, which is blocked when the user has sudo access). All standard tools are allowed.

## Known Issues & Fixes (April 16)

### 1. SDK Dual-Result-Event (FIXED)
The SDK emits two `result` events: `success` then `error_during_execution` (exit code 1). Fixed with `if (!resultText)` guard in `agent.ts` catch block — returns captured result instead of throwing.

### 2. bypassPermissions + sudo (FIXED)
`--dangerously-skip-permissions` is rejected when user has NOPASSWD sudo. Removed from agent.ts. Permissions handled via `.claude/settings.json`.

### 3. OAuth Token Expiry (FIXED, needs automation)
clawdbot's token expired April 5. Root's was fresh. Copied root → clawdbot. Need automated sync (GitHub issue #2).

### 4. Exit Code 1 on Success
Claude Code exits with code 1 even on successful completions. Stderr: "Unexpected non-whitespace character after JSON". Mitigated with `NO_COLOR=1`, `TERM=dumb`, `FORCE_COLOR=0` in systemd env. Reported: [anthropics/claude-code#48971](https://github.com/anthropics/claude-code/issues/48971)

## Debugging

**Service logs:**
```bash
sudo journalctl -u bt-ops -f              # live
sudo journalctl -u bt-ops --since '1h ago' # recent
```

**SDK debug mode:**
```bash
DEBUG_CLAUDE_AGENT_SDK=1 node dist/index.js
# Writes detailed logs to ~/.claude/debug/
```

**Dashboard:** `http://localhost:3141` (requires DASHBOARD_TOKEN)

## Maintenance

```bash
cd /home/clawdbot/lean-stack
npm run build
sudo systemctl restart bt-ops
```

## Environment Variables

All secrets in `/home/clawdbot/lean-stack/.env`:

```
TELEGRAM_BOT_TOKEN       — Telegram bot auth
ALLOWED_CHAT_ID          — Josh's Telegram chat ID (5851857072)
DASHBOARD_TOKEN          — Dashboard auth
DB_ENCRYPTION_KEY        — SQLite encryption
GOOGLE_API_KEY           — Gemini API (embeddings + voice)
MODEL_FALLBACK_CHAIN     — Opus → Sonnet → Haiku
AGENT_MAX_TURNS          — Max agentic turns per query
AGENT_TIMEOUT_MS         — Per-query timeout
CONTEXT_LIMIT            — Token context limit
STREAM_STRATEGY          — Response streaming mode
SMART_ROUTING_ENABLED    — Model routing toggle
SMART_ROUTING_CHEAP_MODEL — Cheap model for simple queries
SHOW_COST_FOOTER         — Cost display toggle
```

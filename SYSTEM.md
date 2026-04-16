# BT Ops — System Architecture

*Last updated: April 16, 2026*

## Overview

Belanger Trading runs an autonomous agent operating system built on [ClaudeClaw](https://github.com/earlyaidopters/claudeclaw-os) — a TypeScript wrapper around Anthropic's Claude Agent SDK that turns Claude Code into a persistent Telegram bot with multi-agent orchestration, scheduled tasks, and tool access.

Two parallel systems run on a single Ubuntu VPS:
- **ClaudeClaw (lean stack)** — Telegram bot, cron scheduler, sub-agents
- **OpenClaw** — Discord agents, heartbeat, memory system

## Version Matrix

| Component | Version | Notes |
|-----------|---------|-------|
| ClaudeClaw | 1.1.0 | `/home/clawdbot/lean-stack` |
| Claude Agent SDK | 0.2.50 | `@anthropic-ai/claude-agent-sdk` |
| Claude Code CLI | 2.1.109 | Auth via OAuth (`~/.claude/`) |
| OpenClaw | 2026.4.14 | `/usr/lib/node_modules/openclaw` |
| Node.js | 22.22.2 | Engine requirement: >=20 |
| OS | Ubuntu 24.04 | Linux 6.8.0-107-generic (x64) |

## Agent Roster

### ClaudeClaw Agents (Telegram)

| Agent | Role | Model | Delivery |
|-------|------|-------|----------|
| **Henry** 🎩 | COO / Main | claude-opus-4-6 | Telegram DM |
| **Hermes** 🔱 | Trading Analyst | claude-opus-4-6 | Telegram (delegated) |
| **Kyle** ✍️ | Head of Marketing | claude-sonnet-4-6 | Telegram (delegated) |
| **Sloane** 🪞 | Head of Content | claude-sonnet-4-6 | Telegram (delegated) |

### OpenClaw Agents (Discord)

Same agents available on Discord via OpenClaw gateway + claude bridges.

| Agent | Bridge | Plan |
|-------|--------|------|
| Henry, Sloane, Ari, Wendy, Kyle | :3456 | Max 20x |
| Hermes | :3457 | Max 20x |

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
│  MCP Servers (tools)                             │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│              Ubuntu VPS (belangertrading)         │
│                                                  │
│  OpenClaw Gateway (Discord agents)                 │
│  Claude Bridges (:3456, :3457)                   │
│  XMCP (Twitter API, :8000)                       │
│  Ops Dashboard (:8888)                           │
└─────────────────────────────────────────────────┘
```

## Services

| Service | Type | Command |
|---------|------|---------|
| bt-ops | systemd | `sudo systemctl {start|stop|restart|status} bt-ops` |
| openclaw-gateway | systemd | `openclaw gateway {start|stop|restart|status}` |
| skygem-bridge | systemd | Port 3456, Henry bridge |
| hermes-bridge | systemd | Port 3457, Hermes bridge |
| xmcp | systemd | Port 8000, Twitter MCP |

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

## Skills (14 installed)

```
bt-skill-creator    email-reply         frontend-design
gmail               gogcli              google-calendar
n8n-workflow        operations-writer   pikastream
project-manager     references          slack
timezone            tldr
```

Skills live in `/home/clawdbot/lean-stack/skills/` and are loaded by the SDK via `.claude/settings.json`.

## Key Files

| Path | Purpose |
|------|---------|
| `/home/clawdbot/lean-stack/` | ClaudeClaw project root |
| `src/agent.ts` | Core agent loop (SDK query wrapper) |
| `src/bot.ts` | Telegram bot handlers |
| `cron/jobs.json` | Scheduled job definitions |
| `agents/*/` | Agent configs (CLAUDE.md + agent.yaml) |
| `skills/*/` | MCP-compatible skill modules |
| `store/claudeclaw.db` | Session state + hive mind |
| `.env` | All secrets (gitignored) |
| `.claude/settings.json` | Tool permissions |
| `CLAUDE.md` | Henry's system prompt (gitignored) |
| `/home/clawdbot/clawd/` | OpenClaw workspace (memory, scripts, data) |
| `/root/.openclaw/` | OpenClaw gateway state |

## GitHub

- **Repo:** [earlyaidopters/claudeclaw-os](https://github.com/earlyaidopters/claudeclaw-os) (public)
- **Auth:** `jmbel13` via `gh` CLI (read-only — needs write access added)
- **Gitignored:** `.env`, `CLAUDE.md`, `agents/*/agent.yaml`, `agents/*/CLAUDE.md`, `store/`, `dist/`

## Known Issues & Workarounds

### SDK Dual-Result-Event Bug
The Claude Agent SDK emits two `result` events: `result/success` then `result/error_during_execution` (exit code 1). Fixed in `agent.ts` with `if (!resultText)` guard. Reported to Anthropic (pending).

### Claude Code Exit Code 1
Claude Code exits with code 1 even on successful completions. The stderr contains "Unexpected non-whitespace character after JSON" — likely ANSI codes in the stream. Mitigated with `NO_COLOR=1`, `TERM=dumb`, `FORCE_COLOR=0` in systemd env.

### GitHub Push Access
`jmbel13` has read-only access to `earlyaidopters/claudeclaw-os`. Needs collaborator invite or auth switch to push.

## Environment Variables

All secrets in `/home/clawdbot/lean-stack/.env`:

```
TELEGRAM_BOT_TOKEN      — Telegram bot auth
ALLOWED_CHAT_ID          — Josh's Telegram chat ID
DAShBOARD_TOKEN          — Dashboard auth
DB_ENCRYPTION_KEY        — SQLite encryption
AGENT_MAX_TURNS          — Max agentic turns per query
AGENT_TIMEOUT_MS         — Per-query timeout (ms)
CONTEXT_LIMIT            — Token context limit
STREAM_STRATEGY          — Response streaming mode
SMART_ROUTING_ENABLED    — Model routing toggle
SMART_ROUTING_CHEAP_MODEL — Cheap model for simple queries
SHOW_COST_FOOTER         — Cost display toggle
EXFILTRATION_GUARD_ENABLED — Data leak protection
```

## Maintenance

**Rebuild after code changes:**
```bash
cd /home/clawdbot/lean-stack
npm run build
sudo systemctl restart bt-ops
```

**Check logs:**
```bash
sudo journalctl -u bt-ops -f              # live
sudo journalctl -u bt-ops --since '1h ago' # recent
```

**Dashboard:** `http://localhost:3141` (requires DASHBOARD_TOKEN)

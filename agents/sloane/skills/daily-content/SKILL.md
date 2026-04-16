---
name: daily-content
description: "Write Josh Belanger's daily social media post following the Mon-Fri weekly content cadence. Each day has a specific format: Monday=What I'm Watching, Tuesday=Trade I Didn't Take, Wednesday=Position Update, Thursday=Weird Shit I'm Seeing, Friday=Week's Reality Check. Use when drafting the day's post, when running the daily content cron, or when Josh asks for a daily post without specifying a content type. Always check the day of the week first and use the matching format."
---

# Daily Content — Josh Belanger

## Step 1: Check the Day

Always determine the day of the week before writing. Each day has its own format.

| Day | Format | Energy |
|-----|--------|--------|
| Monday | What I'm Watching | Specific levels, real positions being considered |
| Tuesday | Trade I Didn't Take | Near-miss, process and hesitation |
| Wednesday | Position Update | Live trade update, real numbers |
| Thursday | Weird Shit I'm Seeing | Unusual flow or data, curiosity not authority |
| Friday | Week's Reality Check | Honest P&L accounting, no spin |

Read `/home/clawdbot/clawd/skills/daily-content/references/formats.md` for the full template and example for each day.

## Step 2: Pull Context (if running as cron)

Use `GOG_KEYRING_PASSWORD="henrybot2026" gog sheets get 1YyATKBbAanLe4xvL1C2CdLuGJFteyGnbCrYv1HjuSO8 'A1:R200' -p` to get open Options Insider positions. Use real trades for context where applicable.

## Step 3: Write

One post. One specific thing. Real prices, real hesitations, real numbers.

**Core rules:**
- Start with the most interesting fact — never with setup or context
- "Lost $3K on Tesla puts today" beats "While everyone was watching the Fed..." every time
- Write like texting a friend who trades
- Show confusion, mistakes, hesitation — that's content too
- Never position Josh as having special secrets
- Some days nothing happened. Say that.

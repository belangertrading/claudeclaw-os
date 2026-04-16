---
name: weekly-damage-report
description: Write Josh Belanger's Friday "Week's Reality Check" post — the weekly damage report. Pulls open position data from Google Sheets, total P&L for the week, biggest win, biggest loss, what's being held over the weekend. Output is a short post in Josh's voice for X/Twitter or email. Use every Friday, or when Josh asks for a weekly recap or damage report.
---

# Weekly Damage Report — Friday Reality Check

## What It Is

End of week. Honest accounting. No spin. Total P&L, biggest win, biggest loss, what's held over the weekend. Written like texting a friend who trades.

## Step 1 — Pull Current Data

Fetch open positions from sheets:
- OI Sheet: `1YyATKBbAanLe4xvL1C2CdLuGJFteyGnbCrYv1HjuSO8`
- HMT Sheet: `12VsTbwaABgz8rLfDJQVm2n1YE-n5SzLUhFM4igpJH5o`
- 48HC Sheet: `1x9xQJAwWxkSY1lpkBLZlHZjhkjw2ZwAH1yybhZz_F00`

Use `GOG_KEYRING_PASSWORD="henrybot2026" gog sheets get <sheetId> 'A1:R200' -p` to pull each sheet.

If Josh provides a week's P&L and trade notes directly, skip the sheet pull and use what he gives.

## Step 2 — Write the Post

See `references/template.md` for format and examples.

## Output Rules

- Total net P&L for the week — real number
- 1–2 specific trades called out (biggest win, biggest loss)
- What's being held over the weekend
- Optional: contrast with a subscriber win if the gap is notable (see contrast-post skill)
- Short. Punchy. One specific thing per line.
- Never spin a bad week. A bad week IS the content.

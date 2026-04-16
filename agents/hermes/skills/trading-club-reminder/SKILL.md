---
name: trading-club-reminder
description: Send the weekly Trading Club session reminder email every Wednesday. Includes market context, trade submission checklist, and Zoom link for Thursday's 3 PM ET session. Triggers on "trading club reminder", "send the reminder", "thursday session email", "trading club email", "remind members about thursday", or any request to send the pre-session reminder to Trading Club members. Also triggered by Wednesday cron job.
---

# Trading Club Weekly Reminder

Every Tuesday, send a reminder to Trading Club + Titans members about Thursday's 3 PM ET session. The email has three jobs: get them excited about the session, give them the trade submission form link (deadline: Wednesday 4 PM ET) so they come prepared, and include fresh market context so it never feels copy-pasted.

## ⛔ HARD RULES

1. **NEVER fire the webhook without Josh's approval.** Draft first, show him, wait for "good" / "approved" / "let it rip."
2. **The webhook is ALWAYS LIVE.** No test pings, no health checks. Every POST sends real emails and SMS.
3. **Fresh market context every week.** Pull real data — never reuse last week's context. If you can't get data, say "markets" generically but never fabricate numbers.
4. **"We"/"I" framing only — never "you" for trading principles.** Compliance requirement. Same rule as trading-club-recap.
5. **Zero member names.** Ever.

## Pipeline

### Step 1: Get Market Context

Pull current market data for the email opener. Keep it to 2-3 sentences max — just enough to make the email feel timely.

Sources (in order of preference):
1. `python3 ~/clawd/scripts/get_price.py SPY` + `python3 ~/clawd/scripts/get_price.py QQQ` for index levels
2. Web fetch for top market story of the day
3. Any open positions from the trade sheets that are moving

The market context is the HOOK — it's why this email doesn't feel like a recurring template.

### Step 2: Draft the Email

**Voice:** Josh — direct, no fluff, like texting his trading group. Short paragraphs.

**Structure:**
1. **Market hook** (2-3 sentences) — What's happening RIGHT NOW. Tie to what makes Thursday's session relevant.
2. **Session details** — Thursday at 3 PM ET, Zoom link
3. **Trade submission form** — Link to the Google Form with deadline callout:
   - "Submit your trade by Wednesday 4 PM ET"
   - Link the form prominently (button style, like the recap CTA)
   - Briefly list what the form asks: ticker, position, entry trigger, exit plan, thesis
4. **Closing** — Short, forward-looking. "Get your trades in, we'll break them all down Thursday."
5. **Sign-off** — "-Josh"

**Google Form:** See `references/form-details.md` for the live form URL and linked Google Sheet ID.

**Zoom link:** `https://us06web.zoom.us/j/85aboredacted` (check references/zoom-details.md if this changes)

### Step 3: Build the HTML Email

Use the standard member-memo HTML template pattern:

```python
import requests
from datetime import datetime

date_str = datetime.now().strftime('%d %b %Y')
subject = "Trading Club — This Thursday at 3 PM ET"
header_img = "https://joshbelanger.com/wp-content/uploads/2023/11/BT_Mentorship_Email_Header.webp"

# body_html = your drafted paragraphs as HTML <p> tags
# sms_text = short version with __NAME__ placeholder

disclaimer = "This communication is for informational purposes only. It is not a recommendation to buy or sell any security. Trading options involves significant risk and is not suitable for all investors. Past performance does not guarantee future results. Always do your own due diligence."

email_html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body style="margin:0; padding:0; background-color:#f5f5f5; font-family:Georgia, 'Times New Roman', serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#f5f5f5;">
<tr><td align="center" style="padding:20px 10px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; max-width:600px; width:100%;">
<tr><td><img src="{header_img}" alt="Trading Club" width="600" style="display:block; width:100%; height:auto;"></td></tr>
<tr><td style="padding:20px 30px 0 30px;"><p style="margin:0; font-size:14px; color:#666;">{date_str}</p></td></tr>
<tr><td style="padding:15px 30px 0 30px;"><h1 style="margin:0; font-size:26px; font-weight:bold; color:#1a1a1a; line-height:1.3;">{subject}</h1></td></tr>
<tr><td style="padding:20px 30px; font-size:17px; line-height:1.7; color:#1a1a1a;">{body_html}</td></tr>
<tr><td style="padding:0 30px;"><hr style="border:none; border-top:2px solid #d4a843; margin:10px 0 20px 0;"></td></tr>
<tr><td style="padding:0 30px 20px 30px; font-size:13px; line-height:1.6; color:#555;"><p style="margin:0;">{disclaimer}</p></td></tr>
</table></td></tr></table></body></html>"""

payload = {
    "service": "Trading Club",
    "subject": subject,
    "emailHtml": email_html,
    "smsText": f"Hi __NAME__, Trading Club is tomorrow (Thursday) at 3 PM ET. Check your email for the trade submission checklist. Reply STOP to unsubscribe",
    "postId": 0,
    "link": "",
    "fromName": "Josh Belanger - Trading Club",
    "replyTo": "support@joshbelanger.com"
}

resp = requests.post("http://localhost:5678/webhook/alert-notify", json=payload, timeout=15)
print(f"Trading Club: {resp.status_code}")
```

### Step 4: Get Approval

Show Josh:
- Subject line
- Full email body text
- SMS text

Wait for explicit approval before firing.

### Step 5: Send

Fire to `"Trading Club"` service. This reaches Trading Club + Titans members.

**Do NOT also send to Alliance.** Alliance doesn't get Trading Club content (they're not in the mentorship program).

### Step 6: Log It

Append to `memory/YYYY-MM-DD.md`:
- Subject, service, webhook status
- Brief note on market context used

## Cron

Schedule: Tuesdays 11 AM ET
Model: sonnet
Session: isolated
Delivery: announce to main session

The cron fires the skill, drafts the email, and delivers to Henry's session for Josh approval before sending.

## Service Routing

| service= | Contacts Matched |
|---|---|
| `"Trading Club"` | Trading Club or Titans |

Titans always get Trading Club content. No need for a separate Titans send.

## Gotchas

1. **Apr 15: Include the full trade submission checklist.** First attempt today was just a generic "come prepared" email. Josh caught it — the checklist IS the value. Members need: ticker, position, entry trigger, exit plan, thesis defense. Every week.

2. **Apr 15: Fresh market context is mandatory.** Without it, the email reads like a recurring calendar invite. Pull real numbers — even just SPY/QQQ levels and the week's story. That's what makes members actually read it instead of skipping.

3. **Apr 15: Don't over-corporate the voice.** First 48HC memo draft same day was too stiff. Josh's voice for member comms is casual, direct — like texting the group. Read member-memo skill voice notes if unsure.

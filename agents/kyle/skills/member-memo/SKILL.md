---
name: member-memo
description: Send a direct memo or update to service members (Options Insider, Hot Money Trader, 48-Hour Cashflow, Alliance, Titans, Trading Club) via n8n webhook without creating a WordPress post. Use when Josh wants to email/SMS members with an update, notice, schedule change, or any communication that isn't a trade alert. Triggers on phrases like "send a memo", "update members", "let subscribers know", "send to OI/HMT/Titans/Alliance members", "member update", or any request to communicate directly with service members outside the normal alert flow.
---

# Member Memo Publisher

Send memos and updates directly to service members via the n8n webhook. No WordPress post created — this is for communications that don't belong on the site.

## When to Use

- Market updates (why no trades this week, schedule changes)
- Service announcements (maintenance, holiday schedule)
- Any member communication that isn't a trade alert

## ⚠️ CRITICAL RULES

1. **NEVER test the webhook.** No curl checks, no `{"test": true}`, no health checks. The webhook is ALWAYS live. Every POST sends real emails and SMS to real members. There is no test mode.
2. **Draft first, always.** Show Josh the subject, email body, and SMS text. Get explicit "good" / "approved" before firing.
3. **One fire per service.** Each service is a separate webhook call with its own branded header.

## Pipeline

### Step 1: Draft the Memo

Write in Josh's voice — direct, no fluff. These are paying members, not blog readers.

Collect from Josh:
- What's the message? (he'll give you the raw idea)
- Which services? (OI, HMT, 48HC, Alliance, Titans, Trading Club, or all)

## Service Routing (IMPORTANT)

N8N routes based on the `service` field. The routing is **hierarchical**:

| service= | Contacts matched (by Service field) |
|---|---|
| `"Options Insider"` | OI or Alliance or Titans |
| `"Hot Money Trader"` | HMT or Alliance or Titans |
| `"48 Hour Cashflow"` | 48HC or Alliance or Titans |
| `"Alliance"` | Alliance or Titans |
| `"Trading Club"` | Trading Club or Titans |
| `"Titans"` | Titans only |

⚠️ **DUPLICATE WARNING:** Titans match ALL sends (except Test). If you fire both `"Alliance"` and `"Trading Club"` for the same email, Titans get it twice. No dedup in n8n. Think before multi-sending: do you actually need both, or does one send already cover Titans?

**Tier hierarchy:** Titans > Alliance > Trading Club > Individual services
- **Titans** get EVERYTHING (all alerts, research, mentorship, extras)
- **Alliance** gets all alerts (OI/HMT/48HC) + research. NO mentorship/Trading Club content.
- **Trading Club** gets mentorship ONLY. No alerts, no reports.
- **Individual services** (OI/HMT/48HC) get only their specific alerts.

⚠️ When Josh says "send to Titans" → use service="Titans" (only Titans get it)
⚠️ When Josh says "send to Alliance" → use service="Alliance" (Alliance + Titans get it)
⚠️ When Josh says "send to everyone" → fire separate calls for each service

Draft:
- **Subject line** — clear, no clickbait
- **Email body** — short paragraphs, Georgia font renders well, no HTML gimmicks
- **SMS text** — under 300 chars ideal, must include `__NAME__` placeholder and end with `Reply STOP to unsubscribe`

### Step 2: Get Approval

Show Josh the complete draft. Do not fire until he says yes.

### Step 3: Build and Send

Use the Python pattern below. One call per service.

```python
import requests
from datetime import datetime

date_str = datetime.now().strftime('%d %b %Y')
subject = "YOUR SUBJECT HERE"
body_html = """<p>Your paragraphs here</p>"""
sms_text = "Hi __NAME__, your SMS here. Reply STOP to unsubscribe"

# Service configs
SERVICES = {
    "Options Insider": {
        "header": "https://joshbelanger.com/wp-content/uploads/2023/11/Belangers_Options_Insider_Email_Header.webp",
        "fromName": "Josh Belanger - Options Insider"
    },
    "Hot Money Trader": {
        "header": "https://joshbelanger.com/wp-content/uploads/2023/11/HMT-Email-Header.webp",
        "fromName": "Josh Belanger - Hot Money Trader"
    },
    "48 Hour Cashflow": {
        "header": "https://joshbelanger.com/wp-content/uploads/2023/11/48-Hour-Cash-Flow-Email-Headers.webp",
        "fromName": "Josh Belanger - 48 Hour Cashflow"
    },
    "Alliance": {
        "header": "https://joshbelanger.com/wp-content/uploads/2023/11/BT_Mentorship_Email_Header.webp",
        "fromName": "Josh Belanger - Trading Alliance"
    },
    "Titans": {
        "header": "https://joshbelanger.com/wp-content/uploads/2023/11/BT_Mentorship_Email_Header.webp",
        "fromName": "Josh Belanger - Titans"
    },
    "Trading Club": {
        "header": "https://joshbelanger.com/wp-content/uploads/2023/11/BT_Mentorship_Email_Header.webp",
        "fromName": "Josh Belanger - Trading Club"
    }
}

disclaimer = "This communication is for informational purposes only. It is not a recommendation to buy or sell any security. Trading options involves significant risk and is not suitable for all investors. Past performance does not guarantee future results. Always do your own due diligence."

for service_name in ["Options Insider", "Hot Money Trader"]:  # adjust per memo
    svc = SERVICES[service_name]
    email_html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body style="margin:0; padding:0; background-color:#f5f5f5; font-family:Georgia, 'Times New Roman', serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#f5f5f5;">
<tr><td align="center" style="padding:20px 10px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; max-width:600px; width:100%;">
<tr><td><img src="{svc['header']}" alt="{service_name}" width="600" style="display:block; width:100%; height:auto;"></td></tr>
<tr><td style="padding:20px 30px 0 30px;"><p style="margin:0; font-size:14px; color:#666;">{date_str}</p></td></tr>
<tr><td style="padding:15px 30px 0 30px;"><h1 style="margin:0; font-size:26px; font-weight:bold; color:#1a1a1a; line-height:1.3;">{subject}</h1></td></tr>
<tr><td style="padding:20px 30px; font-size:17px; line-height:1.7; color:#1a1a1a;">{body_html}</td></tr>
<tr><td style="padding:0 30px;"><hr style="border:none; border-top:2px solid #d4a843; margin:10px 0 20px 0;"></td></tr>
<tr><td style="padding:0 30px 20px 30px; font-size:13px; line-height:1.6; color:#555;"><p style="margin:0;">{disclaimer}</p></td></tr>
</table></td></tr></table></body></html>"""

    payload = {
        "service": service_name,
        "subject": subject,
        "emailHtml": email_html,
        "smsText": sms_text,
        "postId": 0,
        "link": "",
        "fromName": svc["fromName"],
        "replyTo": "support@joshbelanger.com"
    }

    resp = requests.post("http://localhost:5678/webhook/alert-notify", json=payload, timeout=15)
    print(f"{service_name}: {resp.status_code} — {resp.text[:100]}")
```

### Step 4: Log It

After sending, append to today's `memory/YYYY-MM-DD.md`:
- Subject sent
- Which services received it
- Webhook response status
- Brief context of why it was sent

## Webhook Reference

| Field | Required | Notes |
|-------|----------|-------|
| service | ✅ | Exact match: "Options Insider", "Hot Money Trader", "48 Hour Cashflow", "Alliance", "Titans", "Trading Club" |
| subject | ✅ | Email subject line |
| emailHtml | ✅ | Full HTML email with branded header |
| smsText | ✅ | `__NAME__` in SMS is replaced with first name by n8n. ⚠️ `__NAME__` in email HTML is NOT replaced — use "Trader" or no name for emails |
| postId | ✅ | Use `0` for memos (no WordPress post) |
| link | ✅ | Use `""` for memos |
| fromName | ✅ | Service-specific sender name |
| replyTo | ✅ | `support@joshbelanger.com` |

## n8n Webhook

**URL:** `http://localhost:5678/webhook/alert-notify`
**Method:** POST
**Content-Type:** application/json

🚨 **This webhook is ALWAYS LIVE. Every POST sends real emails and SMS. There is no test endpoint. There is no dry run. Do not ping it for any reason other than sending an approved memo.**

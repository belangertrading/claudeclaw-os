---
name: trading-club-recap
description: Write and send the weekly Trading Club session recap. Two deliverables — (1) a full HTML session brief published to joshbelanger.com, and (2) a short teaser email linking to it. Pulls Zoom transcript, builds brief, uploads, drafts teaser email, sends test via n8n, gets approval, sends to Trading Club (or Alliance for open houses). Triggers on phrases like "trading club recap", "session recap", "send the recap", "write the recap email", or any request to summarize a Trading Club/mentorship Zoom session. Also triggered automatically by Thursday 6 PM ET cron job.
---

# Trading Club Weekly Recap

Two deliverables from each session:
1. **Full Session Brief** — A standalone HTML page with Bloomberg-dark styling. Published to `joshbelanger.com/trading-club/`
2. **Teaser Email** — Short email in Josh's voice that hooks with what's working NOW, lists what's in the brief, and links to it. Sent via n8n webhook.

The email is NOT the recap anymore. It's the sell for the brief.

## ⚠️ CRITICAL RULES

1. **ALWAYS send test first** — use `service: "Test"` in n8n webhook. Never skip the test.
2. **Get Josh's approval** before sending to real members.
3. **No disclaimer** — Josh removed it from recap emails.
4. **Read last week's actual email before drafting** — voice drift happens fast.
5. **Trading Club sends to `"Trading Club"` service** (matches Trading Club or Titans). For open houses, also send separately to `"Alliance"` (matches Alliance or Titans). Titans will get it twice — that's expected.
6. **NEVER mention who missed, who was late, who showed up, or attendance details.** This email goes to people who WEREN'T there. "Ed didn't make it" or "finally showed up" is useless to them and awkward for the person named. Write as if talking to someone who missed the whole thing.
7. **NEVER include personal/travel/social details.** No one's travel plans, weekend plans, side conversations about food, jokes between members. Stick to: what was traded, what was taught, what the market did. The reader doesn't care that someone went to Nashville.
8. **ZERO member names anywhere in the email.** Not in trade descriptions, not in headers, not in parentheses, not in homework assignments. Write "First trade we covered" not "Karan's trade" or "DOCN (Karan)". The reader doesn't know who these people are. If the transcript says "Karan brought DOCN" → write "First trade we covered was DOCN."
9. **"We" and "I" framing ONLY — never "you" for trading principles.** This is educational content, not investment advice. Every sentence about trading principles must use "we're" / "I'd" / "I'm" — never "you're" / "you should" / "you need to." This is a compliance requirement.

   ❌ WRONG: "You're risking $7.90 to make $2.10"
   ✅ RIGHT: "That's $7.90 of risk for $2.10 of credit"

   ❌ WRONG: "You need at least a third of the spread width"
   ✅ RIGHT: "What I'd like to see — at least a third of the spread width"

   ❌ WRONG: "If you're holding directional positions overnight"
   ✅ RIGHT: "Holding directional positions overnight means..."

   ❌ WRONG: "You can be right and still lose money"
   ✅ RIGHT: "We can be right on direction and still lose money"

   After drafting, do a search for every instance of "you" in the email. Replace each one. Zero tolerance.

## Pipeline

### Step 1: Get the Zoom Transcript

**Default behavior:** If no transcript path provided, look for today's session:
```bash
ls /home/clawdbot/clawd/data/zoom-transcripts/$(date +%Y-%m-%d)-trading-club*.vtt 2>/dev/null
```

If not found, check Zoom cloud for "Belanger Trading Mentorship Weekly Session":

```bash
source /home/clawdbot/.env

ACCESS_TOKEN=$(curl -s -X POST "https://zoom.us/oauth/token?grant_type=account_credentials&account_id=$ZOOM_ACCOUNT_ID" \
  -u "$ZOOM_CLIENT_ID:$ZOOM_CLIENT_SECRET" | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")

# Find today's recording
RECORDINGS=$(curl -s "https://api.zoom.us/v2/users/me/recordings?from=$(date +%Y-%m-%d)&to=$(date -d '+1 day' +%Y-%m-%d)" \
  -H "Authorization: Bearer $ACCESS_TOKEN")

# Extract audio_transcript URL and download
TRANSCRIPT_URL=$(echo "$RECORDINGS" | python3 -c "import sys,json; r=json.load(sys.stdin); print([f['download_url'] for m in r.get('meetings',[]) for f in m.get('recording_files',[]) if f.get('recording_type')=='audio_transcript'][0] if r.get('meetings') else '')")

if [ -n "$TRANSCRIPT_URL" ]; then
  curl -sL "$TRANSCRIPT_URL" -H "Authorization: Bearer $ACCESS_TOKEN" -o /tmp/zoom-club-transcript.vtt
else
  echo "No recording found for today"
  exit 0
fi
```

### Step 2: Save Transcript

Two copies:
1. **Mac Studio:** Use Zoom's default naming format. Construct from the meeting's `start_time` (UTC):
   ```bash
   # Example: start_time=2026-03-19T18:59:01Z → GMT20260319-185901_Recording.transcript.vtt
   ZOOM_FILENAME="GMT$(echo $START_TIME | sed 's/[T:-]//g' | cut -c1-15)_Recording.transcript.vtt"
   scp /tmp/zoom-club-transcript.vtt "User@100.91.66.81:~/Documents/Belanger_Trading/Products_Services/Trading_Club/Weekly_Transcripts/${ZOOM_FILENAME}"
   ```
2. **Local:** `cp /tmp/zoom-club-transcript.vtt /home/clawdbot/clawd/data/zoom-transcripts/$(date +%Y-%m-%d)-trading-club.vtt`

### Step 3: Analyze the Transcript

Extract:
- Who was on the call (Josh + members)
- Key trades discussed (ticker, strategy, strikes, expiry, thesis, outcome)
- Market context Josh covered
- Teaching moments / lessons
- Announcements (next week, open house, etc.)

### Step 4: Build the Full Session Brief (HTML)

This is the main deliverable. A standalone HTML page that breaks down every trade, every lesson, and the market context from the session.

**Template reference:** `data/presentations/trading-club-2026-04-09-full.html`

**Design system:**
- Fonts: DM Sans (body), JetBrains Mono (data/labels)
- Colors: `--bg: #0a0a0a`, `--surface: #111111`, `--amber: #d4a843`, `--red: #e05555`, `--green: #4caf50`
- Max width: 820px centered
- Header: amber border-bottom, JetBrains Mono section tags, date meta
- Components: snapshot cards (grid), trade cards (with ticker, trade-type badge, trade-grid details), callout boxes (amber/red/green/blue/purple borders), comparison tables, key-lesson boxes

**Structure:**
1. **Header** — "Trading Club Recap | {date}" with subtitle
2. **Snapshot bar** — Market data cards (S&P, VIX, key numbers from session)
3. **Market Context section** — Josh's macro overview from the session opening
4. **The Playbook section** — Core strategy/theme of the session (if applicable)
5. **Trade Review sections** — One per trade discussed, each with:
   - Trade card: ticker, strategy, strikes, expiry, debit/credit, result, allocation
   - Trade grid: key metrics in dark cards
   - Analysis paragraphs: Josh's reasoning, the lesson
   - Callout boxes: key insights, traps, warnings
   - Comparison tables: when comparing approaches (e.g. spread vs long calls)
6. **Position Updates** — Brief status on other open positions mentioned
7. **Key Takeaways** — Thread-through lessons with key-lesson boxes

**All critical rules apply to the brief too** — zero member names, "we"/"I" framing, no personal details, no attendance.

**Save to:** `data/presentations/trading-club-YYYY-MM-DD-full.html`

### Step 5: Upload the Brief

SCP the HTML to the Mac Studio webserver:
```bash
scp /home/clawdbot/clawd/data/presentations/trading-club-YYYY-MM-DD-full.html User@100.91.66.81:/var/www/joshbelanger.com/trading-club/
```

Verify it's live:
```bash
curl -sI https://joshbelanger.com/trading-club/trading-club-YYYY-MM-DD-full.html | head -5
```

URL pattern: `https://joshbelanger.com/trading-club/trading-club-YYYY-MM-DD-full.html`

### Step 6: Read Voice References (for the teaser email)

**Before drafting the teaser:**
1. `/home/clawdbot/clawd/references/email-voice/voice-dna.md`
2. `/home/clawdbot/clawd/references/email-voice/gold-standard.md`
3. **Last week's actual email:**
   ```bash
   GOG_KEYRING_PASSWORD="henrybot2026" gog gmail search "subject:'Trading Club' from:josh@joshbelanger.com newer_than:14d" --account jmbelanger@gmail.com --limit 1 -p
   ```
   Then read the full email with `gog gmail read <ID> --account jmbelanger@gmail.com --full -p`

### Step 7: Draft the Teaser Email

The email is NOT the full recap. It's a short hook that drives to the brief.

**Header image:** `https://joshbelanger.com/wp-content/uploads/2023/11/BT_Mentorship_Email_Header.webp`

**Structure:**
1. **Opening hook** — What's happening RIGHT NOW that connects to what was covered (1-2 sentences). Tie to live market action if possible.
2. **Context on format** (first few times only) — Brief note about the new session brief format.
3. **What's working** — Trades from the session that are already moving. Creates urgency.
4. **What's inside the brief** — List key sections conversationally with bold headers. NOT bullet points — flowing paragraphs with bolded topic names. Each one is a mini-hook.
5. **CTA button** — "Read the Full Session Brief" linking to the HTML brief URL. Amber button (#d4a843 bg, #1a1a1a text).
6. **Close** — "Same time Thursday. -Josh"

**Teaser email voice:**
- Short paragraphs, conversational Josh voice
- Specific numbers when referencing working trades
- The brief does the heavy lifting — the email just needs to make them click
- No "you" framing (same compliance rule)
- No member names

### Step 8: Send Test

```python
import requests
from datetime import datetime

subject = "Trading Club — {Month} {Day} Session Recap"
brief_url = "https://joshbelanger.com/trading-club/trading-club-YYYY-MM-DD-full.html"
body_html = """<p>Teaser paragraphs here with CTA button...</p>
<p style="margin: 24px 0;"><a href="BRIEF_URL_HERE" style="display: inline-block; background-color: #d4a843; color: #1a1a1a; text-decoration: none; padding: 14px 32px; font-weight: bold; border-radius: 4px; font-size: 16px;">Read the Full Session Brief</a></p>
<p>Same time Thursday.</p>
<p>-Josh</p>"""

payload = {
    "service": "Test",
    "subject": subject,
    "emailHtml": f"""<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body style="margin:0; padding:0; background-color:#f5f5f5; font-family:Georgia, 'Times New Roman', serif;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#f5f5f5;">
<tr><td align="center" style="padding:20px 10px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff; max-width:600px; width:100%;">
<tr><td><img src="https://joshbelanger.com/wp-content/uploads/2023/11/BT_Mentorship_Email_Header.webp" alt="Trading Club" width="600" style="display:block; width:100%; height:auto;"></td></tr>
<tr><td style="padding:20px 30px 0 30px;"><p style="margin:0; font-size:14px; color:#666;">{datetime.now().strftime('%d %b %Y')}</p></td></tr>
<tr><td style="padding:15px 30px 0 30px;"><h1 style="margin:0; font-size:26px; font-weight:bold; color:#1a1a1a; line-height:1.3;">{subject}</h1></td></tr>
<tr><td style="padding:20px 30px; font-size:17px; line-height:1.7; color:#1a1a1a;">{body_html}</td></tr>
<tr><td style="padding:0 30px;"><hr style="border:none; border-top:2px solid #d4a843; margin:10px 0 20px 0;"></td></tr>
</table></td></tr></table></body></html>""",
    "smsText": "Hi __NAME__, Trading Club recap is in your inbox. Reply STOP to unsubscribe",
    "postId": 0,
    "link": "",
    "fromName": "Josh Belanger - Trading Club",
    "replyTo": "support@joshbelanger.com"
}

resp = requests.post("http://localhost:5678/webhook/alert-notify", json=payload, timeout=15)
print(f"Test sent: {resp.status_code}")
```

Tell Josh: "Test sent, check your inbox."

### Step 9: Get Approval and Send

Wait for Josh to approve. Then fire to the appropriate service(s):

```python
# Normal week
payload["service"] = "Trading Club"
requests.post("http://localhost:5678/webhook/alert-notify", json=payload, timeout=15)

# Open house week (Josh will tell you)
payload["service"] = "Trading Club"
requests.post("http://localhost:5678/webhook/alert-notify", json=payload, timeout=15)
payload["service"] = "Alliance"
requests.post("http://localhost:5678/webhook/alert-notify", json=payload, timeout=15)
```

### Step 10: Delete Zoom Recording

After sending is confirmed, delete the cloud recording to free storage:

```bash
source /home/clawdbot/.env
ACCESS_TOKEN=$(curl -s -X POST "https://zoom.us/oauth/token?grant_type=account_credentials&account_id=$ZOOM_ACCOUNT_ID" \
  -u "$ZOOM_CLIENT_ID:$ZOOM_CLIENT_SECRET" | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")

# Double-encode the meeting UUID (required if it contains / or =)
ENCODED_UUID=$(python3 -c "import urllib.parse; print(urllib.parse.quote(urllib.parse.quote('$MEETING_UUID', safe=''), safe=''))")

# Move to trash (recoverable for 30 days)
curl -s -o /dev/null -w "%{http_code}" -X DELETE \
  "https://api.zoom.us/v2/meetings/${ENCODED_UUID}/recordings?action=trash" \
  -H "Authorization: Bearer $ACCESS_TOKEN"
```

204 = success. The recording goes to Zoom trash (recoverable for 30 days).

### Step 11: Log It

Append to `memory/YYYY-MM-DD.md`:
- Recap sent, subject, which services, response status
- Brief note on session content

## Service Routing

| service= | Contacts Matched (n8n routing) |
|---|---|
| `"Trading Club"` | Trading Club or Titans |
| `"Alliance"` | Alliance or Titans |
| `"Test"` | Josh only |

⚠️ **Titans get duplicates** when you send to both Trading Club AND Alliance. This is expected for open house weeks.

## Error Handling

- **No Zoom recording found:** Reply HEARTBEAT_OK (no session happened)
- **VTT parse fails:** Check file encoding, try fallback to plain text transcript
- **n8n webhook timeout:** Retry once after 5 seconds. If still fails, notify Josh via Telegram.
- **Voice-dna.md not found:** Use last week's email as sole voice reference

## Gotchas

1. **Mar 19: Voice drift** — First draft was too structured/corporate. Josh said "doesn't sound like last week." ALWAYS re-read the actual previous email before drafting. Command:
   ```bash
   GOG_KEYRING_PASSWORD="henrybot2026" gog gmail search "subject:'Trading Club' from:josh@joshbelanger.com newer_than:14d" --limit 1 -p
   ```
   Then `gog gmail read <ID> --full -p` to read the full email. Don't write from memory.

2. **Mar 19: gog --account flag** — Draft created without `--account jmbelanger@gmail.com` didn't show in drafts. Always pass `--account` if using gmail drafts (though this skill sends directly via webhook).

3. **Mar 19: Alliance routing** — Alliance does NOT get Trading Club content normally. Only send to Alliance when it's an open house. Titans will get duplicates when you send to both.

4. **Mar 19: Don't build HTML from scratch** — Use the member-memo skill's standard branded template. Don't reinvent it.

5. **Mar 19: Test first always** — Use `service: "Test"` to send Josh a preview before firing to real members.

6. **Mar 19: No disclaimer** — Josh explicitly removed it. Don't add it back.
7. **Mar 19: Don't call people out or get too personal** — No "Ed finally showed up," no "your reasoning was..." directed at members by name in a critical way. This email goes to people who missed OR attended. Keep it informative and educational, not like you're publicly grading homework.
8. **Mar 19: No inside-baseball details** — Don't include personal travel plans, side conversations (rice, Nashville hot chicken), or "it's just you and me next week." Stick to what was traded, what was taught, and the market context.
9. **Mar 19: Don't rename VTT files**
10. **Apr 2: Open with context** — Don't assume the reader knows why they're getting this email. Start with "Here's a recap of today's session in the Trading Club" before any market commentary.
11. **Apr 2: Include Josh's market analysis** — Josh always opens with a market regime overview (where S&P is, VIX level, what's working, what's not). Include this before jumping to trades.
12. **Apr 2: No member names** — Don't write "Karan brought" or "Ed put on." Write "First trade we covered was..." The email is educational, not a roll call.
13. **Apr 2: Include strikes** — Always include the full trade structure (strikes, expiry, premium collected/paid). Don't summarize without specifics.
14. **Apr 2: Educational framing, not investment advice** — Use "What I'd like to see if I were doing this" not "The problem is." Use "we're" and "I'm" instead of "you're." These are educational recaps, not directed advice.
15. **Apr 2: "We" not "I" for service trades** — "We closed the USO spread we've been holding" not "I closed." It's a collective service.
16. **Apr 2: n8n returns 200 even on failure** — The webhook always returns 200. Must verify execution status via API after sending. If execution fails (e.g., Google Sheets 503), retry after 60 seconds. Don't give up — keep retrying until it succeeds. — Use Zoom's default naming: `GMT{YYYYMMDD}-{HHMMSS}_Recording.transcript.vtt` (from meeting start_time UTC). Don't invent custom names. Save to `~/Documents/Belanger_Trading/Products_Services/Trading_Club/Weekly_Transcripts/` on Mac Studio.

---
name: email-reply
description: Draft email replies in Josh's voice using gog CLI. Use when replying to any email, drafting customer responses, handling complaints, cancellations, refunds, win celebrations, upgrade pitches, follow-ups, or any outbound email. Also use when Josh says 'reply to this', 'draft a response', 'email them back', 'see email from X', forwards an email for response, or asks to check/handle an email.
---

# Email Reply Skill

Draft email replies that are indistinguishable from Josh writing them himself.

## Workflow

1. **Read the source email first** — Always read the actual email before drafting. Never guess at the situation. Use `GOG_KEYRING_PASSWORD="henrybot2026" gog gmail get <messageId> -p` to fetch the full message.

2. **Identify the situation type** — What kind of reply is this? (See categories below.) This determines tone, length, and structure.

3. **Read voice calibration** — Before drafting, read `references/voice-dna.md` for tone patterns. If this is a complaint or sales situation, also read `references/gold-examples.md` for calibration.

4. **Draft the reply** — Follow the patterns from the reference docs. When in doubt, shorter is right.

5. **Create as Gmail draft** — Use the `scripts/create-draft.sh` helper to create the draft threaded to the original email.

6. **Delete old drafts first** — If replacing a previous draft, delete the old one before creating the new one.

## Situation Categories

| Type | Tone | Length | Key Pattern |
|------|------|--------|-------------|
| Simple confirmation | Neutral, brief | 1-3 sentences | Confirm action, done |
| Data correction / feedback | Acknowledge, brief | 2-4 sentences | "Good catch" → confirm fix → invite more |
| Cancellation | Neutral + curious | 2-4 sentences | Confirm → probe with one question |
| Mistake/refund | Humble, direct | 3-5 sentences | Own it → state fix → timeline → one apology |
| Complaint | Mirror emotions | 3-5 sentences | Tactical empathy → name the feeling → one question |
| Win celebration | Enthusiastic | Medium | Their details → specific praise → teaching moment |
| Upgrade/sales | Validating | Longer | Validate their approach → connect to them → present offer |
| Personal/friendly | Warm, casual | Medium | Reference what they shared → genuine question |
| Tech support | Helpful, brief | 2-4 sentences | State what you see → ask clarifying question |

## Chris Voss Framework (for complaints and difficult replies)

Mirror, don't solve. Name the emotion. Let them respond.

- "It sounds like..." / "It seems like..." — mirror what they said
- Don't guess what they mean. Reflect it back, let them correct you.
- One volley at a time. Don't tackle all their points in one email.
- After empathy: put it back on them with a calibrated question ("Can you see yourself moving forward?")

## Reference Files

- `references/voice-dna.md` — Full voice analysis (sentence structure, vocabulary, tone shifts, templates). **Read before every draft.**
- `references/gold-examples.md` — Best examples by situation type. Read when calibrating for a specific category.
- `references/reply-examples.md` — 50 categorized real replies. Browse when you need more examples of a specific type.

## Gotchas

These are real failures. Each one cost time and trust. Read every time.

1. **Josh's replies are shorter than you think.** The Patrick email (Mar 18, 2026): I wrote "Good catch — you're right, that was incorrect. It's been updated. Appreciate you taking the time to go through the data and flag it. Any other issues you find, let me know." Josh sent: "Good catch — you're right, that was incorrect. It's been updated. If you find any other issues, let me know. -Josh" — Cut the gratitude filler. "Appreciate you taking the time" = unnecessary.

2. **READ THE ACTUAL EMAIL BEFORE DRAFTING.** The Karan disaster (Mar 16, 2026): Drafted 10+ broken replies without reading his email first. Guessed wrong about the entire situation. Fabricated "session recordings" that don't exist. Read the email. Understand the context. Then write.

3. **Never fabricate details.** Don't invent services, recordings, offerings, or promises that don't exist. If you don't know what we offer, check before writing.

4. **Use gog, not himalaya.** `GOG_KEYRING_PASSWORD="henrybot2026" gog gmail ...` — OAuth is permanently fixed. himalaya is the old workaround.

5. **Delete old drafts before creating new ones.** Don't stack drafts. Delete first, then create.

6. **Don't ask "want me to change anything?"** If Josh corrects you, fix it immediately and show the result. Don't ask permission on obvious fixes.

7. **No "I appreciate you taking the time to..."** — Josh doesn't write this. Ever. Cut all gratitude filler.

8. **No "Please don't hesitate to reach out"** — Corporate garbage. Josh says "Let me know" or "If any questions come up let me know."

9. **Sign-off is `-Josh` not `- Josh` not `Best, Josh`** — Dash directly against the name. Or `--Josh` for longer/formal emails. Or nothing for ultra-short replies.

10. **When Josh mentions a framework you don't know (Chris Voss, etc.) — search first, draft second.** Don't wing it.

11. **Don't write content that isn't yours to write.** Mar 18: Josh asked to send Ed (attorney) raw details about dashboard calculations. I wrote full legal disclaimer language instead of passing Josh's notes as-is. Ed writes the legal language — not me. When Josh is sending raw notes/details to a professional, pass them through. Don't rewrite them into polished drafts unless explicitly asked.

12. **Ask before expanding scope, don't selectively ask.** Mar 18: I ask permission on trivial things but took liberty writing legal disclaimers without asking. If the task is "send these details to Ed," do exactly that. Don't add two Google Doc tabs of legal language nobody asked for.

13. **Emails are short. Break it down.** Mar 18: Wrote a wall of text to Ed with dashboard methodology details. Should have been bullet points or a simple list. If the email has more than 2-3 short paragraphs, it's too long. Use line breaks and bullets to make it scannable.

## Adding Gotchas

When Josh corrects a draft, add the correction to this gotchas list immediately. Same turn, not later. Include the date and what specifically was wrong.

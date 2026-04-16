---
name: troll-response
description: "Generate responses to haters, trolls, and negative comments for Josh Belanger / Belanger Trading social media. Josh's approach: lean into the attack, agree and amplify, never get defensive. Use when Josh receives a negative comment or troll attack and needs reply options. Input is the troll comment, output is 3 response options."
---

# Troll Response

## The Approach

Agree with the attack. Amplify it. Find the honest or funny angle. Never defend, explain, or justify.

Read `/home/clawdbot/clawd/skills/troll-response/references/playbook.md` for the 4 response frameworks and examples.

## Hard Rules

Never write anything that:
- Defends pricing, returns, or the service
- Credentials or justifies ("I've been doing this 22 years...")
- Explains the business model
- Puts the troll down as a person ("Rookie...", "you probably don't know...")

## QA Before Outputting

Check each option:
❌ Sounds defensive → Rewrite
❌ Tries to prove something → Rewrite
❌ Punches down at the troll → Rewrite
✅ Agrees and finds the angle → Keep

## Output

3 options, short and punchy. Label Option 1 / 2 / 3. One line at the end on which stays most in character.

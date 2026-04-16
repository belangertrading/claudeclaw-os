# Operations Writing Process

## The Conceptual Mapping QA Method

**Why it exists:** Keyword searches miss ideas expressed in different words. A paragraph-by-paragraph conceptual check catches what keyword searches miss.

**How to run it:**
1. Open both the source notes and the output document side by side
2. For each bullet in the conceptual map, ask: "Is this idea expressed somewhere in the document?"
3. The wording doesn't need to match — the concept needs to be present
4. Mark ✅ found or ❌ missing
5. If >3 items missing → fix agent. If 1-2 → patch inline.

## Common Failure Modes (from Operations Manual history)

- **Sanitizing Josh's voice** — Agent rewrites colorful examples in bland language. Fix: instruct agent to use Josh's exact words
- **Losing specific details** — "3 drinks" becomes "some drinks", Austin/Tesla example gets genericized. Fix: conceptual map must include specifics, not just topics
- **Merging distinct ideas** — Two separate concepts collapse into one paragraph. Fix: map each idea separately before writing
- **Structural over-optimization** — Agent reorganizes sections in ways that make logical sense but lose Josh's mental model. Fix: use existing structure as template, not suggestion

## Document Structure (Operations Manual)

```
operations/operations-manual.md
├── What This Is
├── Section 1: Core Identity — Who Josh Is
├── Section 2: Competitive Positioning — The TJR Comparison
├── Section 3: The Content Approach — Market Commentary Through Confession
├── Section 4: Content Types — The Toolkit (Not Pillars)
├── Section 5: Lifestyle Content — When Personal Details Work
├── Section 6: The Business Model — Why Losses Sell Subscriptions
├── Section 7: Channel Strategy — Email vs. Social Media
├── Appendix A: Troll Response Playbook
├── Appendix B: Weekly Content Templates & Cadence
└── Appendix C: Tagline Options
```

## SOP Structure Template

```markdown
# [Process Name] SOP

**Purpose:** One sentence — what does this SOP accomplish?
**When to use:** Specific trigger conditions
**Owner:** Josh / Henry / Both

## Steps
1. Step with exact details
2. Step with exact details
...

## Quality Check
- [ ] Checklist item
- [ ] Checklist item

## Notes / Edge Cases
```

## File Naming Conventions

| Document type | Path |
|---|---|
| Operations Manual versions | `operations/brand-bible-v[N].md` |
| Josh's notes | `operations/belangers-notes.md` (append, don't overwrite) |
| Conceptual maps | `operations/mapping-[doc-name].md` (temp, delete after QA) |
| SOPs | `operations/sops/[kebab-case-name].md` |
| Skills from processes | `skills/[skill-name]/` |

# FOR_HENRY.md — X Co-Writer Skill

*Last updated: Jan 28, 2026*

## What This Is

A skill that helps generate X/Twitter content in Josh's voice — the "rich uncle who's been through it" persona developed with Charlie Light.

Think of it like having a ghostwriter who's memorized your voice, your stories, and your style. You give them the topic, they draft content that sounds like you.

## The Problem It Solves

Writing good X content takes time. And consistency is key — you need to sound like YOU, every time.

This skill captures:
- Josh's voice profile (tone, style, what to avoid)
- Reply templates that work
- A story bank to draw from
- Target accounts for engagement

Now when I draft content for Josh, it's already in his voice.

## How It Works

### The Voice Profile

`references/voice-profile.md` defines exactly how Josh sounds:

**Core identity:** "The rich uncle who's been through it"
- Direct, no BS
- Real and a little flawed
- Tells you the truth over a beer
- NOT flexing wealth
- 22 years of Wall Street stories to draw from

**Forbidden words:** leverage, optimize, utilize, robust, comprehensive

**Signature phrases:**
- "Here's what most people miss..."
- "When I was on the desk..."
- "I've seen this movie before"
- "That's not how it works"

### The Reply Formula

```
[HOOK - credentials/experience]
[STORY - specific example only Josh knows]
[INSIGHT - what this means / what people miss]
```

### The Templates

`templates/reply-templates.md` has ready-to-adapt structures:

1. **The Insider** — Share insider perspective
2. **The Historical Parallel** — Connect to past events
3. **The Contrarian** — Challenge consensus
4. **The Story** — Lead with a narrative
5. **The "Actually..."** — Add missing context

### The Story Bank

`references/story-bank.md` is where Josh's personal stories live.

This is the differentiator. No TikTok trader can fake 22 years of Wall Street experience. The more stories in the bank, the more unique content we can create.

**Story types that work:**
- Big wins (framed as lessons, not flexing)
- Big losses (builds credibility through vulnerability)
- Behind-the-scenes observations
- "I've seen this before" historical parallels

### Target Accounts

`references/target-accounts.md` lists accounts to engage with.

**Criteria:**
- 50k+ followers
- Finance/trading content
- Active comment sections
- Worth replying to (not just news headlines)

## File Structure

```
skills/x-cowriter/
├── SKILL.md                     # Skill definition (I read this)
├── FOR_HENRY.md                 # This file
├── references/
│   ├── voice-profile.md         # Josh's voice DNA
│   ├── target-accounts.md       # Who to engage with
│   └── story-bank.md            # Personal stories to draw from
└── templates/
    └── reply-templates.md       # Ready-to-adapt reply structures
```

## How to Use

### For Replies

1. I see a post worth replying to (or Josh points me to one)
2. I load the voice profile
3. I match a template to the situation
4. I draft a reply using Josh's stories/experience
5. Josh reviews, edits, posts

### For Original Posts

Same process, but I generate topic ideas based on:
- What's happening in markets
- Stories from the bank that haven't been used
- Parody/humor opportunities

## The Charlie Light Strategy

This skill implements what Josh learned from Charlie Light:

**Reply-first growth:**
- Engage with larger accounts (50k-100k followers)
- Use detailed, story-driven replies
- Let your experience differentiate you
- Drive profile visits → follower growth

**Not about volume — about quality:**
- 10-15 quality replies per week
- 2-3 original posts per week
- ~30 minutes per day

**The differentiator:**
Personal stories no one else can tell. Anyone can tweet about markets. Only Josh can say "In 2008, I watched my desk..."

## What Needs to Be Filled In

The skill structure is complete. What's needed:

1. **Story Bank** — Josh needs to add specific stories:
   - Market events he witnessed
   - Big trades (wins and losses)
   - Behind-the-scenes observations

2. **Target Accounts** — Research and add accounts to engage with

3. **Testing** — Use the templates on real posts and see what resonates

## Technical Decisions

### Why a Skill vs. Just Instructions?

- **Persistence** — The voice profile doesn't need to be re-explained every session
- **Structure** — Templates are ready to grab and adapt
- **Improvement** — Can iterate on what works over time
- **Separation** — X content is separate from trading alerts

### Why Markdown Files?

- Human-readable
- Version controlled
- Easy to edit
- No database needed

## Integration with Bird Skill

The `bird` skill handles actual X/Twitter operations (posting, reading, searching). This skill handles *what* to post. They work together:

1. `x-cowriter` drafts content
2. Josh approves
3. `bird` posts it

## Metrics to Track

Once active:
- Reply impressions
- Profile visits from replies
- Follower growth
- Best-performing story angles
- Which templates work best

---

*This skill captures Josh's voice. The more he uses it and adds to it, the better it gets.*

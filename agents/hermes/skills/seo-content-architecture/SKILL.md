---
name: seo-content-architecture
description: Research, analyze, and plan SEO content architecture for a website. Covers competitor analysis, URL structure decisions, SERP landscape mapping, and content pillar planning. Use when building a content strategy for a new site or pivoting an existing site's content approach.
tags: [seo, content-strategy, competitive-analysis, url-structure, topic-clusters]
triggers:
  - User asks about SEO strategy or content architecture for a website
  - User wants to model their site after competitors
  - User asks about URL structure decisions (/blog/ vs /topic/ vs flat)
  - User needs to plan content pillars and topic clusters
  - User wants to understand who ranks for target keywords and why
---

# SEO Content Architecture Research & Planning

## When to Use
- Planning content strategy for a new site or content pivot
- Deciding on URL structure before building out content
- Analyzing what competitors do well in SEO
- Mapping SERP landscape for target keywords
- Building a content pillar and topic cluster plan

## Phase 1: Parallel Research (3 Subagents)

Deploy 3 parallel subagents with `delegate_task` (all use `["web"]` toolset):

### Subagent 1: URL Structure Research
Research SEO implications of different URL structures. Key sources to check:
- Google Search Central documentation on URL structure
- John Mueller / Gary Illyes statements on URL paths and ranking
- Kevin Indig's analysis on /blog/ vs topical directories
- Ahrefs (Patrick Stox) on silo structures vs internal linking
- Moz on flat vs hierarchical architecture
- Case studies of URL restructuring (Conductor, OnCrawl, HubSpot)
- Real examples: NerdWallet, Investopedia, HubSpot URL patterns

Key questions to answer:
1. Does URL folder structure directly impact rankings? (No — confirmed by Google)
2. What are the indirect benefits? (CTR, breadcrumbs, UX, content organization)
3. What do top practitioners recommend? (Topic-based directories, not format-based)
4. Ranking of approaches: `/topic/article` > `/article` (flat) > `/learn/topic/article` > `/blog/article`

### Subagent 2: Competitor Site Analysis
Analyze 10-15 top sites in the target niche. For each site document:
- URL structure and content architecture
- How they organize education vs news vs tools vs strategies
- Topic cluster/pillar approach
- What makes their SEO work
- Scale (estimated page count, content types)
- Relevance to the user's situation (team size, resources, niche)

**For financial/trading niche specifically**, key sites to analyze:
- MarketBeat (programmatic SEO, bootstrapped to $25M/yr)
- Investopedia (dictionary/glossary model, 49M+ organic visitors)
- projectfinance.com (flat URLs, solo operator, deep strategy guides)
- Barchart (data tools + screeners, ranks #1 for many options terms)
- OptionAlpha (/learn/ + /strategies/ + /calculators/ hub model)
- Benzinga (news + education + tools hybrid)
- tastylive/tastytrade (/concepts-strategies/ education hub)
- Seeking Alpha (UGC model — different but informative)
- StockAnalysis.com (programmatic SEO, side project to 7M monthly)
- InsiderFinance (niche options flow/dark pool tool)
- CBOE Options Institute (authoritative education)

Rank sites by how well their model applies to a small team.

### Subagent 3: SERP Landscape for Target Keywords
For each target keyword/pillar topic:
- Who ranks in top 5-10 positions?
- What type of content ranks? (data tools, education, screeners, guides)
- What URL structure do ranking pages use?
- Content depth and format of top results
- Search intent (informational, transactional, tool-based)
- "People Also Ask" questions (map the full topic cluster)
- Related/long-tail keyword opportunities

## Phase 2: Synthesis

After subagent results return, synthesize into a single strategic brief:

### URL Structure Recommendation
- Present ranked options with pros/cons
- Show what top competitors use
- Make a clear recommendation based on the user's niche and scale

### Competitor Model Rankings
- Rank the 3-5 most relevant models for the user's situation
- Explain WHY each model works and what to take from it
- Be honest about what requires scale vs what a small team can replicate

### SERP Opportunity Analysis
- For each target keyword: who ranks, what type of content wins, gaps to exploit
- Identify the split between data/tool content and educational content
- Map out the topic cluster from PAA and related keywords

### Strategic Recommendations
1. Recommended URL structure with examples
2. Content pillar definitions
3. Priority order for content creation
4. Content types needed (education, tools, data pages, guides)
5. Internal linking strategy principles

## Key Findings to Remember

### URL Structure Truth
- **Google confirmed**: URL folder path is NOT a ranking factor (John Mueller, Gary Illyes)
- **But matters indirectly**: CTR, breadcrumbs in SERPs, content organization discipline, UX
- **`/blog/` is worst**: Signals content format, not topic. Kevin Indig (ex-Shopify SEO) specifically argues against it
- **`/topic/article` is best**: `/options/covered-calls` > `/learn/covered-calls` > `/blog/covered-calls`
- **Internal linking matters MORE than URL structure** for topical authority (Patrick Stox, Ahrefs)

### What Actually Drives Topical Authority
1. **Comprehensive content coverage** — no gaps in the topic
2. **Dense internal linking** — every related page links to related pages
3. **Descriptive anchor text** — tells Google what target pages are about
4. **Content depth** — long-form, genuinely useful content
5. **Consistent publishing** — topical authority compounds over time
6. **E-E-A-T signals** — author expertise, real credentials, original research

### Financial/Trading Niche Insights
- Top results for "unusual options activity" are split: **live data screeners** vs **educational definitions**
- MarketBeat is the best model for bootstrapped financial media (programmatic SEO + editorial)
- projectfinance.com proves solo operators can rank against giants with depth-over-breadth
- Free tools/calculators earn backlinks and capture tool-intent searches
- Programmatic SEO (auto-generated ticker pages) is a massive traffic lever in finance

## Pitfalls
- **Don't let URL structure paralyze you** — content quality and internal linking matter 10x more
- **Subagent file artifacts don't persist** — the research files subagents create live in isolated sessions. Rely on the summary data returned, not file paths
- **Don't try to be Investopedia** — they have hundreds of writers. Focus on depth in your specific niche
- **HarborSEO and similar AI-SEO tools** are middlemen — an AI agent can do the same work directly (research, write, optimize) without the $49-399/mo overhead
- **Case studies about URL restructuring** always have confounding variables (they also fix internal linking, improve content, etc.) — isolating URL structure impact alone is nearly impossible

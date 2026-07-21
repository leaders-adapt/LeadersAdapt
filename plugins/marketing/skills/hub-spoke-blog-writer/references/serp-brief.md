# SERP and Fan-Out Brief (Phase 2, per page)

Every page gets a brief BEFORE it is written. Writing to beat a SERP you have studied outperforms retrofitting an edge in revision, and it catches unwinnable pages before you spend the words. The brief also produces the three inputs the checker needs: the length band, the entity set, and the fan-out questions.

Save each brief as `serp-briefs/NN-slug-brief.md`. A page without a brief cannot be written, and its Competitive Edge metric caps at 8.

## How to build one (10 to 15 minutes per page)

1. Search the primary keyword (and its closest variant) with web search. Look at the top 10 plus every SERP feature.
2. Record what actually ranks: page types (guide, listicle, comparison, tool, product page, forum), who owns them (category-defining brands or beatable sites), content depth and recency.
3. Record the answer surfaces: is there a featured snippet, and in what format (paragraph, list, table)? Is there an AI Overview, and what does it cite? Which People Also Ask questions appear?
4. Enumerate the fan-out set: the sub-questions an AI engine would decompose this query into. Sources: PAA, autocomplete, the H2s of the top 3 results, plus the predictable follow-ups (cost, comparison, how-to, examples, risks, alternatives). Aim for 6 to 12 questions.
5. List the entity set: the concepts, named frameworks, tools, and terms the top results consistently cover. The post must cover these to be competitive, and the checker verifies coverage.
6. Name the information-gain gap: what does NO incumbent have that this business can supply? A first-party number, a named framework, an operator story, an original comparison. This becomes the post's citable asset.
7. Make the winnability call, honestly: winnable now, winnable with links, long-tail only, or unwinnable (category-defining brands own every slot). Unwinnable pages get rescoped to a longer-tail angle or cut.
8. Set the length band from the SERP norm, not from habit: match or slightly exceed the depth of what wins, never pad past it. A definitional query won by 1,200-word pages does not need 3,000 words; bloat dilutes extractability.
9. Choose the angle: the one-line statement of how this page beats the SERP (deeper, more first-hand, more current, better format, the missing perspective).

## Brief template

```markdown
# SERP Brief: [primary keyword]

date: YYYY-MM-DD
page: NN-slug
volume / KD: [from tool or est.]

## What ranks now
| # | URL | Type | Angle | Beatable? |
|---|-----|------|-------|-----------|

## Answer surfaces
- Featured snippet: [none / paragraph / list / table] held by [URL]
- AI Overview: [present? what it cites]
- Quick Answer target format: [match the winning format]

## Fan-out questions (map each to an H2 or FAQ item)
1.
2.
(6 to 12 total)

## Entity set (the post must cover these; feeds --entities)
term1, term2, term3, ...

## Information-gain gap (the citable asset this post will own)
[what no incumbent has, and which evidence-bank item supplies it]

## Winnability: [winnable now / with links / long-tail only / unwinnable]
## Length band: [min] to [max] words (feeds --min-words / --max-words)
## Intent: [informational / commercial / comparison / transactional]
## Angle (one line):
```

## Rules

- Never skip the winnability call. An honest "unwinnable, rescope" saves a week of wasted work.
- The Quick Answer block format must match the SERP's winning answer format (paragraph vs list vs table).
- The fan-out list is a coverage contract: every question maps to an H2 or FAQ item INSIDE the page. Never spin out a separate page per fan-out variation; that is scaled content abuse under Google's spam policy and the brief must never propose it.
- Commercial and recommendation queries: AI engines preferentially extract from pages that already contain a ranked list. If the SERP or AI answer for a commercial cluster is list-shaped, plan one honest ranked-list page (or a ranked-list section on the hub) for that cluster.
- Re-run the brief in Mode D refreshes; SERPs move, and the diff drives the update.

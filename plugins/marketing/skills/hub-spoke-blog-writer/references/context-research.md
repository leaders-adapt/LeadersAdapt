# Context Research (Phase 0.5) (v2)

This phase runs before intake and before writing. Its job is to gather and synthesize real evidence about the company and the specific person whose name goes on the post, so the writing carries genuine first-hand experience, authority, and voice. Without it, every post defaults to competent-but-generic, which E-E-A-T signals, AI answer engines, and skeptical readers all punish.

The rule: a blog post is only as credible as the real material behind it. In v2 this phase also feeds the information-gain requirement; the evidence bank is where citable assets come from.

## Why this phase exists

1. Experience. Real first-hand moments cannot be invented without lying. They come from transcripts, past posts, case notes.
2. Authority. Named credentials, a real author entity, owned frameworks, real citations.
3. Voice. Not three adjectives: the person's actual rhythm, signature phrases, hard avoids. Needs samples.
4. Information gain (v2). The first-party numbers and named frameworks that make passages citable by AI engines come from here, not from writing harder.

## Step 1: Offer the connection menu

Tell the user plainly: the more real material you point me at, the higher the E-E-A-T, the closer the voice, and the more citable the posts. Offer the menu, multiple-choice where supported, in rough order of value:

1. Strategy and positioning documents (Drive, Box, Notion, this project's folders). Richest single source.
2. The author's own writing: past posts, LinkedIn, a book, newsletters. Five to ten samples fingerprints a voice.
3. Meeting and call transcripts (Otter is the default). Spoken voice, real stories, real objections, real client outcomes. Client material is anonymized unless permission is confirmed.
4. Other Cowork or chat projects on the same business.
5. CRM, email, and chat: the audience's own words for their pain.
6. SEO tools and existing site content: Semrush, Ahrefs, GSC, a crawl or export. Real keyword data plus the cannibalization map. Also pull the site's AI-citation baseline if the tool shows it (Semrush AI mentions), so post-publish tracking has a starting number.
7. Analytics (GA4): what already converts.

If they can connect only one thing: the strategy folder or transcripts. If nothing: say clearly that E-E-A-T, voice, and information gain will be capped, run the standard interview, and flag it in the readiness gate.

## Step 2: Ingest and synthesize into four artifacts

Do not dump raw content into posts. Synthesize.

### Artifact A: author-voice-profile.md

```markdown
# Author Voice Profile: [Name]

last_updated: YYYY-MM-DD
sources: [docs, transcripts, posts this was built from]

## Author entity (for E-E-A-T and Person schema)
- Full name and title:
- Credentials that matter: [built X, sold Y, wrote book W]
- Bio line (one sentence, reusable as the byline credential):
- Author page URL on the site:
- Links for sameAs: [LinkedIn, book page, Wikidata if it exists, Crunchbase]

## Voice fingerprint
- Sentence rhythm: [evidenced pattern]
- Signature phrases and constructions: [recurring lines, quoted]
- Vocabulary they reach for:
- Words and patterns they never use: [hard avoids, on top of the global banned list]
- Rhetorical moves: [e.g. opens on a scene, ends on a reframe]
- Formality and stance:

## Quotable lines (verbatim)
Five to ten real lines that could drop into a post as-is.

## Stories bank (real Experience)
Real first-hand moments, one or two lines each, tagged by theme. Mark each
[public], [client-anonymized], or [needs permission]. Never invent these.
- [theme]: "..."

## Do-not-claim list
Anything that sounds like a credential the user has not confirmed.
```

The fingerprint must be evidenced by quotes, not adjectives. Adjectives only means low-confidence voice in the readiness gate.

### Artifact B: evidence-bank.md

```markdown
# Evidence Bank: [Company]

last_updated: YYYY-MM-DD

## Verified external statistics
- [stat] - [source, year, url]

## The company's own data (user-confirmed)
Real client results and metrics, confirmed true and shareable.
- [metric] - [context] - [public / anonymized / needs permission]

## Citable assets (v2: the information-gain inventory)
The unique things posts can own that no competitor has:
- First-party aggregate data: [e.g. "of N assessments run, X% showed..."; note method]
- Owned frameworks with one-sentence definitions: [name: definition]
- Original comparisons the business is uniquely placed to make:
- Operator stories with numbers: [pointer into the stories bank]

## Proof assets
Case studies, named logos, the book, original research, testimonials.
```

Rule: a statistic enters a post only from this bank with a real source, or as user-confirmed company data. The citable-asset inventory is what Phase 3 draws on to satisfy the information-gain requirement; if it is empty, say so and tell the user what data would fill it (aggregating their own assessment or client data is usually the fastest win).

### Artifact C: existing-content-map.md

```markdown
# Existing Content Map: [domain]

last_updated: YYYY-MM-DD
source: [Semrush export, GSC, crawl, sitemap]

## Pages already ranking (do not compete with these)
| URL | Primary term it ranks for | Position | Note |
|-----|---------------------------|----------|------|

## Cannibalization risks for the planned cluster
Planned keyword vs existing page collisions. Verdict each: consolidate,
redirect, differentiate, or optimize the existing page. Flag before writing.

## Internal link targets that already exist
Real URLs the new posts should link to, with suggested anchors.

## Gaps the cluster should own

## AI-citation baseline (if available)
Current AI mentions / cited pages for the domain, by engine, with date.
```

Not optional for an established site. Writing blind into an existing footprint creates self-competition.

### Artifact D: enrich business-profile.md

Fold everything into the profile (format in `intake-guide.md`), each section citing a real source. Unconfirmed stays "unknown", never invented.

## Step 3: The readiness gate

Score the context and show the user. Five dimensions, High / Medium / Low with a one-line reason:

1. Experience evidence: real first-hand stories in the bank?
2. Authority signals: confirmed credentials, author entity, owned frameworks?
3. Voice fidelity: real samples, or only adjectives?
4. Audience language: their pain in their words, or guesses?
5. Existing-content awareness: do we know what ranks?

Verdict and consequence:
- Mostly High: proceed; a 9-plus E-E-A-T outcome is realistic.
- Several Low: name the one or two connections that would raise it most, let the user choose. Proceeding thin caps the E-E-A-T metric and (if the citable-asset inventory is empty) the Information Gain metric, and the scorecards say why.

Never hide a thin context base behind a confident draft.

## How later phases use these artifacts

- Phase 1 intake shrinks to the gaps.
- Phase 2 uses the content map for gap selection, collision verdicts, and real link targets; SERP briefs name which evidence-bank asset each page will own.
- Phase 3 pulls voice from the profile, stories from the bank, stats only from the evidence bank, and the citable asset per post from the inventory.
- Phase 4 caps E-E-A-T by the readiness gate and Information Gain by the inventory.

## When the user has nothing to connect

A valid path, not a failure. Standard interview, dimensions marked Low, honest scene-based hooks, no borrowed authority, and a one-time note on what connecting real material later would unlock. Never compensate for missing evidence by inventing it.

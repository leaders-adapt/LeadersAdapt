# GEO and Citability (read before writing; schema templates included)

This file governs how posts win AI-answer citations, not just rankings. Mid-2026 reality, confirmed by Google's official generative AI optimization guide (July 2026): AI answer surfaces work by retrieval-augmented generation (grounding on ranked, indexed pages) plus query fan-out (the model issues concurrent related sub-queries and synthesizes across the results). ChatGPT search, Perplexity, Gemini, and Claude behave similarly. Engines preferentially quote passages that are neutral, attributed, self-contained, and that ADD something the rest of the corpus does not have. Google's own framing: unique, non-commodity, people-first content wins; commodity content ("7 tips for X") that anyone could have written gets skipped.

## The five things that earn citations

1. Crawlability and indexability. The page must serve full content to a no-JS fetch (most citation crawlers do not execute JavaScript) and be indexed and snippet-eligible in Google (a page not eligible for a snippet is not eligible for AI Overviews or AI Mode). Confirm both at delivery.
2. Extractability. Self-contained chunks an engine can lift without surrounding context: the Quick Answer block, definition callouts, 40 to 90 word FAQ answers, comparison tables, numbered lists. Definition-first openings measurably lift retrieval.
3. Information gain. A passage that says what everyone else says gets skipped in favor of the higher-authority version of the same sentence. A passage with a first-party number, a named framework, a quotable expert line, or an operator observation gets cited because it exists nowhere else. Every post ships at least one. Published GEO research (Princeton and Allen Institute) found the strongest single lifts to AI-answer visibility were adding quotations (about +28%), statistics (about +26%), and source citations (about +25%).
4. Entity clarity. The engine must know who wrote this and why they are credible: a real author entity with the credential in the byline, schema that links author, organization, and framework definitions with stable @ids, and consistent naming across the site. Off-site corroboration (independent mentions, profiles, Wikidata) multiplies it.
5. Freshness. AI answers have a strong recency bias; Google AI Overviews mostly cite sources published or updated within the past six months, and third-party tracking shows citations decay sharply after about three months. GEO-priority pages get a real content refresh (not a fake dateModified bump) every 3 to 6 months.

## What NOT to do (Google's own myth-busting, July 2026)

- Do not create a page per fan-out variation. Cover the fan-out set INSIDE the page via H2s and FAQ. Spinning out thin pages for every query variation is scaled content abuse by Google's spam policy and an ineffective strategy anyway.
- Do not chunk content artificially or write "for AI." Write for the reader; engines understand synonyms and multi-topic pages.
- Do not chase inauthentic mentions. Earned, independent mentions help; manufactured ones do not.
- Do not overweight llms.txt (see below) or invent special AI markup. There is none.

## Zoned writing (the core discipline)

Answer zones are neutral. Persuasion zones persuade. Mixing them costs citations, because engines avoid quoting salesy passages.

Answer zones (clinical, attributed, zero persuasion language):
- The Quick Answer block.
- Definition callouts.
- Stat blocks and their source attributions.
- The FAQ section, every answer.
- Comparison and summary tables.

Persuasion zones (where the 12 psychology principles live):
- The opening hook and narrative body.
- First-hand stories and case examples.
- The conclusion and the CTA section.

Test for an answer zone passage: could a rival publication quote it verbatim with attribution and not look like they ran your ad? If not, rewrite it flat.

## The citable-asset requirement (information gain)

Each post carries at least one of, sourced from `evidence-bank.md`:
- A first-party statistic ("across N assessments we ran, X% of CEOs...") with enough method context to be quotable.
- A named framework with a one-sentence crawlable definition (and a DefinedTerm schema entry).
- An original comparison table that does not exist elsewhere.
- A named or anonymized operator story with a concrete number and outcome.
- A quotable line from a named practitioner (the author or a real, permissioned client), formatted as an attributed quotation. Quotations are the single strongest measured lift to AI-answer visibility.

If the evidence bank has nothing to supply, the post's Information Gain metric caps at 7 and the scorecard says what data to collect. Do not fabricate the asset.

## Format rules for extractable blocks

- Quick Answer: 40 to 70 words, directly answers the primary query, starts with a bolded answer-first sentence, format matched to the SERP's winning snippet format (paragraph, list, or table). No brand pitch inside it.
- Definition callout: one bolded sentence of the form "[Term] is [definition]." placed near first use of the core concept. At least one per post.
- FAQ: 5 or 6 questions phrased the way people search, each answer 40 to 90 words and standalone.
- Stat blocks: number, context, source with year, link. Never a number without a source.
- Hubs additionally carry one comparison table summarizing the cluster's subject.

## Schema: emit it, do not describe it

Honest framing first: Google states structured data is NOT required for its generative AI features. We emit it anyway because it is cheap, it keeps rich-result eligibility, and it is the cleanest way to declare the author entity, credentials, and framework definitions unambiguously for every engine. Never emit schema for content the page does not visibly contain.

Every post ships `schema/NN-slug-schema.json`, ready to paste into the CMS schema field or a script tag. Conventions:

- Stable @ids, defined once site-wide and referenced everywhere: `https://<domain>/#organization`, `https://<domain>/#author`, and `https://<domain>/glossary#<term>` for DefinedTerms.
- The author Person carries the credential and sameAs links (LinkedIn, book page, Wikidata when it exists). This is the E-E-A-T entity spine; every Article references it.

Template (adapt per post; FAQPage mainEntity MUST mirror the post's FAQ exactly):

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "@id": "https://DOMAIN/SLUG/#article",
      "headline": "TITLE TAG TEXT",
      "description": "META DESCRIPTION TEXT",
      "url": "https://DOMAIN/SLUG/",
      "datePublished": "YYYY-MM-DD",
      "dateModified": "YYYY-MM-DD",
      "author": { "@id": "https://DOMAIN/#author" },
      "publisher": { "@id": "https://DOMAIN/#organization" },
      "about": [ { "@id": "https://DOMAIN/glossary#FRAMEWORK" } ]
    },
    {
      "@type": "Person",
      "@id": "https://DOMAIN/#author",
      "name": "AUTHOR NAME",
      "description": "ONE-LINE CREDENTIAL FROM THE VOICE PROFILE",
      "url": "https://DOMAIN/AUTHOR-PAGE/",
      "sameAs": [ "LINKEDIN URL", "BOOK URL" ],
      "knowsAbout": [ "TOPIC 1", "TOPIC 2" ]
    },
    {
      "@type": "Organization",
      "@id": "https://DOMAIN/#organization",
      "name": "COMPANY",
      "url": "https://DOMAIN/"
    },
    {
      "@type": "FAQPage",
      "@id": "https://DOMAIN/SLUG/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "FAQ QUESTION 1",
          "acceptedAnswer": { "@type": "Answer", "text": "THE EXACT ANSWER TEXT" }
        }
      ]
    },
    {
      "@type": "DefinedTerm",
      "@id": "https://DOMAIN/glossary#FRAMEWORK",
      "name": "FRAMEWORK NAME",
      "description": "THE ONE-SENTENCE CRAWLABLE DEFINITION",
      "inDefinedTermSet": "https://DOMAIN/glossary"
    }
  ]
}
```

Include the DefinedTerm node only when the post introduces or centers a named framework. Add a HowTo node only for true step-by-step posts. Never emit schema for content the page does not visibly contain; mismatched schema is a trust penalty.

## Fan-out coverage

The SERP brief's 6 to 12 sub-questions are a contract: each maps to an H2 or an FAQ item INSIDE the page. The checker takes them via `--questions` and reports coverage. A post covering the full decomposition gets pulled into multi-part AI answers; a post answering only the head query gets one shot at one citation. This is Google's own described mechanism (query fan-out), and covering it within one strong page is the compliant version; one page per variation is the spam version.

## llms.txt: honest status (mid-2026)

Google Search officially ignores llms.txt, and independent crawl monitoring shows the major AI citation crawlers almost never fetch it either; its real users today are IDE and documentation agents. Verdict: maintain one only if it is cheap and keep it accurate (a wrong llms.txt is worse than none), but never count it as a citation lever, and never prioritize it over content, entities, or crawlability. The skill treats it as optional hygiene at delivery.

## After publish: track citations, not just ranks

Three layers, logged monthly in the cluster map tracking table:
1. Search Console's Generative AI performance report, the official measure of impressions and clicks from Google's AI features. This is the primary Google-side number.
2. Semrush AI mentions (or equivalent) for cited pages per engine.
3. The fixed prompt panel across ChatGPT, Perplexity, AI Overviews, Gemini, and Claude. The KPI is reference rate: the share of panel responses that mention or cite the brand.
Feed the pattern back: the block formats and assets that earn citations are the ones the next wave doubles down on.

## Refresh triggers (Mode D)

- GEO-priority pages (citation targets, AI-answer battlegrounds): real refresh every 3 to 6 months; recency bias makes stale pages fall out of AI answers even while blue-link ranks hold.
- Year-modified queries: refresh annually at minimum, update the year in title and content.
- Any post at 12 months, or on a 20%+ traffic decline, or when its SERP gains an AI Overview it is not cited in.
- Re-run the SERP brief first; the diff drives the update. Keep the URL stable. Refreshes must change real content; bumping dateModified without changes is a trust risk.

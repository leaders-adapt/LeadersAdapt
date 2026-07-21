# Business Intake Guide (v2)

The goal: collect exactly enough to write posts that sell a specific product to a specific person, then never ask again. Everything lands in `business-profile.md`. After Phase 0.5, most answers are already synthesized with sources; ask only the gaps.

## Step 1: Prefill from the website

Ask for the company URL first. Fetch the homepage, about page, and product or pricing pages. Draft answers for: what the company does, who it serves, products and prices, founder story, proof assets, apparent voice. Present the draft for correction. Confirming takes 2 minutes; answering 12 open questions takes 20.

While fetching, also note two technical facts: does the site serve full content to a no-JS fetch (citation crawlers need this), and does an llms.txt exist. Record both in the profile's SEO context.

## Step 2: The interview (two rounds maximum)

Round 1, identity and offer:
1. Company name and URL.
2. What do you sell? For each offer: name, price, whether the price is PUBLIC (this controls whether the CTA shows it), components, and which one blog readers should buy first.
3. Who exactly is the reader? Role, company stage, situation.
4. Founder or author: name plus the one or two credibility facts that matter, and the URL of the author page on the site (needed for the Person schema @id; if none exists, recommend creating one and note it).

Round 2, positioning and conversion:
5. Top 3 pain points in the audience's own words.
6. What makes you different from the obvious alternatives? Press for specifics.
7. Proof assets: case studies, client results, a book, original research, notable logos. Only real things.
8. Primary conversion goal and secondary goal (newsletter, application, call, assessment).
9. Brand voice: 3 adjectives plus one example they love, plus hard rules. (The voice profile from Phase 0.5 outranks this when it exists.)
10. Publishing stack: CMS and SEO plugin, whether the CMS can inject custom JSON-LD (most SEO plugins can), existing posts worth linking, keyword data source, domain authority if known, cadence.

Skip anything the prefill or Phase 0.5 already answered. Gaps get marked "unknown", never invented.

## Step 3: Write business-profile.md

```markdown
# Business Profile: [Company]

last_updated: YYYY-MM-DD

## Company
- Name:
- URL:
- What it does (one sentence):

## Founder / Author
- Name:
- Credibility facts:
- Author page URL (for Person schema):

## Offer
- Primary product: [name, price, price public? yes/no, components, who for]
- Secondary offer: [name, price, price public? yes/no]
- Free tools: [assessments, quizzes, lead magnets and their URLs]
- Other proof assets:

## Audience
- Who:
- Situation:
- Top pain points (their words):
  1.
  2.
  3.

## Positioning
- Different because:
- Tone of competitors:

## Conversion
- Primary goal:
- Secondary goal:
- CTA target URLs: [product, call, assessment, newsletter]

## Voice
- Adjectives:
- Example or reference:
- Hard rules:

## SEO context
- Domain authority (if known):
- Keyword data source:
- Existing content worth linking:
- CMS and SEO plugin:
- CMS can inject JSON-LD: yes/no
- Server-rendered to no-JS fetch: yes/no
- llms.txt present: yes/no
- Publishing cadence:
```

Confirm the finished profile in a short summary before Phase 2.

## Updating a profile

When a returning user corrects anything, edit the file and bump `last_updated`. The profile is the single source of truth.

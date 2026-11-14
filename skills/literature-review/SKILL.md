---
name: literature-review
description: Retrieve, screen, verify, and organize a substantial scholarly corpus using web search, citation-graph expansion, and evidence mapping. Use for broad or multi-topic literature discovery, coverage analysis, source-grounded answers, and verified evidence packets; use literature-fast for a bounded reading list and doc-literature to turn an authorized corpus into a durable document.
license: Apache-2.0
metadata:
  third_party:
    - kind: service
      name: Crossref
      info_url: https://www.crossref.org/documentation/retrieve-metadata/
      privacy_url: https://www.crossref.org/operations-and-sustainability/privacy/
    - kind: service
      name: OpenAlex
      terms_url: https://openalex.org/OpenAlex_termsofservice.pdf
      privacy_url: https://openalex.org/OpenAlex_privacy_policy.pdf
---

# Literature Review

Retrieve and verify the literature needed for a research decision. The output is an evidence packet or a source-grounded answer, not a polished literature-review document. Use `$doc-literature` after the corpus is authorized and ready for structured synthesis.

This skill contains a hardened cross-agent port of an AcademicForge community copy, not verified Anthropic production source. See the [provenance and local modifications](references/provenance.md) and [Apache License 2.0](LICENSE).

## Boundary

- Own discovery, screening, version resolution, citation expansion, source verification, and coverage analysis.
- Do not choose manuscript voice, rewrite project prose, or impose a literature-document template.
- Do not turn a candidate list into a final related-work section. Hand an authorized corpus and evidence packet to `$doc-literature`.
- Use `$literature-fast` when 3-6 focused queries and approximately 5-10 prioritized papers are sufficient.

## Frame the review

Establish the research question, intended decision, terminology, date and source limits, inclusion/exclusion rules, known seeds, desired corpus size, and time budget. Ask only when a missing choice would materially change retrieval; otherwise proceed with labeled assumptions.

Use the narrowest adequate mode:

- **Broad retrieval:** discover and rank a substantial corpus.
- **Evidence map:** compare an approved or user-provided corpus through atomic claims and locators.
- **Evidence packet:** package verified sources, comparisons, contradictions, and gaps for later writing.
- **Systematic evidence collection:** use this label only with an explicit protocol, suitable database coverage, screening log, and coverage audit.

For large evidence maps or protocol-led collection, read [references/advanced-review.md](references/advanced-review.md).

## Delegate independent lanes

When at least three substantial and mostly independent topic, method, evidence, venue, or time-period lanes exist, use the environment's subagent mechanism and synthesize coverage centrally. Keep narrow or strongly dependent work with the lead agent.

Before delegation, read [references/subagent-review.md](references/subagent-review.md). Workers search and report; the lead resolves versions, deduplicates, records missing lanes, checks load-bearing claims, and assembles the final evidence packet.

## Deterministic helpers

`kernel.py` provides deterministic standard-library helpers; the active model performs the scientific reasoning. Load only the installed local file:

```python
exec(open("<this skill's directory>/kernel.py").read())
```

Available helpers include `verify_dois`, `crossref_lookup`, `search_openalex`, `expand_citations`, and `extract_dois`.

- `OPENALEX_API_KEY` is required for OpenAlex search and citation expansion. Keep it out of chat, files, logs, displayed URLs, and artifacts.
- `HOST_USER_EMAIL` is optional contact information for Crossref and doi.org. It is never sent to OpenAlex.
- Compare Crossref candidates by title, authors, year, venue, and version before verifying a DOI. Never accept the first result automatically.

## Retrieve and expand

1. Search the web and field-appropriate primary sources with multiple phrasings and terminology variants.
2. Use Crossref or OpenAlex metadata to resolve identifiers and versions, not to establish scientific claims.
3. For the two or three strongest seeds, inspect one backward and one forward citation step when this can materially improve recall.
4. Search directly for conflicting, negative, replication, retraction, and null-result evidence when relevant.
5. Deduplicate DOI, arXiv, accepted-manuscript, and published-version lineages before counting studies.

Recall can frame a query; retrieved primary evidence determines the claims. Search snippets, generated summaries, abstracts, reviews, and repository code are routing aids, not proof of a theorem, mechanism, experimental result, or novelty claim.

## Evidence and corpus states

Assign every source one evidence status:

- `DISCOVERED`: metadata or search result only;
- `ABSTRACT_ONLY`: title and abstract inspected;
- `PARTIAL_TEXT`: named sections, pages, tables, figures, or appendices inspected;
- `FULL_TEXT_VERIFIED`: the source text needed for every reported substantive claim was checked.

Keep corpus states separate:

- `candidate`: discovered but not screened;
- `screened`: assessed against the review criteria;
- `approved`: authorized for synthesis;
- `cited`: supports a specific claim with a locator.

For load-bearing claims, record page, section, theorem, table, figure, or appendix locators when available. Do not silently upgrade an evidence level.

## Evidence packet

Return or save, as requested:

1. review question, scope, cutoff, sources searched, and stopping rule;
2. search log with representative queries and coverage gaps;
3. deduplicated source records with stable identifiers and version lineage;
4. taxonomy, where it helps answer the review question, with a stated axis and source evidence for each mechanism. Use the [classification procedure](../explain-literature/SKILL.md#build-a-taxonomy-before-assigning-papers) when synthesizing categories;
5. claim-evidence entries with evidence status and locators;
6. comparable assumptions, targets, guarantees, experiments, and costs;
7. contradictions, negative results, unresolved interpretations, and blind spots;
8. approved corpus and a short handoff for `$doc-literature`.

An evidence packet may include a concise source-grounded answer, but it must not pretend to be a finished manuscript section. Preserve disagreements rather than merging them by majority vote.

## Stopping and safety

- Stop at the agreed paper/time budget or when new queries mostly duplicate known sources.
- Never claim global novelty, completeness, or absence from a failed search.
- Do not fabricate metadata, identifiers, results, or source access.
- Do not upload private or licensed PDFs or write to Zotero or another external system without separate authorization.

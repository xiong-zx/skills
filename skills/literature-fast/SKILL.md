---
name: literature-fast
description: Rapid web-first scholarly discovery and triage. Use for a bounded reading list, a small related-work scan, or a first-pass map before reading; use literature-review for citation-graph expansion and a verified evidence packet, and doc-literature for a durable literature document.
---

# Literature Scan

Find the small set of papers the user should inspect next. Optimize for speed, traceability, and useful prioritization rather than completeness or review prose.

## Boundary

- Search the web first. Use Zotero only when the user explicitly asks for it.
- Keep the scope bounded: normally 3-6 focused queries and 5-10 prioritized papers.
- Do not require Python helpers, API keys, a saved artifact, or a formal protocol.
- Never call this systematic, exhaustive, or proof of novelty.
- For citation-network expansion, a large corpus, or several substantial topics, use `$literature-review`. For a manuscript section or formal report from verified sources, use `$doc-literature`.

## Search

State the interpreted question and any material scope assumption in one or two sentences, then search primary paper pages, official preprints, proceedings, journal pages, and author or project pages. Use more than one phrasing when terminology varies.

Deduplicate DOI, arXiv, accepted-manuscript, and published versions. Prefer the final published version while retaining a useful preprint link when access is better.

Search snippets and secondary summaries are discovery aids, not evidence for detailed scientific claims.

## Evidence labels

Assign one status to each paper:

- `DISCOVERED`: metadata or search result only;
- `ABSTRACT_ONLY`: title and abstract inspected;
- `PARTIAL_TEXT`: named sections, pages, tables, figures, or appendices inspected;
- `FULL_TEXT_VERIFIED`: the source text needed for every reported substantive claim was checked.

Do not infer methods, results, theorems, or novelty beyond the status actually reached.

## Output

Return:

1. the scope and search boundary;
2. a compact theme map;
3. 5-10 prioritized papers with stable links, relevance, evidence status, and what to read first;
4. contradictions or obvious coverage gaps;
5. the single next search that would most reduce uncertainty.

Keep the answer inline unless the user requests a file. Stop when the paper budget is reached or new searches mostly repeat known items.

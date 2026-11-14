---
name: doc-literature
description: Turn an authorized, verified source corpus into a structured and well-written literature-review document, related-work section, application review, or method comparison. Own document scope, synthesis architecture, unified notation, formula-first comparison, claim-evidence placement, citation layout, and literature-specific academic prose; use literature-review when sources still need discovery or verification.
---

# Literature Document

Build the document contract, source-backed structure, and literature-specific prose for a synthesis. This skill decides what the artifact must contain and how its evidence, notation, formulas, comparisons, citations, and conclusions are expressed. It does not own literature retrieval.

## Inputs and boundary

Start from an authorized corpus or evidence packet with source identifiers, evidence levels, and locators. If the corpus is missing or materially incomplete, use `$literature-fast` or `$literature-review` before drafting.

- When `$writing-research` is explicitly combined with this skill, use it as the general academic-writing baseline; this skill's synthesis, evidence, citation, and literature-prose rules override any conflicting general rule.
- Own document scope, required sections, comparison axes, notation, tables, formula placement, claim-evidence structure, citation placement, academic voice, and output format.
- Do not enlarge the corpus, infer missing source claims, or call search snippets verified evidence.
- Write natural academic prose appropriate to literature synthesis while preserving the author's established voice and project terminology.
- Preserve an existing document's class, macros, bibliography system, section hierarchy, and authorized scientific claims unless the user requests a structural change.

## Select the document contract

Identify the intended artifact before drafting:

- literature-review report;
- related-work or background section;
- method-family comparison;
- application review;
- evidence-based research-positioning note.

Record the audience, research question, approved corpus, retrieval cutoff, expected length, citation style, output format, and decision the document should support. Do not silently turn an evidence packet into a systematic-review claim.

For a new substantial report or mathematically sensitive comparison, read [references/literature-document-contract.md](references/literature-document-contract.md). For decision-dependent stochastic optimization, performative prediction, or closely related topics, read [references/decision-dependent-opt.md](references/decision-dependent-opt.md) only when relevant.

## Build the structure

Use the smallest structure that carries the argument. A substantial report usually needs these functions, with headings adapted to the project:

1. main conclusions and scope;
2. unified setting and notation;
3. literature organized by research question or method family;
4. comparable targets, information assumptions, constructions, and guarantees;
5. empirical or computational evidence where relevant;
6. limitations, contradictions, and evidence gaps;
7. relevance to the user's current research.

A short related-work section may compress these functions into a few paragraphs. Do not force report-scale headings into a manuscript subsection.

When the document uses categories, apply the [classification procedure](../explain-literature/SKILL.md#build-a-taxonomy-before-assigning-papers). Use one category per top-level row or subsection, with representative papers as evidence and explicit labels for hybrid methods.

## Organize comparable evidence

Map each source into a shared comparison schema:

- research target or estimand;
- data, information, oracle, or intervention assumptions;
- mathematical objective or core construction;
- guarantee or evaluation criterion;
- statistical, computational, and constraint assumptions;
- datasets, baselines, metrics, and experimental protocol;
- evidence level and exact locator;
- relevance, limitation, and unresolved uncertainty.

Use a table only when rows and columns contain comparable objects. Do not put incommensurate metrics, datasets, or guarantee regimes in one apparent ranking.

## Use formula-first organization

When mathematics affects the comparison:

1. define the shared objects and symbol types;
2. state the load-bearing objective, estimator, update, theorem, or metric;
3. map paper-specific notation into the shared notation;
4. state assumptions and the exact guarantee or reported result;
5. explain how the methods differ and why the difference matters.

Use `$doc-math` when new definitions, proofs, derivations, or formal statements must be developed rather than merely organized.

## Place evidence and citations

- Put each citation next to the claim it supports.
- Preserve the evidence status from `$literature-review`; do not upgrade it during drafting.
- Cite theorem, section, page, table, figure, or appendix locators for load-bearing claims when available.
- Distinguish author-reported findings, cross-source synthesis, inference, contradiction, and absence of disclosed information.
- Preserve preprint and published-version relationships.
- Never delete a citation while leaving its dependent claim unqualified.

## Write synthesis prose

- Organize around conclusions, research questions, mechanisms, or method families rather than presenting one source at a time.
- Begin each synthesis paragraph with the cross-source conclusion or comparison it establishes, then supply the supporting evidence and qualifications.
- Keep citations adjacent to the exact claims they support. Do not collect citations at the end of a paragraph containing several unrelated claims.
- Distinguish author-reported, independently derived, inferred, disputed, and unavailable evidence through precise verbs and qualifications.
- Compare methods only under compatible assumptions, information access, datasets, baselines, and metrics; make mismatches explicit.
- Preserve the author's terminology and natural academic voice. Avoid annotated-bibliography summaries, stock transitions, inflated novelty language, and repeated paper-by-paper openings.
- Keep each paragraph centered on one synthesis job and remove background that does not change the comparison or conclusion.

## Produce the artifact

- Follow the project's existing Markdown or LaTeX conventions when present.
- For a new artifact with no requested format, use Markdown.
- Use compact lists and tables for parallel assumptions, classifications, and comparisons; use connected prose for continuous reasoning.
- Keep figures and tables close to the claims they support and make captions self-contained.
- Compile and visually inspect LaTeX/PDF output when the task includes a rendered document.
- Write only to locations authorized by the user and preserve unrelated work.

Revise the prose only after the evidence structure is stable, without changing claims, citations, equations, section responsibilities, or evidence levels.

## Audit before delivery

Verify that:

- the artifact matches the selected document type and scope;
- the approved corpus and retrieval cutoff are visible;
- comparison axes are consistent across method families;
- notation is defined and not overloaded;
- claims have nearby evidence and citations at the stated level;
- contradictions and gaps remain visible;
- prose presents source-backed synthesis rather than paper-by-paper annotation;
- no new source claim, theorem, experiment, or novelty statement was invented during drafting.

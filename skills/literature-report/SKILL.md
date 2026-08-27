---
name: literature-report
description: Draft or revise literature reviews, related work, application reviews, method comparisons, advisor pre-reads, and LaTeX literature reports using unified notation, core formulas, source-backed comparisons, and explicit research relevance. Use for synthesis across multiple works; do not use for a single citation lookup, reproduction logs, project status or minutes, proof development, or generic technical documentation.
---

# Literature Report

Synthesize a research literature into a conclusion-first, formula-first account
of what existing methods solve, what they assume, where they fail, and how they
relate to the user's current research. Do not produce a sequence of paper
abstracts.

## Working defaults

- Converse with the user in Chinese. Write research documents in concise,
  natural academic English unless the user requests another language.
- Identify the audience, research question, current method, and intended
  decision before drafting. For an advisor, lead with the verdict and
  load-bearing comparisons.
- Preserve an existing document's class, macros, citation style, section
  hierarchy, notation conventions that do not conflict, and authorial voice.
- Prefer compact LaTeX `itemize`, `enumerate`, `description`, and small tables
  for parallel facts, ordered classifications, assumptions, limitations, and
  conclusions. Use prose for genuinely continuous mathematical reasoning.
- List items may be compact fragments rather than complete sentences, but
  their scope, comparison, and logical relation must remain unambiguous.
- Remove long setup, filler, invented terminology, and repeated summaries.

## Core workflow

1. Inspect the authorized source document, bibliography, project conventions,
   and dirty state before editing. Preserve unrelated tracked and untracked
   work.
   If the user forbids live edits, treat the live tree as read-only: copy only
   the authorized inputs to a temporary directory, edit and compile there,
   and return an audit unless a later instruction authorizes source changes.
2. State the main conclusions first: most relevant method families, the
   current research position, feasible applications, and principal gaps or
   risks. If the current method or research objective is not supplied or
   available in the authorized context, mark that gap or ask for it; do not
   invent the project's position.
3. Establish one global notation before comparing papers. Map each paper's
   symbols into it; retain original notation only when the mapping itself
   matters. Never reuse one symbol for unrelated objects.
4. Organize the evidence by research question or method family. For every
   family, give the research target, information or data assumptions, core
   estimator, model, update, or reformulation, guarantee or evaluation
   criterion, computational support, relation to the current research, and
   limitation. Include the load-bearing formulas.
5. Match every guarantee and metric to the actual research target. In
   optimization and learning reviews, keep estimation, prediction,
   stationarity, global optimality, robustness, calibration, and regret
   visibly distinct whenever more than one appears.
6. For application reviews, make the decision, model, design, or scientific
   output, its scale, data and uncertainty, objective or evaluation target,
   constraints and assumptions, evidence-acquisition cost, safety, available
   data/simulators/ground truth, actual estimator or solver, direct
   applicability, and final `keep`/`narrow`/`defer`/`reject` verdict explicit.
7. When optimization constraints affect applicability, treat geometry and
   solver compatibility as a primary comparison dimension. Writing a
   projection symbol does not establish that projection is easy; do not use an
   ordinary gradient norm as a certificate for general constrained or
   mixed-integer problems.
8. Close with evidence gaps and research questions that follow from the
   comparison rather than a generic papers-to-read list.

For a new report, substantial rewrite, application review, or constraint-heavy
comparison, read
[references/literature-report-style.md](references/literature-report-style.md)
before drafting. It contains the general notation workflow, method template,
application checklist, guarantee distinctions, and constraint-to-solver table.

When the literature specifically involves decision-dependent distributions,
performative prediction, decision-dependent stochastic optimization, or
power-system demand response, also read
[references/decision-dependent-opt.md](references/decision-dependent-opt.md).
Do not apply that domain-specific formalism to unrelated literature.

## Sources and claims

- Prefer original papers, publisher or venue pages, and official technical
  documentation. Keep each citation next to the claim it supports.
- Verify titles, authors, years, venues, pages, DOI values, theorem statements,
  and reported results. Never repair a bibliography by guessing.
- Mark evidence as full-text verified, abstract-only, or search-result-only
  when the available source is limited. Do not state an abstract-level claim
  as if the theorem or experiment was inspected.
- Synthesize by problem structure and evidence, not publication order or
  citation count. Do not copy an unverified legacy bibliography into a new
  report.

## LaTeX, Overleaf, and delivery

- Use LaTeX when requested or when the project is already LaTeX-based.
- Normally compile, run the project's bibliography workflow, check citations
  and cross-references, and inspect the rendered PDF page by page. Deliver the
  PDF by default, not the TeX source.
- If the user explicitly requests only an authorized edit in an
  Overleaf-synchronized tree and no PDF delivery, compile in a temporary
  directory, update only the authorized source and necessary bibliography,
  and do not copy or send the PDF.
- Do not push, publish, synchronize Overleaf, or create a Git commit unless the
  current task explicitly authorizes that action.

## Final audit

Before delivery, verify that:

- the opening verdict matches the final conclusions;
- every global symbol is defined once and mapped consistently;
- every problem and method family has a core formula;
- distinct formal targets and guarantees are not conflated;
- each application review specifies decisions or design variables,
  uncertainty, constraints, queries or evidence acquisition, solver
  compatibility, evidence, and a verdict;
- every formal citation has been verified at the stated evidence level;
- no `TODO`, empty section, or `Papers to Read` placeholder remains;
- citations and references are defined, labels are unique, and the LaTeX log
  has no unresolved citation/reference or overfull/underfull box;
- the PDF has no clipping, overlap, broken glyph, or damaged table.

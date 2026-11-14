---
name: doc-meeting
description: Create or revise a concise scientific pre-read for an advisor or research meeting, using formulas, comparison tables, supported results, and focused discussion questions. Adapt to proposal, theory, literature, or experiment meetings; explain the document in plain language when requested. Not for meeting minutes, raw reflection capture, or slides.
---

# Meeting Pre-Read Document

Prepare a focused document that makes the research question, available evidence,
and questions for the advisor easy to understand. Match the current stage of
the work; an exploratory meeting need not have a settled idea or conclusion.

## Output defaults

- Follow the user's requested format, language, organization, and length.
  Otherwise follow the project's convention; use English and Markdown when
  neither is specified. Explain the document in the user's conversation language.
- Find the existing document and update it in place. Preserve notation, macros,
  author comments, and unrelated edits. Preserve useful structure, but shorten
  or reorganize it when requested; the old section order is not binding.
- Use LaTeX when requested or required by the project. Compile the saved source,
  check warnings and references, inspect the rendered PDF, and deliver the PDF
  with a link to the editable source when useful.
- Do not add slides, administration, or reproduction records by default.
- When combined with `writing-research`, use it as the prose baseline; this
  skill controls meeting-specific brevity and organization.

## Choose content for the research discussion

Open with the meeting purpose and strongest supported takeaway, or the central
open question when no conclusion is established. Then arrange only the material
needed to understand and discuss it:

- why the problem matters, with a few concrete applications when useful;
- the mathematical problem, available observations or operations, assumptions,
  target, and resources being counted;
- the requested classification, comparison, theoretical result, or experiment;
- what existing evidence establishes, what remains unresolved, and the specific
  choices on which the advisor's input is needed.

This is a content guide, not a fixed sequence of required sections. Do not add
theorems, experimental settings, metrics, or result sections to a proposal that
does not need them. When the user requests a taxonomy, organize around its
dimensions rather than substituting a list of candidate ideas.

## Select core information and keep the layout readable

- For mathematical material, let formulas and compact tables carry the technical
  content. Use short prose to supply motivation, definitions, and interpretation.
- Honor an explicit page limit. Without one, let the page count follow the core
  information. Keep only what matters for the discussion and what the presenter
  can explain; do not optimize for fewer pages or a denser layout.
- To shorten a draft, remove repeated explanations, merge related definitions
  and comparisons, and omit irrelevant template sections. Do not squeeze pages
  by making text, equations, margins, or tables hard to read.
- Keep assumptions, target metrics, and consequential costs next to the results
  they qualify. Brevity must not hide what a result actually proves.
- Do not reproduce table entries in paragraphs or repeat every formula in words.
  Add only the interpretation needed to draw the relevant conclusion.
- Keep detailed literature audits in the existing review. Preserve the pre-read's
  own citations and reference list as described below.

## Use readable labels and conventional references

- Name categories with ordinary English labels or established abbreviations,
  defined at first use. Use labels such as "Both gradients" or "Frozen base
  with correction", rather than invented codes such as G11, U01, or H_E.
  Mathematical symbols still belong in formulas where they have a defined role.
- For research material that draws on literature, include a proper reference
  list with authors, title, venue or source, year, and a DOI or URL. Cite each
  claim near the relevant text or table. A linked method name does not replace
  its bibliographic entry. Do not delete references merely to save pages.
- Use the project's normal citation mechanism and reuse its bibliography. In
  LaTeX, write paper or method names directly with standard `\cite{...}` calls;
  do not define paper-specific commands just to alias names or hyperlinks.
  When no bibliography exists, a self-contained `thebibliography` is suitable.
  Preserve a user-requested citation style.

## Build classification tables when requested

- Define each dimension by an operational question: what can be observed,
  changed, assumed, or charged? Explain why changing it changes the problem.
- Within a dimension, make categories disjoint and cover the declared scope.
  Properties that can coexist belong on separate axes or explicit flags, not
  opposite sides of a forced either/or classification. State exclusions.
- Separate access and allowed updates from assumptions about errors or noise,
  and separate those from budget and cost conventions.
- Use several compact tables rather than an unreadable Cartesian product.
  Make their relationship clear and show the relevant joint cases; marginal
  coverage alone does not establish coverage of their intersections.
- Place a paper's specific setting or theorem in the appropriate case. A paper
  can cover several cases; do not assign the whole paper a misleading single label.
- Distinguish a populated case, an unverified case, and a possible research gap.
  An empty cell means no matched result in the checked corpus, not proved novelty.

## State results precisely without expanding the document

- Define symbols by first substantive use. A shared notation table helps only
  when it saves repetition; include types, dimensions, and units where needed.
- Show the setup, target metric, and relevant budget in formulas when useful.
  Explain how to read the target. Distinguish a fixed-budget error bound from
  a sample-complexity bound, and an iteration count from a query count.
- For each important literature result, give the relevant assumptions, actual
  guarantee or rate, comparison, and limiting condition. Attach a primary source
  and a theorem or section locator for claims that need precise verification.
  Do not manufacture a guarantee for an empirical or differently scoped paper.
- When claiming a resource saving, count the full procedure, including relevant
  initialization, calibration, estimation, validation, and inner work. State
  what the cost model excludes.
- For experiments, give only the setting, baseline, sample size, aggregation,
  and uncertainty needed to read the result. Define nonstandard metrics; do not
  expand every familiar metric into a separate explanatory section.
- Interpret the important result in a short sentence or list. Discuss magnitude,
  uncertainty, comparison, and limitation where relevant; do not repeat a fixed
  five-part analysis after every table. Empirical uncertainty is not a required
  field for a mathematical theorem or a literature taxonomy.
- Distinguish proved results, empirical observations, conjectures, and unverified
  possibilities. Use formal theorem environments only when they help. Keep long
  proofs in the existing mathematical document rather than duplicating them.

## Explain the document in plain language when requested

Keep the written pre-read compact. Provide the requested walkthrough in the
conversation or requested speaking notes, following the actual meeting order.

- Match the reader's familiarity with the field, not just their mathematical
  training. Introduce necessary terminology at first use; avoid unexplained
  labels and invented compressed phrases.
- For each main question or classification axis, explain the concrete process:
  what we have, what we can do or measure, what is unknown, and why it matters.
  Use a small example before the formula when that makes the distinction clearer.
- Explain each key result through its assumptions, what it achieves relative
  to the comparison method, and what costs or limitations remain. Do not merely
  read the table aloud or translate its labels.
- Connect a possible gap to the closest existing result and the missing step.
  Make the advisor's decision concrete without claiming novelty prematurely.

## Templates and final check

Use `assets/meeting.md` or `assets/meeting.tex` as optional starters. Their
sections are replaceable; preserve a useful existing project template.

Before delivery, check that the meeting purpose is clear, the requested scope
and organization are preserved, formulas and tables remain readable, and the
essential definitions, assumptions, costs, citations, reference list, and evidence
status are clear. Remove duplicated prose and irrelevant scaffolding. Verify the
rendered page count and layout for a PDF. Provide a plain-language walkthrough
when requested without expanding the pre-read into a transcript.

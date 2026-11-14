# Research sources and delivery

Inspect the authoritative source, project instructions, existing edits and requested scope before changing files. Preserve the working format and unrelated changes. Reuse notation, macros, bibliography, semantic theorem environments, numbering and useful structure; do not silently strengthen claims or replace scientific content for stylistic convenience.

## LaTeX source conventions

- Keep one root `.tex` file unless the author requests modular sources or the project already has an authorized modular structure.
- Keep each prose paragraph on one physical source line. Use line breaks for blank paragraphs, environment boundaries, list items and displays, not fixed-column wrapping.
- Use `\label`, `\ref` and `\eqref` rather than manually maintained equation numbers. Preserve labels, citation scope and source locators beside imported results.
- Resolve broken references and accidental duplicate text for a deliverable. Preserve intentional placeholders and incomplete arguments as explicitly marked draft material rather than hiding them.

For a requested rendered LaTeX/PDF artifact, compile from the actual project root, resolve relevant references, inspect warnings and visually check the output. A local build validates the local artifact, not remote synchronization or submission. State any verification that could not be performed.

Before sharing, confirm the reader can identify the purpose, follow the reasoning, locate support and distinguish established results from unfinished work. Use `doc-paper`'s additional evidence and venue checks when publication/submission readiness is the goal. A paper may be unfinished during drafting; do not call it ready while central support is unresolved.

For technical components needing development, use `doc-literature` for verified synthesis, `doc-math` for formal mathematics and `doc-experiment` for execution/reproducibility records when available. Independent proof correctness checks belong to `mathbox:proof-audit`; conservative mathematical proofreading belongs to `mathbox:proofread-math` when relevant. Do not automatically route ordinary notes to a full submission-paper review or turn a narrow wording request into a mathematical audit.

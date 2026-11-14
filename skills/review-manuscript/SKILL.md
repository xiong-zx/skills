---
name: review-manuscript
description: Review existing paper drafts — submission reviews, read-only audits of definitions, terminology and claims, mathematical statement/proof readability and notation burden, and post-draft language audits or polish. Use whenever the user asks to review, audit or check the writing of a manuscript (审稿、审查、只读审计、检查写作、术语统一), even without naming this skill. Assessments are read-only; polish or rewrite requests authorize scoped edits. Use doc-* and writing-research for drafting.
---

# Review Manuscript

Review an existing paper against its intended readers and claims, or polish its language after drafting. Use writing-research for ordinary notes and doc-paper for paper drafting. Keep assessment findings separate from applied changes.

## Establish scope

- Identify the authoritative version, target venue and paper type when known, requested depth, and available material. A full review reads the current paper, figures, captions, and relevant appendices; language work reads the supplied scope and the context needed to interpret it. State material coverage limits.
- Before choosing the lens, check the project's records of what is already verified, such as its status file, author-requirement record and earlier reviews. If correctness has been checked and the author asks about the writing, review the writing; reopen a proof only when a writing finding depends on a suspected error, and say so. When a request could mean either lens, as in "the same standard as before", confirm it in one sentence. Read the author's recent decisions there too; when a proposal would reverse one, mark the conflict and leave the choice to the author.
- Choose the requested task: full paper review, mathematical-exposition review, language audit, or language polish. Review, scan, or feedback requests are read-only. Polish, rewrite, or fix requests authorize edits within the supplied scope; do not require another approval for those edits.
- A language-only request reads the relevant passage and context, then uses only the language reference below. For requests about paragraph logic, transitions, motivation or the purpose of formulas, also read the reader-and-technical reference and trace the passage's dependencies. For mathematical statements, proof progression, notation overload, or formula readability, use the specialized reference below. These focused modes do not initiate a correctness, novelty, or full-paper audit. For a complete review, cover all three lenses and prioritize the central reader and evidence obstacles.

## Maintain reusable author requirements

Follow the project's feedback process. If it accumulates examples for a later update, record the supported observation in its existing record when authorized. Update shared guidance when the task authorizes it. Consolidate general prose in writing-research, paper drafting in doc-paper, and review diagnostics here. Keep manuscript-specific findings in the project.

## Review lenses

1. Read [references/reader-and-technical.md](references/reader-and-technical.md) for a skim-path and linear-path review of the paper's argument, results, notation, explanations, and visual presentation.
2. For a full review or a question about validity, contribution, experiments, novelty, or readiness, read [references/paper-audit.md](references/paper-audit.md). Map central claims to evidence and distinguish manuscript-internal checks from externally verified facts.
3. Read [references/language-audit.md](references/language-audit.md) for standalone language audits, post-draft polish, and the language pass of a full review. Use its linked examples when a technical contrast, logical relation, or proposed edit is ambiguous. In a full review, report language findings after argument and evidence findings.

For a thorough reader-flow and language review, combine the reader-and-technical and language references. Review continuity across paragraphs before sentence-level wording, then reread the complete scope and check semantic fidelity. Include proof prose, formula lead-ins and follow-ups, headings, captions, table notes and the final pages; do not infer whole-appendix coverage from a sample. Keep proposed changes to the result inventory separate from language repairs.

When a disputed proof or external result is load-bearing, use the appropriate specialized audit or source check and state its actual verification status. A readable proof overview, rendered figure, successful compile, or failed literature search does not by itself establish correctness or novelty. Do not automatically launch a broad multi-skill audit for a narrow writing question.

## Mathematical exposition

For mathematical statements, proofs, formula readability or pseudocode, read [references/proof-readability.md](references/proof-readability.md) and its shared standard. Apply the tests relevant to the requested scope and report the actual checks performed.

## Report

When an audit document is requested, save it in the project’s research or review working directory, following the author’s path and project naming conventions. Do not write or copy working audit reports into `deliverables/`, or create delivery-catalog records and manifests for them by default. Providing a link to the working report does not imply frozen-artifact publication. Prepare a separate export only when explicitly requested.

Give each material finding a location, observation, consequence, and smallest supported fix. Separate blockers, major issues, and minor issues by their effect on the paper's claims and interpretation, not by taste. Include strengths worth preserving and disclose what was not checked. Do not manufacture a score, acceptance forecast, reviewer identity, or editorial decision.

For authorized language polish, make the smallest coherent edit here and compare the revised propositions with the source. Preserve numbers, notation, assumptions, citations, evidence status, and unrelated edits. Structural rewriting uses doc-paper when requested. For LaTeX changes, compile and inspect affected pages before claiming the local revision is complete.

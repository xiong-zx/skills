---
name: doc-math
description: Develop or revise the formal mathematical content, structure, and mathematical prose of a research document, including notation, definitions, assumptions, theorem and lemma statements, proofs, metric definitions, derivations, and theory-guided interpretation. Use mathbox:proof-audit for independent correctness review and doc-experiment for reproducibility records.
---

# Mathematics Document

Develop the mathematical objects, statements, derivations, proof structure, and local mathematical prose required by a research document. This skill does not perform an independent adversarial proof audit or own a complete manuscript's global narrative.

## Boundary

- When `$writing-research` is explicitly combined with this skill, use it as the general academic-writing baseline; this skill's notation, theorem, proof, and mathematical-prose rules override any conflicting general rule.
- Own notation, definitions, assumptions, formal statements, derivations, proofs, metric formulas, mathematical exposition, and theory-guided interpretation.
- Preserve established claims, notation, macros, section hierarchy, and unresolved uncertainty when revising an existing document.
- Use `mathbox:proof-audit` when the task is to referee, stress-test, or independently verify an existing proof.
- Use `$writing-research` to integrate mathematics into a presentable note; use `$doc-paper` for publication-paper structure, coordinated sections, and submission readiness.
- Put commands, environments, artifacts, and full reproduction evidence in `$doc-experiment`.

## Establish the mathematical contract

Before writing, identify:

- the research question and exact mathematical object;
- variable types, dimensions, domains, and index ranges;
- assumptions and quantifiers;
- the status of each claim: definition, derived identity, lemma, proposition, theorem, corollary, conjecture, or heuristic;
- which results are new, cited, assumed, or still unproved;
- the required output format and the surrounding document's conventions.

Do not silently turn an intuition, numerical pattern, or desired conclusion into a theorem.

## Define notation before use

Read [shared research presentation](references/research-presentation.md) for notation, model/information conventions, selective formal environments, solver interfaces and mathematical prose. These shared rules apply to both notes and papers; the formal-development requirements below apply within the requested scope.

## Structure formal content

- Put definitions and assumptions before dependent results.
- State load-bearing hypotheses and conclusions in formal statements, with quantifiers and domains explicit or unambiguously established in the preceding setup.
- Use `Lemma`, `Proposition`, `Theorem`, and `Corollary` according to logical role. In a submission paper, also follow doc-paper's contribution hierarchy: central convergence, rate or complexity guarantees should be Theorems, including a central result derived from a broader theorem; supporting steps belong in Lemmas or Propositions. Preserve the actual derivation, provenance and proof status when relabelling.
- Label unproved claims as conjectures, hypotheses, or proof sketches.
- Distinguish equality, approximation, asymptotic relation, bound, empirical fit, and heuristic correspondence.

## Present assumptions

Keep an assumption environment to the core substantive conditions and their quantifiers. Introduce notation, known parameter ranges, probability spaces and routine standing measurability conventions outside the box when they are setup rather than the restriction being studied. State their scope explicitly: relocation must not drop a condition, weaken a quantifier, hide required knowledge of constants or change a theorem's contract.

After each substantive assumption, explain what it means and why or when it is applicable. Support that explanation with precise prior-work attribution where relevant, a concrete model/example, or checkable sufficient conditions; select the evidence appropriate to the assumption rather than requiring all three mechanically. Explain how bounds can be obtained when that matters to the algorithm. Do not claim that a condition is automatic or easy to verify without support, or treat empirical fit, local optimization, or a citation alone as a certificate of the required global condition. Related conditions may share one concise explanation.

For a condition with several components, name for each component the step or result that fails without it and give a minimal example; drop a component with no such role or mark it optional. Develop from the smallest condition that supports the result and add a component only when an example requires it.

## Develop derivations and proofs

For each proof or derivation:

1. state the goal and the assumptions used;
2. expose the load-bearing intermediate implications;
3. name external results and match their hypotheses before use;
4. justify changes of limit, expectation, differentiation, integration, optimization, or matrix factorization;
5. track domains, dimensions, signs, constants, and boundary cases;
6. state exactly what remains when the argument is incomplete.

Do not hide a missing implication behind phrases such as "clearly" or "similarly." Do not replace a proof with experimental evidence.

## Write mathematical prose

Use the same [shared presentation rules](references/research-presentation.md#explain-algorithms-proof-status-and-mathematical-prose), not a separate prose checklist. Improving readability does not authorize repairing a disputed proof or changing the mathematical contract.

## Define metrics formula first

For each mathematical or experimental metric:

1. define all symbols and the summation or integration domain;
2. display the exact formula and normalization;
3. state range, units, null/control value, and aggregation convention when applicable;
4. explain what larger, smaller, zero, or non-monotone values mean;
5. distinguish estimator, population quantity, diagnostic, surrogate, and optimization certificate.

Do not use an unconstrained gradient norm as a feasibility or optimality certificate for a constrained problem without justification.

## Connect theory and evidence carefully

Follow [theory/evidence boundaries](references/research-presentation.md#connect-theory-and-evidence); use `$doc-experiment` for full execution provenance. Mathematical guarantees and empirical or causal interpretations remain distinct.

## Produce the document

- Preserve an existing Markdown or LaTeX structure unless change is authorized.
- For a new document with no requested format, use Markdown.
- Use displayed equations for load-bearing formulas and compact lists for assumptions or cases.
- Keep connected mathematical reasoning in prose when bullets would obscure dependencies.
- In a long note developed in stages, keep the opening current: one table of present results with their premises and proof or review status, and one summary. Do not append stages while the opening still describes an earlier one.
- Compile and inspect LaTeX/PDF output when a rendered artifact is required.

After the formal content is stable, revise its local prose without changing definitions, equations, assumptions, logical dependencies, or claim status.

## Audit before delivery

Verify that:

- every symbol is defined and consistently typed;
- assumptions precede the results that use them;
- statement labels match logical roles;
- proofs expose the necessary intermediate reasoning;
- external results have source and hypothesis checks when required;
- summary tables, overview sentences and comparisons with prior results match the exact statements they summarize and keep each result's premises (assumption version, algorithm class, budget or parameter range);
- empirical evidence has not been promoted to a theorem or causal claim;
- unresolved steps remain labeled;
- mathematical exposition is concise, complete, and distinct from proof auditing, whole-manuscript narrative, and experiment documentation.

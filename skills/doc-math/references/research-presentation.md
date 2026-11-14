# Shared mathematical research presentation

Use these presentation rules for mathematical notes and papers; they do not authorize inventing proofs or changing scientific content. `doc-math` owns formal development and `doc-paper` adds publication completeness. Use [writing-research's source conventions](../../writing-research/references/source-and-delivery.md) for LaTeX files and rendered delivery.

## Make the model and notation understandable

- State relevant oracle, sampling, information, algorithm and cost conventions. Distinguish what an oracle returns, what is computed from data and what is assumed. Specify object types, dimensions, units, normalizations, index ranges and dependencies where ambiguous; keep one meaning per symbol and trace authorized changes through dependent text.
- Define symbols before their first substantive use; reuse project notation/macros and avoid silently changing overloads or row/column conventions. When the author's own manuscript already names assumptions and parameters, use those names in notes and discussion rather than renaming them; record an unavoidable clash once as a short correspondence. Introduce established background where needed, method-specific objects near the method and analysis-only objects near their use. Use a notation table only when symbols recur across sections; define local objects beside their formulas.
- Introduce a symbol when it reduces reader work. Reuse existing definitions or write simple one-off expressions directly rather than naming bookkeeping averages/envelopes/indexed variants. A useful complex one-use expression may still deserve a name; frequency is not a deletion rule.
- Explain a complex formula's purpose and point to its ingredients' definitions. Separate definitions, assumptions, identities, original/cited results, conjectures and open obligations. Explain each assumption's meaning, plausible setting and restriction, distinguishing a true-objective assumption from one on a data-dependent surrogate; related conditions may share one explanation. For substantive assumption development use [Present assumptions](../SKILL.md#present-assumptions).

## Select formal environments by meaning

Give a central definition or substantive result its appropriate logical environment. A recurring established object can deserve a Definition, but a new symbol alone need not. Use ordinary prose for index sets, constants, standard formulas and local auxiliaries; keep independent displays readable.

Place routine solver calculations/supporting properties near the relevant solver or in an appendix, preserving conditions and dependencies. Remove unnecessary wrappers by meaning, not by cosmetically relabeling every Definition as a Remark or every Theorem as a Proposition. For a publication paper, also follow its result hierarchy and main-text selection rules.

## Explain algorithms, proof status and mathematical prose

- Present a modular algorithm's outer information flow and separate solver contracts: objective, domain, inputs, accuracy metric, certificate and known/assumed costs to the extent established. A local stationarity certificate does not establish a global function-gap certificate. Mark unresolved solver, cost or proof obligations rather than calling the draft self-contained.
- Distinguish intuition, heuristic explanation, proof overview, sketch and complete proof. State what a sketch omits; a provisional result remains provisional after polishing. Preserve model, quantifiers, constants, conditions and established claims. Do not replace a proof by numerical evidence or let intuition carry its proof burden.
- Explain a definition/lemma/derivation's purpose when the dependency structure does not make it evident. Introduce displays by their object or implication, and follow with interpretation only if it adds meaning. Keep major proof goals/stages and their actual logical relation visible without rhetorical filler.
- Use precise verbs such as defines, implies, bounds, converges and contradicts; avoid unsupported "clearly," "obviously" and "similarly." Preserve author voice, remove redundant restatement but retain repetition needed for a definition or hypothesis.
- For this author's reported minimizers, prefer local/global minimum and their neighborhoods to valley metaphors. Distinguish exact attainment, proximity and basin membership; never relabel an unverified local minimum as global.

## Connect theory and evidence

Distinguish mathematical consequence, empirical observation, interpretation, causal claim and conjecture. State whether an experiment verifies an assumption, illustrates a theorem, tests a mechanism or merely correlates with a prediction. Keep exact values in figures/tables and explain their implication in prose. Keep experimental context brief here; use `doc-experiment` for independent execution and reproducibility records.

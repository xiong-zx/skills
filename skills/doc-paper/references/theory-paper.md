# Theory Paper Completeness

Apply these additions to the [shared research-presentation conventions](../../doc-math/references/research-presentation.md) inherited through writing-research. Formal claims and deferred proofs must be complete enough for a specialist to verify the paper's central results.

## Arrange the results by dependency

Use [mathematical-exposition.md](mathematical-exposition.md) as the single standard for rule strength, statements-first drafting, main-text result selection, reading order, local proof flow, notation, and formulas. This reference adds completeness and quantitative-contract checks rather than another exposition template.

The main text must expose the exact oracle, information, sampling, algorithm class, complexity measure, and solution criterion of its claims. Deferring calculations does not justify deferring a condition that changes the meaning of a result.

## Interpret the main results

Follow each central theorem with a concise interpretation of its contribution and advantage over the closest relevant results, even if the Introduction already makes the comparison. Name the comparison dimension and give the reason: the optimization target, probability guarantee, feedback used, model assumptions, accuracy or cost. Preserve material qualifications, and distinguish a stronger guarantee on one dimension from universal superiority or a faster rate under matched assumptions. Explain important bound terms and parameter consequences rather than merely repeating the formula or calling the theorem important.

## Explain the objects and information

- Make “known function” operational: state what can be evaluated, at which arguments, and from which observed data. Distinguish a known sample-loss evaluator from a known expected objective. When deployment, evaluation and reference arguments differ, explain their roles and domains. Specify the actual oracle response, and say whether a comparison shares the realized data history or only the observation model.
- Keep the mathematical type visible in interpretation. A fitted signed measure need not be a probability distribution; a kernel uncertainty need not have a Bayesian posterior interpretation. Describe what the estimator computes and which quantities the theorem certifies.
- Separate an exact identity for a fitted object from an interpretation involving the true object and from a statistical accuracy claim. Put differentiability or interchange conditions beside the interpretation that needs them, without silently adding them to the main theorem. A value-error bound alone does not justify gradient accuracy or unbiasedness.
- When the paper compares access models, oracles or protocols, state each simulation by its direction and cost: which model runs which algorithm, what it observes and what it is charged. For example, a $K$-query algorithm runs under the reuse protocol with one new sample index per round and the same number of gradient evaluations. An inclusion diagram or "by inclusion" does not supply this reason. State the costs in the text beside the figure; for this author, the figure does not repeat text the prose already gives. Say which relations are exact and which hold only up to constants.
- When a definition follows a cited source ("following", "as in"), state at that definition the material differences in observed information, cost unit, output timing and quantifiers. An appendix may carry the full bridge, but main-text readers should not have to assume that the protocols coincide.

## Check each formal statement

For every theorem, proposition, or lemma, check:

- object types, dimensions, parameter ranges, assumptions, and quantifiers;
- algorithm and oracle conventions, probability or expectation, and conditioning;
- initialization and admissible output;
- bound, constants, asymptotic regime, and cost unit;
- dimension and sample-budget dependencies;
- endpoint and degenerate cases;
- whether the result is original, adapted, or cited.

Do not make a hypothesis depend only on an equation number when it becomes ambiguous outside the surrounding paragraph. Keep theorem content separate from a broader interpretation.

Apply the shared standard's requirement that main-text statements expose the conditions and ingredients needed to interpret them; deferring a proof does not defer those meanings.

State a finite-horizon inequality with its constants and dependencies before an asymptotic interpretation. When reporting a rate, display the powers and logarithmic factors relevant to that claim. Define any asymptotic notation before its first use and state which parameters are fixed. For this author, avoid soft-O notation in formal result statements and give the logarithmic factors explicitly. If a numerical constant is not derived, quantify its existence and dependencies rather than inventing a value or calling an order bound fully numerical. Distinguish a guarantee for each prespecified horizon from one event holding simultaneously over all horizons, especially when a parameter is selected separately for each run.

When converting an asymptotic rate to a sufficient horizon or budget, give an actual sufficient choice, such as the ceiling of a sufficiently large constant multiple, before stating its order. An \(O(\cdot)\) upper bound alone is not a prescription for choosing a sufficient budget. State which parameters remain fixed and which may vary across runs. Distinguish sample or query complexity from the offline work needed to meet a solver contract.

## Supply complete proofs

A full proof or appendix must:

1. State or precisely reference the claim being proved.
2. Identify intermediate results and verify their hypotheses.
3. Expose every load-bearing probabilistic, analytic, and algebraic implication.
4. Track filtrations, conditioning, independence, domains, constants, and boundary cases.
5. Account for initialization, termination, ceilings, and full computational or oracle costs.
6. Distinguish deterministic, in-expectation, and high-probability conclusions.

For an algorithmic theorem, use the [pseudocode guidance](mathematical-exposition.md#5-present-pseudocode-readers-can-follow) to align the specification and proof. Justify any transfer from an intermediate iterate, event or certificate to the claimed output and guarantee. A local stationary solution does not certify a required global function-value gap. For a lower bound, include membership of the hard instance, information calculations, testing or reduction argument, and the exact algorithm class covered. State the order of instance, algorithm, horizon and randomness quantifiers, including when an adverse instance is chosen; a finite-horizon conclusion is not automatically an infinite-trajectory claim.

If an implication remains unresolved, retain its status in the working draft and treat that contribution as a readiness blocker. Calling an argument standard does not supply a proof or a source with matching hypotheses.

## Use the appendix without obscuring the argument

For this author, a formal verification (for example in Lean) is an auxiliary check, not part of the paper's argument. Mention it in one sentence with a repository link and keep statement correspondence, proof-organization notes and audit details in the repository. Being formalized is not a reason to keep a result in the paper.

Deferred arguments remain complete and precisely referenced. Use the shared standard to choose which results belong in the main text, without turning the appendix into a collection of unexplained technical fragments.

When a passage mixes an identity, a conditional interpretation and a guarantee, separate those roles so the reader can locate the conditions before drawing the conclusion. Prefer a short role reminder and the exact label of an existing bound to an indirect reference such as “the bound after” another equation or a repeated long formula. State comparison directions with both objects named when a pronoun could reverse the operation.

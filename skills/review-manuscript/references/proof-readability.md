# Mathematical exposition review

Use for mathematical statements, proof flow, notation, formulas and pseudocode. Read the relevant parts of the shared [mathematical-exposition standard](../../doc-paper/references/mathematical-exposition.md), including rule strength. These diagnostics are for a read-only review.

## Scope and calibration

Fix the intended reader, reviewed version, statement/proof scope, and required dependencies. A full requested appendix pass reads its full scope; a sample supports only sample findings. Distinguish source-level exposition, rendered layout, correctness, source verification, and novelty coverage.

Apply the shared standard at its actual strength:

- **Requirement:** locate missing meaning, operative conditions, an unresolved load-bearing implication, or loss of mathematical scope. Separate a reporting/interface omission from a suspected proof gap; neither alone establishes a false-theorem verdict.
- **Default workflow:** the writer normally settles statements and dependencies before details. The final manuscript cannot by itself show the order in which it was written. Review the resulting skeleton; do not allege a process violation from its appearance.
- **Flexible advice:** explain concrete avoidable reader work before recommending reordering, moving a definition, adding a transition, or subdividing a proof. Centralized notation, a natural derivation order, deferred proofs, and parallel paragraphs are not violations in themselves.

Poor flow is not an aesthetic score or evidence of AI authorship. Prior correctness certification is not required to identify an exposition problem, but a readability pass does not certify the mathematics.

## Default review sequence

These lenses follow the writing workflow without forcing the paper into that order.

### 1. Recover the statement and dependency skeleton

Read the central claim and identify the intermediate conclusions actually needed. Trace important lemma uses, not only their wording. Can each statement be interpreted from its scoped setup? Does a later proof have to mine another proof for an unstated consequence? Distinguish a clear statement whose proof follows later from a necessary object first defined later.

For a class used in a central claim, pick a representative candidate and decide membership from the stated types, parameters and conditions. Locate any information the reader must infer. For a substantive assumption, read the sentence with its formula and identify the restriction, its scope and the evidence for applicability, if claimed. Check that routine setup remains explicit. The title alone supplies no condition, and an illustrative example establishes only the scope it covers.

Check whether result boundaries isolate meaningful tasks. A key Lemma may contain the hard idea and a Theorem the final assembly. Flag excessive fragmentation or unrelated conclusions bundled together only when they impede use; an equation may be the right checkpoint. Relabelling alone changes neither importance nor evidence.

### 2. Assess main-text selection

Does the main text foreground the important results or those helping readers grasp the mechanism and structure, rather than inventory every technical claim? Do readers learn the answer before extensive preparation, perhaps through an accurate informal version? Do a sequence of lemmas and its surrounding target explain why the sequence belongs here?

Trace any simplified theorem or lemma to its formal counterpart and check whether the scope and success criterion agree. Recommend moves or consolidation where they help the reader follow the argument while preserving material conditions and exact references.

### 3. Follow the reading order

Check when the reader learns the objects, assumptions, targets, and reasons needed for the current passage. Prefer substantive definitions near their first substantial use, but accept coherent foundational setup and an upfront notation overview. No fixed Definition–Lemma–Theorem order or automatic objection to discovery/implementation order.

For this author, flag a section or subsection that opens directly with a formal environment, and check that an opening pointing to several appendices says which proves what. Locate actual backtracking or purposeless preparation, not mere departures from a preferred sequence. Ask whether optional extensions or alternatives repeatedly interrupt an unfinished task. Distinguish those detours from boundary cases required by the theorem. A proof can defer such a case precisely; it cannot silently discard it.

### 4. Inspect local progression and detail

At meaningful task changes, can readers recover what is established and what remains? Transitions are advice: independent prerequisites need no invented causal bridge, and natural algebra needs no sentence between every line.

Reconstruct one consequential implication from the passage, for example how a moment condition constrains a revealing event and that event determines a query cost. Identify the first step a reader cannot recover, and check its formal counterpart when needed to distinguish omitted exposition from an unsupported implication. Check that the assembly reaches the claimed output, metric, probability or expectation, and cost.

For notation and formulas, use the detail probes below instead of counting symbols or demanding a larger glossary.

### 5. Reread both scales

Without calculation details, can the important statements and explanations convey the route? With the details restored, can readers inspect consequential connections and retain their conditions? Report what is visible in the supplied scope, not a claim to have reconstructed an uninspected proof. Preserve a useful positive control and explain why it works.

## Detail probes

- **Aliases and scope:** trace local meanings and uses. Remove a simple unused alias when it lowers translation work; retain recurrent errors, conditional means, and meaningful one-use checkpoints. Check proof-local symbols exported without setup and suppressed dependencies that erase mathematical distinctions. Flag a fixed numerical ratio renamed as a tunable-looking constant, such as \(c_\alpha=1/C_I'\).
- **Decorations and families:** check what hats, bars, primes, or indices distinguish. Suggest a consistent local clarification rather than automatic global renaming. Similar letters in separate local arguments are not inherently wrong. Within one statement, algorithm, proof or section, check that no letter names two objects, counting subscripted family members, and recheck any rename against its new neighbours.
- **Introduction burden:** distinguish unfamiliar constructions introduced without a role from a legitimate upfront notation list. Group related definitions or stage distinct tasks when useful; neither a symbol budget nor one symbol per sentence is justified.
- **Formula interfaces:** identify whether a display defines, rewrites, bounds, or interprets. Locate a consequential unexplained transformation, dense inline target, or numerical sum whose analytic terms are hidden. An aligned calculation, symbolic bound, or helpful shorthand can repair the issue; not every display needs prose on both sides.
- **Pseudocode:** trace initialization, an iteration and termination through the stated steps and references. At each draw, identify what is fixed, which evaluations share a sample, and which stored values are reused. Check the output's index, range and distribution against the theorem and expanded algorithm or proof, and that its name does not collide with another symbol in the algorithm. Check independence where required. Recompute the cost in the theorem's units, distinguishing iterations, draws, evaluations and other work where they differ. Trace optional or final batches when they affect the count. Treat equivalent names as a consistency issue only if the correspondence is unclear.
- **Layout and conventions:** preserve the author's numbering of multiline/multi-formula displays even when unreferenced. Do not infer a rendered-layout defect from source alone or delete terms, conditions, and labels to fit a page.

## Report and boundaries

Give the exact location, the lookup/translation/inference the reader must perform, its consequence, and the smallest supported repair. Indicate whether the basis is a requirement, a default, or flexible advice when that distinction matters; do not turn this into compulsory per-finding labels. State mathematical-change risk: editorial clarification, consistent notation change, or a mathematical/source question needing verification.

Separate readability, notation ambiguity, missing interfaces, and suspected correctness issues. A guideline departure without reader harm is not a finding. Do not infer the drafting process from the finished prose. A short proof can be kept unchanged, and a long proof can be well organized.

Review-only requests do not authorize fixes. Authorized revisions preserve the shared standard's mathematical contract; an uncertain implication must not be silently repaired. No fixed number of steps, headings, formal results, symbols, displays, or intuition paragraphs; no banned-word diagnosis, AI-detection verdict, score, or claim that bounded application tests prove universal readability.

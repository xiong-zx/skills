# Mathematical statements, formulas, and proofs

Use for drafting or revising mathematical statements, proofs, and pseudocode. Assume a reader familiar with standard tools in the field and new to the project. This reference owns the exposition standard used by review-manuscript.

## Rule strength

- **Explicit requirements:** preserve the mathematical contract and evidence status; give the information needed to interpret a statement before its use; expose load-bearing implications and discharge the complete proof obligation. The author's source/numbering conventions below are also requirements.
- **Default workflow:** settle the statements and dependency skeleton before filling proof details, then select main-text content, arrange the reading path, expand the argument, and reread at both scales. This is an iterative writing method, not a mandatory published outline or a rule about how research must be discovered. Apply it within the authorized scope.
- **Flexible guidance:** definition placement, exposition order, transitions, proof subdivision, and notation/layout choices depend on reader work. Prefer definitions near use and a visible main result, but allow coherent foundational setup, centralized notation, natural discovery order, and already clear prose. Recommendations are not automatic defects.

A clear exception to a recommendation is not a mathematical failure. Conversely, a recommendation cannot excuse missing conditions or an unjustified implication. Do not turn these levels into a scorecard.

## 1. Default workflow: settle statements and dependencies first

Before drafting detailed proofs, establish the intended Theorem, the Definitions and assumptions needed to interpret it, and the Lemmas or Propositions that supply its intermediate conclusions. Identify how those conclusions combine. For a local revision, recover that skeleton rather than redesigning unrelated sections.

Use formal environments for their mathematical roles:

- A Theorem presents a central answer or guarantee. Preserve this author's convention of presenting central convergence/rate/complexity guarantees as Theorems, even when derived from a broader result.
- A Proposition gives a substantive standalone or supporting result, not necessarily a less impressive theorem.
- A Lemma isolates a useful reduction, invariant, estimate, or construction property. It may contain the hardest idea.
- A Corollary presents a secondary consequence with a transparent dependency, rather than hiding the paper's central answer.

For this author, title a lemma or proposition with a noun phrase that names its content, such as "Uniform tracker moment".

For an intermediate result, identify its obstacle, the conclusion a later step needs, and the actual use. Prefer a usable statement to a catalogue of incidental facts. Expose an already justified consequence used later rather than making callers extract it from the lemma's proof. Group coupled facts that form one contract; separate unrelated tasks. A transparent calculation can remain an equation inside a proof instead of becoming another lemma.

This skeleton is provisional until the details support it. If the proof reveals missing conditions, an overstrong claim, or an unnatural intermediate statement, revise the skeleton and dependent claims explicitly. Mark unproved connections rather than presenting a polished outline as an established theorem. Settling the skeleton first does not mean publishing every statement before every proof.

## 2. Select the main-text argument

For this author's main text, retain formal Theorems, Propositions, and Lemmas that are most important or help the reader grasp the result, mechanism, or proof structure. Technical certificates and routine auxiliary results can remain in the appendix with complete proofs and usable references. Selection is not deletion of evidence: keep every condition needed to interpret the main claim in the main text or its clearly scoped standing setup.

For this author, the main text is for understanding and the appendix for rigor. When condensing, keep the key steps of each proof as informal lemmas that name their formal counterparts, and cut the prose that restates them instead of reducing the lemmas to a few. Keep the examples and figures that explain why a term of a rate appears; redesign an unhelpful mechanism figure rather than moving it to the appendix. A page target is soft: do not compress a mechanism until readers can no longer follow it. The sentence pointing to a formal version or proof is the last sentence inside the theorem or lemma environment, not a separate paragraph.

Let readers learn the main conclusion before a long technical preparation. For this author, a section or subsection does not open directly with a formal environment: a short sentence first names the question it answers or the role of the result that follows. This orients the reader; it need not be a roadmap or a motivation paragraph. When an opening points to several proof appendices, say which appendix proves which result. If the statement needs substantial setup, an accurate informal preview can come first. Give a simplified theorem or lemma the scope and success criterion needed to read it, and point to its precise formal counterpart and proof.

## 3. Arrange the reading path

**Required information:** a statement must be interpretable with its explicitly scoped setup: object meanings, operative hypotheses, quantifiers, and bound ingredients. A main theorem may defer its proof, not a necessary definition to that proof appendix. A stated result with a deferred proof is not the same as an undefined forward reference; the actual proof dependencies must still be justified and non-circular.

Before optimizing over or quantifying over a class, define its elements, parameter dependence and membership conditions, with the types and quantifiers needed to decide membership. A set builder or a complete prose definition can do this. Introducing an element with a membership assertion leaves the class to be defined.

Use [the substantive-assumption guidance](../../doc-math/SKILL.md#present-assumptions) to place restrictions and routine setup. In a paper, state the object and property of each substantive assumption in a short sentence, with an inline or displayed formula for the precise conditions when helpful. An optional title helps readers find the assumption. Keep quantifiers and exceptional cases close to the condition they govern.

**Preferred placement:** strongly prefer placing substantive definitions just before their first substantial use. Shared foundational definitions can form a coherent preliminary section. Notation naming recurring objects can be collected at the beginning; do not require dispersing it. Distinguish a useful notation overview from a premature collection of constructions whose roles are still unknown.

**Terms (author requirement):** define as few terms as possible. Name an object only when readers need the name repeatedly; otherwise use its notation or a plain description. Explain each remaining term at or just before its first substantive use and set it in bold there. Keep related definitions together, prefer an existing word to a new term, and use one name per object across the main text and appendices. Later uses rely on that definition instead of redefining the term.

There is no fixed Definition–Lemma–Theorem ordering. Method-first, result-first, and interleaved presentations can work. Research, derivation, or implementation order is allowed when it serves comprehension; do not rearrange it merely because of its origin. Mathematical dependency order alone does not establish that readers understand why the ingredients appear.

Keep the central task in view. Avoid repeatedly interrupting an unfinished main argument with optional extensions, alternative proofs, or nonessential boundary discussions. A boundary case affecting validity remains part of the proof obligation; it may be proved in an appropriately referenced place, but its scope cannot be hidden or the case silently discarded.

## 4. Fill the proof details

### Progression and mathematical emphasis

At substantial changes of task, preferably make clear what is available, what remains, and why the next construction or estimate helps. Use a short explanation, a decomposition, or a meaningful checkpoint when needed. Paragraph-to-paragraph transitions are advice, not a requirement for a linking sentence at every boundary. Independent prerequisites can be adjacent; do not invent a causal relation or force a repeated roadmap.

Allocate explanation to the operation that produces the conclusion, such as a cancellation, conditioning step, parameter balance or transfer to the returned point. For a lower-bound construction, show what an observation reveals and which restriction makes learning or progress costly. For an algorithm, connect the design choice to the error or cost it controls. Keep the calculation or reduction that produces a central rate term in view and cite the exact result for deferred details. A short derivation, concrete example or figure can carry the explanation.

Give the applicable reason for a consequential implication, using a descriptive reference or the operative conclusion of an imported theorem. Verify the relevant hypotheses at the necessary level. Routine arithmetic can remain in an aligned chain. The final deduction must reach the claimed output, metric, expectation/event, and cost, rather than an unrelated intermediate quantity; once this is visible, no compulsory recap is needed.

### Notation economy

For a dense passage, privately trace nonstandard symbols' meanings, scope, uses, and replacement cost. This is an editorial aid, not a required ledger in the paper.

- Name recurring objects and useful checkpoints. A complicated one-use expression can also deserve a name; frequency is not a deletion rule.
- Expand a simple one-use alias or alias of an alias when this removes translation work. Do not symbolize every logical step or bookkeeping sum.
- Declare local shorthand and suppressed fixed arguments, but retain dependencies on time, samples, history, parameters, or events that do mathematical work.
- Explain meaningful hats, bars, primes, and indices. Remove redundant objects before inventing ornate replacements. Distinguish unrelated near-identical families within one reading path; local reuse in separate arguments is not inherently wrong.
- Keep one meaning per symbol within a unit read together: a statement, an algorithm, a proof or a section. Readers resolve a letter by its nearest definition, so a second meaning in the same unit makes them re-derive which object is meant. Subscripted family members count as the same letter: an output index \(\tau\) beside thresholds \(\tau_0,\tau_j\) is a collision. Check a new name, including a rename the author requested, against the symbols already in that unit. If a requested name collides, keep it only with a visible distinction or report the conflict to the author instead of applying it silently.
- Do not give a letter with a conventional meaning to an unrelated object: readers take \(e\), \(i\) and \(\pi\) as constants and \(v\) as a vector (author: an exponent became \(\psi\), a map \(\phi\)). This holds even when the two uses sit in different appendices. Do not index cases by a set that mixes labels of different kinds, such as \(\mathsf M\in\{1,2,\mathrm{reuse}\}\); fix the case in words and name each variant's quantity.
- Do not export proof-local notation without an appropriate shared definition. On reuse after a gap, a short role reminder may help more than a larger glossary.
- Group objects forming one structure and stage objects doing different jobs. Neither one-symbol-per-sentence nor a global notation ban is the goal.

### Formulas, constants, and source conventions

A display should define, transform, bound, or interpret an identifiable object. Give a purpose where needed; following prose should add a condition, consequence, or connection, not mechanically read back every symbol. Separate identities, bounds, and heuristics; explanatory intuition cannot supply an unproved implication.

Show a symbolic analytic estimate before a long numerical substitution, making contributions traceable to their source. Keep numerical calibration subordinate when it is not the insight, while retaining required thresholds and constant dependencies. Choose sequential constants non-circularly. Do not give a fixed numerical ratio a new tunable-looking parameter.

Use aligned relations, split bounds, and cases when they expose structure. A useful shorthand may be clearer than repeated expansion. Keep an already legible inline setup intact; do not create a display for every variable or update. Tiny fonts and brittle spacing do not repair an overloaded expression. A revision may leave an effective passage unchanged.

**Author requirements:** write a definition that fits on one line on one line, and never put its left side alone on a line; number multiline/multi-formula displays even when unreferenced; identify them from mathematical content and rendered layout, not only source line breaks. Display crowded related definitions or long target criteria. Follow [shared source conventions](../../writing-research/references/source-and-delivery.md) for one prose paragraph per physical TeX line, the authorized root-file structure, labels and citation scope.

## 5. Present pseudocode readers can follow

State the inputs and what the algorithm returns. Show the order of initialization, sampling and updates, with the indices, branches and stopping or output rule needed to trace a run. For a stochastic oracle, indicate what is fixed before a draw, when evaluations share a sample, and where a previously returned response is used. Put the defining update or an exact reference where the reader needs it. A compact main-text algorithm may delegate detail to a named routine or an expanded version whose inputs, outputs and cost are clear.

Trace initialization, one representative iteration and termination against the theorem and proof. Check that the output object, range and law agree wherever they are used. Reconcile the cost in the theorem's units, including initialization, optional batches and any final evaluation. A notation change to an output index follows that index through the algorithm and analysis, preserving its law, and its new name must not collide with another symbol in the algorithm.

## 6. Reread skeleton and details

First read the statements and necessary explanations without the calculations: can the reader identify the answer, intermediate tasks, and where the important conclusions are used? This is a private reading test, not a compulsory published dependency graph.

Then inspect the expanded argument: are consequential operations justified under the current conditions; do case changes preserve scope; do the ingredients actually combine into the claimed result? Do not substitute a list of equation numbers for a nontrivial assembly. Keep successful compact arguments, meaningful parallelism, and necessary repetition.

**Preservation requirement:** retain assumptions, quantifier order, domains, conditioning, randomness, output conventions, constants/dependencies, endpoints, cost units, and evidence status. If a connection cannot be recovered, flag it and continue supported edits elsewhere; do not repair it silently under an exposition label. A sketch or certificate does not replace the requested complete human-readable proof. No AI-authorship verdict, readability score, or quota for symbols, lemmas, paragraphs, or intuition.

## Contrastive examples

These are examples of decisions, not replacement templates.

### An unnecessary notation ladder

Suppose three vectors occur only in a triangle-inequality calculation. Introducing separate symbols for each pairwise distance and another symbol for their sum makes the reader translate four names to read one bound. Prefer the direct relation

\[
\|u-w\|\le\|u-v\|+\|v-w\|.
\]

By contrast, retain \(e_t=\widehat g_t-\nabla F(x_t)\) when its recurrence, moments, and accumulated effect are studied over several pages. Explain that it is the estimator error and keep its time/randomness dependencies. The relevant difference is function, not the presence of notation.

### A useful lemma versus a constants container

A statement with ten freshly named constants followed by several unrelated bounds hides its interface. If the later proof needs only a uniform moment estimate, state that estimate under the declared setup and give its constant dependencies. Derive the numerical calibration in the proof and keep other facts where needed. If those facts are all required as one construction certificate, retain them together but explain that contract rather than deleting them.

A useful lemma can also explain importance without hype: a uniform-in-time estimate permits the subsequent summation without an additional horizon factor. That sentence is warranted only if the estimate and its later use actually establish that benefit.

### Expose the transfer, then estimate what remains

Suppose a majorant \(Q(\cdot;z)\ge F\), an approximate global inner solve with gap \(\delta\), and a minimizer \(x^\star\) give

\[
F(\widehat x)-F(x^\star)
\le Q(\widehat x;z)-F(x^\star)
\le \delta+Q(x^\star;z)-F(x^\star).
\]

This isolates the remaining majorant-mismatch term before bounding it. Preserve existence, domains, and the global inner-gap requirement. A local stationary inner point does not supply the displayed comparison. Do not add a new error symbol unless it helps the subsequent reasoning.

### A direct proof that should remain direct

For square-integrable martingale differences, two distinct-time terms have zero cross expectation: the earlier term is measurable before the later one, whose conditional mean is zero. Once that conditioning is stated, a short tower-property calculation can finish the claim. It needs no three-step roadmap, new named lemma, intuition paragraph, or separate discussion of each equality.

### Deferred proof versus deferred meaning

A lemma may be stated, used to assemble a theorem, and proved later when the dependency is non-circular. Its statement and conditions must already be clear. By contrast, putting an unexplained quantity in a theorem and defining it only in its later proof forces the reader to guess the theorem's meaning. Repair the missing definition, not the legitimate deferred-proof structure.

### Independent tasks need not have a causal bridge

Instance admissibility and response counting may be independent prerequisites for a theorem. Adjacent arguments can address them separately without pretending one implies the other. Add orientation only where the reader would otherwise lose the task. A case needed for validity is not an optional aside merely because it interrupts a convenient story.

## Sources and adaptation boundary

Original guidance informed by [Tao on appropriate detail](https://terrytao.wordpress.com/advice-on-writing-papers/give-appropriate-amounts-of-detail/), [Lamport on proof structure](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/12/How-to-Write-a-21st-Century-Proof.pdf), [math-prose equation discourse](https://github.com/TianhuaGao/math-prose/blob/main/references/equation-discourse.md), and [proof-readability](https://github.com/flonat/flonat-research/blob/main/skills/proof-readability/SKILL.md). Their useful distinctions are adapted, not their mandatory templates. Mathematical detail and proof placement remain audience- and argument-dependent.

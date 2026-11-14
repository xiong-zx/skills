# Compare ideas, propose useful checks and delegate bounded work

## Compare without manufacturing a winner

Keep scientific value, evidence-bounded novelty, taste/strategic fit and resource feasibility separate. Prioritize important questions and new understanding without allowing easy implementation, field popularity, a confident reviewer or a weighted average to decide the topic. Do not use Elo tournaments, total novelty scores or agent majority votes as scientific evidence.

For broad topic selection, retain important questions needing several connected advances alongside questions whose key uncertainty can be checked now. Name the missing advances and explain how a quick check would help. Do not promise a completion date from a toy example. For a focused request, honor its scope instead of forcing both kinds or a quota of candidates.

Distinguish the importance of the question from the current quality of a proposed solution. A bad mechanism can be replaced while the question remains worthwhile. Separate a scientific obstacle, an implementation problem and missing evidence before recommending rejection. A tool combination, a popular area or an apparently empty gap is not enough.

When selection is requested, explain what would change the recommendation: uncertain prior art, a measurement issue, resource access or a missing theoretical bridge. Recommend exploring, revising, setting aside or rejecting with reasons; keep the user's decision explicit. Preserve unresolved objections and informative disagreement rather than averaging them away. During open brainstorming, do not force a ranking.

## Stress-test the contribution that is actually proposed

- **Mechanism/explanation:** what does this explain beyond the closest account? Derive implications that distinguish it from competing explanations; identify an intervention, counterfactual, counterexample or observation that would discriminate. Distinguish descriptive association from a causal/mechanistic conclusion. Do not demand a new optimizer as a substitute for explanatory evidence.
- **Theory:** state the target claim, assumptions, information model and genuinely unresolved implication. An observation outside the assumptions may motivate an extension but does not disprove a conditional theorem. Try the simplest relevant model, limiting regime or counterexample family; identify the proof bottleneck. A promising derivation is not a proved theorem or verified novelty.
- **Empirical phenomenon:** specify a reproducible observation, strongest alternative explanation, fair baseline/control, metric and resource limit. Prefer a small diagnostic over expensive end-to-end training when it can answer the question; do not generalize a toy result beyond what it tests.
- **Method/system:** state the precise improvement and budget-matched comparator. For multiple components, explain the interaction and which ablation would refute it; a bundle of components or fortunate training run is not itself the contribution.
- **Negative/boundary result:** identify what accepted claim, assumption or expectation it changes, rather than treating failure alone as a contribution.
- **Unification/measurement:** explain the new implication, reduced ambiguity or changed scientific conclusion. A taxonomy or metric should be evaluated for what it enables, rather than assumed novel because it is newly named.

## Match the first check to the claim

Propose the smallest check that could change the decision: a key paper passage, narrow lemma, low-dimensional construction, limiting-case calculation, controlled toy experiment or existing-data analysis. State the question it answers, what plausible outcomes would imply, resources/effort or an explicit unknown, and a stopping/return condition.

If the entire direction depends on an alleged failure or discrepancy, first check that it exists under the relevant conditions. If the question concerns improving an established legitimate task, test the proposed benefit and tradeoff; do not invent a new failure phenomenon as a prerequisite. If the proposed contribution is explanatory, the check must distinguish explanations rather than merely show a better score.

A useful feasibility check tests an uncertainty, not just whether a script runs. Separate what the first check establishes from the further evidence needed for the main contribution. Present an unperformed check as a proposal. Substantive experiments or a research program do not become authorized merely because a check was proposed.

## Delegate when it adds independent information

Use subagents only within the user's and host's delegation permissions. When authorized and several substantial independent directions or verification lanes exist, useful tasks include independent question/mechanism generation, nearest-work search and adversarial review. Give generation workers shared neutral context, taste and constraints without first feeding them a preferred solution. A reviewer needs the actual candidate and supporting evidence, not a demand to endorse it.

Every task needs a concrete question, corpus/search boundary, resource/time budget, return format and stopping condition. Workers return sources with evidence status, claimed differences, objections and unknowns. The lead resolves duplicate versions, incompatible assumptions and objections; agreement is not verification. Avoid identical broad reviews or per-worker files by default.

Respect the user's model/resource instructions and actual concurrency. Do not invent unavailable agents, fixed team sizes or multi-role independence from one model merely adopting different voices. If delegation is unavailable, unauthorized or unhelpful for a narrow/dependent task, do the stages serially and identify material checks that remain unperformed. This is not permission to create user-facing sessions, schedules or unattended runs.

## Explain the idea before comparing it

Use [communication](communication.md) to explain each idea before judging it. The completeness checks above are not mandatory headings, a scorecard or a requirement to repeat the entire assessment after every reply.

Keep routine output in chat. When saving is requested, find and update the existing active topic document. Maintain one working document and, when useful, its bibliography; use existing STATUS and archive conventions. Do not create a second literature map, citation guide, progress report or per-candidate/per-agent handoff.

Selective source acknowledgments are consolidated in [community sources](community-sources.md); the previous explanation examples and communication-source acknowledgments are retained in [communication](communication.md).

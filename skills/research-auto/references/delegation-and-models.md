# Delegation, models, and cost

## Choose the work container

Before dispatch, check the existing task records and actual worker state. Give each concrete question one primary owner. Parallel routes should address distinct uncertainties or have an explicit comparison or review purpose. Reuse completed work and preserve live ownership. Record the question, owner, expected contribution and write scope in the existing state system rather than another assignment ledger.

Use a subagent for a bounded question the supervisor will integrate. A longer-lived user-visible chat needs user authorization; a skill invocation does not authorize chat creation or cross-chat messaging. Distinguish prepared work from actual dispatch.

Give each worker the project root and instructions, parent goal and module role, exact question, current evidence and relevant prior attempts, permitted assumptions/access, intended rigor, resources, owned files, and a stopping or return condition. Keep the brief compact while preserving load-bearing details. Allow alternate approaches inside scope; require a meaningful departure to be identified with its payoff and return condition.

Workers return the claim or counterexample, supporting reasoning, checked and unchecked dependencies, and its effect on the parent question. They do not stop at the first useful equation or spawn further workers without authorization. Parallel write scopes must be disjoint; the supervisor owns integration. Independent reviewers receive the candidate and raw evidence without the author's desired verdict.

Worker visibility varies by client. The supervisor filters findings into a self-contained report using the common reporting method; the user should not have to read every return. Longer-lived handoffs also specify non-goals, pending choices and the reporting channel, using actual task identifiers. Messages still require the user's authorization for that communication.

## Size substantive work packages

Assign enough continuity for a worker to develop the mechanism, close necessary dependencies, check errors, and explain algorithm or budget implications and applicable limits where relevant. Define completion for the research question, not just its first equation or supporting lemma. The brief should identify the expected result or decisive alternatives and the verification needed before returning it.

A 60–90 minute soft planning window can be a reference for substantial exploration when consistent with the user's assignment. It is not a universal default, enforced duration, or reason to delay a complete result. Adapt the scope to the deadline, resources, and time needed for independent review; narrow repairs and rechecks may be short.

Return early when the assigned question is actually solved, a decisive obstacle prevents useful progress within scope, or the applicable limit is reached. A first substantive finding may justify an interim update rather than ending the assignment. Continue the remaining main obligations while useful and authorized. Never wait artificially, add low-value branches, or pad derivations to occupy a window.

## Audit logic before numerical certificates

The independent reviewer should reconstruct the critical implication, checking missing assumptions, algebra and signs, quantifiers, constant dependencies, and parameter-choice order. Where relevant, check local domains and stopping times, global applicability, adaptivity, correlations and conditioning, information legality, endpoints, source applicability, and whether the leading term dominates the remainder. For a sufficiently-large-N claim, verify existence and the claimed scope of uniformity; do not require a concrete threshold merely to make the review look complete.

Do not default to a numerical parameter bundle, a huge grid rerun, or a computation-success verdict. If the actual proposition includes a numerical interval, finite-budget threshold, or computational proof, those claims still need their relevant checks. A preference for symbolic reasoning does not retrospectively waive required verification or turn an unproved implication into a theorem.

Return the reconstructed implication, decisive gaps or validated dependencies, and any genuinely necessary repair. A separate computation or formalization is appropriate only when it addresses an authorized proof obligation or decision; preserve unverified claims as unverified when the needed check is unavailable.

Brief reviewers to try to refute each conjecture with a counterexample or a better bound, and to check overview sentences, summary tables and comparisons with existing results against the exact source statements and line numbers; premises are most often lost there. Ask for the range of validity of numerical constants. Send the line ranges a reviewer needs rather than whole ledgers. Re-derive any new result a reviewer proposes before adding it, review it again, and mark additions not yet reviewed.

## Worker model defaults

| Work | Default model | Reasoning effort |
|---|---|---|
| New theory, constructions, proof ideas, substantive repairs | gpt-6.1-sol | ultra |
| Independent checks, counterexamples, calculations, source implications | gpt-6.1-sol | xhigh by default; high for narrowly scoped checks |

Use xhigh for audits of new central claims, complete proof arguments, or technically ambiguous dependencies. High is permitted for bounded local rechecks, straightforward calculations, or source implications with clear assumptions. Select the effort explicitly. If a check run at high uncovers a substantial unresolved issue, pass that issue to an xhigh audit within the allowed resources or report it as unresolved.

The supervisor retains its user-selected model and effort. A session name, supervisor model, or project in an example is a run parameter, not a global default. Current explicit user settings override the table.

In Claude Code, use the configured reviewer model and effort. When supported and no user preference is specified, use model `opus` with effort `high` for independent checks.

Use actual model and effort arguments when the runtime supports them. With the collaboration API, a model-specific fresh-context spawn uses:

- exploration: model=gpt-6.1-sol, reasoning_effort=ultra, fork_turns=none;
- verification: model=gpt-6.1-sol, reasoning_effort=xhigh (or high for the bounded checks above), fork_turns=none.

Use distinct task names for distinct attempts. Check that the selected model and effort are supported. If dispatch fails or selection is unavailable, preserve the prepared task and report the limit; do not silently substitute a model or claim the switch worked. Nested CLI agents, paid APIs, or user-visible chats are not fallback mechanisms without applicable user authorization.

## Spend on decisive work

For a focused bounded cycle, default to one explorer followed by one independent verifier. A pure check skips exploration and may be performed directly by its assigned reviewer; independently auditing a candidate developed during the run requires a separate reviewer. After a failed review, isolate the smallest meaningful repair and recheck changed dependencies, with one repair-and-recheck by default.

For a substantial authorized run, organize several complementary modules in rolling groups, using parallel exploration when different routes can materially change the research judgment. A bounded worker question limits that worker's task, not the whole program's ambition. Pipeline independent reviews as candidates return, and use each round's goal assessment to choose the next packages. Respect runtime limits and useful concurrency; do not fill slots, duplicate derivations or multiply expensive speculative lanes merely to appear active.

The user's latest resource instructions prevail. Never invent a numerical token budget, equate a soft prompt limit with an enforced cap, or report measured usage the runtime did not supply. Reopen a failed route only with a changed assumption, construction, argument, or piece of evidence. Rephrasing the same task is not a new attempt.

Keep the supervisor's context small: read the needed line ranges of long notes and reviews, and do not poll a running worker with scheduled wake-ups when the runtime reports completion. At a stage boundary, suggest continuing in a fresh session from the current-state record rather than relying on automatic context compaction.

Runtime details about subagent visibility and model inheritance can be checked in [OpenAI Docs](https://developers.openai.com/codex/subagents); the user's current model choice and available tools govern the actual run.

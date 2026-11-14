# Formula-First Literature Document Contract

Read this reference for a new literature report, a substantial related-work
rewrite, an application review, or a comparison where mathematical targets,
assumptions, or solver compatibility affect the conclusion.

## Default report shape

Adapt headings to the document, but make these functions easy to locate:

1. **Main Conclusions**
   - most relevant method families;
   - where the current research sits;
   - applications or uses that remain plausible;
   - decisive gaps, failure modes, and risks.
2. **Unified Setting and Notation**
3. **Method Literature**
4. **Constraint Geometry and Computational Compatibility**, when relevant
5. **Application Literature**, when relevant
6. **Evidence Gaps and Research Questions**

Use a comparison table only when cells contain comparable mathematical or
evidentiary objects. Useful columns include target, information or data,
construction, guarantee, assumptions, constraints, computational cost,
evidence level, relevance, and limitation.

## Build notation from the research question

Do not force every review into one domain-specific formalism. First identify
the objects shared across the literature:

- data, observations, states, inputs, or random variables;
- model, hypothesis, policy, estimator, or decision variables;
- objective, loss, likelihood, operator, dynamics, or governing equation;
- constraints, regularizers, priors, and admissible sets;
- population quantities, finite-sample estimators, and reported metrics;
- iteration, sample, time, layer, or experiment indices.

Prefer the current project's accepted notation. Otherwise choose one compact
notation system and map each source into it before comparison. State the map
when it prevents ambiguity; use original paper symbols only when the symbol
choice itself matters. Never let one symbol denote unrelated objects.

Representative starting points, used only when they fit the literature, are:

- **Population risk or stochastic objective**

  \[
  \min_{\theta\in\Theta}
  R(\theta)
  :=
  \mathbb E_{Z\sim P}[\ell(\theta;Z)].
  \]

- **Regularized empirical estimation**

  \[
  \widehat\theta_n
  \in
  \arg\min_{\theta\in\Theta}
  \frac{1}{n}\sum_{i=1}^n \ell(\theta;Z_i)
  +\lambda\Omega(\theta).
  \]

- **Conditional predictive model**

  \[
  p_\theta(y\mid x),
  \qquad
  \widehat y(x)
  \in
  \arg\min_{a}\mathbb E_{Y\sim p_\theta(\cdot\mid x)}
  [L(a,Y)].
  \]

- **Dynamical or control model**

  \[
  s_{t+1}=T(s_t,u_t,w_t),
  \qquad
  \min_{u_{0:T-1}}\mathbb E
  \left[\sum_{t=0}^{T-1}c(s_t,u_t)+c_T(s_T)\right].
  \]

Replace these templates with the field's actual mathematical object rather
than adding an irrelevant optimization wrapper.

## Formula-first method template

For each problem class or method family, report in this order:

1. **Research target** — the mathematical quantity, decision, prediction,
   explanation, control objective, or scientific claim.
2. **Information assumptions** — data, measurements, oracle calls, simulator,
   labels, interventions, model access, or prior knowledge.
3. **Core construction** — estimator, objective, update, architecture,
   reformulation, identification strategy, or algorithm.
4. **Guarantee or evaluation criterion** — exact metric and necessary
   assumptions.
5. **Constraint and computational support** — geometry, subproblems, scaling,
   and actual solver or implementation class.
6. **Relation to the current research** — direct reuse, missing component,
   competing target, or incompatible assumption.
7. **Limitation** — statistical, computational, modeling, identifiability,
   safety, scope, or evidence boundary.

Put the load-bearing formula before the comparison or interpretation. Do not
add equations merely to decorate a descriptive method.

## Keep targets and guarantees distinct

Do not call every result “convergence” or “performance.” Identify the object
being controlled. Common examples include:

- **Parameter or function estimation**

  \[
  \|\widehat\theta_n-\theta_\star\|,
  \qquad
  \|\widehat f_n-f_\star\|_{L^2(P)}.
  \]

- **Excess risk**

  \[
  R(\widehat\theta_n)-\inf_{\theta\in\Theta}R(\theta).
  \]

- **Optimization stationarity**

  \[
  \|\nabla R(\theta)\|,
  \]

  only for an unconstrained differentiable problem; use a gradient mapping or
  KKT residual for constrained problems.

- **Robust objective**

  \[
  \min_{\theta\in\Theta}
  \sup_{P\in\mathcal U}
  \mathbb E_{Z\sim P}[\ell(\theta;Z)].
  \]

- **Coverage or calibration**

  \[
  \mathbb P\{Y\in C_\alpha(X)\}\ge 1-\alpha,
  \]

  with the conditioning, marginal/conditional scope, and finite-sample or
  asymptotic status stated exactly.

- **Bayesian posterior predictive probability**

  \[
  p(y\mid x,\mathcal D)
  =
  \int p(y\mid x,\theta)p(\theta\mid\mathcal D)\,d\theta,
  \qquad
  \int_{C_\alpha(x)}p(y\mid x,\mathcal D)\,dy=1-\alpha.
  \]

  This is conditional on the model, prior, likelihood, and observed data; it
  is not automatically a frequentist coverage statement.

- **Ensemble prediction and empirical calibration**

  \[
  \widehat p_M(y\mid x)
  =
  \frac{1}{M}\sum_{m=1}^M p_m(y\mid x),
  \qquad
  \widehat{\mathrm{Cov}}_\alpha
  =
  \frac{1}{N}\sum_{i=1}^N
  \mathbf1\{Y_i\in\widehat C_\alpha(X_i)\}.
  \]

  A held-out empirical estimate is evidence about the evaluated sample and
  protocol, not a distribution-free guarantee by itself.

- **Online regret**

  \[
  R_T
  :=
  \sum_{t=1}^T \ell_t(\theta_t)
  -
  \min_{\theta\in\Theta}\sum_{t=1}^T\ell_t(\theta).
  \]

Separate identification from estimation, prediction from causal effect,
average performance from worst-case performance, and asymptotic guarantees
from finite-sample guarantees. Do not exchange frequentist coverage,
posterior credible probability, and empirical calibration language.

## Constraint metrics and solver compatibility

For a simple convex feasible set \(\Theta\), define the gradient mapping rather
than quoting an unconstrained gradient norm:

\[
G_\eta(\theta)
=
\frac{1}{\eta}
\left(
\theta-\Pi_{\Theta}[\theta-\eta\nabla R(\theta)]
\right).
\]

For nonlinear constraints, use a KKT residual that includes stationarity,
primal feasibility, dual feasibility, and complementarity. For mixed-integer
problems, use optimization gaps, primal/dual bounds, feasibility, or
problem-specific certificates; an ordinary gradient norm is not a solver
certificate.

| Constraint or computation | Plausible method family | Required caveat |
| --- | --- | --- |
| Box, simplex, separable budget | Projected or proximal gradient | Projection must have a cheap closed form or verified routine. |
| General convex set | Projected/proximal method, conditional gradient, conic or QP subproblem | Writing \(\Pi_\Theta\) may hide a full optimization problem. |
| Nonlinear or nonconvex constraints | SQP, interior point, augmented Lagrangian, sequential approximation, relaxation | Report feasibility and KKT-type residuals; local convergence may be all that is available. |
| Mixed-integer constraints | MILP, MINLP, decomposition, branch-and-bound, relaxation/rounding | Gradient-only methods do not enforce integrality. |
| Safety or chance constraints | Safe exploration, scenario, surrogate, robust, or constrained learning methods | Unsafe or infeasible queries may be unavailable; objective data alone may be insufficient. |
| Large models or datasets | Stochastic, distributed, low-rank, approximate, or first-order methods | Report memory, communication, approximation, and scaling assumptions. |

Judge computational compatibility as part of the literature verdict, not as an
implementation footnote.

## Application review checklist

For each candidate application, answer the questions that determine whether a
method can be used rather than merely named:

1. What is the decision, model, design, or scientific output?
2. What is its approximate dimension or scale?
3. What data, uncertainty, dynamics, or latent variables enter?
4. How do they depend on the decision, environment, intervention, or sampling
   process?
5. What is the mathematical objective or evaluation target?
6. What are the load-bearing constraints or physical/statistical assumptions?
7. Are variables continuous, discrete, structured, or mixed?
8. What does one observation, query, simulation, experiment, or deployment
   cost?
9. Can unsafe, infeasible, unethical, or invalid configurations be evaluated?
10. Do suitable data, simulators, interventions, and credible ground truth
    exist?
11. Which estimator, algorithm, or solver does the application literature
    actually use?
12. Can the current research method be used directly, or only after a narrowed
    reformulation?
13. What is the verdict: `keep`, `narrow`, `defer`, or `reject`?

Every verdict should name the decisive mathematical or evidentiary reason.

## Source evidence levels

Use the strongest available primary evidence and label weaker evidence:

- **Full-text verified:** objective, assumptions, theorem, algorithm, or
  experiment checked in the paper or official full text.
- **Official metadata verified:** title, authors, venue, year, DOI, and basic
  scope checked on the publisher or venue page.
- **Abstract-only:** only abstract-level claims are safe.
- **Search-result-only:** routing lead, not a formal claim unless independently
  verified.

Citations should support the exact nearby statement. Do not infer a theorem,
constraint class, solver, dataset result, or causal conclusion from keywords
alone.

## LaTeX validation

Use the project's existing engine and bibliography workflow. In a temporary
build when required:

1. compile enough passes for labels and citations to settle;
2. run BibTeX or Biber as configured;
3. fail on undefined citations/references and duplicate labels;
4. inspect overfull and underfull box warnings rather than hiding them;
5. render and inspect every PDF page for clipping, overlap, broken glyphs, and
   damaged tables;
6. remove `TODO`, empty sections, and reading-list placeholders.

For an explicitly source-only edit or any no-live-edit request, keep the
verified PDF in the temporary build area and update only files authorized by
the user.

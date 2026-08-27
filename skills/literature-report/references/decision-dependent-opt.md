# Decision-Dependent Optimization Literature Reviews

Read this reference only when the literature involves decision-dependent
distributions, performative prediction, decision-dependent stochastic
optimization, or an application whose uncertainty changes with the decision.

## Unified setting

Use a common notation when it fits the sources:

\[
\min_{x\in\mathcal X}
F(x)
:=
\mathbb E_{\xi\sim Q_x}[f(x;\xi)].
\]

Define:

- decision \(x\in\mathbb R^d\) and feasible set \(\mathcal X\);
- random scenario \(\xi\in\Xi\);
- decision-dependent distribution \(Q_x\);
- scenario loss \(f(x;\xi)\) and population objective \(F(x)\);
- datasets, estimators, sample sizes, and iteration indices;
- constraints \(g(x)\le0\) and \(h(x)=0\), when present.

Separate the decision used in the loss from the decision inducing the
distribution when needed:

\[
J(y\mid x)
:=
\mathbb E_{\xi\sim Q_x}[f(y;\xi)],
\qquad
F(x)=J(x\mid x).
\]

Map paper-specific symbols to this notation before comparison. Never use one
symbol for both a probability distribution and an unrelated matrix or
operator.

## Distinguish the information model

Do not group these three settings under one sampling-only label:

1. **Unknown decision-dependent distribution**

   \[
   \xi\sim Q_x,
   \qquad
   Q_x\text{ is accessible only through samples or data}.
   \]

   A method must learn an objective, gradient, response, likelihood ratio,
   feasibility probability, or another functional of \(Q_x\).

2. **Known decision-dependent uncertainty set**

   \[
   \min_{x\in\mathcal X}
   \sup_{P\in\mathcal U(x)}
   \mathbb E_{\xi\sim P}[f(x;\xi)].
   \]

   This is a robust or distributionally robust formulation, not learning an
   unknown \(Q_x\).

3. **Known push-forward model**

   \[
   \varepsilon\sim P_0,
   \qquad
   \xi=T(x,\varepsilon),
   \qquad
   F(x)=\mathbb E_{\varepsilon\sim P_0}
   [f(x;T(x,\varepsilon))].
   \]

   Reparameterization, automatic differentiation, or model-based simulation
   may be available.

State whether one query is a simulation, laboratory experiment, historical
observation, controlled intervention, or real deployment.

## Decision-dependent gradients

When differentiability and interchange assumptions are supported,

\[
\nabla F(x)
=
\left.\nabla_yJ(y\mid x)\right|_{y=x}
+
\left.\nabla_xJ(y\mid x)\right|_{y=x}.
\]

If \(Q_x\) has a differentiable density \(q_x\), a representative score-form
identity is

\[
\nabla F(x)
=
\mathbb E_{\xi\sim Q_x}
\left[
\nabla_x f(x;\xi)
+f(x;\xi)\nabla_x\log q_x(\xi)
\right].
\]

For a differentiable known push-forward,

\[
\nabla F(x)
=
\mathbb E_{\varepsilon\sim P_0}
\left[
\nabla_xf(x;T(x,\varepsilon))
+D_xT(x,\varepsilon)^\top
\nabla_\xi f(x;T(x,\varepsilon))
\right].
\]

Do not use these identities when their density, smoothness, domination, or
simulator-derivative assumptions are unavailable.

## Distinguish the target

- **Performatively stable point**

  \[
  x_{\mathrm{PS}}
  \in
  \arg\min_{y\in\mathcal X}J(y\mid x_{\mathrm{PS}}).
  \]

  A retraining fixed point need not minimize \(F(x)=J(x\mid x)\).

- **True-objective stationarity**

  \[
  \nabla F(x_\star)=0
  \]

  in the unconstrained smooth case, or an appropriate gradient mapping or KKT
  residual.

- **Robust optimum**

  \[
  x_{\mathrm{rob}}
  \in
  \arg\min_{x\in\mathcal X}
  \sup_{P\in\mathcal U(x)}
  \mathbb E_{\xi\sim P}[f(x;\xi)].
  \]

- **Online regret**

  \[
  R_T
  :=
  \sum_{t=1}^TF_t(x_t)
  -
  \min_{x\in\mathcal X}\sum_{t=1}^TF_t(x).
  \]

Identify dynamic, policy, or performative regret separately when the comparator
or environment differs.

## Application-specific questions

In addition to the general application checklist, require:

1. Why exactly does \(Q_x\) change with \(x\)?
2. Is \(Q_x\) unknown, is \(\mathcal U(x)\) known, or is
   \(\xi=T(x,\varepsilon)\) known?
3. What does one \(Q_x\) query cost?
4. Can infeasible or unsafe decisions be queried?
5. Does the literature learn only the objective, or also feasibility and
   safety?

## Power-system triage when relevant

Do not recommend power systems as one homogeneous application:

- **Simple demand-response incentives**

  \[
  \min_{0\le x\le\bar x}
  \mathbb E_{\xi\sim Q_x}[C(x,\xi)]
  \quad\text{s.t.}\quad
  \mathbf1^\top x\le B.
  \]

  Projected or proximal updates may be credible when \(x\) is an incentive
  vector, \(Q_x\) is genuinely unknown and queryable, and projection is cheap.
  Box constraints plus a sum budget form a capped-simplex or resource-allocation
  projection, not independent coordinate clipping; verify the projection
  routine and its complexity.

- **DC optimal power flow**

  \[
  p_i-d_i(x,\xi)
  =
  \sum_{j:(i,j)\in\mathcal E}
  b_{ij}(\theta_i-\theta_j),
  \qquad
  |b_{ij}(\theta_i-\theta_j)|\le\bar f_{ij},
  \qquad
  \underline p_i\le p_i\le\bar p_i.
  \]

  Projection is generally a network QP or structured solve, not clipping.

- **AC optimal power flow**

  \[
  P_i(V,\theta)
  =
  \sum_jV_iV_j
  (G_{ij}\cos\theta_{ij}+B_{ij}\sin\theta_{ij}),
  \]

  \[
  Q_i(V,\theta)
  =
  \sum_jV_iV_j
  (G_{ij}\sin\theta_{ij}-B_{ij}\cos\theta_{ij}).
  \]

  Active/reactive balance, voltage, and thermal limits form a nonlinear,
  nonconvex feasible set; NLP, relaxation, or sequential approximation is
  normally required.

- **Unit commitment**

  \[
  u_{g,t}\in\{0,1\},
  \qquad
  \underline p_gu_{g,t}\le p_{g,t}\le\bar p_gu_{g,t},
  \qquad
  -R_g^\downarrow\le p_{g,t}-p_{g,t-1}\le R_g^\uparrow,
  \]

  plus minimum up/down and startup logic. MILP, MINLP, or decomposition is
  required; a continuous gradient method addresses at most a relaxation.

Verify the response model, query cost, safety constraints, and solver used by
the actual application literature before assigning `keep`, `narrow`, `defer`,
or `reject`.

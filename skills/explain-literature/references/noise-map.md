# Noise maps: an example of precise axes

Use these distinctions for stochastic optimization or related noise questions. They are an example, not a fixed taxonomy for every field.

Define the random object first: centered oracle noise, raw stochastic gradient, optimizer update, parameter distribution, or a matrix spectrum. For oracle noise state the conditioning and filtration, e.g. g_t = grad F(x_t) + xi_t and E[xi_t | F_t] = 0 before the current sample.

## Tail or moment axis

- Finite second moment is the variance-based regime. It does not imply Gaussian or sub-Gaussian tails. Gaussian, sub-Gaussian and other finite-variance cases may be marked separately.
- A p-moment assumption for 1<p<2 permits infinite variance; it does not assert it or identify the exact tail exponent.
- Common p with different scales is different from direction-specific moment orders, including mixed finite-2/finite-p subspaces.
- A general p-moment theorem includes finite-variance distributions but may discard their stronger structure. Do not count that as adaptation to heterogeneous moment orders.

## Directional-structure axis

- With finite covariance, isotropic second-order structure means Sigma = sigma^2 I; Sigma <= sigma^2 I is only a uniform upper envelope and also allows anisotropic covariance.
- Full rotational symmetry of a distribution is stronger than isotropic covariance. State which meaning is used.
- Without covariance, use a declared notion such as rotational symmetry or equal directional p-scales. A global bound E||xi||^p <= sigma^p imposes neither.
- Distinguish a known coordinate basis, a rotated fixed subspace, time-varying subspaces, and subspaces chosen from the same samples. Diagonal covariance does not imply independent coordinates.
- Keep deterministic curvature H separate from noise geometry. A Hessian eigenspace is not automatically a noise eigenspace, and an uncentered E[gg^T] is not Cov(g).

## Information axis

Use a companion annotation rather than confusing "known in the proof" with "used by the algorithm":

- geometry and scales supplied to the algorithm;
- a coordinate basis supplied but noisy groups/scales unknown;
- unknown geometry explicitly estimated;
- unknown geometry not estimated or applied, with one scalar scheduler;
- geometry used only to state assumptions or evaluate performance;
- evidence does not establish the algorithm's information requirements.

Record whether the algorithm still needs curvature bounds, spectral counts, the tail order, noise bounds, a horizon, repeated samples at one point, or function values.

## Interpreting a 2-by-2 map

A finite-2 versus finite-p axis crossed with isotropic versus anisotropic structure is a useful main map. Put common-p/heterogeneous-scale and mixed-order cases inside the anisotropic-p cell as different subregions. Mark broad moment-envelope results as spanning or direction-unspecified rather than filling the isotropic cell by default.

For each cell state whether the evidence establishes structure, optimizes an algorithm under it, or merely provides a guarantee over a broader class. An empty cell is not a novelty certificate.

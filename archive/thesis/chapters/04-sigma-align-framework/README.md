# Chapter 4: The Σ-Align Framework

**Source**: Paper 03 — *The Σ-Align Framework* (Conceptual)
**Status**: ⚪ Not started — wait for Ch 2–3 adaptation
**Timeline**: Months 13–16
**Role**: The **conceptual centre** of the thesis (external assessment F3). The framework stands
or falls on the operational definition of σ.

## Operational Specification of σ (required — CC.3.4)

The chapter must fully specify:

- **Construct**: what exactly is being measured (degree of internal consistency of representation structure).
- **Unit**: the object whose coherence is measured — neuron / layer / representation / latent space / model / task-conditioned representation / trajectory through representation space.
- **Metric**: the mathematical quantity giving σ (e.g. spectral measure, representational-similarity statistic, rank-collapse index — `code/sigma_align/ode/` provides the dynamical-system context).
- **Range**: e.g. σ ∈ [0,1] or σ ∈ ℝ — stated explicitly.
- **Invariance**: behaviour under rotation, permutation, scaling, reparameterisation, representation-basis changes. A metric that changes merely because the latent basis rotates is not measuring a meaningful model property.

Also required: a precise definition of the **σ-trap** (stable low-σ regime) and the **σcrit**
bifurcation threshold, consistent with the notation registry (`back-matter/notation-registry.tex`).

## Construct-Validity Tests (required — assessment F3)

1. **Convergent validity** — σ correlates with other measures that should reflect coherent structure.
2. **Discriminant validity** — σ is distinct from accuracy, robustness, interpretability, simplicity, mutual information, representational similarity, and compositionality itself.
3. **Predictive validity** — σ predicts unseen compositional generalisation.
4. **Intervention validity** — manipulating σ changes the predicted outcome.

The chapter also states the **falsifiability conditions** of the mechanism claim (see
`Σ-Align/13-external-assessment-response.md`): e.g. a low-σ regime with intact systematic
generalisation falsifies the primary claim.

See `phases/` for chapter phase roadmaps (to be created).

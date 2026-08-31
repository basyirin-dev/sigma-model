# Preregistered Study Protocol & Hypotheses (RPF v2.0)

- **Date:** 2026-08-24
- **Status:** DRAFT (Targeting Human Gate `HG-01` sign-off in Phase P03)
- **Protocol ID:** `PREREG-SIGMA-2026-01`

---

## 1. Primary Hypotheses

### Hypothesis H1 ($\sigma$-Trap Formation)
Standard cross-entropy gradient descent on multi-step compositional tasks causes representation depth $D(t)$ to grow exponentially faster than schema coherence $S(t)$, leading to an asymptotic equilibrium where $S(\infty) < S_{crit}$.

- **Falsification Threshold:** If $\ge 20\%$ of standard runs achieve $S(t) \ge S_{crit}$ without explicit structural intervention, H1 is falsified.

### Hypothesis H2 (Two-Subspace Orthogonality)
Representation spaces under compositional pressure decompose into two orthogonal geometric subspaces: a syntax subspace $\mathcal{V}_{syn}$ and a semantic schema subspace $\mathcal{V}_{sem}$, such that the principal subspace angle $\cos \theta(\mathcal{V}_{syn}, \mathcal{V}_{sem}) < 0.15$.

- **Falsification Threshold:** If the principal subspace cosine similarity remains $\ge 0.35$ across all trained layers, H2 is falsified.

---

## 2. Statistical Analysis Plan

- **Sample Size:** $N \ge 5$ distinct pre-registered random seeds per condition.
- **Significance Level:** $\alpha = 0.01$ (with Bonferroni / Benjamini-Hochberg FDR correction across multi-benchmark sweeps).
- **Statistical Tests:** Two-sided Welch's t-test and Two One-Sided Tests (TOST) for equivalence testing.
- **Power Target:** $1 - \beta \ge 0.90$ for effect size Cohen's $d \ge 0.8$.

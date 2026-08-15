# Statistical Power Analysis for N=500 Brittle Domain Experiment

> **Source**: Statistical methodology review using DeepSearch AI (Jun 2026)
> **Purpose**: Fix the OSF pre-registration protocol before any data collection. Informs C.2 (pre-registration draft).

---

## Overview

**Research design**: N=500 runs of a transformer language model trained on Pfam domain architecture sequences, split across 3 conditions (familiar combinations, new family recombinations, cross-clan recombinations). Primary hypothesis test: Welch's t-test comparing high σ_A vs low σ_A groups on OOD accuracy, with Bonferroni correction for 8 comparisons (α = 0.00625). Expected effect size: Cohen's d ≥ 0.5.

**Six design decisions** addressed below verify adequacy, recommend optimal choices, quantify risks, propose robustness checks, and evaluate whether dichotomisation is the best approach.

---

## 1. Power Verification

### 1.1 Analytic Approximation

For a two-sided Welch's t-test with equal group sizes, required n per group:

$$n_{\text{per group}} \approx \frac{2\,(z_{1-\alpha/2} + z_{1-\beta})^{2}}{d^{2}}$$

With α = 0.00625, d = 0.5, target power 0.80:
- $z_{1-\alpha/2} = z_{0.996875} \approx 2.738$
- $z_{1-\beta} = z_{0.80} \approx 0.842$
- $n_{\text{per group}} \approx 2(2.738 + 0.842)^2 / 0.25 \approx \mathbf{103}$ per group, **206 total**.

### 1.2 Power at N=500 (Pooled Across Conditions)

If all 500 runs enter the primary comparison (250 / 250):
- Noncentrality δ = d√(n/2) = 0.5√125 ≈ 5.59
- Power ≈ Φ(δ − z_{1−α/2}) = Φ(5.59 − 2.738) = Φ(2.85) ≈ **0.998**

✅ **N = 500 is far more than sufficient when pooled** — actual power ≈ 99.8%, well above the 80% target.

### 1.3 Critical Caveat: "Split Across 3 Conditions"

If the primary t-test is conducted **within a single condition** (i.e., 500/3 ≈ 167 runs, ≈ 83 per σ_A group):
- δ = 0.5√41.5 ≈ 3.22
- Power ≈ Φ(3.22 − 2.738) = Φ(0.48) ≈ **0.685** — **below 80%**.

To achieve 80% power per condition under Bonferroni at α = 0.00625, you would need ≈ 206 runs per condition, i.e., ≈ 618 total.

**Recommendation**: Pre-register which interpretation is the target. If per-condition, either (a) increase N, (b) reduce the number of Bonferroni-corrected comparisons (e.g., via hierarchical/linear-model F-tests), or (c) use a less conservative correction (Holm–Bonferroni, Hochberg, or FDR-controlled procedure).

---

## 2. Optimal Allocation Ratio (High vs Low σ_A)

**Recommendation: 1:1 allocation (250/250), unless pilot data indicate substantial variance heterogeneity.**

| Factor | Guidance |
|--------|----------|
| Under homoscedasticity | Equal allocation maximises noncentrality δ = d√(n₁n₂/(n₁+n₂)) |
| Under heteroscedasticity | Neyman allocation n₁/n₂ = σ₁/σ₂ is variance-minimising |
| Practical rule | Default 1:1; if pilot data suggest σ_high/σ_low ≈ r > 1.5, deviate toward Neyman allocation and pre-register the ratio and its justification |

Welch's t-test corrects degrees of freedom for unequal variances but does not protect against power loss from suboptimal allocation.

---

## 3. Assumptions and Robustness Checks

### 3.1 Assumptions of Welch's t-test

| Assumption | Risk in This Design | Mitigation |
|------------|---------------------|------------|
| Independence of observations | **High** — runs may share random seeds, model initialisations, or hyperparameter sweeps | Block/cluster bootstrap; mixed-effects model with random effect for seed/run |
| Normality of sampling distribution | Low at n ≈ 250 via CLT, but OOD accuracy bounded [0,1] can be heavy-tailed | Inspect Q–Q plots; consider logit transform if accuracy near 0 or 1 |
| Homoscedasticity | Not assumed by Welch's — still report group SDs and variance ratio | No mitigation needed beyond reporting |
| No extreme outliers | Moderate — OOD generalisation can produce failure modes | Report analyses with and without outliers; pre-register exclusion rule |

### 3.2 Pre-Registered Robustness Checks

All seven should be pre-registered:

1. **Mann–Whitney U** — distribution-free alternative
2. **Permutation test** (10⁵ permutations) — exact Type I error control under exchangeability
3. **Yuen's trimmed-mean t-test** (20% trimming) — robust to skew and outliers
4. **Cluster bootstrap** — if runs are nested within seeds/configs
5. **Bootstrap 95% CI** for Cohen's d (bias-corrected and accelerated)
6. **Sensitivity analysis** — report results dropping top/bottom 1% of OOD accuracy
7. **Visual diagnostics** — histograms, violin plots, Q–Q plots per group (supplementary)

---

## 4. Bayesian Secondary Analysis Plan

**Recommendation**: Use the BEST framework (Kruschke, 2013) — Bayesian Estimation Supersedes the t-test.

### Model

$$y_i \sim \text{Student-}t(\nu, \mu_{g[i]}, \sigma_{g[i]}), \quad g \in \{\text{high}, \text{low}\}$$

### Priors (Weakly Informative)

| Parameter | Prior | Rationale |
|-----------|-------|-----------|
| μ_g | N(ȳ, 2s_y) | Broad, centred on grand mean |
| σ_g | Half-Cauchy(0, s_y) | Half-Cauchy on group SDs |
| ν | Gamma(2, 0.1) | Favours heavier tails a priori; lets data speak |

### Quantities of Interest

- Δ = μ_high − μ_low (raw difference)
- δ_Bayes = Δ / σ̃ (standardised effect using pooled robust SD)

### Inference and Decision Rule

- Sample 4 chains × 4,000 iterations (Stan/PyMC); verify R̂ < 1.01, ESS > 1000
- Report 95% highest-density interval (HDI) for Δ and δ_Bayes
- **Practical-decision rule**: Declare a meaningful effect if the 95% HDI of δ_Bayes excludes the ROPE [−0.1, +0.1]
- Optionally: Savage–Dickey Bayes Factor for H₀: Δ = 0 vs H₁

### Why This Complements the Frequentist Test

- Yields magnitude with uncertainty (not just reject/accept)
- Robust to non-normality via Student-t likelihood
- Naturally accommodates heteroscedasticity by estimating separate σ_g
- The ROPE decision rule avoids the problems of null-hypothesis significance testing

---

## 5. Split Rule: Median vs Quantile-Based

**Recommendation: use a median split if dichotomisation is unavoidable.**

| Criterion | Median Split | Extreme-Quantile (e.g., top/bottom tertile) |
|-----------|-------------|---------------------------------------------|
| Sample size retained | 100% (250/250) | ~67% (167/167) |
| Statistical power | Higher (99.8%) | Lower (~95%) |
| Effect-size inflation | Moderate | Larger (extreme groups) |
| Reproducibility | Median is unique and stable | Quantile cutpoints are noisier |
| Selection bias | None | Excludes middle — non-representative |

At α = 0.00625, the power cost of dropping the middle tertile is acceptable in pure power terms but creates interpretational problems: the "effect" becomes a contrast between extremes, not a population-level statement. Median split is more defensible for a pre-registered primary analysis.

---

## 6. Beyond Dichotomisation: Continuous σ_A Predictor

**Strongest recommendation in this report: replace dichotomisation with regression using σ_A as a continuous predictor.**

### Why Dichotomisation Is Suboptimal

MacCallum et al. (2002) showed that median splitting a continuous predictor costs up to **~33% loss of statistical power** — equivalent to throwing away a third of data. Additional problems:

- **Arbitrary threshold** θ_σ — different choices yield different significance decisions (Maxwell & Delaney, 1993)
- **Inflated Type I error** when cutpoint is chosen post hoc
- **Loss of information about functional form** — cannot detect non-linear or threshold effects
- **Spurious interaction effects** when both predictors in an interaction are dichotomised

### Recommended Alternative: Continuous Regression

**Primary model**: linear regression (or beta regression if OOD accuracy is near 0 or 1)

$$\text{OOD\_acc}_i = \beta_0 + \beta_1 \sigma_{A,i} + \beta_2 \text{Condition}_i + \beta_3(\sigma_{A,i} \times \text{Condition}_i) + \varepsilon_i$$

- Test H₀: β₁ = 0 (main effect of σ_A) — replaces the t-test, with Bonferroni applied across 8 coefficient tests
- Interaction term β₃ directly tests whether the σ_A → OOD accuracy slope differs across conditions — eliminating the need for separate per-condition t-tests and **reducing the comparison family**
- Report standardised slope β₁* and its 95% CI as the effect size

### Approach Comparison

| Approach | Power vs Continuous | Threshold Arbitrariness | Detects Nonlinearity | Comparisons |
|----------|--------------------|------------------------|---------------------|-------------|
| Median split + t-test | −33% | Yes (median) | No | 8 |
| Extreme quantile + t-test | −60% | Yes | No | 8 |
| **Linear regression on σ_A** | **Reference (best)** | **No** | **With splines** | 8 or fewer |
| GAM (spline on σ_A) | Slightly less | No | Yes | 8 |
| Piecewise/segmented | Comparable | Pre-registered breakpoint | Yes | 8 |

### Recommended Hybrid Pre-Registration

1. **Primary analysis**: linear regression with σ_A as continuous predictor, Bonferroni across 8 pre-specified coefficient tests. Most powerful and least arbitrary.
2. **Secondary analysis**: median-split t-test (as originally planned) — included for comparability with prior literature.
3. **Exploratory**: GAM or segmented regression to detect non-linear / threshold effects of σ_A (e.g., a phase transition in generalisation).
4. If a theoretical phase-transition threshold θ_σ exists a priori, pre-register it and use a piecewise model with that breakpoint — never fit-and-then-report.

---

## 7. Summary of Recommendations

| Question | Recommendation |
|----------|---------------|
| (1) Is N=500 sufficient? | **Yes** if pooled across conditions (~99.8% power). **No** if per-condition (~68%) — increase N to ~620 or reduce comparison family. |
| (2) Allocation ratio | **1:1 (250/250)** unless pilot data justify Neyman allocation. |
| (3) Assumptions & robustness | Independence is highest risk. Pre-register all 7 robustness checks (Mann–Whitney, permutation, Yuen, cluster bootstrap, bootstrap CI, sensitivity, diagnostics). |
| (4) Bayesian plan | BEST framework (Student-t likelihood, separate σ_g, ν prior). 95% HDI with ROPE [−0.1, +0.1] decision rule. |
| (5) Split rule | If dichotomising, **median split** (maximises n, reproducibility, interpretability). |
| (6) Continuous vs dichotomous | **Linear regression on continuous σ_A as primary analysis**. Retains ~33% power, removes threshold arbitrariness, unifies 3 conditions into a single interaction model. Retain t-test as secondary only. |

---

## 8. Implications for OSF Pre-Registration (C.2)

The six design decisions above directly populate the OSF pre-registration's Analysis Plan section. Key action items for C.2:

1. **Resolve the "split across 3 conditions" ambiguity** — specify in the pre-registration whether the primary test is pooled or per-condition
2. **Swap primary analysis to continuous regression** — this is the single most impactful change; the pre-registration should describe the linear model and its coefficients
3. **Pre-register all 7 robustness checks** — each with its own criterion for when it supersedes the primary analysis
4. **Add the Bayesian (BEST) plan as secondary analysis** — include the ROPE decision rule
5. **Specify median split (not extreme quantile)** for the secondary t-test analysis
6. **Document the power analysis** — cite the 99.8% pooled / 68% per-condition figures and the pre-registered resolution

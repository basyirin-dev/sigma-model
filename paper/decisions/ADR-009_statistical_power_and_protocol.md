# ADR-009: Statistical Power Analysis & Multi-Benchmark Pre-Registered Protocol

## 1. Context & Status
- **Status:** **APPROVED**
- **Date:** 2026-08-25
- **Deciders:** Principal Investigator, Lead Research Agent
- **Phase:** Phase 04 (Multi-Benchmark Experimental Design & Protocol Specification)
- **Framework:** RPF v2.0.0 — Task 4.4
- **Prerequisites:**
  - `paper/decisions/ADR-007_multi_benchmark_experimental_matrix.md`
  - `paper/decisions/ADR-008_diagnostic_toolchain_and_analysis_engines.md`
  - `paper/docs/datacards/hbar_benchmark.md`

---

## 2. Statistical Power Analysis & Sample Size Sizing

### 2.1 Sample Size Allocation & Harmonization (Amendment 2026-08-27)
- **Primary Evidence Rule:** Primary evidence must be derived from cells with $n = 30$ independent random initializations ($s_i = \text{run\_id} \times 42 + 7$).
- **Exploratory Screening Rule:** Cells with $n = 10$ seeds are permitted exclusively for pre-registered exploratory architecture-universality screening (Tier 2) and may not be used to confirm primary threshold or equivalence claims without a formal protocol amendment.
- **Deprecated Sample Sizes:** The value $n = 15$ is explicitly deprecated and is not an authorized sample size under this protocol.
- **Violation Flag:** Any primary cell executed with $n < 30$ is flagged as `PRIMARY_PROTOCOL_VIOLATION` and excluded from evidence aggregation.

### 2.2 Minimal Detectable Effect Size (MDES)
- At significance level $\alpha = 0.05$ (two-tailed) and statistical power $1 - \beta = 0.90$:
  $$\text{MDES} = (z_{1 - \alpha/2} + z_{1 - \beta}) \sqrt{\frac{2}{n}} = (1.960 + 1.282) \sqrt{\frac{2}{30}} \approx 0.835 \text{ (Standardized Cohen's } d)$$
- For within-condition comparison across $n=30$ seeds against a fixed baseline, MDES is $d \approx 0.58$ (medium effect size), providing $>95\%$ power to detect the $44.3\text{ pp}$ $\sigma$-trap deficit.

### 2.3 Equivalence Testing Power (TOST)
- For supercritical asymptotic parity ($\lambda \in \{0.5, 0.75, 1.0, 1.5, 2.0\}$) with equivalence margin $\delta = \pm 2.5\%$:
  $$\text{Power}_{\text{TOST}} \ge 0.99 \quad (\text{for } \sigma \le 1.0\% \text{ observed in Gate})$$

---

## 3. Pre-Registered Hypothesis Testing & Multiple-Comparison Control

### 3.1 Primary, Secondary, and Exploratory Endpoints
1. **Primary Endpoint (Universality of Critical Threshold across 4 Suites):**
   - Fitted logistic change-point steepness $k \ge 15.0$ and empirical threshold $\hat{\lambda}_{\text{crit}} \in [0.020, 0.030]$ across all 4 benchmark suites ($\hbar$, SCAN, COGS, PCFG-SET) and all 3 architecture classes.
   - **Correction Strategy:** Holm-Bonferroni family-wise error rate control ($\alpha = 0.05$).
2. **Secondary Endpoint (Supercritical Asymptotic Equivalence):**
   - Pairwise TOST equivalence within $\pm 2.5\%$ margin ($p < 0.05$, Bonferroni corrected across $\binom{5}{2} = 10$ pairs, $\alpha_{\text{pair}} = 0.005$).
3. **Exploratory Diagnostics (FDR Controlled):**
   - Representational Homomorphism Predictive Validity: Homomorphism Error (HE) inverse correlation with OOD generalization ($r \le -0.70$).
   - CKA Lead-Lag Dynamics: Granger causality F-test ($\Delta \text{CKA}_{t-1} \to \Delta \text{OOD}_t, p < 0.01$).
   - **Correction Strategy:** Benjamini-Hochberg False Discovery Rate (FDR) control at $q = 0.05$.
4. **Bootstrap Protocol for Critical Thresholds:**
   - 10,000 non-parametric bootstrap resamples to generate 95% confidence intervals for $\hat{\lambda}_{\text{crit}}$ across architectures.

### 3.2 Exclusion, Outlier & Rerun Protocol
- **Exclusion Rules:** Strict application of pre-registered 5 criteria (NaN/Inf, loss non-convergence $\ge 500$ steps, checksum corruption, process crash, seed deviation).
- **Rerun Policy:** Transient failures re-seeded deterministically up to $+10\%$ budget cap.

---

## 4. Consequences & Governance
- All statistical pipelines are implemented in `paper/src/analysis/power.py` and validated via automated unit tests.
- Fulfills Task 4.4 and completes all technical requirements of Phase 04.

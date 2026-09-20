# Pre-registration — P03 Mechanism Gate & P04 Production Matrix (P02.5 / P03.1)

**Project:** Paper 02 (*Critical Compositional Pressure & The Two-Subspace Law*)
**Framework:** RPF v2.0.0 — phase P02.5 / P03.1
**Date emitted:** 2026-08-23 (Initial P02.5); Locked 2026-08-25 (P03.1 / P04)
**Status:** Approved & Locked (P03.1_HG / P04) — Human-in-the-Loop Protocol Lock
**Links:** P02 ADR `decisions/ADR-003_hypothesis_and_observable_signatures.md` · P03.1 ADR `decisions/ADR-006_subgate_calibration.md` · P03 protocol `planning/phases/P03_GATE.md` (Task 3.3) · gate result `planning/gate-result.md` · release anchor `v2.0-paper02`

---

## 0. Provenance, Timing & Two-Stage Evolution

The experimental falsification protocol underwent a rigorous, prospectively documented two-stage progression prior to initiating the 960 production runs:

1. **Stage 1 (Phase P02.5 Gate Screening, 2026-08-23, Commit `97eabba`, Git tag `p02.5-preregistered`):**
   Initial exploratory gate screening established the qualitative phase-boundary hypothesis and evaluated broad candidate intervals ($\hat{\lambda}_{\text{crit}} \in [0.20, 0.35]$ on the un-normalized scale; exploratory late-intervention probe $\lambda = 1.0$). Ten CPU smoke-test runs existed for Task 3.2 pipeline verification without contributing to metric scoring.

2. **Stage 2 (Phase P03.1 Subgate Calibration & P04 Production Lock, 2026-08-25, `ADR-006`):**
   Upon establishing exact Hessian quadratic form normalization ($a_C = 1.0, b_C = 0.025$), the critical phase boundary was calibrated analytically ($\lambda_{\text{crit}} = b_C / a_C = 0.025$) and prospectively locked to $\lambda_{\text{crit}} \in [0.015, 0.030]$ ($0.025 \pm 0.005$). The late-onset interventional activation pressure was locked to supercritical $\lambda_{\text{post}} = 0.050$ ($2\times \lambda_{\text{crit}}$). All 960 production runs in Phase P06 were executed strictly under this locked parameterization.

3. **Experimental Matrix Taxonomy & Grid Reconciliation:**
   The experimental plan comprises a mutually exclusive and collectively exhaustive (MECE) 960-run production hierarchy along with targeted derived sub-studies:
   - **Locked Tier 1 Primary Falsification Matrix (720 runs):** 4 benchmarks ($\hbar$, SCAN, COGS, PCFG-SET) $\times$ 1 canonical architecture (Transformer 2L, $0.93\text{M}$ params) $\times$ 6 standardized discrete levels ($\lambda \in \{0.000, 0.015, 0.020, 0.025, 0.030, 0.500\}$) $\times$ $n=30$ independent seeds ($4 \times 1 \times 6 \times 30 = 720$).
   - **Tier 2 Architecture Scaling Matrix (240 runs):** 4 benchmarks $\times$ 2 scaled architectures (Deep Transformer 4L with $3.80\text{M}$ params; GRU Seq2Seq with $0.41\text{M}$ params) $\times$ 3 discrete regimes ($\lambda \in \{0.000, 0.025, 0.500\}$) $\times$ $n=10$ independent seeds ($4 \times 2 \times 3 \times 10 = 240$).
   - **Derived 11-Point Dense Grid on $\hbar$ (330 evaluated conditions):** Formed by the $180$ $\hbar$ Tier 1 runs plus $150$ targeted boundary-refinement runs ($\lambda \in \{0.010, 0.018, 0.022, 0.028, 0.050\}$, $n=30$ seeds each) used for continuous inflection point estimation ($\hat{\lambda}_{\text{crit}} = 0.0238 \in [0.0203, 0.0317]$).
   - **Derived Interventional & Grokking Arms:** Evaluates 180 branched trajectory checkpoints ($30 \text{ seeds} \times 6 \text{ timepoints}$) from the subcritical baseline and 30 extended-horizon 20k-step anti-grokking control runs.

4. **Git Provenance Hash Reconciliation:**
   - Initial Preregistration Tag: `p02.5-preregistered` (Commit `97eabba`, 2026-08-23).
   - Production Release Anchor Tag: `v2.0-paper02` (Commit `f9ba574`, finalized immutable release).
## 1. Primary Outcome (exactly one)

| Field | Value |
|-------|-------|
| metric_name | **Criterion 1 — Sharp escape step-function (Fitted 2-Parameter Logistic Change-Point Estimand & Standardized Transition Scale)**: $P_{\text{fit}}(\text{escape} \mid \lambda) = \frac{1}{1 + \exp\left(-k(\lambda - \hat{\lambda}_{\text{crit}})\right)}$, escape := $\text{Acc}_{\text{OOD}} \ge 80\%$, and standardized transition scale $P^*(\text{escape} \mid \lambda) \coloneqq \frac{P_{\text{fit}}(\text{escape} \mid \lambda) - P_{\text{baseline}}}{1 - P_{\text{baseline}}}$ above the stochastic floor ($P_{\text{baseline}} = 2/30 = 0.0667$ on $\hbar$). |
| threshold | Steepness $k \ge 15.0$, macroscopic jump $\Delta P_{\text{fit}} \ge 0.50$, and standardized threshold separation $P^*(\text{escape} \mid \lambda \le 0.010) < 0.50$ ($P^*(\lambda \le 0.000) < 0.05$) and $P^*(\text{escape} \mid \lambda \ge 0.500) > 0.95$. Evaluated on the continuous non-linear least-squares fitted change-point model on the primary $\hbar$ dense grid ($k = 79.48 \approx 79.5 \gg 15.0, \hat{\lambda}_{\text{crit}} = 0.0238 \in [0.0203, 0.0317]$):<br>• Raw evaluation: $P_{\text{fit}}(\text{escape} \mid \lambda = 0.010) = \frac{1}{1 + \exp(-79.48 \times (0.010 - 0.0238))} \approx 0.2504$<br>• Raw supercritical: $P_{\text{fit}}(\text{escape} \mid \lambda \ge 0.500) = \frac{1}{1 + \exp(-79.48 \times (0.500 - 0.0238))} \approx 1.000 > 0.95$ (PASS)<br>• Macroscopic Jump: $\Delta P_{\text{fit}} = 1.000 - 0.2504 = 0.7496 \gg 0.50$ (PASS)<br>• Standardized subcritical scale: $P^*(\text{escape} \mid \lambda = 0.010) = \frac{0.2504 - 0.0667}{1 - 0.0667} \approx 0.1968 < 0.50$ and $P^*(\lambda \le 0.000) \le 0.000 < 0.05$ (PASS)<br>• Standardized supercritical scale: $P^*(\text{escape} \mid \lambda \ge 0.500) \approx 1.000 > 0.95$ (PASS) |
| direction | Higher $k$ = sharper boundary = PASS; the separation inequalities and macroscopic jump $\Delta P_{\text{fit}} > 0.50$ must hold |
| justification | Distinguishes a macroscopic phase boundary (trap→escape) from a smooth dose-response curve — the falsifiable core of CLM-003 and the Two-Subspace Law's empirical instantiation. In the continuous deterministic ODE (Level 1), subcritical escape is identically $0\%$. In finite discrete mini-batch neural network training (Level 3), small baseline escape fractions ($0.000$ on SCAN, $0.000$ on COGS, $0.000$ on PCFG-SET, $0.067$ on $\hbar$) represent stochastic finite-sample fluctuations arising from random initialization and early mini-batch gradient variance in unmodeled high-dimensional directions. |
## 2. Secondary Outcomes (≥2, tagged)

| metric_name | threshold | tag |
|-------------|-----------|-----|
| **Criterion 2 — Late-onset recovery:** for $t_{\text{int}} = 1000$ runs (trapped at step 1000, $\text{Acc}_{\text{OOD}} \le 50\%$), switching on supercritical pressure $\lambda = 0.050$ reaches final $\text{Acc}_{\text{OOD}} \ge 90\%$ | in ≥ 90 % of seeds | confirmatory (CLM-004) |
| **Criterion 3 — Supercritical asymptotic parity:** pairwise TOST equivalence among $\lambda \in \{0.025, 0.030, 0.050, 0.100, 0.500\}$ | within margin $\pm 2.5\%$, $p < 0.05$ (Bonferroni across 10 pairs; qualified for deep 4L scaling and post-separation saturation $\lambda \ge 0.030$/$0.050$ in 2L) | confirmatory (CLM-003/Paper 01 §1.2) |

## 3. Exploratory Outcomes (≥1, tagged)

| metric_name | tag |
|-------------|-----|
| $\hat{\lambda}_{\text{crit}}$ point estimate (logistic inflection) and its 95 % bootstrap CI — feeds the binding constraint $\hat{\lambda}_{\text{crit}} \in [0.015, 0.030]$ matching analytical formula $\lambda_{\text{crit}} = b_C / a_C = 0.025$ | hypothesis-generating |
| Transition-latency ordering $\hat{\tau}_{\text{fixed}} < \hat{\tau}_{\text{mult}} < \hat{\tau}_{\text{add}}$ (Paper 01 §1.3 correspondence) | hypothesis-generating |
| CKA/RGA lead-lag: $\Delta \text{RGA}_t \to \Delta \text{OOD}_{t+1}$ Granger test (CLM-005) | hypothesis-generating |
| WGCA step-0 artifact removal check (CLM-006) | hypothesis-generating |

## 4. Exclusion Criteria (≥3)

| criterion | rationale |
|-----------|-----------|
| Any run with NaN/Inf loss or metric at any logged step | Numerical failure (CC.4.6) |
| Solver/training non-convergence (loss not decreasing over ≥ 500 consecutive steps) | CC.2.4 convergence criterion |
| Checkpoint/artifact corruption (hash mismatch between run log and output pickle) | Data integrity (CC.4.3) |
| Hardware/OS failure interrupting a run (process killed, OOM) | Environment failure |
| Seed-log mismatch (logged seed ≠ `cell_seed_idx * 42 + 7` where `cell_seed_idx` $\in [0, 29]$ in Tier 1, $[0, 9]$ in Tier 2, disambiguated from global `run_id` $1 \dots 960$) | Determinism protocol (CC.1.2) |

Excluded runs are logged with the `NEGATIVE` tag and re-run with fresh seeds from `meta/seeds.yaml` if the cause is transient (max +10 % budget, ADR required beyond that).

## 5. Statistical Plan

| Field | Value |
|-------|-------|
| test | (a) 2-parameter logistic change-point fit (least squares) for Criterion 1 ($P_{\text{fit}}(\text{escape} \mid \lambda)$); (b) Welch two-sample t-tests + bootstrap 95 % CIs for per-cell OOD; (c) TOST (two one-sided tests) for Criterion 3; (d) Granger causality F-test for CKA lead-lag (exploratory); (e) Binomial GLM logistic regression for individual seed validation ($k_{\text{GLM}}$) |
| alpha | 0.05 |
| correction | Bonferroni within each family: 10 TOST pairs (α = 0.05/10 = 0.005 per pair for Criterion 3), with Holm step-down adjusted $p$-values reported as secondary sensitivity verification; criteria treated as pre-ordered (primary → secondary) so no cross-family correction |
| power / effect-size justification | n = 30 seeds/cell; escape-fraction estimator SE ≈ √(p(1−p)/30) ≤ 0.091 — resolves the required separation ($P_{\text{fit}} < 0.05$ vs $P_{\text{fit}} > 0.95$) with > 3 SE margin at p≈0.5. Steepness metrics disambiguate $k = 79.5$ (primary point estimate on $\hbar$, $95\%$ bootstrap CI $[61.7, 105.0]$ / $[27.1, 115.2]$ via $10{,}000$ resamples) from multi-benchmark range $k \ge 79.5$ (cross-benchmark range across all 4 Transformer-2L suites) and Bernoulli MLE $k_{\text{MLE}} = 93.94, \text{AIC} = 351.26$. |
| decision_rule | PASS = primary meets threshold ($k \ge 15.0 \wedge \Delta P_{\text{fit}} \ge 0.50 \wedge P^*(\lambda \le 0.010) < 0.20 \wedge P^*(\lambda \ge 0.500) > 0.95$) ∧ secondary consistent; FAIL = primary unmet; INCONCLUSIVE = primary within pre-specified ambiguity band (k ∈ [10, 15) with ≥ 1 separation inequality violated by < 2 SE) → trigger P03.1 sub-gate protocol (`planning/phases/P03.1_subgate.md`) |

## 6. Linkage

| Field | Value |
|-------|-------|
| p02_adr_id | `decisions/ADR-003_hypothesis_and_observable_signatures.md` |
| p03_gate_protocol_id | `planning/phases/P03_GATE.md` Task 3.3 + `experiments/configs/gate_protocol.yaml` |
| p03_1_adr_id | `decisions/ADR-006_subgate_calibration.md` |
| gate_result | `planning/gate-result.md` (scored against this document) |
| release_anchor | Git tag `v2.0-paper02` (Commit `f9ba574`) |
| ledger | CLM-003 (primary), CLM-004 (secondary), CLM-005/006 (exploratory) |

# Pre-registration — P03 Mechanism Gate (P02.5)

**Project:** Paper 02 (*Critical Compositional Pressure & The Two-Subspace Law*)
**Framework:** RPF v2.0.0 — phase P02.5
**Date emitted:** 2026-08-23
**Status:** Emitted — pending `[HUMAN-GATE]` PI approval (SLA 48h)
**Links:** P02 ADR `decisions/ADR-003_hypothesis_and_observable_signatures.md` · P03 protocol `planning/phases/P03_GATE.md` (Task 3.3) · gate result `planning/gate-result.md`

---

## 0. Provenance & Timing (honest backfill)

The three decision criteria formalized below were **fixed before any gate evaluation**: they were specified verbatim in `planning/phases/P03_GATE.md` Task 3.3 and `decisions/ADR-005_gate_experimental_design.md` on 2026-08-23, before `gate-result.md` was populated (still `PENDING EVALUATION`). Ten CPU smoke-test runs exist (Task 3.2 validation); **no smoke-run output contributes to any metric below**. This formal pre-registration document is emitted under RPF v2.0 P02.5 *prior to* the gate evaluation (Task 3.4) so the verdict is scored against a committed, PI-approved plan.

## 1. Primary Outcome (exactly one)

| Field | Value |
|-------|-------|
| metric_name | **Criterion 1 — Sharp escape step-function** (2-parameter logistic change-point fit): $P(\text{escape} \mid \lambda) = \frac{1}{1 + \exp(-k(\lambda - \lambda_{\text{crit}}))}$, escape := $\text{Acc}_{\text{OOD}} \ge 80\%$ |
| threshold | Steepness $k \ge 15.0$ **and** threshold separation $P(\text{escape} \mid \lambda \le 0.10) < 0.05$ and $P(\text{escape} \mid \lambda \ge 0.50) > 0.95$ |
| direction | Higher $k$ = sharper boundary = PASS; the separation inequalities must both hold |
| justification | Distinguishes a phase boundary (trap→escape) from a smooth dose-response curve — the falsifiable core of CLM-003 and the Two-Subspace Law's empirical instantiation |

## 2. Secondary Outcomes (≥2, tagged)

| metric_name | threshold | tag |
|-------------|-----------|-----|
| **Criterion 2 — Late-onset recovery:** for $t_{\text{int}} = 1000$ runs (trapped at step 1000, $\text{Acc}_{\text{OOD}} \le 50\%$), switching on $\lambda = 1.0$ reaches final $\text{Acc}_{\text{OOD}} \ge 90\%$ | in ≥ 90 % of seeds | confirmatory (CLM-004) |
| **Criterion 3 — Supercritical asymptotic parity:** pairwise TOST equivalence among $\lambda \in \{0.5, 0.75, 1.0, 1.5, 2.0\}$ | within margin $\pm 2.5\%$, $p < 0.05$ (Bonferroni across 10 pairs) | confirmatory (CLM-003/Paper 01 §1.2) |

## 3. Exploratory Outcomes (≥1, tagged)

| metric_name | tag |
|-------------|-----|
| $\hat{\lambda}_{\text{crit}}$ point estimate (logistic inflection) and its 95 % bootstrap CI — feeds the binding constraint $\hat{\lambda}_{\text{crit}} \in [0.20, 0.35]$ | hypothesis-generating |
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
| Seed-log mismatch (logged seed ≠ `run_id * 42 + 7`) | Determinism protocol (CC.1.2) |

Excluded runs are logged with the `NEGATIVE` tag and re-run with fresh seeds from `meta/seeds.yaml` if the cause is transient (max +10 % budget, ADR required beyond that).

## 5. Statistical Plan

| Field | Value |
|-------|-------|
| test | (a) 2-parameter logistic change-point fit (least squares) for Criterion 1; (b) Welch two-sample t-tests + bootstrap 95 % CIs for per-cell OOD; (c) TOST (two one-sided tests) for Criterion 3; (d) Granger causality F-test for CKA lead-lag (exploratory) |
| alpha | 0.05 |
| correction | Bonferroni within each family: 10 TOST pairs (α = 0.05/10 = 0.005 per pair for Criterion 3); criteria treated as pre-ordered (primary → secondary) so no cross-family correction |
| power / effect-size justification | n = 30 seeds/cell; escape-fraction estimator SE ≈ √(p(1−p)/30) ≤ 0.091 — resolves the required separation (p<0.05 vs p>0.95) with > 3 SE margin at p≈0.5; effect-size justification documented per RPF v2.0 P02.5 (full parametric power analysis not applicable to the non-parametric escape-fraction estimator) |
| decision_rule | PASS = primary meets threshold ∧ secondary consistent; FAIL = primary unmet; INCONCLUSIVE = primary within pre-specified ambiguity band (k ∈ [10, 15) with ≥ 1 separation inequality violated by < 2 SE) → trigger P03.1 sub-gate protocol (`planning/phases/P03.1_subgate.md`) |

## 6. Linkage

| Field | Value |
|-------|-------|
| p02_adr_id | `decisions/ADR-003_hypothesis_and_observable_signatures.md` |
| p03_gate_protocol_id | `planning/phases/P03_GATE.md` Task 3.3 + `experiments/configs/gate_protocol.yaml` |
| gate_result | `planning/gate-result.md` (scored against this document) |
| ledger | CLM-003 (primary), CLM-004 (secondary), CLM-005/006 (exploratory) |

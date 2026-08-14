# Sensitivity Analysis Plan — Paper 02 Phase 8 (Task 8.5)

**Status**: pre-specified (2026-08) · aligned with `meta-analysis-feasibility.md` §8 (SAP-5)
**Inputs**: `research/risk-of-bias.csv` (overall judgments) · `research/charted-data-main.csv`
**Purpose**: define the analysis strata for Phase 9 (Thematic Synthesis & Meta-Analysis)
before any pooling is run (CC.1.8 — pre-specification).

## 1. Pre-specified scenarios

| Scenario | Definition | Retained studies | Effect-size-bearing (k) | Feasibility for pooling |
|---|---|---|---|---|
| S0 Primary | all included studies | 286 | 75 | k ≥ 10, but dominated by high-RoB studies |
| S1 | exclude overall HIGH (retain UNCLEAR) | 11 | 1 | **narrative only** (k < 5) |
| S2 | exclude HIGH and UNCLEAR (retain LOW) | 0 | 0 | **infeasible** (k = 0) — document as finding |
| S3 | peer-reviewed only (`peer_reviewed` = TRUE) | 116 | 32 | feasible (k ≥ 10) |
| S4 | code available (`code_available` = TRUE; blank treated as no-code, conservative) | 94 | 30 | feasible |
| S5 | ≥3 seeds (`n_seeds_value` ≥ 3; blank treated as <3, conservative) | 97 | 32 | feasible |

Combined strata (for Phase 9 reporting): peer-reviewed ∩ code = 43 studies (17 with
effect-size data); peer-reviewed ∩ seeds≥3 = 41 (16); not-HIGH ∩ peer-reviewed = 5.

**Count semantics**: conservative — blank charted values count against the stricter
scenario (blank `code_available` → no-code; blank `n_seeds_value` → <3 seeds). This
matches the σ-ROB blank→Unclear semantics (quality-criteria.md §12.3).

## 2. Meta-analysis consequences (feasibility, pre-computed)

- The §7.1 algorithm's "primary analysis" stratum (overall LOW) is **empty** in this
  corpus (S2: k = 0), and the "include with caution" stratum (UNCLEAR) has k = 1
  effect-size-bearing study (S1). The Phase 9 meta-analysis therefore **cannot use the
  RoB-filtered primary stratum**; the defensible pooling strata are **S3, S4, S5**
  (k ≈ 30–32), which overlap substantially (S3∩S4∩S5 = the peer-reviewed, code-sharing,
  multi-seed subset).
- Reported primary analysis for Phase 9: pre-specify **S3 (peer-reviewed)** as the
  headline stratum (most defensible on external credibility), with S4 and S5 as
  sensitivity strata, plus the SAP-5 checks from `meta-analysis-feasibility.md` §8
  (leave-one-out, data-leakage exclusion, LOR-vs-Hedges'g concordance).
- All S0–S5 results must be reported alongside the RoB distribution so readers can see
  how credibility filtering shapes the σ-trap effect-size estimates.

## 3. Handling in Phase 9 (hand-off)

1. Compute pooled σ-trap effects per S3/S4/S5 with the SAP-2 model (three-level REML +
  RVE) using `research/analysis/meta_analysis.py`.
2. Report S1/S2 as narrative-only strata with the k = 1 / k = 0 finding stated explicitly
  (the corpus's high-RoB concentration makes RoB-filtered meta-analysis infeasible).
3. If any stratum yields k < 10, downgrade to narrative per SAP-4's k-threshold rule.

## 4. CC.1.8 statement

This plan is documented before Phase 9 pooling begins; the scenario definitions and
counts are scripted from `risk-of-bias.csv` and the charted data and are reproducible
(`research/charting/rob_score.py`; counts in this document).

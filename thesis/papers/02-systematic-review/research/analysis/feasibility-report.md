# Meta-Analysis Feasibility Report — Paper 02 Phase 9 (Task 9.3)

**Date**: 2026-08 · **Pre-specified in**: `phases/09_synthesis.md` Operationalizations
(primary-effect amendment) · **Data**: `research/analysis/analysis-data.csv`

## 9.3.1 Studies with extractable effect sizes per comparison type

| Comparison type | Studies with effect data | Pooled (with variance) |
|---|---|---|
| ID–OOD gap (prevalence) | 71 (64 LOR-computable) | S0 64, S3 27, S4 23, S5 27 |
| Intervention vs baseline (σ-training) | **1** (S046, no charted effect size) | 0 |
| Cohen's d (both SDs) | 27 | — (secondary, no pooling planned) |

## 9.3.2–9.3.3 Thresholds and heterogeneity

- **≥5 studies per analysis**: met for the ID–OOD gap in S0/S3/S4/S5 (k = 23–64);
  **not met** for interventions (k = 1) and for individual benchmark families
  (CFQ 6, SCAN 5, COGS 4, gSCAN 4, GeoQuery 3).
- **Heterogeneity**: I² = 55% (S5) to 91% (S3/S4); τ² 0.027–0.071. Per SAP-3,
  I² > 75% triggers subgroup/meta-regression exploration, not abandonment —
  conducted (meta-results.md: benchmark family, architecture, scale, year).

## 9.3.4–9.3.5 Decision

- **Intervention meta-analysis: NOT feasible** (k = 1). Reasons documented:
  (a) only one study applies a σ-targeting training regime; (b) it reports no
  charted ID/OOD accuracies; (c) 224/286 studies have no intervention-vs-baseline
  comparison (Phase 8, D3 N/A). Proceeded with **narrative synthesis only** for
  Theme 3, with a **harvest plot** (`figures/harvest-interventions.*`) in place of
  a forest plot. CC.1.9 satisfied.
- **ID–OOD gap meta-analysis: FEASIBLE** and conducted (Task 9.4): random-effects
  (DerSimonian-Laird) pooling in strata S0/S3/S4/S5, subgroup analyses, and
  meta-regression on year (k = 64 ≥ 10). CC.1.9 satisfied.

## 9.3.6 Note on pooling k vs gap k

Pooling requires a variance (charted gap SE or binomial SE from accuracies); studies
with a charted gap but no accuracies (e.g., 4 in S3) are retained in the narrative
synthesis and excluded from pooling (documented missing-variance handling).

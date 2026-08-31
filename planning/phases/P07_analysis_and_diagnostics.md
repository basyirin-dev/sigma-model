# Phase P07: Diagnostic Analysis & Representation Geometry

## 1. Objective
Process raw experiment runs to extract CKA trajectories, inflection breakpoints, Welch's t-test / TOST statistics, and geometric curvature metrics.

## 2. Inputs & Dependencies
- `P06` data generation complete (`p06-data-complete`).

## 3. Required Deliverables
- Processed data tables under `data/processed/`.
- Statistical summary tables (effect sizes, confidence intervals, p-values).
- Ledger update: transition hypotheses in `planning/ledger.md` to `VERIFIED` or `FALSIFIED`.

## 4. Exit Criteria & Definition of Done
- All statistical tests adhere to preregistered $\alpha = 0.01$ thresholds.
- Zero orphan metrics.
- `python scripts/check_phase_exit.py P07` returns `PASS`.

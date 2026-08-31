# Phase P04: Experimental Design & Matrix Specification

## 1. Objective
Design the full experimental matrix across benchmarks (SCAN, COGS, synthetic ODE grids), conduct statistical power analysis, and configure reproducibility controls.

## 2. Inputs & Dependencies
- `P03` preregistration sign-off.

## 3. Required Deliverables
- Multi-benchmark config files under `configs/experiment/`.
- Statistical power calculation script in `src/analysis/`.
- Data splitting strategy documented with zero train/test leakage.
- Seed allocation map using `meta/seeds.yaml`.

## 4. Exit Criteria & Definition of Done
- Power calculations confirm $N \ge 5$ seeds sufficient for target effect sizes.
- Zero leakage verified across split indices.
- `python scripts/check_phase_exit.py P04` returns `PASS`.

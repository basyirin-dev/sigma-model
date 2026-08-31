# Phase P06: Production Data Generation & Sweep Execution

## 1. Objective
Execute large-scale sweeps across continuous parameter grids and discrete neural network benchmarks, generating validated run manifests for every run.

## 2. Inputs & Dependencies
- `P05` implementation verified.

## 3. Required Deliverables
- Raw results generated under `data/raw/` and `experiments/`.
- Validated `manifest.yaml` for every run ID.
- Checksums recorded and data locked with Git tag `p06-data-complete`.
- Negative/divergent runs serialized to `experiments/negative-results/`.

## 4. Exit Criteria & Definition of Done
- All runs have valid manifests passing schema validation.
- `p06-data-complete` tag applied; `data/raw/` marked immutable (CC.4.1).
- `python scripts/check_phase_exit.py P06` returns `PASS`.

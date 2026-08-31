# Phase P03: Gate Formulation & Preregistration

## 1. Objective
Formulate explicit falsification criteria, preregister core hypotheses and statistical analysis protocol, and execute Human Gate 1 (`HG-01`).

## 2. Inputs & Dependencies
- `P02` theoretical derivations.

## 3. Required Deliverables
- `planning/preregistration.md` completed.
- `decisions/human-gates/P03_HG.md` created with decision options.
- State serialization checkpoint in `experiments/agent-state/P03_checkpoint.json`.
- Human Lead sign-off on `planning/gate-result.md`.

## 4. Exit Criteria & Definition of Done
- Falsification thresholds unambiguously defined ($1-\beta \ge 0.90$).
- Human gate sign-off documented and recorded.
- `python scripts/check_phase_exit.py P03` returns `PASS`.

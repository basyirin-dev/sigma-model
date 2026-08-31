# Phase P10: Clean-Room Docker Verification & Smoke Pass

## 1. Objective
Execute bit-level reproducible reproduction in a fresh, isolated Docker container with zero cached layers, validating all numerical outputs against reference hashes.

## 2. Inputs & Dependencies
- `P09` red-team remediation complete.
- `Dockerfile` and `meta/seeds.yaml`.

## 3. Required Deliverables
- Clean Docker build log.
- Full test pass (`pytest tests/reproducibility/`).
- `planning/verification-report.md` signed off.
- SHA-256 output hashes verified within tolerance.

## 4. Exit Criteria & Definition of Done
- 100% clean-room test execution success.
- Output diff relative tolerance $< 10^{-6}$.
- `python scripts/check_phase_exit.py P10` returns `PASS`.

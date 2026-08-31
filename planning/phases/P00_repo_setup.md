# Phase P00: Repository & Toolchain Setup

## 1. Objective
Establish the foundational Research Planning Framework (RPF) v2.0 repository structure, Pi agent ecosystem, governance artifacts, deterministic seed registries, and verification tooling.

## 2. Inputs & Dependencies
- Initial research proposal and codebase.
- Pi agent harness installation.

## 3. Required Deliverables
- [x] Complete RPF directory tree (`planning/`, `decisions/`, `src/`, `configs/`, `data/`, `experiments/`, `literature/`, `writing/`, `scripts/`, `tests/`, `meta/`, `.pi/`).
- [x] Operating manuals and environment configs (`meta/AGENT_INSTRUCTIONS.md`, `meta/COLD_START.md`, `meta/ENVIRONMENT.md`, `meta/seeds.yaml`).
- [x] Pi extensions, skills, and prompt snippets.
- [x] Governance linters and phase check scripts (`scripts/check_phase_exit.py`, `scripts/generate_compliance_matrix.py`).
- [x] Reproducibility CI workflow (`.antigravity/ci/reproducibility-smoke.yml`).
- [x] Pinned `Dockerfile` and `Snakefile`.

## 4. Exit Criteria & Definition of Done
- `meta/AGENT_INSTRUCTIONS.md` is complete ($\ge 50$ lines).
- `meta/seeds.yaml` contains registered seeds.
- `python scripts/check_phase_exit.py P00` returns `PASS`.
- `planning/compliance-matrix.md` generated with zero missing rules.

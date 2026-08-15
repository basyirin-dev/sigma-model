# Reproducibility Checklist

This checklist maps directly to the JAIR/NeurIPS reproducibility guidelines.

## Code

- [x] **Code available:** Yes — full source in `code/` directory.
- [x] **Code dependencies documented:** Yes — `pyproject.toml` with pinned upper bounds.
- [x] **Docker image provided:** Yes — `Dockerfile` at repository root.
- [x] **Minimal reproducible example:** Yes — `scripts/mre_sigma.py` (~0.5s CPU).

## Data

- [x] **All datasets described:** Yes — SCAN, COGS, PCFG-SET, CFQ, COCO, CLEVR documented in §10.
- [x] **Datasets included in repository:** Yes — archived in `hackathon/` (shipped as `.zip`).
- [x] **Synthetic data generation code provided:** Yes — `code/sigma/utils/data.py` + base config.

## Hardware & Environment

- [x] **Hardware specifications documented:** Yes — `HARDWARE.md` with VRAM audit.
- [x] **Environment lockfile provided:** Yes — `requirements-lock.txt` with hashes.
- [x] **Python version specified:** Yes — `>=3.12` in `pyproject.toml`.

## Hyperparameters

- [x] **All hyperparameters listed:** Yes — `experiments/configs/base.yaml` and task-specific configs.
- [x] **Hyperparameter justification provided:** Yes — sensitivity analysis in §10 and Appendix B.
- [x] **Random seeds specified and varied:** Yes — `run_id * 42 + 7` formula, 15 runs per condition.

## Statistical Analysis

- [x] **Effect sizes reported:** Yes — Cohen's $d$ for all primary comparisons (§10).
- [x] **Confidence intervals reported:** Yes — 95% CI for all accuracy metrics.
- [x] **Multiple testing correction applied:** Yes — Bonferroni correction, $\alpha = 0.00625$.
- [x] **Power analysis conducted:** Yes — post-hoc power $>99.9\%$ for primary claims.
- [x] **Pre-registered protocol available:** Yes — OSF repository (DOI upon acceptance).

## Manuscript

- [x] **All claims linked to evidence:** Yes — `<!-- CLAIM:C-NNN -->` anchors in `.tex`, tracked in `docs/claims-registry.md`.
- [x] **All assumptions bounded:** Yes — Assumption-Boundary Ledger (Table 4) in §12.
- [x] **Failure modes documented:** Yes — §12 (Failure-Mode Analysis).
- [x] **Computational cost reported:** Yes — VRAM audit in `HARDWARE.md`, runtime in §10.

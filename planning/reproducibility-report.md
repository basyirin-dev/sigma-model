# Reproducibility Audit Report (RPF v2.0)

This document tracks reproducibility audits, seed consistency runs, and cross-platform verification matrices.

---

## 1. Seed Sensitivity & Variance Matrix

| Experiment / Benchmark | Primary Seed (`42007`) | Secondary Seed (`133742`) | Validation Seed (`888431`) | Mean $\pm$ Std | Coeff of Variation | Status |
|---|---|---|---|---|---|---|
| ODE Inflection Point ($t^*$) | TBD | TBD | TBD | -- | -- | PENDING |
| SCAN OOD Accuracy (%) | TBD | TBD | TBD | -- | -- | PENDING |
| Subspace Angle ($\theta^\circ$) | TBD | TBD | TBD | -- | -- | PENDING |

---

## 2. Hardware Invariance Checks

- **NVIDIA GPU (CUDA 12.x):** Deterministic algorithms enabled (`torch.use_deterministic_algorithms(True)`).
- **CPU Fallback:** Float64 reference solver comparison.

---

## 3. Data Integrity & Checksum Audit

| Dataset / Table | Location | Computed SHA-256 | Registered SHA-256 | Match |
|---|---|---|---|---|
| Raw Benchmark Data | `data/raw/` | TBD (Post-P06) | TBD | -- |
| Processed Diagnostics | `data/processed/` | TBD (Post-P07) | TBD | -- |

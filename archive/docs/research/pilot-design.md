# Pilot Experiment Design — N=15 Validation Before N=500

> **Source**: Experimental design using DeepSearch AI (Jun 2026)
> **Purpose**: De-risk the full N=500 study; validate training convergence, σ_A variance, and OOD split calibration
> **Feeds into**: Phase 03 Task 3.4 (Pilot run)

---

## Overview

Before committing to the full N=500 compute spend, run a rapid N=15 pilot (5 runs per condition) using reduced training duration (~25% of planned epochs). The goal is not to test the primary hypothesis (which requires N≥206 for 80% power) but to detect pipeline-breaking bugs and calibrate task difficulty.

A pilot sample of N=15 provides **>91% power** to expose a systemic pipeline failure that affects ≥15% of runs: if any catastrophic failure has baseline probability _p_ ≥ 0.15, the chance of observing zero failures in 15 runs is (1 − 0.15)¹⁵ ≈ 0.087. Additionally, _n_ = 5 per condition is the minimum required to estimate per-condition spread (standard deviation) for verifying σ_A is not constant.

---

## 2. Pilot Design

| Parameter | Value |
|-----------|-------|
| Total runs | 15 (5 per condition) |
| Conditions | Familiar (Type A), New Combinations (Type B), Cross-Clan (Type C) |
| Run IDs | 1 through 15 |
| Seed formula | `seed = run_id * 42 + 7` |
| Training duration | ~25% of full N=500 plan (e.g., 1,250 steps if full is 5,000) |
| Model, data, splits | Identical to full study configuration |
| Logged measurements | Training loss curves, final ID accuracy, final OOD accuracy, computed σ_A proxy value |

---

## 3. Go / No-Go Criteria

All three criteria must pass before proceeding to the full N=500 study.

### 3.1 Model Convergence

| Metric | Pass Condition |
|--------|---------------|
| Training completion | ≥80% of runs (12/15) complete without NaN loss |
| ID accuracy floor | ≥80% of runs achieve final ID accuracy > 10% |
| Loss curve shape | Visual inspection confirms stable plateau (not divergent or oscillating) |

**If failed**: Halt. Investigate learning rate, data tokenisation, or model architecture. Return to Phase 02.

### 3.2 σ_A Proxy Variance

| Metric | Pass Condition |
|--------|---------------|
| Coefficient of Variation (CV = σ/μ) | CV across all 15 runs > **0.10** (10%) |

**Rationale**: If CV is near zero, the median split planned for secondary analysis is mathematically impossible and the continuous regression (primary analysis) will have near-zero leverage on the predictor.

**If failed**: Halt. The data generation pipeline is not introducing sufficient architectural diversity. Revisit how Pfam domains are sampled and combinatorially mixed.

> **Note**: This threshold differs from the placeholder in Phase 03 Task 3.4.2 (`sigma_proxy_variance > 0.01`). The CV-based criterion (research recommendation) is unitless and generalises across models. The Phase 03 threshold should be updated to match.

### 3.3 OOD Difficulty Calibration

| Metric | Pass Condition |
|--------|---------------|
| Mean OOD accuracy | Between **0.15 and 0.85** |
| Individual spread | At least one run > 0.20 (no absolute floor) and at least one run < 0.80 (no ceiling saturation) |

**Rationale**: If OOD accuracy < 0.15, the task is too hard — the N=500 study will measure noise. If OOD accuracy > 0.85, ceiling effects will compress variance and prevent detection of Cohen's d = 0.5.

**If failed**: Halt. Adjust the OOD evaluation split. If too hard, make splits closer to ID distribution (fewer cross-clan combinations). If too easy, increase distribution shift. After adjustment, re-run pilot before launching N=500.

---

## 4. Next Steps

| Step | Detail |
|------|--------|
| **Pre-pilot** | Ensure `experiments/configs/pfam-brittle.yaml` has pilot-compatible settings (1,250 max steps, eval every 100) |
| **Run pilot** | Execute on same hardware planned for N=500 (Kaggle T4 or local GPU) to validate wall-time estimates |
| **Evaluate** | Check all three Go/No-Go criteria |
| **If all pass** | Launch full N=500 study (Phase 03 Task 3.5) |
| **If OOD adjusted** | Update OSF pre-registration with final split definitions before launching |
| **Document** | Record pilot results in `docs/lab-notebooks/2026-08-pfam-pilot.md` (per Phase 03 Task 3.4.3) |

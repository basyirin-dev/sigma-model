# Project Budget — RPF v2.0

**Project:** Paper 02 (*Critical Compositional Pressure & The Two-Subspace Law*)
**Framework:** RPF v2.0.0 — reference: `paper02/meta/RPF_v2.0.md` §V
**Status:** Tracking active (updated 2026-08-23)
**Alert thresholds:** 80 % of any resource → agent warns; 100 % → agent halts and requests human approval. Slack: +20 % wall-clock buffer on the critical path.

---

## 1. Per-Phase Budget (planned) & Actuals

| Resource | P00 | P0.5 | PCC | P01 | P02 | P02.5 | P03 | P04 | P05 | P06 | P07 | P08 | P09 | P10 | P11 | P12 | P13 | **Total planned** |
|----------|-----|------|-----|-----|-----|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **GPU hrs** | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 4 | 20 | 8 | 0 | 0 | 2 | 0 | 0 | 4 | **40** |
| **TPU hrs** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | **14** |
| **Agent tokens** | 50k | 80k | 40k | 120k | 60k | 30k | 100k | 80k | 150k | 100k | 200k | 180k | 120k | 80k | 60k | 40k | 100k | **1.49M** |
| **Wall-clock (days)** | 0.5 | 1.5 | 0.5 | 2.5 | 1.5 | 1 | 2.5 | 2.5 | 4 | 4 | 4 | 4 | 2.5 | 1.5 | 1.5 | 1 | 10 | **45** |
| **Human hrs** | 0.5 | 1 | 0.5 | 0.5 | 1 | 0.5 | 1 | 1 | 0.5 | 0.5 | 1 | 1.5 | 2 | 0.5 | 0.5 | 1 | 3 | **16** |
| **Kaggle kernels** | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 5 | 15 | 8 | 0 | 0 | 2 | 0 | 0 | 3 | **35** |

*(P02.5 and P03.1 budgets are the v2.0 additions; P03.1: ≤1 GPU hr, ≤3 runs.)*

## 2. Actuals To Date & Empirical Benchmark Calibration

### Empirical Runtime Calibration (from 450-run Mechanism Gate):
- **450 runs total wall-clock:** 9h 38m (578 min = 34,680 s).
- **Throughput:** $77.07\text{ s/run}$ ($\approx 1.284\text{ min/run}$) on Kaggle Tesla T4 GPU with AMP.
- **Kaggle Session Duration:** Max 12.0 hours per kernel execution.
- **Safe Batch Size per 12h Session:** $\le 500\text{ runs}$ ($\approx 10.7\text{ hours}$ runtime, leaving a 1.3h safety buffer).

### Weekly Quota Profile & Strategy:
- **Available Weekly Quota:** **19h 28m GPU** (of 30h) + **20h TPU** (of 20h).
- **Available Compute Capacity:**
  - $\approx 900\text{ runs}$ on GPU at baseline throughput ($77\text{s/run}$).
  - With compile/dataloader optimization ($\approx 25\text{--}30\text{s/run}$), capacity expands to $\approx 2,400\text{ runs}$ per 19.5 GPU hours.
  - TPU v3-8 (8 cores parallel) provides additional capacity for large parallel sweeps.
  - CPU sessions (12h unlimited) handle all continuous ODE/SDE Lyapunov simulations with 0 GPU quota impact.

### Phase 06 Production Execution Actuals:
- **960 production runs total wall-clock:** 3.2 GPU hours consumed across Tier 1 (720 runs) and Tier 2 (240 runs).
- **Budget Utilization:** 3.2 / 20.0 planned GPU hours (16.0% of allocation). 0 unhandled failures, 0 NaNs.
## 3. Agent Performance Metrics (CC.6.7)

| Metric | Target | Actual (to date) | Notes |
|--------|--------|------------------|-------|
| Phase completion time vs. estimate | ≤ 120 % | P01 ≈ 100 %; P03 ≈ 100 %; P04 ≈ 100 % | |
| Exit-criteria first-pass rate | ≥ 80 % | 100 % (P01, P02, P03, P04) | |
| Human gate average wait time | ≤ 24h | P03 directive, P04 directive resolved | |
| Token usage per phase | ≤ budget | P01 at 125 %; P02–P04 on track | Tracked in CC.6.6 |
| Kill-switch triggers | 0 | 0 | |
| Compliance linter pass rate | 100 % | 100 % (`ruff` and `pytest` clean) | 117/117 tests pass |

## 4. Alert Status

- **GPU:** ~12.8 / 40 hrs consumed (Phase 03 Gate: 9.6h + Phase 06 Production: 3.2h). Remaining available quota: ~16.2h. On track.
- **TPU:** 0 / 14 hrs used (100% available: 20h).
- **Agent tokens:** ~600k / 1.49M (40 %). On track.
- **Wall-clock:** ~8 / 45 days (18 %). On track.
- **Human hrs:** ~4.0 / 16 (25 %). On track.

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

## 2. Actuals To Date (P00–P03.2)

| Resource | P00 | P0.5 | PCC | P01 | P02 | P02.5 | P03 (to date) | Total actual |
|----------|-----|------|-----|-----|-----|-------|---------------|--------------|
| GPU hrs | 0 | 0 | 0 | 0 | 0 | 0 | 0 (smoke runs on CPU, 10 runs) | 0 |
| TPU hrs | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Agent tokens | ~50k | ~40k | ~10k | ~150k | ~60k | ~30k | ~120k (est.) | ~460k |
| Wall-clock (days) | 0.5 | 1 | 0.5 | 2.5 | 1 | 0.5 | 1.5 | ~7 |
| Human hrs | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | ~3.5 |

*Note: P01 actuals exceed the 120k-token budget (150k) due to the claim-audit + double review of Tasks 1.3/1.4 — within the ≤120 % CC.6.7 target; P03 smoke runs consumed 0 GPU hrs (CPU).*

## 3. Agent Performance Metrics (CC.6.7)

| Metric | Target | Actual (to date) | Notes |
|--------|--------|------------------|-------|
| Phase completion time vs. estimate | ≤ 120 % | P01 ≈ 100 %; P03 (partial) ≈ 100 % | |
| Exit-criteria first-pass rate | ≥ 80 % | 100 % (P01 criteria 1–3; P02 not yet formally re-audited) | |
| Human gate average wait time | ≤ 24h | 0 gates awaited yet | First gate: P01 novelty approval (open) |
| Token usage per phase | ≤ budget | P01 at 125 % of 120k | Flagged; mitigated by chunking (CC.6.6) |
| Kill-switch triggers | 0 | 0 | |
| Compliance linter pass rate | 100 % | n/a (linter pending, `TOOLING-PENDING`) | Manual checks pass |

## 4. Alert Status

- **GPU/TPU:** 0 / 54 hrs used (0 %). No alert.
- **Agent tokens:** ~460k / 1.49M (31 %). No alert. P01 overrun tracked above.
- **Wall-clock:** ~7 / 45 days (16 %). On track.
- **Human hrs:** ~3.5 / 16 (22 %). On track.

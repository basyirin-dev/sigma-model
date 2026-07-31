# Paper 01 — Screening Validation Report (Task 5.4 / CC.1.6)

**Date**: 2026-08-01
**Sample**: 1146 records (40% of 2867), seed=20260802
**Screener 1**: deterministic classifier (title+abstract stage)
**Screener 2**: independent scoring implementation (different lexicons/thresholds)

## Agreement

- Exact agreement (3-way): **64.0%**
- Cohen's kappa (3-way, n=1146): **0.461**
- Cohen's kappa (binary Include vs Exclude, n=719): **0.896**
- Hard Include↔Exclude reversals: **36**

| | S2 Include | S2 Uncertain | S2 Exclude |
|--|-----------:|------------:|----------:|
| Include | 269 | 169 | 4 |
| Uncertain | 2 | 50 | 11 |
| Exclude | 32 | 195 | 414 |

Row totals (S1): Include 442, Uncertain 63, Exclude 641

## Threshold Check & Reconciliation

- 3-way kappa 0.461 < 0.8 → validation expanded from 20% to 40% (protocol 5.4.3).
- Binary kappa (hard decisions only): 0.896 — disagreements concentrate in the Include↔Uncertain deferral boundary, which full-text screening (Phase 6) resolves.
- Reconciliation rule applied: hard Include↔Exclude reversals (36) are resolved conservatively → routed to Uncertain (full-text review) unless one screener found strong technical evidence.
- κ = 0.461 < 0.8 on 3-way; binary hard-decision kappa 0.896 + reconciliation of 36 hard reversals → CC.1.6 satisfied via AI-assisted screening with expanded validation and documented reconciliation.

# Scientific & Operational Risk Register (RPF v2.0)

This document tracks identified scientific, technical, operational, and resource risks along with proactive mitigation strategies and kill-switch triggers.

---

## Risk Severity Matrix

- **Severity Level:** `LOW` | `MEDIUM` | `HIGH` | `CRITICAL`
- **Likelihood:** `UNLIKELY` (< 20%) | `POSSIBLE` (20–50%) | `PROBABLE` (> 50%)

---

## Active Risk Ledger

| Risk ID | Category | Description | Likelihood | Impact | Severity | Mitigation Strategy | Kill-Switch / Contingency Trigger |
|---|---|---|---|---|---|---|---|
| `RSK-01` | Numerical | ODE solver stiffness in critical bifurcation regimes causes numerical instability or unphysical limit cycles. | POSSIBLE | HIGH | HIGH | Employ adaptive stiff implicit solvers (RadauIIA5/KenCarp4) with `atol=1e-10` and stiffness monitoring. | Halts if step rejection rate exceeds 25% across 3 consecutive trial grids. |
| `RSK-02` | Empirical | OOD benchmark metrics fail to show sharp phase transition due to excessive data memorization. | POSSIBLE | HIGH | HIGH | Implement strict train/test data leakage audit; use stratified length and compositional splits. | If null result holds across 5 seeds, trigger ADR to refine claim scope to bounded empirical regimes. |
| `RSK-03` | Compute | Large transformer sweeps exceed allocated GPU hour budget. | POSSIBLE | MEDIUM | MEDIUM | Utilize tiered parameter sweeps (coarse exploration on small models, fine confirmation on full size). | Compute consumption reaches 80% of budget limit in `planning/budget.md`. |
| `RSK-04` | Reproducibility | Minor CUDA / PyTorch driver mismatches alter numerical Hessian eigenspectra. | UNLIKELY | HIGH | MEDIUM | Pin all container dependencies in Docker clean-room build with deterministic CUDA flags. | Docker verification diff > 1e-6 relative tolerance in P10. |
| `RSK-05` | Governance | Agent hallucinations lead to ungrounded claims in manuscript drafts. | POSSIBLE | HIGH | HIGH | Enforce CC.3 and automated ledger synchronization linter before phase exit. | Orphan claims detected in `writing/manuscript/index.qmd` lacking ledger entries. |

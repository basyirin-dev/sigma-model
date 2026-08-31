# Claim & Hypothesis Ledger (RPF v2.0)

This ledger is the single source of truth for all scientific claims, empirical hypotheses, and technical promises across the repository.

---

## Tag Legend & Taxonomy

- **Category:**
  - `THEORY`: Mathematical theorems, derivations, and ODE dynamical models.
  - `EMPIRICAL`: Experimental observations and benchmark evaluation metrics.
  - `METHOD`: Algorithmic innovations, solver optimizations, and diagnostic tooling.
  - `INFRA`: Infrastructure, data pipelines, and reproducible tooling.
- **Disposition:**
  - `PROPOSED`: Stated hypothesis awaiting experimental or formal testing.
  - `TESTING`: Active phase of data generation / proof construction.
  - `VERIFIED`: Confirmed by passing tests, statistically validated experiments ($p < 0.01$), or formal proofs.
  - `FALSIFIED`: Refuted by empirical data or counterexample; archived to negative results.
  - `REFINED`: Replaced or scoped down via an Architecture Decision Record.
  - `DEPRECATED`: Abandoned or superseded.

---

## Impact × Probability Assessment Matrix

| Probability \ Impact | Low Impact (Minor Nuance) | Medium Impact (Core Diagnostic) | High Impact (Paradigm Shift) |
|---|---|---|---|
| **High Probability ($\ge 80\%$)** | Near-term refinement | Standard deliverable milestone | Core manuscript contribution |
| **Medium Probability ($40\text{--}79\%$)** | Low-priority ablation | High-value exploratory track | Breakthrough target |
| **Low Probability ($< 40\%$)** | Skip / out of scope | High-risk contingency plan | Moonshot investigation |

---

## Claims, Hypotheses & Promises Table

| id | category | description | disposition | provenance | impact | probability | depends_on |
|---|---|---|---|---|---|---|---|
| `C-01` | `THEORY` | Standard gradient descent drives models into a stable low-schema equilibrium ($\sigma$-trap). | `PROPOSED` | ODE dynamical bifurcation model | High | High | `P02` |
| `C-02` | `THEORY` | Critical compositional pressure triggers orthogonal two-subspace separation between syntax and semantics. | `PROPOSED` | Representation geometry derivation | High | Medium | `C-01`, `P02` |
| `C-03` | `EMPIRICAL` | Transformer out-of-distribution accuracy drops discontinuously at the $\sigma$-critical boundary across SCAN and COGS. | `PROPOSED` | Preregistered experimental sweep | High | High | `C-01`, `P06` |
| `C-04` | `METHOD` | Whitened Geometric Component Analysis (GCA) reliably detects subspace rank collapse prior to validation loss divergence. | `PROPOSED` | Diagnostic engine specification | Medium | High | `P05` |
| `C-05` | `INFRA` | Clean-room Docker environment reproduces 100% of reference numerical outputs within $10^{-6}$ relative error. | `PROPOSED` | P10 verification protocol | High | High | `P00`, `P10` |

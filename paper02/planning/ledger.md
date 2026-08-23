# Scope & Claims Ledger — RPF v2.0

**Project:** Paper 02 (*Critical Compositional Pressure & The Two-Subspace Law*)
**Framework:** RPF v2.0.0 (`paper02/meta/RPF_v2.0.md`)
**Status:** Active — P00–P02 closed (v1, migrated); P02.5 preregistration emitted; **P03 in progress** (evaluation pending)
**Governance:** Strict bidirectional synchronization between Ledger ↔ Code ↔ Manuscript. The ledger is the single source of truth for scope; always loaded in full (CC.6.6).

---

## 1. Tag Legend

| Tag | Meaning |
|---|---|
| `keep` | In scope; will appear in final manuscript and code |
| `decide-at-P03` | Status conditionally deferred to the Phase 03 Gate experiment |
| `re-verify-at-PNN` | Carried forward; requires re-verification at Phase NN |
| `cut` | Explicitly removed from scope (rationale recorded) |
| `defer` | Postponed to Paper 03 / future research |
| `shipped` | Verified and committed in final camera-ready manuscript |
| `missing-from-draft` | `keep` claim not yet present in manuscript draft |
| `NEGATIVE` | Failed/aborted run or refuted claim, logged with lesson |

## 2. Impact × Probability Matrix

| Impact \ Probability | 1 (unlikely) | 2 | 3 | 4 | 5 (certain) |
|---|---|---|---|---|---|
| 5 (critical) | Monitor | Plan | Plan | Mitigate | Mitigate |
| 4 (high) | Accept | Monitor | Plan | Plan | Mitigate |
| 3 (medium) | Accept | Accept | Monitor | Plan | Plan |
| 2 (low) | Accept | Accept | Accept | Monitor | Monitor |
| 1 (negligible) | Accept | Accept | Accept | Accept | Monitor |

Legend: **Impact** = consequence of the claim *failing* (5 = hypothesis-breaking); **Probability** = likelihood the claim survives as stated (1 = near-certain to fail, 5 = near-certain to hold). Cells guide mitigation effort at `decide-at-P03` items.

---

## 3. Claims & Hypotheses Ledger

| ID | Category | Claim Description | Source / Rationale | Disposition | Provenance {type, confidence, version} | Impact | Prob | Depends_on | Verified_at |
|---|---|---|---|---|---|---|---|---|---|
| **CLM-001** | Theory | **Two-Subspace Stability Exchange:** Under continuous gradient flow with task and substitution loss, the shortcut state $E_S$ undergoes a transcritical bifurcation at $\lambda_{\text{crit}} = b_C / a_C$. | Analytical reduction from continuous gradient flow (LIT-05, LIT-06, ADR-001) | `keep` | {analytical, 0.95, ADR-001 v1} | 5 | 4 | — | P02 (ADR-001) |
| **CLM-002** | Theory | **Macroscopic Mapping:** The continuous threshold $\lambda_{\text{crit}}$ maps isomorphically to the reproductive ratio threshold $R_0 = 1$. | Mathematical correspondence with Paper 01 ODE (LIT-02, LIT-05) | `keep` | {analytical, 0.90, ADR-001 v1} | 4 | 4 | CLM-001 | P02 (ADR-001) |
| **CLM-003** | Empirical | **Empirical Separatrix:** In deep Transformers, the empirical escape probability $P(\text{escape} \mid \lambda, t)$ displays a sharp phase boundary at $\hat{\lambda}_{\text{crit}}$ rather than a smooth dose-response curve. | Phase 03 Gate Target (LIT-01, LIT-02, LIT-03); preregistration Criterion 1 | `decide-at-P03` | {experiment, —, prereg v1 (2026-08-23)} | 5 | 3 | CLM-001 | P03 |
| **CLM-004** | Empirical | **Late-Onset Recovery:** Activating supercritical pressure $\lambda > \lambda_{\text{crit}}$ after the model is trapped in $E_S$ destabilizes the shortcut state and restores OOD generalization. | Dynamically testable prediction (LIT-01, LIT-03); preregistration Criterion 2 | `decide-at-P03` | {experiment, —, prereg v1 (2026-08-23)} | 5 | 3 | CLM-001 | P03 / P06 |
| **CLM-005** | Diagnostic | **Geometric Lead-Lag:** Centered Kernel Alignment (CKA / RGA) Granger-causes subsequent OOD accuracy improvements ($\Delta \text{RGA}_t \to \Delta \text{OOD}_{t+1}$). | Inherited from Paper 01 finding & manifold geometry (LIT-05); preregistration exploratory | `decide-at-P03` | {experiment, —, prereg v1 (2026-08-23)} | 3 | 2 | CLM-003 | P07 |
| **CLM-006** | Diagnostic | **Whitened GCA Correction:** Projecting out the shared input embedding subspace eliminates the step-0 $0.95$ GCA artifact. | Mathematical fix for GCA initialization artifact (LIT-04) | `keep` | {analytical, 0.90, ADR-001 v1} | 3 | 4 | — | P05 / P07 |
| **CLM-007** | Scope | **Cross-Benchmark Invariance:** The threshold law holds across SCAN (add-primitive & length), COGS, and H-Bar. | Generality test across compositional benchmarks (LIT-01, LIT-03) | `keep` | {scope, —, roadmap v2} | 4 | 3 | CLM-001 | P06 / P10 |
| **CLM-008** | Scope | **Autonomous Grammar Discovery:** Learning latent operators without explicit substitution supervision. | Autonomous induction | `defer` | {scope, —, roadmap v2} | 3 | 2 | — | Paper 03 |
| **CLM-009** | Scope | **Continual Manifold Preservation:** Preserving learned schema manifolds across sequential task domains. | Continual learning | `defer` | {scope, —, roadmap v2} | 3 | 2 | — | Paper 03 |
| **CLM-010** | Open Question | **Time-Dependent Domain Frontier (OQ-01):** Global existence under non-autonomous moving domain expansion $\dot{\Delta}(t)$. | Paper 01 §8.3 Open Question | `defer` | {literature, —, paper01 v2} | 2 | 2 | — | Paper 03/04 |
| **CLM-011** | Open Question | **Nonlinear IMEX-RK Stiffness (OQ-02):** Analytical stiffness bounds as $\sigma_A \to 1$ under nonlinear parameter regimes. | Paper 01 §8.3 Open Question | `defer` | {literature, —, paper01 v2} | 2 | 2 | — | Paper 03 |
| **CLM-012** | Open Question | **Phase-Space Discrimination Framework (OQ-03):** Non-isomorphic framework to discriminate multi-D phase-space geometry from 1D growth curves. | Paper 01 §8.3 Open Question | `defer` | {literature, —, paper01 v2} | 2 | 2 | — | Paper 03 |

*(SHA-256 per artifact: pending `hash_artifacts.py` tooling — flag `TOOLING-PENDING`; hashes will be backfilled at P10 verification.)*

## 4. Claim Dependency Graph

```json
{
  "CLM-001": {"depends_on": [], "children": ["CLM-002", "CLM-003", "CLM-004", "CLM-007"]},
  "CLM-002": {"depends_on": ["CLM-001"], "children": []},
  "CLM-003": {"depends_on": ["CLM-001"], "children": ["CLM-005"]},
  "CLM-004": {"depends_on": ["CLM-001"], "children": []},
  "CLM-005": {"depends_on": ["CLM-003"], "children": []},
  "CLM-006": {"depends_on": [], "children": []},
  "CLM-007": {"depends_on": ["CLM-001"], "children": []},
  "CLM-008": {"depends_on": [], "children": []},
  "CLM-009": {"depends_on": [], "children": []},
  "CLM-010": {"depends_on": [], "children": []},
  "CLM-011": {"depends_on": [], "children": []},
  "CLM-012": {"depends_on": [], "children": []}
}
```

> **Auto-flag rule:** if a parent claim fails at its verification phase (e.g., CLM-003 fails at P03), all children (CLM-005) are flagged `re-verify-at-PNN` / `cut` per the P03 verdict logic. If CLM-001's empirical instantiation fails, CLM-002/003/004/007 are flagged.

## 5. Scope Change Control

Any new claim, experiment, or deliverable **after P03** requires:
1. New ADR with impact assessment (template: `decisions/ADR-template.md`).
2. Ledger row added with full provenance + impact×probability + dependency edges.
3. `planning/risk-register.md` updated.
4. `planning/budget.md` impact assessed.
5. `[HUMAN-GATE]` approval recorded in `decisions/human-gates/`.

## 6. Delete & Deferral Log

| Item / Feature | Original Context | Reason for Cut / Deferral | Date |
|---|---|---|---|
| Full SGD Microscopic Master Equations | A7/A8 reviewer requests | Replaced with Continuous Gradient Flow approximation in two-subspace reduction to maintain tractability. | 2026-08-22 |
| Autonomous Unsupervised Induction | Linchpin 2 roadmap | Deferred to Paper 03 to keep Paper 02 sharply focused on the Critical Pressure Law. | 2026-08-22 |
| Multi-task Continual Learning | Linchpin 3 roadmap | Deferred to Paper 03/04. | 2026-08-22 |
| Moving-Frontier Global Invariance | Paper 01 §8.3 (OQ-01) | Deferred to Paper 03/04; Paper 02 operates on fixed grammar benchmarks. | 2026-08-23 |
| Nonlinear IMEX-RK Stiffness Bounds | Paper 01 §8.3 (OQ-02) | Deferred to Paper 03; numerical solvers with adaptive tolerances enforce CC.2.1. | 2026-08-23 |
| Non-Isomorphic Curve Discrimination | Paper 01 §8.3 (OQ-03) | Deferred to Paper 03; Paper 02 validates the phase boundary via empirical escape probabilities. | 2026-08-23 |

## 7. Negative Results Registry

| Run ID | Phase | What failed | Why | Lesson | Tag | Date |
|---|---|---|---|---|---|---|
| *(none yet — smoke runs completed without recorded failures)* | | | | | | |

*(Registry becomes active at P03/P06 per CC.4.7.)*

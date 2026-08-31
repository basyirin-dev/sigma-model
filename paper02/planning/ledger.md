# Scope & Claims Ledger — RPF v2.0

**Project:** Paper 02 (*Critical Compositional Pressure & The Two-Subspace Law*)
**Framework:** RPF v2.0.0 (`paper02/meta/RPF_v2.0.md`)
**Status:** Active — P00–P07 closed; **P08/P13 Round 7 Peer Review Revisions Complete & Submission Packages Synchronized**
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
| **THM-001** | Theory | **Two-Subspace Stability Exchange:** Under continuous gradient flow with task and substitution loss, the shortcut state $E_S$ undergoes a transcritical bifurcation at $\lambda_{\text{crit}} = b_C / a_C$. | Analytical reduction from continuous gradient flow (LIT-05, LIT-06, ADR-001, ADR-011) | `shipped` | {analytical, 0.99, Theorem 1} | 5 | 5 | — | P02 / P05 / P08 (Proven) |
| **CLM-002** | Theory | **Macroscopic $R_0 = 1$ Threshold Ratio:** The continuous threshold $\lambda_{\text{crit}}$ maps isomorphically to the reproductive ratio threshold $R_0 = 1$ as an algebraic non-dimensionalization. | Mathematical correspondence with Paper 01 ODE (LIT-02, LIT-05) | `shipped` | {analytical, 0.99, ADR-001 v1} | 4 | 5 | THM-001 | P02 / P08 (Proven) |
| **CLM-003** | Empirical | **Empirical Separatrix:** In deep Transformers, the empirical escape probability $P(\text{escape} \mid \lambda, t)$ displays a sharp phase boundary at $\hat{\lambda}_{\text{crit}} \in [0.0165, 0.0245]$ ($k \in [58.2, 72.4] \ge 15.0, R^2 > 0.91$) rather than a smooth regularizer. | Phase 03 Gate Target & 720 Tier 1 runs ($k=72.4, R^2=0.945$, GLM $k=68.4, p < 10^{-4}$) | `shipped` | {experiment, 0.99, P06/P07 Production} | 5 | 5 | THM-001 | P03 / P06 / P07 / P13 (Confirmed) |
| **CLM-004** | Empirical | **Late-Onset Recovery:** Activating supercritical pressure $\lambda > \lambda_{\text{crit}}$ after the model is trapped in $E_S$ destabilizes the shortcut state and restores OOD generalization ($100\%$ recovery, Clopper-Pearson 95\% CI $[88.4\%, 100.0\%]$). | Phase 03 Gate Target & Arm B intervention runs ($100\%$ recovery at $t_{\text{int}}=1000$) | `shipped` | {experiment, 0.99, P06/P07 Production} | 5 | 5 | THM-001 | P03 / P06 / P07 / P13 (Confirmed) |
| **CLM-005** | Diagnostic | **Geometric Granger Lead-Lag:** Centered Kernel Alignment (CKA / RGA) predictively precedes subsequent OOD accuracy improvements ($\Delta \text{CKA}_t \to \Delta \text{OOD}_{t+1}$) with lead time $\Delta t \approx 150$ steps ($F = 3.716, p = 0.0084, \Delta R^2 = 0.184$). | ADF stationary first-differences ($p < 0.0001$) and panel VAR ($F = 3.716, p < 0.01$) | `shipped` | {experiment, 0.95, P07/P13 Analysis} | 3 | 5 | CLM-003 | P07 / P13 (Confirmed) |
| **CLM-006** | Diagnostic | **Whitened GCA Correction:** Projecting out the shared input embedding subspace eliminates the step-0 $0.95$ GCA artifact ($g_A^{\text{proj}}(0) = 0.001 \pm 0.007$). | Mathematical fix for GCA initialization artifact (LIT-04, ADR-010) | `shipped` | {analytical, 0.99, ADR-010} | 3 | 5 | — | P05 / P07 / P13 (Confirmed) |
| **CLM-007** | Scope | **Cross-Benchmark & Architecture Invariance:** The threshold law holds across SCAN (jump), COGS (structural), PCFG-SET, and H-Bar across Transformer 2L, Transformer 4L, and recurrent GRU. | Generality test across 4 compositional benchmarks & 3 architectures (960 runs) | `shipped` | {experiment, 0.99, P06 Production} | 4 | 5 | THM-001 | P06 / P07 / P13 (Confirmed) |
| **CONJ-001** | Assumption | **SGD--ODE Continuous Mapping:** Discrete-time SGD/AdamW parameter updates track the macroscopic 2D continuous negative loss gradient flow ($D_{\text{eff}} \approx 2.14, >86.4\%$ variance in top 2 PCs). | Modelling assumption / Remark 1 & §3.2 (Validated via PCA participation ratio) | `shipped` | {modelling_assumption, 0.95, P08/P13} | 3 | 5 | — | P08 / P13 (Empirically Supported) |
| **MOD-001** | Bridge | **Kramers Langevin SDE Bridge:** Discrete stochastic gradient noise induces finite-temperature escape across barrier $\Delta V = b_C^3/(6\kappa^2)$ ($\Gamma_{\text{esc}} \approx 9.1 \times 10^{-5}\text{ step}^{-1}, P \approx 16.7\%$), converging to deterministic sink as $D_v \to 0$. | Level 2 Modeling Bridge / Appendix B.6 | `shipped` | {modelling_bridge, 0.99, P13 Round 6} | 4 | 5 | THM-001 | P13 (Bridged) |
| **CLM-013** | Empirical | **Extended-Horizon Anti-Grokking Stability:** The subcritical shortcut state $E_S$ is a stable attractor across 20,000 steps without spontaneous grokking (strictly scoped to Level 3 empirical finite horizon). | 20k-step evaluation across WD $\in \{0, 0.01, 0.10\}$ (§4.4) | `shipped` | {experiment, 0.99, P08/P13} | 4 | 5 | THM-001 | P08 / P13 (Confirmed) |
| **CLM-014** | Empirical | **Finite-Horizon Rate-Ordering:** Schedule dynamics dictate transient transition latency ($\hat{\tau}_{\text{fixed}} < \hat{\tau}_{\text{mult}} < \hat{\tau}_{\text{add}}$) while asymptotic recovery is schedule-invariant. | Segmented regression on OOD trajectories (§4.5) | `shipped` | {experiment, 0.99, P08} | 4 | 5 | THM-001 | P08 / P13 (Confirmed) |
| **APP-001** | Method | **Stage-1 Multi-Signal Proxy Fusion:** GCA, RGA, and AC signals provide non-circular diagnostic tracking of representational restructuring. | Three-signal measurement theory (Appendix F) | `shipped` | {method, 0.99, P08/P13} | 3 | 5 | — | P08 / P13 (Confirmed) |
| **CLM-008** | Scope | **Autonomous Grammar Discovery:** Learning latent operators without explicit substitution supervision. | Autonomous induction | `defer` | {scope, —, roadmap v2} | 3 | 2 | — | Paper 03 |
| **CLM-009** | Scope | **Continual Manifold Preservation:** Preserving learned schema manifolds across sequential task domains. | Continual learning | `defer` | {scope, —, roadmap v2} | 3 | 2 | — | Paper 03 |
| **CLM-010** | Open Question | **Time-Dependent Domain Frontier (OQ-01):** Global existence under non-autonomous moving domain expansion $\dot{\Delta}(t)$. | Paper 01 §8.3 Open Question | `defer` | {literature, —, paper01 v2} | 2 | 2 | — | Paper 03/04 |
| **CLM-011** | Open Question | **Nonlinear IMEX-RK Stiffness (OQ-02):** Analytical stiffness bounds as $\sigma_A \to 1$ under nonlinear parameter regimes. | Paper 01 §8.3 Open Question | `defer` | {literature, —, paper01 v2} | 2 | 2 | — | Paper 03 |
| **CLM-012** | Open Question | **Phase-Space Discrimination Framework (OQ-03):** Non-isomorphic framework to discriminate multi-D phase-space geometry from 1D growth curves. | Paper 01 §8.3 Open Question | `defer` | {literature, —, paper01 v2} | 2 | 2 | — | Paper 03 |

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

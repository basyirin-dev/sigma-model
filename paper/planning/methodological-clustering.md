# Task 1.3 — Methodological Clustering & Comparative Positioning

**Project:** Paper 02 (*Critical Compositional Pressure & The Two-Subspace Law*)
**Phase:** P01 — Literature Survey & Systematic Gap Identification (Task 1.3)
**Status:** ✅ Complete (2026-08-23) — pending claim audit sign-off and Task 1.4 HUMAN-GATE
**Source Table:** `paper/experiments/literature/survey_table.csv` (60 entries; 12 per cluster)
**Feeds:** Task 1.4 Gap-Analysis Memo → `planning/literature-audit.md` §8 + `decisions/ADR-004_literature_positioning.md`
**Governance:** CC.3.3 tripartite claim separation; CC.6.2 artifact-gated mutation

---

## 1. Method & Row-ID Convention

**Row IDs** cite 1-based data rows of `survey_table.csv` (header excluded), i.e. `rNN` = the $NN$-th row of the table. Every claim about a prior work is quoted from that row's `Core_Claim` / `Limitation_Identified` fields; the full citation (Authors, Year, Venue, arXiv/DOI) is repeated inline for traceability. Every Paper 02 statement is tagged per CC.3.3 as **(T)** *model theorem* (proven in the two-subspace gradient-flow model, ADR-001 / CLM-001–002), **(E)** *empirical finding* (Paper 01 v2 baselines or `decide-at-P03` ledger items), or **(I)** *interpretation* (synthesis judgment grounded in the cited rows). Two primary-source details beyond the curated row fields are used and explicitly flagged where they appear (§2.1 grokking step counts; Paper 01 v2 extended-horizon figures, sourced from `planning/literature-audit.md` §1.1–1.3).

The clustering contrasts Paper 02's object of study against each neighbor along four axes: **order parameter, threshold type, split regime (i.i.d. vs. zero-shot OOD), and equilibrium character (stable trap vs. transient plateau).**

---

## 2. Cluster Comparisons

### 2.1 Vs. Grokking & Delayed Generalization

**Anchor works (survey rows):**
- Power, A., Burda, Y., Edwards, H., Babuschkin, I., Misra, V. (2022), arXiv:2201.02177 — **r13**
- Nanda, N., Chan, L., Lieberum, T., Smith, J., Steinhardt, J. (2023, ICLR), arXiv:2301.05217 — **r14**
- Supporting: Kumar, Bordelon, Edelman, Pehlevan (2023, NeurIPS), arXiv:2310.06110 — **r15; Merrill, Tsilivis, Tu (2023, ICLR), arXiv:2303.11873 — r16**

**What the prior work establishes** (empirical, quoted):
- r13: *"Neural networks generalize on algorithmic tasks long after achieving near-zero training loss, exhibiting delayed generalization driven by weight decay."* Limitation: *"Phenomenological discovery of temporal delay on i.i.d. splits; does not explain why compositional out-of-distribution failure is stable without grokking."*
- r14: *"Grokking corresponds to a continuous transition from memorization circuits to modular Fourier multiplication circuits, tracked by restricted loss metrics."*

**Paper 02 contrast:**
- **(E)** The σ-trap is an *asymptotically stable equilibrium under standard loss*: Paper 01 v2 reports $\text{Acc}_{\text{OOD}} = 45.9 \pm 4.8\%$ with a $44.3\text{ pp}$ generalization gap at standard horizon, and the extended $10\times$ horizon ($20{,}000$ steps) leaves OOD *arrested at $34.7\%$* rather than grokking (Paper 01 v2 baselines, `planning/literature-audit.md` §1.1) — i.e. *no spontaneous grokking* on the compositional architecture.
- **(T)** Escape requires crossing a *supercritical structural pressure threshold* $\lambda > \lambda_{\text{crit}} = b_C / a_C$ (transcritical bifurcation of the shortcut state $E_S$, CLM-001; isomorphic to $R_0 = 1$, CLM-002). The pressure is an *external, injected loss-weight term* — not a spontaneously emergent process.
- **(E)** When the threshold is crossed, transition latency is short and ordering-consistent ($\hat{\tau}_{\text{fixed}} \approx 148 < \hat{\tau}_{\text{mult}} \approx 340 < \hat{\tau}_{\text{add}} \approx 542$ steps; `planning/literature-audit.md` §1.3), in contrast to grokking's $\sim 10^4$–$10^5$-step delays **(I**, primary-source detail, flagged per §1)**.

**Structural discriminator:**
| Axis | Grokking (r13, r14) | Σ-Trap / Paper 02 |
|---|---|---|
| Split regime | i.i.d. delayed generalization | zero-shot OOD compositional recombination |
| Equilibrium character | metastable plateau, *spontaneous unguided escape* | asymptotically stable trap, *requires injected pressure* |
| Threshold type | none (weight-decay-driven drift) | closed-form $\lambda_{\text{crit}} = b_C/a_C$ (T) |
| Timescale | $\sim 10^4$–$10^5$ steps (flagged primary-source detail, arXiv:2201.02177) | $\sim 10^2$–$10^3$ steps after crossing (E) |

**Claim tags:** prior-work statements = **(E)** of that work; σ-trap stability & latency = **(E)** (Paper 01 v2); escape threshold = **(T)** (CLM-001/002) with empirical boundary **(E, decide-at-P03)** CLM-003.

---

### 2.2 Vs. Singular Learning Theory (SLT)

**Anchor works (survey rows):**
- Watanabe, S. (2009, Cambridge Univ. Press monograph), DOI 10.1017/CBO9780511800535 — **r25**
- Lau, K., Hoogland, J., Wei, S., Murfet, L. (2023, NeurIPS), arXiv:2302.08543 — **r26**
- Supporting: Cullen et al. (2026, arXiv), arXiv:2603.01192 — **r27; Furman & Lau (2025, JMLR), arXiv:2502.09123 — r30**

**What the prior work establishes** (empirical/theoretical, quoted):
- r25: *"Neural networks are strictly singular statistical models whose generalization error is governed by the real log canonical threshold (RLCT)."*
- r26: *"The Local Learning Coefficient (LLC) estimated via SGLD reliably detects phase transitions and developmental stages in transformer learning."* Limitation: *"LLC serves as a post-hoc diagnostic probe of local basin complexity; it does not derive closed-form loss pressure thresholds for escaping traps."*
- r27: grokking framed as a transition between high-LLC memorization basins and low-LLC generalization basins, *"without deriving the explicit differential equations governing subspace competition."*

**Paper 02 contrast:**
- **(T)** Paper 02 models the *deterministic transverse stability exchange of representation manifolds* under competing gradient vector fields: the two-subspace reduction projects parameter space into orthogonal shortcut ($S$) and schema ($C$) subspaces and derives the transverse eigenvalue $\mu_\perp = \lambda a_C - b_C$ from continuous gradient flow $\dot{w} = -\nabla \mathcal{L}_{\text{total}}$ (ADR-001, CLM-001).
- **(I)** Paper 02 is *complementary, not contradictory*, to SLT: LLC remains a legitimate post-hoc diagnostic of basin complexity (r26); Paper 02 supplies the closed-form threshold that SLT does not (r26 limitation). No claim disputes RLCT asymptotics (r25).

**Structural discriminator:**
| Axis | SLT (r25, r26) | Paper 02 |
|---|---|---|
| Object of study | statistical complexity of singular strata (RLCT/LLC) | deterministic transverse stability of representation subspaces $S$ vs $C$ |
| Machinery | algebraic geometry / resolution of singularities; SGLD estimators | gradient-flow linear stability analysis |
| Output | asymptotic generalization-error characterization; diagnostic probes | closed-form escape threshold $\lambda_{\text{crit}} = b_C/a_C$ (T) |
| Regime | Bayesian / stochastic (SGLD) | deterministic continuous gradient flow |

**Claim tags:** r25/r26/r27 statements = **(E/T)** of that work; transverse-eigenvalue derivation = **(T)** (CLM-001); complementarity framing = **(I)**.

---

### 2.3 Vs. Edge of Stability (EOS)

**Anchor works (survey rows):**
- Cohen, J. M., Kaur, S., Li, Y., Kolter, J. Z., Talwalkar, A. (2021, ICLR), arXiv:2103.00065 — **r37**
- Damian, A., Ma, T., Lee, J. D. (2023, ICML), arXiv:2209.15594 — **r38**

**What the prior work establishes** (empirical/theoretical, quoted):
- r37: *"Gradient descent operates in a non-monotonic regime where the top Hessian eigenvalue progressively sharpens until hovering near $2/\eta$."* Limitation: *"Focuses on scalar step-size stability boundaries; does not analyze the competitive transverse stability between shortcut and schema representations."*
- r38: EOS dynamics *"can be modeled continuously by augmenting gradient flow with implicit third-order curvature coupling potentials"* — i.e., modified continuous systems capture discrete EOS transitions (consistent with `literature-audit.md` §6.6).

**Paper 02 contrast:**
- **(T)** Paper 02 tracks the stability *exchange of orthogonal representation subspaces* ($S$ vs $C$) rather than a scalar sharpness eigenvalue: the control parameter is the *structural pressure* $\lambda$ in loss-weight space, not the learning rate $\eta$ in step-size space; the boundary is the transverse eigenvalue $\mu_\perp(\lambda) = 0$, i.e. $\lambda_{\text{crit}} = b_C/a_C$ (ADR-001, CLM-001).
- **(I)** The two concerns are orthogonal in mechanism (optimizer step-size stability vs. loss-composition stability) and can coexist: Paper 02's deterministic subspace flow belongs to the same *modified* continuous-flow family that r38 shows can represent EOS, extended from scalar sharpness to multi-objective subspace competition (see `literature-audit.md` §6.6, Claim 6).

**Structural discriminator:**
| Axis | EOS (r37, r38) | Paper 02 |
|---|---|---|
| Stability object | top Hessian eigenvalue $\lambda_{\text{max}}(H)$ | transverse eigenvalue $\mu_\perp = \lambda a_C - b_C$ of the $S \to C$ exchange |
| Control parameter | learning rate $\eta$ (vs $2/\eta$ boundary) | structural pressure $\lambda$ (vs $\lambda_{\text{crit}}$ boundary) |
| Regime | finite-step discrete SGD, non-monotonic oscillations | continuous gradient flow (modified, subspace-reduced) |
| Output | sharpness bound / non-blow-up containment | representation-formation phase boundary (T) |

**Claim tags:** r37/r38 statements = **(E/T)** of that work; $\mu_\perp$ boundary = **(T)** (CLM-001); mechanism-orthogonality framing = **(I)**.

---

### 2.4 Vs. Standard Compositional Generalization Literature

**Anchor works (survey rows):**
- Lake, B. M., Baroni, M. (2018, ICML), arXiv:1711.00350 — **r49**
- Kim, N., Linzen, T. (2020, EMNLP), arXiv:2010.05465 — **r50**
- Supporting: Hacohen & Weinshall (2019, ICML), arXiv:1904.03626 — **r55**

**What the prior work establishes** (empirical, quoted):
- r49: *"Standard sequence-to-sequence neural networks achieve near-perfect in-distribution accuracy but fail catastrophically at zero-shot compositional recombination on SCAN."* Limitation: *"Foundational empirical benchmark paper establishing compositional failure; supplies no dynamical systems explanation or critical threshold law."*
- r50: *"Transformers and LSTMs fail systematically on syntactic and semantic structural recombinations (e.g. passive to active voice, novel primitive modifier bindings)."* Limitation: *"Benchmark paper documenting failure modes across 21 syntactic splits; does not model loss-space optimization dynamics or representation bifurcations."*
- r55: curriculum learning *"accelerates convergence speed but does not alter the asymptotic global minimum"* — the empirical premise behind Paper 02's static-$\lambda$ framing (Paper 01 v2 fixed-weight parity, $\Delta = -0.01\text{ pp}$, TOST-equivalent within $\pm 2.5\%$; `planning/literature-audit.md` §1.2).

**Paper 02 contrast:**
- **(T)** Prior work documents failure or proposes heuristic architectures; Paper 02 *derives the exact critical threshold condition* $\lambda_{\text{crit}} = b_C/a_C$ from continuous gradient flow (CLM-001), turning the empirical failure into a falsifiable phase-boundary law.
- **(E, decide-at-P03)** The law predicts a *sharp* escape-probability phase boundary (CLM-003) and late-onset recovery under supercritical pressure (CLM-004), both testable on SCAN/COGS/H-Bar (CLM-007, `keep`).
- **(I)** Paper 02 takes r49/r50 as *empirical premises* (support-disjoint zero-shot splits, CC.4.2), not as targets of critique; its novelty claim is the missing threshold law, not a denial of the documented failures.

**Structural discriminator:**
| Axis | Compositional literature (r49, r50) | Paper 02 |
|---|---|---|
| Contribution type | empirical failure documentation / benchmark construction | mechanistic theory of *when and why* failure is stable |
| Remedy type | heuristic architectures / curricula | closed-form critical pressure (T) + late-onset recovery (E) |
| Order parameter | exact sequence accuracy (ID vs OOD) | escape probability, CKA/RGA, transverse coordinate $v(t)$ |
| Split regime | zero-shot OOD recombination (premise, shared) | zero-shot OOD recombination (object of the law) |

**Claim tags:** r49/r50/r55 statements = **(E)** of that work; threshold derivation = **(T)** (CLM-001); sharp-boundary/recovery predictions = **(E, decide-at-P03)** (CLM-003/004); premise framing = **(I)**.

---

### 2.5 Note: Vs. Bifurcations & Phase Transitions in Learning (closest-formalism neighbor)

**Anchor works (survey rows):**
- Park, D., Sompolinsky, H., et al. (2026, NeurIPS), arXiv:2602.04512 — **r1**
- Ziyin, L., Ueda, N. (2023, ICLR), arXiv:2302.01234 — **r2**
- Biroli, G., Mézard, M., et al. (2020, Phys. Rev. E), DOI 10.1103/PhysRevE.102.032115 — **r4**
- Montanari, A., Wang, F. (2026, Ann. Statist.), arXiv:2602.01434 — **r5**
- Cooper, Y. (2018, arXiv), arXiv:1810.12059 — **r7**
- Sorscher, B., Sompolinsky, H. (2022, PRL), DOI 10.1103/PhysRevLett.128.258301 — **r9**
- Li, Z., Arora, S., et al. (2021, ICML), arXiv:2103.04567 — **r10**
- Wang, K. (2026, arXiv Preprint), arXiv:2604.04655 — **r11**

**What the prior work establishes** (quoted):
- r2: loss landscapes contain *"pitchfork and transcritical bifurcation boundaries where critical learning rates dictate symmetry breaking"* — the closest existing formalism to Paper 02's transcritical claim, but *"restricted to toy weight-symmetry breaking; lacks explicit task vs schema subspace decomposition…"*
- r4: dynamical phases in deep *linear* networks; r7: discrete GD two-phase dynamics *"that naive continuous gradient flow fails to capture"* (the §6.6 motif); r9: replica-symmetry breaking of *static frozen* manifolds, not their dynamical formation; r10: trajectory bifurcation near generic saddle manifolds *"does not isolate shortcut vs schema representation subspaces."*
- r1: BBP spectral transitions in generic clustering; r5: sample-complexity threshold for two-layer networks *"does not address deep sequence architectures or compositional generalisation."*
- r11: gradient-field avalanches exhibit self-organized criticality, but *"lacks closed-form threshold conditions on supervision loss weights."*

**Paper 02 relation** **(I):** This cluster is Paper 02's *primary citation neighborhood* (shared formalism: bifurcation theory of gradient flow). The gap the cluster leaves open — stated by the rows themselves — is the absence of (i) an explicit task-vs-schema subspace decomposition (r2, r10), (ii) closed-form supervision thresholds (r1, r11), and (iii) application to compositional sequence architectures (r4, r5). Paper 02's two-subspace transcritical analysis (CLM-001) is positioned as the direct continuation of r2/r10's bifurcation program in the compositional setting.

**Claim tags:** r1/r2/r4/r5/r7/r9/r10/r11 statements = **(E/T)** of that work; positioning judgment = **(I)**.

---

## 3. Discrimination Matrix (Summary)

| Cluster | Anchor rows | Order parameter | Threshold type | Split regime | Equilibrium character | Closest-in-kind claim |
|---|---|---|---|---|---|---|
| Grokking | r13, r14 | validation acc / circuit loss | none (spontaneous) | i.i.d. | metastable plateau, self-escape | delayed generalization |
| SLT | r25, r26 | RLCT / LLC | statistical (basin complexity) | — | diagnostic probe | singular model complexity |
| EOS | r37, r38 | $\lambda_{\text{max}}(H)$ | step-size $2/\eta$ | i.i.d. | sharpening equilibrium | sharpness dynamics |
| Compositional | r49, r50 | exact sequence accuracy | none | zero-shot OOD | documented failure (stable) | empirical failure |
| Bifurcations | r1, r2, r4, r5, r7, r9, r10, r11 | spectral/saddle quantities | critical rates / sample counts | — | landscape phase boundaries | phase transitions in learning |
| **Paper 02** | — | escape probability, CKA/RGA, $v(t)$ | **$\lambda_{\text{crit}} = b_C/a_C$ (loss weight, T)** | **zero-shot OOD** | **asymptotically stable trap $E_S$; supercritical escape (T/E)** | **transcritical stability exchange (CLM-001)** |

---

## 4. Synthesis & Gap Implication (feeds Task 1.4)

Across all five clusters, prior work either (i) documents *i.i.d.* delayed generalization without addressing stable OOD failure (r13, r14), (ii) offers *diagnostics* of basin complexity rather than escape thresholds (r25, r26), (iii) characterizes *optimizer* stability rather than *loss-composition* stability (r37, r38), (iv) documents compositional failure *without* a dynamical mechanism (r49, r50), or (v) applies bifurcation theory to generic, toy, or linear landscapes *without* a task-vs-schema subspace decomposition (r2, r10) or a closed-form supervision threshold (r1, r11).

This clustering directly supports the **Novelty Proposition** (verbatim, Phase P01 Task 1.4):

> *"No existing framework derives a closed-form critical supervision threshold for compositional representation formation from continuous gradient flow, nor characterizes the resulting transcritical stability exchange."*

The proposition is scoped by construction: its own terms — *closed-form critical supervision threshold*, *continuous gradient flow*, *transcritical stability exchange* — delimit the claim to Paper 02's two-subspace formalism; it asserts neither the absence of any related dynamical-systems or grokking work, nor priority over SLT/EOS diagnostics.

---

## 5. Traceability & Claim Discipline

- **Row-level citations:** every prior-work statement above carries its `survey_table.csv` row ID + arXiv/DOI (see §2). No citation is asserted beyond the curated table, except the two primary-source details flagged in §1 (grokking step counts; Paper 01 v2 extended-horizon figures).
- **Ledger mapping:** CLM-001 (two-subspace stability exchange, **T**), CLM-002 ($R_0 = 1$ isomorphism, **T**), CLM-003/004/005 (**E**, `decide-at-P03`), CLM-006 (WGCA, **E**), CLM-007 (cross-benchmark, **E**).
- **CC.3.3 tripartite separation:** **(T)** model theorems are confined to ADR-001/CLM-001–002; **(E)** empirical findings cite Paper 01 v2 baselines (as summarized in `planning/literature-audit.md` §1.1–1.3) or carry `decide-at-P03`; **(I)** interpretations are flagged and grounded in cited `Limitation_Identified` fields.
- **Standards:** complies with CC.3.3 (writing discipline) and CC.6.1 (commit format). No prior-phase artifact is modified or discarded (CC.6.2); this document is additive.
- **Status of the phase:** Tasks 1.1–1.3 of P01 are complete; Task 1.4 (gap memo + ADR-004) and the `[HUMAN-GATE]` on novelty positioning remain open.

# Master Summary — σ-Trap Systematic Review

**Document type:** Phase 0.5 exit artifact — compiled key decisions across all 14 research files
**Purpose:** Single reference for Phase 1 (protocol) onward; eliminates need to re-read all research docs
**Status:** Final
**Cross-references:** All 14 research files in `research/`, `phases/01_protocol.md`–`phases/99_finale.md`

---

## 1. PICO Framework

Five PICO blocks (defined in `search-terms.md`):

| Block | P (Population) | I/C (Intervention/Comparator) | O (Outcome) | S/B (Setting/Benchmark) |
|---|---|---|---|---|
| **A — σ-trap detection** | Neural network models | Standard SGD / Adam | ID-OOD accuracy gap | SCAN, COGS, CFQ, PCFG-SET, gSCAN |
| **B — σ-targeting interventions** | Neural network models | SAM, ASAM, SWAD, entropy-SGD, MESA vs SGD/Adam | Δ ID-OOD gap, Δ OOD accuracy | WILDS, PACS, OfficeHome, VLCS, TerraIncognita, DomainNet |
| **C — non-σ interventions** | Neural network models | Curriculum, augmentation, meta-learning, IRM, contrastive vs SGD/Adam | Δ ID-OOD gap, Δ OOD accuracy | Same as B |
| **D — schema coherence** | Neural network models | Any training regime | Schema coherence proxy (probing, RSA, CKA, clustering) | Any benchmark |
| **E — safety connection** | Neural network / RL agents | Any training regime | Goal misgeneralization, reward hacking, deceptive alignment | CoinRun, BBQ, HANS, custom |

---

## 2. σ-Trap Formal Definition

**σ-trap** (defined in `sigma-trap-boundary.md` §1): A training dynamic where a model converges to a sharp minimum (low σ<sub>A</sub>) that achieves high in-distribution accuracy but fails on out-of-distribution inputs because the learned representations encode dataset-specific shortcuts rather than the compositional / causal structure of the task.

**Formal:** A model f<sub>θ</sub> exhibits the σ-trap when ∃ a perturbation δ such that:
- L<sub>ID</sub>(f<sub>θ</sub>) ≈ L<sub>ID</sub>(f<sub>θ+δ</sub>) (equivalent ID loss)
- L<sub>OOD</sub>(f<sub>θ+δ</sub>) << L<sub>OOD</sub>(f<sub>θ</sub>) (lower OOD loss for flatter minima)

**σ<sub>A</sub>** = sharpness metric computed as the maximum eigenvalue of the Hessian (λ<sub>max</sub>) or the trace of the Fisher information matrix. Lower values indicate flatter minima and correlate with OOD generalization.

### Taxonomic boundary

| Not σ-trap | Why excluded |
|---|---|
| Catastrophic forgetting | Sequential learning, not single-model convergence |
| Adversarial vulnerability | Worst-case perturbations, not systematic OOD |
| Overfitting (ID gap) | ID performance degrades; σ-trap preserves high ID |
| Domain adaptation | Uses target-domain data; σ-trap is fully unsupervised OOD |
| Simple data shift without shortcut reliance | Lacks the schema-coherence mediation mechanism |

---

## 3. Key Decisions

| # | Decision | Choice | Source | Rationale |
|---|---|---|---|---|
| 1 | Effect size (primary) | Log odds ratio (LOR) | `meta-analysis-feasibility.md` §2 | Scale-free, symmetric, variance-stabilizing; derivable from accuracy + n |
| 2 | Effect size (secondary) | Hedges' g | `meta-analysis-feasibility.md` §2 | For continuous metrics (BLEU, perplexity) |
| 3 | Effect size (avoid) | Raw Δ accuracy | `meta-analysis-feasibility.md` §2 | Cannot pool across benchmarks with different baselines |
| 4 | Pooling model | Three-level RVE with benchmark-as-random-effect | `meta-analysis-feasibility.md` §3 | Handles dependency from multiple per-benchmark outcomes; `metafor::rma.mv` + `clubSandwich` |
| 5 | Heterogeneity | REML τ² estimator, HKSJ CIs | `meta-analysis-feasibility.md` §4 | Standard in meta-analysis; HKSJ mandatory when k < 40 |
| 6 | ROB domains | 6-domain σ-ROB | `quality-criteria.md` §§1–6 | Adapted QUADAS-2 + ROBINS-I + PROBAST+AI; External Validity is the 6th domain |
| 7 | Preprint handling | Include, with preprint covariate | `review-methodology.md` §5 | Sensitivity test by exclusion |
| 8 | Search strategy | Primary + secondary Boolean + grey literature | `search-terms.md` §4 | Primary captures 92.6% of landmark papers; safety papers need grey lit |
| 9 | Extraction | 2 independent extractors, κ ≥ 0.70 | `extraction-template.md` §5 | Double-coding with escalation; pilot on 5 papers |
| 10 | Meta-analysis threshold | k ≥ 10 for random-effects; k ≥ 5 for subgroups | `meta-analysis-feasibility.md` §4 | Otherwise narrative synthesis + vote-count + Albatross plot |
| 11 | Publication bias | Funnel plot + Egger + trim-and-fill (if k ≥ 10) | `meta-analysis-feasibility.md` §6 | Pre-registered in SAP |
| 12 | Schema coherence proxy | Multiple (probing, RSA, CKA, clustering) — not one primary | `coherence-proxies.md` §1 | Field lacks consensus on best proxy; use all available |
| 13 | Theoretical framework | Simplicity bias (Teney et al. 2021) — strongest match | `theoretical-frameworks.md` §3 | NTK and capacity bounds do not predict OOD failure direction |
| 14 | Safety bridge | Compositional gen → alignment bridge = open contribution | `safety-connection.md` §5 | No paper explicitly connects σ-trap to alignment failure |

---

## 4. Gap Analysis Summary

| Gap | Confidence | Impact on thesis | Source |
|---|---|---|---|
| G1: No pooled ID-OOD gap estimate exists | High | Paper 02's primary contribution | `existing-reviews.md` §4 |
| G2: No intervention effect-size comparison across σ-targeting methods | High | Paper 02's secondary contribution | `existing-reviews.md` §4 |
| G3: Schema coherence lacks validated measure; no meta-analytic synthesis of proxy-outcome correlation | Low (no validated measure exists) | Candidate contribution for Paper 03 | `coherence-proxies.md` §4 |
| G4: No explicit bridge from compositional gen failure to alignment failure | Low-Speculative | ← Σ-Model's novel contribution (Paper 07) | `safety-connection.md` §5 |
| G5: Several required benchmarks lack extractable ID/OOD numerics | Medium | Phase 2 search calibration needed | `empirical-evidence.md` §4 |
| G6: ML-specific meta-analytic methods lack consensus | Medium | Method contribution for Paper 02 | `review-methodology.md` §1 |

### Thesis dependency graph

```
Paper 02 (Systematic Review) ──feeds──→ Paper 03 (Schema Coherence)
     │                                       │
     │                                       └──feeds──→ Paper 07 (Σ-Model)
     └──provides gap G4 justification ────────→ Paper 03 method
```

---

## 5. Evidence Readiness

| Benchmark | Papers found | ID/OOD extractable? | Missing data |
|---|---|---|---|
| SCAN | 6+ | Yes (most papers report both) | Sometimes seed-level SD missing |
| COGS | 4 | Yes | Small n; many single-seed |
| CFQ | 3 | Yes | Only best-of-N reported in key papers |
| PCFG-SET | 3 | Partial | Split details vary |
| gSCAN | 2 | Partial | Abstract but accuracy reported |
| WILDS (Camelyon17, FMoW, PovertyMap, CivilComments) | 6 | Yes (standardized leaderboard) | Subgroup data (per-domain) sometimes missing |
| PACS / OfficeHome / VLCS / TerraIncognita / DomainNet | 10+ | Yes (standardized evaluation) | Seed-level variance incompletely reported |
| ImageNet-C/-R/-A | 5 | Yes | CIs rarely reported |
| ColoredMNIST / Waterbirds / CelebA | 4 | Yes | Spurious correlation setting is standard |
| COFE / MathQA / QED / NACS / SQuAD comp. | 0–1 each | Unknown | Need Phase 2 capture |

**Missing-data strategy** (`extraction-template.md` §4.2): Tier 1 (full) if effect size derivable; Tier 2 (partial, narrative only) if not; Tier 3 (author contact) if <50% required fields.

---

## 6. Search Strategy Summary

| Property | Value | Source |
|---|---|---|
| Primary Boolean strings | 5 PICO-specific (SCN, WLS, INT, SAF, REP) | `search-terms.md` §3 |
| Secondary (snowball) | Reference + citation harvesting from 27 landmark papers | `search-terms.md` §4 |
| Grey literature | Submit to ML-Safety arXiv lists, Anthropic papers, alignment forum | `search-terms.md` §4 |
| Recall validation | 92.6% of 27 landmark papers (primary+secondary); 100% with grey | `search-terms.md` §4 |
| Databases | Scopus, Web of Science, ACM DL, IEEE Xplore, arXiv (api), PsycINFO | `search-terms.md` §4.8 |
| Syntax notes | Scopus truncation: comp*; WoS lemmatization may double-count | `search-terms.md` §4.8 |
| Too broad diagnostics | "deep learning" AND "out-of-distribution" → 15,000+ hits (need PICO narrowing) | `search-terms.md` §4.6 |

---

## 7. Meta-Analysis Plan

**Feasibility verdict:** Feasible with caveats (see `meta-analysis-feasibility.md` §1).

| Decision | Value |
|---|---|
| Primary effect size | Log odds ratio (LOR) = ln((ID_acc/(1-ID_acc)) / (OOD_acc/(1-OOD_acc))) |
| Secondary effect size | Hedges' g |
| Pooling model | Three-level random-effects: (1) within-study, (2) between-study, (3) between-benchmark |
| Software | `metafor::rma.mv` (R), `clubSandwich` for robust CIs |
| Heterogeneity estimator | REML |
| CIs | HKSJ (Hartung-Knapp-Sidik-Jonkman) adjustment |
| Pre-specified subgroups (8) | By intervention type, architecture, benchmark, model scale, training data size, OOD split type, peer-review status, year |
| Minimum k per meta-analysis | 10 (random-effects); 5 (subgroup) |
| Publication bias battery | Funnel plot + Egger + Begg + trim-and-fill + PET-PEESE + selection models + preprint covariate + time-lag bias |
| If meta-analysis infeasible | Narrative synthesis + vote-count + Albatross plot |

---

## 8. Safety Connection

Six alignment failure modes mapped to σ-trap (`safety-connection.md` §3):

| Failure mode | σ-trap mechanism | Papers |
|---|---|---|
| Mesa-optimization | Sharp minima → fragile objective channel | Hubinger et al. 2019 |
| Goal misgeneralization | Representations encode proxy goals, not true intent | Shah et al. 2022; Langosco et al. 2022 |
| Specification gaming | Shortcut exploitation | Krakovna et al. 2020 |
| Deceptive alignment | Few-shot OOD reversion (similar to σ-trap reset) | Ngo et al. 2022; Hubinger et al. 2021 |
| Reward model hacking | RM exploits spurious features (σ-trap in RLHF) | Gao et al. 2022; Perez et al. 2022 |
| Representation quality → safety | Low σ<sub>A</sub> → unreliable intermediate representations | Geiger et al. 2021; Mueller et al. 2024 |

**Key finding:** No paper explicitly bridges compositional generalization failure (σ-trap) to alignment failure — this is the thesis's open contribution.

---

## 9. Remaining Risks

| Risk | Severity | Mitigation |
|---|---|---|
| k < 10 studies with extractable LOR in primary comparison | High | Narrative synthesis + vote-count planned; SAP already specifies fallback |
| Schema coherence proxies too heterogeneous to pool | Medium | No pooled effect planned for proxy-outcome correlation; narrative synthesis |
| Safety connection papers require grey literature | Medium | Grey literature strategy in `search-terms.md` §4 |
| Single-arch findings may dominate (Transformer vs RNN) | Medium | Architecture subgroup pre-specified; sensitivity analysis |
| σ-trap phenomenon may be named differently across papers | Medium | Search terms include 20+ synonyms for σ-trap (simple-solvable, procedural, compositional generalization gap, etc.) |
| Validation: no existing meta-analysis to replicate | Low | Methodological novelty accepted; transparent reporting via PRISMA |

---

## 10. Quick-Reference Tables

### 10.1 Landmark Papers (27)

| # | Paper | Area | Benchmark | σ? | Code? |
|---|---|---|---|---|---|
| L1–L10 | See `landmark-papers.md` §1 | Diagnostic (10) | SCAN, COGS, CFQ, PCFG-SET, gSCAN, WILDS, etc. | — | Various |
| L11–L16 | See `landmark-papers.md` §2 | Probing (6) | SCAN, COGS, CFQ, PCFG-SET | — | Various |
| L17–L27 | See `landmark-papers.md` §3 | Interventions (11) | SCAN, WILDS, PACS, etc. | SAM, ASAM, SWAD, etc. | Various |

### 10.2 Interventions (24, across 7 families)

| Family | Count | Examples | Cost tier | Source |
|---|---|---|---|---|
| σ-targeting | 6 | SAM, ASAM, Friendly-SAM, Tilted-SAM, SWAD, MESA | Medium–High | `interventions.md` §2 |
| Regularization | 4 | Weight decay, dropout, label smoothing, Mixout | Low | `interventions.md` §3 |
| Data augmentation | 4 | Mixup, CutMix, AugMix, RandAugment | Low–Medium | `interventions.md` §4 |
| Representation learning | 4 | Contrastive, IRM, DANN, V-REx | Medium | `interventions.md` §5 |
| Prediction-based | 3 | Self-training, knowledge distillation, MC Dropout | Low–Medium | `interventions.md` §6 |
| Architecture | 2 | Neuro-symbolic, modular networks | High | `interventions.md` §7 |
| Sequential | 1 | Curriculum learning | Low | `interventions.md` §8 |

### 10.3 Schema Coherence Proxies (7 families)

| Proxy | Papers | Cost | Validation | Source |
|---|---|---|---|---|
| Probing | 10+ | Low | Well-established | `coherence-proxies.md` §2 |
| RSA | 5 | Medium | Cognitive science validated | `coherence-proxies.md` §3 |
| CKA | 5 | Medium | ML community standard | `coherence-proxies.md` §4 |
| Effective rank | 4 | Low | Information-theoretic | `coherence-proxies.md` §5 |
| Clustering quality | 4 | Medium | Correlates with generalization | `coherence-proxies.md` §6 |
| NTK alignment | 3 | High | Analytic but expensive | `coherence-proxies.md` §7 |
| Mutual information | 3 | Medium | Ground-truth factors needed | `coherence-proxies.md` §8 |

### 10.4 Theoretical Frameworks (7)

| Framework | Match to σ-trap | Predicts OOD failure? | Source |
|---|---|---|---|
| Simplicity bias | Strongest | Yes — OOD requires complex features | `theoretical-frameworks.md` §2 |
| NTK linearization | Weak | Does not predict direction of failure | `theoretical-frameworks.md` §3 |
| Capacity bounds (VC, Rademacher) | Moderate | Overparameterization decreases OOD but bound is vacuous | `theoretical-frameworks.md` §4 |
| Information bottleneck | Moderate | Compression phase may discard compositional structure | `theoretical-frameworks.md` §5 |
| Loss landscape geometry | Strong | Sharp minima → OOD fragility | `theoretical-frameworks.md` §6 |
| Compositional learning theory | Strong | Compositional generalization requires algebraic structure | `theoretical-frameworks.md` §7 |
| PAC-Bayes | Strong | Flat minima have tighter generalization bounds | `theoretical-frameworks.md` §8 |

---

## 11. Phase Dependency Map

```
Phase 0.5 (Research) ──feeds──→ Phase 1 (Protocol)
     │                              │
     │                              ├──→ Phase 2 (Search Calibration) ──→ Phase 3 (Database Search)
     │                              │                                        │
     │                              │                                        └──→ Phase 4 (Deduplication)
     │                              │                                                  │
     │                              │                                                  └──→ Phase 5 (Screening)
     │                              │                                                            │
     │                              │                                                            ├──→ Phase 6 (Full Text) ──→ Phase 7 (Extraction)
     │                              │                                                            │                          │
     │                              │                                                            │                          └──→ Phase 8 (Quality Assessment)
     │                              │                                                            │                                    │
     │                              │                                                            │                                    └──→ Phase 9 (Synthesis)
     │                              │                                                            │                                              │
     │                              │                                                            │                                              └──→ Phase 10 (First Draft)
     │                              │                                                                                                                        │
     │                              ├──→ Phase 11 (Revision) ←─────────────────────────────────────────────────────────────────────────────────────────────────┘
     │                              │
     └──→ Phase 99 (Finale)
```

---

## 12. File Inventory

| # | File | Area | Lines | Feeds |
|---|---|---|---|---|
| 1 | `sigma-trap-boundary.md` | A.1 | 201 | Phase 1 (criteria) |
| 2 | `landmark-papers.md` | A.2 | 445 | Phase 2 (calibration) |
| 3 | `coherence-proxies.md` | A.3 | 283 | Phase 7 (extraction template) |
| 4 | `empirical-evidence.md` | B.1 | 362 | Phase 9 (synthesis) |
| 5 | `interventions.md` | B.2 | 445 | Phase 2 (search), Phase 9 |
| 6 | `theoretical-frameworks.md` | B.3 | 170 | Phase 1 (background) |
| 7 | `existing-reviews.md` | C.1 | 149 | Phase 1 (gap justification) |
| 8 | `review-methodology.md` | C.2 | 208 | Phase 8 (ROB), Phase 9 (meta) |
| 9 | `meta-analysis-feasibility.md` | C.3 | 257 | Phase 9 (SAP) |
| 10 | `safety-connection.md` | D.1 | 153 | Paper 07 (thesis bridge) |
| 11 | `gap-analysis.md` | D.2 | 183 | Phase 1, Paper 03, Paper 07 |
| 12 | `search-terms.md` | E.1 | 363 | Phase 2 (search strategy) |
| 13 | `extraction-template.md` | E.2 | 530 | Phase 7 (extraction) |
| 14 | `quality-criteria.md` | E.3 | 556 | Phase 8 (ROB assessment) |
| 15 | **`master-summary.md`** | **Exit** | **this** | **All phases** |

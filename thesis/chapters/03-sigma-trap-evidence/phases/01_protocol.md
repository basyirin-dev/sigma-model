# Phase 1 — Research Question & Protocol

**Duration**: 1 week (Month 1)
**Deadline**: 2026-07-31
**Dependencies**: Phase 0.5 (research artifacts completed)
**Output**: Registered protocol on PROSPERO (and OSF) with finalized PICO question, objectives, and inclusion/exclusion criteria

---

### Task 1.1: Finalize Research Question

- [x] 1.1.1: Review Phase 0.5 research outputs — especially `research/sigma-trap-boundary.md`, `research/gap-analysis.md`, `research/empirical-evidence.md`
  - All 14 research artifacts drafted and reviewed; citations validated (see research artifacts)
  - Key finding: 11 core studies with extractable ID-OOD numerics confirmed; 4 citation errors in `sigma-trap-boundary.md` corrected
  - **PICO operational note**: The primary PICO below is operationalized across five search domains (A: σ-trap detection, B: σ-targeting interventions, C: non-σ interventions, D: schema coherence proxies, E: safety connection) as defined in `research/master-summary.md` §1
- [x] 1.1.2: Refine the overarching research question using PICO (Population, Intervention, Comparison, Outcome) framework:
  - **Population**: Neural network models trained with gradient-based optimization on compositional generalization or out-of-distribution (OOD) tasks
  - **Intervention**: Any training intervention that explicitly or implicitly targets schema coherence (σ_A), including curriculum learning, data augmentation, multi-task learning, representation regularization, meta-learning, coupling interventions
  - **Comparison**: Standard SGD baseline or non-targeted training
  - **Outcome**: OOD / compositional generalization accuracy; ID-OOD gap (primary); schema coherence proxy measures; representation quality metrics (secondary)
- [x] 1.1.3: Finalized primary and secondary research questions:
  - **Primary**: In neural network models trained via gradient-based optimization, what is the effect of σ-targeting training interventions on compositional out-of-distribution generalization performance compared to standard SGD?
  - **Secondary 1**: What empirical evidence exists for the σ-trap (stable low-σ_A equilibrium) across benchmarks and architectures?
  - **Secondary 2**: What proxy measures of schema coherence have been validated, and how do they correlate with OOD performance?
  - **Secondary 3** [demoted to exploratory synthesis in Discussion]: What is the relationship between σ-trap failure and alignment failure modes (mesa-optimization, deceptive alignment)?
    - *Rationale*: `research/gap-analysis.md` confirms "Low-Speculative" confidence with no paper explicitly connecting σ-trap to alignment failure. Formal systematic search would yield zero included studies. Retained as theoretical synthesis in Discussion.
- [x] 1.1.4: Draft explicit objectives using SMART framework:
  - **O1 (Evidence mapping)**: Systematically identify all empirical studies (2017–2026) reporting both ID and OOD accuracy on compositional generalization benchmarks in neural networks, producing an evidence map of ≥20 studies with extractable effect sizes. [S: ID+OOD reporting; M: ≥20 studies; A: 6 databases + snowball; R: core evidence base; T: Phase 3 (2026-08-14) + Phase 7 (2026-10-16)]
  - **O2 (Gap quantification)**: Quantify the pooled ID-OOD accuracy gap via log odds ratio random-effects meta-analysis (three-level RVE, REML τ², HKSJ CIs) if k≥10; otherwise deliver a structured narrative synthesis with per-study effect-size catalog and Albatross plot. [S: LOR with 95% CI; M: meta-analysis threshold k≥10; A: pre-specified SAP in `research/meta-analysis-feasibility.md`; R: primary quantitative contribution; T: Phase 9 (2026-12-04)]
  - **O3 (Intervention catalog)**: Catalog all training interventions from included studies with extractable OOD effect sizes, grouped by intervention family (σ-targeting, regularization, augmentation, representation learning, architectural), with subgroup meta-analysis if k≥5 per group. [S: intervention-by-family catalog; M: subgroup thresholds; A: 24 candidate interventions mapped in `research/interventions.md`; R: informs Paper 03 conceptual framework; T: Phase 9 (2026-12-04)]
  - **O4 (Proxy correlation)**: Map the relationship between schema coherence proxy measures (probing, RSA, CKA, effective rank, clustering) and OOD generalization performance across studies reporting both, via narrative synthesis of proxy-outcome correlations. [S: proxy→OOD correlation mapping; M: narrative synthesis (pooling infeasible per `research/coherence-proxies.md`); A: 7 proxy families documented; R: foundational for Paper 03 methodology; T: Phase 9 (2026-12-04)]
- [x] 1.1.5: Satisfy CC.1.4 — inclusion/exclusion criteria drafted concurrently with question (see Task 1.2 below)

### Task 1.2: Define Inclusion/Exclusion Criteria

- [x] 1.2.1: Inclusion criteria (with PICO mapping):
  - **P (Population)**: Studies that train neural network models (any architecture: RNN, LSTM, GRU, Transformer, CNN, MLP, ODE) on compositional generalization or OOD tasks
  - **I (Intervention)**: Studies that report OOD or compositional generalization performance on at least one held-out test split that requires recombination of learned primitives
  - **C (Comparison)**: Studies that include a baseline condition (standard SGD, standard training pipeline) OR report ID accuracy alongside OOD accuracy (allowing within-study gap calculation)
  - **O (Outcome)**: Studies that report quantitative accuracy, error rate, or performance metric on both ID and OOD/test splits
  - **Study design**: Peer-reviewed journal paper, peer-reviewed conference paper, arXiv preprint, or technical report
  - **Language**: Written in English
  - **Date**: Published 2017–2026. *Justification*: SCAN (Lake & Baroni, 2018) is the formative benchmark for compositional generalization in neural networks; 2017 captures the arXiv preprint. Upper bound 2026 includes papers published during the review's execution.
- [x] 1.2.2: Exclusion criteria:
  - Studies on reinforcement learning without a compositional/OOD evaluation component (maps to P — RL without compositional eval is outside population)
  - Studies on generative models only (no discriminative task) (maps to O — no quantitative accuracy metric)
  - Studies on transfer learning or domain adaptation without a compositional structure (maps to I — not σ-trap relevant per `research/sigma-trap-boundary.md`)
  - Studies that discuss alignment failure modes only in RL without a compositional/OOD evaluation component in neural network training (maps to scope narrowing — Secondary 3 demoted)
  - Opinion pieces without empirical or theoretical substance (maps to study design)
  - Duplicate publications (same content — keep the most complete version)
  - Studies on biological neural networks (not artificial) (maps to P)
- [x] 1.2.3: Each criterion justified against Phase 0.5 findings (see PICO mapping above; cross-reference `research/sigma-trap-boundary.md` §Taxonomic Disambiguation for the σ-trap boundary definition that underpins the "compositional structure" requirement)
- [x] 1.2.4: Satisfy CC.1.4 — criteria explicitly stated before screening

### Task 1.3: Write Protocol

- [ ] 1.3.1: Draft protocol following PRISMA-P (PRISMA for Protocols) guidelines:
  - Title: "Schema Coherence and the σ-Trap: A Systematic Review and Meta-Analysis of Compositional Generalisation Failure in Neural Networks"
  - Abstract (structured)
  - Introduction / rationale — with explicit reference to the broader thesis
  - Research question(s) and objectives — PICO framework
  - Eligibility criteria (inclusion/exclusion with justifications)
  - Information sources (all databases, search dates)
  - Search strategy (summary; detailed strings deferred to Phase 2)
  - Study selection process (dual independent screening protocol)
  - Data collection process (extraction form template)
  - Data items (list of extracted variables)
  - Risk of bias assessment (tool and domains)
  - Synthesis methods (meta-analysis plan if feasible, narrative synthesis otherwise)
  - Meta-analysis plan (effect size measure, model, heterogeneity assessment, subgroup analyses, sensitivity analyses, publication bias assessment)
  - Confidence in cumulative evidence (GRADE)
- [ ] 1.3.2: Decide on staged approach (whether to search simultaneously or iteratively)
- [ ] 1.3.3: Protocol length: ~10-15 pages (PRISMA-P standard)
- [ ] 1.3.4: Satisfy CC.1.7 — register protocol on PROSPERO and OSF

### Task 1.4: Pilot Search Test

- [x] 1.4.1: Choose one representative database (e.g., Scopus or arXiv)
- [x] 1.4.2: Execute preliminary search with draft terms from Phase 0.5 `research/search-terms.md`
- [x] 1.4.3: Review 30-50 random results to verify the search captures known landmark papers (from Phase 0.5 `research/landmark-papers.md`)
- [x] 1.4.4: Calculate recall: known landmark papers captured / total landmark papers
- [x] 1.4.5: Adjust inclusion/exclusion criteria if pilot reveals missing or irrelevant results
- [x] 1.4.6: Record pilot search details (database, date, string, yield, recall, adjustments made)
- [x] 1.4.7: Satisfy CC.1.5 — data extraction form piloted on 5 papers from pilot search results

### Task 1.5: Protocol Registration

- [x] 1.5.1: PROSPERO assessed — not eligible (non-medical systematic review of computer science / AI literature)
- [x] 1.5.2: Protocol uploaded to OSF instead (see 1.5.4)
- [x] 1.5.3: OSF project created: "Schema Coherence and the σ-Trap — A Systematic Review"
- [x] 1.5.4: Protocol registered on OSF: https://osf.io/m3asw (Open-Ended Registration, 2026-07-08)
- [x] 1.5.5: Recorded OSF link in `README.md` and `protocol.tex`
- [x] 1.5.6: Satisfy CC.1.7 — protocol registered prior to formal search

---

**Phase 1 Exit Criteria**:
- [x] Research question finalized with PICO framework
- [x] Primary and secondary research questions explicitly stated
- [x] Inclusion/exclusion criteria explicitly stated with justifications
- [x] Protocol registered on OSF with public access (https://osf.io/m3asw); PROSPERO not applicable
- [x] Pilot search executed with recall assessment
- [x] Data extraction form piloted on 5 papers
- [x] CC.1.1 (template in place), CC.1.4 ✅, CC.1.5 ✅, CC.1.7 ✅ satisfied; CC.3.1 deferred to Phase 10
- [x] CC.5.3 satisfied — phase completion committed

# Phase 1 — Research Question & Protocol

**Duration**: 1 week (Month 1)
**Deadline**: 2026-07-31
**Dependencies**: Phase 0.5 (research artifacts completed)
**Output**: Registered protocol on PROSPERO (and OSF) with finalized PICO question, objectives, and inclusion/exclusion criteria

---

### Task 1.1: Finalize Research Question

- [ ] 1.1.1: Review Phase 0.5 research outputs — especially `research/sigma-trap-boundary.md`, `research/gap-analysis.md`, `research/empirical-evidence.md`
- [ ] 1.1.2: Refine the overarching research question using PICO (Population, Intervention, Comparison, Outcome) framework:
  - **Population**: Neural network models trained with gradient-based optimization on compositional generalization or OOD tasks
  - **Intervention**: Any training intervention that explicitly or implicitly targets schema coherence (σ_A), including curriculum learning, data augmentation, multi-task learning, representation regularization, meta-learning, coupling interventions
  - **Comparison**: Standard SGD baseline or non-targeted training
  - **Outcome**: OOD / compositional generalization accuracy; ID-OOD gap; schema coherence proxy measures; representation quality metrics
- [ ] 1.1.3: Draft the primary and secondary research questions:
  - **Primary**: In neural network models trained via gradient-based optimization, what is the effect of σ-targeting training interventions on OOD generalization performance compared to standard SGD?
  - **Secondary 1**: What empirical evidence exists for the σ-trap (stable low-σ_A equilibrium) across benchmarks and architectures?
  - **Secondary 2**: What proxy measures of schema coherence have been validated, and how do they correlate with OOD performance?
  - **Secondary 3**: What is the relationship between σ-trap failure and alignment failure modes (mesa-optimization, deceptive alignment)?
- [ ] 1.1.4: Draft explicit objectives using SMART framework
- [ ] 1.1.5: Satisfy CC.1.4 — inclusion/exclusion criteria drafted concurrently with question

### Task 1.2: Define Inclusion/Exclusion Criteria

- [ ] 1.2.1: Inclusion criteria:
  - Population: Studies that train neural network models (any architecture: RNN, LSTM, GRU, Transformer, CNN, MLP, ODE)
  - Intervention: Studies that report OOD or compositional generalization performance on at least one held-out test split
  - Comparison: Studies that include a baseline condition (standard SGD, standard training pipeline) OR report ID accuracy alongside OOD accuracy (allowing within-study gap calculation)
  - Outcome: Studies that report quantitative accuracy, error rate, or performance metric on both ID and OOD/test splits
  - Study design: Peer-reviewed journal paper, peer-reviewed conference paper, arXiv preprint, or technical report
  - Language: Written in English
  - Date: Published 2017–2026 (SCAN paper published 2018; formative years for the field)
- [ ] 1.2.2: Exclusion criteria:
  - Studies on reinforcement learning without a compositional/OOD evaluation component
  - Studies on generative models only (no discriminative task)
  - Studies on transfer learning or domain adaptation without a compositional structure
  - Opinion pieces without empirical or theoretical substance
  - Duplicate publications (same content — keep the most complete version)
  - Studies on biological neural networks (not artificial)
- [ ] 1.2.3: Justify each criterion with reference to Phase 0.5 findings (especially `research/sigma-trap-boundary.md`)
- [ ] 1.2.4: Satisfy CC.1.4 — criteria explicitly stated before screening

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

- [ ] 1.4.1: Choose one representative database (e.g., Scopus or arXiv)
- [ ] 1.4.2: Execute preliminary search with draft terms from Phase 0.5 `research/search-terms.md`
- [ ] 1.4.3: Review 30-50 random results to verify the search captures known landmark papers (from Phase 0.5 `research/landmark-papers.md`)
- [ ] 1.4.4: Calculate recall: known landmark papers captured / total landmark papers
- [ ] 1.4.5: Adjust inclusion/exclusion criteria if pilot reveals missing or irrelevant results
- [ ] 1.4.6: Record pilot search details (database, date, string, yield, recall, adjustments made)
- [ ] 1.4.7: Satisfy CC.1.5 — data extraction form piloted on 5 papers from pilot search results

### Task 1.5: Protocol Registration

- [ ] 1.5.1: Create PROSPERO account and register systematic review protocol
- [ ] 1.5.2: Upload protocol document to PROSPERO
- [ ] 1.5.3: Create OSF project for Paper 02 with supplementary materials
- [ ] 1.5.4: Upload protocol to OSF as well (for broader accessibility)
- [ ] 1.5.5: Record PROSPERO ID and OSF link in `README.md`
- [ ] 1.5.6: Satisfy CC.1.7 — protocol registered prior to formal search

---

**Phase 1 Exit Criteria**:
- [ ] Research question finalized with PICO framework
- [ ] Primary and secondary research questions explicitly stated
- [ ] Inclusion/exclusion criteria explicitly stated with justifications
- [ ] Protocol registered on PROSPERO and OSF with public access
- [ ] Pilot search executed with recall assessment
- [ ] Data extraction form piloted on 5 papers
- [ ] CC.1.1, CC.1.4, CC.1.5, CC.1.7, CC.3.1 satisfied
- [ ] CC.5.3 satisfied — phase completion committed

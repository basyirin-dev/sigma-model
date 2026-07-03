# Phase 7 — Data Extraction & Charting

**Duration**: 3 weeks (Month 3–4)
**Deadline**: 2026-10-16
**Dependencies**: Phase 6 (final included-studies list)
**Output**: Completed data extraction tables (CSV/JSON) and charted data ready for synthesis

---

### Task 7.1: Finalize Extraction Template

- [ ] 7.1.1: Review Phase 0.5 `research/extraction-template.md` and iterate based on full-text experience (5 pilot papers from Phase 6)
- [ ] 7.1.2: Finalize extraction fields for the systematic review:

  **Bibliographic:**
  - Study ID (S001–SXXX)
  - Title, authors, year, venue, DOI, URL

  **Study design:**
  - Publication type: peer-reviewed journal / peer-reviewed conference / arXiv preprint / technical report / PhD thesis / workshop paper
  - Study type: empirical (intervention) / empirical (measurement only) / theoretical / review
  - Number of independent seeds/runs reported

  **Task & benchmark:**
  - Benchmark name: SCAN / COGS / CFQ / PCFG-SET / gSCAN / COFE / MathQA / NACS / SQUAD-Comp / custom / other
  - Task type: semantic parsing / question answering / language modeling / vision / reasoning / navigation / other
  - OOD split type: primitive recombination / length generalization / novel composition / systematicity / productivity / substitutivity / compound divergence / other
  - OOD difficulty metric reported? (e.g., compound divergence score)

  **Model architecture:**
  - Architecture family: RNN / LSTM / GRU / Transformer / CNN / MLP / ODE / hybrid / other
  - Encoder type: bidirectional / unidirectional
  - Attention mechanism: none / additive / multiplicative / self-attention / cross-attention
  - Parameter count (if reported)
  - Number of layers
  - Hidden dimension
  - Embedding dimension

  **Training regime:**
  - Optimizer: SGD / Adam / AdamW / RMSProp / other
  - Learning rate (value, schedule if reported)
  - Batch size
  - Training epochs / steps
  - Data size (training examples)
  - Intervention type (if applicable): none (baseline) / curriculum learning / data augmentation / multi-task / meta-learning / regularization / representation learning / σ-coupling (additive) / σ-coupling (multiplicative) / architectural modification / pretraining / other
  - Intervention description (free text)

  **Results (critical for meta-analysis):**
  - ID accuracy reported: value / standard deviation / confidence interval / n
  - OOD accuracy reported: value / standard deviation / confidence interval / n
  - ID-OOD gap (calculated or extracted)
  - Effect size (Cohen's d, Hedges' g, or raw Δ) — calculated or extracted
  - Effect size confidence interval (if reported)
  - Statistical significance test used
  - Any other metrics reported (F1, precision, recall, perplexity, BLEU)

  **Schema coherence & representation analysis:**
  - Schema coherence proxy measured? yes / no / unclear
  - Proxy name (if yes): RSA dissimilarity / probing accuracy / cluster quality / mutual information / disentanglement / neural tangent kernel / other
  - Representation analysis method: probing / RSA / clustering / PCA / feature visualization / none
  - Representation metric value (if reported)
  - Correlation between representation metric and OOD performance (if reported)

  **Quality & relevance:**
  - Code available? yes / no / upon request
  - Data available? yes / no / upon request
  - Seeds reported? yes / partial / no
  - Limitations explicitly discussed? yes / partial / no
  - Relevance to σ-trap (1–5 scale, with justification)
  - Relevance to alignment/safety (1–5 scale, with justification)
  - Key limitations (free text)
  - Extracted by (reviewer initials)

- [ ] 7.1.3: Pilot extraction on 5 papers (already retrieved full text) — verify template covers all relevant information
- [ ] 7.1.4: Refine template based on pilot — add missing fields, merge redundant, clarify ambiguous field definitions
- [ ] 7.1.5: Satisfy CC.1.5 — data extraction form developed, piloted, and iterated

### Task 7.2: Full Data Extraction

- [ ] 7.2.1: Extract data from all included studies using finalized template — record in `research/charted-data.csv`
- [ ] 7.2.2: For each extraction: assign Study ID, complete all fields, add free-text notes
- [ ] 7.2.3: For studies with empirical results: extract effect sizes, datasets used, sample sizes (number of runs/seeds)
- [ ] 7.2.4: For studies reporting multiple OOD splits: extract data for each split separately (record in multiple rows with Split ID)
- [ ] 7.2.5: For studies reporting multiple architectures: extract data for each architecture separately
- [ ] 7.2.6: For studies reporting multiple interventions: extract data for each intervention vs baseline comparison

### Task 7.3: Extraction Validation

- [ ] 7.3.1: Second extractor (or AI) re-extracts 20% random sample of included studies
- [ ] 7.3.2: Calculate inter-extractor agreement for categorical fields (Cohen's κ)
- [ ] 7.3.3: Calculate inter-extractor correlation for continuous fields (ICC)
- [ ] 7.3.4: Resolve any systematic disagreements — refine template or criteria if needed
- [ ] 7.3.5: Satisfy CC.1.6 — dual extraction on validation sample

### Task 7.4: Data Quality Checks

- [ ] 7.4.1: Check for missing data: any fields with >10% missing values — decide whether to impute, exclude, or flag
- [ ] 7.4.2: Check for inconsistent coding: same value in different forms (e.g., "SCAN", "scan", "SCAN dataset")
- [ ] 7.4.3: Normalize controlled vocabulary fields (benchmark names, architecture types, intervention types)
- [ ] 7.4.4: Validate numerical fields — check for out-of-range accuracy values (>100% or <0%) or implausible effect sizes
- [ ] 7.4.5: Generate data quality report with completeness statistics

### Task 7.5: Charted Data Export

- [ ] 7.5.1: Export completed charted data as CSV: `research/charted-data.csv`
- [ ] 7.5.2: Export completed charted data as JSON: `research/charted-data.json`
- [ ] 7.5.3: Generate summary statistics:
  - Total studies charted
  - Distribution by publication type
  - Distribution by benchmark
  - Distribution by architecture
  - Distribution by intervention type
  - Distribution by year
  - Mean ID accuracy, mean OOD accuracy, mean gap
- [ ] 7.5.4: Create initial visualizations (bar charts, swarm plots, time series) for data familiarization
- [ ] 7.5.5: Satisfy CC.4.3 — charted data exported as CSV/JSON

---

**Phase 7 Exit Criteria**:
- [ ] Extraction template finalized and piloted
- [ ] All included studies extracted
- [ ] Extraction validation complete (κ ≥ 0.80, ICC ≥ 0.90)
- [ ] Data quality checks passed and documented
- [ ] Charted data exported (CSV + JSON)
- [ ] Summary statistics and initial visualizations generated
- [ ] CC.1.5, CC.1.6, CC.4.3 satisfied
- [ ] CC.5.3 satisfied — phase completion committed

# Phase 8 — Quality Assessment

**Duration**: 3 weeks (Month 4)
**Deadline**: 2026-11-06
**Dependencies**: Phase 7 (data extraction complete)
**Output**: Risk of bias assessments for all included studies; structured dataset for sensitivity analysis

---

### Task 8.1: Develop Risk of Bias Tool

- [ ] 8.1.1: Review Phase 0.5 `research/quality-criteria.md` for proposed risk of bias (RoB) domains
- [ ] 8.1.2: Adapt QUADAS-2 (for diagnostic accuracy studies) and PROBAST (for prediction models) to the ML experiment context
- [ ] 8.1.3: Define final RoB domains and signalling questions:

  **Domain 1 — Reproducibility (6 signalling questions):**
  - 1.1: Are random seeds reported for all experimental runs?
  - 1.2: Is the complete training configuration reported (optimizer, LR, batch size, epochs)?
  - 1.3: Is the model architecture specified in sufficient detail to reproduce?
  - 1.4: Is the data split procedure described exactly (ID vs OOD)?
  - 1.5: Is the evaluation metric clearly defined?
  - 1.6: Is the code publicly available?
  - RoB judgment: Low (≥5 Yes) / Unclear (3–4 Yes) / High (≤2 Yes)

  **Domain 2 — Benchmark Validity (5 signalling questions):**
  - 2.1: Is the OOD split genuinely compositional (not random)?
  - 2.2: Does the OOD split control for ID performance (i.e., not trivially harder)?
  - 2.3: Is the metric appropriate for the task?
  - 2.4: Are multiple OOD splits evaluated (not cherry-picked)?
  - 2.5: Are floor/ceiling effects discussed?
  - RoB judgment: Low (≥4 Yes) / Unclear (3 Yes) / High (≤2 Yes)

  **Domain 3 — Confounding & Fair Comparison (5 signalling questions):**
  - 3.1: Are comparisons between methods matched on architecture?
  - 3.2: Are comparisons matched on compute (parameters, FLOPs, training steps)?
  - 3.3: Are comparisons matched on data?
  - 3.4: Is the baseline reasonable and state-of-the-art (not straw-man)?
  - 3.5: Are multiple random seeds used (n ≥ 3)?
  - RoB judgment: Low (≥4 Yes) / Unclear (3 Yes) / High (≤2 Yes)

  **Domain 4 — Reporting Completeness (5 signalling questions):**
  - 4.1: Are both ID and OOD results reported?
  - 4.2: Is variability reported (SD, CI, error bars)?
  - 4.3: Are negative or null results reported (not just positive findings)?
  - 4.4: Are failure cases or error analyses discussed?
  - 4.5: Are limitations explicitly stated?
  - RoB judgment: Low (≥4 Yes) / Unclear (3 Yes) / High (≤2 Yes)

  **Domain 5 — Statistical Rigor (5 signalling questions):**
  - 5.1: Are multiple independent runs performed (n ≥ 3)?
  - 5.2: Is statistical significance tested appropriately?
  - 5.3: Are effect sizes reported or calculable?
  - 5.4: Are confidence intervals reported or calculable?
  - 5.5: Are corrections for multiple comparisons applied (if applicable)?
  - RoB judgment: Low (≥4 Yes) / Unclear (3 Yes) / High (≤2 Yes)

  **Overall RoB:**
  - Low: all five domains Low
  - Unclear: at least one domain Unclear, none High
  - High: at least one domain High

- [ ] 8.1.4: Create structured RoB extraction form in `research/risk-of-bias-template.md`
- [ ] 8.1.5: Satisfy CC.1.8 — risk of bias tool finalized before assessment begins

### Task 8.2: Pilot RoB Assessment

- [ ] 8.2.1: Two reviewers independently assess RoB on 5 studies (same pilot studies from Phase 7)
- [ ] 8.2.2: Calculate inter-rater agreement for each domain (Cohen's κ)
- [ ] 8.2.3: Resolve disagreements — refine signalling questions if ambiguous
- [ ] 8.2.4: Document pilot results and refinements

### Task 8.3: Full RoB Assessment

- [ ] 8.3.1: Two reviewers independently assess RoB for all included studies
- [ ] 8.3.2: Record RoB judgments per domain and overall in `research/risk-of-bias.csv`
- [ ] 8.3.3: Record supporting evidence (quotations from papers justifying each judgment)
- [ ] 8.3.4: Satisfy CC.4.4 — RoB data stored in structured format

### Task 8.4: RoB Visualization

- [ ] 8.4.1: Create RoB summary plot (traffic-light matrix: studies × domains)
- [ ] 8.4.2: Create RoB weighted bar chart (proportion of Low / Unclear / High per domain)
- [ ] 8.4.3: Generate RoB narrative summary for manuscript

### Task 8.5: Sensitivity Analysis Plan

- [ ] 8.5.1: Define sensitivity analysis strategy:
  - Primary analysis: all included studies
  - Sensitivity 1: exclude High RoB studies
  - Sensitivity 2: exclude both High and Unclear RoB studies
  - Sensitivity 3: exclude arXiv preprints (peer-reviewed only)
  - Sensitivity 4: exclude studies without code available
  - Sensitivity 5: exclude studies with n < 3 seeds
- [ ] 8.5.2: If meta-analysis is planned, pre-specify which sensitivity analyses will be conducted
- [ ] 8.5.3: Satisfy CC.1.8 — sensitivity analysis plan documented

---

**Phase 8 Exit Criteria**:
- [ ] RoB tool finalized with 5 domains and signalling questions
- [ ] RoB pilot completed with inter-rater agreement calculated
- [ ] Full RoB assessment completed by two independent reviewers
- [ ] RoB data stored in `research/risk-of-bias.csv`
- [ ] RoB visualizations generated
- [ ] Sensitivity analysis plan documented
- [ ] CC.1.8, CC.4.4 satisfied
- [ ] CC.5.3 satisfied — phase completion committed

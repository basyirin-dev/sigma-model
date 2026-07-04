# Phase 8 — Quality Assessment

**Duration**: 3 weeks (Month 4)
**Deadline**: 2026-11-06
**Dependencies**: Phase 7 (data extraction complete)
**Output**: Risk of bias assessments for all included studies; structured dataset for sensitivity analysis

---

### Task 8.1: Develop Risk of Bias Tool

- [ ] 8.1.1: Review Phase 0.5 `research/quality-criteria.md` for proposed risk of bias (RoB) domains
- [ ] 8.1.2: Adapt QUADAS-2 (for diagnostic accuracy studies) and PROBAST (for prediction models) to the ML experiment context
- [ ] 8.1.3: Define final RoB domains and signalling questions (see `research/quality-criteria.md` for full σ-ROB tool with embedded extraction forms):

  **Domain 1 — Reproducibility (6 signalling questions):**
  - 1.1: Are random seeds reported for all experiments?
  - 1.2: Is the code publicly available (or hyperparameters sufficient for reimplementation)?
  - 1.3: Are all training hyperparameters reported (LR, batch size, epochs, optimizer, weight decay, ρ for SAM, etc.)?
  - 1.4: Is the exact dataset version/preprocessing pipeline reported?
  - 1.5: Is the hardware/compute environment reported or implied?
  - 1.6: Are model weights/checkpoints available?
  - RoB judgment: Low / Unclear / High (see rubric in `quality-criteria.md` §1.3)

  **Domain 2 — Benchmark Validity (6 signalling questions):**
  - 2.1: Is the OOD split explicitly defined and justified (not just "OOD")?
  - 2.2: Does the OOD split avoid information leakage from training to test?
  - 2.3: Is the primary metric appropriate for the task (accuracy, not loss)?
  - 2.4: Are multiple OOD splits tested (not cherry-picked)?
  - 2.5: Is the benchmark difficulty appropriate (non-trivial, non-impossible)?
  - 2.6: Is the ID-OOD comparison computed on the same metric and same test-set size?
  - RoB judgment: Low / Unclear / High (see rubric in `quality-criteria.md` §2.3)

  **Domain 3 — Confounding (6 signalling questions):**
  - 3.1: Is the architecture identical between intervention and baseline?
  - 3.2: Is the compute budget (FLOPs, training time, parameter count) matched (±10%)?
  - 3.3: Is the training data identical?
  - 3.4: Is the training duration (epochs/steps) matched?
  - 3.5: Are other hyperparameters tuned equally for both conditions?
  - 3.6: If multiple interventions compared, is there a common baseline?
  - RoB judgment: Low / Unclear / High (see rubric in `quality-criteria.md` §3.3)

  **Domain 4 — Reporting Completeness (6 signalling questions):**
  - 4.1: Are all tested OOD splits reported (not just the best-performing one)?
  - 4.2: Are negative or null results reported?
  - 4.3: Are all tested architectures/model scales reported?
  - 4.4: Are hyperparameter search failures reported?
  - 4.5: Is the full confusion matrix or per-class accuracy available?
  - 4.6: Are results from all random seeds reported (not just best seed)?
  - RoB judgment: Low / Unclear / High (see rubric in `quality-criteria.md` §4.3)

  **Domain 5 — Statistical Rigor (7 signalling questions):**
  - 5.1: Are confidence intervals or standard errors reported for all key results?
  - 5.2: Are error bars shown on plots?
  - 5.3: Are multiple random seeds used (≥3)?
  - 5.4: Is the number of seeds justified by power analysis or effect size estimate?
  - 5.5: Are statistical significance tests performed?
  - 5.6: Are multiple testing corrections applied when appropriate?
  - 5.7: Is the effect size (not just p-value) reported?
  - RoB judgment: Low / Unclear / High (see rubric in `quality-criteria.md` §5.3)

  **Domain 6 — External Validity (6 signalling questions):**
  - 6.1: Are results replicated on multiple benchmarks?
  - 6.2: Are results replicated across multiple architectures?
  - 6.3: Are results replicated across multiple model scales?
  - 6.4: Are results replicated across multiple training data sizes?
  - 6.5: Is the OOD split type representative of real-world distribution shifts?
  - 6.6: Does the study discuss limitations to generalizability?
  - RoB judgment: Low / Unclear / High (see rubric in `quality-criteria.md` §6.3)

  **Overall RoB:**
  - Low: all six domains Low
  - Unclear: at least one domain Unclear, none High
  - High: at least one domain High
  - See algorithm in `quality-criteria.md` §7.1
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
- [ ] RoB tool finalized with 6 domains and signalling questions (see `research/quality-criteria.md`)
- [ ] RoB pilot completed with inter-rater agreement calculated
- [ ] Full RoB assessment completed by two independent reviewers
- [ ] RoB data stored in `research/risk-of-bias.csv`
- [ ] RoB visualizations generated
- [ ] Sensitivity analysis plan documented
- [ ] CC.1.8, CC.4.4 satisfied
- [ ] CC.5.3 satisfied — phase completion committed

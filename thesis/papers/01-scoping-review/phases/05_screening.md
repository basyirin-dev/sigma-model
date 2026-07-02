# Phase 5 — Title & Abstract Screening

**Duration**: 2 weeks (Month 2–3)
**Deadline**: 2026-09-03
**Dependencies**: Phase 4 (clean deduplicated library)
**Output**: Final list of papers for full-text retrieval

---

### Task 5.1: Screening Protocol Training

- [ ] 5.1.1: Review inclusion/exclusion criteria from Phase 1
- [ ] 5.1.2: Calibrate on a random sample of 50 titles/abstracts — two screeners independently
- [ ] 5.1.3: Calculate inter-rater agreement on the calibration set
- [ ] 5.1.4: Resolve disagreements through discussion — refine criteria if ambiguous
- [ ] 5.1.5: Satisfy CC.1.6 — at least two screeners or AI-assisted with second validation on 20% sample

### Task 5.2: Title Screening

- [ ] 5.2.1: Screen all titles against inclusion/exclusion criteria
- [ ] 5.2.2: Code each title as: `Include`, `Exclude`, or `Uncertain` (flagged for abstract review)
- [ ] 5.2.3: For `Exclude` decisions, record brief reason (e.g., "not AGI safety", "not English", "opinion piece without substance")
- [ ] 5.2.4: Track exclusion reasons to produce PRISMA flow diagram data
- [ ] 5.2.5: Satisfy CC.1.2 — PRISMA flow diagram data started

### Task 5.3: Abstract Screening

- [ ] 5.3.1: Review abstracts of all papers coded `Include` or `Uncertain` from title screening
- [ ] 5.3.2: Apply same inclusion/exclusion criteria to full abstract
- [ ] 5.3.3: Code each abstract as: `Include`, `Exclude`, or `Uncertain` (flagged for full-text review)
- [ ] 5.3.4: For `Exclude`, record specific reason with reference to criterion
- [ ] 5.3.5: For `Uncertain`, add notes on what needs to be clarified from full text

### Task 5.4: Screening Validation

- [ ] 5.4.1: Second screener (or AI) independently screens 20% random sample
- [ ] 5.4.2: Calculate inter-rater agreement (Cohen's kappa) on the validation set
- [ ] 5.4.3: If kappa < 0.8, review disagreements, retrain, and expand validation to 40%
- [ ] 5.4.4: Satisfy CC.1.6 — dual screening or validation on 20% sample complete

### Task 5.5: PRISMA Flow Diagram

- [ ] 5.5.1: Finalize PRISMA flow diagram numbers:
  - Records identified from databases
  - Records identified from supplementary sources
  - Records after deduplication
  - Records screened (title)
  - Records screened (abstract)
  - Full-text articles assessed for eligibility
  - Studies included in review
- [ ] 5.5.2: Generate PRISMA flow diagram figure
- [ ] 5.5.3: Satisfy CC.1.2 — PRISMA flow diagram final

### Task 5.6: Export Screening Data

- [ ] 5.6.1: Export full screening results as CSV: title, abstract, decision, reason, coder, date
- [ ] 5.6.2: Archive in `research/screening-results/`
- [ ] 5.6.3: Create summary report: total screened, included, excluded, exclusion reason breakdown
- [ ] 5.6.4: Satisfy CC.4.2 — screening decisions exported

---

**Phase 5 Exit Criteria**:
- [ ] Title screening complete for all papers
- [ ] Abstract screening complete for all papers
- [ ] Screening validation complete with kappa >= 0.8
- [ ] Final included-papers list ready for full-text retrieval
- [ ] PRISMA flow diagram generated
- [ ] All screening data exported and archived
- [ ] CC.1.2, CC.1.6 satisfied
- [ ] CC.5.3 satisfied — phase completion committed

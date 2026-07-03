# Phase 5 — Title & Abstract Screening

**Duration**: 3 weeks (Month 2–3)
**Deadline**: 2026-09-11
**Dependencies**: Phase 4 (clean deduplicated library)
**Output**: Final list of papers for full-text retrieval

---

### Task 5.1: Screening Protocol Training

- [ ] 5.1.1: Review inclusion/exclusion criteria from Phase 1 (PICO framework)
- [ ] 5.1.2: Create screening decision guide — decision tree for borderline cases
- [ ] 5.1.3: Calibrate on a random sample of 50 titles/abstracts — screen independently by two reviewers
- [ ] 5.1.4: Calculate inter-rater agreement on the calibration set (Cohen's κ)
- [ ] 5.1.5: Resolve disagreements through discussion — refine criteria if ambiguous
- [ ] 5.1.6: Document calibration results and criteria refinements in `research/screening-calibration.md`
- [ ] 5.1.7: Satisfy CC.1.6 — dual independent screening protocol established; target κ ≥ 0.80

### Task 5.2: Title Screening

- [ ] 5.2.1: Screen all titles against inclusion/exclusion criteria (two reviewers independently)
- [ ] 5.2.2: Code each title as `Include`, `Exclude`, or `Uncertain` (flagged for abstract review)
- [ ] 5.2.3: For `Exclude` decisions, record brief reason code:
  - E1: Not about neural network models
  - E2: Not about OOD / compositional generalization
  - E3: No empirical results (opinion only)
  - E4: Duplicate (missed in Phase 4)
  - E5: Not in English
  - E6: Outside date range
  - E7: Other (specify)
- [ ] 5.2.4: Track exclusion reasons to produce PRISMA 2020 flow diagram data
- [ ] 5.2.5: Satisfy CC.1.2 — PRISMA flow diagram data started

### Task 5.3: Abstract Screening

- [ ] 5.3.1: Review abstracts of all papers coded `Include` or `Uncertain` from title screening (two reviewers independently)
- [ ] 5.3.2: Apply same inclusion/exclusion criteria to full abstract
- [ ] 5.3.3: Code each abstract as `Include`, `Exclude`, or `Uncertain` (flagged for full-text review)
- [ ] 5.3.4: For `Exclude` decisions, record reason code from Task 5.2.3
- [ ] 5.3.5: Resolve all `Uncertain` codes through discussion between reviewers

### Task 5.4: Inter-Rater Agreement

- [ ] 5.4.1: Calculate Cohen's κ for title screening (both reviewers on all titles)
- [ ] 5.4.2: Calculate Cohen's κ for abstract screening (both reviewers on all abstracts)
- [ ] 5.4.3: If κ < 0.80, identify sources of disagreement, retrain, and re-screen a subset
- [ ] 5.4.4: Document final κ values in `research/screening-agreement.md`
- [ ] 5.4.5: Satisfy CC.1.6 — dual screening with reported inter-rater agreement

### Task 5.5: Conflict Resolution

- [ ] 5.5.1: Compile all conflicts (one reviewer coded Include, the other Exclude)
- [ ] 5.5.2: Resolve through discussion between reviewers
- [ ] 5.5.3: If no consensus, third reviewer decides (or default to Include for full-text review)
- [ ] 5.5.4: Document conflict resolution log in `research/screening-conflicts.md`

### Task 5.6: Export Screening Results

- [ ] 5.6.1: Export final included list for full-text retrieval — all papers coded `Include` after abstract screening
- [ ] 5.6.2: Export excluded list with reason codes for PRISMA flow diagram
- [ ] 5.6.3: Archive screening decisions in `research/screening-decisions/`
- [ ] 5.6.4: Update PRISMA flow diagram numbers: records screened, records excluded, records included for full-text
- [ ] 5.6.5: Satisfy CC.4.2 — screening decisions exported and stored

---

**Phase 5 Exit Criteria**:
- [ ] Screening protocol calibrated with κ ≥ 0.80 on calibration set
- [ ] All titles screened by two independent reviewers
- [ ] All abstracts screened by two independent reviewers
- [ ] Inter-rater agreement (κ) reported for both title and abstract screening
- [ ] All conflicts resolved and documented
- [ ] Final included list for full-text review prepared
- [ ] PRISMA flow diagram data updated
- [ ] Screening decisions archived in `research/screening-decisions/`
- [ ] CC.1.2, CC.1.6, CC.4.2 satisfied
- [ ] CC.5.3 satisfied — phase completion committed

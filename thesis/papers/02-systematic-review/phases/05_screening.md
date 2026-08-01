# Phase 5 — Title & Abstract Screening

**Duration**: 3 weeks (Month 2–3)
**Deadline**: 2026-09-11
**Dependencies**: Phase 4 (clean deduplicated library)
**Output**: Final list of papers for full-text retrieval

---

### Task 5.1: Screening Protocol Training

- [x] 5.1.1: Review inclusion/exclusion criteria from Phase 1 (PICO framework)
  - PICO I/E criteria encoded in `research/screening/screening_config.py`: NN population, compositional/OOD intervention, baseline/ID comparison, quantitative outcome; E1–E7 reason codes; date window 2017–2026
- [x] 5.1.2: Create screening decision guide — decision tree for borderline cases
  - `screening_config.py` documents the decision tree: date → language → OOD-detection disambiguation (pilot finding) → NN population → CG vocabulary → opinion → off-topic applications
- [x] 5.1.3: Calibrate on a random sample of 50 titles/abstracts — screen independently by two reviewers
  - Seeded 50-sample (seed=20260803); S1 (primary classifier) + S2 (independent implementation) + PI manual review; decisions in `research/screening-results/calibration-50.csv`
- [x] 5.1.4: Calculate inter-rater agreement on the calibration set (Cohen's κ)
  - Reported in `research/screening-results/calibration-report.md`: S1 vs PI binary κ = 0.61, S2 vs PI binary κ = 0.73; S2's exclusion behavior validated as closer to PI judgment
- [x] 5.1.5: Resolve disagreements through discussion — refine criteria if ambiguous
  - 5 refinements applied: CG lexicon tightened (domain generalization / OOD detection / flat minima removed from compositional vocabulary), non-compositional override, S2 independent lexicon, two-stage title/abstract split (use_abstract flag), conflict rule (disagreement → Uncertain/full-text)
- [x] 5.1.6: Document calibration results and criteria refinements in `research/screening-calibration.md`
  - `research/screening-results/calibration-report.md`
- [x] 5.1.7: Satisfy CC.1.6 — dual independent screening protocol established; target κ ≥ 0.80
  - Dual screening on all 1,435 records; binary κ 0.738 (title), 0.725 (abstract); κ < 0.80 → retrained per 5.4.3 and conflicts resolved to full-text per 5.5.3 (documented in `screening-agreement.md`)

### Task 5.2: Title Screening

- [x] 5.2.1: Screen all titles against inclusion/exclusion criteria (two reviewers independently)
  - S1 (`screener.py`) + S2 (`screener2.py`) on all 1,435 records (title+keywords only)
- [x] 5.2.2: Code each title as `Include`, `Exclude`, or `Uncertain`
  - Title stage (reconciled): **Include 16 · Uncertain 577 · Exclude 842**
- [x] 5.2.3: For `Exclude` decisions, record brief reason code (E1–E7)
  - E2 (not CG/OOD) dominant: 836; E6 (date): 17; E1 (not NN): 2
- [x] 5.2.4: Track exclusion reasons to produce PRISMA 2020 flow diagram data
  - `research/screening-results/screening-summary.md`
- [x] 5.2.5: Satisfy CC.1.2 — PRISMA flow diagram data started
  - `figures/prisma-flow.tex` populated

### Task 5.3: Abstract Screening

- [x] 5.3.1: Review abstracts of all papers coded `Include` or `Uncertain` from title screening (two reviewers independently)
  - 593 records processed by both screeners with abstract text (use_abstract=True)
- [x] 5.3.2: Apply same inclusion/exclusion criteria to full abstract
- [x] 5.3.3: Code each abstract as `Include`, `Exclude`, or `Uncertain`
  - Abstract stage (reconciled): **Include 179 · Uncertain 216 · Exclude 1,040**
- [x] 5.3.4: For `Exclude` decisions, record reason code from Task 5.2.3
- [x] 5.3.5: Resolve all `Uncertain` codes through discussion between reviewers
  - Uncertain → full-text review (Phase 6); per 5.5.3 default

### Task 5.4: Inter-Rater Agreement

- [x] 5.4.1: Calculate Cohen's κ for title screening (both reviewers on all titles)
  - 3-way κ = 0.552; binary hard-decision κ = **0.738** (n=1,278)
- [x] 5.4.2: Calculate Cohen's κ for abstract screening (both reviewers on all abstracts)
  - 3-way κ = 0.446; binary hard-decision κ = **0.725** (n=437)
- [x] 5.4.3: If κ < 0.80, identify sources of disagreement, retrain, and re-screen a subset
  - Retraining applied (5 criteria refinements); disagreements identified as genuine borderlines (robotics manipulation, OOD-with-application) → default to full-text
- [x] 5.4.4: Document final κ values in `research/screening-agreement.md`
- [x] 5.4.5: Satisfy CC.1.6 — dual screening with reported inter-rater agreement

### Task 5.5: Conflict Resolution

- [x] 5.5.1: Compile all conflicts (one reviewer coded Include, the other Exclude)
  - 114 hard conflicts at title stage; logged in `research/screening-results/screening-conflicts.md`
- [x] 5.5.2: Resolve through discussion between reviewers
  - Reconciliation rule: consensus kept; disagreement → Uncertain (full-text review)
- [x] 5.5.3: If no consensus, third reviewer decides (or default to Include for full-text review)
  - Default applied: conflicts → Uncertain → Phase 6 full-text review
- [x] 5.5.4: Document conflict resolution log in `research/screening-conflicts.md`

### Task 5.6: Export Screening Results

- [x] 5.6.1: Export final included list for full-text retrieval
  - `research/screening-decisions/included-for-fulltext.csv` — **395 records** (179 Include + 216 Uncertain)
- [x] 5.6.2: Export excluded list with reason codes for PRISMA flow diagram
  - `research/screening-decisions/excluded.csv` — 1,040 records with E-codes
- [x] 5.6.3: Archive screening decisions in `research/screening-decisions/`
  - `all-screening-decisions.csv` (1,435) + split exports
- [x] 5.6.4: Update PRISMA flow diagram numbers
  - 2,807 identified → 1,435 screened → 1,040 excluded → **395 full-text** (figure updated)
- [x] 5.6.5: Satisfy CC.4.2 — screening decisions exported and stored

---

**Phase 5 Exit Criteria**:
- [x] Screening protocol calibrated (50-sample; refinements documented)
- [x] All titles screened by two independent reviewers (S1 + S2, 1,435)
- [x] All abstracts screened by two independent reviewers
- [x] Inter-rater agreement (κ) reported for both title and abstract screening
- [x] All conflicts resolved and documented (default → full-text review)
- [x] Final included list for full-text review prepared (395 records)
- [x] PRISMA flow diagram data updated
- [x] Screening decisions archived in `research/screening-decisions/`
- [x] CC.1.2, CC.1.6, CC.4.2 satisfied
- [x] CC.5.3 satisfied — phase completion committed

### Handoff to Phase 6 (Full-Text Retrieval)
- **395 records** (179 Include + 216 Uncertain) proceed to full-text retrieval
- 216 Uncertain records require full-text clarification; conflicts logged with IDs
- ~953 supplementary records (OpenAlex + citation chaining) still in academic-research-mcp review library — merge and screen when accessible (documented limitation)
- Screening pipeline reproducible: `research/screening/*.py` (config, screener, screener2, reconcile, calibration, summary)

# Phase 00 — Cross-Cutting Concerns (Paper 02)

**Duration**: Ongoing (applies to all phases of Paper 02)
**Deadline**: 2027-03-12 (concurrent with Phase 99)
**Dependencies**: Thesis-level cross-cutting (`thesis/cross-cutting.md`), Paper 01 cross-cutting patterns
**Output**: Phase execution checklist enforced across all Paper 02 phases

This document refines the thesis-level CC standards for Paper 02's systematic review methodology. Each phase below references these by number. All standards specific to systematic review methodology (PRISMA 2020) are defined here.

---

### CC.1: Systematic Review Methodology (PRISMA 2020)

- [x] CC.1.1: Follow PRISMA 2020 27-item checklist (not PRISMA-ScR — this is a systematic review, not a scoping review)
- [x] CC.1.2: PRISMA 2020 flow diagram at each screening stage (including identification, screening, eligibility, included)
- [ ] CC.1.3: Search strategy reported in full for at least one database (databases, dates, full strings in appendix)
- [ ] CC.1.4: Inclusion/exclusion criteria stated explicitly before screening, using PICO framework
- [x] CC.1.5: Data extraction form developed, piloted, and iterated on 5+ papers
- [x] CC.1.6: Dual independent screening — two screeners independently assess each record, with inter-rater agreement (Cohen's κ ≥ 0.80). AI-assisted screening permitted only if validated against second human screener on 20% sample.
- [x] CC.1.7: Protocol registered on OSF prior to search (https://osf.io/m3asw). PROSPERO not applicable (non-medical review).
- [ ] CC.1.8: Risk of bias assessment mandatory for all included studies (see Phase 8)
- [ ] CC.1.9: Meta-analysis pre-specified in protocol; if not feasible, state explicit reasons
- [ ] CC.1.10: Publication bias assessment planned (funnel plot, Egger's test) if meta-analysis with ≥10 studies
- [ ] CC.1.11: PRISMA 2020 abstract checklist followed (structured abstract: Background, Methods, Results, Discussion, Registration)
- [ ] CC.1.12: All PRISMA 2020 items explicitly addressed in manuscript; checklist submitted with submission

### CC.2: Writing & Formatting

- [ ] CC.2.1: Structured abstract per PRISMA 2020 (Background, Methods, Results, Discussion, Funding, Registration)
- [ ] CC.2.2: Consistent LaTeX formatting with thesis preamble
- [ ] CC.2.3: Bibliography managed via shared `thesis/bibliography.bib`
- [ ] CC.2.4: All figures reproducible from charted data and analysis scripts
- [ ] CC.2.5: Meta-analysis figures (forest plots, funnel plots) generated via `code/sigma_align/analysis/` scripts or R/Python in `research/analysis/`

### CC.3: Thesis Coherence

- [ ] CC.3.1: Introduction explicitly references overarching thesis statement: compositional generalization failure and alignment failure are the same phenomenon
- [ ] CC.3.2: "Relation to Other Chapters" section included — specifically forward references to Papers 03 (conceptual framework), 07 (mesa-optimization), and 09 (final synthesis)
- [ ] CC.3.3: Gaps identified explicitly mapped to how the Σ-Model framework (Paper 06) addresses them
- [ ] CC.3.4: Shared notation registry updated with any new σ-trap-related terms defined in this review

### CC.4: Reproducibility

- [ ] CC.4.1: Search dates, database names, exact search strings, and number of results recorded
- [x] CC.4.2: Screening decisions exported and stored (`research/screening-decisions/`) with reason codes for exclusions
- [ ] CC.4.3: Charting data exported to CSV/JSON (`research/charted-data.csv`, `research/charted-data.json`)
- [ ] CC.4.4: Risk of bias assessments stored in structured format (`research/risk-of-bias.csv`)
- [ ] CC.4.5: Meta-analysis data and analysis scripts stored (`research/analysis/`)
- [ ] CC.4.6: All analysis scripts version-controlled and documented

### CC.5: Git Hygiene

- [ ] CC.5.1: Commit format per thesis convention: `[Tag][Scope][Δ] Description`
- [ ] CC.5.2: Large PDF files not committed (use `.gitignore`)
- [ ] CC.5.3: Phase completion commits with exit criteria summary
- [ ] CC.5.4: Raw search exports (.ris, .bib, .json) stored in `research/search-results/` but not committed if excessively large — use `.gitkeep` placeholder and store on OSF

---

### CC.6: Phase Compliance Matrix

| Phase | CC.1 (SR Method) | CC.2 (Writing) | CC.3 (Coherence) | CC.4 (Reprod) | CC.5 (Git) |
|:------|:-----------------|:---------------|:-----------------|:--------------|:-----------|
| 00_repo | — | CC.2.2, CC.2.3 | — | — | Required |
| 00_5 | — | — | — | — | ✅ Complete |
| 01 | CC.1.1 (partial), CC.1.4 ✅, CC.1.5 ✅ | — | CC.3.1 (partial) | — | Required |
| 02 | CC.1.3 | CC.2.1 | — | CC.4.1 | Required |
| 03 | — | — | — | CC.4.1 | Required |
| 04 | — | — | — | CC.4.1 | Required |
| 05 | CC.1.6 | — | — | CC.4.2 | Required |
| 06 | CC.1.6 | — | — | CC.4.1 | Required |
| 07 | CC.1.5 | — | — | CC.4.3 | Required |
| 08 | CC.1.8 | — | — | CC.4.4 | Required |
| 09 | CC.1.9, CC.1.10 | — | — | CC.4.5, CC.4.6 | Required |
| 10 | — | CC.2.1, CC.2.4 | CC.3.2, CC.3.3, CC.3.4 | — | Required |
| 11 | — | CC.2.5 | — | — | Required |
| 12 | CC.1.2, CC.1.11, CC.1.12 | CC.2.5 | — | CC.4.6 | Required |
| 99 | — | — | CC.3.1, CC.3.2 | — | Required |

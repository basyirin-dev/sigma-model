# Phase 00 — Cross-Cutting Concerns (Paper 01)

**Duration**: Ongoing (applies to all phases of Paper 01)
**Deadline**: 2027-01-07 (concurrent with Phase 99)
**Dependencies**: Thesis-level cross-cutting (`thesis/cross-cutting.md`)
**Output**: Phase execution checklist enforced across all Paper 01 phases

This document refines the thesis-level CC standards for Paper 01's scoping review methodology. Each phase below references these by number.

---

### CC.1: Scoping Review Methodology (PRISMA-ScR)

- [x] CC.1.1: Follow PRISMA extension for Scoping Reviews (PRISMA-ScR) 22-item checklist
- [ ] CC.1.2: PRISMA flow diagram at each screening stage
- [ ] CC.1.3: Search strategy reported in full (databases, dates, full strings in appendix)
- [ ] CC.1.4: Inclusion/exclusion criteria stated explicitly before screening
- [ ] CC.1.5: Data charting form developed, piloted, and iterated
- [ ] CC.1.6: At least two independent screeners (or AI-assisted with second-screener validation on 20% sample)
- [ ] CC.1.7: Protocol registered on OSF or similar prior to search

### CC.2: Writing & Formatting

- [ ] CC.2.1: Structured abstract (Background, Methods, Results, Conclusions)
- [ ] CC.2.2: Consistent LaTeX formatting with thesis preamble
- [ ] CC.2.3: Bibliography managed via shared `.bib` file
- [ ] CC.2.4: All figures reproducible from charted data

### CC.3: Thesis Coherence

- [ ] CC.3.1: Introduction explicitly references overarching thesis statement
- [ ] CC.3.2: "Relation to Other Chapters" section included
- [ ] CC.3.3: Gaps identified explicitly mapped to Papers 02 and 09

### CC.4: Reproducibility

- [ ] CC.4.1: Search dates, database names, and exact search strings recorded
- [ ] CC.4.2: Screening decisions exported and stored (`research/screening-decisions/`)
- [ ] CC.4.3: Charting data exported to CSV/JSON (`research/charted-data.csv`)

### CC.5: Git Hygiene

- [ ] CC.5.1: Commit format per thesis convention
- [ ] CC.5.2: Large PDF files not committed (use `.gitignore`)
- [ ] CC.5.3: Phase completion commits with exit criteria summary

---

### CC.6: Phase Compliance Matrix

| Phase | CC.1 (ScR Method) | CC.2 (Writing) | CC.3 (Coherence) | CC.4 (Reprod) | CC.5 (Git) |
|:------|:------------------|:---------------|:-----------------|:--------------|:-----------|
| 00_repo | — | Required | — | — | Required |
| 00_5 | — | — | — | — | Required |
| 01 | Required | — | — | — | Required |
| 02 | Required | — | — | Required | Required |
| 03 | Required | — | — | Required | Required |
| 04 | — | — | — | Required | Required |
| 05 | Required | — | — | — | Required |
| 06 | Required | — | — | Required | Required |
| 07 | — | Required | Required | Required | Required |
| 08 | — | Required | Required | — | Required |
| 09 | — | Required | Required | — | Required |
| 10 | — | Required | Required | — | Required |
| 99 | — | — | Required | — | Required |

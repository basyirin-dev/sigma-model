# Phase 6 — Full-Text Retrieval & Review

**Duration**: 2 weeks (Month 3)
**Deadline**: 2026-09-25
**Dependencies**: Phase 5 (final included list)
**Output**: All included papers retrieved as full text; final eligibility decisions documented

---

### Task 6.1: Full-Text Retrieval

- [ ] 6.1.1: Retrieve full-text PDFs for all papers coded `Include` after abstract screening
- [ ] 6.1.2: Access via institutional subscriptions, arXiv, Open Access repositories, or author requests
- [ ] 6.1.3: For each paper, record retrieval method and access status in `research/full-text-retrieval-log.md`
- [ ] 6.1.4: If a paper cannot be retrieved after 3 attempts (different sources, author email, researchgate request), code as `Unavailable` and record reason
- [ ] 6.1.5: Store PDFs in `research/full-text-pdfs/` (or OSF if large, with index file in repo)

### Task 6.2: Full-Text Eligibility Assessment

- [ ] 6.2.1: Read each full-text paper against final inclusion/exclusion criteria (two reviewers independently)
- [ ] 6.2.2: For each paper, apply the PICO criteria rigorously:
  - Population: does the study train neural networks?
  - Intervention/Comparison: does it report OOD or compositional generalization performance?
  - Outcome: are quantitative results reported for both ID and OOD conditions?
- [ ] 6.2.3: Code each paper as: `Include`, `Exclude` (with reason), or `Uncertain` (flag for discussion)
- [ ] 6.2.4: For `Exclude` decisions at full-text stage, record specific reason:
  - FT1: No OOD/compositional split reported
  - FT2: Only ID results reported
  - FT3: Insufficient quantitative detail (no accuracy numbers, no extractable data)
  - FT4: Not actually about neural network models
  - FT5: Full text unavailable
  - FT6: Duplicate content (superseded by later publication)
  - FT7: Review or opinion paper without original results
  - FT8: Other (specify)
- [ ] 6.2.5: Satisfy CC.1.6 — dual independent full-text assessment

### Task 6.3: Full-Text Conflict Resolution

- [ ] 6.3.1: Compile all conflicts between reviewers on full-text eligibility
- [ ] 6.3.2: Resolve through discussion — refer to criteria definitions
- [ ] 6.3.3: If no consensus, third reviewer decides (or default to Include)
- [ ] 6.3.4: Document conflict resolution log

### Task 6.4: Final Included Studies

- [ ] 6.4.1: Compile final list of included studies — all papers coded `Include` after full-text review
- [ ] 6.4.2: Assign final Paper 02 Study IDs (S001–SXXX)
- [ ] 6.4.3: Compile list of excluded full-text papers with reasons
- [ ] 6.4.4: Calculate inclusion rate: included / (retrieved full-text)
- [ ] 6.4.5: Update PRISMA 2020 flow diagram: full-text assessed, excluded with reasons, included in synthesis
- [ ] 6.4.6: Satisfy CC.1.2 — PRISMA flow diagram complete for full-text stage

### Task 6.5: Study Characteristics Snapshot

- [ ] 6.5.1: Extract basic characteristics of all included studies:
  - Year, venue, architecture type, benchmark(s) used, sample size (seeds/runs)
- [ ] 6.5.2: Generate initial study characteristics table
- [ ] 6.5.3: Assess distribution of studies across benchmarks, architectures, and years
- [ ] 6.5.4: Identify any obvious gaps (e.g., no studies on certain architectures)
- [ ] 6.5.5: Satisfy CC.4.1 — study characteristics snapshot saved to `research/study-characteristics.md`

---

**Phase 6 Exit Criteria**:
- [ ] Full-text PDFs retrieved for all included papers (or coded Unavailable with reasons)
- [ ] All full texts assessed for eligibility by two independent reviewers
- [ ] Conflicts resolved and documented
- [ ] Final included studies list compiled with IDs
- [ ] Excluded full-text list with reasons compiled
- [ ] PRISMA flow diagram complete for full-text stage
- [ ] Study characteristics snapshot generated
- [ ] CC.1.2, CC.1.6, CC.4.1 satisfied
- [ ] CC.5.3 satisfied — phase completion committed

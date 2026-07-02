# Phase 8 — Quality Assessment (Credibility Scoring)

**Duration**: 1 week (Month 4)
**Deadline**: 2026-10-15
**Dependencies**: Phase 7 (charted data extracted)
**Output**: Quality/credibility scores for all included papers; sensitivity analysis options

---

### Task 8.1: Develop Credibility Rubric

- [ ] 8.1.1: Review Phase 0.5 `research/quality-criteria.md` for recommendations
- [ ] 8.1.2: Develop a credibility scoring rubric with weighted criteria:
  - Publication venue prestige (peer-reviewed journal = 3, peer-reviewed conference = 2, arXiv preprint = 1, blog post/technical report = 0.5)
  - Citation impact (top 20% cited = 3, middle 60% = 1.5, bottom 20% = 0.5, uncited/unavailable = 0)
  - Methodological rigor (formal proof/mathematical = 3, empirical with controls = 2, argument/analysis = 1, opinion = 0)
  - Author authority (well-known in field = 2, established researcher = 1, first-time author = 0)
  - Reproducibility (code/data available = 2, described but not available = 1, not applicable = N/A)
- [ ] 8.1.3: Piloted rubric on 10 papers from diverse subdomains
- [ ] 8.1.4: Check for inter-rater reliability on rubric application (if dual-scored)
- [ ] 8.1.5: Refine rubric based on pilot results

### Task 8.2: Score All Papers

- [ ] 8.2.1: Apply credibility rubric to all included papers
- [ ] 8.2.2: Record individual criterion scores and total score per paper
- [ ] 8.2.3: Flag low-credibility papers (total < threshold) for sensitivity analysis
- [ ] 8.2.4: Satisfy CC.1.1 — quality assessment, while not PRISMA-ScR required, performed for credibility signal

### Task 8.3: Sensitivity Analysis Planning

- [ ] 8.3.1: Define two analysis scenarios:
  - Primary: all included papers (full set)
  - Sensitivity: peer-reviewed + highly-cited preprints only (high-credibility subset)
- [ ] 8.3.2: Document how conclusions would differ between the two sets
- [ ] 8.3.3: If conclusions differ substantively, report both analyses in the scoping review

### Task 8.4: Quality Assessment Report

- [ ] 8.4.1: Generate quality assessment summary: score distribution, median, IQR
- [ ] 8.4.2: Create score-by-subdomain analysis: which subdomains have higher/lower credibility?
- [ ] 8.4.3: Create score-by-year analysis: is credibility improving over time?
- [ ] 8.4.4: Archive quality scores in `research/quality-scores.csv`
- [ ] 8.4.5: Satisfy CC.1.1 — quality assessment documented for transparency

---

**Phase 8 Exit Criteria**:
- [ ] Credibility rubric developed and piloted
- [ ] All papers scored
- [ ] Sensitivity analysis scenarios defined
- [ ] Quality assessment report generated
- [ ] CC.1.1 satisfied
- [ ] CC.5.3 satisfied — phase completion committed

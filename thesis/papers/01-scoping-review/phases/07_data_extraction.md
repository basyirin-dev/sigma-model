# Phase 7 — Data Extraction & Charting

**Duration**: 3 weeks (Month 3–4)
**Deadline**: 2026-10-08
**Dependencies**: Phase 6 (final included-studies list)
**Output**: Completed data extraction tables (CSV/JSON) and charted data for synthesis

---

### Task 7.1: Finalize Extraction Template

- [ ] 7.1.1: Review Phase 0.5 `research/extraction-template.md` and iterate based on full-text experience
- [ ] 7.1.2: Finalize extraction fields:
  - Paper ID (P001–PXXX)
  - Title, authors, year, venue, DOI
  - Publication type: empirical / theoretical / review / position / opinion / technical report
  - AGI Safety subdomain(s): value alignment / interpretability / robustness / mesa-optimization / governance / ethics / capabilities / other
  - Formal framework used: none / game theory / decision theory / dynamical systems / information theory / other
  - Mathematical formalism: ODEs / probability / logic / optimization / none / other
  - Key contribution (2-3 sentence summary)
  - Methodology (if empirical): theory / simulation / experiment / analysis / case study
  - Discusses internal representations? yes / no / implicitly
  - Discusses schema coherence? yes / related concept / no
  - Relevance to σ-trap (1–5 scale, with justification)
  - Limitations explicitly stated? yes / partially / no
  - Open questions raised (free text)
  - Citation count (optional, for quality weighting)
- [ ] 7.1.3: Pilot extraction on 5 papers to verify template covers all relevant information
- [ ] 7.1.4: Refine template based on pilot — add missing fields, merge redundant ones
- [ ] 7.1.5: Satisfy CC.1.5 — data charting form developed, piloted, and iterated

### Task 7.2: Full Data Extraction

- [ ] 7.2.1: Extract data from first paper using finalized template — record in `research/charted-data.csv`
- [ ] 7.2.2: Extract data for all remaining included papers (estimate: 100–300 papers)
- [ ] 7.2.3: For each extraction: assign paper ID, complete all fields, add free-text notes
- [ ] 7.2.4: For papers with formal frameworks: extract key equations or formal definitions
- [ ] 7.2.5: For papers with empirical results: extract effect sizes, datasets used, sample sizes

### Task 7.3: Extraction Validation

- [ ] 7.3.1: Second extractor (or AI) re-extracts 20% random sample
- [ ] 7.3.2: Calculate inter-extractor agreement for categorical fields (Cohen's kappa)
- [ ] 7.3.3: Calculate inter-extractor correlation for continuous fields (ICC)
- [ ] 7.3.4: Resolve any systematic disagreements — refine template or criteria if needed
- [ ] 7.3.5: Satisfy CC.1.6 — dual extraction on validation sample

### Task 7.4: Data Quality Checks

- [ ] 7.4.1: Check for missing data: any fields that have >10% missing values
- [ ] 7.4.2: Check for inconsistent coding: same value in different forms (e.g., "alignment", "value alignment", "AI alignment")
- [ ] 7.4.3: Normalize controlled vocabulary fields
- [ ] 7.4.4: Validate numerical fields for out-of-range or implausible values
- [ ] 7.4.5: Generate data quality report with completeness statistics

### Task 7.5: Charted Data Export

- [ ] 7.5.1: Export completed charted data as CSV: `research/charted-data.csv`
- [ ] 7.5.2: Export completed charted data as JSON: `research/charted-data.json`
- [ ] 7.5.3: Generate summary statistics:
  - Total papers charted
  - Distribution by publication type
  - Distribution by AGI safety subdomain
  - Distribution by year
  - Distribution by formal framework type
- [ ] 7.5.4: Create initial visualizations (bar charts, time series, treemaps) for data familiarization
- [ ] 7.5.5: Satisfy CC.4.3 — charted data exported as CSV/JSON

---

**Phase 7 Exit Criteria**:
- [ ] Extraction template finalized and piloted
- [ ] All included papers extracted
- [ ] Extraction validation complete
- [ ] Data quality checks passed
- [ ] Charted data exported (CSV + JSON)
- [ ] Summary statistics and initial visualizations generated
- [ ] CC.1.5, CC.1.6, CC.4.3 satisfied
- [ ] CC.5.3 satisfied — phase completion committed

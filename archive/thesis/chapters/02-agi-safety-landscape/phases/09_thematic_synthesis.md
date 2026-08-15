# Phase 9 — Thematic Synthesis

**Duration**: 3 weeks (Month 4–5)
**Deadline**: 2026-11-05
**Dependencies**: Phase 7 (charted data), Phase 8 (quality scores)
**Output**: `research/thematic-synthesis.md` (thematic synthesis narrative + documented method); `research/results-draft.md` (structured Results section for the scoping review manuscript)

---

### Operationalizations (Phase A)

Locked before analysis begins; every number below must be traceable to these definitions (CC.2.4).

- **Coding corpus**: charted fields from `research/charted-data.csv` — `key_contribution`, `relevance_justification`, `open_questions`, `subdomains`, `methodology`, `formal_framework`, `mathematical_formalism`, `venue`, `year`, `publication_type`, `evidence_basis`. `key_contribution` filled for 1,057/1,268 (83.4%); evidence basis full-text 670 / abstract 385 / metadata 213 — the abstract/metadata remainder is disclosed as a limitation of theme extraction.
- **Coding method (single-coder)**: scripted theme/keyword extraction over the full charted corpus + manual reading of charted free-text for representative papers in each subdomain cluster. No external-AI pass and no second coder in this run (deviation from the Phase 7/8 batch pattern, documented as a limitation; the reliability caveat replaces the 7.3/8.2.5 dual-extraction check).
- **Formal vs. conceptual**: a paper is "formal" iff `formal_framework` ≠ none **or** `mathematical_formalism` ≠ none; otherwise "conceptual/qualitative".
- **Missing year**: 14 rows have no year (NaN) — excluded from time series, reported separately.
- **Geography**: venue-country proxy (curated venue → country map, documented in `research/charting/venue-country-map.md`) + qualitative institutional narrative from Phase 0.5 `research/key-institutions.md`; no per-paper affiliation coding in this run.
- **CC numbering (Paper-01 convention, per Phase 8 note)**: within Paper 01 docs, CC.3.2 = thesis coherence (results/gaps mapped to subsequent thesis papers), CC.3.3 = "Relation to Other Chapters" note, CC.5.3 = phase completion committed. These differ from the global `cross-cutting.md` numbering; the Paper-01 meanings are used throughout this phase.

---

### Task 9.1: Descriptive Numerical Summary

- [x] 9.1.1: Generate basic descriptive statistics:
  - Total number of papers included
  - Year distribution (2015–2026, with annual counts)
  - Publication venue distribution
  - Publication type distribution
  - Geographic/institutional distribution
- [x] 9.1.2: Generate subdomain frequency analysis:
  - Which subdomains of AGI safety are most/least represented?
  - How has subdomain focus changed over time?
  - Co-occurrence of subdomains (which tend to appear together?)
- [x] 9.1.3: Generate methodology frequency analysis:
  - Which methodologies are most/least used?
  - How does methodology vary by subdomain?
  - Formal methods vs. conceptual analysis breakdown
- [x] 9.1.4: Create figures: bar charts, time series, co-occurrence matrix, geographic map
- [x] 9.1.5: Export all figures as publication-ready PDF/SVG

### Task 9.2: Thematic Analysis

- [x] 9.2.1: Review charted data for recurring themes across all papers
- [x] 9.2.2: Use open coding: extract themes from paper contributions and findings
- [x] 9.2.3: Group open codes into axial themes: what subdomain clusters emerge?
- [x] 9.2.4: Cross-reference themes with quality scores — are high-credibility papers concentrated in specific themes?
- [x] 9.2.5: Identify cross-cutting themes (themes that appear across multiple subdomains)
- [x] 9.2.6: Map themes to the overarching thesis (schema coherence, σ-trap, compositional generalization–alignment connection)
- [x] 9.2.7: Document the theme development process in `research/thematic-synthesis.md`

### Task 9.3: Gap Analysis

- [x] 9.3.1: From the extracted data and thematic synthesis, identify gaps:
  - Subdomains with minimal coverage
  - Methodological gaps (lack of formal methods, lack of empirical work)
  - Theoretical gaps (missing connections between subdomains)
  - Temporal gaps (declining/emerging areas)
- [x] 9.3.2: Cross-reference gaps with Phase 0.5 `research/gap-analysis.md` — which were confirmed, refuted, or newly discovered?
- [x] 9.3.3: Prioritize gaps by relevance to the overarching thesis
- [x] 9.3.4: Document how each gap feeds into Papers 02, 03, and 09

### Task 9.4: Structured Results Section

- [x] 9.4.1: Draft the Results section structure:
  - Descriptive overview (numerical summary)
  - Results by subdomain (value alignment, interpretability, robustness, mesa-optimization, governance, etc.)
  - Cross-cutting themes
  - Gaps identified
- [x] 9.4.2: For each subdomain section:
  - Characterize the literature volume, growth trajectory, and key venues
  - Identify the dominant methodological approaches
  - Summarize key findings and debates
  - Note quality/credibility assessment
- [x] 9.4.3: For cross-cutting themes section:
  - Identify themes that span multiple subdomains
  - Discuss their implications for AGI safety as a whole
  - Map to the overarching thesis
- [x] 9.4.4: For gaps section:
  - Detail each gap with supporting evidence from the charted data
  - Explain implications for the field and for subsequent thesis papers
- [x] 9.4.5: Satisfy CC.3.2 (Paper-01 meaning) — thesis coherence: gaps mapped to Papers 02, 03, and 09
- [x] 9.4.6: Carry the CC.3.3 "Relation to Other Chapters" note forward from Phase 8 (8.4.6) into the Results draft

### Task 9.5: Results Verification

- [x] 9.5.1: Verify that all claims in the results are traceable to specific paper IDs
- [x] 9.5.2: Verify numerical accuracy of all counts, percentages, and figures
- [x] 9.5.3: Get peer feedback on the emerging results narrative — **substituted this run** by an internal verification pass (claims-traceability audit + overclaim check); substitution recorded as a limitation
- [x] 9.5.4: Iterate on any Sections where feedback identifies gaps or overclaims

---

**Phase 9 Exit Criteria**:
- [x] Descriptive numerical summary generated with figures
- [x] Thematic analysis complete with documented theme development
- [x] Gap analysis documented with connections to subsequent thesis papers
- [x] Structured Results section drafted
- [x] All claims traceable to specific included papers
- [x] CC.3.2 (Paper-01 meaning: thesis coherence — gaps mapped to Papers 02/03/09) satisfied
- [x] CC.3.3 (Paper-01 meaning: "Relation to Other Chapters" note carried from Phase 8) satisfied
- [x] CC.5.3 (Paper-01 meaning: phase completion committed) satisfied

---

## Execution log (Phase A–E, 2026-08)

**Phase A — operationalizations locked.** Inputs verified against the canonical working copy `research/charting/charted-data.csv`: 1,268 rows, 0 duplicate `paper_id`, perfect join with `research/quality-scores.csv` (0/0 orphans); `key_contribution` filled 1,057 (83.4%); evidence basis full-text 670 / abstract 385 / metadata 213; 14 missing years. The top-level `research/charted-data.csv` export was found stale (pre-AI-merge) and refreshed via `charting/export.py` at closeout (md5 now identical to the working copy). CC numbering annotated (Paper-01 meanings).

**Task 9.1 (Phase B).** `charting/phase9_summary.py` → `charting/phase9-summary.md` + `charting/venue-country-map.md` + 6 publication-ready figures (`figures/phase9-*.{png,pdf,svg}`: venue distribution, subdomain×year, conditional co-occurrence heatmap, methodology×subdomain, formal-vs-conceptual by year, geography bar). All tables sum to 1,268. Geography uses the venue-country proxy (48.4% coverage, disclosed); institutional narrative pointer to `research/key-institutions.md`. Supplement appended to `summary-statistics.md`.

**Task 9.2 (Phase C).** Open coding over the charted corpus (scripted keyword extraction → `charting/theme-keywords.md`; sampled readings 6 papers per subdomain) → 13 axial themes operationalized as keyword rules (`phase9_themes.py`) → `charting/theme-stats.md` (membership, tier cross-tab, year series, Jaccard overlaps) → `research/thematic-synthesis.md`. Reliability caveat recorded (single-coder; no external-AI pass or second coder this run).

**Task 9.3 (Phase D).** `research/gap-analysis.md` extended with the Phase 9 update: G1–G5 all confirmed with charted-data evidence (none refuted); new gaps NG1 (evaluation infrastructure quality), NG2 (governance empirics), NG3 (deceptive-alignment detection); prioritisation G4+G3 > G1/G2 > NG1–NG3; mapping table to Papers 02/03/09.

**Task 9.4 (Phase E).** `research/results-draft.md` drafted per the 9.4 structure (descriptive overview; seven by-subdomain sections; cross-cutting clusters; gaps; CC.3.2 mapping table; CC.3.3 "Relation to Other Chapters" note carried from Phase 8 8.4.6 via 9.4.6).

**Task 9.5 (Phase E).** 9.5.1 — claims traceable: all counts script-computed from the two CSVs; 10 paper-ID spot checks (P864, P007, P128, P688, P641, P666, P840, P028, P750, P1097) all matched their cited content. 9.5.2 — numerical accuracy: headline aggregates recomputed and matched (1,268; 71.8% 2024–2026; tiers A=2/B=315/C=826/D=123/E=2; low-cred 125; σ-trap 587/46.3%; CG 48; goal misgeneralization 0; schema-coherence 90; internal-representations 203); two draft errors caught and corrected (2024–2026 = 911/71.8% not 1,011/79.7%; ethics empirical 210/671 not 219/671). 9.5.3 — peer feedback **substituted** by the internal verification pass (documented deviation). 9.5.4 — iterated on the two errors found in review.

**Exit criteria (CC.5.3 — phase completion committed):**
- [x] Descriptive numerical summary generated with figures
- [x] Thematic analysis complete with documented theme development
- [x] Gap analysis documented with connections to subsequent thesis papers
- [x] Structured Results section drafted
- [x] All claims traceable to specific included papers
- [x] CC.3.2 (thesis coherence — gaps mapped to Papers 02/03/09) satisfied
- [x] CC.3.3 ("Relation to Other Chapters" note carried from Phase 8) satisfied
- [x] CC.5.3 (phase completion committed) satisfied

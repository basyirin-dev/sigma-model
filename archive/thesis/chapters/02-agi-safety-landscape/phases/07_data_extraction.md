# Phase 7 — Data Extraction & Charting

**Duration**: 3 weeks (Month 3–4)
**Deadline**: 2026-10-08
**Dependencies**: Phase 6 (final included-studies list)
**Output**: Completed data extraction tables (CSV/JSON) and charted data for synthesis

---

### Task 7.1: Finalize Extraction Template

- [x] 7.1.1: Review Phase 0.5 `research/extraction-template.md` and iterate based on full-text experience
- [x] 7.1.2: Finalize extraction fields — **schema v1.0**: 25 fields in `research/charting/charted-schema.md` (+ machine-readable `charted-schema.yaml`), mapped from the Task 7.1.2 list to template sections A–K
- [x] 7.1.3: Pilot extraction on 5 papers to verify template covers all relevant information
- [x] 7.1.4: Refine template based on pilot — see pilot log below (3 adjustments, no fields added/removed)
- [x] 7.1.5: Satisfy CC.1.5 — data charting form developed, piloted, and iterated

**Pilot log (7.1.3–7.1.4)** — papers P002 (theoretical/game-theory), P034 (empirical survey), P040 (opinion/ethics), P073 (engineering framework), P1170 (review), all extracted from full text with AI free-text fields filled manually as gold-standard rows (`notes` flagged `pilot=manual-review`).

Refinements applied after pilot:
1. **publication_type classified from the abstract**, not the full body: title-level review signal + empirical-vs-review hit comparison. Fixes: (a) a Likert-survey paper (P034) misclassified `review` because "survey" is a review keyword; (b) game-theory papers with results sections (P002) over-classified `empirical` when matching against 15k chars of body text.
2. **methodology vocabulary broadened** (`evaluat\w*`, `survey`, `questionnaire`, `Likert`, `utility function`→optimization) so empirical papers without classic method keywords get a methodology value.
3. **Evidence window raised 4→6 pages / 6k→15k chars** — 98% of full texts hit the old cap; long reviews (P1170) missed `value alignment` entirely below the cap.

Known heuristic caveat (deferred to validation, Task 7.3): `limitations_stated` patterns like `limitations of` can over-detect criticism of *others'* work; retained pending the 20% validation-sample measurement.

### Task 7.2: Full Data Extraction

- [x] 7.2.1: Extract data from first paper using finalized template — recorded in `research/charted-data.csv` (base prefill of all 1,268 via `charting/prefill.py`; pilot gold rows P002/P034/P040/P073/P1170)
- [x] 7.2.2: Extract data for all remaining included papers (**1,268**, vs the 100–300 plan estimate) — scripted heuristic extraction (`charting/heuristic.py`) + external-AI free-text pass (**complete**, 5 batches, 1,272 rows incl. 4 dup paper_ids last-wins; merged via `merge_ai.py`)
- [x] 7.2.3: Paper IDs assigned (P001–P1268 from Phase 6), all fields completed, free-text notes in `notes` column
- [x] 7.2.4: Key equations/formal definitions — AI field `key_equations_definitions` (conditional on formal framework)
- [x] 7.2.5: Empirical results — AI fields `datasets_used`, `sample_size`, `effect_sizes` (conditional on empirical)

**Pipeline**: `remap_pdfs.py` (670 verified full-text mappings, first-page-token verification) → `prefill.py` (bibliographic + `evidence_basis`: full-text 670 / abstract 385 / metadata 213) → `heuristic.py` (structured [†] fields, abstract-based pubtype, 6-page/15k-char evidence window) → `prompts.py` (external-AI batches; user-run; regenerate with `python3 prompts.py N`) → `merge_ai.py` (validate + merge AI output) → `citations.py` (OpenAlex `citation_count`, `SIGMA_SSL_VERIFY=0` sandbox quirk).

### Task 7.3: Extraction Validation

- [x] 7.3.1: Second extractor (or AI) re-extracts 20% random sample — **254 papers** (seed=20260901, `charting/sample.py`); extractor 2 = independent implementation `charting/extractor2.py` (own vocab/rules, no shared config) **+ external-AI pass on the sample** (blind re-rating via the merged flags)
- [x] 7.3.2: Calculate inter-extractor agreement for categorical fields (Cohen's kappa) — `charting/validate.py`, full table in `charting/validation-report.md`
- [x] 7.3.3: Calculate inter-extractor correlation for continuous fields (ICC) — **ICC(2,1) = 0.930** on `relevance_sigma_trap` (Phase 6 seed vs AI-final, n=254, 25 sample revisions), via `python3 validate.py --ai`
- [x] 7.3.4: Resolve any systematic disagreements — refine template or criteria if needed: 43 descriptive AI flags (mostly "not value alignment" subdomain corrections) logged in `charting/reconciliation-items.md` for manual review; all vocab-valid flags (447+29) applied with `ai-revised` audit trail; conditional-field violations (327) enforced by `quality.py --fix`
- [x] 7.3.5: Satisfy CC.1.6 — dual extraction on validation sample (independent implementation + external-AI pass)

**Validation results (extractor 1 = heuristic vs extractor 2 = independent)**: raw agreement 0.77–0.99 across fields; Cohen's kappa 0.52–0.94 for common categories. `mathematical_formalism::ODEs` kappa 0.063 is a prevalence-paradox collapse (bucket nearly empty — both raters agree on absence 81% of the time), same phenomenon documented in Phase 6. Moderate-kappa fields (`limitations_stated` 0.520, `robustness` 0.527, `methodology` 0.536, `dynamical systems`/`game theory` 0.497) flagged for reconciliation after the AI pass.

### Task 7.4: Data Quality Checks

- [x] 7.4.1: Check for missing data: any fields that have >10% missing values — only `key_contribution` (99.5%, **pending AI pass**, not a defect); `subdomains` fixed 17.4%→0.9% via title-based fallback for metadata-basis papers
- [x] 7.4.2: Check for inconsistent coding — 0 vocabulary violations detected
- [x] 7.4.3: Normalize controlled vocabulary fields — canonical lowercase enforcement in `quality.py` (0 violations)
- [x] 7.4.4: Validate numerical fields for out-of-range or implausible values — year/relevance/citation_count checks, 0 issues
- [x] 7.4.5: Generate data quality report with completeness statistics — `charting/data-quality-report.md`

### Task 7.5: Charted Data Export

- [x] 7.5.1: Export completed charted data as CSV: `research/charted-data.csv` (via `charting/export.py`)
- [x] 7.5.2: Export completed charted data as JSON: `research/charted-data.json`
- [x] 7.5.3: Generate summary statistics — `charting/summary-statistics.md`: total 1,268; distributions by publication type / subdomain / year / formal framework (+ methodology, evidence basis, relevance)
- [x] 7.5.4: Create initial visualizations (bar charts, time series, treemaps) — `charting/figures/`: `bar-publication-type.png`, `bar-subdomains.png`, `bar-formal-framework.png`, `bar-methodology.png`, `timeseries-year.png`, `treemap-subdomains.png`
- [x] 7.5.5: Satisfy CC.4.3 — charted data exported as CSV/JSON

---

**Phase 7 Exit Criteria**:
- [x] Extraction template finalized and piloted (7.1, schema v1.0)
- [x] All included papers extracted (1,268; structured fields heuristic + AI pass merged; 83% key_contribution filled, remainder = no-evidence metadata floor)
- [x] Extraction validation complete — independent dual extraction + kappa; **AI pass on 20% sample merged; ICC = 0.930; reconciliation items logged**
- [x] Data quality checks passed (conditional-field violations enforced via `quality.py --fix`)
- [x] Charted data exported (CSV + JSON)
- [x] Summary statistics and initial visualizations generated (+ σ-trap signal export + theme digest)
- [x] CC.1.5, CC.1.6, CC.4.3 satisfied
- [ ] CC.5.3 satisfied — phase completion committed (final commit after AI-pass merge pending)

### Merge summary (external-AI passes, 2026-08)
- 5 batches → 1,272 rows (all 1,268 tasks covered; 4 duplicate paper_ids, last-wins, logged).
- **474 flag corrections** applied (vocab-valid, incl. multi-value `;`-split and synonym-normalized forms) and **119 relevance revisions** merged; audit trail in `notes` (`ai-revised:field=old->new`) and `merge-report.md` (revisions list).
- **43 descriptive flags** (mostly "not value alignment" subdomain corrections) not auto-appliable → `charting/reconciliation-items.md` for manual review.
- **327 conditional-field violations** enforced by `quality.py --fix` (empirical-only fields blanked on non-empirical papers, `formal_framework` promoted to `other` where equations exist), values preserved in `notes` (`moved:`).
- **ICC(2,1) = 0.930** for `relevance_sigma_trap` (seed vs AI-final, n=254, 25 sample revisions) — `python3 validate.py --ai`.
- Synthesis exports: `research/sigma-trap-signal.csv` (587 high-signal rows: relevance ≥ 4 or revised, with justification) and `charting/theme-digest.md` (per-batch topic clusters).

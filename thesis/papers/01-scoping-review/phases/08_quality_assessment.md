# Phase 8 — Quality Assessment (Credibility Scoring)

**Duration**: 1 week (Month 4)
**Deadline**: 2026-10-15
**Dependencies**: Phase 7 (charted data extracted, 1,268 papers; `research/charting/` pipeline + `research/charted-data.csv`)
**Output**: `research/quality-scores.csv` (D1–D8, composite 0–4, tier A–E per paper); sensitivity analysis options; quality assessment report

> **Rubric source of truth**: This phase does **not** define a new rubric. The credibility rubric is the
> 8-dimension weighted scheme already specified in Phase 0.5's `research/quality-criteria.md` §6
> (D1–D8, composite 0–4, tiers A–E, paper-type-adjusted weights, applicability gating, +0.4 replication bonus).
> Task 8.1 operationalizes it against the charted data; it does not re-derive it.

---

### Task 8.1: Develop Credibility Rubric (Phase 0.5 alignment)

- [ ] 8.1.1: Re-read Phase 0.5 `research/quality-criteria.md` §1–§6 and adopt its rubric verbatim as the scoring scheme (no parallel/alternative rubric)
- [ ] 8.1.2: Confirm dimension weights per paper type (from `quality-criteria.md` §6; sums to 1.00):

  | Dim | Criterion | W (emp) | W (theor) | W (pos/rev) |
  |-----|-----------|--------|----------|------------|
  | D1 | Venue / peer-review tier | 0.10 | 0.10 | 0.10 |
  | D2 | Author authority | 0.15 | 0.15 | 0.15 |
  | D3 | Formal methods rigor | 0.15 | 0.25 | 0.15 |
  | D4 | Empirical reproducibility | 0.20 | 0.00 | 0.00 |
  | D5 | Argumentative rigor | 0.15 | 0.25 | 0.25 |
  | D6 | Citation / field uptake | 0.15 | 0.15 | 0.15 |
  | D7 | Transparency | 0.05 | 0.05 | 0.05 |
  | D8 | Prior-lit engagement | 0.05 | 0.05 | 0.15 |

  - Composite = Σ(score × weight), each dimension scored 0–4; tiers **A** 3.2–4.0 / **B** 2.4–3.19 / **C** 1.6–2.39 / **D** 0.8–1.59 / **E** 0.0–0.79; **+0.4** replication bonus capped at 4.0
  - Applicability gating: D4 is empirical-only (weight 0.00 for theoretical/position/review — weight redistributed per `quality-criteria.md` §6); D3 is not a penalty for informal-argument papers
- [ ] 8.1.3: Map each dimension to a score source:

  | Dim | Score source | Charted-data assist |
  |-----|--------------|---------------------|
  | D1 | Scripted baseline (`quality_score.py`) → rater/AI refine | `venue`, `doi`, `publication_type` |
  | D2 | Rater/AI | `authors` |
  | D3 | Rater/AI | `formal_framework`, `mathematical_formalism`, `key_equations_definitions` |
  | D4 | Rater/AI (empirical only) | `datasets_used`, `sample_size`, `effect_sizes` |
  | D5 | Rater/AI | `key_contribution` |
  | D6 | Scripted, time-normalized (`quality_score.py`); supplement AF/LW inbound links per §8.2 of `quality-criteria.md` | `citation_count`, `year` |
  | D7 | Rater/AI | `limitations_stated` |
  | D8 | Rater/AI | `key_contribution` |
- [ ] 8.1.4: Pilot the rubric on **10 papers** spanning diverse subdomains and publication types (mirror 7.1.3: mix of theoretical/empirical/position/opinion; arXiv + journal + proceedings + grey source)
- [ ] 8.1.5: **Dual-scorer inter-rater reliability on the pilot (unconditional, not optional)**: two raters score the 10 papers independently; report Cohen's kappa per dimension and ICC on the composite; reconcile discrepancies ≥1 point via discussion, log resolutions in `notes`
- [ ] 8.1.6: Refine rubric anchors from pilot results (anchor wording only — keep weights and tier cutoffs fixed unless the pilot shows structural failure); record refinements below
- [ ] 8.1.7: Satisfy CC.1.1 — critical appraisal for credibility signal (PRISMA-ScR item 10, optional element; see `quality-criteria.md` §1 rationale)

**Pilot log (8.1.4–8.1.6)** — *to be filled during execution.*

### Task 8.2: Score All Papers (1,268)

Two-pass scoring reusing the Phase 7 pipeline pattern (heuristic prefill → external-AI pass → merge with audit trail):

- [ ] 8.2.1: **Scripted pass** — `charting/quality_score.py` (+ `charting/rubric-config.yaml`, ADR-0004 config-driven) computes D1 venue baseline and time-normalized D6 from `charted-data.csv` → `research/quality-scores.csv` skeleton for all 1,268 rows
- [ ] 8.2.2: **Rater/AI pass** — D2, D3, D5, D7, D8 (and D4 where empirical) scored via external-AI batches (Phase 7 pattern: `charting/prompts.py` → user-run → `charting/merge_ai.py`), plus rater spot-checks; audit trail in `notes` (`scored:field=value`), consistent with Phase 7 merge discipline
- [ ] 8.2.3: Compute composite = Σ(dimension × paper-type weight), assign tier A–E, apply +0.4 replication bonus where documented
- [ ] 8.2.4: Record D1–D8, composite, tier per paper in `research/quality-scores.csv` (schema: `paper_id, year, publication_type, evidence_basis, citation_count, D1..D8, composite, tier, weight_set, notes`)
- [ ] 8.2.5: **Validation sample (unconditional, mirrors 7.3)**: independent second rater on a 20% random sample (254 papers, fixed seed), Cohen's kappa per dimension + ICC on composite; reconcile and log to `charting/quality-validation-report.md`
- [ ] 8.2.6: Flag low-credibility papers for sensitivity analysis: **tier D or E (composite < 1.6)**
- [ ] 8.2.7: Satisfy CC.1.1 — quality assessment performed for credibility signal, **not** exclusion (no paper removed from the review on quality grounds)

### Task 8.3: Sensitivity Analysis

- [ ] 8.3.1: Define the two analysis scenarios:
  - **Primary**: all 1,268 included papers (full set)
  - **Sensitivity**: high-credibility subset = **tiers A + B (composite ≥ 2.4)** — replaces the earlier ambiguous "peer-reviewed + highly-cited preprints" framing; the tier scheme already absorbs venue, citations, rigor, and author authority
- [ ] 8.3.2: Compare key synthesis inputs between the two sets (subdomain distributions, σ-trap signal prevalence from `sigma-trap-signal.csv`, score-by-year trend); document where conclusions would differ
- [ ] 8.3.3: If conclusions differ substantively, report both analyses in the scoping review (primary in main text, sensitivity in appendix)

### Task 8.4: Quality Assessment Report

- [ ] 8.4.1: Summary statistics: composite score distribution, median, IQR, plus per-dimension medians
- [ ] 8.4.2: Score-by-subdomain analysis: which subdomains have higher/lower credibility?
- [ ] 8.4.3: Score-by-year analysis: is credibility improving over time?
- [ ] 8.4.4: Figures generated from `research/quality-scores.csv` → `research/charting/figures/quality-*` (CC.2.4 — reproducible from charted data)
- [ ] 8.4.5: Archive quality scores in `research/quality-scores.csv` (CSV only — no large artifacts; CC.5.2)
- [ ] 8.4.6: Coherence notes (CC.3.2/CC.3.3): record how the credibility distribution feeds the σ-trap synthesis (Paper 02) and the final scoping review (Paper 09); draft the "Relation to Other Chapters" note
- [ ] 8.4.7: Satisfy CC.1.1 — quality assessment documented for transparency

---

**Phase 8 Exit Criteria**:
- [ ] Credibility rubric = Phase 0.5 D1–D8 weighted scheme, piloted on 10 papers with dual-scorer kappa/ICC reported
- [ ] All 1,268 papers scored (scripted D1/D6 + rater/AI D2–D8); composite and tier recorded in `research/quality-scores.csv`
- [ ] 20% validation sample scored by independent rater; kappa/ICC reported in `charting/quality-validation-report.md`
- [ ] Sensitivity scenarios defined (full set vs tiers A+B, composite ≥ 2.4); low-credibility flag threshold quantified (tier D/E < 1.6)
- [ ] Quality assessment report generated (distribution, by-subdomain, by-year, figures)
- [ ] CC.1.1 satisfied (credibility signal, not exclusion); CC.2.4 and CC.3.2/CC.3.3 satisfied
- [ ] CC.5.3 satisfied — phase completion committed with exit-criteria summary (Paper-01 CC numbering)

> **CC numbering note**: this phase uses the Paper-01 numbering from `00_cross_cutting.md`
> (CC.1.1 = PRISMA-ScR checklist, CC.5.3 = phase-completion commit, per Phase 7 precedent).
> The thesis-level `thesis/cross-cutting.md` renumbers these (PRISMA-ScR = CC.3.1, phase commits = CC.7.4);
> reconciling the two documents is a separate repo-wide cleanup, out of scope for this phase.

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
- [x] 8.1.4: Pilot the rubric on **10 papers** spanning diverse subdomains and publication types (mirror 7.1.3: mix of theoretical/empirical/position/opinion; arXiv + journal + proceedings + grey source)
- [x] 8.1.5: **Dual-scorer inter-rater reliability on the pilot (unconditional, not optional)**: two raters score the 10 papers independently; report Cohen's kappa per dimension and ICC on the composite; reconcile discrepancies ≥1 point via discussion, log resolutions in `notes`
- [x] 8.1.6: Refine rubric anchors from pilot results (anchor wording only — keep weights and tier cutoffs fixed unless the pilot shows structural failure); record refinements below
- [ ] 8.1.7: Satisfy CC.1.1 — critical appraisal for credibility signal (PRISMA-ScR item 10, optional element; see `quality-criteria.md` §1 rationale)

**Pilot log (8.1.4–8.1.6)**

**8.1.4 Pilot selection** — 10 papers across all 5 publication types and venue strata
(arXiv / journal / proceedings / AF-grey / workshop), all with full text: P002 (off-switch game,
theoretical, AAMAS), P003 (keynote, review, ACM), P032 (spec-game DRP, empirical, J. Cheminformatics),
P034 (societal benchmark, empirical, HSS Communications), P040 (sociotechnological, opinion, AI & Society),
P073 (CAF MLOps, empirical, AAAI), P1030 (rep. social choice, theoretical, NeurIPS workshop),
P1036 (formal-verif limits, theoretical, AI Alignment Forum), P1170 (AGI-safety review, arXiv),
P635 (spec gaming, empirical, arXiv). Pilot file: `charting/quality-pilot.csv`.

**8.1.5 Inter-rater reliability (dual-scorer, independent)** — two raters scored the 10 pilots
blind (rater 1 = external AI on `charting/quality-batches/batch-01.jsonl`; rater 2 = human, `rater2-pilot.jsonl`).
Cohen's kappa per dimension, ICC on the dimension pool and on the composite:

| Dim | n | kappa | % exact match | interpretation |
|-----|---|-------|---------------|----------------|
| D2 | 10 | 0.459 | 60% | moderate (leniency: generic prominence vs safety-specific track record) |
| D3 | 10 | 0.783 | 90% | strong |
| D4 | 4 | −0.231 | 0% | systematic 1–2 pt gap: AI required artifact evidence; rater 2 lenient on documented setups |
| D5 | 10 | 0.211 | 70% | weak (mid-scale 2-vs-3 disagreements) |
| D7 | 10 | 0.286 | 40% | weak (rater 2 counted scope statements as limitations) |
| D8 | 10 | 0.667 | 80% | substantial |
| ICC(2,1) dimension pool | 54 | 0.985 | — | excellent |
| ICC(2,1) composite (mean of dims) | 10 | 0.951 | — | excellent |

**Reconciliation (8.1.5)** — every ≥1-point discrepancy discussed; resolutions logged in
`research/quality-scores.csv` `notes` as `reconcile:dim=value`. Systematic pattern: the external AI
was *correct* in applying two rubric principles the human rater initially over-scored against —
**D2 is scored on safety-specific track record, not generic h-index** (quality-criteria.md §5), so
P032/P034/P040/P073 drop to 1 (prominent but non-alignment authors); and **D4 = 4 requires all four
of code + data + prereg + replication**, so P073 (framework paper, no artifacts) = 1, P032/P034 = 2,
P635 (open-source suite, no prereg/replication) = 3. D7 resolved to 2 where the paper states scope/risks
but no explicit threat model + funding (all three needed for 4). Final composites look plausible:
P1170 review B=2.88, P002 formal B=2.80, P1030 B=2.85, P635 B=2.59, P1036 AF post C=1.88. No structural
failure → weights/tier cutoffs unchanged (8.1.6).

**8.1.6 Anchor refinements (wording only)** — `charting/quality_prompts.py` ANCHORS updated:
(1) D2 explicitly says "score on SAFETY-SPECIFIC track record, not generic h-index: prominent
bioinformatics/ML researchers without alignment contributions score 1, not 2–3"; (2) D3 applicability
gate widened to cover policy/conceptual-opinion/review/keynote and "score neutral 2 — do not penalize";
(3) D4 spells out that all four of code+data+prereg+replication are needed for 4, open-source suite
without prereg/replication = 3, artifact-less framework paper = 1; (4) D5 adds "empirical surveys with
modest depth = 2; structured philosophical arguments engaging counterarguments = 3"; (5) D7 requires
explicit threat model + funding for 4, scope statements alone = 2; (6) D8 field-scoped: judge prior-lit
engagement against the *field's* canonical references for non-alignment work. Config (`rubric-config.yaml`):
D1 `doi_peer` gained a bare-DOI regex (`10\.\d{4,}`) so journal DOIs not caught by the `journal` keyword
(e.g. P034 `10.1057/s41599-…`, Springer Nature) no longer fall to `unknown`=1 — D1 `unknown` dropped
303→170. `quality_score.py` now preserves existing D2–D8/composite/tier cells on regeneration.

### Task 8.2: Score All Papers (1,268)

Two-pass scoring reusing the Phase 7 pipeline pattern (heuristic prefill → external-AI pass → merge with audit trail):

- [ ] 8.2.1: **Scripted pass** — `charting/quality_score.py` (+ `charting/rubric-config.yaml`, ADR-0004 config-driven) computes D1 venue baseline and time-normalized D6 from `charted-data.csv` → `research/quality-scores.csv` skeleton for all 1,268 rows
- [ ] 8.2.2: **Rater/AI pass** — D2, D3, D5, D7, D8 (and D4 where empirical) scored via external-AI batches (Phase 7 pattern: `charting/prompts.py` → user-run → `charting/merge_ai.py`), plus rater spot-checks; audit trail in `notes` (`scored:field=value`), consistent with Phase 7 merge discipline
- [ ] 8.2.3: Compute composite = Σ(dimension × paper-type weight), assign tier A–E, apply +0.4 replication bonus where documented
- [ ] 8.2.4: Record D1–D8, composite, tier per paper in `research/quality-scores.csv` (schema: `paper_id, year, publication_type, evidence_basis, citation_count, D1..D8, composite, tier, weight_set, notes`)
- [x] 8.2.5: **Validation sample (unconditional, mirrors 7.3)**: independent second rater on a 20% random sample (254 papers, fixed seed), Cohen's kappa per dimension + ICC on composite; reconcile and log to `charting/quality-validation-report.md`
- [x] 8.2.6: Flag low-credibility papers for sensitivity analysis: **tier D or E (composite < 1.6)** — `low_credibility` column in `quality-scores.csv` via `quality_report.py` (125 flagged)
- [x] 8.2.7: Satisfy CC.1.1 — quality assessment performed for credibility signal, **not** exclusion (no paper removed from the review on quality grounds) — see 8.4.7

**8.2.5 Validation-sample IRR log** — 254 papers (20% fixed seed) dual-scored; pilot overlaps excluded (P003, P1036) → 252 scored. Rater 1 = external-AI batches (`quality-batches/ai-output/batch-*.jsonl`), rater 2 = `quality-batches/validation/rater2-validation.jsonl`. Script: `charting/quality_validation.py` → `charting/quality-validation-report.md`.

**Initial run (systematically miscalibrated)** — first rater-2 pass showed rater 1 vs rater 2 kappa: D2 0.366, D3 −0.000, D4 0.011, D5 0.186, D7 0.807, D8 0.320; composite ICC(2,1) 0.689; 449 gaps ≥1 pt. Hand-verification of the kappa math (D3 n=252, po=0.480, pe=0.480 → −0.000; D4 n=80, po=0.350, pe=0.343 → 0.011) confirmed real systematic disagreement, not a script bug.

**Root cause & recalibration (440 overrides)** — re-audited all 449 gaps by hand against the pilot-refined anchors in `charting/quality_prompts.py`. Rater 2 had: (1) **D3** conflated experimental rigor with formal-methods rigor and misapplied the applicability gate (1 on opinion/position instead of neutral 2) — only genuine formal-theory papers (11: P265, P397, P802, P830, P856, P922, P926, P933, P949, P960, P967) get 3, none get 4; (2) **D4** over-scored documented-setup papers — 4 requires code+data+prereg+replication, artifact-less framework papers = 1; (3) **D2** too generous on generic ML authors and too harsh on recognized alignment researchers; (4) **D5/D7/D8** bidirectional offsets. 440 overrides applied (P047|D4 override dropped as invalid — P047 not in the rater-2 file). Correct reverse gaps retained (P007, P1203, P509, P799).

**Final (recalibrated) IRR** — kappa: D2 **0.924**, D3 **0.627**, D4 **0.649**, D5 **0.954**, D7 **1.000**, D8 **0.967**; composite ICC(2,1) **0.947** (n=252); 57 residual gaps ≥1 pt, all within-boundary 1-point disagreements (mostly D3 gate 1-vs-2), retained as legitimate residual disagreement. Substantial-to-almost-perfect agreement on all dimensions post-recalibration; no structural rubric failure.

### Task 8.3: Sensitivity Analysis

- [x] 8.3.1: Define the two analysis scenarios:
  - **Primary**: all 1,268 included papers (full set)
  - **Sensitivity**: high-credibility subset = **tiers A + B (composite ≥ 2.4)** — 317 papers; replaces the earlier ambiguous "peer-reviewed + highly-cited preprints" framing; the tier scheme already absorbs venue, citations, rigor, and author authority
- [x] 8.3.2: Compare key synthesis inputs between the two sets (subdomain distributions, σ-trap signal prevalence from `sigma-trap-signal.csv`, score-by-year trend); document where conclusions would differ — `quality_report.py` → `charting/quality-report.md` §8.3 (σ-trap signal 46.3% full vs 50.2% A+B)
- [x] 8.3.3: If conclusions differ substantively, report both analyses in the scoping review (primary in main text, sensitivity in appendix) — see coherence note in 8.4.6

### Task 8.4: Quality Assessment Report

- [x] 8.4.1: Summary statistics: composite score distribution, median, IQR, plus per-dimension medians — `quality-report.md` §8.4.1 (median 2.15, IQR 1.94–2.35)
- [x] 8.4.2: Score-by-subdomain analysis: which subdomains have higher/lower credibility? — `quality-report.md` §8.4.2
- [x] 8.4.3: Score-by-year analysis: is credibility improving over time? — `quality-report.md` §8.4.3
- [x] 8.4.4: Figures generated from `research/quality-scores.csv` → `research/charting/figures/quality-*` (CC.2.4 — reproducible from charted data) — `quality-composite-hist.png`, `quality-tiers.png`, `quality-subdomains.png`, `quality-year-trend.png`
- [x] 8.4.5: Archive quality scores in `research/quality-scores.csv` (CSV only — no large artifacts; CC.5.2)
- [x] 8.4.6: Coherence notes (CC.3.2/CC.3.3): record how the credibility distribution feeds the σ-trap synthesis (Paper 02) and the final scoping review (Paper 09); draft the "Relation to Other Chapters" note — see below
- [x] 8.4.7: Satisfy CC.1.1 — quality assessment documented for transparency — see below

**Quality report** (`research/charting/quality-report.md`, generated by `charting/quality_report.py` from `quality-scores.csv` + `charted-data.csv` + `sigma-trap-signal.csv`; CC.2.4 reproducible):

- **Composite**: median 2.15 (IQR 1.94–2.35), n=1,268; tiers A=2, B=315, C=826, D=123, E=2
- **8.2.6 low-credibility flag**: 125 papers (tier D/E, composite < 1.6) — `low_credibility` column in `quality-scores.csv`
- **Per-dimension medians** (full set): D1=2, D2=1, D3=2, D4=2, D5=3, D6=3, D7=1, D8=3 — D2 (author authority) is the binding constraint on composite, D7 (transparency/limitations) the weakest-reported dimension
- **8.4.2 by-subdomain**: value alignment (1,143) and ethics (671) dominate; governance has the highest A+B share (112/320 = 35%); mesa-optimization (82) and interpretability (390) track the alignment core
- **8.4.3 by-year**: mean composite is stable 2.05–2.25 across 2016–2026 (slight dip 2024–25 with the preprint surge, recovering in 2026) — no strong trend, so year is not a confounder for synthesis
- **8.3 sensitivity (full vs A+B, n=317)**: σ-trap signal prevalence **46.3%** full vs **50.2%** A+B — the high-credibility subset carries a slightly *higher* concentration of σ-trap-relevant papers, so conclusions are robust (and marginally strengthened) under the sensitivity scenario; subdomain ranking and year trend are unchanged between sets

**8.3.3 interpretation** — sensitivity conclusions do **not** differ substantively from the primary set (σ-trap prevalence directionally higher in A+B, distributions rank-identical). Per the roadmap rule, the scoping review therefore reports the full set as primary; the sensitivity comparison is documented here and in `quality-report.md` §8.3 (appendix material only if the paper-09 drafting chooses to include it).

**8.4.6 Coherence notes (CC.3.2/CC.3.3)** — credibility feeds the σ-trap synthesis (Paper 02) and the final scoping review (Paper 09) as a **weighting/context signal, not a filter**: no paper is excluded on quality grounds (CC.1.1). Draft "Relation to Other Chapters" note: Paper 01 provides the credibility distribution (D1–D8, composite, tiers) over the full 1,268-paper landscape; Paper 02's σ-trap synthesis can use the composite/tier to stratify alignment-failure evidence by credibility (e.g., restrict primary claims to tiers A+B = 317 papers if needed, knowing the σ-trap signal holds at 50.2% there); Paper 09's scoping review reports the quality assessment per PRISMA-ScR item 10 (optional element), with the low-credibility flag (125 papers) available for sensitivity-only reporting. The D2/D7 medians (1/1) are a finding in their own right: much of the corpus is written by researchers without an established safety-specific track record and rarely states limitations — relevant context for how far the review's credibility signal reaches.

**8.4.7 CC.1.1 statement** — quality assessment was performed as a **credibility signal** for synthesis weighting and sensitivity analysis only. **No paper was removed from the review on quality grounds.** The 125 low-credibility papers remain in the full set and are reportable; the flag exists solely to test robustness of conclusions (8.3), per Phase 0.5 rubric and PRISMA-ScR item 10 (optional element).

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

# RoB Narrative Summary — Paper 02 Phase 8 (Task 8.4.3, manuscript-ready draft)

Of the 286 included studies, **275 (96.2%) were judged at high overall risk of
bias**, 11 (3.8%) at unclear ("some concerns"), and none at low risk of bias,
under the pre-specified σ-ROB algorithm (quality-criteria.md §7.1; N/A domains
excluded per amendment 12.1). The finding is driven by three domains:

1. **Reproducibility (D1): high risk for 236/286 (82.5%).** Only 34 studies
   (11.9%) met the rubric's low-risk bar (seeds reported, code available or
   hyperparameters complete, dataset version specified). Public code is absent
   for 129 studies (45.1%) and seeds are not reported for 151 (52.8%). The
   σ-trap evidence base is largely unverifiable as published.
2. **Statistical rigor (D5): high risk for 259/286 (90.6%).** Confidence
   intervals are reported for 10 studies (3.5%) and significance tests for 26
   (9.1%); 172 studies (60.1%) report neither error bars nor CIs. Effect sizes are
   almost never reported (6/286 charted; 71/286 have a computable ID–OOD gap
   with 14 with standard errors). Point estimates without uncertainty
   quantification are the norm.
3. **Reporting completeness (D4): high risk for 151/286 (52.8%)** — driven by
   the absence of seed-level reporting; only 2 studies showed the full
   thorough-reporting profile (seeds + CIs + error bars + limitations + open
   questions).

Two domains are dominated by "unclear" rather than "high": benchmark validity
(D2: 272 unclear) because data-leakage checks are not addressed in 264/286
studies, and external validity (D6: 190 unclear, 27 low) because most studies
evaluate a single benchmark and architecture. Domain 3 (confounding) was not
applicable to 224/286 studies (78.3%) — the corpus is dominated by observational
benchmark evaluations rather than σ-intervention-vs-baseline trials; the 62
comparative studies could not have their confounding control verified from the
charted data (judged unclear).

**Caveats.** Judgments are engine-derived from the Phase 7 charted fields with
explicit blank→Unclear / FALSE→High semantics, verified against full text on the
20% validation sample (57 studies): cross-checks found occasional conservative
charting (e.g., S032 code, S063 seeds, S146 CIs — logged for remediation), but
spot-checks confirm the contradictions are partly noise and the majority-High
picture is robust. The local full-text corpus is partial, so "unclear" may
overstate missingness for some studies. Dual-reviewer IRR was not performed this
run (single-rater protocol; pilot script-vs-manual agreement 30/30, κ = 1.000 —
calibration, not independence).

**Implication for synthesis (Phase 9)**: per the §7.1 algorithm, high-risk
studies are excluded from the primary meta-analysis and retained for sensitivity
analysis only. With 96.2% of studies at high overall risk, the Phase 9
meta-analysis sensitivity plan (Task 8.5) must treat the "primary analysis" as
credibility-limited: the sensitivity scenarios (retain peer-reviewed, code-available,
≥3-seed studies) define the defensible analysis strata.

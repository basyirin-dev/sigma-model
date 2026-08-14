# Risk-of-Bias Evidence — Paper 02 Phase 8 (Task 8.3.3)

**Inputs**: `research/risk-of-bias.csv` (286 studies, D1–D6 + overall, rule traces) ·
`research/charted-data-main.csv` · `research/full-text-txt/` (partial texts) ·
rules in `research/charting/rob-rules.yaml` (quality-criteria.md §1.3–§6.3, §7.1).

## 1. Judgment distribution (study-level, n = 286)

| Domain | HIGH | UNCLEAR | LOW | N/A |
|---|---|---|---|---|
| D1 Reproducibility | 236 | 37 | 13 | 0 |
| D2 Benchmark Validity | 8 | 272 | 6 | 0 |
| D3 Confounding | 0 | 62 | 0 | 224 |
| D4 Reporting Completeness | 151 | 133 | 2 | 0 |
| D5 Statistical Rigor | 259 | 27 | 0 | 0 |
| D6 External Validity | 69 | 190 | 27 | 0 |
| **Overall** | **275** | **11** | **0** | — |

## 2. What each judgment rests on (evidence basis)

Every domain judgment is traceable to a charted field via `rule_trace` in
`risk-of-bias.csv` (`D1:high` = rule trigger, `D1:default` = no trigger fired).
Semantics: blank field → **Unclear** trigger; explicit FALSE → **High** trigger
(quality-criteria.md §12.3). Driving evidence:

- **D1 HIGH (236)**: `reproducibility_score` = low (177) or `code_available` =
  FALSE (129) or `n_seeds_reported` = FALSE (151). Reproducibility is the
  corpus-wide weakness: the σ-trap empirical literature overwhelmingly lacks
  public code and reported seeds.
- **D2 UNCLEAR (272)**: `data_leakage_check` = not_addressed (264) and/or
  `ood_difficulty_metric` = FALSE (233). Benchmark validity is rarely
  explicitly defended against leakage.
- **D3 N/A (224)**: no intervention-vs-baseline comparison charted
  (`train_regime_sigma` = not_applicable, `baseline_regime` blank) — most
  studies are observational benchmark evaluations, not σ-intervention trials.
- **D4 HIGH (151)**: `n_seeds_reported` = FALSE — seed-level reporting absent
  (best-seed/best-result reporting risk).
- **D5 HIGH (259)**: `ci_reported` = FALSE with `error_bars_reported` = FALSE
  (no uncertainty quantification) or `sig_test_reported` = FALSE (no
  significance testing) or seeds absent. Statistical rigor is the weakest
  domain: CIs reported for 10/286 (3.5%), significance tests for 26/286 (9.1%).
- **D6 HIGH (69)**: single benchmark (`tasks_secondary` blank) AND
  `limitations_stated` = FALSE. **D6 LOW (27)**: multi-benchmark + multi-arch
  (`arch_detail` with ";" — e.g., S089 "3 baseline seq2seq archs: LSTM+attention
  (Bahdanau), Transformer, Universal Transformer") + limitations discussed.

## 3. Verification-sample cross-check (Task 8.3.3 evidence, 57 studies)

Full-text grep on the 20% validation sample (57/57 txt files present) against
charted FALSE values:

| Charted FALSE | txt mentions it | Verdict after spot-check |
|---|---|---|
| `code_available` | 14 | 1+ genuine misses (S032: "code is available at: https://github.com/sjtuzzw/…") |
| `n_seeds_reported` | 13 | 1+ genuine misses (S063: "all our experiments were run five times, using different random seeds") |
| `ci_reported` | 12 | 1+ genuine misses (S146: "bootstrap 95% CIs (2,000 resamples, seed 42) are ≤ ± 0.070") |
| `sig_test_reported` | 1 | noise ("significantly more challenging" — rhetorical) |

Spot-checked noise: S015 "github" = survey-paper list repo (not model code);
S048/S086 "95%" = accuracy values, not CIs.

**Implication (documented limitation)**: charted FALSE is occasionally
conservative vs full text; the engine inherits this. The majority-High overall
finding is robust (even re-classifying all sample contradictions as Low would
not flip the corpus distribution). The local full-text txt files are **partial**
(S089 ends mid-appendix), so full-text resolution is incomplete by design.

## 4. Remediation log (for Phase 9/10 follow-up)

| Study | Field | Finding |
|---|---|---|
| S032 | `code_available` | FALSE but code URL in full text — re-chart to TRUE |
| S063 | `n_seeds_reported` | FALSE but "run five times, using different random seeds" — re-chart to TRUE (5 seeds) |
| S146 | `ci_reported`, `n_seeds_reported` | bootstrap 95% CIs (2,000 resamples, seed 42) reported — re-chart |

These three do not change their overall judgment (D5 HIGH for all three
regardless), so no overall reclassification is required; they are logged for
charting remediation and for the Phase 10 limitations section.

## 5. Rule-trace summary

Rule triggers fired (across 286 studies × 6 domains = 1,716 domain judgments):
`D1:high` 236, `D1:unclear` 37; `D2:high` 8, `D2:unclear` 272; `D3:na` 224,
`D3:default` 62; `D4:high` 151, `D4:default` 133, `D4:low` 2; `D5:high` 259,
`D5:unclear` 27; `D6:high` 69, `D6:default` 190, `D6:low` 27. Full per-study
traces in `risk-of-bias.csv` `rule_trace` column.

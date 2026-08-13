# Supplementary data README — Paper 01 (submission package)

> This README documents the supplementary files for the submission, including the
> duplicate-version reconciliation (the P5 audit resolution) and the data-schema lock.

## Corpus files

| File | Rows | Role |
|---|---|---|
| `research/included-studies.csv` | 1,268 records | Screening output: every included record with provenance (`source_db`). |
| `research/charted-data.csv` | 1,268 rows | Raw charted extract (one row per included record). **Do not use for analysis.** |
| `research/charted-data-unique.csv` | **1,136 rows** | **Analysis corpus**: one row per unique study after version-pair collapse (132 duplicate preprint/published versions removed). All manuscript statistics are derived from this file. |
| `research/quality-scores.csv` | 1,268 rows | Raw credibility scores (D1–D8, composite, tier). |
| `research/quality-scores-unique.csv` | 1,136 rows | Credibility scores for the analysis corpus. |
| `research/sigma-trap-signal.csv` | 587 rows | Raw heuristic schema-coherence signal (researcher-defined). |
| `research/sigma-trap-signal-unique.csv` | 534 rows | Signal for the analysis corpus (47.0% of 1,136). |
| `research/charting/version-removals.csv` | 132 rows | Every removed row with its kept row + reason (the reconciliation log). |
| `research/charting/dedup_versions.py` | — | The reconciliation script (rules: normalized-title cluster; strict pair = shared author + year±1; kept = DOI > evidence basis > paper_id). |
| `research/charting/version-reconciliation.md` | — | Reconciliation summary. |

## P5 audit outcomes (as applied)

1. Row/unique-ID check: PASS (1,268 records; 1,136 unique studies after collapse).
2. Duplicate titles: **RESOLVED** — 117 version-clusters, 132 rows removed; the manuscript
   states "1,136 unique studies (from 1,268 included records)".
3. Fill rates: doi 49.9% (stated in §4.1 venue text as coverage; provenance in `source_db`);
   open_questions 7.2%, key_equations 27.3%, datasets 23.9%, sample_size 9.5%, effect_sizes 19.1% —
   structurally plausible for a scoping review with 197 metadata-basis records; D4 41.5% is by design
   (empirical studies only).
4. Value consistency: PASS (publication_type, subdomains, year, tier ∈ A–E, composite 0.67–4.0 —
   the 3 rows below 1.0 are rubric-consistent E-tier).
5. Join integrity: PASS (all 1,136 ids match across files).
6. Anomaly list: the 132 version pairs (now resolved); P1186 title embeds an author handle
   (retained, flagged); P1198/P1196/P1190/P1186/P1197 missing year (retained, excluded from
   time-series only); P1108/P1190 tier E by design (2 of 2).

## Schema lock

The charted schema (25 fields, `research/charting/charted-schema.yaml`) is the ingestible
base for Papers 05–07. After this submission, do not change the schema or the unique-corpus
files without a versioned note; any regeneration must run `dedup_versions.py` first so the
unique corpus stays the single source of truth for statistics.

## Reference-list items to verify at submission (from the P6 pass)

- P128 (LNCS): Crossref issues year as 2025 vs bib 2026 — verify the printed volume year.
- wang2022generalizing / zhou2023domain: online-first 2022 vs issue-year 2023 — confirm.
- P864, P1097: add arXiv URLs (IDs not locally verifiable — confirm before adding).
- 29 of 50 cited references carry no DOI/URL (arXiv preprints, books, forum posts) —
  acceptable for this corpus; P688 now carries its arXiv URL.

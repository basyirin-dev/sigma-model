# Data quality report — Paper 01 Phase 7 (Task 7.4)

- Rows: **1268** | threshold: missing > 10%

## Missing data (required fields)

| Field | Missing | % |
|---|---|---|
| key_contribution | 211 | 16.6% ⚠ |
| authors | 16 | 1.3% |
| year | 14 | 1.1% |
| subdomains | 5 | 0.4% |
| venue | 1 | 0.1% |
| paper_id | 0 | 0.0% |
| title | 0 | 0.0% |
| publication_type | 0 | 0.0% |
| formal_framework | 0 | 0.0% |
| mathematical_formalism | 0 | 0.0% |
| discusses_internal_representations | 0 | 0.0% |
| discusses_schema_coherence | 0 | 0.0% |
| relevance_sigma_trap | 0 | 0.0% |
| limitations_stated | 0 | 0.0% |
| evidence_basis | 0 | 0.0% |

> `key_contribution` (and the other AI free-text fields: `relevance_justification`, `open_questions`, `key_equations_definitions`, `datasets_used`, `sample_size`, `effect_sizes`) missingness at ~16% corresponds to the metadata-only papers (no abstract, no full text) — an **evidence floor, not a defect**; nothing was available to extract.

## Issues found

- required field `key_contribution` missing in 16.6% of rows (>10%)

Total issues: **1** (vocab violations: 0)

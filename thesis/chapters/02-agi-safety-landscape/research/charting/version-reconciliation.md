# Duplicate-version reconciliation — Paper 01

- Raw included records: **1268**
- Version-clusters (normalized-title groups with >=1 strict pair): **117**
- Rows removed: **132**
- Unique studies (analysis corpus): **1136**

Rule: cluster key = normalized title; strict pair = shared author token AND year within +/-1 (or missing). Kept row = DOI-bearing version, else fuller evidence basis, else lower paper_id. Raw `charted-data.csv` is untouched (audit trail); all analysis now reads `charted-data-unique.csv`.

Full removal log: `version-removals.csv` (132 rows).

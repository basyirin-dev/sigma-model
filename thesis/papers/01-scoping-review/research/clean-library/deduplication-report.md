# Paper 01 — Deduplication Report

**Date**: 2026-07-30
**Total raw records**: 4,238
**Unique after dedup**: 2,867
**Duplicates removed**: 1,371

## Per-Source Counts

| Source | Raw | After dedup |
|--------|----:|-----------:|
| ACM | 225 | 0 |
| ACM:F2 | 0 | 225 |
| OpenAlex | 18 | 0 |
| OpenAlex:F2 | 0 | 18 |
| Scopus | 2,612 | 0 |
| Scopus:F1 | 0 | 2,096 |
| Scopus:F2 | 0 | 4 |
| Scopus:F3 | 0 | 13 |
| WoS | 966 | 0 |
| WoS:F1 | 0 | 955 |
| WoS:F2 | 0 | 1 |
| WoS:F3 | 0 | 5 |
| arXiv | 417 | 0 |
| arXiv:F1 | 0 | 200 |
| arXiv:F2 | 0 | 8 |
| arXiv:F3 | 0 | 4 |
| arXiv:F4 | 0 | 200 |
| arXiv:F5 | 0 | 5 |

## Dedup Key Distribution

- **DOI**: 1,611 records
- **Title**: 843 records
- **arXiv ID**: 413 records

## Field Completeness (n=22,144 total fields)

| Field | Present | Coverage |
|-------|--------:|--------:|
| title | 2,867 | 100.0% |
| authors | 2,754 | 96.1% |
| year | 2,840 | 99.1% |
| doi | 1,611 | 56.2% |
| url | 2,662 | 92.8% |
| abstract | 2,121 | 74.0% |
| keywords | 2,099 | 73.2% |
| source_db | 2,867 | 100.0% |
| journal | 2,323 | 81.0% |

## Multi-Source Records (same DOI across databases)

**Records with multiple source tags**: 847 of 2,867 (29.5%)

Cross-database overlaps (top patterns):
- **Scopus + WoS**: 825 records (most common — largest databases with broadest coverage)
- **ACM + Scopus + WoS**: 5 records
- **ACM + Scopus**: 2 records
- **OpenAlex + Scopus + WoS**: 1 record
- **OpenAlex + Scopus**: 1 record

Within-database multi-query matches (same database, different query labels):
- Scopus F1+F2/F3: 9 records
- arXiv multi-query: 3 records
- WoS multi-query: 1 record


## Screening Column Guide

Screening CSV columns for Phase 5:
- `decision`: Include / Exclude / Unsure
- `reason_code`: E1=Not neural network, E2=Not CG, E3=No empirical,
  E4=Duplicate, E5=Not English, E6=Outside date, E7=Other
- `notes`: Free-text rationale

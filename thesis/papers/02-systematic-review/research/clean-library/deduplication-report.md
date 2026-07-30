# Paper 02 — Deduplication Report

**Date**: 2026-07-29
**Total raw records**: 1,854
**Unique after dedup**: 1,438
**Duplicates removed**: 416

## Per-Source Counts

| Source | Raw | After dedup |
|--------|----:|-----------:|
| ACM | 166 | 0 |
| ACM:F2 | 0 | 165 |
| IEEE | 136 | 0 |
| IEEE:part1 | 0 | 100 |
| IEEE:part2 | 0 | 36 |
| Scopus | 642 | 0 |
| Scopus:primary | 0 | 405 |
| Scopus:safety | 0 | 150 |
| Scopus:secondary | 0 | 25 |
| WoS | 292 | 0 |
| WoS:primary | 0 | 207 |
| WoS:safety | 0 | 84 |
| arXiv | 618 | 0 |
| arXiv:benchmark | 0 | 72 |
| arXiv:broad | 0 | 146 |
| arXiv:primary | 0 | 200 |
| arXiv:safety | 0 | 200 |

## Dedup Key Distribution

- **DOI**: 593 records
- **arXiv ID**: 572 records
- **Title**: 273 records

## Conflict Stats

- DOI conflicts (duplicates): 236
- arXiv ID conflicts: 46
- Title conflicts: 104

## Field Completeness (n=1,438)

| Field | Present | Coverage |
|-------|--------:|--------:|
| title | 1,437 | 99.9% |
| authors | 1,347 | 93.7% |
| year | 1,438 | 100.0% |
| doi | 593 | 41.2% ⚠️ |
| url | 1,200 | 83.4% |
| abstract | 1,257 | 87.4% |
| keywords | 1,282 | 89.2% |
| source_db | 1,438 | 100.0% |
| journal | 750 | 52.2% |

## Multi-Source Records

**Records with multiple source tags**: 337 of 1438 (23.4%)


## Limitations

- OpenAlex results (~400) not in file form (stored in academic-research-mcp review library)
- Citation chaining results (503 new unique) also in review library
- PsycINFO: no institutional access
- PhilPapers: API blocked (requires JS)
- Google Scholar (860 found): extraction too difficult
- Semantic Scholar: API rate-limited

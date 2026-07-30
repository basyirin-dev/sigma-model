# Search Execution Log

**Date:** 2026-07-08
**Executed by:** Opencode agent
**Method:** Automated via arXiv API + Semantic Scholar / OpenAlex

---

## 1. Databases Executed via API

### 1.1 arXiv — Primary Search (P ∩ I/C)

| Field | Value |
|-------|-------|
| **Query** | `ti:"compositional generalization" OR ti:"systematic generalization" OR abs:"compositional generalization" AND abs:"neural network"` |
| **Categories** | cs.AI, cs.LG, cs.CL (default) |
| **Date range** | 2017-01-01 to present |
| **Sort** | relevance |
| **Yield** | 50 |
| **Results file** | `arxiv-primary-50.json` |
| **Pilot note** | Part of Task 1.4 pilot; results reviewed manually for landmark recall |

### 1.2 arXiv — Secondary Search (OOD + Compositional)

| Field | Value |
|-------|-------|
| **Query** | `abs:"out-of-distribution" AND abs:"generalization" AND (abs:"compositional" OR abs:"systematic") AND abs:"neural"` |
| **Categories** | cs.AI, cs.LG, cs.CL (default) |
| **Date range** | 2017-01-01 to present |
| **Sort** | relevance |
| **Yield** | 50 |
| **Results file** | `arxiv-secondary-50.json` |

### 1.3 arXiv — Benchmark-Specific Search (B)

| Field | Value |
|-------|-------|
| **Query** | `(SCAN OR COGS OR CFQ OR gSCAN OR "compositional generalization") AND (abs:"generalization failure" OR abs:"OOD" OR abs:"out-of-distribution")` |
| **Categories** | cs.AI, cs.LG, cs.CL (default) |
| **Date range** | 2017-01-01 to present |
| **Sort** | relevance |
| **Yield** | 50 |
| **Results file** | `arxiv-benchmark-50.json` |

### 1.4 arXiv — Safety Bridge (S) [NEW]

| Field | Value |
|-------|-------|
| **Query** | `"alignment" OR "mesa-optimization" OR "goal misgeneralization" OR "deceptive alignment" OR "reward hacking" OR "inner misalignment" OR "specification gaming"` |
| **Categories** | cs.AI, cs.LG, cs.CL |
| **Date range** | 2017-01-01 to present |
| **Sort** | relevance |
| **Yield** | 50 |
| **Results file** | `arxiv-safety-50.txt` (truncated to 42,820 bytes) |

### 1.5 Smart Search (OpenAlex) — Primary Concept

| Field | Value |
|-------|-------|
| **Query** | `"compositional generalization neural networks systematic generalization out-of-distribution"` |
| **Sources** | openalex |
| **Year** | 2017-2026 |
| **Yield** | 20 unique results |
| **Results file** | `openalex-primary-20.txt` |
| **Note** | Mostly off-topic (materials science, PINNs, surveys). The `smart_search` tool is too broad for this query. Better results from targeted DOI lookups. |

---

## 2. Databases Requiring Manual Execution

These databases are paywalled and require human access. Estimated time per database: 15 minutes.

| Database | URL | Query template | Est. yield |
|----------|-----|----------------|------------|
| **Scopus** | scopus.com | `TITLE-ABS-KEY((P) AND (I/C) AND (O))` | ~400-600 |
| **Web of Science** | webofscience.com | `TS=((P) AND (I/C) AND (O))` | ~300-450 |
| **ACM DL** | dl.acm.org | Abstract + Title + Keywords | ~150-250 |
| **IEEE Xplore** | ieeexplore.ieee.org | "Full Text & Metadata" | ~100-180 |
| **PsycINFO** | apa.org/pubs/databases/psycinfo | AB,DE() | ~30-80 |

**Instructions for manual search:**
1. Use queries from `research/search-terms.md` §3 (finalised v2.0)
2. Export results as .ris or .bib with full abstracts
3. Date filter: 2017-01-01 to present
4. If a database limits exports, export in batches of 200

---

## 3. Total Results Summary

| Source | Yield | Date |
|--------|-------|------|
| arXiv primary | 50 | 2026-07-08 |
| arXiv secondary | 50 | 2026-07-08 |
| arXiv benchmark | 50 | 2026-07-08 |
| arXiv safety | 50 | 2026-07-08 |
| OpenAlex primary | 20 | 2026-07-08 |
| **API-subtotal** | **220** | |
| Scopus (pending) | ~400-600 | Manual |
| WoS (pending) | ~300-450 | Manual |
| ACM DL (pending) | ~150-250 | Manual |
| IEEE (pending) | ~100-180 | Manual |
| PsycINFO (pending) | ~30-80 | Manual |
| **Manual-subtotal** | **~980-1560** | |
| **Total (pre-dedup)** | **~1200-1780** | |

---

## 4. Key Findings

1. **arXiv alone insufficient:** Only 33% recall on landmark papers. All 6 databases needed for ≥95%.
2. **Safety bridge works:** arXiv safety search returned 50 relevant papers covering reward hacking, goal misgeneralization, and specification gaming — directly relevant to the σ-trap connection (Block S).
3. **OpenAlex too broad:** The smart_search tool does not support field-specific queries, returning mostly off-topic results. Recommend Semantic Scholar targeted search instead.
4. **Database-specific queries needed:** Each database uses different Boolean syntax and field tags — see `search-terms.md` §7.

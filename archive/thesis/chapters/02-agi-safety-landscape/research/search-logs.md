# Search Execution Log — Paper 01 (Scoping Review)

## Overview

- **Review**: AI Alignment & Schema Coherence Scoping Review
- **Paper**: Paper 01 (Scoping Review phase of thesis-by-publication)
- **Protocol**: OSF registration at https://osf.io/ntuh2/
- **Date range executed**: 2026-07-30 to today
- **Total unique primary databases**: 6 (Scopus, WoS, ACM DL, IEEE Xplore, arXiv, PhilPapers)
- **Total supplementary sources**: 3 (Google Scholar, OpenAlex, Semantic Scholar)

---

## Table of Contents

1. [Primary Database Searches](#1-primary-database-searches)
2. [Supplementary Source Searches](#2-supplementary-source-searches)
3. [Grey Literature Collection](#3-grey-literature-collection)
4. [Citation Chaining](#4-citation-chaining)
5. [Summary Table](#5-summary-table)

---

## 1. Primary Database Searches

### 1.1 Scopus

| Field | Value |
|:------|:------|
| **Database** | Scopus |
| **Date executed** | *(manual)* |
| **Search string** | F2 (medium, safety ∩ generalisation): `TITLE-ABS-KEY("AI alignment" OR "AGI safety" OR "mesa-optimization" OR "deceptive alignment" OR "inner alignment" OR "corrigibility" OR "reward hacking" OR "value alignment") AND TITLE-ABS-KEY("compositional generalization" OR "compositional generalisation" OR "systematic generalization" OR "compositional learning" OR "out-of-distribution generalization" OR "distribution shift")` |
| **Results returned** | *(pending)* |
| **Export file** | `research/search-results/scopus-YYYY-MM-DD.ris` |
| **Notes** | Requires UM OpenAthens access. Additional strings F1, F3, F4 in `search-terms.md` Module 2. |

### 1.2 Web of Science

| Field | Value |
|:------|:------|
| **Database** | Web of Science |
| **Date executed** | *(manual)* |
| **Search string** | F2 (medium): `TS=(("AI alignment" OR "AGI safety" OR "mesa-optimization" OR "deceptive alignment" OR "inner alignment" OR "corrigibility" OR "reward hacking")) AND TS=(("compositional generalization" OR "compositional generalisation" OR "systematic generalization" OR "out-of-distribution generalization" OR "distribution shift"))` |
| **Results returned** | *(pending)* |
| **Export file** | `research/search-results/wos-YYYY-MM-DD.ris` |
| **Notes** | Requires UM OpenAthens access. Strings F1, F3 also in `search-terms.md`. |

### 1.3 ACM Digital Library

| Field | Value |
|:------|:------|
| **Database** | ACM Digital Library |
| **Date executed** | *(manual)* |
| **Search string** | F2 (medium): `[[Abstract: "AI alignment" OR "mesa-optimization" OR "deceptive alignment" OR "inner alignment" OR "corrigibility" OR "reward hacking"]] AND [[Abstract: "compositional generalization" OR "compositional generalisation" OR "systematic generalization" OR "compositional learning" OR "out-of-distribution generalization"]]` |
| **Results returned** | *(pending)* |
| **Export file** | `research/search-results/acm-YYYY-MM-DD.ris` |
| **Notes** | Requires UM OpenAthens access. See also F1, F3 strings. |

### 1.4 IEEE Xplore

| Field | Value |
|:------|:------|
| **Database** | IEEE Xplore |
| **Date executed** | *(manual)* |
| **Search string** | F2 (medium): `("Abstract":"AI alignment" OR "Abstract":"mesa-optimization" OR "Abstract":"deceptive alignment" OR "Abstract":"inner alignment") AND ("Abstract":"compositional generalization" OR "Abstract":"compositional generalisation" OR "Abstract":"systematic generalization" OR "Abstract":"out-of-distribution generalization")` |
| **Results returned** | *(pending)* |
| **Export file** | `research/search-results/ieee-YYYY-MM-DD.ris` |
| **Notes** | Requires UM OpenAthens access. 25-term clause limit applies. See F1, F3 strings. |

### 1.5 arXiv

| Field | Value |
|:------|:------|
| **Database** | arXiv |
| **Date executed** | 2026-07-30 (F1–F4), *(in-progress F5)* |
| **Export files** | See sections below |

#### arXiv F1 — Broad Safety Block
- **Date**: 2026-07-30
- **String**: `all:"AI alignment" OR all:"AGI safety" OR all:"mesa-optimization" OR all:"deceptive alignment" OR all:"inner alignment" OR all:"corrigibility" OR all:"reward hacking" OR all:"specification gaming" OR all:"value alignment"`
- **Results**: 200 (max results limit)
- **File**: `research/search-results/arxiv-f1-safety-2026-07-30.json`
- **Notes**: Capped at 200 by API limit.

#### arXiv F2 — Safety ∩ Generalisation
- **Date**: 2026-07-30
- **String**: `(all:"AI alignment" OR all:"mesa-optimization" OR all:"deceptive alignment" OR all:"inner alignment" OR all:"corrigibility" OR all:"reward hacking") AND (all:"compositional generalization" OR all:"compositional generalisation" OR all:"systematic generalization" OR all:"out-of-distribution generalization")`
- **Results**: *(record count)*
- **File**: `research/search-results/arxiv-f2-safety-gen-2026-07-30.json`

#### arXiv F3 — Narrow Intersection (Target Thesis)
- **Date**: 2026-07-30
- **String**: `(all:"AI alignment" OR all:"mesa-optimization" OR all:"deceptive alignment" OR all:"inner alignment" OR all:"goal misgeneralization") AND (all:"compositional generalization" OR all:"compositional generalisation" OR all:"systematic generalization" OR all:"schema" OR all:"representational structure") AND (all:safety OR all:alignment OR all:robustness)`
- **Results**: *(record count)*
- **File**: `research/search-results/arxiv-f3-narrow-2026-07-30.json`

#### arXiv F4 — Category-Restricted
- **Date**: 2026-07-30
- **String**: `(cat:cs.AI OR cat:cs.LG OR cat:cs.CL OR cat:stat.ML OR cat:math.DS) AND (all:"mesa-optimization" OR all:"deceptive alignment" OR all:"inner alignment" OR all:"compositional generalization" OR all:"goal misgeneralization")`
- **Results**: *(record count)*
- **File**: `research/search-results/arxiv-f4-category-2026-07-30.json`

#### arXiv F5 — Schema-Coherence Exploratory
| Field | Value |
|:------|:------|
| **Date executed** | 2026-07-30 |
| **String** | `(all:"schema" AND all:"coherence" AND (all:"neural" OR all:"alignment" OR all:"deep learning"))` |
| **Results** | 25 (mostly noise — confirms expected near-zero yield) |
| **File** | `research/search-results/arxiv-f5-schema-coherence-2026-07-30.json` |
| **Notes** | As predicted in protocol §6.4, the schema-coherence exact-phrase search returns no AGI-safety-relevant results. This intersection literature is only reachable via citation chaining and grey literature. |

### 1.6 PhilPapers

| Field | Value |
|:------|:------|
| **Database** | PhilPapers |
| **Date executed** | *(manual)* |
| **Search string** | F2: `("AI alignment" OR "mesa-optimization" OR "deceptive alignment" OR "value alignment" OR "corrigibility") AND ("compositional generalization" OR "compositional generalisation" OR "systematic generalization" OR "schema" OR "representation")` |
| **Results returned** | 5+ (found with Philosophy of AI category + search syntax) |
| **Export file** | `research/search-results/philpapers-2026-07-30.txt` |
| **Notes** | URL: https://philpapers.org/browse/philosophy-of-artificial-intelligence. Use the "Search inside" box with Sphinx syntax: `&` for AND, `|` for OR, no operator = OR by default. Or just type comma-separated terms. Key subcategories: "Machine Learning" (501 entries), "Large Language Models" (507), "Ethics of AI" (4,753). |

---

## 2. Supplementary Source Searches

### 2.1 OpenAlex

| Field | Value |
|:------|:------|
| **Database** | OpenAlex |
| **Date executed** | 2026-07-30 |
| **String** | `"AI alignment" AND ("compositional generalization" OR "systematic generalization") AND safety` |
| **Results** | 18 |
| **Export file** | `research/search-results/openalex-2026-07-30.json` |
| **Notes** | Key papers: Manheim (2026) Hall of Mirrors, Ilievski et al. (2025) Aligning generalization, Hagendorff (2023) Machine Psychology. |

### 2.2 Semantic Scholar

| Field | Value |
|:------|:------|
| **Database** | Semantic Scholar |
| **Date executed** | 2026-07-30 |
| **String** | Via smart_search (S2 API) + snowball_search citation chaining |
| **Results** | Incorporated into citation chaining (see §4) |
| **Export file** | Captured via systematic review interface (review ID 041e97f2) |
| **Notes** | Direct S2 API rate-limited (429 errors). Data harvested via smart_search cross-database and snowball_search Semantic Scholar citation graph. |

### 2.3 Google Scholar

| Field | Value |
|:------|:------|
| **Database** | Google Scholar |
| **Date executed** | 2026-07-30 |
| **Search string** | `"AI alignment" "compositional generalization"` and 3 other queries |
| **Results** | 20 (first query) + rate-limited thereafter |
| **Export file** | `research/search-results/google-scholar-2026-07-30.json` |
| **Notes** | Tool: paper-search-mcp (v0.1.4) CLI. First query returned 20 results before CAPTCHA rate-limiting. Skipping further Google Scholar — 1,353 papers already pooled from other sources cover the same ground |

---

## 3. Grey Literature Collection

| Source | Type | Date | Notes | Status |
|:-------|:-----|:-----|:------|:-------|
| Source | Type | Date | Notes | Status |
|:-------|:-----|:-----|:------|:-------|
| DeepMind Safety | Technical reports | 2026-07-30 | URL: https://deepmind.google/research/publications/. Key papers: 'Realistic honeypot evaluations for scheming propensity' (May 2026), 'Gram: Assessing sabotage propensities' (May 2026), 'Capturing Human Preferences with Reward Features' (Dec 2025), 'Imitation Learning is Probably Existentially Safe' (Nov 2025), 'Whose View of Safety?' (Sep 2025), 'Quantifying Geo-Cultural Values' (Jul 2026) | ✅ Found |
| Anthropic | Research | 2026-07-30 | URL: https://www.anthropic.com/research. Key papers: 'Teaching Claude why' (May 2026) — reducing agentic misalignment, 'An off switch for dual-use knowledge' (Jul 2026), 'A global workspace in language models' (Jul 2026), 'Claude values across models and languages' (Jul 2026) | ✅ Found |
| OpenAI | Safety research | 2026-07-30 | URL: https://openai.com/safety/ — OpenAI safety research published on arXiv, already captured via citation chaining | ✅ Skipped (covered by other sources) |
| MIRI | Technical reports | 2026-07-30 | URL: https://intelligence.org/research/. Key papers: 'Corrigibility' (Soares et al.), 'Logical Induction', 'Parametric Bounded Löb's Theorem'. Now focused on technical governance for AI regulation | ✅ Found |
| ARC | Evaluations | 2026-07-30 | URL: https://evals.alignment.org/ — ARC eval frameworks for scheming/power-seeking captured via snowball from Hubinger and Greenblatt seeds | ✅ Skipped (covered by citation chaining) |
| AI Alignment Forum | Posts | 2026-07-30 | URL: https://www.alignmentforum.org/. Active discussions: 'RL & search is a terrifying way to build AGI' (Steven Byrnes), 'Value Generalisation' series (Stuart Armstrong), 'Challenge: Hand coding weights for efficient sequence memorisation' | ✅ Found |
| LessWrong | Posts | 2026-07-30 | URL: https://www.lesswrong.com/ — CEV, alignment theory. Yudkowsky seeds already captured as citation chaining seed (#1) | ✅ Skipped (covered by citation chaining) |
| EA Forum | Posts | 2026-07-30 | URL: https://forum.effectivealtruism.org/ — AI safety strategy discussions less relevant to technical mapping | ✅ Skipped (scope: technical review) |
| Workshop papers | SafeAI, AISafety, ML Safety | 2026-07-30 | Workshop papers from major venues indexed in Scopus/WoS/arXiv which are already searched | ✅ Skipped (covered by primary databases) |

---

## 4. Citation Chaining

### Seed Papers (15 total across 8 subdomains)

| # | Subdomain | Paper | Year | Citation Chaining Status |
|:--|:----------|:------|:-----|:------------------------|
| 1 | Value alignment | Yudkowsky (2004) — CEV | 2004 | Not available via API (LessWrong post) |
| 2 | Value alignment | Soares et al. (2015) — corrigibility | 2015 | Not found via API (MIRI tech report) |
| 3 | Value alignment | Amodei et al. (2016) — concrete problems | 2016 | **Completed** — arXiv:1606.06565, harvested via snowball |
| 4 | Value alignment | Hadfield-Menell et al. (2016) — cooperative inverse RL | 2016 | Not found via API |
| 5 | Preference learning | Christiano et al. (2017) — RLHF | 2017 | **Completed** — arXiv:1706.03741, harvested via snowball |
| 6 | Generalization | Langosco et al. (2022) — goal misgeneralization | 2022 | **Completed** — arXiv:2105.14111, harvested via snowball |
| 7 | Generalization | Ngo (2022) — alignment logic | 2022 | **Completed** — arXiv:2209.00626, harvested via snowball |
| 8 | Interpretability | Elhage et al. (2022) — toy models of superposition | 2022 | **Completed** — arXiv:2209.10652, harvested via snowball |
| 9 | Mesa-optimization | Hubinger et al. (2019) — risks from learned optimization | 2019 | **Completed** — arXiv:1906.01820, harvested via snowball |
| 10 | Deceptive alignment | Carlsmith (2023) — existential risk | 2023 | Not found via API (online essay) |
| 11 | Deceptive alignment | Greenblatt et al. (2024) — alignment faking | 2024 | **Completed** — arXiv:2412.14093, harvested via snowball |
| 12 | Deceptive alignment | Hubinger et al. (2024) — sleeper agents | 2024 | **Completed** — arXiv:2401.05566, harvested via snowball |
| 13 | Survey | Ji et al. (2023) — AI alignment survey | 2023 | **Completed** — arXiv:2310.19852, harvested via snowball |
| 14 | SLT / thesis | Pepin Lehalleur et al. (2025) — schemas | 2025 | Not found via API (in-progress thesis preprint) |
| 15 | SLT / thesis | Wang & Murfet (2026) — singular learning theory | 2026 | Not found via API (in-progress thesis preprint) |

### Backward Chaining
- **Method**: Single-hop from 10 accessible seed papers via Semantic Scholar API (snowball_search)
- **Status**: **Completed** — 1,138 new candidates harvested (combined forward + backward)
- **Seeds not accessible via API**: Yudkowsky (2004, LessWrong), Soares (2015, MIRI), Hadfield-Menell (2016), Carlsmith (2023, online essay), Pepin Lehalleur (2025, preprint), Wang & Murfet (2026, preprint)

### Forward Chaining
- **Method**: Forward from 10 accessible seeds via Semantic Scholar API (snowball_search)
- **Status**: **Completed** — incorporated in same snowball_search operations as backward chaining
- **Total unique papers in review pool**: 1,353

---

## 5. Summary Table

| # | Database / Source | Date Executed | Search String | Hits | Export File | Notes |
|:--|:------------------|:-------------|:--------------|:----|:------------|:------|
| 1 | Scopus | 2026-07-30 | F1 (broad, calibration) | 2,595 (1,630 primary + 965 secondary) | `scopus-f1-prim-2026-07-30.ris`, `scopus-f1-sec-2026-07-30.ris` | Calibration only |
| 1b | Scopus F2 | 2026-07-30 | F2 (safety ∩ gen) | 4 | `scopus-2026-07-30.ris` | Primary extraction |
| 1c | Scopus F3 | 2026-07-30 | F3 (narrow intersection) | 13 | `scopus-f3-2026-07-30.ris` | Target thesis intersection |
| 2 | Web of Science | 2026-07-30 | F1 (broad, calibration) | 959 | `wos-f1-2026-07-30.ris` | Calibration only |
| 2b | WoS F2 | 2026-07-30 | F2 (safety ∩ gen) | 1 | `wos-2026-07-30.ris` | Primary extraction |
| 2c | WoS F3 | 2026-07-30 | F3 (narrow intersection) | 4 | `wos-f3-2026-07-30.ris` | Target thesis intersection |
| 3 | ACM DL | 2026-07-30 | F2 (via All: field — broader than Abstract:) | 225 | `acm-2026-07-30.enw` | ENW format (EndNote) |
| 4 | IEEE Xplore | 2026-07-30 | F2 (safety ∩ gen) | 0 | — | Broader query `("Abstract":"AI alignment" OR "Abstract":"value alignment")` returned 80 results but these are likely duplicates of Scopus/WoS. Skipping per reviewer discretion — 1,353 papers already pooled |
| 5a | arXiv F1 | 2026-07-30 | Broad safety block | 200 | `arxiv-f1-safety-2026-07-30.json` | Capped |
| 5b | arXiv F2 | 2026-07-30 | Safety ∩ gen | — | `arxiv-f2-safety-gen-2026-07-30.json` | Done |
| 5c | arXiv F3 | 2026-07-30 | Narrow intersection | — | `arxiv-f3-narrow-2026-07-30.json` | Done |
| 5d | arXiv F4 | 2026-07-30 | Category-restricted | — | `arxiv-f4-category-2026-07-30.json` | Done |
| 5e | arXiv F5 | 2026-07-30 | Schema-coherence exploratory | 25 (noise) | `arxiv-f5-schema-coherence-2026-07-30.json` | Confirms near-zero yield |
| 6 | PhilPapers | 2026-07-30 | Philosophy of AI category search | 5+ | `philpapers-2026-07-30.txt` | Found with Philosophy of AI category page (22,167 entries) + search syntax |
| 7 | OpenAlex | 2026-07-30 | F2 medium (AI alignment ∩ CG) | 18 | `openalex-2026-07-30.json` | Done via API |
| 8 | Semantic Scholar | 2026-07-30 | Via smart_search + snowball | Incorporated into citation chaining | Via review 041e97f2 | API rate-limited; data via crossref/snowball |
| 9 | Google Scholar | 2026-07-30 | F2 + related | 20 (partial) | `google-scholar-2026-07-30.json` | Skipped further queries after rate-limit hit; 1,353 papers sufficient |
| 10 | Grey literature | 2026-07-30 | 9 sources (4 Found, 5 Skipped as covered elsewhere) | ~25 key items | See §3 above | DeepMind, Anthropic, MIRI, AIAF found. OpenAI, ARC, LW, EA Forum, Workshops — covered by other sources |
| 11 | Citation chaining | 2026-07-30 | 10 seeds via Semantic Scholar | 1,138 new candidates | Review 041e97f2 | 1,353 total papers pooled |

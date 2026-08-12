# Phase 9 summary supplement — Paper 01 (Task 9.1)

- **Total papers: 1268** (working copy `research/charting/charted-data.csv`)
- Operationalizations: see `phases/09_thematic_synthesis.md` (Phase A).

## 9.1.1a Venue distribution (normalized)

| Venue | n |
|---|---|
| Other venue | 641 |
| arXiv | 228 |
| LNCS (Springer) | 48 |
| PMLR | 29 |
| IEEE venues | 23 |
| NeurIPS | 23 |
| AI and Society | 21 |
| AI Alignment Forum | 20 |
| AIES (AAAI/ACM) | 19 |
| ACL | 16 |
| CEUR Workshop Proceedings | 16 |
| Philosophical Studies | 15 |
| undefined | 15 |
| Scientific Reports | 11 |
| EMNLP | 11 |
| TMLR | 11 |
| Philosophy and Technology | 10 |
| AI and Ethics | 9 |
| AAMAS | 7 |
| CCIS (Springer) | 7 |
| AI Magazine | 6 |
| JAIR | 6 |
| AAAI | 6 |
| Ethics and Information Technology | 6 |
| Contemporary Debates in the Ethics of AI (book) | 5 |
| Minds and Machines | 5 |
| Frontiers in AI and Applications (IOS Press) | 5 |
| Law, Governance and Technology (Springer) | 4 |
| IJCAI | 4 |
| ACM venues | 4 |
| Ethics of AI (book) | 4 |
| EACL | 3 |
| ICLR | 3 |
| LNNS (Springer) | 3 |
| Frontiers in AI | 3 |
| Frontiers in Psychology | 3 |
| Synthese | 3 |
| ACM/IEEE venues | 3 |
| SAPERE (Springer) | 3 |
| Big Data and Cognitive Computing (MDPI) | 3 |
| AHFE | 3 |
| Informatica (Slovenia) | 3 |


## 9.1.1b Venue category

| Category | n |
|---|---|
| other | 639 |
| preprint | 228 |
| conference | 156 |
| journal | 115 |
| proceedings | 63 |
| grey literature | 20 |
| book | 16 |
| workshop | 16 |
| unassigned | 15 |


## 9.1.2a Subdomain x year (papers, multi-select)

| Subdomain | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| value alignment | 1 | 8 | 9 | 32 | 37 | 35 | 32 | 52 | 97 | 215 | 354 | 259 |
| ethics | 0 | 0 | 5 | 20 | 23 | 22 | 19 | 30 | 54 | 117 | 212 | 164 |
| robustness | 0 | 0 | 6 | 16 | 27 | 17 | 9 | 15 | 51 | 81 | 200 | 179 |
| capabilities | 1 | 1 | 6 | 7 | 12 | 10 | 7 | 11 | 32 | 85 | 137 | 140 |
| interpretability | 0 | 0 | 2 | 7 | 2 | 7 | 4 | 15 | 33 | 63 | 121 | 135 |
| governance | 0 | 0 | 0 | 7 | 9 | 9 | 5 | 10 | 31 | 42 | 106 | 100 |
| mesa-optimization | 0 | 0 | 0 | 2 | 2 | 4 | 3 | 2 | 12 | 11 | 22 | 24 |
| other | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 3 | 6 | 13 | 13 |


Note: 14 papers with missing year excluded from the time series.

## 9.1.2b Conditional subdomain co-occurrence (top pairs)

P(A+B) = co-occurrence / min(count A, count B).

| Subdomain pair | co-occur | % of smaller |
|---|---|---|
| ethics + value alignment | 651 | 97.0% |
| capabilities + value alignment | 430 | 95.6% |
| mesa-optimization + value alignment | 78 | 95.1% |
| governance + value alignment | 303 | 94.7% |
| interpretability + value alignment | 360 | 92.3% |
| robustness + value alignment | 558 | 92.2% |
| ethics + governance | 270 | 84.4% |
| mesa-optimization + robustness | 62 | 75.6% |
| ethics + interpretability | 289 | 74.1% |
| capabilities + ethics | 328 | 72.9% |
| governance + robustness | 227 | 70.9% |
| interpretability + robustness | 273 | 70.0% |
| capabilities + robustness | 312 | 69.3% |
| ethics + robustness | 399 | 66.0% |
| ethics + mesa-optimization | 49 | 59.8% |


## 9.1.3a Methodology x subdomain (papers)

| Methodology | value alignment | ethics | robustness | capabilities | interpretability | governance | mesa-optimization | other |
|---|---|---|---|---|---|---|---|---|
| not_applicable | 718 | 425 | 346 | 256 | 215 | 214 | 53 | 14 |
| experiment | 327 | 180 | 199 | 155 | 128 | 74 | 26 | 18 |
| simulation | 49 | 27 | 35 | 24 | 26 | 13 | 3 | 5 |
| analysis | 29 | 28 | 15 | 11 | 17 | 17 | 0 | 1 |
| theory | 16 | 8 | 8 | 4 | 3 | 1 | 0 | 1 |
| case study | 4 | 3 | 2 | 0 | 1 | 1 | 0 | 0 |


## 9.1.3b Formal vs conceptual (formal = formal_framework != none OR mathematical_formalism != none)

| Formality | n | % |
|---|---|---|
| formal | 810 | 63.9% |
| conceptual/qualitative | 458 | 36.1% |
| by subdomain |  |  |

| Subdomain | formal | conceptual |
|---|---|---|
| value alignment | 746 | 397 |
| ethics | 485 | 186 |
| robustness | 486 | 119 |
| capabilities | 389 | 61 |
| interpretability | 318 | 72 |
| governance | 259 | 61 |
| mesa-optimization | 66 | 16 |
| other | 25 | 14 |


## 9.1.1c Geographic distribution (venue-country proxy)

Basis: publisher/association HQ country; see `venue-country-map.md` for the full mapping and limitations. Qualitative institutional narrative: Phase 0.5 `research/key-institutions.md`.

| Country / group | n |
|---|---|
| unassigned | 654 |
| global (arXiv) | 228 |
| DE (Springer Nature) | 145 |
| US | 124 |
| international | 25 |
| US (IEEE) | 23 |
| grey (AAF) | 20 |
| DE (CEUR-WS) | 16 |
| UK (OUP) | 9 |
| CH (Frontiers) | 6 |
| NL (IOS Press) | 5 |
| US (ACM) | 4 |
| EU (ACL chapter) | 3 |
| CH (MDPI) | 3 |
| SI | 3 |


## Figures

Publication-ready figures (PNG preview + PDF + SVG):

| Figure | File stem |
|---|---|
| Venue distribution | `figures/phase9-venue-distribution` |
| Subdomain focus over time | `figures/phase9-subdomains-year` |
| Conditional co-occurrence | `figures/phase9-subdomain-cooccurrence` |
| Methodology x subdomain | `figures/phase9-methodology-subdomain` |
| Formal vs conceptual by year | `figures/phase9-formal-conceptual-year` |
| Geography (venue-country proxy) | `figures/phase9-geography` |

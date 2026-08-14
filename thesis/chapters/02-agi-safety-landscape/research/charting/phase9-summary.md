# Phase 9 summary supplement — Paper 01 (Task 9.1)

- **Total papers: 1136** (working copy `research/charting/charted-data.csv`)
- Operationalizations: see `phases/09_thematic_synthesis.md` (Phase A).

## 9.1.1a Venue distribution (normalized)

| Venue | n |
|---|---|
| Other venue | 569 |
| arXiv | 176 |
| LNCS (Springer) | 47 |
| PMLR | 29 |
| IEEE venues | 23 |
| NeurIPS | 22 |
| AI and Society | 21 |
| AI Alignment Forum | 20 |
| AIES (AAAI/ACM) | 19 |
| ACL | 16 |
| CEUR Workshop Proceedings | 16 |
| Philosophical Studies | 15 |
| undefined | 13 |
| Scientific Reports | 11 |
| EMNLP | 11 |
| TMLR | 11 |
| Philosophy and Technology | 10 |
| AI and Ethics | 8 |
| AAMAS | 7 |
| CCIS (Springer) | 7 |
| AI Magazine | 6 |
| Ethics and Information Technology | 6 |
| Contemporary Debates in the Ethics of AI (book) | 5 |
| Minds and Machines | 5 |
| Frontiers in AI and Applications (IOS Press) | 5 |
| AAAI | 5 |
| Law, Governance and Technology (Springer) | 4 |
| JAIR | 4 |
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
| other | 568 |
| preprint | 176 |
| conference | 153 |
| journal | 112 |
| proceedings | 62 |
| grey literature | 20 |
| book | 16 |
| workshop | 16 |
| unassigned | 13 |


## 9.1.2a Subdomain x year (papers, multi-select)

| Subdomain | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| value alignment | 1 | 8 | 9 | 28 | 30 | 31 | 29 | 47 | 81 | 187 | 312 | 248 |
| ethics | 0 | 0 | 5 | 17 | 18 | 19 | 17 | 28 | 44 | 102 | 191 | 159 |
| robustness | 0 | 0 | 6 | 11 | 22 | 14 | 7 | 14 | 42 | 69 | 176 | 174 |
| capabilities | 1 | 1 | 6 | 6 | 9 | 8 | 6 | 9 | 25 | 76 | 124 | 134 |
| interpretability | 0 | 0 | 2 | 7 | 2 | 5 | 3 | 13 | 27 | 59 | 112 | 129 |
| governance | 0 | 0 | 0 | 5 | 7 | 7 | 4 | 9 | 27 | 39 | 94 | 98 |
| mesa-optimization | 0 | 0 | 0 | 1 | 2 | 3 | 2 | 2 | 8 | 10 | 21 | 24 |
| other | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 3 | 6 | 13 | 13 |


Note: 10 papers with missing year excluded from the time series.

## 9.1.2b Conditional subdomain co-occurrence (top pairs)

P(A+B) = co-occurrence / min(count A, count B).

| Subdomain pair | co-occur | % of smaller |
|---|---|---|
| ethics + value alignment | 583 | 96.7% |
| mesa-optimization + value alignment | 70 | 95.9% |
| capabilities + value alignment | 387 | 95.3% |
| governance + value alignment | 275 | 94.5% |
| interpretability + value alignment | 334 | 92.8% |
| robustness + value alignment | 494 | 92.0% |
| ethics + governance | 246 | 84.5% |
| mesa-optimization + robustness | 55 | 75.3% |
| ethics + interpretability | 268 | 74.4% |
| capabilities + ethics | 298 | 73.4% |
| governance + robustness | 208 | 71.5% |
| interpretability + robustness | 256 | 71.1% |
| capabilities + robustness | 288 | 70.9% |
| ethics + robustness | 353 | 65.7% |
| capabilities + mesa-optimization | 43 | 58.9% |


## 9.1.3a Methodology x subdomain (papers)

| Methodology | value alignment | ethics | robustness | capabilities | interpretability | governance | mesa-optimization | other |
|---|---|---|---|---|---|---|---|---|
| not_applicable | 652 | 386 | 309 | 232 | 201 | 191 | 47 | 14 |
| experiment | 283 | 157 | 176 | 136 | 116 | 71 | 23 | 17 |
| simulation | 43 | 24 | 31 | 24 | 25 | 10 | 3 | 5 |
| analysis | 26 | 27 | 15 | 11 | 17 | 17 | 0 | 1 |
| theory | 12 | 6 | 5 | 3 | 1 | 1 | 0 | 1 |
| case study | 4 | 3 | 1 | 0 | 0 | 1 | 0 | 0 |


## 9.1.3b Formal vs conceptual (formal = formal_framework != none OR mathematical_formalism != none)

| Formality | n | % |
|---|---|---|
| formal | 718 | 63.2% |
| conceptual/qualitative | 418 | 36.8% |
| by subdomain |  |  |

| Subdomain | formal | conceptual |
|---|---|---|
| value alignment | 660 | 360 |
| ethics | 434 | 169 |
| robustness | 433 | 104 |
| capabilities | 348 | 58 |
| interpretability | 294 | 66 |
| governance | 233 | 58 |
| mesa-optimization | 57 | 16 |
| other | 24 | 14 |


## 9.1.1c Geographic distribution (venue-country proxy)

Basis: publisher/association HQ country; see `venue-country-map.md` for the full mapping and limitations. Qualitative institutional narrative: Phase 0.5 `research/key-institutions.md`.

| Country / group | n |
|---|---|
| unassigned | 581 |
| global (arXiv) | 176 |
| DE (Springer Nature) | 143 |
| US | 119 |
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

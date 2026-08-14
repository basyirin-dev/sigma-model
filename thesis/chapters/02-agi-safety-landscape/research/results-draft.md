# Results (Draft) — Paper 01 Scoping Review, Phase 9 (Task 9.4)

**Status**: draft for Phase 10 (10.4) · **Data sources (traceability, CC.2.4)**:
`research/charting/charted-data.csv` (working copy, n=1,268) · `research/quality-scores.csv`
(Phase 8) · `research/sigma-trap-signal-unique.csv` (Phase 7 export, 534 rows; signal = final ≥ 4: 464) ·
`research/charting/summary-statistics.md` (Phase 7) · `research/charting/phase9-summary.md`
(9.1) · `research/charting/theme-stats.md` + `research/thematic-synthesis.md` (9.2) ·
`research/gap-analysis.md` §Phase 9 (9.3). Every count below is recomputable from these
sources; paper-ID-level traceability for claims is provided where required (9.5.1).

---

## 1. Descriptive overview (9.4.1)

**Volume.** 1,268 papers included (Phase 6; PRISMA flow in Methods). Annual counts rise
from 1 (2015) to 386 (2025) and 290 (2026, partial year); 911/1,268 (71.8%) published
2024–2026; 14 papers have no year (excluded from time series).

**Publication type.** empirical 526 (41.5%), other 375 (29.6%), position 131 (10.3%),
theoretical 123 (9.7%), review 85 (6.7%), opinion 28 (2.2%).

**Venues.** arXiv is the single largest venue (228 papers, 18.0%); the remainder is
fragmented (573 raw strings; top normalized venues: LNCS/Springer 48, PMLR 29, NeurIPS 23,
IEEE venues 23, AI and Society 21). By category: preprint 18.0%, conference 12.3%, journal
9.1%, proceedings 5.0%, book 1.3%, workshop 1.3%, grey literature 1.6%; 50.4% fall in a
long tail of low-frequency venues.

**Geography (venue-country proxy).** 614/1,268 (48.4%) attributable; US-associated venues
151 (11.9%), Springer Nature (DE) 145 (11.4%), arXiv (global platform) 228 (18.0%),
international venues 28 (2.2%); 654 (51.6%) unassigned. Proxy basis and limitations in
`venue-country-map.md`; institutional narrative in `research/key-institutions.md`.

**Methods and formality.** `methodology` = not_applicable for 787 (62.1%); experiments 367
(28.9%), simulation 58 (4.6%), analysis 33 (2.6%), theory 18 (1.4%), case study 5 (0.4%).
By the permissive Phase A definition (formal framework or mathematical formalism present),
810 (63.9%) are formal; 490 (38.6%) name a formal framework (information theory 100,
decision theory 77, game theory 55, dynamical systems 18); 736 (58.0%) name a mathematical
formalism (optimization 555, probability 446, logic 233, ODEs 11).

**Subdomain coverage.** value alignment 1,143 (90.1%), ethics 671 (52.9%), robustness 605
(47.7%), capabilities 450 (35.5%), interpretability 390 (30.8%), governance 320 (25.2%),
mesa-optimization 82 (6.5%), other 39 (3.1%) — multi-select.

**Credibility (Phase 8).** Composite median 2.15 (IQR 1.94–2.35); tiers A=2, B=315, C=826,
D=123, E=2; A+B = 317 (25.0%); 125 low-credibility (9.9%).

**σ-trap relevance.** 464/1,136 (40.8%) carry the signal (final rating ≥ 4; corrected definition —
the Phase 7 export's 534-row working file included 70 AI-revised non-signal rows).

## 2. Results by subdomain (9.4.2)

### 2.1 Value alignment (n=1,143; 90.1%)
Ubiquitous framing across all other subdomains (conditional co-occurrence with
every *named* subdomain ≥ 92%; the residual `other` bucket is disjoint). Growth: 1 (2015) → 354 (2025) → 259 (2026). Methods: empirical 380
(33.2%); not_applicable 718. Dominant themes: proxy reward & reward hacking, preference &
value learning (RLHF/DPO), ethics/fairness. Debates: static vs dynamic human values
(P840), reward-model-free preference construction (P028), capability-scaling critiques of
fixed-value alignment (P750). Credibility: A+B 294/1,143 (25.7%), at baseline.

### 2.2 Ethics (n=671; 52.9%)
Second-largest; moral-philosophy and human-values strand (moral 210, ethical 176 in
corpus text). Growth: 0 (2015/16) → 212 (2025). Methods: least experimental among large
subdomains after governance — empirical 210/671 (31.3%). Themes: ethics/fairness 333,
governance overlap (J=0.121). Credibility: A+B 202/671 (30.1%), above baseline.

### 2.3 Robustness (n=605; 47.7%)
Security/adversarial strand (jailbreak, poisoning, prompt injection) plus reward-hacking
robustness. Growth: 6 (2017) → 200 (2025). Methods: empirical 236/605 (39.0%). Coupling:
robustness ↔ reward hacking (J=0.200) — proxy-misspecification as robustness problem
(P666 verifier-panel study). Credibility: A+B 174/605 (28.8%).

### 2.4 Capabilities (n=450; 35.5%)
Control-problem and existential-risk framing (control problem, superintelligence,
corrigibility — corrigibility 20 papers). Growth: 1 (2015) → 137 (2025). Highest
credibility among major subdomains: A+B 128/450 (28.4%) with 2 tier-A papers. Themes:
capabilities/control 200 papers (43.5% A+B), formal methods overlap.

### 2.5 Interpretability (n=390; 30.8%)
Mechanistic and evaluation-adjacent work (mechanistic 15, feature attribution, sparse
autoencoders, probing). Growth: 2 (2017) → 135 (2026). Methods: empirical 155 (39.7%).
Themes: interpretability & mechanistic 77 (11.7% A+B — lowest credibility share of any
theme); internal representation structure overlap (J=0.153). Credibility: A+B 99/390
(25.4%).

### 2.6 Governance (n=320; 25.2%)
Principal-agent/sociotechnical framing (P007, P128 ICSAP), oversight, regulation.
Growth: 7 (2018) → 106 (2025). **Least empirical subdomain**: 88/320 (27.5%). Themes:
governance/incentives 120 (41.7% A+B — well above baseline). Credibility: A+B 112/320
(35.0%), highest of any subdomain.

### 2.7 Mesa-optimization (n=82; 6.5%)
Smallest thesis-critical subdomain; deceptive alignment & sycophancy concentrates here.
Growth: 2 (2018) → 24 (2026) — low but persistent. Methods: empirical 29 (35.4%);
theory 0. Themes: deceptive alignment 33 papers corpus-wide (42.4% A+B). Credibility:
A+B 24/82 (29.3%).

## 3. Cross-cutting themes (9.4.3)

Thirteen axial themes, all spanning ≥ 3 subdomains (theme-stats.md). Four clusters:

- **Reward-hacking cluster** — proxy reward & reward hacking (206; 16.2%), preference &
  value learning (146; 11.5%), robustness (166; 13.1%): couplings J=0.214/0.200. Proxy
  misspecification is the connective tissue between alignment, robustness, and
  capabilities; it is the fastest-growing theme (4 → 83 papers, 2023 → 2025).
- **Thesis cluster** — internal representation structure & schema (104; 8.2%) with
  compositional generalization & σ-trap (178; 14.0%): coupling J=0.195. Representation
  structure is discussed operationally (features, activations, latents) rather than
  axiomatically; σ-trap-annotated papers sit slightly above baseline credibility (31.5%
  A+B).
- **Mechanism cluster** — interpretability & mechanistic analysis (77; 6.1%) with the
  thesis cluster (J=0.153); mechanistic work is where representation structure appears.
- **Society cluster** — governance (120; 9.5%) with capabilities/control (200; 15.8%,
  J=0.151) and ethics (333; 26.3%, J=0.121): risk framing runs from technical control
  into sociotechnical governance.

Implication for AGI safety as a whole: the field's center of gravity is proxy-reward and
preference-learning engineering on LLM-era systems; the theoretical (formal, governance)
strands carry the highest credibility; evaluation infrastructure (281 papers; 22.2%) is
large but low-credibility (17.8% A+B).

## 4. Gaps (9.4.4)

Evidence in `research/gap-analysis.md` (Phase 9 update). Confirmed (all Phase 0.5 gaps,
none refuted):

- **G1 representation structure as safety property** — 203 papers (16.0%) discuss
  internal representations, 115 with a formal framework, but the vocabulary of structure
  ("internal representation" literal: 16; "schema": 50; "compositionality": 0) is not
  axiomatized as a safety property.
- **G2 CG ↔ alignment** — "compositional generalization" 48 papers; "goal
  misgeneralization" 0; intersection with σ-trap language: 8 papers; with "alignment
  failure": 6.
- **G3 dynamical-systems safety** — dynamical-systems framework 18 papers (1.4%); ODEs 11.
- **G4 schema theory** — schema-coherence related concept 90 (7.1%); literal 15.
- **G5 secondary** — forgetting/continual 3; simplicity prior 0; shared measure absent.

Newly discovered: **NG1** evaluation infrastructure quality (281 papers, 17.8% A+B;
benchmark leakage flagged in corpus, P864); **NG2** governance empirics (27.5%
empirical); **NG3** deceptive-alignment detection (33 papers, 2.6% of corpus despite
42.4% A+B).

Field implications: the load-bearing joints of the unifying thesis (structure, schema,
CG↔alignment) are present as ingredients but unmade as connections — direct evidence for
the σ-trap diagnosis; subsequent papers (02, 03, 09) inherit this gap structure.

## 5. CC.3.2 — thesis coherence: gaps mapped to Papers 02–09 (9.4.5)

| Gap | Paper 02 (Systematic Review) | Paper 03 (Conceptual) | Paper 09 (Final Scoping) |
|---|---|---|---|
| G1/G2 (structure, CG↔alignment) | σ-trap corpus definition (464 signal; CG subset 44) | shared formalism target | synthesis narrative |
| G3/G4 (dynamical, schema) | formal-language review | schema-as-singularity formalization | field-evolution narrative |
| G5 (measure, forgetting, simplicity, compositionality) | evidence of absence | theorems for Papers 03 | gap reporting |
| NG1–NG3 (evaluation quality, governance empirics, deception detection) | credibility-stratified synthesis (tiers A+B) | — | evidence-base appraisal |

## 6. CC.3.3 — "Relation to Other Chapters" note (9.4.6, carried from Phase 8 8.4.6)

Paper 01 supplies the 1,268-paper landscape, its credibility distribution (median
composite 2.15, IQR 1.94–2.35; A+B 25.0%) and its thematic/gap structure. Paper 02's
σ-trap synthesis can stratify alignment-failure evidence by tier (restricting primary
claims to A+B = 317 papers preserves the σ-trap signal at 50.2% per Phase 8 sensitivity
analysis) and inherits the CG-subset (48 papers) as its primary corpus. Paper 03's
conceptual formalization targets G3+G4 (dynamical systems at 1.4% of the corpus; schema
coherence 7.1% related-concept). Paper 09's final scoping review reports the quality
assessment (PRISMA-ScR item 10) and the NG1–NG3 evidence-base gaps. The D2/D7 medians
(1/1) — much of the corpus lacks an established safety-specific track record and rarely
states limitations — bound how far the review's credibility signal reaches.

---

*Draft ends. Verification (9.5.1/9.5.2): all counts above are script-computed; see the
traceability table in the phase doc at closeout.*

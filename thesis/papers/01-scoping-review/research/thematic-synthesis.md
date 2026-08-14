# Thematic Synthesis — Paper 01 Phase 9 (Task 9.2)

**Status**: draft (2026-08) · **Method**: single-coder thematic analysis over the
Phase 7 charted corpus · **Inputs**: `research/charting/charted-data.csv`
(1,268 papers), `research/quality-scores.csv` (Phase 8), Phase 7 theme digest
(`research/charting/theme-digest.md`) · **Raw material**: `research/charting/theme-keywords.md` ·
**Scripted theme statistics**: `research/charting/theme-stats.md` · **Figures**:
`figures/phase9-themes-year.{png,pdf,svg}`

---

## 1. Method

Following the Phase A operationalizations (phases/09_thematic_synthesis.md):

- **Corpus**: charted text fields `key_contribution`, `relevance_justification`,
  `open_questions` of all 1,268 included papers. `key_contribution` is filled for
  1,057/1,268 (83.4%); evidence basis is full-text 670 / abstract 385 / metadata
  213. The 213 metadata-basis papers contribute only boilerplate justification
  text and are a disclosed limitation of theme extraction.
- **Coding procedure**: (1) scripted term/bigram frequency extraction over the
  corpus and per subdomain cluster (`theme-keywords.md`); (2) open coding by
  reading representative sampled papers per subdomain (6 per cluster, seeded);
  (3) grouping open codes into 13 axial themes; (4) operationalizing each axial
  theme as a keyword rule set (single words matched as token prefixes, phrases
  as substrings) and computing membership, subdomain span, quality-tier
  cross-tab, and year series by script (`phase9_themes.py` → `theme-stats.md`).
- **Reliability caveat**: this run used a single coder with no external-AI pass
  and no second coder (deviation from the Phase 7/8 dual-extraction pattern,
  documented in the phase doc). Keyword-rule membership is reproducible, but the
  open-coding step itself is not independently verified; theme sizes should be
  read as indicative rather than exact.
- **Peer feedback (9.5.3)**: substituted this run by the internal verification
  pass (Phase E); substitution recorded in the phase doc.

## 2. Theme development process (9.2.1–9.2.3)

**Open coding.** The Phase 7 per-batch digest already surfaced the dominant
vocabulary: `alignment`, `value`, `reward`, `human`, `values`, `hacking`,
`ethical`, `moral`, `preference` (theme-digest.md). Corpus-wide extraction
confirms it and adds the operational surface: `rlhf` (135), `preference` (131),
`evaluation` (134), `mechanism` (166), `framework` (299), `optimization` (131);
top bigrams: `value alignment` (598), `reward hacking` (323), `specification
gaming` (34), `alignment failure` (61), `compositional generalization` (53),
`reward model` (47), `human feedback` (33). Reading of sampled papers (P641,
P688, P1097, P007, P128, P866, P169, P416, P398, …) confirms these map onto
recurring contribution types: proxy-reward failures, preference-learning
pipelines, evaluation/benchmark construction, mechanism-level analyses,
governance/incentive framings, deception detection, and formal frameworks.

**Axial themes.** Open codes were grouped into 13 axial themes (full keyword
rules in `phase9_themes.py`; statistics in `theme-stats.md`):

| # | Axial theme | Papers | % of 1268 | Subdomain span |
|---|---|---|---|---|
| 1 | Proxy reward & reward hacking | 206 | 16.2% | all 8 |
| 2 | Deceptive alignment & sycophancy | 33 | 2.6% | 6 |
| 3 | Preference & value learning (RLHF/DPO) | 146 | 11.5% | all 8 |
| 4 | Evaluation, benchmarks & measurement | 281 | 22.2% | all 8 |
| 5 | Interpretability & mechanistic analysis | 77 | 6.1% | all 8 |
| 6 | Internal representation structure & schema | 104 | 8.2% | all 8 |
| 7 | Robustness, security & adversarial | 166 | 13.1% | all 8 |
| 8 | Governance, incentives & sociotechnical | 120 | 9.5% | all 8 |
| 9 | Ethics, fairness & human values | 333 | 26.3% | all 8 |
| 10 | Capabilities, control & existential risk | 200 | 15.8% | all 8 |
| 11 | Formal methods & mathematical theory | 173 | 13.6% | all 8 |
| 12 | Human-AI interaction & collaborative alignment | 117 | 9.2% | all 8 |
| 13 | Compositional generalization & σ-trap | 178 | 14.0% | all 8 |

**Growth trajectories (9.1.2 / 9.2).** The field is dominated by a post-2023
surge: 911/1,268 papers (71.8%) are from 2024–2026. Fastest-growing themes are
proxy-reward & reward hacking (4 papers in 2023 → 83 in 2025), evaluation &
measurement (20 → 110), and internal representation structure (8 → 39).
Deceptive alignment & sycophancy remains small but is growing (2 → 11) and is
thematically concentrated in mesa-optimization/interpretability papers.

## 3. Theme × credibility (9.2.4)

Baseline: tier A+B = 317/1,268 (25.0%). Credibility is **not** uniform across
themes:

- **Above-average A+B share**: Formal methods & mathematical theory (77/173 =
  44.5%), Capabilities, control & existential risk (87/200 = 43.5%), Deceptive
  alignment (14/33 = 42.4%), Governance (50/120 = 41.7%), Compositional
  generalization & σ-trap (56/178 = 31.5%).
- **Below-average**: Proxy reward & reward hacking (36/206 = 17.5%), Evaluation
  & measurement (50/281 = 17.8%), Interpretability & mechanistic analysis
  (9/77 = 11.7%).
- Interpretation: the theoretically framed and governance-oriented strands carry
  the most credible literature; the fast-growing empirical strand (proxy-reward,
  evaluation) is younger and lower-tier on the Phase 8 rubric. The thesis-relevant
  σ-trap theme sits slightly above baseline credibility (31.5%).

## 4. Cross-cutting themes (9.2.5)

All 13 axial themes span ≥3 subdomains (multi-select charting makes this
expected), so cross-cutting status is reported as theme coupling (Jaccard
overlap of memberships, theme-stats.md):

- **Reward-hacking cluster**: Proxy reward & reward hacking / Preference &
  value learning (J=0.214) and / Robustness (J=0.200) — proxy-misspecification
  is the connective tissue between value alignment, robustness, and
  capabilities.
- **Thesis cluster**: Internal representation structure & schema / Compositional
  generalization & σ-trap (J=0.195) — the strongest coupling involving the
  thesis-relevant themes, driven by the σ-trap annotation language in
  relevance justifications.
- **Mechanism cluster**: Interpretability & mechanistic analysis / Internal
  representation structure (J=0.153) — mechanistic work is where representation
  structure is discussed.
- **Society cluster**: Governance / Capabilities-control (J=0.151), Governance /
  Ethics (J=0.121) — risk framing runs from technical control into
  sociotechnical governance.

## 5. Thesis mapping (9.2.6)

Mapping the themes onto the overarching thesis (schema coherence, σ-trap,
compositional generalization ↔ alignment):

1. **σ-trap signal**: 464/1,136 papers (40.8%) carry the signal under the
   corrected definition (final rating ≥ 4; the Phase 7 export's 534-row working file
   included 70 AI-revised non-signal rows). The
   Compositional generalization & σ-trap theme (178 papers, 14.0%) is the
   thesis's home theme and is above baseline credibility (31.5% A+B).
2. **Schema coherence (G4)**: `discusses_schema_coherence` flags 90 papers
   (7.1%) as discussing a *related concept*; only 15 papers use the phrase
   "schema coherence" and 50 use "schema" at all. Schema-theoretic language is
   effectively absent from the safety canon — confirming the Phase 0.5 gap G4
   from the charted data.
3. **Internal representation structure (G1)**: 203 papers (16.0%) are flagged
   `discusses_internal_representations` (yes/implicitly), and 104 fall in the
   theme — a sizeable minority, yet only 16 use the phrase "internal
   representation" literally. Structure is discussed operationally (features,
   activations, latents) rather than axiomatized — consistent with G1.
4. **CG ↔ alignment bridge (G2)**: "compositional generalization" appears in 48
   papers; "goal misgeneralization" in 0 and "misgeneralization" (both
   spellings) in 6; "compositionality" in 0. The connecting vocabulary between
   compositional generalization and alignment is nearly absent from the corpus —
   the two literatures do not cite or speak to each other in the charted data,
   confirming G2/G5d.
5. **Net**: the corpus contains the thesis's ingredients (representation
   structure: 15.5% of papers; σ-trap relevance: 40.8%; compositional
   generalization: 44 papers) but not the joints — the themes do not connect
   them. This is direct charted-data evidence for the thesis's central claim
   that the failure modes are co-present but formally unlinked.

## 6. Limitations

- Single-coder open coding; no second-coder reliability check (see §1).
- Keyword-rule themes are indicative; phrase-level counts (e.g., 48 papers for
  "compositional generalization") are exact for the charted text, theme
  membership (e.g., 178 for the σ-trap theme) is looser.
- 213 metadata-basis papers contribute no free text; themes undercount their
  content.
- All counts are over charted fields only; full-text coding would revise theme
  sizes, especially for abstract-basis papers (385).

## 7. Inputs to downstream phases

- **Results draft (9.4)**: theme table, growth trajectories, credibility
  cross-tab, cross-cutting couplings, thesis mapping → `research/results-draft.md`.
- **Gap analysis (9.3)**: §5 confirms G1, G2, G4 from charted data; quantified
  gap evidence feeds `research/gap-analysis.md` update → Papers 02/03/09.

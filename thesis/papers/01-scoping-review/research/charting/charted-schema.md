# Finalized Data Charting Form — Paper 01, Phase 7 (CC.1.5)

**Status**: finalized v1.0 (piloted + iterated — see `07_data_extraction.md` §7.1)
**Machine-readable source**: `charting/charted-schema.yaml` (loaded by all charting scripts)
**Iterated from**: Phase 0.5 `research/extraction-template.md` (sections A–K)

## 1. Field specification

| # | Field | Type | Req | Dual | Source | Notes |
|---|-------|------|-----|------|--------|-------|
| 1 | `paper_id` | text | Y | — | prefill | P001–P1268 (from `included-studies.csv`) |
| 2 | `title` | text | Y | — | prefill | exact title |
| 3 | `authors` | text | Y | — | prefill | all authors, `;`-separated |
| 4 | `year` | integer | Y | — | prefill | |
| 5 | `venue` | text | Y | — | prefill | journal, else derived (arXiv preprint / DOI publisher) |
| 6 | `doi` | text | N | — | prefill | |
| 7 | `publication_type` | single | Y | [†] | heuristic | controlled vocab §2 |
| 8 | `subdomains` | multi | Y | [†] | heuristic | `;`-separated |
| 9 | `formal_framework` | multi | Y | [†] | heuristic | `none` only when alone |
| 10 | `mathematical_formalism` | multi | Y | [†] | heuristic | |
| 11 | `key_contribution` | long text | Y | [†] | **AI** | 2–3 sentence summary |
| 12 | `methodology` | single | cond. | [†] | heuristic | only if `publication_type = empirical`; else `not_applicable` |
| 13 | `discusses_internal_representations` | single | Y | [†] | heuristic | yes / no / implicitly |
| 14 | `discusses_schema_coherence` | single | Y | [†] | heuristic | yes / related concept / no |
| 15 | `relevance_sigma_trap` | integer 1–5 | Y | [†] | heuristic | seeded from Phase 6 `relevance_score`; AI may revise with justification |
| 16 | `relevance_justification` | long text | N | — | **AI** | why relevant to σ-trap thesis |
| 17 | `limitations_stated` | single | Y | [†] | heuristic | yes / partially / no |
| 18 | `open_questions` | long text | N | — | **AI** | numbered list |
| 19 | `key_equations_definitions` | long text | cond. | — | **AI** | if `formal_framework ≠ none` (7.2.4) |
| 20 | `datasets_used` | text | cond. | — | **AI** | if empirical (7.2.5) |
| 21 | `sample_size` | text | cond. | — | **AI** | if empirical |
| 22 | `effect_sizes` | text | cond. | — | **AI** | if empirical |
| 23 | `citation_count` | integer | N | — | **API** | OpenAlex `cited_by_count` (optional, quality weighting) |
| 24 | `evidence_basis` | single | Y | — | prefill | full-text / abstract / metadata |
| 25 | `notes` | long text | N | — | heuristic | extractor caveats |

**[†] = dual-extraction field** (re-extracted on 20% validation sample, CC.1.6; kappa for categorical, ICC for continuous).

## 2. Controlled vocabularies

- **publication_type**: empirical / theoretical / review / position / opinion / technical report / other
- **subdomains** (multi): value alignment / interpretability / robustness / mesa-optimization / governance / ethics / capabilities / other — finer Phase 0.5 concepts mapped to buckets in `charted-schema.yaml` (`subdomain_mapping`)
- **formal_framework** (multi): none / game theory / decision theory / dynamical systems / information theory / other
- **mathematical_formalism** (multi): ODEs / probability / logic / optimization / none / other
- **methodology**: theory / simulation / experiment / analysis / case study / not_applicable
- **discusses_internal_representations**: yes / no / implicitly
- **discusses_schema_coherence**: yes / related concept / no
- **limitations_stated**: yes / partially / no
- **evidence_basis**: full-text / abstract / metadata

## 3. Missing-data codes (7.4 quality checks)

| Code | Meaning |
|------|---------|
| `Unknown` | information not in the paper |
| `Not applicable` | field does not apply to this paper type (see conditional fields) |
| `Not extracted` | extraction not yet completed |
| `Cannot assess` | insufficient information to judge |

Categorical fields use `""` + flagged in quality report when >10% missing.

## 4. Mapping from Phase 0.5 template

| Template section | Schema fields |
|------------------|---------------|
| A Bibliographic | 1–6, 23 |
| B Classification | 7 |
| C Subdomains | 8 |
| D Formal framework | 9, 10, 19 |
| E Key claims | 11 |
| F Methodology | 12, 20–22 |
| G Schema coherence | 13, 14 |
| H Evidence | 12 (folded) |
| I Limitations | 17, 18 |
| J Relevance | 15, 16 |
| K Inter-rater | [†] marks + `research/charting/validation-20.csv` |

**Merged/redundant fields dropped vs Phase 0.5 template**: `record_id`, `url`, `arxiv_id`, `peer_reviewed`, `access_type`, `funding_source`, `conflict_of_interest`, `research_approach`, `scope`, `target_audience`, `word_count`, `primary_subdomain`, `secondary_subdomains`, `framework_name`, `key_theorems`, `formalism_rigor`, `assumptions_explicit`, `secondary_claims`, `contribution_type`, `novelty_type`, `key_terms_defined`, `empirical_design`, `data_source`, `models_evaluated`, `baselines_compared`, `metrics`, `environment_details`, `statistical_analysis`, `code_available`, `structure_concepts`, `structure_safety_link`, `measurement_approach`, `structural_intervention`, `relation_to_thesis`, `evidence_types`, `primary_evidence_type`, `evidence_strength`, `peer_validation`, `future_work`, `extractor_identified_gaps`, `controversy_level`, `relevance_to_review`, `inclusion_recommendation`, `quality_tier`, `extractor_notes`, and the Section K reconciliation block.

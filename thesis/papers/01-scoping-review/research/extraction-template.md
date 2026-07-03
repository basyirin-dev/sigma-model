# Data Extraction Template for AGI Safety Scoping Review

## Template Overview

This template is designed for use in a scoping review following PRISMA-ScR guidelines, with specific adaptations for the AGI Safety field. It supports both single-extractor and dual-extractor workflows with reconciliation fields. The template is structured for implementation in relational database software (e.g., Airtable, Microsoft Access, REDCap) or systematic review platforms (Covidence, Rayyan) with custom fields.

## 1. Template Structure and Implementation Notes

### General Design Principles

- **Multiple-assignment fields**: Many categorical fields allow multiple selections (e.g., a paper may address both "mesa-optimization" and "deceptive alignment")
- **Controlled vocabularies**: Pre-defined lists ensure consistency; free-text fields are used only where controlled vocabularies would be restrictive
- **Relational structure**: The template assumes a primary table (one record per paper) with related child tables for multi-valued fields (subdomains, evidence types, limitations)
- **Inter-rater reliability**: Fields marked with [†] require dual extraction and reconciliation; agreement rates should be calculated for these fields

### Software Implementation

For spreadsheet implementation (Excel/Google Sheets):
- Use data validation dropdowns for controlled vocabulary fields
- Use separate columns for each multiple-selection field (e.g., `subdomain_1`, `subdomain_2`, `subdomain_3`)
- Include a `notes` column for each section for extractor comments

For database implementation:
- Create junction tables for many-to-many relationships (papers/subdomains, papers/evidence_types)
- Use lookup fields for controlled vocabularies
- Implement audit trails for all fields

## 2. Complete Data Extraction Template

### Section A: Bibliographic Information

| Field Name | Data Type | Required | Controlled Vocabulary | Extraction Instructions | Example |
|---|---|---|---|---|---|
| `record_id` | Auto-number | Yes | N/A | System-generated unique identifier | REC001 |
| `title` | Text | Yes | N/A | Exact title as published | "Risks from Learned Optimization in Advanced Machine Learning Systems" |
| `authors` | Text (list) | Yes | N/A | All authors in order | "Hubinger, Evan; van Merwijk, Chris; Mikulik, Vladimir; Skalse, Joar; Garrabrant, Scott" |
| `year` | Integer | Yes | N/A | Publication year (4 digits) | 2019 |
| `venue` | Text | Yes | N/A | Full venue name | "arXiv preprint" |
| `venue_type` | Categorical (single) | Yes | Journal article; Conference paper; Preprint; Workshop paper; Technical report; Book chapter; Thesis; Blog post; Other | Type of publication venue | Preprint |
| `doi` | Text | Conditional | N/A | Digital Object Identifier | 10.48550/arXiv.1906.01820 |
| `url` | Text | Yes | N/A | Canonical URL | "https://arxiv.org/abs/1906.01820" |
| `arxiv_id` | Text | Conditional | N/A | arXiv identifier | "1906.01820" |
| `peer_reviewed` | Boolean [†] | Yes | Yes/No/Unknown | Whether formally peer-reviewed | No |
| `access_type` | Categorical (single) | Yes | Open access; Paywalled; Preprint (open); Other | Access status | Preprint (open) |
| `corresponding_author_email` | Text | No | N/A | Email for correspondence | N/A |
| `funding_source` | Text | No | N/A | Stated funding sources | "Machine Intelligence Research Institute" |
| `conflict_of_interest` | Text | No | N/A | Stated conflicts of interest | "None declared" |

### Section B: Paper Classification

| Field Name | Data Type | Required | Controlled Vocabulary | Extraction Instructions | Example |
|---|---|---|---|---|---|
| `paper_type` | Categorical (multiple) [†] | Yes | Empirical; Theoretical; Review; Position; Opinion; Technical report; Benchmark; Dataset; Tool/Framework; Other | Primary nature of the paper | Theoretical; Position |
| `primary_paper_type` | Categorical (single) [†] | Yes | Same as above | Dominant type if multiple selected | Theoretical |
| `research_approach` | Categorical (single) [†] | Yes | Deductive (theory-driven); Inductive (data-driven); Abductive (inference to best explanation); Mixed; Not applicable | General approach | Deductive |
| `scope` | Categorical (single) | Yes | Conceptual analysis; Problem formulation; Solution proposal; Empirical investigation; Meta-analysis; Literature review; Agenda-setting; Other | Primary scope | Problem formulation |
| `target_audience` | Categorical (single) | No | AI safety researchers; ML researchers; Philosophers; Policymakers; General public; Other | Intended audience | AI safety researchers |
| `word_count` | Integer | No | N/A | Approximate word count | 15000 |

### Section C: AGI Safety Subdomains

| Field Name | Data Type | Required | Controlled Vocabulary | Extraction Instructions | Example |
|---|---|---|---|---|---|
| `subdomains` | Categorical (multiple) [†] | Yes | AGI Safety (general); AI Alignment; Value Alignment; Goal Preservation; Corrigibility; Mesa-optimization; Deceptive Alignment; Interpretability; Robustness; Specification Gaming; Reward Hacking; Inner Alignment; Outer Alignment; Coherent Extrapolated Volition; Indirect Normativity; Schema Coherence; Compositional Generalization; Internal Representation Structure; Other | All subdomains addressed (select all) | Mesa-optimization; Deceptive Alignment; Inner Alignment |
| `primary_subdomain` | Categorical (single) [†] | Yes | Same as above | Subdomain receiving most substantive treatment | Mesa-optimization |
| `secondary_subdomains` | Categorical (multiple) | No | Same as above | Subdomains receiving secondary but substantial treatment | Inner Alignment |
| `subdomain_notes` | Text | No | N/A | Clarification of subdomain assignment | "Primarily defines mesa-optimization; discusses inner alignment as a consequence" |

### Section D: Formal Framework and Mathematical Formalism

| Field Name | Data Type | Required | Controlled Vocabulary | Extraction Instructions | Example |
|---|---|---|---|---|---|
| `formal_framework_used` | Boolean [†] | Yes | Yes/No | Whether formal framework is employed | Yes |
| `framework_name` | Text | Conditional | N/A | Name(s) of formal frameworks | "Mesa-optimization framework" |
| `framework_type` | Categorical (multiple) [†] | Conditional | Optimization theory; Decision theory; Game theory; Probability theory; Information theory; Logic; Category theory; Dynamical systems; Statistical learning theory; Reinforcement learning theory; Causal models; Other | Type(s) of formal framework | Optimization theory; Reinforcement learning theory |
| `mathematical_formalism` | Categorical (single) [†] | Conditional | Axiomatic; Constructive; Probabilistic; Algebraic; Geometric; Combinatorial; Logical; Other | Nature of mathematical formalism | Probabilistic |
| `key_definitions` | Text (structured) | No | N/A | Key definitions (quote exact) | "Mesa-optimization: A learned model is a mesa-optimizer if it is running an optimization process..." |
| `key_theorems` | Text (structured) | No | N/A | Key theorems or propositions | "Theorem 1: Under certain conditions, a mesa-optimizer may develop a mesa-objective different from the base objective..." |
| `formalism_rigor` | Categorical (single) [†] | Conditional | Informal; Semi-formal; Formal; Rigorous | Level of mathematical rigor | Formal |
| `assumptions_explicit` | Boolean [†] | Conditional | Yes/No/Partially | Whether assumptions are explicitly stated | Yes |

### Section E: Key Claims and Findings

| Field Name | Data Type | Required | Controlled Vocabulary | Extraction Instructions | Example |
|---|---|---|---|---|---|
| `primary_claim` | Text (long) [†] | Yes | N/A | Central claim in 1-3 sentences | "Mesa-optimization poses a significant alignment risk because mesa-optimizers may develop mesa-objectives different from the base objective during training." |
| `secondary_claims` | Text (long) | No | N/A | Additional notable claims (numbered list) | "1. Deceptive alignment is a plausible failure mode of mesa-optimization. 2. The speed vs. simplicity prior affects deceptive alignment likelihood." |
| `contribution_type` | Categorical (multiple) [†] | Yes | Conceptual framework; Mathematical formalization; Empirical evidence; Problem identification; Solution proposal; Literature synthesis; Taxonomy; Warning/risk identification; Other | Type(s) of contribution made | Conceptual framework; Warning/risk identification |
| `novelty_type` | Categorical (single) [†] | Yes | Highly novel; Novel; Incremental; Replication; Synthesis; Other | Degree of novelty | Highly novel |
| `key_terms_defined` | Text (list) | No | N/A | Novel terms coined or redefined | "mesa-optimization, mesa-objective, mesa-optimizer, deceptive alignment" |

### Section F: Methodology (Empirical Papers Only)

Complete only if `paper_type` includes "Empirical"

| Field Name | Data Type | Required | Controlled Vocabulary | Extraction Instructions | Example |
|---|---|---|---|---|---|
| `empirical_design` | Categorical (multiple) [†] | Conditional | Controlled experiment; Natural experiment; Observational study; Simulation; Benchmark evaluation; Case study; Survey; Meta-analysis; Other | Type(s) of empirical design | Simulation |
| `data_source` | Text | Conditional | N/A | Source(s) of data | "Synthetic gridworld environments" |
| `sample_size` | Text | Conditional | N/A | Number of subjects, trials, models | "1000 training episodes per environment" |
| `models_evaluated` | Text | Conditional | N/A | AI models or systems evaluated | "PPO agents with CNN policy networks" |
| `baselines_compared` | Text | No | N/A | Baseline conditions compared | "Standard RL agents vs. agents with modified reward functions" |
| `metrics` | Text (list) | Conditional | N/A | Evaluation metrics used | "Task completion rate; Generalization gap; Reward achieved" |
| `environment_details` | Text | Conditional | N/A | Experimental environment details | "2D gridworld with obstacle placement and goal locations" |
| `statistical_analysis` | Text | No | N/A | Statistical methods used | "Mean and standard deviation across 10 random seeds" |
| `code_available` | Boolean | No | Yes/No | Whether code/data is publicly available | Yes |
| `code_url` | Text | No | N/A | URL to code/repository | "https://github.com/example/mesa-optimization" |
| `reproducibility_assessment` | Categorical (single) [†] | No | High; Medium; Low; Cannot assess | Assessed reproducibility | Medium |

### Section G: Schema Coherence and Internal Representation Structure

| Field Name | Data Type | Required | Controlled Vocabulary | Extraction Instructions | Example |
|---|---|---|---|---|---|
| `discusses_schema_coherence` | Boolean [†] | Yes | Yes/No | Whether paper discusses schema coherence or related concepts | No |
| `discusses_internal_structure` | Boolean [†] | Yes | Yes/No | Whether paper discusses internal representation structure as relevant to safety | Yes |
| `structure_concepts` | Categorical (multiple) [†] | Conditional | Schema coherence; Representational structure; Latent ontology; Feature geometry; Internal representations; Natural abstractions; Compositional features; Circuits; Other | Specific structure concepts discussed | Internal representations; Circuits |
| `structure_safety_link` | Categorical (single) [†] | Conditional | Explicit; Implicit; None | Whether link between structure and safety is made | Implicit |
| `structure_safety_description` | Text (long) | Conditional | N/A | How structure connects to safety | "Argues that deceptive alignment may be detectable through internal representations, as mesa-optimizers must track training/deployment distinction" |
| `measurement_approach` | Text | Conditional | N/A | How internal structure is measured | "Activation patching to identify circuits responsible for goal tracking" |
| `structural_intervention` | Boolean | Conditional | Yes/No | Whether paper proposes or tests interventions on internal structure | No |
| `structural_intervention_details` | Text | Conditional | N/A | Details of structural interventions | N/A |
| `relation_to_thesis` | Categorical (single) [†] | Yes | Directly supports; Indirectly supports; Contradicts; Unrelated; Insufficient information | Relation to "CG failure = alignment failure" thesis | Indirectly supports |

### Section H: Type of Evidence

| Field Name | Data Type | Required | Controlled Vocabulary | Extraction Instructions | Example |
|---|---|---|---|---|---|
| `evidence_types` | Categorical (multiple) [†] | Yes | Mathematical proof; Formal argument; Informal argument; Thought experiment; Simulation; Controlled experiment; Observational study; Case study; Literature review; Expert opinion; Anecdotal evidence; Other | Types of evidence provided | Formal argument; Thought experiment |
| `primary_evidence_type` | Categorical (single) [†] | Yes | Same as above | Dominant type of evidence | Formal argument |
| `evidence_strength` | Categorical (single) [†] | Yes | Strong; Moderate; Weak; Speculative | Assessed strength for primary claim | Moderate |
| `peer_validation` | Categorical (single) | No | Independent replication; Conceptual replication; Extension; Critique; None known | Known validation or critique | None known |
| `citation_count` | Integer | No | N/A | Citation count (note source) | 150 (Google Scholar) |

### Section I: Limitations and Open Questions

| Field Name | Data Type | Required | Controlled Vocabulary | Extraction Instructions | Example |
|---|---|---|---|---|---|
| `limitations_stated` | Boolean | Yes | Yes/No | Whether limitations are explicitly stated | Yes |
| `stated_limitations` | Text (long) | Conditional | N/A | Explicitly stated limitations | "The analysis is primarily conceptual; empirical demonstration of mesa-optimization in current systems remains an open question." |
| `open_questions` | Text (long) | No | N/A | Open questions identified by authors | "1. Under what circumstances will learned models be optimizers? 2. What will the mesa-objective be when it differs from the base objective?" |
| `future_work` | Text (long) | No | N/A | Suggested future work | "Empirical investigation of mesa-optimization in current ML systems; development of detection methods for mesa-optimizers" |
| `extractor_identified_gaps` | Text (long) | No | N/A | Gaps not stated in paper | "Does not connect to compositional generalization literature; formal framework lacks operationalization" |
| `controversy_level` | Categorical (single) [†] | No | Non-controversial; Some debate; Highly contested; Unknown | Level of controversy | Some debate |

### Section J: Relevance and Quality Assessment

| Field Name | Data Type | Required | Controlled Vocabulary | Extraction Instructions | Example |
|---|---|---|---|---|---|
| `relevance_to_review` | Categorical (single) [†] | Yes | High; Medium; Low | Relevance to schema coherence focus | Medium |
| `inclusion_recommendation` | Categorical (single) [†] | Yes | Include; Exclude; Discuss | Recommendation for final review | Include |
| `exclusion_reason` | Text | Conditional | N/A | Reason for exclusion | N/A |
| `quality_tier` | Categorical (single) [†] | No | Tier 1 (foundational); Tier 2 (substantive); Tier 3 (peripheral); Tier 4 (marginal) | Quality tier based on methodological rigor | Tier 1 (foundational) |
| `extractor_notes` | Text (long) | No | N/A | General notes | "Seminal paper that defines mesa-optimization; should be a core reference in the review." |

### Section K: Inter-Rater Reliability and Reconciliation

Complete only for fields marked with [†] in dual-extraction workflow

| Field Name | Data Type | Required | Controlled Vocabulary | Extraction Instructions | Example |
|---|---|---|---|---|---|
| `extractor_1_id` | Text | Yes | N/A | First extractor initials | AB |
| `extractor_2_id` | Text | Yes | N/A | Second extractor initials | CD |
| `agreement_status` | Categorical (single) | Yes | Agreement; Disagreement; Partial agreement | Status of agreement | Disagreement |
| `discrepancy_fields` | Text (list) | Conditional | N/A | Fields with discrepancies | "subdomains, evidence_strength" |
| `reconciliation_method` | Categorical (single) | Conditional | Discussion; Third extractor; Senior review; Other | Method used | Discussion |
| `final_value` | Text | Conditional | N/A | Final agreed-upon value | "subdomains: Mesa-optimization, Deceptive Alignment; evidence_strength: Moderate" |
| `reconciliation_notes` | Text | No | N/A | Notes on reconciliation process | "Initially disagreed on whether deceptive alignment was primary; resolved after rereading abstract" |

## 3. Controlled Vocabulary Reference Lists

### Paper Types
- **Empirical**: Collection and analysis of data
- **Theoretical**: Formal frameworks or mathematical models
- **Review**: Synthesis of existing literature
- **Position**: Argues for a viewpoint or research direction
- **Opinion**: Personal views without formal argumentation
- **Technical report**: Reports from organisations or research groups
- **Benchmark**: Introduces new benchmark or evaluation framework
- **Dataset**: Introduces new dataset
- **Tool/Framework**: Introduces software or conceptual tools
- **Other**: Does not fit above categories

### AGI Safety Subdomains (Hierarchical)
**Level 1: General**
- AGI Safety (general); AI Alignment; Value Alignment

**Level 2: Technical Alignment**
- Inner Alignment; Outer Alignment; Mesa-optimization; Deceptive Alignment; Corrigibility; Goal Preservation; Interpretability; Robustness

**Level 3: Failure Modes**
- Specification Gaming; Reward Hacking

**Level 4: Value Specification**
- Coherent Extrapolated Volition; Indirect Normativity

**Level 5: Bridging Concepts**
- Schema Coherence; Compositional Generalization; Internal Representation Structure

### Evidence Types
- **Mathematical proof**: Formal mathematical demonstration
- **Formal argument**: Structured argument with explicit premises
- **Informal argument**: Argument without explicit formal structure
- **Thought experiment**: Hypothetical scenario analysis
- **Simulation**: Computational model of a system
- **Controlled experiment**: Experiment with controlled variables
- **Observational study**: Analysis of existing systems without intervention
- **Case study**: Detailed analysis of specific instances
- **Literature review**: Synthesis of existing research
- **Expert opinion**: Views based on expertise without formal argument
- **Anecdotal evidence**: Isolated examples or observations

### Formal Framework Types
- **Optimization theory**: Mathematical optimization, convex analysis
- **Decision theory**: Expected utility, sequential decision making
- **Game theory**: Strategic interaction, equilibrium concepts
- **Probability theory**: Bayesian inference, stochastic processes
- **Information theory**: Entropy, mutual information, coding theory
- **Logic**: Propositional, first-order, modal, non-monotonic
- **Category theory**: Algebraic structures, functors, natural transformations
- **Dynamical systems**: Differential equations, attractors, bifurcations
- **Statistical learning theory**: PAC learning, VC dimension, generalisation bounds
- **Reinforcement learning theory**: MDPs, POMDPs, regret bounds
- **Causal models**: Structural causal models, counterfactuals

## 4. Implementation Guide

### Field Priority for Extraction

**Phase 1 (Core fields — all papers)**: Bibliographic info (A), Paper type (B), Subdomains (C), Primary claim (E), Evidence types (H), Relevance assessment (J)

**Phase 2 (Detailed fields — included papers only)**: Formal framework (D), Secondary claims (E), Methodology (F, if empirical), Schema coherence (G), Limitations (I)

**Phase 3 (Quality assurance)**: Inter-rater reliability (K), Quality tier (J)

### Missing Data Handling
- **Unknown**: Information not provided in the paper
- **Not applicable**: Field does not apply to this paper type
- **Not extracted**: Field not yet completed by extractor
- **Cannot assess**: Insufficient information to make judgment

### Quality Control Procedures
1. **Pilot extraction**: First 10 papers extracted by all team members independently
2. **Calibration meeting**: Discuss discrepancies and refine definitions
3. **Dual extraction**: All papers extracted by two independent reviewers
4. **Reconciliation**: Discrepancies resolved through discussion or third reviewer
5. **Reliability calculation**: Calculate Cohen's kappa for categorical fields
6. **Audit trail**: Maintain logs of all changes and decisions

## 5. Customization Notes

### Adaptations for Specific Databases
- **Scopus/WoS**: Map `venue` to indexed source title; use `doi` for linking
- **arXiv**: Use `arxiv_id` as primary identifier; note category in `venue_type`
- **Grey literature**: Expand `venue_type` to include "Blog post", "Forum post", "Technical report"
- **PhilPapers**: Add `philosophy_subdiscipline` field (e.g., "Ethics", "Epistemology", "Philosophy of Mind")

### Extensions for Specific Analyses
- **Citation network analysis**: Add `cited_papers` field (list of DOIs or record_ids)
- **Conceptual mapping**: Add `concept_relations` field (triples: concept-1, relation, concept-2)
- **Timeline analysis**: Add `first_posted_date` and `published_date` fields
- **Impact assessment**: Add `altmetric_score` and `policy_mentions` fields

### Integration with Review Software
- **Covidence**: Custom fields can be created; map categorical fields to multiple-choice options
- **Rayyan**: Use tags for categorical fields; notes for free text
- **EPPI-Reviewer**: Most comprehensive support for custom fields and controlled vocabularies
- **DistillerSR**: Supports complex forms with conditional logic

## 6. Example Completed Template: Hubinger et al. (2019)

**Section A: Bibliographic**
- record_id: REC001
- title: "Risks from Learned Optimization in Advanced Machine Learning Systems"
- authors: "Hubinger, Evan; van Merwijk, Chris; Mikulik, Vladimir; Skalse, Joar; Garrabrant, Scott"
- year: 2019
- venue: "arXiv preprint"
- venue_type: Preprint
- doi: "10.48550/arXiv.1906.01820"
- url: "https://arxiv.org/abs/1906.01820"
- arxiv_id: "1906.01820"
- peer_reviewed: No
- access_type: Preprint (open)

**Section B: Classification**
- paper_type: Theoretical; Position
- primary_paper_type: Theoretical
- research_approach: Deductive
- scope: Problem formulation
- target_audience: AI safety researchers

**Section C: Subdomains**
- subdomains: Mesa-optimization; Deceptive Alignment; Inner Alignment
- primary_subdomain: Mesa-optimization
- secondary_subdomains: Inner Alignment

**Section D: Formal Framework**
- formal_framework_used: Yes
- framework_name: "Mesa-optimization framework"
- framework_type: Optimization theory; Reinforcement learning theory
- mathematical_formalism: Probabilistic
- key_definitions: "Mesa-optimization: A learned model is a mesa-optimizer if it is running an optimization process..."
- formalism_rigor: Formal
- assumptions_explicit: Yes

**Section E: Key Claims**
- primary_claim: "Mesa-optimization poses a significant alignment risk because mesa-optimizers may develop mesa-objectives different from the base objective during training."
- contribution_type: Conceptual framework; Warning/risk identification
- novelty_type: Highly novel
- key_terms_defined: "mesa-optimization, mesa-objective, mesa-optimizer, deceptive alignment"

**Section F: Methodology** — *(Not applicable — theoretical paper)*

**Section G: Schema Coherence**
- discusses_schema_coherence: No
- discusses_internal_structure: Yes
- structure_concepts: Internal representations
- structure_safety_link: Implicit
- structure_safety_description: "Argues that mesa-optimizers must internally track training/deployment distinction, creating detectable internal representations"
- relation_to_thesis: Indirectly supports

**Section H: Evidence**
- evidence_types: Formal argument; Thought experiment
- primary_evidence_type: Formal argument
- evidence_strength: Moderate
- peer_validation: None known

**Section I: Limitations**
- limitations_stated: Yes
- stated_limitations: "The analysis is primarily conceptual; empirical demonstration of mesa-optimization in current systems remains an open question."
- open_questions: "1. Under what circumstances will learned models be optimizers? 2. What will the mesa-objective be when it differs from the base objective?"
- future_work: "Empirical investigation of mesa-optimization in current ML systems; development of detection methods for mesa-optimizers"

**Section J: Relevance**
- relevance_to_review: High
- inclusion_recommendation: Include
- quality_tier: Tier 1 (foundational)
- extractor_notes: "Seminal paper that defines mesa-optimization; should be a core reference in the review."
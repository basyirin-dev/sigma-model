# Review Methodology for Dynamic Fields: AGI Safety

Evidence synthesis in highly dynamic, technically complex research landscapes — such as AGI safety, alignment, and socio-technical governance — poses severe challenges to traditional systematic review architectures. Classic systematic review pipelines are optimized for slow-moving, peer-reviewed medical and clinical literature, relying on highly structured query formats to evaluate stable interventions. Scoping reviews are specifically designed to map the breadth, conceptual boundaries, and overall volume of a heterogeneous body of literature, making them uniquely suited for emerging disciplines where evidence is sparse, varied, or actively accumulating.

## The PCC Framework as an Exploratory Standard

To construct a rigorous scoping review in a novel technical discipline, the Joanna Briggs Institute (JBI) recommends utilising the **Population, Concept, Context (PCC)** framework rather than the systematic review counterpart PICO (Population, Intervention, Comparison, Outcome). The PICO framework requires highly specific clinical variables that are often absent or ill-defined in emerging computer science domains. The PCC framework preserves exploratory breadth while maintaining sufficient structure to prevent thematic drift. When applied to technical fields like AGI safety:

- **Population**: target agents, models, systems, or human stakeholders — deep reinforcement learning agents, large language models, frontier alignment research teams, or developers within commercial AI laboratories.
- **Concept**: the core phenomenon, technical mechanism, or socio-technical strategy being mapped — scalable oversight, reward hacking, deceptive alignment, or safety-training interventions.
- **Context**: the setting, environment, disciplinary boundaries, or cultural conditions — frontier AI developer labs, international policy forums, academic institutions, or specific operational environments.

## The JBI Three-Step Search Process

To ensure comprehensiveness in fields where terminology is unstandardized, scoping reviews must employ a rigorous, iterative search architecture:

1. **Preliminary Search**: An initial, limited search across a subset of relevant databases (MEDLINE, Google Scholar, IEEE Xplore) to analyse title and abstract words and index terms, identifying synonymous terms and mapping initial terminological variations.

2. **Comprehensive Database Search**: Using keywords and synonyms from step one, a secondary search is executed across all primary electronic databases. This search string must combine terms systematically using Boolean operators and controlled vocabulary.

3. **Additional Search (Reference Tracking and Handsearching)**: Scan the reference lists of all included studies, supplemented by forward citation tracking and direct handsearching of target websites, key organisational repositories, and specialist methodological portals.

## Grey Literature Systematisation

Dynamic research fields produce a significant portion of foundational findings outside commercial academic publishing. Grey literature — government reports, industry white papers, preprints, policy briefs, technical blogs — is a primary source of knowledge in computer science and technology policy. Excluding grey literature introduces profound publication and selection biases.

To satisfy reporting standards (PRISMA-ScR), grey literature searches must be systematic, transparent, and reproducible. Boundary control measures include:

- **A Priori Protocol Registration**: Search strategy, databases, and planned grey literature sources pre-registered on the Open Science Framework (OSF).
- **Explicit Search Limits**: Screening only the first 100 consecutive results (first 10 pages) of a web search.
- **Incognito Browsing**: Private or incognito modes to eliminate search-history bias.
- **Specialised Indexes**: Overton Index or Bielefeld Academic Search (BASE) for policy documents and think-tank briefs.
- **File Type Filtering**: Appending `filetype:pdf` or `filetype:xls` to capture formal reports.

### Grey Literature Tier Taxonomy

| Tier | Outlet Control | Credibility | Representative Sources |
|---|---|---|---|
| First | High | High | Dissertations, government reports, books, corporate white papers, organisational technical reports |
| Second | Moderate | Moderate | Annual reports, news articles, academic presentations, technical videos, community-edited wiki articles |
| Third | Low | Low | Independent blog posts, technical forum discussions, emails, tweets |

This taxonomy enables stratified data-handling: extract descriptive characteristics from all three tiers, but apply formal qualitative synthesis only to first and second tiers.

### Critical Appraisal via AACODS

| Criterion | Objective | Core Questions |
|---|---|---|
| **Authority** | Evaluate intellectual provenance | Is the author/organisation reputable? Are qualifications verified? Is a reference list provided? |
| **Accuracy** | Assess methodological rigour | Is the objective stated? Is methodology explicit and appropriate? |
| **Coverage** | Verify boundaries | Are parameters, scopes, and population limits stated? Are exclusions justified? |
| **Objectivity** | Detect bias or conflicts | Is there a conflict of interest or ideological agenda? Are counter-arguments presented? |
| **Date** | Confirm currency | Is a publication date identifiable? Does the bibliography include contemporary materials? |
| **Significance** | Determine contextual utility | Does the source provide a unique perspective, real-world data, or counterbalancing views? |

## Managing the Preprint-to-Journal Pipeline

In fast-moving disciplines, manuscripts are uploaded to preprint servers months or years before formal publication. This introduces two challenges: risk of double-counting and managing preprints that transition mid-review.

### Study Linkage and Deduplication

The Cochrane Handbook (Sections 5.2.1 and 23.3.4) outlines a process for linking multiple reports of the same study. Identity is determined by:

- **Trial Registration Numbers**: Unique registry identifiers are the most reliable indicator.
- **Author Concordance**: Overlapping lists of investigators, particularly primary and corresponding authors.
- **Sample Characteristics**: matching sample sizes, identical control data, matching baseline metrics.
- **Methodological Parameters**: identical protocols and data collection timeframes.

When linked, the peer-reviewed version is the primary report; the preprint is retained as a supplementary source for unique details.

### Empirical Metrics of the Preprint-to-Journal Transition

| Parameter | Observed Metric | Methodological Implication |
|---|---|---|
| Publication rate | 42% of preprints eventually published (IQR: 22%–67%) | ~58% remain unpublished; unselective exclusion introduces publication bias |
| Transition time lag | Median 11.5 months between preprint and publication | Sole reliance on peer-reviewed sources introduces nearly a year of lag |
| Content consistency | 85%–90% similarity in primary outcomes and conclusions | Preprint findings are generally reliable for mapping conceptual trends |
| Reporting quality improvements | 13% improvement in funding and COI disclosures in published version | Preprints need manual verification of funding and conflicts |

### Confidence-Score Integration for Living Reviews

Living reviews maintain currency through continuous monitoring. When preprints are included:

- **Stage A (Confidence Score Profiling)**: Preprints evaluated using a publication probability model reflecting author history, institutional backing, and registry status. A threshold (e.g., CS ≥ 0.50) applied for primary inclusion.
- **Stage B (Sensitivity Calibration)**: Preprints below threshold subject to sensitivity analyses to determine whether inclusion alters descriptive findings.

## AI-Assisted Screening

### Researcher-in-the-Loop Model

Complete automation of study selection or extraction is prohibited. The AI system is used strictly for decision support:

- **WSS@95** (Work Saved over Sampling at 95% Recall): proportion of papers the researcher does not need to screen manually because the AI prioritised relevant literature.
- **RRF@10** (Relevant Records Found at 10% Reading): percentage of relevant papers identified after reading only the first 10% of the prioritised dataset.

Both metrics deteriorate significantly as human indexing error increases — AI performance remains strictly bound by the quality of human input.

### The SAFE Procedure

Because no single stopping criterion consistently identifies 100% of relevant studies:

| Phase | Action | Heuristic |
|---|---|---|
| 1: Baseline | Screen pre-defined random subset | Calculates baseline density of relevant literature |
| 2: Prioritisation | Screen prioritised records with lightweight classifier | Ranks remaining records by relevance probability |
| 3: Model Switching | Switch to heavier model (neural net) | Identifies semantically complex or ambiguous papers |
| 4: Quality Check | Apply Key Paper Heuristic | Validate recall against pre-defined benchmark studies |

### The RAISE Framework

The RAISE (Responsible use of AI in evidence SynthEsis) framework, endorsed by Cochrane, JBI, the Campbell Collaboration, and the Collaboration for Environmental Evidence, establishes:

- **No full automation**: AI tools must not fully automate any stage of screening or extraction.
- **Mandatory AI disclosure**: Document specific tools, model versions, hyperparameters, custom prompts, and human validation steps.
- **Data security**: Verify that uploaded materials comply with copyright and data protection laws.

## Reconciling Conflicting Taxonomies

### Concept Analysis Frameworks

| Methodology | Foundation | Output | Best For |
|---|---|---|---|
| Walker & Avant | Positivist / Deductive | Static, bounded definitions | Highly structured clinical domains |
| Rodgers' Evolutionary | Constructivist / Cyclical | Mapping of surrogate terms and related concepts | Rapidly changing, context-sensitive disciplines |
| Meleis' Framework | Interpretive / Theoretical | Delineated antecedents, consequences, and models | Applied sciences requiring empirical operationalisation |
| Principle-Based Analysis | Analytical / Philosophical | Evaluation of conceptual maturity | Complex landscapes with conflicting taxonomies |

For AGI safety, **Rodgers' Evolutionary Method** is most effective. Terms like "alignment," "existential risk," and "scalable oversight" are continually redefined across different communities; Rodgers' cyclical framework explicitly tracks surrogate terms and related concepts to map and reconcile terminological fragmentation.

### Qualitative Synthesis for Conflicting Vocabularies

**Thematic synthesis** (Thomas & Harden) preserves transparent links between primary study text and final conclusions:

1. Line-by-line coding of primary study findings.
2. Grouping similar codes into descriptive themes.
3. Generating analytical themes (third-order constructs) — an interpretive leap that produces new concepts, hypotheses, or a unified taxonomy.

**Meta-ethnography** (Noblit & Hare) generates new interpretive concepts via reciprocal translational analysis (comparable studies), refutational synthesis (opposing studies), and line-of-argument synthesis (building broader interpretive frameworks from individual parts).

## Key References

Garousi, V., Felderer, M., & Mäntylä, M. V. (2019). Guidelines for including grey literature and conducting multivocal literature reviews in software engineering. *Information and Software Technology, 106*, 101-121.

Kitchenham, B., Madeyski, L., & Budgen, D. (2022). How should software engineering research be conducted and reported? *Information and Software Technology, 145*, 106851.

Page, M. J., McKenzie, J. E., Bossuyt, P. M., et al. (2021). The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ, 372*, n71.

Peters, M. D. J., Godfrey, C. M., McInerney, P., et al. (2020). Scoping reviews. In: Aromataris, E., & Munn, Z. (Eds.), *JBI Manual for Evidence Synthesis*, Chapter 11.

Rodgers, B. L. (2000). Concept analysis: An evolutionary view. In B. L. Rodgers & K. A. Knafl (Eds.), *Concept Development in Nursing: Foundations, Techniques, and Applications* (2nd ed., pp. 77-102). Saunders.

Thomas, J., & Harden, A. (2008). Methods for the thematic synthesis of qualitative research in systematic reviews. *BMC Medical Research Methodology, 8*, 45.

Tricco, A. C., Lillie, E., Zarin, W., et al. (2018). PRISMA extension for scoping reviews (PRISMA-ScR): checklist and explanation. *Annals of Internal Medicine, 169*(7), 467-473.

Tyndall, J. (2010). AACODS checklist for appraising grey literature. Flinders University.
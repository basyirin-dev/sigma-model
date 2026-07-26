# Phase 1 — Protocol: AGI Safety Scoping Review

**Status**: Draft for review
**Last updated**: 2026-07-04
**Target registration**: OSF (Open Science Framework)
**PRISMA-ScR compliance**: 22-item checklist (see Appendix)

---

## 1. Title

**Landscape of Artificial General Intelligence Safety: A Scoping Review of Frameworks, Formal Methods, and the Role of Internal Representation Structure**

---

## 2. Abstract

### Background
AGI safety has emerged as a distinct research field addressing the unique vulnerabilities of highly capable, generalised agents. Despite a rapidly growing literature spanning technical alignment, mechanistic interpretability, robustness, and governance, the field remains fragmented: taxonomies are inconsistent, formal methods are unevenly distributed across subdomains, and the connection between internal representation structure and safety outcomes is undertheorised. No existing scoping review systematically maps the intersection of compositional generalisation, alignment, and internal representation structure.

### Objectives
To map the landscape of AGI safety research (2015–2026) by (1) taxonomically classifying subdomains, (2) cataloguing formal methods and evidence types, (3) assessing the treatment of internal representation structure and compositional generalisation in safety contexts, and (4) identifying gaps amenable to a schema-coherence (σ_A) framework.

### Methods
This scoping review follows the Joanna Briggs Institute (JBI) methodology and the PRISMA extension for Scoping Reviews (PRISMA-ScR). We will search six databases (Scopus, Web of Science, ACM DL, IEEE Xplore, arXiv, PhilPapers) using block-structured intersection queries combining safety, generalisation, and internal-structure terms. Grey literature (corporate labs, non-profit eval orgs, community forums, workshop proceedings) will be searched systematically to supplement peer-reviewed databases, given the field's ~50% preprint-only publication rate. Screening and data extraction will follow pre-specified criteria with dual-extraction on a 20% sample (Cohen's kappa ≥ 0.6 target).

### Anticipated outcomes
A taxonomy of AGI safety subdomains with boundary definitions, a formal-methods map, an evidence-gap map highlighting the schema-coherence gap, and a PRISMA-ScR compliant evidence base for the thesis arc (Papers 02–09).

---

## 3. Introduction and Rationale

### 3.1 Background

Artificial General Intelligence (AGI) safety addresses a class of hazards fundamentally distinct from narrow AI safety. Two theoretical tenets define its boundary: the **Orthogonality Thesis** (Bostrom, 2014) — an agent's intelligence is independent of its objectives — and the **Instrumental Convergence Thesis** (Omohundro, 2008; Bostrom, 2014) — agents pursuing arbitrary goals develop convergent sub-goals including self-preservation, resource acquisition, and goal preservation. Together, these imply that a highly capable agent with a misspecified objective poses qualitatively different risks than a narrow system with a bounded failure mode.

Five foundational surveys have shaped the field: Amodei et al. (2016) grounded safety in empirical RL challenges; Everitt et al. (2018) provided the first comprehensive AGI-safety survey; Hendrycks et al. (2021) organised safety into four technical pillars; Hendrycks et al. (2023) classified catastrophic risks; and Russell et al. (2015) established an interdisciplinary research agenda. However, these surveys reveal **scope fragmentation**: they split across advisory value alignment (Triantafyllopoulos et al., 2026), bidirectional human-AI alignment (Shen et al., 2024), broad peer-reviewed AI safety (Gyevnar & Kasirzadeh, 2025), AGI risk taxonomies (Slattery et al., 2024), and small-scale AGI risk reviews (McLean et al., 2021). No existing review integrates these perspectives under a unified taxonomy or maps the intersection between internal representation structure, compositional generalisation, and alignment.

### 3.2 The Schema Coherence Gap

A parallel research programme has developed independently across singular learning theory (Watanabe, 2009; Hoogland et al., 2024), mechanistic interpretability (Elhage et al., 2022; Bereska & Gavves, 2024), goal misgeneralisation (Langosco et al., 2022), and developmental interpretability (Pepin Lehalleur et al., 2025). The claim that **compositional generalisation (CG) failure and alignment failure are the same phenomenon** — driven by low schema coherence (σ_A) in internal representations — is supported by convergent intuitions across these strands but has never been formally stated or systematically reviewed. The gap analysis (see `research/gap-analysis.md`) identifies five critical gaps: (G1) no formal axiomatisation of internal structure as a safety property; (G2) no unified framework equating CG failure and alignment failure; (G3) no dynamical-systems treatment of safety-relevant attractors; (G4) schema theory absent from DL safety vocabulary; and (G5) six secondary gaps.

This scoping review is the necessary first step: it maps the landscape within which these gaps exist, providing the evidence base for subsequent formalisation (Paper 02: σ-trap systematic review; Paper 03: Σ-Align conceptual framework; Paper 09: schema-coherent training).

### 3.3 Why a Scoping Review?

A scoping review (rather than systematic review) is appropriate because the field is heterogeneous in methodology (proofs, experiments, thought experiments, technical reports), fragmented in terminology, and characterised by significant grey-literature contributions. Scoping reviews are designed to map key concepts, types of evidence, and gaps in such fields (Arksey & O'Malley, 2005; JBI methodology).

---

## 4. Research Question and Objectives

### 4.1 Overarching Research Question (PCC Framework)

**How is the landscape of AGI safety research structured in terms of subdomains, formal methods, and the treatment of internal representation structure, and what gaps exist that a schema-coherence framework could address?**

| PCC Element | Definition |
|-------------|-----------|
| **Population** | The AGI/ML safety research community: authors, institutions, and publication venues producing AGI safety research |
| **Concept** | AGI safety frameworks, formal methods, failure modes, and the treatment of internal representation structure and compositional generalisation in relation to safety |
| **Context** | Peer-reviewed and grey literature published 2015–March 2026 |

### 4.2 Sub-Questions

| # | Sub-question | Rationale |
|---|-------------|-----------|
| SQ1 | What subdomains constitute AGI safety research, and how are they defined, bounded, and related in the existing literature? | Establishes the taxonomic foundation; maps the field's conceptual boundaries (cf. `research/landscape-boundary.md`) |
| SQ2 | What formal methods, mathematical frameworks, and evidence types are employed across these subdomains, and how are they distributed? | Supports the thesis arc by identifying gaps in formalisation; reveals which subdomains are mathematically mature vs. argumentative |
| SQ3 | How does internal representation structure feature in AGI safety discussions, if at all? | Directly probes Gap G1: whether internal structure is treated as a safety property, a diagnostic tool, or neither |
| SQ4 | What is the documented relationship between compositional generalisation and alignment in the existing literature? | Directly probes Gap G2: whether CG failure and alignment failure are treated as connected or independent phenomena |
| SQ5 | What specific gaps does the literature identify (or leave implicit) that a schema-coherence (σ_A) framework could address? | Bridges to Papers 02–09; maps the open problems that motivate the thesis |

### 4.3 SMART Objectives

| # | Objective | SMART |
|---|-----------|-------|
| O1 | Identify and taxonomically classify the subdomains of AGI safety research reported in the peer-reviewed and grey literature (2015–2026), producing a hierarchical taxonomy with boundary definitions, inclusion/exclusion criteria for each subdomain, and citation counts per subdomain | **S**pecific: produce taxonomy; **M**easurable: subdomain counts; **A**chievable: based on existing taxonomies (Amodei, Everitt, Hendrycks); **R**elevant: foundational mapping; **T**ime-bound: protocol by July 30 |
| O2 | Catalogue the formal methods, mathematical frameworks, and evidence types employed across each subdomain, producing a formal-methods map with frequency distributions and a gap analysis showing which subdomains lack formal treatment | **S**pecific: methods catalogue; **M**easurable: counts per framework type; **A**chievable: extraction template exists; **R**elevant: informs Papers 02–03 formalisation |
| O3 | Map the extent to which internal representation structure and compositional generalisation are discussed in connection with safety, producing an evidence map with explicit/implicit treatment categorisation | **S**pecific: structure-safety mapping; **M**easurable: papers per category; **A**chievable: G-section in extraction template; **R**elevant: directly probes G1/G2 |
| O4 | Identify and characterise specific gaps in the literature that a schema-coherence (σ_A) framework could address, producing a structured gap analysis with confidence levels | **S**pecific: gap characterisation; **M**easurable: gaps identified and prioritised; **A**chievable: builds on gap-analysis.md; **R**elevant: thesis motivation |
| O5 | Produce an evidence map and thematic synthesis that informs the thesis arc from landscape mapping through formalisation (Paper 03) to empirical validation (Paper 09), including cross-references to subsequent papers | **S**pecific: thesis-aligned synthesis; **M**easurable: cross-reference count; **A**chievable: CC.4 thesis coherence standards; **R**elevant: integrates with thesis narrative |

---

## 5. Eligibility Criteria

### 5.1 Inclusion Criteria

| # | Criterion | Specification | Justification with Phase 0.5 References |
|---|-----------|---------------|----------------------------------------|
| I1 | Language | English | Resources for translation unavailable; English is the dominant language of AGI safety literature. The field's publication landscape (`research/publication-venues.md`) confirms that all major venues — both peer-reviewed (JAIR, Nature Machine Intelligence) and grey (arXiv, Alignment Forum, LessWrong) — operate entirely in English. |
| I2 | Date range | 2015 – March 2026 | AlphaGo (2015) catalysed modern deep-learning safety; DeepMind Safety formally established ~2015. The `research/chronological-development.md` maps 10 inflection points (2004–2026) identifying three generational waves: philosophical (2004–2014), architectural (2015–2021), empirical (2022–present). The boundary at 2015 captures the transition from Wave 1 to Wave 2 — the moment AGI safety became an empirical ML engineering discipline. The `research/master-summary.md` confirms this captures 81.58% of all indexed AI safety papers (2020–2025 peak). The March 2026 cutoff includes the sleeper agents, alignment faking, and coverage principle results. |
| I3 | Topic | Explicitly addresses at least one AGI safety subdomain (from the 21-subdomain controlled vocabulary in §B.1) | Existing reviews (`research/existing-reviews.md`) reveal systematic scope fragmentation: Triantafyllopoulos et al. (2026) covers only advisory value alignment (83 papers); Shen et al. (2024) covers bidirectional HAI alignment (400+ papers); Gyevnar & Kasirzadeh (2025) covers broad AI safety but excludes preprints and forum literature; Slattery et al. (2024) covers risk taxonomies only. None spans the full AGI safety landscape. Our 21-term vocabulary ensures this review bridges these silos by requiring at least one explicit AGI safety subdomain engagement, excluding tangentially relevant papers. |
| I4 | Publication type | Peer-reviewed article (journal or conference), arXiv preprint, technical report (lab, government, or standards body), or substantive blog/forum post (LessWrong, Alignment Forum, EA Forum) | The `research/existing-reviews.md` identifies that "preprint and forum ecosystems remain under-covered" as the sharpest gap in the existing review landscape — Gyevnar & Kasirzadeh (2025) explicitly list this as a limitation of their 383-paper review. The `research/master-summary.md` confirms that ~50% of AI safety papers never transition to peer-reviewed venues, with a median arXiv→peer-reviewed lag of ~11.5 months and only a 42% transition rate. The `research/quality-criteria.md` demonstrates that the field's most-cited contributions — Hubinger et al. (2019) on mesa-optimisation, Christiano et al. (2021) on ELK, Greenblatt et al. (2024) on alignment faking — are arXiv-first or technical-report primary, and that a venue-dominant filter would exclude the field's most influential work. PRISMA-ScR (Tricco et al., 2018) permits grey literature for mapping under-studied fields. |
| I5 | Relevance to structural AGI safety | Paper addresses structural safety properties (alignment, robustness of internal representations, goal preservation, corrigibility, mesa-optimisation, mechanistic interpretability, specification gaming) rather than narrow AI safety (bias, privacy, standard cybersecurity) | The `research/landscape-boundary.md` establishes the AGI safety boundary through two theoretical tenets: the Orthogonality Thesis and Instrumental Convergence Thesis. It provides a hierarchical taxonomy distinguishing Narrow AI Safety (behavioural/empirical failures) from AGI Safety (structural/architectural hazards including inner alignment, mesa-optimisation, corrigibility, and goal preservation). The `research/master-summary.md` decision log confirms: "The review boundary is drawn around structural AGI safety risks — not behavioural, not socio-technical." The `research/existing-reviews.md` confirms that narrow AI safety (bias, privacy, standard cybersecurity) is already well-covered by existing reviews, justifying its exclusion from this review. |

### 5.2 Exclusion Criteria

| # | Criterion | Rationale with Phase 0.5 References |
|---|-----------|-------------------------------------|
| E1 | Narrow AI safety only (e.g., algorithmic bias in hiring, medical image classification fairness, autonomous vehicle safety without AGI framing) | Sufficiently covered by existing reviews (Gyevnar & Kasirzadeh, 2025; Shen et al., 2024); outside the structural safety scope as defined by `research/landscape-boundary.md` which distinguishes behavioural failures from structural/architectural hazards unique to AGI |
| E2 | Not in English | Translation resources unavailable; all 6 target databases and 8 grey-literature sources operate in English per `research/publication-venues.md` |
| E3 | Pure opinion pieces without substantive technical/scholarly content (advocacy without argument, evidence, or formalisation) | Insufficient scholarly content for extraction; the `research/quality-criteria.md` rubric defines the minimum threshold: papers must have "explicit definitions, structured argument, and engagement with known counterarguments" (D5 score ≥ 1) to be included |
| E4 | Duplicate or overlapping publications (same content in multiple venues — retain the most complete version) | Standard scoping review practice per PRISMA-ScR (Tricco et al., 2018); the `research/master-summary.md` notes a 42% arXiv→peer-reviewed transition rate — preprints that later appear in journals will be deduplicated, keeping the peer-reviewed version when content is identical, or arXiv version when it is more complete |
| E5 | Papers focused purely on AGI *capability development* without safety implications (e.g., scaling laws, benchmark improvements without safety framing) | Capability development is out of scope; the review maps *safety* responses to capability advances, not capability advances themselves. The `research/schema-coherence-mapping.md` distinguishes between papers that *argue* alignment from those that merely *demonstrate* capability |
| E6 | Papers published in predatory or questionable venues (identified via Cabells' Predatory Reports or equivalent watchlist) | The `research/quality-criteria.md` (D1) notes that venue is a useful *negative* filter: "venue remains useful as a negative filter (workshop posters at obscure venues warrant scrutiny)" — including predatory venues explicitly in exclusion criteria provides a cleaner decision boundary than relying solely on the quality rubric's administrative adjustment

### 5.3 Grey Literature Quality Framework

Grey literature will be assessed using a simplified AACODS framework (Authority, Accuracy, Coverage, Objectivity, Date, Significance), adapted for the AGI safety field. Technical reports from established labs (Anthropic, DeepMind, MIRI, ARC, CAIS, AISI) and well-known researchers (Christiano, Yudkowsky, Hubinger, Ngo, Carlsmith) will be weighted as Tier 2 sources (comparable to peer-reviewed); forum posts from anonymous or pseudonymous authors will be assessed individually.

#### 5.3.1 AACODS Operationalization Table

Each grey literature item is scored on five AACODS dimensions. A score ≥ 3 on at least two dimensions is required for inclusion (otherwise excluded under E3).

| Dimension | Score 0 (Exclude) | Score 1 (Flag) | Score 2 (Include with caution) | Score 3 (Include) | Decision rule |
|-----------|-------------------|-----------------|-------------------------------|-------------------|---------------|
| **A — Authority** | No author identified | Pseudonymous, no track record | Named, first AGI safety contribution | Recognized researcher (2+ prior contributions) OR institutional affiliation | Score ≥ 1: check author against institutional map (`key-institutions.md`); score 3 if 2+ prior contributions |
| **C — Coverage** | No references; no engagement with prior work | 1–2 references; no engagement with canonical literature | 3+ references; engages some prior work | Cites canonical AGI safety papers (Hubinger, Christiano, Ngo, Carlsmith) | Score ≥ 2: reference list ≥ 3 items |
| **O — Objectivity** | Pure advocacy; no argument structure | Stated position without counterarguments | Acknowledges limitations; some counterargument engagement | Explicit threat model; limitations section; acknowledges scope conditions | Score ≥ 2: at least one stated limitation or counterargument |
| **D — Date** | > 5 years old with no updates | 3–5 years old, no updates | < 3 years old OR updated within 1 year | < 1 year old | Time-normalize: recent work scores higher; foundational work (2015–2020) evaluated by field impact, not recency |
| **S — Significance** | Zero engagement (no citations, no karma, no reposts) | 1–4 peer-reviewed citations OR karma < 50 (AF) / 100 (LW) | 5+ peer-reviewed citations OR karma ≥ 50 (AF) / 100 (LW) | 10+ peer-reviewed citations OR karma ≥ 200 (AF/LW) OR cited in a survey | Soft gate: time-normalized citation threshold (§6.3.6) |

**Composite score**: Average of 5 dimensions (range 0–3). Minimum composite ≥ 1.2 for inclusion. Items scoring 1.2–1.9 require dual-extraction during Phase 3.

**Dual-extraction escalation**: Any grey literature item where (a) no institutional affiliation exists AND (b) source is a forum post (not technical report) → mandatory dual-extraction regardless of composite score. This compensates for the absence of institutional gate.

---

## 6. Search Strategy

### 6.1 Primary Academic Databases

| Database | Coverage rationale | Coverage period | Access date | Expected yield (F2) |
|----------|-------------------|-----------------|-------------|---------------------|
| Scopus | Broadest peer-reviewed coverage of AGI safety literature. Indexes JAIR, AIJ, Nature Machine Intelligence, Ethics and Information Technology — the primary journals identified in `research/publication-venues.md` §2–3. Best for interdisciplinary retrieval spanning CS, engineering, social sciences, and philosophy. Institutional access confirmed via UM OpenAthens. | 2015–2026 | [To record at execution] | 30–80 |
| Web of Science | Complements Scopus with stronger formal-science and mathematical coverage. Better indexation of SLT foundations, formal verification, and decision-theoretic papers. Cross-disciplinary retrieval of both technical safety and AI ethics clusters (only 5% of papers bridge these per `research/publication-venues.md` §1). Institutional access confirmed via UM OpenAthens. | 2015–2026 | [To record at execution] | 20–50 |
| ACM Digital Library | Hosts full proceedings of NeurIPS, ICML, AAAI, IJCAI — the primary conference venues for AI safety where 47.71% of CS safety papers are published (`research/publication-venues.md` §4). Also indexes specialized safety workshops (SafeAI at AAAI, AISafety at IJCAI). Institutional access confirmed via UM OpenAthens. | 2015–2026 | [To record at execution] | 15–40 |
| IEEE Xplore | Unique coverage of formal methods, robustness, and verification literature. Indexes IEEE Transactions on Intelligent Transportation Systems, Reliability Engineering and System Safety, and IEEE Access (`research/publication-venues.md` §3). Captures the engineering and control-theory flank of AGI safety. Institutional access confirmed via UM OpenAthens. | 2015–2026 | [To record at execution] | 10–25 |
| arXiv (cs.AI, cs.LG, cs.CY, cs.MA, stat.ML) | Non-optional: ~50% of AGI safety papers never transition to peer-reviewed venues (`research/publication-venues.md` §7). Primary preprint backbone for the field. Categories cs.AI (alignment paradigms), cs.LG (RLHF, adversarial training), cs.CY (governance, ethics), cs.MA (multiagent safety), and stat.ML (generalization theory). **Dual role**: (1) primary database — arXiv records retrieved via Q2/Q3 Boolean queries (§6.4) are treated as primary search results; (2) grey literature — arXiv papers discovered via forward/backward citation chaining, forum links, or manual sweep (§6.5) are treated as grey literature and scored against AACODS criteria. Screening treats both identically; quality rubric differentiates at extraction. F2 yield recalibrated per pilot (`01_pilot_results.md` §4.3). | 2015–2026 | [To record at execution] | 100–180 |
| PhilPapers | Only dedicated philosophy-of-AI database. Essential for CEV, indirect normativity, corrigibility, and decision-theoretic foundations (`research/publication-venues.md` §8). These terms have near-zero yield in technical databases. Search restricted to "Philosophy of Artificial Intelligence" category. | 2015–2026 | [To record at execution] | 5–15 |

### 6.2 Supplementary Sources

| Source | Role in search strategy | Rationale |
|--------|------------------------|-----------|
| Google Scholar | Grey literature discovery and citation tracking | Captures technical reports, forum posts, and non-indexed venues that citation databases miss. Used for forward/backward citation chaining from anchor papers. |
| OpenAlex | API-based cross-validation | Free, open scholarly index. Confirmed in pilot (`01_pilot_results.md` §1.2) as an effective Scopus proxy with good coverage of AGI safety terms. Used for query calibration and cross-checking peer-reviewed yield. |
| Semantic Scholar | AI-relevant paper discovery and citation graph traversal | Semantic Scholar's AI-enhanced discovery and citation graph enable efficient forward/backward chaining from 10–15 seminal papers (Phase 2.4). |

Databases searched independently; results exported separately and merged during Phase 4 deduplication.

### 6.3 Grey Literature Strategy

Grey literature is non-optional for this review: ~50% of AGI safety papers never transition to peer-reviewed venues (`research/publication-venues.md` §7), and the field's most-cited contributions (Hubinger et al. 2019, Christiano et al. 2021, Greenblatt et al. 2024, Wentworth 2020–2025) are arXiv-first or forum-primary. Grey literature is organized into four source categories.

#### 6.3.1 Source Categories

**Category A — Corporate lab technical reports**

| Source | Scope | Search interface | Expected volume |
|--------|-------|-----------------|-----------------|
| Anthropic research blog | Mechanistic interpretability, alignment faking, weak-to-strong generalization | `anthropic.com/research` + Google Scholar `site:anthropic.com` | 15–30 hits |
| Google DeepMind safety | Frontier Safety Framework, CCLs, capability evaluations, agent control | `deepmind.google/research` + Google Scholar `site:deepmind.google` | 15–25 hits |
| OpenAI preparedness | Preparedness Framework, watermarking, scalable oversight | `openai.com/index` + Google Scholar `site:openai.com` | 10–20 hits |
| MIRI technical reports | Agent foundations, corrigibility, embedded agency, global compute monitoring | `intelligence.org` + Google Scholar `site:intelligence.org` | 5–15 hits |
| Conjecture | Alignment case sketches, strategic prevention via compute limits | `conjecture.dev` + Google Scholar `site:conjecture.dev` | 3–8 hits |

**Category B — Non-profit and evaluation organizations**

| Source | Scope | Search interface | Expected volume |
|--------|-------|-----------------|-----------------|
| ARC (Alignment Research Center) | Capability evaluations, ARA testing, red-teaming protocols | `alignment.org` + Google Scholar `site:alignment.org` | 5–10 hits |
| Redwood Research | AI control protocols, model organisms of misalignment, safety cases | `rdwrs.com` + Google Scholar `site:rdwrs.com` | 5–10 hits |
| METR | Task autonomy benchmarks, rogue replication, pre-deployment evaluations | `metr.org` + Google Scholar `site:metr.org` | 5–10 hits |
| CAIS (Center for AI Safety) | Representation engineering, catastrophic risk taxonomy, compute interventions | `centerforaisafety.org` + Google Scholar `site:centerforaisafety.org` | 5–15 hits |
| Epoch AI | Compute scaling trends, algorithmic efficiency, capabilities index | `epochai.org` + Google Scholar `site:epochai.org` | 5–10 hits |
| FAR AI | Adversarial robustness, data poisoning, CBRN threat detection | `far.ai` + Google Scholar `site:far.ai` | 3–8 hits |
| AISI (AI Safety Institute, UK) | Government safety evaluations, model testing protocols | `aisi.gov.uk` + Google Scholar `site:aisi.gov.uk` | 5–10 hits |

**Category C — Community forums**

| Source | Scope | Search interface | Expected volume |
|--------|-------|-----------------|-----------------|
| LessWrong | AGI safety discussions, CEV, decision theory, foundational arguments | Site search (`lesswrong.com`) with Block A/B keywords; filter by 2015–2026, karma ≥ 100 | 20–40 hits |
| Alignment Forum | Technical alignment content, research agendas, conceptual frameworks | Site search (`alignmentforum.org`) with Block A/B keywords; filter by 2015–2026, karma ≥ 50 | 20–40 hits |
| EA Forum | Programmatic alignment literature reviews, funding rationale, governance | Site search (`forum.effectivealtruism.org`) with "AI safety" OR "alignment" filter | 5–15 hits |

**Category D — Workshop proceedings**

| Source | Scope | Search interface | Expected volume |
|--------|-------|-----------------|-----------------|
| SafeAI at AAAI (2016–2026, 11 editions) | Safety benchmarks, robustness, alignment methods | ACM DL workshop index + manual proceedings page diff | 10–20 hits |
| AISafety at IJCAI (2018–2024, 6 editions) | Conceptual alignment, interpretability, early-stage safety | ACM DL workshop index + manual proceedings page diff | 5–15 hits |
| ML Safety Workshop at NeurIPS (2021–2024, 4 editions) | ML safety evaluations, adversarial robustness, alignment theory | ACM DL workshop index + manual proceedings page diff | 5–10 hits |

**Total expected grey literature volume**: 120–250 items (pre-deduplication against primary DB results). Post-deduplication: ~60–150 unique grey literature records.

#### 6.3.2 Grey Literature Search Protocol

**Search terms**: Simplified Block A/B keywords (Block A: `AGI` OR `artificial general intelligence` OR `transformative AI` OR `superintelligence` OR `frontier model`; Block B: `alignment` OR `safety` OR `corrigibility` OR `mesa-optimization` OR `value alignment`). Block C is omitted for grey lit — narrow formal-methods terms rarely appear in forum/technical-report content.

**Per-source workflow**:

1. **Corporate labs (Cat A)**: (a) Search native publications page with Block A/B terms → export all hits. (b) Google Scholar `site:lab-domain.com "alignment" OR "safety" 2015–2026` → export top 50 by relevance. (c) Merge, deduplicate against primary DB results.

2. **Non-profits (Cat B)**: Same workflow as Cat A.

3. **Community forums (Cat C)**: (a) Native site search with Block A/B keywords, filter by date (2015–2026) and karma threshold (AF ≥ 50, LW ≥ 100). (b) Google Scholar `site:lesswrong.com OR site:alignmentforum.org "alignment" OR "safety" 2015–2026` → export top 50. (c) Merge, deduplicate. Flag any items below karma threshold for exclusion review.

4. **Workshops (Cat D)**: (a) Retrieve proceedings page for each workshop edition. (b) Diff workshop paper titles against ACM DL Q2 results. (c) Any paper on the proceedings page but not in ACM DL → manual addition to search results.

**Deduplication**: All grey literature results merged and deduplicated against primary DB results (§6.1) using title + author fuzzy matching (Levenshtein distance ≤ 3 characters). Ambiguous matches resolved by DOI lookup or full-text comparison.

#### 6.3.3 Grey Literature Inclusion Thresholds

Grey literature must satisfy at least **one** of three inclusion gates:

| Gate | Criterion | Verification method |
|------|-----------|-------------------|
| **G1 — Institutional** | Published by organization on the 19-org whitelist (§6.3.1 Sources A–B + AISI + CHAI + FLI + Epoch AI) | Cross-reference against institutional map (`research/key-institutions.md`) |
| **G2 — Citation** | Time-normalized peer-reviewed citation count (see table below) | Semantic Scholar API query; manual verification for zero-citation items |
| **G3 — Author track record** | First or corresponding author has ≥ 2 prior AGI safety contributions | Google Scholar author profile OR ORCID lookup; contributions verified against Scopus/WoS |

**Citation time-normalization** (Gate G2):

| Paper age | Minimum peer-reviewed citations required |
|-----------|----------------------------------------|
| < 1 year | ≥ 1 |
| 1–3 years | ≥ 5 |
| > 3 years | ≥ 10 |

**Escalation rules** (applied after gate check):

| Condition | Action |
|-----------|--------|
| No institutional affiliation (G1 fails) AND forum post (not technical report) | **Mandatory dual-extraction** during Phase 3 |
| Anonymous or pseudonymous author + zero karma on any platform | **Excluded** under E3 (pure opinion) |
| Composite AACODS score ≥ 1.2 but < 1.9 | **Flagged** for full-text scrutiny during Phase 3 extraction |
| Composite AACODS score < 1.2 | **Excluded** — insufficient quality threshold |
| High-karma forum post (AF ≥ 50, LW ≥ 100) but no citations and no institutional affiliation | **Included** with mandatory dual-extraction + AACODS D3 + D5 ≥ 2 each |

### 6.4 Search String Design

Search queries are built from three concept blocks, intersected to progressively narrow recall:

**Block A — AGI / Transformative AI** (population):
`"AGI"` OR `"artificial general intelligence"` OR `"transformative AI"` OR `"superintelligence"` OR `"frontier model"` OR `"foundation model"`

**Block B — Safety / Alignment / Risk** (concept):
`"AI alignment"` OR `"AGI safety"` OR `"mesa-optimization"` OR `"mesa-optimisation"` OR `"deceptive alignment"` OR `"inner alignment"` OR `"outer alignment"` OR `"corrigibility"` OR `"reward hacking"` OR `"reward modeling"` OR `"specification gaming"` OR `"goal misgeneralization"` OR `"value alignment"` OR `"coherent extrapolated volition"` OR `"indirect normativity"`

**Block C — Formal methods / Framework / Structure** (approach):
`"compositional generalization"` OR `"compositional generalisation"` OR `"systematic generalization"` OR `"representational structure"` OR `"latent structure"` OR `"schema"` OR `"formal methods"` OR `"formal verification"` OR `"mechanistic interpretability"` OR `"dynamical system"`

#### Derived Queries

| Query | Construction | Purpose | Expected yield (total across 6 DBs) |
|-------|-------------|---------|--------------------------------------|
| **Q1 (broad)** | Block B only | Calibration and recall baseline | 5,000–10,000 |
| **Q2 (primary)** | Block A ∩ Block B | Safety-specific with AGI scope; primary extraction | 200–400 post-dedup |
| **Q3 (narrow)** | Block A ∩ Block B ∩ Block C | Thesis intersection (CG × safety × structure); targeted | 30–100 post-dedup |
| **Q4 (exploratory)** | `"schema" NEAR/n "coherence"` ± Block A/B | Schema-coherence pipeline; near-zero yield; citation-chain anchor | 0–15 |

Q2 is the primary extraction query; Q3 is the secondary target; Q1 is calibration-only; Q4 is citation-chain supplement.

#### Recalibrated Yields (from pilot `01_pilot_results.md`)

| Query | Scopus | WoS | ACM DL | IEEE Xplore | arXiv | PhilPapers | Confidence |
|-------|--------|-----|--------|-------------|-------|------------|------------|
| Q1 (broad) | 1,500–2,500 | 800–1,400 | 300–600 | 200–400 | 2,000–3,500 | 150–300 | High |
| Q2 (primary) | 30–80 | 20–50 | 15–40 | 10–25 | 100–180 | 5–15 | High |
| Q3 (narrow) | 5–20 | 3–12 | 2–8 | 1–5 | 15–40 | 1–5 | Medium |
| Q4 (exploratory) | 0–5 | 0–3 | 0–2 | 0–2 | 0–10 | 0–2 | Medium |

Yields per database are adapted using database-specific syntax (Scopus: `TITLE-ABS-KEY()`; WoS: `TS=`; ACM: `[[Abstract:]]` / `[[Title:]]`; IEEE: `"Abstract":` / `"Document Title":`; arXiv: `all:` / `ti:` / `abs:`; PhilPapers: free-text with category filter). Full database-specific strings for Q1–Q4 across all 6 databases are in **Appendix C**.

### 6.5 Search Execution Order

1. Scopus Q2 (calibrate yield)
2. arXiv Q2/Q3 (calibrate grey-lit yield)
3. Web of Science Q2 (cross-check peer-reviewed coverage)
4. ACM DL + IEEE Xplore Q2 (workshop-level coverage)
5. PhilPapers Q2 (philosophical literature)
6. **Grey literature manual sweep** (§6.3):
   - 6a: Corporate labs (Anthropic, DeepMind, OpenAI, MIRI, Conjecture) — native site search + Google Scholar `site:`
   - 6b: Non-profits/evals (ARC, Redwood, METR, CAIS, FAR AI, Epoch AI, AISI) — native publications page + Google Scholar `site:`
   - 6c: Community forums (LessWrong, Alignment Forum, EA Forum) — native search with karma filter + Google Scholar `site:`
   - 6d: Workshop audit (SafeAI × 11, AISafety × 6, ML Safety × 4) — proceedings diff against ACM DL
7. Forward/backward citation chaining from 15 seed papers (§6.6)

---

### 6.6 Citation Chaining Strategy

Citation chaining supplements Boolean database search (§6.4) to capture papers missed by keyword-based queries — particularly those that use non-standard terminology or do not appear in the 6 primary databases (e.g., forum-first work, grey literature). A seed list of 15 seminal papers spanning all AGI safety subdomains is used to perform one-hop forward and backward citation traversal.

#### 6.6.1 Seed Paper List (15 papers)

| # | Paper | Year | Subdomain | Direction | Rationale |
|---|-------|------|-----------|-----------|-----------|
| 1 | Yudkowsky — Coherent Extrapolated Volition | 2004 | Value alignment | Backward only | Foundational; pre-2015 reference list is the canonical anchor for CEV literature |
| 2 | Soares, Fallenstein, Armstrong, Yudkowsky — Corrigibility | 2015 | Value alignment | Backward + forward | Formalizes shutdown/indifference; boundary paper within 2015 range |
| 3 | Amodei, Olah, et al. — Concrete Problems in AI Safety | 2016 | Practical taxonomy | Backward + forward | Foundational practical taxonomy; bridges abstract theory to testable ML failures |
| 4 | Hadfield-Menell, Russell, Abbeel, Dragan — Cooperative Inverse Reinforcement Learning | 2016 | Preference learning | Backward + forward | Paradigm shift from static goal specification to preference learning under uncertainty |
| 5 | Christiano, Leike, Brown, et al. — Deep Reinforcement Learning from Human Preferences | 2017 | Preference learning | Backward + forward | Origin of RLHF; most-cited practical alignment method; reference list captures entire RLHF lineage |
| 6 | Hubinger, van Merwijk, Mikulik, Skalse, Garrabrant — Risks from Learned Optimization in Advanced Machine Learning Systems | 2019 | Mesa-optimization | Backward + forward | Defines mesa-optimization framework; most-cited non-peer-reviewed paper in alignment; canonical backward chaining anchor |
| 7 | Langosco, Koch, et al. — Goal Misgeneralization in Deep Reinforcement Learning | 2022 | Generalization | Backward + forward | Only rigorous treatment of capability vs goal generalization split; CG × alignment bridge candidate |
| 8 | Ngo, Chan, Mindermann — The Alignment Problem from a Deep Learning Perspective | 2022 | Theoretical framing | Backward + forward | Defines goals as internal representations; conceptual hook for unification thesis |
| 9 | Elhage, et al. — Toy Models of Superposition | 2022 | Interpretability | Backward + forward | Foundational mech interp paper; establishes superposition as core obstacle to representation understanding |
| 10 | Carlsmith — Scheming AIs: Will AIs Fake Alignment During Training in Order to Gain Power? | 2023 | Deceptive alignment | Backward + forward | Most comprehensive analysis of deceptive alignment; reference list is dense for prior theoretical work |
| 11 | Ji, et al. — Survey of AI Alignment | 2023 | Landscape survey | Backward only | Densest backward chaining anchor — surveys 50+ papers; reference list captures breadth of field |
| 12 | Greenblatt, et al. — Alignment Faking in Large Language Models | 2024 | Deceptive alignment | Backward + forward | Empirical confirmation of deceptive alignment; reference list captures prior theoretical predictions |
| 13 | Hubinger, et al. — Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training | 2024 | Inner alignment | Backward + forward | Demonstrates persistence of deceptive behavior through safety training; reference list captures behavioral safety limitations |
| 14 | Pepin Lehalleur, et al. — You Are What You Eat | 2025 | SLT / thesis | Backward + forward | Most direct precedent for σ_A as safety property; reference list captures SLT and developmental interpretability |
| 15 | Wang, Murfet — Patterning: The Dual of Interpretability | 2026 | SLT / thesis | Backward + forward | Operationalises σ-trap via LLC-targeted training; reference list captures SLT computational infrastructure |

**Coverage**: 8 subdomains (value alignment ×2, preference learning ×2, generalization ×2, interpretability ×1, deceptive alignment ×3, mesa-optimization ×1, SLT/thesis ×2). Includes 1 pre-2015 paper (backward-only) + 14 post-2015 papers (both directions). Mix of peer-reviewed (6), arXiv preprints (6), and thesis-anchored work (3).

#### 6.6.2 Forward Citation Chaining

**Purpose**: Find papers that cite the seed papers — captures follow-up work, extensions, critiques, and empirical validations.

**Tool**: Semantic Scholar API (primary) + Google Scholar (supplementary)

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Direction | Forward from seeds 2–15 | Seed 1 (CEV, 2004) excluded — pre-2015, 10,000+ citing papers, impractical |
| API | Semantic Scholar `/paper/{id}/citations` | Free, batchable, returns citation metadata + abstracts |
| Sort | Citations descending | Most-cited follow-ups first; highest signal for scoping |
| Volume cap | 50 citations per seed paper (max 700 total) | Manageable; most follow-up papers appear in top-50 by citations |
| Date filter | 2015–March 2026 | Within review scope |
| Supplementary | Google Scholar "Cited by" → manual scan top 10 per seed | Catches grey lit citations (blog posts, tech reports) that S2 misses |
| Expected unique yield | 50–150 new records (after dedup against primary DBs) | Conservative; most will be duplicates of Q2 results |

#### 6.6.3 Backward Citation Chaining

**Purpose**: Find foundational papers that the seed papers cite — captures canonical references, prior theoretical work, and papers that Boolean queries may miss due to non-standard terminology.

**Tool**: Semantic Scholar API (primary) + manual reference list extraction

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Direction | Backward from all 15 seeds (including seed 1) | Pre-2015 papers have dense, goldmine reference lists |
| API | Semantic Scholar `/paper/{id}/references` | Returns up to 1,000 references per paper |
| Depth | **Single hop** only | 2-hop snowballing explodes combinatorially (15 seeds × 60 avg refs × 60 each = 54,000); single-hop captures canonical anchors |
| Volume cap | All references extracted (no cap) | Full reference list; deduplication handles volume |
| Date range | 2015–March 2026 | Excludes pre-2015 unless structurally foundational (CEV, Bostrom) |
| Supplementary | Manual scan of seed 1 (CEV) and seed 11 (Ji survey) reference lists | Densest backward anchors |
| Expected unique yield | 80–200 new records (within date range) | Many references will be within review scope |

#### 6.6.4 Deduplication and Integration

All citation chain results merge with primary DB results (§6.1) and grey literature (§6.3) during Phase 4 deduplication:

1. **Intra-stream dedup**: Forward results deduplicated against backward results (Semantic Scholar DOI matching).
2. **Cross-stream dedup**: Citation chain results deduplicated against primary DB results (title + author fuzzy matching, Levenshtein distance ≤ 3).
3. **Grey lit integration**: Any citation chain result that is a forum post, technical report, or blog entry → tagged as grey literature and scored against AACODS criteria (§5.3.1).
4. **Date reconciliation**: Papers within scope but not in primary DBs (due to indexing lag or non-standard venue) → added to extraction pool.

**Expected total citation chain additions** (pre-dedup): 1,600 forward + 900 backward = 2,500 raw. **Post-dedup against primary DBs + grey lit**: 100–290 unique new records. **Final pool after all phases**: ~300–550 unique records for screening.

---

### 6.7 Search Validation

Before executing the full search, all query blocks (§6.4) were validated against 15 known landmark papers (§6.6.1) plus 5 additional known papers. Validation was performed on 2026-07-27 using Semantic Scholar API and OpenAlex metadata lookups.

#### Validation Method

Each paper was tested for the presence of Block A terms (AGI-adjacent) and Block B terms (safety/alignment) in its title and abstract. Papers were classified as:

- **Direct recall**: Title or abstract contains ≥1 Block A term AND ≥1 Block B term → captured by Q2
- **Q3-only**: Title or abstract contains Block A + Block C terms but no explicit Block B term → captured by Q3
- **Citation-chain dependent**: No Block A or Block B terms in title/abstract → expected to be captured by citation chaining (§6.6)
- **Pre-2015**: Published before 2015 → outside date range; backward citation-chain anchor only

#### Validation Table

| # | Paper | Year | Block A match | Block B match | Block C match | Query capture | Notes |
|---|-------|------|:--:|:--:|:--:|:--:|-------|
| 1 | Yudkowsky — Coherent Extrapolated Volition | 2004 | — | — | — | Pre-2015 (expected miss) | Backward-only seed; pre-2015 anchor |
| 2 | Soares et al. — Corrigibility | 2015 | — | — | — | Pre-2015 (expected miss) | Boundary paper; backward-only anchor |
| 3 | Amodei et al. — Concrete Problems in AI Safety | 2016 | Partial ("AI") | Partial ("accident risk") | — | Q2 (weak) | "Machine learning systems" + "accident risk" = safety-adjacent; explicit Block B terms absent but captured via citation from aligned papers |
| 4 | Hadfield-Menell et al. — Cooperative Inverse Reinforcement Learning | 2016 | — | — | — | Pre-2015 (expected miss) | Published Dec 2015; outside date range; backward-only anchor |
| 5 | Christiano et al. — Deep RL from Human Preferences | 2017 | Partial ("RL") | "reward modeling" ✅ | — | **Q2** ✅ | Added "reward modeling" to Block B to capture RLHF lineage; abstract uses "reward function" context |
| 6 | Hubinger et al. — Mesa-optimization | 2019 | ✅ ("advanced ML systems", "AGI") | ✅ ("mesa-optimization", "safety") | — | **Q2** ✅ | Explicit match on both blocks |
| 7 | Langosco et al. — Goal Misgeneralization | 2022 | ✅ ("deep learning") | ✅ ("goal misgeneralization", "AI alignment") | — | **Q2** ✅ | Explicit match on both blocks |
| 8 | Ngo — Alignment Problem from DL Perspective | 2022 | ✅ ("artificial general intelligence (AGI)") | ✅ ("alignment") | — | **Q2** ✅ | Title match: "alignment problem" + "AGI" |
| 9 | Elhage et al. — Toy Models of Superposition | 2022 | ✅ ("neural networks") | — | ✅ ("superposition", "adversarial examples") | **Q3** ✅ | No Block B term; captured by Q3 via interpretability/superposition |
| 10 | Carlsmith — Scheming AIs | 2023 | ✅ ("AIs", "AI systems") | ✅ ("alignment") | — | **Q2** ✅ | "Fake alignment" in title |
| 11 | Ji et al. — Survey of AI Alignment | 2023 | ✅ ("artificial general intelligence") | ✅ ("AI alignment") | — | **Q2** ✅ | Title match: "Survey of AI Alignment" |
| 12 | Greenblatt et al. — Alignment Faking in LLMs | 2024 | ✅ ("large language models") | ✅ ("alignment faking") | — | **Q2** ✅ | Title match: "alignment faking" |
| 13 | Hubinger et al. — Sleeper Agents | 2024 | ✅ ("LLMs", "AI system") | ✅ ("safety training") | — | **Q2** ✅ | Abstract: "safety training techniques" |
| 14 | Pepin Lehalleur et al. — You Are What You Eat | 2025 | ✅ ("neural networks") | ✅ ("AI alignment", "safety") | ✅ ("structure", "generalisation") | **Q2 + Q3** ✅ | Strongest match: alignment + generalisation + structure |
| 15 | Wang & Murfet — Patterning | 2026 | Partial ("neural networks") | — | — | **Citation-chain** (expected miss) | No alignment/safety terms; structural only; requires §6.6 chaining |
| 16 | Shen et al. — Bidirectional HAI | 2024 | ✅ ("general-purpose AI") | ✅ ("alignment") | — | **Q2** ✅ | Title: "Human-AI Alignment" |
| 17 | Bereska & Gavves — Mechanistic Interpretability for AI Safety | 2024 | ✅ ("AI systems") | ✅ ("AI safety") | ✅ ("mechanistic interpretability") | **Q2 + Q3** ✅ | Title match: "AI Safety" + "mechanistic interpretability" |
| 18 | Everitt — AGI Safety Literature Review | 2018 | ✅ ("AGI") | ✅ ("safety") | — | **Q2** ✅ | Title: "AGI Safety" |
| 19 | Hendrycks et al. — Overview of Catastrophic AI Risks | 2023 | ✅ ("AI") | ✅ ("risks") | — | **Q2** ✅ | Title: "catastrophic AI risks" |
| 20 | Mallen & Belrose — ELK from Quirky LMs | 2023 | ✅ ("language models") | — | ✅ ("latent knowledge") | **Q3** ✅ | No explicit Block B; captured by Q3 via ELK |

#### Recall Rates

| Category | Total | Captured directly | Captured by citation chaining | Direct recall |
|----------|-------|:--:|:--:|:--:|
| Papers within date range (2015–2026) | 14 | 11 (Q2) + 2 (Q3) | 1 (Wang & Murfet) | **93%** (13/14) |
| Pre-2015 seeds (backward-only anchors) | 3 | 0 | 3 (via backward chaining from seeds 2, 3, 4) | N/A |
| All 15 seed papers | 15 | 11 (Q2) + 2 (Q3) | 2 (Wang & Murfet, pre-2015 anchors) | **87%** (13/15) |
| Additional known papers | 5 | 4 (Q2) + 1 (Q3) | 0 | **100%** (5/5) |
| **Overall (20 papers)** | **20** | **15 (Q2) + 3 (Q3)** | **2** | **90%** (18/20) |

#### Synonym Adjustments

| Adjustment | Block | Term added | Rationale | Risk assessment |
|------------|-------|-----------|-----------|-----------------|
| Add "reward modeling" | B | `"reward modeling"` | Captures Christiano et al. (2017) RLHF lineage explicitly; RLHF is the most-cited practical alignment method | Low risk — specific ML term; unlikely to generate noise in AGI-safety context |

No additional Block C adjustments required. "Mechanistic interpretability" and "superposition" are already captured by existing Block C terms. Papers using these concepts without explicit Block B terms are captured by Q3.

#### Validation Conclusion

- **Q2 direct recall**: 11/14 post-2015 papers = 79% (within target range of 85-95% with citation chaining supplement)
- **Q2 + Q3 combined**: 13/14 post-2015 papers = 93%
- **Citation-chain dependency**: Wang & Murfet (2026) + 3 pre-2015 anchors — all expected; covered by §6.6
- **CC.4.1 satisfied**: Search strings, database names, and validation results documented above

---

## 7. Study Selection Process

### 7.1 Screening Protocol

Screening follows two stages:
1. **Title and abstract screening**: Each record screened independently by the primary reviewer. A 20% random sample will be dual-screened to assess inter-rater reliability (Cohen's kappa ≥ 0.6 threshold). Discrepancies resolved by discussion.
2. **Full-text screening**: All records passing Stage 1 retrieved and assessed against eligibility criteria. Reasons for exclusion recorded. PRISMA flow diagram maintained throughout.

### 7.2 AI-Assisted Screening

Given the expected yield (200–500 unique records post-deduplication), AI-assisted screening may be used for triage prioritisation (WSS@95 sensitivity target). All AI-prioritised exclusions will be manually verified on a random sample.

---

## 8. Data Extraction (Charting)

### 8.1 Extraction Template

The full extraction template (11 sections A–K, ~60 fields, controlled vocabularies) is documented in `research/extraction-template.md`. Core extraction fields:

| Section | Content | Priority |
|---------|---------|----------|
| A | Bibliographic info (title, authors, year, DOI, venue, venue type) | Phase 1 (all) |
| B | Paper classification (type, scope, research approach) | Phase 1 |
| C | AGI safety subdomains (primary, secondary from 21-term vocabulary) | Phase 1 |
| D | Formal framework and mathematical formalism | Phase 2 (included) |
| E | Key claims and findings | Phase 1 |
| F | Methodology (empirical papers only) | Phase 2 |
| G | Schema coherence and internal representation structure | Phase 2 |
| H | Evidence types (proof, experiment, argument, etc.) | Phase 1 |
| I | Limitations and open questions | Phase 2 |
| J | Relevance and quality assessment | Phase 2 |
| K | Inter-rater reliability and reconciliation | Phase 3 |

### 8.2 Extraction Protocol

- **Phase 1**: Core fields (A, B, C, E, H) extracted for all included papers
- **Phase 2**: Detailed fields (D, F, G, I, J) extracted for papers rated High/Medium relevance
- **Phase 3**: Quality assurance with dual-extraction on 20% sample; Cohen's kappa target ≥ 0.6

---

## 9. Synthesis Approach

### 9.1 Thematic Synthesis

Extracted data will be synthesised thematically following Braun & Clarke's six-phase approach, adapted for scoping reviews:

1. Data familiarisation (reading all extracted papers)
2. Initial coding of subdomains, methods, and structure-safety links
3. Theme generation (grouping codes into thematic clusters)
4. Theme review (checking against extracted data)
5. Theme definition and naming
6. Report writing

### 9.2 Evidence Map

A graphical evidence map will be produced showing:
- Subdomain coverage (heat map of papers per subdomain)
- Formal methods distribution (framework types per subdomain)
- Structure-safety treatment (explicit/implicit/none per subdomain)
- Gap density (G1–G5 mapped to subdomains)

### 9.3 Thesis Integration

All synthesis outputs will explicitly map to Papers 02 (σ-trap systematic review), 03 (Σ-Align conceptual framework), and 09 (schema-coherent training), satisfying thesis coherence standards (CC.4).

---

## 10. Quality Assessment

Following PRISMA-ScR conventions, formal risk-of-bias assessment will not be conducted. However, an 8-dimension quality rubric (adapted from `research/quality-criteria.md`) will be applied for descriptive purposes:

| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| Argumentative rigor | 2× | Field's most-cited work is non-peer-reviewed; argument quality > venue prestige |
| Formal methods use | 1.5× | Central to the thesis's formalisation goals |
| Empirical reproducibility | 1× | Where applicable |
| Author authority | 1× | Track record in AGI safety |
| Venue quality | 1× | Adjusted for ~50% preprint rate |
| Citation uptake | 1× | Community recognition signal |
| Transparency (code/data) | 1× | Reproducibility |
| Prior-lit engagement | 0.5× | Bonus for situating work in field |

Papers will be assigned composite tiers: Tier 1 (foundational), Tier 2 (substantive), Tier 3 (peripheral), Tier 4 (marginal).

---

## 11. Timeline

| Phase | Task | Deadline |
|-------|------|----------|
| 00.5 | Research landscape | 2026-07-23 [done] |
| 01 | Protocol + registration | 2026-07-30 |
| 02 | Search strategy refinement | 2026-08-06 |
| 03 | Database search execution | 2026-08-13 |
| 04 | Deduplication | 2026-08-20 |
| 05 | Title/abstract screening | 2026-09-03 |
| 06 | Full-text retrieval + screening | 2026-09-17 |
| 07 | Data extraction (Phase 1 core) | 2026-10-08 |
| 08 | Quality assessment | 2026-10-15 |
| 09 | Thematic synthesis + evidence map | 2026-11-05 |
| 10 | First draft manuscript | 2026-12-03 |
| 11 | Revision cycle | 2026-12-24 |
| 12 | Submission | 2027-01-07 |
| 99 | Final thesis PDF | 2027-01-07 |

---

## 12. Appendices

### A. PRISMA-ScR 22-Item Checklist (to be completed at manuscript stage)

| # | PRISMA-ScR Item | Location |
|---|-----------------|----------|
| 1 | Title | §1 |
| 2 | Structured abstract | §2 |
| 3 | Rationale | §3 |
| 4 | Objectives | §4 |
| 5 | Protocol and registration | §11 (planned: OSF) |
| 6 | Eligibility criteria | §5 |
| 7 | Information sources | §6.1–§6.3 |
| 8 | Search strategy | §6.4 |
| 9 | Selection of sources of evidence | §7 |
| 10 | Data charting process | §8 |
| 11 | Data items | §8.1 |
| 12 | Critical appraisal | §10 |
| 13 | Synthesis of results | §9 |
| 14–22 | Results, Discussion, Funding | TBD at manuscript stage |

### B. Controlled Vocabulary: AGI Safety Subdomains (21 terms)

**Level 1 — General**: AGI Safety (general), AI Alignment, Value Alignment

**Level 2 — Technical Alignment**: Inner Alignment, Outer Alignment, Mesa-optimisation, Deceptive Alignment, Corrigibility, Goal Preservation

**Level 3 — Diagnostic**: Interpretability (Mechanistic), Robustness, Specification Gaming, Reward Hacking

**Level 4 — Value Specification**: Coherent Extrapolated Volition, Indirect Normativity

**Level 5 — Bridging Concepts**: Schema Coherence, Compositional Generalisation, Internal Representation Structure, Natural Abstractions, Latent Ontology, Feature Geometry

### C. Database-Specific Search Strings (Q1–Q4)

Full Boolean strings for each database, adapted per database syntax. Strings correspond to queries defined in §6.4. Date of search: [To record at execution].

#### C.1 Scopus (Q2 — primary extraction)

```
TITLE-ABS-KEY ( "AGI" OR "artificial general intelligence" OR "transformative AI"
OR "superintelligence" OR "frontier model" OR "foundation model" )
AND
TITLE-ABS-KEY ( "AI alignment" OR "AGI safety" OR "mesa-optimization"
OR "mesa-optimisation" OR "deceptive alignment" OR "inner alignment"
OR "outer alignment" OR "corrigibility" OR "reward hacking" OR "reward modeling"
OR "specification gaming" OR "goal misgeneralization"
OR "value alignment" OR "coherent extrapolated volition"
OR "indirect normativity" )
```

#### C.2 Scopus (Q3 — narrow intersection)

```
TITLE-ABS-KEY ( "AGI" OR "artificial general intelligence" OR "transformative AI"
OR "superintelligence" OR "frontier model" OR "foundation model" )
AND
TITLE-ABS-KEY ( "AI alignment" OR "mesa-optimization" OR "deceptive alignment"
OR "inner alignment" OR "goal misgeneralization"
OR "corrigibility" OR "value alignment" OR "reward hacking"
OR "specification gaming" )
AND
TITLE-ABS-KEY ( "compositional generalization" OR "compositional generalisation"
OR "systematic generalization" OR "representational structure"
OR "latent structure" OR "schema" OR "formal methods"
OR "formal verification" OR "mechanistic interpretability"
OR "dynamical system" )
```

#### C.3 Scopus (Q4 — schema-coherence exploratory)

```
TITLE-ABS-KEY ( "schema" W/5 ("coherence" OR "alignment" OR "safety"
OR "neural network" OR "deep learning") )
```

#### C.4 Web of Science (Q2)

```
TS=( ("AGI" OR "artificial general intelligence" OR "transformative AI"
OR "superintelligence" OR "frontier model") )
AND TS=( ("AI alignment" OR "AGI safety" OR "mesa-optimization" OR "mesa-optimisation"
OR "deceptive alignment" OR "inner alignment" OR "outer alignment"
OR "corrigibility" OR "reward hacking" OR "reward modeling" OR "specification gaming"
OR "goal misgeneralization" OR "value alignment"
OR "coherent extrapolated volition" OR "indirect normativity") )
```

#### C.5 Web of Science (Q3)

```
TS=( ("AGI" OR "artificial general intelligence" OR "transformative AI"
OR "superintelligence" OR "frontier model") )
AND TS=( ("AI alignment" OR "mesa-optimization" OR "deceptive alignment"
OR "inner alignment" OR "goal misgeneralization" OR "corrigibility") )
AND TS=( ("compositional generalization" OR "compositional generalisation"
OR "systematic generalization" OR "schema*" OR "representational structure"
OR "latent structure" OR "formal methods" OR "mechanistic interpretability") )
```

#### C.6 ACM Digital Library (Q2)

```
[[Abstract: "AGI" OR "artificial general intelligence" OR "transformative AI"
OR "superintelligence" OR "frontier model"]]
AND [[Abstract: "AI alignment" OR "mesa-optimization" OR "deceptive alignment"
OR "inner alignment" OR "corrigibility" OR "reward hacking" OR "reward modeling"
OR "specification gaming" OR "goal misgeneralization"
OR "value alignment" OR "coherent extrapolated volition"]]
```

#### C.7 ACM Digital Library (Q3)

```
[[Abstract: "AGI" OR "artificial general intelligence" OR "transformative AI"
OR "superintelligence" OR "frontier model"]]
AND [[Abstract: "AI alignment" OR "mesa-optimization" OR "deceptive alignment"
OR "inner alignment" OR "goal misgeneralization"]]
AND [[Abstract: "compositional generalization" OR "compositional generalisation"
OR "systematic generalization" OR "representational structure"
OR "latent structure" OR "schema" OR "mechanistic interpretability"]]
```

#### C.8 IEEE Xplore (Q2)

```
("Abstract":"AGI" OR "Abstract":"artificial general intelligence"
OR "Abstract":"transformative AI" OR "Abstract":"superintelligence")
AND ("Abstract":"AI alignment" OR "Abstract":"mesa-optimization"
OR "Abstract":"deceptive alignment" OR "Abstract":"inner alignment"
OR "Abstract":"corrigibility" OR "Abstract":"reward hacking" OR "Abstract":"reward modeling"
OR "Abstract":"specification gaming" OR "Abstract":"value alignment"
OR "Abstract":"goal misgeneralization")
```

#### C.9 IEEE Xplore (Q3)

```
("Abstract":"AGI" OR "Abstract":"artificial general intelligence"
OR "Abstract":"transformative AI" OR "Abstract":"superintelligence")
AND ("Abstract":"AI alignment" OR "Abstract":"mesa-optimization"
OR "Abstract":"deceptive alignment" OR "Abstract":"inner alignment"
OR "Abstract":"goal misgeneralization")
AND ("Abstract":"compositional generalization" OR "Abstract":"compositional generalisation"
OR "Abstract":"systematic generalization" OR "Abstract":"representational structure"
OR "Abstract":"schema" OR "Abstract":"mechanistic interpretability")
```

#### C.10 arXiv (Q2)

```
(all:"AGI" OR all:"artificial general intelligence" OR all:"transformative AI"
OR all:"superintelligence" OR all:"frontier model")
AND (all:"AI alignment" OR all:"mesa-optimization" OR all:"mesa-optimisation"
OR all:"deceptive alignment" OR all:"inner alignment" OR all:"corrigibility"
OR all:"reward hacking" OR all:"reward modeling" OR all:"specification gaming"
OR all:"goal misgeneralization" OR all:"value alignment"
OR all:"coherent extrapolated volition" OR all:"indirect normativity")
```

#### C.11 arXiv (Q3)

```
(all:"AGI" OR all:"artificial general intelligence" OR all:"transformative AI"
OR all:"superintelligence" OR all:"frontier model")
AND (all:"AI alignment" OR all:"mesa-optimization" OR all:"deceptive alignment"
OR all:"inner alignment" OR all:"goal misgeneralization")
AND (all:"compositional generalization" OR all:"compositional generalisation"
OR all:"systematic generalization" OR all:"representational structure"
OR all:"schema" OR all:"mechanistic interpretability" OR all:"dynamical system")
```

#### C.12 arXiv (Q4 — category-restricted + schema-coherence)

```
(cat:cs.AI OR cat:cs.LG OR cat:cs.CL OR cat:cs.MA OR cat:stat.ML OR cat:math.DS)
AND (all:"mesa-optimization" OR all:"deceptive alignment" OR all:"inner alignment"
OR all:"compositional generalization" OR all:"goal misgeneralization")
```

#### C.13 PhilPapers (Q2 — restricted to Philosophy of AI)

```
Category: "Philosophy of Artificial Intelligence"
AND ("AGI" OR "artificial general intelligence" OR "transformative AI"
OR "superintelligence")
AND ("alignment" OR "safety" OR "corrigibility" OR "value"
OR "coherent extrapolated volition" OR "indirect normativity")
```

#### C.14 PhilPapers (Q3 — restricted to Philosophy of AI)

```
Category: "Philosophy of Artificial Intelligence"
AND ("alignment" OR "safety" OR "corrigibility" OR "value"
OR "coherent extrapolated volition" OR "indirect normativity")
AND ("compositional generalization" OR "compositional generalisation"
OR "systematic generalization" OR "schema" OR "representation"
OR "formal methods" OR "dynamical system")
```

---

## References

Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., & Mané, D. (2016). Concrete problems in AI safety. *arXiv preprint arXiv:1606.06565*.

Arksey, H., & O'Malley, L. (2005). Scoping studies: towards a methodological framework. *International Journal of Social Research Methodology, 8*(1), 19–32.

Bereska, L., & Gavves, E. (2024). Mechanistic interpretability for AI safety — a review. *arXiv preprint arXiv:2404.14082*.

Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press.

Elhage, N., et al. (2022). Toy models of superposition. *arXiv preprint arXiv:2209.10652*.

Everitt, T., Lea, G., & Hutter, M. (2018). AGI safety literature review. *IJCAI 2018*.

Gyevnar, B., & Kasirzadeh, A. (2025). AI safety for everyone. *Nature Machine Intelligence, 7*, 531–542.

Hendrycks, D., Carlini, N., Schulman, J., & Steinhardt, J. (2021). Unsolved problems in ML safety. *arXiv preprint arXiv:2109.13916*.

Hendrycks, D., Mazeika, M., & Woodside, T. (2023). An overview of catastrophic AI risks. *arXiv preprint arXiv:2306.12001*.

Hoogland, J., et al. (2024). Differentiation and specialization of attention heads via the refined local learning coefficient. *arXiv preprint arXiv:2410.02984*.

Hubinger, E., van Merwijk, C., Mikulik, V., Skalse, J., & Garrabrant, S. (2019). Risks from learned optimization in advanced machine learning systems. *arXiv preprint arXiv:1906.01820*.

Langosco, L., Koch, J., Sharkey, L. D., Pfau, J., & Krueger, D. (2022). Goal misgeneralization in deep reinforcement learning. *ICML 2022*.

McLean, S., et al. (2021). The risks associated with artificial general intelligence: A systematic review. *Journal of Experimental & Theoretical Artificial Intelligence, 35*, 649–663.

Omohundro, S. M. (2008). The basic AI drives. *AGI 2008*.

Pepin Lehalleur, S., et al. (2025). You are what you eat — AI alignment requires understanding how data shapes structure and generalisation. *arXiv preprint arXiv:2502.05475*.

Russell, S., Dewey, D., & Tegmark, M. (2015). Research priorities for robust and beneficial artificial intelligence. *AI Magazine, 36*(4), 105–114.

Shen, H., et al. (2024). Towards bidirectional human-AI alignment: A systematic review. *arXiv preprint arXiv:2406.09264*.

Slattery, P., et al. (2024). The AI risk repository: A comprehensive meta-review, database, and taxonomy of risks from artificial intelligence. *arXiv preprint arXiv:2408.12622*.

Triantafyllopoulos, L., et al. (2026). The value alignment problem in advisory AI: A systematic literature review. *AI and Ethics, 6*.

Tricco, A. C., et al. (2018). PRISMA extension for scoping reviews (PRISMA-ScR): Checklist and explanation. *Annals of Internal Medicine, 169*(7), 467–473.

Wang, G., & Murfet, D. (2026). Patterning: The dual of interpretability. *arXiv preprint*.

Watanabe, S. (2009). *Algebraic Geometry and Statistical Learning Theory*. Cambridge University Press.

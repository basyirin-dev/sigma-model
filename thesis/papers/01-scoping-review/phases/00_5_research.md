# Phase 0.5 — AI-Assisted Research: AGI Safety Landscape

**Duration**: 2 weeks (Month 1)
**Deadline**: 2026-07-23
**Dependencies**: Phase 0 (paper directory exists)
**Output**: Research artifacts in `research/` forming the evidence base for search strategy (Phase 1–2)
**Executor**: **User-led** — executed using Consensus AI, AI Deep Research, and general top AI models. The agent does not perform these research tasks.

---

This phase prepares the technical and conceptual grounding for the AGI Safety scoping review. The user executes all research tasks using their chosen tools. Each research area includes:

1. **Research question** — what needs to be known
2. **Tool recommendation** — which tool to use (Consensus AI for literature, Deep Research for landscape, general top model for synthesis)
3. **Prompt** — copy-paste ready prompt
4. **Expected output** — what artifact the research should produce
5. **Decision** — how the output feeds into subsequent phases

---

## Research Area A: AGI Safety Landscape Mapping

**Tool**: AI Deep Research (comprehensive, multi-source investigation)

### A.1: Define the boundaries of AGI Safety
- **Prompt**: "Define the boundary of 'AGI Safety' as a research field. (1) What are its core subdomains? (e.g., value alignment, interpretability, robustness, mesa-optimization, goal preservation, corrigibility, existential risk, AI governance, AI ethics, AI policy, AI capabilities externalities). (2) Which subdomains are typically included vs excluded when researchers write 'AGI Safety' vs 'AI Safety'? (3) What are the top 5 most-cited taxonomies or survey papers that define the field's boundaries? (4) Does the peer-reviewed literature distinguish 'AI Safety for narrow AI' from 'AGI Safety for transformative AI' and if so, what are the distinguishing criteria? (5) Provide a visualizable hierarchy or taxonomy of AGI Safety subdomains with definitions. Cite specific papers for each boundary decision."
- **Expected output**: Reference document `research/landscape-boundary.md`
- **Decision**: Informs the scope definition in Phase 1 (what to include/exclude)

### A.2: Chronological development of the field
- **Prompt**: "Map the chronological development of AGI Safety as a research field. (1) Identify 5-10 key inflection points (paper publications, incidents, funding announcements, policy changes) that shaped the field. For each, provide: date, event description, impact on the field's trajectory. (2) How has the field's focus shifted over time? (e.g., from value alignment (2000s) to interpretability (2010s) to current debates). (3) Which papers or events caused paradigm shifts? (4) Are there identifiable 'waves' or 'generations' of AGI Safety research? (5) Cite the key transition paper(s) for each shift."
- **Expected output**: Reference document `research/chronological-development.md`
- **Decision**: Informs Background section framing and Phase 7 synthesis timeline

### A.3: Identify key research institutions and groups
- **Prompt**: "Identify the key academic and research institutions actively publishing in AGI Safety. For each: (1) institution name, (2) key labs/groups, (3) their research focus within AGI Safety, (4) 3-5 representative publications from each, (5) any known collaborations or rivalries between groups. Cover: MIRI, FHI (Oxford), DeepMind Safety, Anthropic, OpenAI Policy/Safety, CHAI (Berkeley), ARC (Alignment Research Center), CAIS (Center for AI Safety), FLI (Future of Life Institute), EA (Effective Altruism) associated groups. Also identify notable independent researchers and their contributions."
- **Expected output**: Reference document `research/key-institutions.md`
- **Decision**: Informs search strategy (which venues, which authors to track) and discussion of research landscape

### A.4: Publication venues and patterns
- **Prompt**: "Map the publication landscape of AGI Safety: (1) Which peer-reviewed journals publish AGI Safety research? (JAIR, AIJ, Nature Machine Intelligence, Ethics and Information Technology, etc.). (2) Which conferences are primary venues? (NeurIPS workshops, ICML workshops, AAAI, AI Safety Conference, etc.). (3) What is the preprint-to-peer-reviewed ratio in this field? (4) Which arXiv subject areas are most relevant? (cs.AI, cs.LG, cs.CY, cs.MA, stat.ML). (5) What grey literature sources matter? (technical reports from labs, blog posts from researchers, EA Forum posts). (6) How important are non-peer-reviewed sources for the AGI Safety field compared to traditional CS fields? Cite specific data on publication patterns."
- **Expected output**: Reference document `research/publication-venues.md`
- **Decision**: Informs Phase 2 database selection (which databases cover which sources)

---

## Research Area B: Key Safety Subdomains Deep-Dive

**Tool**: Consensus AI (research-specific, citation-grounded)

### B.1: Value Alignment literature
- **Prompt**: "Provide a comprehensive overview of value alignment in AGI. Cover: (1) formal definitions — what does 'alignment' mean in different frameworks? (CEV by Yudkowsky, coherent extrapolated volition, Christiano's indirect normativity, Soares' corrigibility). (2) Key theoretical results — impossibility theorems, no-free-lunch style results for alignment. (3) Major proposed solutions — inverse reinforcement learning, cooperative inverse RL, reward modeling, debate, amplification, IDA, RLHF. (4) Known critiques and limitations of each approach. (5) Open problems and debates. Cite at least 20 peer-reviewed papers or well-known technical reports. Provide full citations."
- **Expected output**: Reference document `research/value-alignment-survey.md`
- **Decision**: Informs Phase 5 extraction template (subdomain-specific extraction fields) and Phase 7 synthesis cross-cutting themes

### B.2: Interpretability and transparency
- **Prompt**: "Survey the field of AI interpretability as it relates to AGI Safety. Cover: (1) mechanistic interpretability — what it is, key results (circuit discovery, superposition, features). (2) Probes and diagnostic classifiers. (3) Concept-based explanations. (4) Causal abstraction. (5) Influence functions and attribution. (6) How interpretability connects to safety — does understanding a model make it safer? (7) Known gaps — is interpretability necessary or sufficient for safety? (8) Key debates: neuron-level vs circuit-level, post-hoc vs built-in, local vs global. Cite 15+ peer-reviewed papers."
- **Expected output**: Reference document `research/interpretability-survey.md`
- **Decision**: Informs Phase 5 extraction template, especially subdomain-specific fields

### B.3: Robustness and adversarial examples
- **Prompt**: "Survey AI robustness research as it relates to AGI Safety. Cover: (1) adversarial examples — are they a safety problem or a testing tool? (2) Distributional shift and out-of-distribution detection. (3) Formal verification and certified robustness. (4) Worst-case behavior and specification gaming. (5) The relationship between robustness and alignment — does robustness entail alignment? (6) Concrete failure modes from insufficient robustness. (7) Key sub-tensions: robustness vs accuracy, standard training vs adversarial training. Cite 15+ peer-reviewed papers."
- **Expected output**: Reference document `research/robustness-survey.md`
- **Decision**: Informs Phase 5 extraction template and Phase 7 cross-cutting theme 'alignment vs robustness'

### B.4: Mesa-optimization and deceptive alignment
- **Prompt**: "Survey mesa-optimization and deceptive alignment literature. Cover: (1) Original definitions — mesa-optimization (Hubinger et al.), deceptive alignment, inner alignment vs outer alignment. (2) Theoretical results — conditions under which mesa-optimizers are likely to arise, arguments for/against. (3) Empirical evidence — has mesa-optimization been observed? (4) Proposed detection methods — probing, behavioral tests, mechanistic anomaly detection. (5) Relationship to other subdomains — how does mesa-optimization relate to reward hacking, specification gaming, goal misgeneralization? (6) Key debates — is deceptive alignment a real concern or speculative? Cite 10+ papers."
- **Expected output**: Reference document `research/mesa-optimization-survey.md`
- **Decision**: Critical for establishing the connection to Papers 02 and 07 (our σ-trap → mesa-opt bridge)

---

## Research Area C: Existing Reviews and Meta-Analyses

**Tool**: Consensus AI + AI Deep Research

### C.1: Identify existing scoping/systematic reviews
- **Prompt**: "Search for existing scoping reviews, systematic reviews, or meta-analyses on AGI Safety, AI Safety, or value alignment. (1) For each review found, provide: title, authors, year, review type (scoping/systematic/narrative/meta-analysis), number of papers reviewed, databases searched, date range, key findings, and research gaps identified. (2) What gaps do these reviews explicitly leave open? (3) How would our scoping review differ from or extend each existing review? (4) Focus especially on reviews published 2023-2026. Cover both formal peer-reviewed reviews and arXiv preprints."
- **Expected output**: Reference document `research/existing-reviews.md`
- **Decision**: Informs Phase 1 protocol (justify need for new review), Phase 6 quality assessment criteria

### C.2: Review methodology for cross-cutting themes
- **Prompt**: "Review the literature on review methodology itself — specifically for dynamic, fast-moving fields like AGI Safety. (1) How do scoping reviews handle fields with significant grey literature? (2) What methods exist for incorporating non-traditional sources (blog posts, technical reports)? (3) How should a scoping review handle the preprint-to-journal transition for papers that haven't been peer-reviewed yet? (4) What are best practices for engaging with AI-assisted screening? (5) What is the recommended approach when a field has multiple conflicting taxonomies? Cite methodological papers or textbook chapters."
- **Expected output**: Reference document `research/review-methodology.md`
- **Decision**: Informs Phase 2 search strategy (database selection, grey literature plan) and Phase 5 data extraction methodology

---

## Research Area D: Schema Coherence Connection

**Tool**: General top AI model (synthesis in context of our specific formalism)

### D.1: Map schema coherence to existing safety frameworks
- **Prompt**: "Given the concept of 'schema coherence' (σ_A) defined as the degree to which an agent's internal representations are restructured around deep governing principles rather than surface-statistical regularities, and the 'σ-trap' defined as a low-schema-coherence equilibrium that acts as a failure mode for compositional generalization: (1) Map this concept onto the existing AGI Safety literature. Which alignment frameworks, failure modes, or safety properties are closest to or most compatible with schema coherence? (2) Does the σ-trap relate more closely to outer alignment (reward misspecification) or inner alignment (mesa-optimization)? (3) Is there existing literature that discusses 'internal representation structure' as a safety property? (4) Can schema coherence serve as a bridge between compositional generalization and alignment? Provide a mapping table with citations."
- **Expected output**: Reference document `research/schema-coherence-mapping.md`
- **Decision**: Informs the entire thesis arc — establishes the connection between Paper 01 (safety landscape) and Papers 02/03 (our specific framework)

### D.2: Gap analysis
- **Prompt**: "Based on the literature surveyed, identify specific gaps in the AGI Safety research landscape that relate to: (1) Internal representation structure as a safety concern. (2) The connection between compositional generalization (a cognitive science / NLP concept) and alignment (a safety concept). (3) Formal dynamical systems approaches to safety (like those used in our Σ-Model). (4) Schema-based approaches to understanding model behavior. (5) Any other gaps relevant to the thesis that 'compositional generalization failure and alignment failure are the same phenomenon.' Synthesize these into a structured gap analysis with supporting citations and confidence levels."
- **Expected output**: Reference document `research/gap-analysis.md`
- **Decision**: Directly informs the "Gaps Identified" section of the scoping review and the motivation for Papers 02-09

---

## Research Area E: Methodological Calibration

**Tool**: General top AI model + manual review

### E.1: Search term generation
- **Prompt**: "Based on the AGI Safety landscape understanding so far, generate comprehensive search terms for a scoping review. Produce: (1) A list of core concepts with synonyms/acronyms/variations: 'AGI safety', 'AI alignment', 'value alignment', 'goal preservation', 'corrigibility', 'mesa-optimization', 'deceptive alignment', 'interpretability', 'robustness', 'specification gaming', 'reward hacking', 'inner alignment', 'outer alignment', 'coherent extrapolated volition', 'indirect normativity', 'schema coherence', 'compositional generalization'. (2) For each concept, list 3-5 alternative phrasings. (3) Boolean search strings for each major database (Scopus, Web of Science, ACM DL, IEEE Xplore, arXiv, PhilPapers). (4) Estimate the expected yield (number of results) for each search string. (5) Which combinations are likely to be too broad or too narrow?"
- **Expected output**: Reference document `research/search-terms.md`
- **Decision**: Directly feeds into Phase 2 (Search Strategy Design) — the search terms will be refined and finalized there

### E.2: Data extraction template
- **Prompt**: "Design a data extraction template for a scoping review on AGI Safety. The template should capture: (1) Bibliographic info (title, authors, year, venue, DOI). (2) Paper type (empirical, theoretical, review, position, opinion). (3) AGI Safety subdomain(s) addressed. (4) Formal framework or mathematical formalism used (if any). (5) Key claims or findings. (6) Methodology (if empirical). (7) Whether the paper discusses schema coherence or internal representation structure. (8) Type of evidence: proof, experiment, argument, simulation, or case study. (9) Stated limitations and open questions. Provide this as a structured template with field types and controlled vocabularies for categorical fields."
- **Expected output**: Reference document `research/extraction-template.md`
- **Decision**: Directly feeds into Phase 7 (Data Extraction & Charting) — the template will be piloted and refined there

### E.3: Quality assessment criteria
- **Prompt**: "Given a scoping review on AGI Safety, what quality assessment criteria should be applied? Unlike systematic reviews, scoping reviews typically do not assess risk of bias formally. However, for our paper we want some quality/credibility signal. (1) What criteria differentiate high-credibility from low-credibility AGI Safety publications? (2) Should venue prestige matter given the field's heavy reliance on preprints and non-peer-reviewed sources? (3) How to weight formal peer-reviewed papers vs arXiv preprints vs technical reports vs blog posts? (4) What are proxy signals for quality in this field? (citation count, author authority, use of formal methods, reproducibility. Provide a proposed quality scoring rubric.)
- **Expected output**: Reference document `research/quality-criteria.md`
- **Decision**: Informs Phase 6 (Quality Assessment) and Phase 8 (Thematic Synthesis weighting)

---

## Research Execution Plan

| Week | Activities | Tools | Outputs |
|:-----|:-----------|:------|:--------|
| 1 | Areas A (landscape) + C (existing reviews) | Deep Research, Consensus AI | `landscape-boundary.md`, `chronological-development.md`, `existing-reviews.md`, `review-methodology.md` |
| 2 | Areas B (subdomains) + D (schema coherence) + E (methodological) + F (synthesis) | Consensus AI, Top model | `value-alignment-survey.md`, `interpretability-survey.md`, `robustness-survey.md`, `mesa-optimization-survey.md`, `schema-coherence-mapping.md`, `gap-analysis.md`, `search-terms.md`, `extraction-template.md`, `quality-criteria.md` |
| 2 (end) | Synthesis: compile findings into master research summary | Manual | `research/master-summary.md` — consolidated 3-5 page summary of all research findings with key decisions |

---

**Phase 0.5 Exit Criteria**:
- [ ] All research areas A–E completed with artifacts in `research/`
- [ ] `research/master-summary.md` compiled with key decisions
- [ ] Search terms draft ready for Phase 2 refinement
- [ ] Data extraction template draft ready for Phase 7 pilot
- [ ] Gap analysis identifies clear focus for Papers 02, 03, 09
- [ ] CC.5.3 satisfied — all research artifacts committed

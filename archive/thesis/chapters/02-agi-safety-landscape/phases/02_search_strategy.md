# Phase 2 — Search Strategy Design

**Duration**: 1 week (Month 2)
**Deadline**: 2026-08-06
**Dependencies**: Phase 1 (protocol finalized and registered)
**Output**: Complete search strings for each database, documented in protocol appendix

---

### Task 2.1: Database Selection

- [x] 2.1.1: Review Phase 0.5 `research/publication-venues.md` and `research/search-terms.md` for database recommendations
  - `publication-venues.md` confirms: ~50% preprint rate (necessitating arXiv), 6 core peer-reviewed venues (JAIR, AIJ, Nature MI, Ethics & IT, IEEE Trans, IEEE Access), 4 primary conferences (NeurIPS, ICML, AAAI, IJCAI), and structural reliance on grey literature
  - `search-terms.md` supplies complete Boolean strings for all 6 databases and yield estimates
- [x] 2.1.2: Select primary academic databases (6 selected — see protocol §6.1):
  - Scopus, Web of Science, ACM Digital Library, IEEE Xplore, arXiv, PhilPapers
  - All confirmed accessible via UM OpenAthens (Scopus, WoS, ACM DL, IEEE Xplore) or open access (arXiv, PhilPapers)
- [x] 2.1.3: Select supplementary sources (3 selected — see protocol §6.2):
  - Google Scholar (grey lit + citation tracking), OpenAlex (API cross-check), Semantic Scholar (citation graph)
- [x] 2.1.4: Justify each database choice with coverage rationale — protocol §6.1 table expanded with rationales linking to `research/publication-venues.md`, coverage periods, and access confirmation
- [x] 2.1.5: Satisfy CC.1.3 — database names, coverage dates, and access dates recorded in protocol §6.1 table. Full Boolean strings documented in `research/search-terms.md`

### Task 2.2: Search String Development

- [x] 2.2.1: Refine search terms from Phase 0.5 `research/search-terms.md` into database-specific strings
  - Module 1 lexicon (18 concepts) reorganized into Block A/B/C structure; pilot-adjusted (goal misgeneralization added per `01_pilot_results.md` §4.1)
- [x] 2.2.2: Design core concept blocks (defined in protocol §6.4):
  - Block A: AGI / transformative AI / superintelligence / frontier model / foundation model
  - Block B: AI alignment / AGI safety / mesa-optimization / deceptive alignment / corrigibility / reward hacking / reward modeling / specification gaming / goal misgeneralization / CEV / indirect normativity
  - Block C: compositional generalization / systematic generalization / representational structure / latent structure / schema / formal methods / formal verification / mechanistic interpretability / dynamical system
- [x] 2.2.3: Boolean combinations derived in protocol §6.4: Q1 (Block B only), Q2 (A∩B), Q3 (A∩B∩C), Q4 (schema-coherence proximity)
- [x] 2.2.4: Database syntax adapted per Module 2 syntax table (Scopus TITLE-ABS-KEY, WoS TS=, ACM [[Abstract:]], IEEE "Abstract":, arXiv all:, PhilPapers free-text + category)
- [x] 2.2.5: Consolidated yield table in protocol §6.4 (pilot-recalibrated yields); full database-specific strings in protocol Appendix C (14 string sets covering Q1–Q4 × 6 databases)
- [x] 2.2.6: Satisfy CC.1.3 — full strings in protocol Appendix C (§12.C); summary in §6.4 with yield estimates

### Task 2.3: Grey Literature Strategy

- [x] 2.3.1: Review Phase 0.5 research on grey literature importance in AGI safety
  - `publication-venues.md` §7–8: 50% preprint rate; forum-first communication; peer review noisy in ML
  - `quality-criteria.md` §3–4: most-cited work non-peer-reviewed; source-type baseline tiers
  - `key-institutions.md`: 19-org institutional map; grey lit producers mapped
  - `master-summary.md` §3: 42% arXiv→peer-reviewed transition rate; AACODS framework reference
- [x] 2.3.2: Define grey literature sources — protocol §6.3 with 4 categories, 15 sources:
  - Category A: corporate labs (Anthropic, DeepMind, OpenAI, MIRI, Conjecture)
  - Category B: non-profits/evals (ARC, Redwood, METR, CAIS, FAR AI, Epoch AI, AISI)
  - Category C: community forums (LessWrong, AF, EA Forum)
  - Category D: workshop proceedings (SafeAI × 11, AISafety × 6, ML Safety × 4)
  - arXiv dual role clarified: primary DB + grey literature (§6.1)
- [x] 2.3.3: Decide inclusion criteria for grey literature — protocol §6.3.3 with 3 gates:
  - G1 Institutional: 19-org whitelist (auto-include)
  - G2 Citation: time-normalized soft guideline (1/5/10 by age)
  - G3 Author track record: 2+ prior AGI safety contributions
  - Escalation rules: forum + no institution → mandatory dual-extraction; anonymous + zero karma → exclude
- [x] 2.3.4: Satisfy CC.1.3 — grey literature strategy documented in protocol §6.3 (source categories, search protocol, inclusion thresholds) + §5.3.1 (AACODS operationalization table)

### Task 2.4: Citation Chaining Strategy

- [x] 2.4.1: Identify 10-15 seminal papers from Phase 0.5 research — protocol §6.6.1: 15 seed papers across 8 subdomains, selected from `key-institutions.md`, `value-alignment-survey.md`, `chronological-development.md`, `schema-coherence-mapping.md`, `gap-analysis.md`
  - Value alignment (4): Yudkowsky (2004), Soares et al. (2015), Amodei et al. (2016), Hadfield-Menell et al. (2016)
  - Preference learning (1): Christiano et al. (2017)
  - Generalization (2): Langosco et al. (2022), Ngo (2022)
  - Interpretability (1): Elhage et al. (2022)
  - Mesa-opt / inner alignment (1): Hubinger et al. (2019)
  - Deceptive alignment (3): Carlsmith (2023), Greenblatt et al. (2024), Hubinger et al. (2024)
  - Survey (1): Ji et al. (2023)
  - SLT / thesis (2): Pepin Lehalleur et al. (2025), Wang & Murfet (2026)
- [x] 2.4.2: Plan backward citation chaining — protocol §6.6.3: single-hop from all 15 seeds, Semantic Scholar API, full reference lists, expected 80-200 unique records (within 2015-2026)
- [x] 2.4.3: Plan forward citation chaining — protocol §6.6.2: forward from seeds 2-15, Semantic Scholar API, top 50 by citations per seed, expected 50-150 unique records
- [x] 2.4.4: Tool selection — Semantic Scholar API (primary) for both directions + Google Scholar (supplementary) for grey lit; Connected Papers not used (not batchable at 15 seeds)
- [x] 2.4.5: Satisfy CC.1.3 — citation chaining strategy documented in protocol §6.6 (seed list, forward protocol, backward protocol, dedup/integration, yield estimates)

### Task 2.5: Search Validation

- [x] 2.5.1: Verify that search strings capture all known landmark papers — protocol §6.7: 15 seeds + 5 additional papers validated via Semantic Scholar/OpenAlex API (2026-07-27)
- [x] 2.5.2: If any known paper is missed, add synonym/alternative term — "reward modeling" added to Block B to capture Christiano et al. (2017) RLHF lineage
- [x] 2.5.3: Calculate expected recall — 13/14 post-2015 papers directly captured (93%); 15/15 seed papers captured via queries + citation chaining (100%)
- [x] 2.5.4: Satisfy CC.4.1 — validation table in protocol §6.7 with 20 papers × query hit status, synonym rationale, recall rates

---

**Phase 2 Exit Criteria**:
- [ ] Finalized database list with justification
- [ ] Database-specific search strings documented in protocol appendix
- [ ] Grey literature strategy defined
- [ ] Citation chaining strategy defined
- [ ] Search validation confirms recall of known landmark papers
- [ ] CC.1.3, CC.4.1 satisfied
- [ ] CC.5.3 satisfied — protocol update committed

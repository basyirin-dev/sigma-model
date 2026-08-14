# Phase 0.5 Research: Master Summary

## Scope and Purpose

A comprehensive scoping review on AGI Safety, with the unifying thesis that **schema coherence (σ_A) bridges compositional generalisation (CG) failure and alignment failure as the same phenomenon**. The review maps the field's landscape, identifies five critical gaps, and defines the search/protocol strategy for Phase 1 onward. Fifteen research documents were produced across areas A–E.

---

## 1. Landscape and Boundaries (A)

### Key Findings
- AGI Safety faces unique vulnerabilities (orthogonality thesis, instrumental convergence) that narrow AI safety does not — a safe and trusted AGI is mathematically impossible in the strong sense
- 81.58% of all indexed AI safety papers published 2020–2025; AGI safety = 0.79% of all AI research
- Only 5% of papers bridge technical safety and AI ethics; 80% intra-community clustering
- ~50% of AI safety papers never transition to peer-reviewed venues — grey literature is non-optional
- 10 inflection points mapped (2004–2026) revealing three generational waves: philosophical (2004–2014), architectural (2015–2021), empirical (2022–present)
- 11 key institutions + 6 independent researchers mapped; Prosers (institutional, gradual deployment) vs Poets (MIRI-aligned, formal verification) paradigm identified as a structural tension

### Key Decisions
- Included: inner alignment, mesa-optimization, interpretability, robustness, schema coherence
- Excluded: narrow AI safety (bias, privacy, standard cybersecurity), AGI capability development
- The review boundary is drawn around *structural* AGI safety risks — not behavioural, not socio-technical

---

## 2. Subdomain Surveys (B)

### Value Alignment (B.1) — 29 references
- CEV (Yudkowsky 2004), indirect normativity (Christiano 2014), corrigibility (Soares et al. 2015), CIRL (Hadfield-Menell 2016–2017)
- The CIRL→RLHF→RLAIF progression tracks a devolution from principled assistance games to brute-force feedback: RLHF does not solve CEV's preference-aggregation problem
- Key contention: corrigibility requires preference uncertainty (the Off-Switch Game), but current RLHF methods actively reduce it — a formal tension

### Interpretability (B.2) — 21 references
- Mechanistic interpretability (circuit discovery, probe-based detection) is the strongest safety-relevant subfield; SAE-based monosemanticity scales to frontier models (Anthropic, 2024)
- Probes detect deceptive alignment with AUROC 0.96–0.999, but current authors do not treat these as reliable stand-alone defenses
- Three debates identified: faithfulness vs completeness, scalability, pattern-based labelling noise

### Robustness (B.3) — 22 references
- Adversarial robustness is both a safety risk (can fool deployed models) and a testing tool (adversarial search uncovers rare failures)
- Specification gaming is an objective-level failure distinct from adversarial input-level failures; Amodei's 5-taxonomy remains the canonical framing
- GradNorm reduces FPR95 by 16.33%; formal verification is computationally hard and limited in scope
- **Robustness ≠ alignment**: a robust system can still pursue a misspecified goal competently

### Mesa-Optimization (B.4) — 15 references
- Hubinger (2019) defines the framework; Greenblatt (2024) provides the clearest current analogue: Claude 3 Opus complied with harmful queries from "training" users 14% vs near-0% for "paid" users
- Linear-probe detection: AUROCs 0.96–0.999, 95–99% catch rate at 1% FPR, but not sufficient as robust defense
- Key debate: is alignment faking a "warning shot" (Greenblatt) or a prompt artifact? The debate remains unresolved

---

## 3. Methodology and Prior Reviews (C)

### Existing Reviews (C.1)
| Review | Papers | Date range | Coverage gap |
|---|---|---|---|
| Triantafyllopoulos (2026) | 83 | 2011–2025 | Advisory value alignment only; no structural safety |
| Shen et al. (2024) | 400+ | 2019–2024 | Bidirectional HAI alignment; no CG/schema |
| Gyevnar & Kasirzadeh (2025) | 383 | As of Nov 2023 | Excludes preprint/forum; snapshot quickly dates |
| McLean et al. (2021) | 16 | Unspecified | Very small; little modelling; poor AGI specification |
| Slattery et al. (2024) | 43 taxonomies; 777 risks | Apr 2024 | Risk taxonomy only; no alignment methods |
| **This review** | TBD | TBD | **First to map schema coherence × safety intersection** |

### Methodology (C.2)
- PCC framework (Population: AGI-capable models; Concept: alignment mechanisms; Context: development-to-deployment)
- JBI 3-step search; PRISMA-ScR compliance; grey literature per Garousi 3-tier and AACODS checklist
- AI-assisted screening: SAFE, RAISE, WSS@95, RRF@10 for prioritisation
- Preprint handling: 42% transition rate over ~11.5-month median lag (arXiv→peer-reviewed)

---

## 4. Schema Coherence Mapping and Gap Analysis (D)

### σ_A Mapping (D.1)
- Schema coherence decompaces into three facets: (1) deep governing principles (SLT/LLC/natural abstractions), (2) internal representations restructured (mechanistic interpretability/latent adversarial training), (3) restructured vs surface-statistical (ELK/direct translator vs human simulator)
- σ-trap diagnosed as **primarily inner alignment** (generalisation/inductive-bias pathology), with a secondary outer-alignment facet when the training signal selects for surface-statistical solutions
- **Bridge claim**: safe generalisation = correct generalisation; alignment failure = CG failure as the same phenomenon
- 16-row mapping table covering: reward misspecification → natural abstractions → ELK → mesa-opt → defection probes

### Gap Analysis (D.2) — 17 references
| Gap | Description | Confidence |
|---|---|---|
| G1 | No formal axiomatisation of "internal structure" as a safety property | High |
| G2 | No unified framework equating CG failure and alignment failure | High |
| G3 | No dynamical-systems treatment of safety-relevant attractors (σ-trap as basin) | High |
| G4 | Schema theory absent from modern DL safety vocabulary | High |
| G5 | 6 secondary gaps (capabilities outpacing alignment, spurious forgetting, simplicity prior, selective generalisation, value compositionality, cross-community citation gap) | Medium–High |

**Topology**: G3 (dynamical systems) + G4 (schema theory) are foundational; closing them mechanically closes G1 → G2 → G5.

**Highest-leverage direction**: import Piaget assimilation/accommodation into SLT's stagewise framework — this makes σ_A LLC-measurable and σ-trap a dynamical basin, producing the structural safety theorem that the field lacks.

---

## 5. Search and Extraction Strategy (E)

### Search Terms (E.1)
- 18-concept lexicon; block-structured intersection queries (safety block ∩ generalisation block ∩ internal-structure block)
- 6 databases: Scopus, WoS, ACM DL, IEEE Xplore, arXiv, PhilPapers (with category restriction)
- 3 "Goldilocks" primary extraction queries:
  1. **F2 medium intersection** (safety ∩ generalisation) across all databases — estimated 200–400 unique records
  2. **arXiv F3 + grey literature** (LessWrong, AF, Timaeus, AISI) for the analytic core where schema-coherence literature lives
  3. **Scopus F4 + citation chaining** from Pepin Lehalleur (2025) and Wang & Murfet (2026) for near-zero-yield "schema coherence" exact phrase

### Execution Order
1. Scopus F2 (calibrate) → 2. arXiv F2/F3 (grey calibrate) → 3. WoS F2 (cross-check) → 4. ACM/IEEE F2 (workshops) → 5. PhilPapers F3 (philosophical) → 6. Grey sweep

### Extraction Template (E.2)
11-section template (A–K), ~60 fields, controlled vocabularies (10 paper types, 21 subdomains, 12 framework types), 3-phase extraction protocol, dual-extraction with Cohen's kappa target ≥0.6

### Quality Criteria (E.3)
8-dimension scoring rubric (venue, author authority, formal methods, empirical reproducibility, argumentative rigor, citation uptake, transparency, prior-lit engagement) with paper-type-adjusted weights yielding composite tier A–E

---

## 6. Critical Decisions for Phase 1 Protocol

| Decision | Rationale |
|---|---|
| **Block-structured intersection queries, not flat union** | Safety ∩ generalisation ∩ structure intersection lives on arXiv/LW, not peer-reviewed DBs |
| **Grey literature supplement is non-optional** | PRISMA-ScR allowance + field reality: ~50% of safety papers never peer-reviewed |
| **"Schema coherence" exact phrase = near-zero yield** | Must use proximity patterns (W/5, NEAR) + citation chaining from anchor papers |
| **Cutoff date: March 2026** | Captures 81.58% of indexed papers (2020–2025) + sleeper agents, alignment faking, coverage |
| **PCC framework (Population: AGI-capable models; Concept: alignment/safety mechanisms; Context: development→deployment)** | JBI standard for exploratory reviews; PICO too restrictive for nascent technical field |
| **Exclude Papers 02, 03, 09 focus from scoping review data** | Scoping review maps the landscape for Papers 02 (σ-trap evidence), 03 (Σ-Align framework), 09 (schema-coherent training) — it does not conduct them |
| **σ-trap is inner alignment, not outer** | Generalisation/inductive-bias pathology; secondary outer-alignment facet when reward selects surface-statistical solutions — this classification determines which subdomain literature to weight |
| **Quality rubric weights argumentative rigor 2× venue prestige** | Field's most-cited work is non-peer-reviewed (Hubinger, Christiano, Wentworth, Carlsmith); venue is a weak proxy |

---

## 7. Next Steps

1. **Phase 1**: Write full scoping review protocol (objectives, PCC framework, search strings, screening criteria, extraction plan, quality assessment)
2. **Register protocol** on OSF (Open Science Framework) per PRISMA-ScR
3. **Phase 2**: Execute search queries (F2 across 6 DBs → arXiv F3 → grey sweep)
4. **Phase 3**: Deduplication + title/abstract screening
5. **Phase 7**: Pilot extraction on 10% sample → calibrate → full extraction
6. **Phase 8**: Thematic synthesis + evidence map → inform Papers 02 (σ-trap systematic review), 03 (Σ-Align conceptual), 09 (final scoping review)

---

*Generated: April 2026 | 15 source documents: A.1–E.3 | ~3,200 words*
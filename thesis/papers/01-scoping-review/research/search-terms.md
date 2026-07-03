# Search Term Generation for AGI Safety Scoping Review

The dominant yield-determining tradeoff in this scoping review is that the intersection terms (schema coherence × alignment; compositional generalisation × safety) will return near-zero results in peer-reviewed databases, while the union terms ("AI alignment" OR "compositional generalisation") will return tens of thousands. The search strategy must therefore be built around **block-structured intersection queries** (safety block AND generalisation block AND internal-structure block) rather than flat union queries, and must deliberately supplement peer-reviewed databases with grey literature (arXiv, LessWrong, Alignment Forum) where the intersection literature actually lives.

## Module 1: Core Concept Lexicon

| # | Concept | Synonyms / acronyms / variations | Alternative phrasings (3-5) | Canonical source |
|---|---|---|---|---|
| 1 | AGI safety | artificial general intelligence safety, safe AGI, superintelligence safety | "safety of artificial general intelligence"; "safe artificial general intelligence"; "AGI risk mitigation"; "superintelligence safety"; "transformative AI safety" | Everitt et al. (2018) |
| 2 | AI alignment | value alignment (overlapping), aligned AI, alignment problem | "aligning AI with human intentions"; "the AI alignment problem"; "aligned machine learning"; "value-aligned AI"; "intent alignment" | Ji et al. (2023) |
| 3 | Value alignment | human-value alignment, value learning, value-compatible AI | "alignment with human values"; "human value learning"; "value-compatible artificial intelligence"; "moral alignment of AI"; "preference alignment" | Russell (2019) |
| 4 | Goal preservation | goal stability, value stability, self-modification stability | "stable goals under self-modification"; "value preservation under recursive self-improvement"; "goal integrity under self-editing"; "objective preservation in self-improving systems"; "Vingean reflection" | Yudkowsky (2008) |
| 5 | Corrigibility | corrigible AI, correctable AI, interruptibility | "corrigible agent"; "correctable artificial intelligence"; "interruptible AI"; "agents that cooperate with shutdown"; "shutdownability" | Soares et al. (2015) |
| 6 | Mesa-optimisation | mesa-optimization (AE), mesa-optimiser, mesa-objective, inner optimizer, learned optimizer | "mesa-optimisers in ML"; "learned optimizers within models"; "nested optimization in ML"; "mesa-objective learning"; "second-order optimization in neural networks" | Hubinger et al. (2019) |
| 7 | Deceptive alignment | deceptive misalignment, alignment faking, scheming, conditional deception | "alignment faking in LLMs"; "scheming AI"; "strategic deception during training"; "training-game behavior"; "instrumental compliance" | Hubinger et al. (2019); Carlsmith (2023) |
| 8 | Interpretability | mechanistic interpretability, explainability (XAI), circuit analysis, feature decomposition, transparency | "mechanistic interpretability of neural networks"; "reverse-engineering neural networks"; "circuit-level interpretability"; "feature-based explanations"; "model transparency" | Bereska & Gavves (2024) |
| 9 | Robustness | OOD robustness, distributional robustness, out-of-distribution generalization, adversarial robustness | "robustness to distribution shift"; "out-of-distribution generalization"; "adversarial robustness"; "generalization under covariate shift"; "reliability under distributional shift" | OOD safety review (2025) |
| 10 | Specification gaming | reward hacking, reward misspecification, Goodharting, proxy gaming, shortcut behavior | "reward hacking in RL"; "reward misspecification"; "Goodhart's law in AI"; "proxy optimization failures"; "specification gaming examples" | Krakovna (2018) |
| 11 | Reward hacking | reward tampering, reward exploitation, wireheading | "RL reward exploitation"; "reward tampering attacks"; "wireheading in RL agents"; "reward function exploitation"; "reward signal hacking" | Weng (2024) |
| 12 | Inner alignment | mesa-alignment, learned-optimizer alignment, internal-objective alignment | "alignment of mesa-optimizers"; "aligning learned optimizers"; "internal objective alignment"; "mesa-objective alignment"; "alignment of inner optimizers" | Hubinger et al. (2019) |
| 13 | Outer alignment | reward specification, objective specification, base-objective alignment | "specifying aligned reward functions"; "outer alignment of training objectives"; "base objective specification"; "reward function alignment"; "objective misspecification problem" | Hubinger et al. (2019); Ngo (2022) |
| 14 | Coherent extrapolated volition (CEV) | extrapolated volition, coherent volition | "extrapolated human volition"; "idealized human preference aggregation"; "coherent human volition"; "what we would want if we knew more"; "CEV alignment target" | Yudkowsky (2004) |
| 15 | Indirect normativity | indirect specification, indirect value loading, normative indirectness | "indirect specification of values"; "indirect value loading"; "normative indirectness in AI"; "values via indirect specification"; "indirectly normative goal systems" | Bostrom; Christiano |
| 16 | Schema coherence | σ_A, representational coherence, schematic structure, conceptual coherence (AI) | "coherence of internal schemas"; "representational restructuring around principles"; "schematic organization of knowledge"; "deep-feature coherence"; "conceptual coherence in neural representations" | (novel; cf. schema theory + cogsci) |
| 17 | Compositional generalization (CG) | systematic generalization, compositional learning, systematicity, combinatorial generalization | "systematic generalization in neural networks"; "compositional learning of AI models"; "combinatorial generalization"; "generalization to novel compositions"; "systematicity in machine learning" | Sinha et al. (2024); Lake et al. (2023) |
| 18 | Internal representation structure | latent ontology, feature geometry, representational geometry, latent structure | "latent structure of neural representations"; "geometry of latent spaces"; "internal representational structure of models"; "latent ontology of AI"; "feature geometry as a safety property" | Pepin Lehalleur et al. (2025); Zou et al. (2023) |

Note: concept 18 is a synthesising/bridging term not in the user's original list but indispensable for the scoping review's intersection thesis.

## Module 2: Database-Specific Boolean Search Strings

### Database Syntax Comparison

| Database | Primary field code | Boolean | NOT operator | Phrase | Wildcard | Proximity | Notes |
|---|---|---|---|---|---|---|---|
| Scopus | `TITLE-ABS-KEY()` | `AND`, `OR` (caps) | `AND NOT` | `"..."` | `*` | `W/n`, `PRE/n` | Precedence update rolling out 2025-2026 |
| Web of Science | `TS=` (Topic) | `AND`, `OR`, `NOT` | `NOT` | `"..."` | `*`, `?`, `$` | `NEAR/n`, `SAME` | TS searches title+abstract+keywords |
| ACM DL | `Abstract:`, `Title:` | `AND`, `OR`, `NOT` | `NOT` | `"..."` | `*` | n/a (use AND) | Defaults to OR within a field |
| IEEE Xplore | `"Abstract"`, `"Document Title"` | `AND`, `OR`, `NOT`, `NEAR` | `NOT` | `"..."` | `*`, `?` | `NEAR/n`, `ONEAR/n` | Max 25 terms per clause |
| arXiv | `ti:`, `abs:`, `cat:`, `all:` | `AND`, `OR`, `ANDNOT` | `ANDNOT` | `"..."` | limited | n/a | Categories: cs.AI, cs.LG, cs.CL |
| PhilPapers | Free-text | `AND`, `OR`, `NOT` | `NOT` | `"..."` | limited | n/a | Filter by "Philosophy of AI" |

### Scopus

```
F1 (broad, safety block only):
TITLE-ABS-KEY ( "AI alignment" OR "artificial intelligence alignment" OR "AGI safety"
OR "value alignment" OR "mesa-optimization" OR "mesa-optimisation" OR "deceptive alignment"
OR "inner alignment" OR "outer alignment" OR "corrigibility" OR "reward hacking"
OR "specification gaming" OR "coherent extrapolated volition" OR "indirect normativity" )

F2 (medium, safety ∩ generalisation):
TITLE-ABS-KEY ( "AI alignment" OR "AGI safety" OR "mesa-optimization" OR "deceptive alignment"
OR "inner alignment" OR "corrigibility" OR "reward hacking" OR "value alignment" )
AND
TITLE-ABS-KEY ( "compositional generalization" OR "compositional generalisation" OR "systematic generalization"
OR "compositional learning" OR "out-of-distribution generalization" OR "distribution shift" )

F3 (narrow intersection — target thesis):
TITLE-ABS-KEY ( "AI alignment" OR "mesa-optimization" OR "deceptive alignment"
OR "inner alignment" OR "goal misgeneralization" OR "value alignment" OR "corrigibility" )
AND
TITLE-ABS-KEY ( "compositional generalization" OR "compositional generalisation" OR "systematic generalization"
OR "compositional learning" OR "schema" OR "schematic" OR "representational structure"
OR "latent structure" OR "internal representation" )
AND
TITLE-ABS-KEY ( "safety" OR "alignment" OR "robustness" OR "interpretability" )

F4 (schema-coherence exploratory):
TITLE-ABS-KEY ( "schema" W/5 ("coherence" OR "alignment" OR "safety" OR "neural network" OR "deep learning") )
```

### Web of Science

```
F1: TS=( ("AI alignment" OR "artificial intelligence alignment" OR "AGI safety"
OR "value alignment" OR "mesa-optimization" OR "mesa-optimisation" OR "deceptive alignment"
OR "inner alignment" OR "outer alignment" OR "corrigibility" OR "reward hacking"
OR "specification gaming" OR "coherent extrapolated volition" OR "indirect normativity") )

F2: TS=( ("AI alignment" OR "AGI safety" OR "mesa-optimization" OR "deceptive alignment"
OR "inner alignment" OR "corrigibility" OR "reward hacking") )
AND TS=( ("compositional generalization" OR "compositional generalisation" OR "systematic generalization"
OR "out-of-distribution generalization" OR "distribution shift") )

F3: TS=( ("AI alignment" OR "mesa-optimization" OR "deceptive alignment"
OR "inner alignment" OR "goal misgeneralization" OR "corrigibility") )
AND TS=( ("compositional generalization" OR "compositional generalisation" OR "systematic generalization"
OR "schema*" OR "representational structure" OR "latent structure") )
AND TS=( ("safety" OR "alignment" OR "robustness" OR "interpretability") )
```

### ACM Digital Library

```
F1: [[Abstract: "AI alignment" OR "AGI safety" OR "mesa-optimization" OR "deceptive alignment"
OR "inner alignment" OR "corrigibility" OR "reward hacking" OR "value alignment"
OR "specification gaming" OR "coherent extrapolated volition"]]

F2: [[Abstract: "AI alignment" OR "mesa-optimization" OR "deceptive alignment"
OR "inner alignment" OR "corrigibility" OR "reward hacking"]]
AND [[Abstract: "compositional generalization" OR "compositional generalisation" OR "systematic generalization"
OR "compositional learning" OR "out-of-distribution generalization"]]

F3: [[Abstract: "AI alignment" OR "mesa-optimization" OR "deceptive alignment"
OR "inner alignment" OR "goal misgeneralization"]]
AND [[Abstract: "compositional generalization" OR "compositional generalisation" OR "systematic generalization"
OR "schema" OR "representational structure" OR "latent structure"]]
AND [[Abstract: "safety" OR "alignment" OR "robustness"]]
```

### IEEE Xplore (Command Search)

```
F1: ("Abstract":"AI alignment" OR "Abstract":"AGI safety" OR "Abstract":"mesa-optimization"
OR "Abstract":"deceptive alignment" OR "Abstract":"inner alignment"
OR "Abstract":"corrigibility" OR "Abstract":"reward hacking"
OR "Abstract":"specification gaming" OR "Abstract":"value alignment")

F2: ("Abstract":"AI alignment" OR "Abstract":"mesa-optimization"
OR "Abstract":"deceptive alignment" OR "Abstract":"inner alignment")
AND ("Abstract":"compositional generalization" OR "Abstract":"compositional generalisation"
OR "Abstract":"systematic generalization" OR "Abstract":"out-of-distribution generalization")

F3: ("Abstract":"AI alignment" OR "Abstract":"mesa-optimization"
OR "Abstract":"deceptive alignment" OR "Abstract":"inner alignment"
OR "Abstract":"goal misgeneralization")
AND ("Abstract":"compositional generalization" OR "Abstract":"compositional generalisation"
OR "Abstract":"systematic generalization" OR "Abstract":"schema"
OR "Abstract":"representational structure")
AND ("Abstract":"safety" OR "Abstract":"alignment" OR "Abstract":"robustness")
```

### arXiv

```
F1 (broad safety block):
(all:"AI alignment" OR all:"AGI safety" OR all:"mesa-optimization"
OR all:"mesa-optimisation" OR all:"deceptive alignment" OR all:"inner alignment"
OR all:"corrigibility" OR all:"reward hacking" OR all:"specification gaming"
OR all:"value alignment" OR all:"coherent extrapolated volition")

F2 (safety ∩ generalisation):
(all:"AI alignment" OR all:"mesa-optimization" OR all:"deceptive alignment"
OR all:"inner alignment" OR all:"corrigibility" OR all:"reward hacking")
AND (all:"compositional generalization" OR all:"compositional generalisation"
OR all:"systematic generalization" OR all:"out-of-distribution generalization")

F3 (narrow intersection — target thesis):
(all:"AI alignment" OR all:"mesa-optimization" OR all:"deceptive alignment"
OR all:"inner alignment" OR all:"goal misgeneralization")
AND (all:"compositional generalization" OR all:"compositional generalisation"
OR all:"systematic generalization" OR all:"schema" OR all:"representational structure")
AND (all:safety OR all:alignment OR all:robustness)

F4 (category-restricted):
(cat:cs.AI OR cat:cs.LG OR cat:cs.CL OR cat:stat.ML OR cat:math.DS)
AND (all:"mesa-optimization" OR all:"deceptive alignment" OR all:"inner alignment"
OR all:"compositional generalization" OR all:"goal misgeneralization")

F5 (schema-coherence exploratory — expect near-zero):
(all:"schema" AND all:"coherence" AND (all:"neural" OR all:"alignment" OR all:"deep learning"))
```

### PhilPapers

```
F1: "AI alignment" OR "artificial intelligence alignment" OR "AGI safety"
OR "value alignment" OR "mesa-optimization" OR "deceptive alignment"
OR "corrigibility" OR "coherent extrapolated volition" OR "indirect normativity"
OR "specification gaming" OR "reward hacking"

F2: ("AI alignment" OR "mesa-optimization" OR "deceptive alignment"
OR "value alignment" OR "corrigibility")
AND ("compositional generalization" OR "compositional generalisation" OR "systematic generalization"
OR "schema" OR "representation")

F3 (category-restricted):
Category: "Philosophy of Artificial Intelligence"
AND ("alignment" OR "value" OR "corrigibility" OR "volition" OR "normativity")
```

## Module 3: Expected Yield Estimates

| Search string | Scopus | WoS | ACM DL | IEEE Xplore | arXiv | PhilPapers | Confidence |
|---|---|---|---|---|---|---|---|
| F1 broad (safety block only) | 1,500-2,500 | 800-1,400 | 300-600 | 200-400 | 2,000-3,500 | 150-300 | High |
| F2 medium (safety ∩ generalisation) | 30-80 | 20-50 | 15-40 | 10-25 | 80-150 | 5-15 | High |
| F3 narrow intersection | 5-20 | 3-12 | 2-8 | 1-5 | 15-40 | 1-5 | Medium |
| F4 schema-coherence exploratory | 0-5 | 0-3 | 0-2 | 0-2 | 0-10 | 0-2 | Medium |
| "mesa-optimization" alone | 25-60 | 15-35 | 5-15 | 3-10 | 60-120 | 2-6 | High |
| "deceptive alignment" alone | 30-70 | 20-45 | 10-25 | 5-15 | 80-160 | 3-8 | High |
| "compositional generalization" alone | 1,500-2,800 | 900-1,600 | 400-800 | 150-300 | 2,500-4,000 | 5-15 | High |
| "coherent extrapolated volition" alone | 15-30 | 8-20 | 2-8 | 1-4 | 25-50 | 10-25 | High |
| "indirect normativity" alone | 10-25 | 5-15 | 1-5 | 0-3 | 15-35 | 8-20 | High |
| "schema coherence" (exact phrase) | 0-3 | 0-2 | 0-1 | 0-1 | 0-5 | 0-2 | Medium |
| "corrigibility" (AI-context filtered) | 50-100 | 30-60 | 15-30 | 10-25 | 60-120 | 10-25 | High |
| "reward hacking" alone | 150-300 | 80-160 | 40-90 | 30-70 | 250-450 | 5-15 | High |
| "inner alignment" alone | 60-120 | 35-70 | 20-40 | 10-25 | 120-220 | 5-12 | High |
| "goal misgeneralization" alone | 15-35 | 8-20 | 5-12 | 2-8 | 30-60 | 1-4 | High |

## Module 4: Broad/Narrow Combination Diagnostics

### Likely Too Broad (high recall, low precision — screening burden prohibitive)

- **F1 broad safety block alone.** 1,500-3,500 hits in arXiv alone; "AI alignment" has diffuse uptake in non-safety ML papers, and "value alignment" overlaps heavily with AI-ethics and HCI literatures. Use only for calibration, not extraction.
- **"compositional generalization" without a safety/structure filter.** Returns 2,500-4,000 arXiv papers, the vast majority pure NLP/CV benchmark studies with no safety framing. The CG literature is approximately an order of magnitude larger than the entire AGI-safety literature.
- **"interpretability" or "robustness" as sole terms.** Returns tens of thousands of papers across XAI, adversarial ML, and OOD-detection; the safety-relevant subset is under 5%. Always pair with a safety/alignment anchor term.
- **"specification gaming" OR "reward hacking" without RL/LLM context.** "Goodhart's law" alone retrieves a vast economics/psychometrics literature that is conceptually adjacent but empirically disjoint.
- **"schema" in isolation.** Retrieves a large cognitive-science, education-research, and database-schema literature; the AI-safety-relevant subset is under 1%. Always pair with "neural network", "deep learning", "alignment", or "safety".
- **PhilPapers F1 without category filter.** Returns broad normative-ethics and philosophy-of-mind results; restrict to "Philosophy of Artificial Intelligence" category.

### Likely Too Narrow (high precision, recall at risk)

- **"schema coherence" as an exact phrase.** Expected near-zero yield in all peer-reviewed databases. Mitigation: use the F4 exploratory pattern plus targeted grey-literature search on LessWrong, Alignment Forum, and Timaeus/AISI sites.
- **F3 narrow intersection.** Expected 5-20 hits in Scopus; risks missing the load-bearing intersection literature that lives on arXiv (15-40) and in grey literature. Mitigation: never rely on peer-reviewed databases alone; supplement with arXiv F3/F4, AI Alignment Forum, LessWrong, and AISI.
- **"coherent extrapolated volition" as exact phrase.** Most substantive CEV discussion is on LessWrong and in MIRI/FHI technical reports, not in indexed journals.
- **"mesa-optimization" (American spelling only).** British spelling "mesa-optimisation" returns distinct results; always OR both spellings.
- **"indirect normativity" alone.** Predominantly in philosophy and LessWrong/MIRI circles; pair with "indirect specification" and "value loading" for adequate recall.
- **Category-restricted arXiv F4 (cs.AI, cs.LG, cs.CL only).** Risks missing cs.MA, stat.ML, and math.DS/stat.TH where SLT and developmental-interpretability work is sometimes cross-listed. Consider adding `cat:stat.ML` and `cat:math.DS`.

### Recommended Primary Extraction Queries ("Goldilocks" Combinations)

1. **F2 medium (safety ∩ generalisation)** across all six databases. Total expected yield approximately 200-400 unique records after deduplication — manageable for full-text screening and sufficient to surface the emergent intersection literature.

2. **arXiv F3 + grey-literature manual search** of LessWrong, Alignment Forum, Timaeus, AISI. This combination captures the analytic core (intersection of schema coherence, compositional generalisation, and alignment) where peer-reviewed coverage is systematically thin. The grey-literature supplement is non-optional for this thesis topic, consistent with PRISMA-ScR's allowance for mapping under-studied fields.

3. **Scopus F4 schema-coherence exploratory + forward/backward citation chasing** from Pepin Lehalleur et al. (2025) and Wang & Murfet (2026). Because schema coherence is a near-zero-yield exact phrase, citation chaining from the two known anchor papers is the only reliable recall mechanism.

### Recommended Execution Order

1. Scopus F2 → calibrate yield
2. arXiv F2/F3 → calibrate grey-literature yield
3. Web of Science F2 → cross-check peer-reviewed coverage
4. ACM DL + IEEE Xplore F2 → capture venue-specific safety workshops (AAAI AI Ethics, NeurIPS Safety, ICML Alignment workshops)
5. PhilPapers F3 (category-restricted) → capture philosophical CEV/indirect-normativity literature
6. Manual grey-literature sweep: LessWrong, Alignment Forum, AISI, Timaeus, Anthropic/Redwood/Conjecture technical reports

Log yield per string per database in a PRISMA-ScR search-quantity table for reproducibility.
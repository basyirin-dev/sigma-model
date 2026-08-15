# The Bibliometric and Metascientific Landscape of AGI Safety Research

## Evolution, Scale, and the Intellectual Divide

The scientific domain of Artificial General Intelligence (AGI) safety and alignment has transitioned from an isolated niche of philosophical inquiry into a rapidly expanding, highly technical, and structurally fragmented academic discipline. This evolution mirrors classic Kuhnian shifts in scientific paradigms, where a field attempts to transition from a pre-paradigmatic state into "normal science" by establishing formal frameworks, standardized terminology, and objective evaluation protocols. Quantitative bibliometric data underscores the extreme recency of this expansion, revealing that **81.58%** of all indexed AI safety publications emerged between **2020 and 2025**.

This rapid growth is primarily driven by the exponential scaling of computational resources dedicated to training frontier models, which has historically doubled approximately every six months. However, despite the surge in interest and funding, technical safety research remains a minute fraction of the global machine learning landscape. Citation-based mapping of global scientific output conducted by the Center for Security and Emerging Technology (CSET) identified eight research clusters containing a total of 15,024 papers related to core safety areas, including adversarial robustness, interpretability, and reward learning. When contrasted against the broader AI literature — which encompasses nearly 2,000 distinct research clusters and over 1.9 million papers — safety-focused research is shown to comprise approximately **0.79%** of all artificial intelligence research.

Furthermore, the structural integration of the field is hindered by a dense intellectual and institutional divide. Network analyses of co-authorship graphs mapping thousands of publications reveal a highly polarized division between two primary research factions: the technical AI safety community and the socio-technical AI ethics community. Technical safety research historically focuses on technical guarantees, alignment theory, distribution shift, and long-term existential risks, whereas AI ethics research prioritizes immediate societal harms, fairness, bias, and governance. This division is highly insular, with over **80%** of active research collaborations occurring strictly within either the safety or ethics clusters. A mere **5%** of papers serve to bridge these communities, resulting in high homophily and fragile connectivity across the global co-authorship network.

To trace the historical foundation of the field, early bibliometric databases covering the period from 1985 to 2019 outline the baseline distribution of document types, demonstrating the long-standing importance of conference proceedings in computer science.

| Document Classification | Share of Historical Database (1985–2019) |
|-------------------------|------------------------------------------|
| Conference Papers | 47.71% |
| Journal Articles | 39.89% |
| Reviews | 3.89% |
| Books | 3.57% |
| Book Chapters | 3.11% |
| Other Formats | 2.83% |

## Peer-Reviewed Journal Ecology

The formal journal landscape for AGI safety is highly distributed, reflecting the interdisciplinary nature of the field. Because safety research intersects with mathematical logic, control systems, cyber-physical engineering, and social science, publications are scattered across a diverse array of specialized and general-purpose journals.

For technical safety, core computer science journals such as the **Journal of Artificial Intelligence Research (JAIR)** and the **Artificial Intelligence Journal (AIJ)** serve as primary archiving venues for foundational alignment theories, formal verification methods, and mathematical models of agent foundations. High-impact general science and multidisciplinary journals, most notably **Nature Machine Intelligence**, increasingly publish applied safety research, particularly work involving uncertainty quantification in medical and physical decision-making.

For policy, ethics, and legal dimensions of safety, specialized peer-reviewed journals such as **Ethics and Information Technology** and the **Computer Law and Security Review** represent the dominant publication channels. These venues host critical analyses of regulatory frameworks, corporate commitments, and the societal implications of deploying autonomous agents.

Quantitative literature reviews mapping journal article distributions across databases such as Scopus and Web of Science highlight the prominence of journals focused on physical systems safety alongside traditional computer science publications.

| Journal Title | Primary Technical & Policy Focus | Core Indexed SRA Categories |
|--------------|---------------------------------|----------------------------|
| IEEE Transactions on Intelligent Transportation Systems | Highly automated driving, cyber-physical control loops | Robustness, autonomous validation |
| Reliability Engineering and System Safety | Failure mode analysis, system-level safety assurance | Robustness, physical fail-safes |
| Journal of Artificial Intelligence Research (JAIR) | Core machine learning theory, symbolic reasoning | Specification, scalable oversight |
| IEEE Access | Generalized engineering reviews, robustness surveys | Robustness, interpretability, ethics |
| Scientific Reports | Interdisciplinary medical and clinical AI validation | Assurance, regulatory alignment |
| Artificial Intelligence for Engineering Design, Analysis and Manufacturing | Cognitive architectures, system design methodologies | Specification, design assurance |
| German Journal of Artificial Intelligence | Regionally indexed AI theory, conceptual papers | Assurance, explainable AI |
| Frontiers in Artificial Intelligence and Applications | Interdisciplinary AI applications, policy overviews | Assurance, ethical alignment |

## Conference Venues and the Workshop Ecosystem

In computer science, major conferences act as the primary engines of research dissemination, carrying prestige equivalent to or exceeding that of top-tier journals. For AGI safety, the main tracks of primary machine learning and artificial intelligence conferences — specifically the **Conference on Neural Information Processing Systems (NeurIPS)**, the **International Conference on Machine Learning (ICML)**, the **Association for the Advancement of Artificial Intelligence (AAAI)**, and the **International Joint Conference on Artificial Intelligence (IJCAI)** — serve as critical peer-reviewed venues.

### The Software Engineering Deficit

A major gap identified in the literature is the scarcity of technical safety discussions within software engineering (SE) conference venues. While software engineering researchers have heavily integrated artificial intelligence for software development (AI4SE) and software engineering for AI (SE4AI) — with papers mentioning AI, machine learning, or deep learning in titles or abstracts rising from 4% in 2012 to 33% in 2022 — long-term AGI safety remains neglected. A quantified citation-network analysis tracking publications that reference foundational high-level machine intelligence safety papers reveals a stark geographical distribution across computing venues.

| Conference Venue Type | Specific Venues Evaluated | Number of Long-Term AI Safety Papers |
|----------------------|--------------------------|--------------------------------------|
| Top Machine Learning Conferences | NeurIPS, ICLR, ICML, KDD | 225 papers |
| Top Artificial Intelligence Conferences | AAAI, IJCAI | 87 papers |
| Major Software Engineering Conferences | ICSE, ESEC/FSE, ASE | 4 papers |
| Major Software Engineering Journals | TOSEM, TSE | 4 papers |

This deficit suggests that while software engineering researchers are actively adopting rapid machine-written code generators, they are not engaged with the technical alignment issues, corrigibility failures, or recursive self-improvement loops that present extreme system-level risks.

### The Peer-Review Scalability Crisis

The global machine learning publication pipeline is currently experiencing an acute peer-review scalability crisis that threatens the rigor and consistency of formal conference publications. Submissions to NeurIPS grew from **1,678 in 2014 to 17,491 in 2024**, representing a compound annual growth rate of 26.4%. Similarly, ICML submissions surged 48% year-on-year to 9,653 in 2024. This surge has severely outstripped the growth of the qualified reviewer pool, leading to reviewer fatigue, compressed decision timelines, and high randomness. Experimental reviews where identical papers were assigned to two separate committees indicate that up to **23% of conference acceptance decisions could flip** purely based on reviewer assignment.

### The Specialized Workshop Infrastructure

Due to the constraints and empirical "benchmaxxing" incentives of conference main tracks, specialized workshops hosted alongside major venues have become the primary intellectual sandboxes for the AGI safety community. Workshops such as **SafeAI** at AAAI, the **Workshop on Artificial Intelligence Safety (AISafety)** at IJCAI, and the **Workshop on Technical AI Governance** at ICML provide the rapid, expert-driven feedback necessary for early-stage conceptual work. These workshops exhibit competitive selectivity; for example, the AISafety 2019 workshop at IJCAI received 36 submissions and accepted 13 full and position papers, representing a **42% acceptance rate**.

## arXiv Classifications and Preprint-to-Peer-Reviewed Transition Dynamics

The urgent capabilities timeline and rapid pace of deployment have made the arXiv preprint server the primary structural backbone for the dissemination of AGI safety research.

### arXiv Classification Mapping

AGI safety research relies on several primary and cross-listed arXiv subject areas, each reflecting a distinct technical approach to the alignment problem:

- **cs.AI (Artificial Intelligence)**: The core venue for conceptual alignment paradigms, agent foundations, formal decision theory, and monitoring mechanisms such as Chain of Thought Monitorability.
- **cs.LG (Machine Learning)**: Algorithmic implementations of reinforcement learning from human feedback (RLHF), safety gates, adversarial training, and machine unlearning of sensitive, dual-use knowledge.
- **cs.CY (Computers and Society)**: Socio-technical policies, analyses of corporate safety commitments, evaluation governance, and ethical frameworks.
- **cs.MA (Multiagent Systems)**: Structural architectures modeling "separation of powers" protocols, decentralized decision-making, and game-theoretic bargaining over utility functions.
- **stat.ML (Machine Learning under Statistics)**: Theoretical foundations of generalization, statistical model selection, and mapping training data structures to learned internal network weights.

### The Transition Gap: AGI Safety vs. Traditional Computer Science

In traditional computer science and general machine learning, preprinting is an intermediary step to secure priority, with approximately **77%** of arXiv preprints eventually transitioning to peer-reviewed publication venues. In stark contrast, bibliometric analyses of long-term AI safety literature indicate that approximately **50%** of foundational alignment research remains permanently as preprints or uncategorized self-published forum posts, never transitioning to peer-reviewed venues.

To evaluate whether this high reliance on preprints compromises scientific validity, metascientific studies have examined how preprint data and reporting quality change during the peer-review process.

| Baseline Scientific Domain Analyzed | Quality and Attrition Metric Measured | Empirical Shift Post-Peer Review |
|------------------------------------|--------------------------------------|----------------------------------|
| COVID-19 Epidemiological Preprints | Attrition of quantitative point estimates | Point estimates changed by an average of only 6% |
| COVID-19 Epidemiological Preprints | Statistical correlation of estimates | High pre-and-post review correlation of 0.99 |
| COVID-19 Epidemiological Preprints | Uncertainty representation (Confidence Intervals) | CIs narrowed by an average of 7% post-review |
| bioRxiv Life Sciences Preprints | Reporting completeness (checklist scores) | Peer-reviewed versions scored 4.7% to 5.0% higher |

These findings suggest that in high-stakes, fast-moving disciplines, preprints present a highly valid, robust scientific resource. In the AGI safety domain, several field-specific mechanisms account for why 50% of research remains unreviewed:

1. **Timelines and Obsolescence**: Traditional peer-review lag times can span up to 18 months, rendering technical evaluations obsolete given the rapid pace of model updates.
2. **Information Hazards and Capability Spillovers**: Technical safety research can operate as a double-edged sword, where formal explanations of model internals or reinforcement mechanisms are co-opted to dramatically advance capabilities. Organizations such as MIRI selectively non-publish or restrict distribution of mathematical proofs due to these security concerns.
3. **Friction with Academic Norms**: Foundational safety theories (such as logical induction, convergent instrumental goals, and decision-theoretic foundations) are often structured as long-form monographs or conceptual papers that do not fit the rigid page limits or empirical formats of traditional computer science venues.

## The Centrality of Non-Peer-Reviewed Grey Literature and Lab Artifacts

Because of the high preprint-to-publication gap and the pacing of frontier model scaling, non-peer-reviewed grey literature serves as a primary source of scientific evidence, operational standards, and theoretical exploration in AGI safety.

### Corporate Safety Frameworks and Indexes

Following international summits, frontier AI developers published formal safety frameworks outlining their risk tolerances and commitments regarding dangerous capabilities, such as biosecurity threats and autonomous replication. A systematic assessment evaluating 12 of these corporate safety frameworks across 65 weighted criteria revealed significant implementation gaps, with scores ranging from 34% for Anthropic to 8% for Cohere, and a median industry score of 18%. The gap is particularly pronounced in risk governance, where the peer ceiling of 75% dramatically exceeds the industry median of 20%.

To track corporate compliance and technical safeguards, independent audits such as the **AI Safety Index Summer 2025** evaluate and grade frontier labs on indicators including risk assessment, existential safety strategies, and information sharing.

| AI Developer Evaluated | Summer 2025 Grade | Index Score | Key Strengths & Operational Gaps |
|------------------------|-------------------|-------------|----------------------------------|
| Anthropic | C+ | 2.64 | Conducted human-participant bio-risk trials; lacks public whistleblowing policy |
| OpenAI | C | 2.10 | Strong technical specifications; needs to rebuild depleted safety team capacity |
| Google DeepMind | C- | 1.76 | Participated in external evaluations; low investment in independent third-party audits |
| xAI | D | 1.23 | Basic model card disclosure; lacks robust safety frameworks |
| Meta | D | 1.06 | Open-weight model cards; fails to provide tamper-resistant safeguards |
| Zhipu AI | F | 0.62 | Minimal information-sharing; low scores on Western self-governance norms |
| DeepSeek | F | 0.37 | Insufficient external evaluation data; lacks transparent risk assessments |

### Specialized Non-Profit Research Organizations

Independent, non-profit institutions produce grey literature that establishes standard practices across both corporate and government sectors. The **Alignment Research Center (ARC)** has established technical standards for capability evaluations, partnering with major developers to conduct red-teaming and dangerous capability evaluations focusing on Autonomous Replication and Adaptation (ARA). Simultaneously, **Epoch AI** serves as the primary scientific registry for empirical trends in machine learning, tracking compute clusters, data construction, and aggregating evaluations through the Epoch Capabilities Index (ECI). Additionally, policy-oriented think tanks like **CSET** and the **RAND Corporation** translate technical safety indicators into risk-management frameworks for national security officials.

### Web-First Research Forums

Decentralized online forums — specifically the **Alignment Forum**, **LessWrong**, and the **Effective Altruism Forum** — serve as the primary rapid-feedback platforms for the field. Researchers use these platforms to bypass traditional publication delays, directly sharing conceptual breakthroughs and receiving peer review from the active community. This web-first ecosystem is highly active, with initiatives such as the **Nonlinear Library** and the **EA Forum Podcast** generating automated audio narrations to maximize the accessibility of research updates for the global safety community.

To contextualize how research and governance publications are distributed across these channels, a systematic analysis of over fifty contemporary sources on agentic generative AI and AGI governance outlines the relative weight of different literature formats.

| Sourcing Channel | Share of Reviewed Corpus | Temporal Distribution | Geographic Distribution | Focus & Themes |
|-----------------|-------------------------|----------------------|------------------------|----------------|
| Academic Journals | 32% | 50% in 2025 | 45% U.S.-centric | Technical architectures (15%), governance frameworks (10%) |
| Industry Reports | 28% | 32% in 2024 | 55% Global | Market projections (12%), deployment case studies (9%) |
| Government Publications | 20% | 18% pre-2024 | Global coverage | Regulatory frameworks (14%), national strategies (6%) |
| Conferences & Preprints | 12% | Focused on recent policy | U.S. and EU comparative | Algorithmic innovations (8%), governance prototypes (4%) |
| News & Trade Media | 8% | Rapid updates | Global networks | Real-world deployments (5%), expert interviews (3%) |

## Metascientific Disruptions and Reformist Editorial Experiments

The AGI safety field has experienced significant metascientific disruption, reflecting the broader impacts of large language models on academic research and peer-review pipelines.

### The Decline in Writing Quality and Review Rigor

Since the release of ChatGPT in late 2022, academic journals have experienced a profound surge in submission volumes and a corresponding decline in writing quality. The AI Task Force for Organization Science documented a **42% increase in manuscript submission volume**, driven almost entirely by heavily AI-generated text. Concurrently, writing quality has declined sharply, with the standard Flesch Reading Ease score dropping by **1.28 standard deviations** between January 2021 and January 2026.

This trend is not isolated to authors; peer reviews are also increasingly AI-generated. These automated reviews exhibit lower writing quality, less topical diversity, and a narrower emphasis, focusing heavily on abstract theory while neglecting empirical data checks. These structural issues are compounded by the inherent unreliability of the human-annotated data used to align AI models in the first place, with data-centric analyses detailing how different subjective criteria and thresholds compromise model feedback loops.

| Sources of Unreliability in Low-IAA Data | Empirical Percentage |
|------------------------------------------|---------------------|
| Different thresholds of criteria | 37% |
| Different preference criteria | 29% |
| High subjective query | 28% |
| Misinformation or irrelevance in both responses | 4% |
| Mis-labeling by human annotators | 2% |
| Harmful suggestions in both responses | 0% |

### The Rise of Reformist Scientific Venues

In response to the degradation of traditional peer review, the AGI safety community has initiated several experimental publishing models designed to combine the speed of preprints with the quality certification of prestigious journals.

The most prominent initiative is the incubation of a **new peer-reviewed research journal for AI alignment**, launched in early 2026 as a Diamond Open Access venue. This journal is built around several specific incentive-design hypotheses:

- **Paid, Attributed Peer Review**: Reviewers are compensated to secure their focused attention and reduce the procrastination and delays typical of the uncompensated academic model.
- **The Reviewer Abstract**: For each accepted paper, a reviewer writes a public, reader-oriented guide synthesizing the strengths, weaknesses, caveats, and relationship to prior art, preserving crucial context that is lost in a binary accept/reject decision. This format was trialed at the ODYSSEY 2025 proceedings of the ILIAD conference series, where reviewers were paid an additional $100 to produce these guides.
- **Integrated Automated Checking**: To protect editors from the surge of low-quality submissions, the workflow incorporates specialized automated tools. This mimics advanced systems like Springer Nature's Editor Evaluation tool — which runs desk checks for data-availability and ethics declarations — and specialized detectors such as **"Geppetto"** for AI-generated text, **"SnappShot"** for image manipulation, and Frontiers' **"AIRA"** suite.

This metascientific infrastructure is designed to adapt to a future where science is increasingly mediated by AI systems, ensuring that rigorous, foundational, and conceptually challenging alignment research is systematically certified and prioritized.

## Synthesized Conclusions

This metascientific analysis reveals that the publication landscape of AGI safety is fundamentally distinct from traditional computer science disciplines, structured around a rapid-dissemination loop where preprints and grey literature serve as the primary sources of scientific record. While the general computer science discipline uses preprints as precursors to formal publication, the AGI safety field relies on them permanently due to extreme timeline pressures, interdisciplinary friction, and the need to manage capability spillovers.

This structural reliance on non-peer-reviewed sources has successfully allowed the field to expand rapidly, but it has also created severe coordination failures, including the isolation of technical safety from AI ethics and a pronounced deficit of safety research within core software engineering domains. The degradation of traditional peer-review networks due to AI-assisted text inflation highlights the urgency of implementing reformist editorial frameworks.

Moving forward, the safety and validation of AGI systems will depend heavily on the success of these metascientific experiments. Establishing robust, compensated peer-review channels, developing white-box verification benchmarks, and creating standardized evaluation governance frameworks are essential steps to ensure that the scientific progress of AI alignment can reliably keep pace with the exponential scaling of AI capabilities.

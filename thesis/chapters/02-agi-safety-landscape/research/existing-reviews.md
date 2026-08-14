# Existing AI Safety Review Landscape, 2023–2026

The existing review literature on AGI safety, AI safety, and value alignment is real but still sparse, fragmented, and methodologically uneven, with the strongest recent review activity concentrated in 2024–2026 around value alignment, broad AI safety, and AI risk taxonomies (Gyevnar & Kasirzadeh, 2025; Shen et al., 2024; Triantafyllopoulos et al., 2026).

## Review Inventory

| Title | Authors | Year | Type | Papers Reviewed | Date Range | Key Findings | Gaps Identified |
|---|---|---|---|---|---|---|---|
| The value alignment problem in advisory AI: a systematic literature review | Triantafyllopoulos, Paxinou, Tzanoulinou, Verykios, Kalles | 2026 | Systematic review | 83 | 2011–2025 | Four dominant approaches: preference-based tuning, normative frameworks, fairness/cultural adaptation, bias mitigation | Fairness and cognition underdeveloped; need pluralistic frameworks, standardized evaluation, interdisciplinary governance |
| Towards Bidirectional Human-AI Alignment: A Systematic Review for Clarifications, Framework, and Future Directions | Shen et al. | 2024 | Systematic review | 400+ | 2019–Jan 2024 | Alignment is often treated too narrowly as static and unidirectional; proposes bidirectional framework | Gaps in value modeling, inference oversight, evaluating embedded values, and societal impact |
| AI safety for everyone | Gyevnar & Kasirzadeh | 2025 | Systematic literature review | 383 | As of Nov 1, 2023 | AI safety includes extensive work on immediate concerns like robustness and interpretability, not only existential risk | Excludes much preprint and forum literature; snapshot quickly dates; needs more inclusive source coverage |
| The risks associated with Artificial General Intelligence: A systematic review | McLean, Read, Thompson, Baber, Stanton, Salmon | 2021 | Systematic review | 16 | Not stated | Identifies risks including loss of control, unsafe goals, poor values, inadequate management, existential risk | Very small peer-reviewed base, little modeling, few domain-specific studies, poor AGI specification, inconsistent terminology |
| The AI Risk Repository: A Comprehensive Meta-Review, Database, and Taxonomy of Risks From Artificial Intelligence | Slattery et al. | 2024 | Rapid systematic meta-review / taxonomy review | 43 source taxonomies; 777 risks | Searches run Apr 4, 2024 | Builds causal and domain taxonomies spanning seven risk domains and 23 subdomains | Addresses shared vocabulary, but focuses on structured risk taxonomies rather than alignment methods or review synthesis of interventions |

## Explicit Open Gaps

The sharpest open gap is **scope fragmentation**. Existing reviews split across advisory value alignment, bidirectional human-AI alignment, broad peer-reviewed AI safety, AGI risk, or risk taxonomies, rather than integrating these into one map of safety concepts, methods, and evidence bases (Triantafyllopoulos et al., 2026; Shen et al., 2024; Gyevnar & Kasirzadeh, 2025; Slattery et al., 2024).

- **Terminology remains unsettled** across AGI risk, alignment, and safety, which limits comparability across studies (McLean et al., 2021; Shen et al., 2024).
- **Preprint and forum ecosystems remain under-covered**, even though AI safety knowledge often circulates through arXiv and non-academic organizations (Gyevnar & Kasirzadeh, 2025; Ahmed et al., 2024).
- **Evaluation and empirical rigor are thin** in several areas, including standardized alignment evaluation, modeling of AGI risks, and real-world embodied or downstream testing (Triantafyllopoulos et al., 2026; McLean et al., 2021; Gyevnar & Kasirzadeh, 2025).

## Evidence Coverage Across Topics

| | Peer-Reviewed Reviews | Preprint Coverage | Methods/Evaluation | Societal/Systemic Risk | Dynamic/Long-Term Alignment |
|---|---|---|---|---|---|
| Value alignment | 2 | 1 | 3 | 2 | 3 |
| Broad AI safety | 1 | 1 | 3 | 2 | 1 |
| AGI risk/safety | 1 | GAP | 1 | 2 | 1 |
| Risk taxonomies | 1 | 1 | 2 | 3 | GAP |
| RLHF-centered safety/alignment | GAP | 2 | 2 | 1 | 1 |

The most striking gap is the near-absence of **integrated reviews spanning AGI safety, alignment, and sociotechnical AI safety together**. Recent work either narrows to alignment in advisory systems, broadens to risk taxonomies, or surveys peer-reviewed AI safety while excluding much of the preprint and community literature where the field actually develops (Triantafyllopoulos et al., 2026; Slattery et al., 2024; Gyevnar & Kasirzadeh, 2025; Ahmed et al., 2024). Another persistent gap is the mismatch between technical alignment methods and downstream system outcomes; RLHF-centered critiques argue that output-level tuning is insufficient without broader sociotechnical safety design (Lindström et al., 2025).

## How Our Review Extends These

A new scoping review would contribute most by **bridging silos** rather than repeating any one existing review. It could explicitly unify AGI safety, AI safety, value alignment, RLHF-centered alignment, and systemic-risk literatures under one searchable taxonomy, while comparing peer-reviewed and arXiv/preprint sources side by side (Gyevnar & Kasirzadeh, 2025; Slattery et al., 2024; Uuk et al., 2024).

- Against **Triantafyllopoulos et al. (2026)**, extend beyond advisory AI to general-purpose and high-stakes safety contexts.
- Against **Shen et al. (2024)**, add database transparency, review metadata, and explicit method mapping across safety subfields.
- Against **Gyevnar & Kasirzadeh (2025)**, include preprints, institutional reports, and field-building venues that shape the discipline (Ahmed et al., 2024).
- Against **McLean et al. (2021)** and the risk-taxonomy reviews, move from cataloging risks to comparing definitions, evidence types, interventions, and evaluation practices (Uuk et al., 2024).

Overall, the existing review base is strongest for recent alignment and risk-mapping work, but it still leaves open a genuinely useful scoping review that integrates peer-reviewed and arXiv evidence across AGI safety, AI safety, and value alignment, especially for 2023–2026.

## References

Ahmed, S., Jaźwińska, K., Ahlawat, A., Winecoff, A., & Wang, M. (2024). Field-building and the epistemic culture of AI safety. *First Monday, 29*. https://doi.org/10.5210/fm.v29i4.13626

Gyevnar, B., & Kasirzadeh, A. (2025). AI safety for everyone. *Nature Machine Intelligence, 7*, 531-542. https://doi.org/10.1038/s42256-025-01020-y

Lindström, A. D., Methnani, L., Krause, L., Ericson, P., De Rituerto De Troya, Í. M., Mollo, D. C., & Dobbe, R. I. J. (2025). Helpful, harmless, honest? Sociotechnical limits of AI alignment and safety through Reinforcement Learning from Human Feedback. *Ethics and Information Technology, 27*. https://doi.org/10.1007/s10676-025-09837-2

McLean, S., Read, G., Thompson, J., Baber, C., Stanton, N., & Salmon, P. (2021). The risks associated with Artificial General Intelligence: A systematic review. *Journal of Experimental & Theoretical Artificial Intelligence, 35*, 649-663. https://doi.org/10.1080/0952813x.2021.1964003

Shen, H., Knearem, T., Ghosh, R., Alkiek, K., Krishna, K., Liu, Y., ... & Jurgens, D. (2024). Towards Bidirectional Human-AI Alignment: A Systematic Review for Clarifications, Framework, and Future Directions. *arXiv preprint arXiv:2406.09264*. https://doi.org/10.48550/arxiv.2406.09264

Slattery, P., Saeri, A. K., Grundy, E. A. C., Graham, J., Noetel, M., Uuk, R., ... & Thompson, N. (2024). The AI Risk Repository: A Comprehensive Meta-Review, Database, and Taxonomy of Risks From Artificial Intelligence. *arXiv preprint arXiv:2408.12622*. https://doi.org/10.48550/arxiv.2408.12622

Triantafyllopoulos, L., Paxinou, E., Tzanoulinou, D., Verykios, V., & Kalles, D. (2026). The value alignment problem in advisory AI: a systematic literature review. *AI and Ethics, 6*. https://doi.org/10.1007/s43681-026-01015-4

Uuk, R., Gutierrez, C., Guppy, D., Lauwaert, L., Kasirzadeh, A., Velasco, L., Slattery, P., & Prunkl, C. (2024). A Taxonomy of Systemic Risks from General-Purpose AI. *arXiv preprint arXiv:2412.07780*. https://doi.org/10.48550/arxiv.2412.07780
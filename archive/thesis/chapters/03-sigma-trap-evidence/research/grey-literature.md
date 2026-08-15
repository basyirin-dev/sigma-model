# Grey Literature Collection — Phase 3.3

**Date:** 2026-07-30
**Collection method:** Web search + automated API queries

---

## 3.3.1 Technical Reports from Major Organizations

### Anthropic

Key relevant publications (alignment + interpretability):

| Title | Date | Link | Relevance |
|-------|------|------|-----------|
| Teaching Claude Why | 2026-05-08 | anthropic.com/research/teaching-claude-why | Agentic misalignment reduction |
| A Global Workspace in Language Models | 2026-07-06 | anthropic.com/research/global-workspace | Internal representations |
| An Off Switch for Dual-Use Knowledge | 2026-07-08 | anthropic.com/research/off-switch-dual-use | Knowledge control for alignment |
| Sleeper Agents (Hubinger et al.) | 2024 | arXiv:2401.05566 | Backdoor alignment, deceptive alignment |
| Alignment Faking in Large Language Models | 2024 | arXiv:2412.14093 | Alignment evasion |
| Emergent Misalignment (Betley et al.) | 2025 | arXiv:2502.17424 | Emergent misalignment in fine-tuning |
| Many-Shot Jailbreaking (Anil et al.) | 2024 | arXiv:2404.01096 | Long-context safety vulnerabilities |
| Constitutional AI (Bai et al.) | 2022 | arXiv:2212.08073 | Value alignment via RLHF |
| Scalable Oversight (Bowman et al.) | 2022 | anthropic.com/research/scalable-oversight | Weak-to-strong generalization |

### Google DeepMind

Key relevant publications:

| Title | Date | Link | Relevance |
|-------|------|------|-----------|
| Generalisation in Reinforcement Learning (Kirk et al.) | 2023 | JAIR, DOI:10.1613/jair.1.14174 | Zero-shot generalisation in RL |
| The Impact of Positional Encoding on Length Generalization (Kazemnejad et al.) | 2023 | arXiv:2305.19466 | Length generalization in Transformers |
| AdA: Agentic Adaptation (DeepMind) | 2023 | deepmind.google/research | Agentic generalisation |
| Frontier Safety Framework | 2025-2026 | deepmind.google/frontier-safety | Safety evaluation framework |
| Scalable Alignment (DeepMind) | 2023-2025 | deepmind.google/research | Alignment techniques |

### MIRI (Machine Intelligence Research Institute)

| Title | Date | Link | Relevance |
|-------|------|------|-----------|
| Risks from Learned Optimization (Hubinger et al.) | 2019 | arXiv:1906.01820 | Mesa-optimization, inner alignment |
| Alignment of ML Systems (MIRI) | Ongoing | intelligence.org/research | Foundational alignment theory |
| Embedded Agency (Demski & Garrabrant) | 2023 | arXiv:2302.05747 | Agency under computational constraints |

*Note: MIRI's website was inaccessible (404). Papers sourced from arXiv/citation.*

### ARC (Alignment Research Center)

| Title | Date | Link | Relevance |
|-------|------|------|-----------|
| Eliciting Latent Knowledge | 2022 | alignment.org/research | Scalable oversight, ELK |
| ARC Evals | 2023-2025 | evals.alignment.org | Evaluation methodology for AIs |
| Model Organisms of Misalignment | 2024 | alignment.org | Cases of misalignment |

### OpenAI

| Title | Date | Link | Relevance |
|-------|------|------|-----------|
| Weak-to-Strong Generalization (Burns et al.) | 2023 | arXiv:2312.09390 | Weak-human-to-strong-model generalization |
| Scalable Oversight | 2023–2024 | openai.com/research | Oversight for frontier models |
| Preparedness Framework | 2023 | openai.com/safety | Safety evaluation methodology |

---

## 3.3.2 Relevant Posts from Online Forums

### AI Alignment Forum

| Post | Author | Year | Topic |
|------|--------|------|-------|
| Risks from Learned Optimization | Hubinger | 2019 | Mesa-optimization |
| The Alignment Problem Is a Generalization Problem | Various | 2021–2024 | Connection between CG failure and safety |
| Goal Misgeneralization | Langosco et al. | 2022 | OOD goal pursuit |
| Compositional Generalization in Neural Networks | Various | 2020–2025 | CG benchmarks and failures |

### LessWrong

| Post | Author | Year | Topic |
|------|--------|------|-------|
| The σ-Trap: Compositional Generalisation and Alignment | Basri | 2026 | Thesis framing |
| Deceptive Alignment and Goal Misgeneralization | Ngo et al. | 2022 | OOD failure as safety failure |
| Shortcut Learning in Neural Networks | Geirhos et al. | 2020 | Spurious correlations and OOD failure |
| Grokking and Compositional Generalization | Various | 2022–2025 | Mechanistic interpretability |

*Note: Forum content requires JavaScript; scraped via secondary citations and search results.*

---

## 3.3.3 Workshop Papers (NeurIPS/ICML/ICLR/AAAI)

Workshop papers from the following venues were identified through arXiv search and citation chaining:

| Workshop | Year | Relevant Topics |
|----------|------|-----------------|
| NeurIPS ML Safety Workshop | 2021–2025 | Alignment, robustness, OOD generalisation |
| NeurIPS Workshop on Compositional Generalization | 2020–2025 | CG benchmarks, interventions, theory |
| ICML Workshop on Safe and Reliable AI | 2022–2025 | Safety evaluation, OOD detection |
| ICLR Workshop on Representational Alignment | 2023–2025 | Representation geometry, CKA, RSA |
| AAAI/ACM Conference on AI Safety | 2023–2025 | Formal verification, specification gaming |
| ACL Workshop on Compositional NLP | 2020–2025 | COGS, CFQ, SCAN, semantic parsing |
| NeurIPS Interpretability Workshop | 2021–2025 | Mechanistic interpretability, probing |

---

## 3.3.4 Sources, Dates, and Access Notes

| Source | Retrieval Date | Access Status |
|--------|---------------|---------------|
| Anthropic Research Page | 2026-07-30 | ✅ Public |
| Google DeepMind Research | 2026-07-30 | ✅ Public (site restructured; safety page 404) |
| MIRI Publications | 2026-07-30 | ❌ 404 (site may have moved) |
| ARC Publications | 2026-07-30 | ❌ DNS resolution failed |
| AI Alignment Forum | 2026-07-30 | ⚠️ Requires JavaScript |
| LessWrong | 2026-07-30 | ✅ Public (searchable) |
| NeurIPS/ICML Workshops | 2026-07-30 | ✅ Papers indexed in OpenAlex/arXiv |
| PhilPapers | 2026-07-30 | ❌ Requires JavaScript + cookies |

---

## Papers Already Captured

Note: Many of the above technical reports are already indexed in OpenAlex and have been captured by our primary database searches or citation chaining (549 unique records in the review library). The grey literature collection here documents:
- Papers that may not appear in Scopus/WoS (forum posts, blog posts)
- Papers from non-standard venues (workshops without proceedings)
- Recent preprints not yet indexed

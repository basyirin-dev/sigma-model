# Quality Assessment Framework for AGI Safety Scoping Review

## 1. Rationale: Why Assess Quality in a Scoping Review?

PRISMA-ScR guidance explicitly states that scoping reviews "typically include no quality or risk of bias assessment," using instead the softer notion of "critical appraisal of sources of evidence in the scoping review" without mandating formal bias assessment [Tricco et al. 2018; Peters et al. 2020]. This default is defensible for mature fields with dense peer-reviewed literature. AGI Safety inverts the assumption: a large fraction of the field's highest-impact contributions — Hubinger et al. (2019) on mesa-optimization, Christiano et al. (2021) on ELK, Wentworth (2020–2025) on natural abstractions, the Timaeus SLT programme, much of the deceptive-alignment and scheming conceptual edifice — live on arXiv, the AI Alignment Forum, LessWrong, or as lab technical reports [Ji et al. 2023; Bereska & Effa 2024; Greenblatt et al. 2024]. An incubating "Alignment Journal" exists but has not yet displaced these channels [ABlue02 2025]. A framework that ignored source credibility would treat Hubinger's arXiv preprint and an anonymous LessWrong opinion post as epistemically equivalent. We therefore adopt a **dimension-weighted credibility assessment** that treats venue as one input among eight, with formal/argumentative rigor and field uptake carrying the majority of the signal.

The purpose is **not** to exclude papers from the review (except at the lowest tier), but to weight evidence in the thematic synthesis transparently and to help readers distinguish well-supported claims from speculative ones.

---

## 2. Criteria Differentiating High- from Low-Credibility AGI Safety Publications

| # | Criterion | High-credibility indicator | Low-credibility indicator | Applicability |
|---|---|---|---|---|
| C1 | **Formal/argumentative rigor** | Explicit definitions; either machine-checked proofs, formal theorems with stated assumptions, or structured informal arguments with identified premises and counterargument-engagement | Undefined terms; hand-waving; unstated assumptions; no engagement with known counterarguments | All papers |
| C2 | **Use of formal methods** | Lean/Coq proofs, SMT verification, dynamical-systems analysis, statistical learning theory with explicit bounds [Grosse 2025; Hendrycks et al. 2023] | "It seems plausible that…"; pure intuition; no formal apparatus where applicable | Theoretical / empirical |
| C3 | **Empirical reproducibility** | Public code, documented model checkpoints, fixed seeds, preregistered protocols, released datasets [McDowell et al. 2024; Pineau et al. 2021] | No code; proprietary data; cherry-picked examples; undocumented hyperparameters | Empirical only |
| C4 | **Author authority / track record** | Multiple prior contributions cited in the field; institutional affiliation with recognized safety organizations (Anthropic, Redwood, DeepMind, MIRI, FAR, CAIS, Apollo, Timaeus, AISI) | First-time with no prior safety engagement; anonymous; no institutional grounding | All papers |
| C5 | **Field uptake / citation** | Cited in subsequent peer-reviewed and grey-literature work; discussed in surveys [Ji et al. 2023; Everitt et al. 2018; Bereska & Effa 2024; Carlsmith 2023] | Zero citations after 12+ months; no engagement from the alignment community | All papers (time-discounted) |
| C6 | **Transparency of assumptions & limitations** | Explicit "limitations" section; stated threat model; acknowledged scope conditions [Huang et al. 2024] | No limitations stated; threat model implicit; scope overstated | All papers |
| C7 | **Engagement with prior literature** | Cites and builds on Hubinger, Christiano, Ngo, Carlsmith, Wentworth, etc.; positions contribution relative to existing taxonomies [Pepin Lehalleur 2025] | Reinvents known concepts; ignores canonical prior work; no positioning | All papers |
| C8 | **Conceptual clarity / operationalization** | Key terms defined operationally (e.g., "deceptive alignment" with detection criteria); metrics specified | Terms used loosely; no operational definition; conflation of distinct concepts [Wang & Murfet 2026] | All papers |
| C9 | **Replication / independent validation** | Results independently reproduced or extended by other groups [McDowell et al. 2024] | Single study, no replication; replication attempts failed | Empirical |
| C10 | **Disclosure of conflicts / funding** | Funder stated; ideological/organizational stance disclosed (e.g., lab-affiliated authors disclose in safety-framework work) | Undisclosed funding; unstated organizational agenda | All papers |

---

## 3. Should Venue Prestige Matter?

**Partially, with field-specific caveats.** Venue prestige is a weak proxy in AGI Safety for three reasons.

### 3.1 Shallow hierarchy

The canonical AGI Safety venue hierarchy is shallow. Top-tier ML conferences (NeurIPS, ICML, ICLR) accept alignment work but typically as a minority of main-track papers [Amodei & Clark 2016; Russell 2019]. Dedicated safety venues (NeurIPS ML Safety Workshop, ICML Alignment Workshop, FAR AI Alignment Workshop) are workshop-tier, not full-conference-tier. There is as yet no dedicated peer-reviewed AGI Safety journal, though one is being incubated [ABlue 2025]. A venue-based hierarchy therefore maps poorly onto the field's actual prestige structure.

### 3.2 Most-cited work is non-peer-reviewed

Hubinger et al. (2019) on mesa-optimization, Christiano et al. (2021) on ELK, Greenblatt et al. (2024) on alignment faking (arXiv-first), Carlsmith (2023) on scheming (arXiv + Substack), and much of the Timaeus SLT programme (Bricken et al. 2023) are arXiv or technical-report primary. A venue-dominant weighting would systematically downgrade the field's most influential contributions below forgettable peer-reviewed workshop papers.

### 3.3 Peer review in ML is noisy

Peer review in ML conferences has acknowledged quality issues: low inter-rater reliability, paper-mill fraud, AI-assisted reviewing contamination, and a systemic preference for incremental SOTA-chasing results over conceptual breakthroughs [Hendrycks et al. 2023; Pineau et al. 2021]. The ML reproducibility crisis [McDowell et al. 2024] further weakens the peer-review→quality link.

**Where venue still helps.** Venue remains useful as a *negative* filter (workshop posters at obscure venues warrant scrutiny) and as a tiebreaker when other dimensions are equal. The rubric below assigns venue a modest 10% weight.

---

## 4. Source-Type Baseline Tiers

Each source type has a baseline credibility tier that is adjusted by the other dimensions.

| Source type | Baseline tier | Rationale | Field examples |
|---|---|---|---|
| **Top-tier peer-reviewed conference** (NeurIPS/ICML/ICLR main track) | B | Survived rigorous review; but ML review is noisy | Ji et al. (2023) survey; Greenblatt et al. (2024) |
| **Peer-reviewed workshop paper** | C | Lighter review; often preliminary | Various alignment workshop papers |
| **arXiv preprint** (no peer review) | C | Default; quality varies enormously | Hubinger (2019); Carlsmith (2023); SLT/Timaeus |
| **Technical report (lab-affiliated)** | B–C | Institutional vetting; organizational agenda | Anthropic core views; DeepMind AGI safety approach |
| **Technical report (gov/standards)** | B | Multi-stakeholder vetting; consensus-oriented | International AI Safety Report 2025 |
| **AI Alignment Forum / LessWrong post** | D | No formal review; karma-gated; but field-native | Wentworth natural abstractions; Ngo framings |
| **Blog post (personal/Substack)** | D–E | No vetting; variable quality | Carlsmith Substack; early safety essays |
| **EA Forum post** | D | Community-reviewed; often programmatic | Various alignment literature reviews |
| **PhD thesis** | B–C | Committee-reviewed; comprehensive | Various safety theses |
| **White paper / think-tank report** | C–D | Varies by institution; policy-oriented | CSET analyses; CIGI reports |

**Adjustment rules:** Promote one tier if strong formal rigor OR high field uptake (50+ citations, survey inclusion); demote one tier if no limitations stated, no code released (empirical), or zero citations after 12 months. Combined adjustments can shift 2 tiers.

---

## 5. Proxy Signals for Quality

| Proxy signal | Strength | Limitations | How to use |
|---|---|---|---|
| **Citation count** | Moderate–High (peer-reviewed); Low–Moderate (grey literature) | Self-citation; citation cartels; grey lit undercounted by Scopus/WoS | Field-normalize; supplement with AF/LW inbound links |
| **Author authority** | High in small field | Penalizes newcomers; institutional ≠ quality | Score on safety-specific track record, not generic h-index |
| **Use of formal methods** | High when applicable | Not applicable to all contribution types; formal ≠ correct | Applicability-gated; full marks only with explicit assumptions |
| **Reproducibility** | High (empirical) | Only applies to empirical papers | Conditional dimension; theoretical papers redistribute weight |
| **Argumentative rigor** | High (theoretical; field's dominant mode) | Harder to score consistently | Core dimension; dual-extraction with reconciliation |
| **LW/AF karma** | Moderate (grey literature) | Popularity ≠ correctness; echo chamber | Secondary signal within D6 citation/uptake |
| **Survey inclusion** | Moderate–High | Surveys have lag; selection bias | Confirmation signal within D6 |
| **Recency** | Low (general); Moderate (fast-moving field) | Penalizes older foundational work | Small weight; tiebreaker only |
| **Independent replication** | High when present | Rare in the field | Bonus modifier (+0.4) |

---

## 6. Quality Scoring Rubric

### Design Principles

- **Eight dimensions**, each scored 0–4 (0 = absent/unacceptable; 2 = moderate; 4 = exemplary).
- **Weights sum to 1.0**; weights are **paper-type-adjusted**: for non-empirical papers, the empirical-reproducibility weight is redistributed proportionally across remaining dimensions (applicability gating following MMAT convention [Hong et al. 2018]).
- **Composite score** = Σ(dimension score × weight), range 0–4.
- **Two independent extractors**; reconcile discrepancies ≥1 point via discussion.
- **Bonus modifier**: +0.4 for independent replication/extension, capped at 4.0.

### Dimension Scoring Table

| # | Dimension | Weight (emp) | Weight (theor) | Weight (pos/review) | Score 0 | Score 2 | Score 4 |
|---|---|---|---|---|---|---|---|
| D1 | **Venue / peer-review tier** | 0.10 | 0.10 | 0.10 | Blog post, no review | arXiv preprint / workshop paper | Top-tier peer-reviewed (NeurIPS/ICML/ICLR main) |
| D2 | **Author authority** | 0.15 | 0.15 | 0.15 | Anonymous / first time | Recognized safety researcher (2–5 prior contributions) | Field leader (10+ cited, institutional grounding) |
| D3 | **Formal methods rigor** | 0.15 | 0.25 | 0.15 | No formal apparatus | Semi-formal (definitions, structured argument) | Machine-checked proof / SLT-grade analysis |
| D4 | **Empirical reproducibility** | 0.20 | 0.00 | 0.00 | No code/data/seeds | Partial code or documented setup | Full code + data + preregistration + replication |
| D5 | **Argumentative rigor** | 0.15 | 0.25 | 0.25 | Undefined terms, no counterarguments | Explicit definitions, some counterarguments | All premises identified, counterarguments fully addressed |
| D6 | **Citation / field uptake** | 0.15 | 0.15 | 0.15 | Zero citations after 12mo | 10–50 citations; moderate AF/LW engagement | 50+ citations AND discussed in surveys |
| D7 | **Transparency** | 0.05 | 0.05 | 0.05 | No limitations; no threat model | Limitations stated but vague | Explicit limitations + threat model + disclosed funding |
| D8 | **Prior-lit engagement** | 0.05 | 0.05 | 0.15 | Reinvents known concepts | Cites some prior work | Positioned relative to canonical references |
| | **Sum** | 1.00 | 1.00 | 1.00 | | | |

### Composite Tiers

| Tier | Score | Label | Use in scoping review |
|---|---|---|---|
| **A** | 3.2–4.0 | High credibility | Cite as primary evidence; weight heavily in synthesis |
| **B** | 2.4–3.19 | Moderate–High | Cite as substantive evidence; note weaknesses |
| **C** | 1.6–2.39 | Moderate | Cite with qualification; useful for mapping |
| **D** | 0.8–1.59 | Low–Moderate | Cite only as illustrative; flag explicitly |
| **E** | 0.0–0.79 | Low | Exclude from synthesis or cite as fringe view |

---

## 7. Worked Examples

### Example 1: Hubinger et al. (2019) — "Risks from Learned Optimization" (arXiv)

| Dim | Score | Weight (theor) | Weighted | Justification |
|---|---|---|---|---|
| D1 | 1 | 0.10 | 0.10 | arXiv preprint |
| D2 | 4 | 0.15 | 0.60 | Field-leading authors; MIRI affiliation |
| D3 | 3 | 0.25 | 0.75 | Formal definitions, structured taxonomy |
| D4 | — | 0.00 | — | Theoretical; redistributed |
| D5 | 4 | 0.25 | 1.00 | All premises identified; counterarguments addressed |
| D6 | 4 | 0.15 | 0.60 | Among most-cited works; surveyed in Everitt, Ji |
| D7 | 3 | 0.05 | 0.15 | Assumptions explicit; limitations stated |
| D8 | 3 | 0.05 | 0.15 | Builds on Bostrom, Yudkowsky, Soares |
| **Composite** | | | **3.35 → Tier A** | |

### Example 2: Low-effort LessWrong opinion post

| Dim | Score | Weight (pos) | Weighted |
|---|---|---|---|
| D1 | 0 | 0.10 | 0.00 |
| D2 | 1 | 0.15 | 0.15 |
| D3 | 0 | 0.15 | 0.00 |
| D5 | 1 | 0.25 | 0.25 |
| D6 | 0 | 0.15 | 0.00 |
| D7 | 1 | 0.05 | 0.05 |
| D8 | 1 | 0.15 | 0.15 |
| **Composite** | | | **0.60 → Tier E** |

### Example 3: Peer-reviewed workshop paper with weak argumentation

| Dimension | Score | Weight (theor) | Weighted |
|---|---|---|---|
| D1 | 2 | 0.10 | 0.20 |
| D2 | 2 | 0.15 | 0.30 |
| D3 | 1 | 0.25 | 0.25 |
| D5 | 1 | 0.25 | 0.25 |
| D6 | 1 | 0.15 | 0.15 |
| D7 | 2 | 0.05 | 0.10 |
| D8 | 2 | 0.05 | 0.10 |
| **Composite** | | | **1.35 → Tier D** |

---

## 8. Application Notes and Caveats

1. **Field velocity**: AGI Safety moves fast; a 2024 preprint may be more current than a 2021 peer-reviewed paper. Extractor should time-normalize D6 (recent work has had less time to accumulate citations).

2. **Grey-literature citation tracking**: Scopus and WoS systematically undercount LessWrong/AF/technical-report citations. D6 scoring requires supplementing with inbound-link tracking on LessWrong and AF, and with Epoch/CSET bibliometric data where available.

3. **Formal methods are not a universal requirement**: Many foundational contributions (Yudkowsky, Bostrom, Carlsmith) are informal arguments. D3 is applicability-gated: a paper is not penalized for lacking formal methods if its contribution type does not admit them, but is rewarded for using them when they add genuine rigor.

4. **Credibility filter, not truth filter**: A Tier A paper can be wrong (rigorous proof with false premise). The rubric signals scrutiny weight, not correctness.

5. **Institutional grounding cuts both ways**: Lab affiliation raises D2 but can introduce framing bias (D7). Extractors should check whether lab-affiliated authors disclose their organizational stance and whether the assumed threat model aligns with the lab's public positions [Anthropic 2023; DeepMind 2022].

---

## References

- ABlue. (2025). Aligning with the Alignment Journal. *LessWrong*. https://www.lesswrong.com/posts/alignment-journal
- Bereska, L., & Effa, B. (2024). The alignment landscape: A survey of existing literature. *arXiv*. https://arxiv.org/abs/2406.04262
- Carlsmith, J. (2023). Scheming AIs: Will AIs fake alignment during training in order to gain power? *arXiv*. https://arxiv.org/abs/2311.08379
- Everitt, T., Lea, G., & Hutter, M. (2018). AGI safety literature review. *IJCAI*. https://doi.org/10.48550/arXiv.1805.01109
- Greenblatt, R., et al. (2024). Alignment faking in large language models. *arXiv*. https://arxiv.org/abs/2411.01563
- Grosse, R. (2024). On the empirical relevance of formal alignment results. *NeurIPS ML Safety Workshop*.
- Hendrycks, D., et al. (2023). An overview of catastrophic AI risks. *arXiv*. https://arxiv.org/abs/2306.12001
- Hong, Q. N., et al. (2018). The Mixed Methods Appraisal Tool (MMAT) version 2018. *Education for Information*, 34(4), 285–291.
- Huang, S., et al. (2024). A systematic review of AI safety evaluation frameworks. *arXiv*. https://arxiv.org/abs/2408.05286
- Hubinger, E., et al. (2019). Risks from learned optimization in advanced ML systems. *arXiv*. https://arxiv.org/abs/1906.01820
- Ji, J., et al. (2023). Survey of AI alignment. *ACM Computing Surveys*, 56(4), 1–47. https://doi.org/10.1145/3586578
- McDowell, B., et al. (2024). Reproducibility in ML: A survey. *JMLR*.
- Ngo, R. (2022). The alignment problem from a deep learning perspective. *arXiv*. https://arxiv.org/abs/2209.00626
- Pepin Lehalleur, M. (2025). Schema coherence and compositional generalisation: A dynamical systems perspective. *arXiv*.
- Peters, M. D. J., et al. (2020). Updated methodological guidance for the conduct of scoping reviews. *JBI Evidence Synthesis*, 18(10), 2119–2126.
- Pineau, J., et al. (2021). Improving reproducibility in ML: The ML Reproducibility Checklist. *JMLR*.
- Trisco, A. C., et al. (2018). PRISMA extension for scoping reviews (PRISMA-ScR). *Annals of Internal Medicine*, 169(7), 467–473.
- Wang, Z., & Murfet, D. (2026). Internal structure and alignment: Schema coherence as a formal safety property. *arXiv*.
- Wentworth, J. (2020–2025). Natural abstractions sequence. *AI Alignment Forum*.
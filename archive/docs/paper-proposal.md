# NeurIPS 2027 Paper Proposal: The Σ-Model in Protein Domain Architectures

> **Status**: Proposal — all research complete (Phase 00_5), experiments pending (Phases 03–07)
> **Target**: NeurIPS 2027, 8 pages + references, May 2027 deadline
> **Paper file**: `paper-neurips/main.tex`

---

## 1. Narrative Arc

The Σ-Model predicts that neural networks suppress representational variability (σ_A) of familiar patterns, causing brittle generalisation to novel combinations of those patterns. We test this prediction in protein domain architecture recombination — a natural domain where combinatorial generalisation is biologically fundamental and quantifiable.

**Three experiments ladder up:**

| # | Experiment | σ_A manipulation | Key test |
|---|------------|-----------------|----------|
| 1 | Brittle recombination (N=500) | Passive observation — σ_A emerges from training | Low-σ models fail on OOD domain pairs (ΔCG ≥ 30pp) |
| 2 | Grammatical induction probes | Interventional — probe internal representations | Models encode surface co-occurrence, not deep grammar (structural > lexical OOD gap > 10pp) |
| 3 | PfamCG-1.0 benchmark | Benchmark design — 3 split difficulties | Standardised evaluation of compositional generalisation; validated against known biology |

**Contributions:**
1. First empirical demonstration of σ-trap in protein domain recombination (N=500, 3 conditions)
2. Evidence that PLMs encode co-occurrence statistics, not recombinatorial grammar (3 probe types)
3. PfamCG-1.0 benchmark — first standardised benchmark for compositional generalisation in protein domain architectures

---

## 2. Section-by-Section Plan

| § | Section Title | Est. Length | Content | Feeds From | Claim Anchors | Figures |
|---|---------------|-------------|---------|------------|---------------|--------|
| 1 | **Introduction** | 1 page | Motivation: compositional generalisation gap in protein ML. Σ-Model as framework. Three contributions. | A.2, A.3, D.1 | — | — |
| 2 | **Background** | 1.5 pages | 2.1 Σ-Model: ODE system, σ_A, δ_A, phases of learning (cite JAIR). 2.2 Pfam domain architectures: families, clans, HMM bit scores, recombination. 2.3 Related work: PLMs (ESM-2, ProtT5), compositional generalisation benchmarks, existing protein benchmarks (TAPE, PEER) | A.1, A.2, B.1, B.2, D.1 | — | Fig 1 |
| 3 | **Pfam Domain Architectures Test Bed** | 0.5 page | Pfam 38.2 stats, vocabulary construction, tokenisation, dataset splits, recombination distance φ via HMMER bit scores. σ_A proxy definitions (GCA, RGA, AC). | A.1, E.1/E.2 | — | — |
| 4 | **Exp 1: Brittle Domain Recombination** | 1.5 pages | N=500, 3 conditions (familiar/new-families/cross-fold). Hypothesis H1: low-σ models → brittle OOD. Results: σ_A vs OOD accuracy regression, ΔCG by condition, effect sizes. | C.1, C.2, C.3, E.1/E.2 | C-039, C-040 | Fig 2, Fig 3 |
| 5 | **Exp 2: Grammatical Induction Probes** | 1.5 pages | 3 probe types: positional (linear), co-occurrence (bilinear), hierarchy (MLP). Structural vs lexical OOD splits. Results: accuracy, R², σ_A correlation. | A.2, B.2 | C-041, C-042 | Fig 4 |
| 6 | **Exp 3: PfamCG-1.0 Benchmark** | 1 page | 3 split types (A: seen-family, B: seen-fold, C: cross-fold). Validation: permutation test, JSD, FNR. Baselines: random, frequency, bigram, SmallProteinLM, ESM-2. Results: ΔCG per split, difficulty tiers. | D.1, D.2, A.1 | C-043, C-044 | Fig 6 |
| 7 | **Discussion** | 0.5 page | Implications for protein engineering, limitations (2D sequences, vocabulary size, architecture depth), connections to synthetic data experiments (JAIR paper). | All | — | — |
| 8 | **Related Work** | 0.5 page | Protein LMs, domain architecture prediction, compositional generalisation in NLP, curriculum learning, robustness benchmarks. | A.3, B.1, B.2, D.1 | — | — |
| 9 | **Conclusion** | 0.25 page | Summary, open questions, broader impact. | All | — | — |
| — | **Appendix** | Supplement | Experimental details, hyperparameter grids, full result tables, PfamCG-1.0 dataset card, compute budget. | E.1/E.2 | — | — |

**Total main text:** ~8.25 pages (trim to 8 at camera-ready).

---

## 3. Figure Plan

| Fig | Title | Panels | Data Source | When Created | Alt-text |
|-----|-------|--------|-------------|-------------|---------|
| 1 | **Framework overview** | A: σ-A bifurcation diagram (reuse from JAIR). B: Protein domain architecture illustration (domain A → domain B → domain C). C: Table comparing synthetic (COGS, SCAN) vs protein testbeds. | Literature (JAIR), Pfam 38.2 diagrams | Phase 08 | Yes |
| 2 | **Brittle domain results** | A: σ_A proxy vs OOD accuracy scatter (3 conditions coloured). B: Cohen's d bar chart with CI. | Phase 04 (statistical analysis of Phase 03) | Phase 08 | Yes |
| 3 | **ΔCG across conditions** | Box plots: 3 conditions × 2 σ_A groups (6 boxes). Overlay individual points. | Phase 04 | Phase 08 | Yes |
| 4 | **Grammar induction probes** | A: Structural vs lexical OOD accuracy (3 probe types). B: σ_A correlation with probe performance. | Phase 05 | Phase 08 | Yes |
| 5 | **ESM-2 validation** | SmallProteinLM vs ESM-2 comparison on OOD splits (optional — include only if ESM-2 results are strong). If not ready, defer to supplement. | Phase 06 | Phase 08 | Yes |
| 6 | **PfamCG-1.0 benchmark** | A: 3 split types visualised (Venn-like diagram). B: ΔCG across splits for each baseline (grouped bar). C: Difficulty heatmap (Easy/Medium/Hard × Split). D: Permutation test result (real vs random ΔCG). | Phase 07 | Phase 08 | Yes |

**Colour palette:** Okabe-Ito (colourblind-safe). **Resolution:** 300 DPI. **Format:** PDF.

---

## 4. Claims-to-Sections Mapping

| Claim | Text | Section | Status | Data Source | Verification |
|-------|------|---------|--------|-------------|-------------|
| C-039 | σ-trap replicates in protein domain data (H1) — ΔCG ≥ threshold | §4 | DESIGNED | Phase 03 results | `verify_claims.py` checks p < 0.00625 |
| C-040 | ΔCG ≥ 30pp for low-σ models on Pfam OOD splits | §4 | DESIGNED | Phase 03 results | `verify_claims.py` checks ΔCG ≥ 30 |
| C-041 | PLMs encode surface co-occurrence, not domain grammar (H2) | §5 | DESIGNED | Phase 05 results | Structural vs lexical OOD gap > 10pp |
| C-042 | Structural OOD accuracy < lexical OOD accuracy by >10pp | §5 | DESIGNED | Phase 05 results | Check gap |
| C-043 | Multiplicative model fits better than additive (H3) | §6 | DESIGNED | Phase 07 baselines | F-test on incremental R² |
| C-044 | PfamCG-1.0 benchmark valid against known biology | §6 | DESIGNED | Phase 07 validation | Permutation test p < 0.01, FNR < 5% |

---

## 5. Research-Doc-to-Section Map

| Doc | File | Informs § |
|-----|------|-----------|
| A.1 Pfam structure | `docs/research/pfam-structure-notes.md` | §2.2, §3 (testbed), §6 (benchmark data) |
| A.2 Domain grammar literature | `docs/research/domain-grammar-literature.md` | §1 (motivation), §2.2, §5 (grammar probes) |
| A.3 Pfam ML literature | `docs/research/pfam-ml-literature.md` | §1 (gap), §2.3, §8 (related work) |
| B.1 ESM-2 audit | `docs/research/esm2-audit.md` | §2.3, Fig 5 (ESM-2 baseline) |
| B.2 PLM comparison | `docs/research/plm-comparison.md` | §2.3, §5 (ProstT5 vs ESM-2 for grammar) |
| C.1 Power analysis | `docs/research/power-analysis.md` | §4 (N=500 justification) |
| C.2 OSF preregistration | `docs/research/osf-preregistration-draft.md` | §4 (pre-registered design) |
| C.3 Pilot design | `docs/research/pilot-design.md` | §4 (pilot validation, supplement) |
| D.1 Existing benchmarks | `docs/research/existing-benchmarks.md` | §1 (novelty), §6 (PfamCG-1.0 distinction), §8 |
| D.2 Validation criteria | `docs/research/benchmark-validation-criteria.md` | §6 (benchmark validation protocol) |
| E.1/E.2 Kaggle architecture | `docs/research/kaggle-experiment-architecture.md` | §4 (methods), supplement (compute budget) |

---

## 6. Structural Discrepancies

The current `main.tex` (126-line scaffold) issues:

| Issue | main.tex currrent | Phase 08 says | Resolution |
|-------|-------------------|---------------|------------|
| **§6 mismatch** | §6 = "Exp 3: PfamCG-1.0 Benchmark" | §6 = "Cross-Domain Discovery: H3" | **Keep main.tex** — H3 is part of PfamCG-1.0 analysis, not a separate experiment. Update Phase 08 to match. |
| **§7–§9 ordering** | Discussion → Related Work → Conclusion | Discussion & Conclusion merged | **Keep main.tex** — NeurIPS expects separate Related Work §. Update Phase 08. |
| **§2.3 (Related Work) location** | Embedded in §2 Background | §8 separate | **Keep both** — brief mentions in §2.3, full treatment in §8. |
| **Phase 08 §3 (Problem Formulation)** | Not in main.tex | §3 described separately | **Absorb into main.tex §3** (Pfam testbed + σ_A proxy definitions). |
| **Claims anchors** | `<!-- CLAIM:C-039 -->` etc. in comments | Not yet placed | Insert at final draft stage — keep in comments, one per quantitative result. |

**Phase 08 update needed:** Sections 1–9 should mirror main.tex exactly to avoid confusion.

---

## 7. Content Gaps

| Gap | Needed For | Source | Priority |
|-----|-----------|--------|----------|
| ESM-2 LoRA fine-tuning results | Fig 5, §2.3 comparison | Phase 06 (not yet executed) | High |
| PfamCG-1.0 baseline scores | §6, Fig 6 | Phase 07 (not yet executed) | High |
| Bibliography completeness: `heinzinger2023prostt5` | §2.3 (ProstT5 citation) | Missing from `bibliography.bib` | **Medium — add now** |
| Bibliography completeness: D.1 benchmark refs | §8 (existing benchmarks) | Missing from `bibliography.bib` | **Medium — add now** |
| Supplement §D: compute budget | Appendix | E.1/E.2 doc has cost estimates | Low (fill in Phase 08) |

---

## 8. Timeline

| Phase | When | Output | Paper Impact |
|-------|------|--------|-------------|
| **03** (Brittle domain) | Aug–Dec 2026 | N=500 results | §4 data, Fig 2–3, C-039/C-040 |
| **04** (Statistical analysis) | Jan–Feb 2027 | Effect sizes, regressions | §4 results, Fig 2–3 refinement |
| **05** (Grammar induction) | Feb–Mar 2027 | Probe task results | §5 data, Fig 4, C-041/C-042 |
| **06** (ESM-2 validation) | Mar–Apr 2027 | ESM-2 baseline | §2.3 comparison, Fig 5 |
| **07** (PfamCG-1.0 benchmark) | May–Jul 2027 | Benchmark + validation | §6 data, Fig 6, C-043/C-044 |
| **08** (Paper writing) | Mar–May 2027 | Draft, figures, claims | All sections |
| **09** (Submission) | May 2027 | arXiv, NeurIPS upload | — |

**Critical path:** Phase 03 → Phase 04 → Phase 08 (Fig 2–3). If Phase 03 is delayed, the core contribution (Exp 1) cannot be written. Phase 06 and Phase 07 can be deferred to supplement if behind schedule.

---

## 9. Appendix: Bibliography Status

| Citation | In `bibliography.bib`? | Needed In |
|----------|----------------------|-----------|
| `basri2026sigma` — Σ-Model JAIR paper | ✅ Yes | §2.1 |
| `rives2021esm` — ESM-1b | ✅ Yes | §2.3 |
| `lin2023esm2` — ESM-2 | ✅ Yes | §2.3 |
| `elnaggar2021protbert` — ProtT5 | ✅ Yes | §2.3 |
| `heinzinger2023prostt5` — ProstT5 | ✅ Added Jun 2026 | §2.3 |
| `mistry2021pfam` — Pfam 38.2 | ✅ Yes | §2.2 |
| `finn2016pfam` — Pfam clans | ✅ Added Jun 2026 | §2.2 |
| `eddy2011hmmer` — HMMER | ✅ Added Jun 2026 | §3 |
| `rao2019tape` — TAPE | ✅ Added Jun 2026 | §8 |
| `xu2022peer` — PEER | ✅ Added Jun 2026 | §8 |
| `lake2018cogs` — COGS (compositional gen) | ✅ Added Jun 2026 | §8 |
| `keysers2020measuring` — compositional split | ✅ Added Jun 2026 | §8 |

**Action:** Add missing citations to `paper-neurips/bibliography.bib` during Phase 08 — or ideally now, since research is complete and DOIs are known.

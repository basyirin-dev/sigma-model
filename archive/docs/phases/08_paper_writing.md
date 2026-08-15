# Phase 08 — Paper Writing & Figure Generation

**Deadline**: 2 May 2027
**Dependencies**: Phase 04, Phase 05, Phase 06 (at least available for draft)
**Output**: NeurIPS 2027 paper draft, verify_claims.py, arXiv preprint

---

### Task 8.1: Paper outline and section drafting

- [ ] 8.1.1: Finalise paper structure (8 pages, NeurIPS format):
  - §1 Introduction (1 page)
  - §2 Background: Σ-Model framework + Protein domain architectures (1 page)
  - §3 Problem Formulation: σ_A adaptation for proteins (0.5 page)
  - §4 Brittle Domain Similarity: H1 experiment (1.5 pages)
  - §5 Domain Grammar Induction: H2 experiment (1.5 pages)
  - §6 Cross-Domain Discovery: H3 (0.5 page)
  - §7 PfamCG-1.0 Benchmark (1 page)
  - §8 Discussion & Conclusion (0.5 page)
- [ ] 8.1.2: Write §1 Introduction:
  - Problem: σ-trap from synthetic → natural data
  - Why protein domains are the ideal testbed
  - Summary of contributions
- [ ] 8.1.3: Write §2 Background:
  - §2.1: Σ-Model summary — cite JAIR paper as framework source; do NOT repeat the ODE derivation
  - §2.2: Protein domain architectures — Pfam, HMMER, compositional structure
  - §2.3: Related work — existing protein ML, compositional generalisation in NLP vs protein
- [ ] 8.1.4: Write §3 Problem Formulation:
  - σ_A proxy adaptation for proteins (GCA, RGA, AC)
  - φ(d1,d2) via HMMER bit scores
  - Compositional gap ΔCG
  - Hypotheses H1–H3
- [ ] 8.1.5: Write §4 Brittle Domain Similarity:
  - Experiment design (N=500, 3 conditions)
  - Results: σ_A vs OOD accuracy, ΔCG by condition, H1 test
  - Figure references
- [ ] 8.1.6: Write §5 Domain Grammar Induction:
  - Probe tasks (next-domain, masked-domain, analogy)
  - Structural vs lexical OOD splits
  - Results: H2 test, σ_A correlation
- [ ] 8.1.7: Write §6 Cross-Domain Discovery (if H3 analysis is ready):
  - Additive vs multiplicative coupling comparison
  - F-test on incremental R²
- [ ] 8.1.8: Write §7 PfamCG-1.0 Benchmark:
  - Split definitions, validation, baselines
  - Release as community resource
- [ ] 8.1.9: Write §8 Discussion:
  - Implications for protein ML and de novo design
  - Limitations (Pfam domain sequences only, not 3D structure)
  - Relationship to the three-paper programme

### Task 8.2: Figure finalisation

- [ ] 8.2.1: Figure 1 (Framework overview):
  - Panel A: Σ-Model σ-A bifurcation diagram (reuse from JAIR paper, cite as source)
  - Panel B: Protein domain architecture concept (new)
  - Panel C: Comparison table (synthetic vs natural testbeds)
- [ ] 8.2.2: Figure 2 (Brittle domain results):
  - σ_A proxy vs OOD accuracy scatter (from Phase 04)
  - Cohen's d bar chart
- [ ] 8.2.3: Figure 3 (ΔCG across conditions):
  - Box plot by condition and σ_A group (from Phase 04)
- [ ] 8.2.4: Figure 4 (Grammar induction):
  - Structural vs lexical accuracy (from Phase 05)
- [ ] 8.2.5: Figure 5 (ESM-2 validation):
  - SmallProteinLM vs ESM-2 comparison (from Phase 06), or remove if not ready
- [ ] 8.2.6: Figure 6 (PfamCG-1.0):
  - Split types + baseline results (from Phase 07), or defer to supplement
- [ ] 8.2.7: All figures: Okabe-Ito palette, 300 DPI, alt-text registered

### Task 8.3: Bibliography and claims

- [ ] 8.3.1: Complete `paper-neurips/bibliography.bib`:
  - Core Σ-Model citations (Basri 2026 JAIR, TMLR)
  - Pfam citations (Mistry et al. 2021, Finn et al. 2016)
  - ESM-2 citation (Lin et al. 2023, Science)
  - Protein ML benchmarks (TAPE — Rao et al. 2019, PEER — Xu et al. 2022)
  - Compositional generalisation (Lake & Baroni 2018, Kim & Linzen 2020, Keysers et al. 2020)
  - HMMER (Finn et al. 2011, Eddy 2011)
  - Statistical methods (Pineau et al. 2021 reproducibility checklist)
- [ ] 8.3.2: Add <!-- CLAIM:C-NNN --> anchors at every quantitative result in the manuscript
- [ ] 8.3.3: Update all claims in `docs/claims-registry.md` to VERIFIED where applicable
- [ ] 8.3.4: Verify all claims are discoverable: `grep '<!-- CLAIM:' paper-neurips/main.tex` lists all

### Task 8.4: Verification script

- [ ] 8.4.1: Create `paper-neurips/verify_claims.py` following pattern from `paper-jmlr/verify_contributions.py`:
  - For each quantitative claim (C-039 to C-044), load the relevant result file and verify the number
  - Example: C-039: load `results/pfam-brittle/h1-test-results.json`, check `p_value < 0.00625`
  - Example: C-040: load ΔCG data, check `mean_deltaCG_low_sigma >= 30`
  - Example: C-044: load benchmark validation, check permutation test p < 0.05
- [ ] 8.4.2: Verify all claims pass: `PYTHONPATH=../code:$PYTHONPATH python verify_claims.py`
- [ ] 8.4.3: Handle optional/conditional claims: claims about ESM-2 (Phase 06) should skip gracefully if Phase 06 not complete

### Task 8.5: Supplementary materials

- [ ] 8.5.1: Write supplement sections:
  - A. Σ-Model proxy measurement details (GCA, RGA, AC formulas)
  - B. Extended results (per-condition tables, per-family accuracy)
  - C. PfamCG-1.0 dataset card
  - D. Computational resource usage (GPU hours, carbon cost estimate)
  - E. Author contributions (single author)
- [ ] 8.5.2: Package supplement as `paper-neurips/supplement/main.pdf`

### Task 8.6: arXiv preprint

- [ ] 8.6.1: Prepare arXiv submission:
  - Verify paper compiles: `make pdf` from `paper-neurips/`
  - Verify no undefined references, no overfull boxes
  - Create arXiv tarball: `make arxiv`
  - Set arXiv category: cs.LG (primary), q-bio.BM (secondary)
- [ ] 8.6.2: Submit to arXiv (can update later before NeurIPS camera-ready)

---

**Phase 08 Exit Criteria**:
- [ ] Complete NeurIPS-format paper draft (8 pages + references)
- [ ] 6 figures (final resolution, Okabe-Ito, alt-text)
- [ ] All claims verified: `python verify_claims.py` passes
- [ ] Supplementary materials complete
- [ ] arXiv preprint submitted
- [ ] Paper compiles with 0 errors, 0 undefined refs

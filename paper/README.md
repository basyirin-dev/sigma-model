# Paper 02: Critical Compositional Pressure

**Full Title:** Critical Compositional Pressure: A Phase-Boundary Framework for Compositional Representation Formation in Neural Networks  
**Author:** Basyirin Amsyar Basri (Independent Researcher, Kuala Lumpur, Malaysia)  
**Submission Target:** SSRN CompSciRN Preprint / arXiv Preprint (Peer Review at a Later Date)  
**Release Tag:** `v2.0-paper02` · **Commit Anchor:** `540c992` · **Preregistration Tag:** `p02.5-preregistered` (Commit `97eabba`, 2026-08-23)

---

## 📂 Directory Layout

```
paper/
├── Makefile                        # Build pipeline automation (pdf, journal, figures, test, submission)
├── writing/                        # LaTeX source files and publication figures
│   ├── manuscript.tex              # Comprehensive 38-page research monograph (main + appendices)
│   ├── manuscript_journal.tex      # Streamlined 22-page journal article (Sections 1–8, References)
│   ├── supplementary_materials.tex # Standalone 17-page Supplementary Materials (Appendices A–F)
│   ├── bibliography.bib            # Curated BibTeX references
│   └── figures/                    # Vector PDF/PNG figures with JSON metadata sidecars
│       ├── figure1_phase_portrait.*
│       ├── figure2_bifurcation_boundary.*
│       ├── figure3_representation_geometry.*
│       ├── figure4_cross_benchmark_generalization.*
│       └── figure5_hessian_spectral_dynamics.*
├── submission_arxiv/                # arXiv submission bundle directory
│   ├── manuscript.tex              # Clean flat LaTeX source
│   ├── manuscript.bbl              # Compiled BibTeX references
│   ├── tmlr.sty / tmlr.bst         # Stylesheet & bibliography style
│   └── figures/                    # Standalone vector figures
├── arxiv_bundle.tar.gz             # Packaged tarball for direct arXiv upload
├── submission_ssrn/                # SSRN CompSciRN preprint portal package & metadata
│   ├── ssrn_metadata.md            # Portal abstract, JEL/CompSci classifications & checklist
│   ├── manuscript.pdf              # Full monograph PDF for preprint archive
│   └── supplementary_materials.zip # Synchronized reproducibility bundle
├── src/                            # Modular Python implementation package
│   ├── continuous/                 # Analytical Two-Subspace ODE solver & signature engine
│   ├── data/                       # Benchmark dataset generators (hbar, SCAN, COGS, PCFG)
│   ├── models/                     # Transformers (2L, 4L) and Recurrent Seq2Seq (GRU, LSTM)
│   ├── analysis/                   # Figure generation, VAR econometric panel, Lanczos Hessian
│   └── experiments/                # Production sweep orchestration & gate runners
├── tests/                          # 130 automated unit & regression tests (100% passing)
├── data/processed/                 # Derived analysis summaries, trajectories & statistical tables
├── notebooks/                      # Self-contained Jupyter notebooks for Kaggle replication
└── planning/                       # Research Planning Framework (RPF v2.0) ledgers & roadmap
    ├── preregistration.md          # Locked preregistration protocol (commit 97eabba)
    ├── ledger.md                   # Master Claim Ledger (Four-Level Epistemic Ladder)
    ├── roadmap.md                  # Phase tracking & milestone audit
    └── standards.md                # 54 cross-cutting operational rules (CC.1–CC.7)
```

---

## ⚡ Build & Verification Commands

From the `paper/` directory:

```bash
# Run the 147 unit & regression tests
make test

# Regenerate all publication figures with metadata sidecars
python src/analysis/generate_publication_figures.py

# Recompute full Phase 07 analysis and econometric panel models
python -m paper.src.analysis.run_phase07_analysis

# Compile all manuscript deliverables and package submission bundles
make submission
```

---

## 📄 Deliverables Summary

| Deliverable | Location | Pages | Status |
|---|---|:---:|:---:|
| **Comprehensive Monograph** | `writing/manuscript.pdf` | 40 | ✅ 0 errors, 0 undefined citations/references |
| **Journal Main Article** | `writing/manuscript_journal.pdf` | 23 | ✅ 0 errors, 0 undefined citations/references |
| **Supplementary Materials** | `writing/supplementary_materials.pdf` | 18 | ✅ 0 errors, 0 undefined citations/references |
| **arXiv Submission Bundle** | `arxiv_bundle.tar.gz` | — | ✅ Complete standalone flat sources & figures |
| **SSRN Submission Bundle** | `submission_ssrn/` | — | ✅ PDF + metadata + reproducibility ZIP |
| **Reproducibility Bundle** | `submission_ssrn/supplementary_materials.zip` | — | ✅ Complete `src/`, `tests/`, `figures/`, `data/` |


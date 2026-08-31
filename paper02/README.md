# Paper 02: Critical Compositional Pressure

**Full Title:** Critical Compositional Pressure: A Phase-Boundary Framework for Compositional Representation Formation in Neural Networks  
**Author:** Basyirin Amsyar Basri (Independent Researcher, Kuala Lumpur, Malaysia)  
**Submission Target:** Advances in Artificial Intelligence and Machine Learning (AAIML) / SSRN CompSciRN Preprint  
**Release Tag:** `v2.0-paper02` · **Commit Anchor:** `69e1f57b` · **Preregistration Tag:** `p02.5-preregistered` (2026-08-23)

---

## 📂 Directory Layout

```
paper02/
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
├── submission_aaiml/               # Complete AAIML journal submission portal package
│   ├── aaiml_submission_guide.md   # Step-by-step submission metadata, keywords, abstract & checklist
│   ├── cover_letter.tex / .pdf     # Formal signed submission cover letter to Editor-in-Chief
│   ├── manuscript_journal.pdf      # Synchronized journal manuscript PDF
│   ├── supplementary_materials.pdf # Synchronized Supplementary Materials PDF
│   └── supplementary_materials.zip # Standalone reproducibility bundle
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
├── tests/                          # 129 automated unit & regression tests (100% passing)
├── data/processed/                 # Derived analysis summaries, trajectories & statistical tables
├── notebooks/                      # Self-contained Jupyter notebooks for Kaggle replication
└── planning/                       # Research Planning Framework (RPF v2.0) ledgers & roadmap
    ├── preregistration.md          # Locked preregistration protocol (commit 69e1f57b)
    ├── ledger.md                   # Master Claim Ledger (Four-Level Epistemic Ladder)
    ├── roadmap.md                  # Phase tracking & milestone audit
    └── standards.md                # 54 cross-cutting operational rules (CC.1–CC.7)
```

---

## ⚡ Build & Verification Commands

From the `paper02/` directory:

```bash
# Run the 129 unit & regression tests
make test

# Regenerate all publication figures with metadata sidecars
python src/analysis/generate_publication_figures.py

# Recompute full Phase 07 analysis and econometric panel models
python -m paper02.src.analysis.run_phase07_analysis

# Compile all manuscript deliverables and package submission bundles
make submission
```

---

## 📄 Deliverables Summary

| Deliverable | Location | Pages | Status |
|---|---|:---:|:---:|
| **Comprehensive Monograph** | `writing/manuscript.pdf` | 38 | ✅ 0 errors, 0 undefined citations/references |
| **Journal Main Article** | `writing/manuscript_journal.pdf` | 22 | ✅ 0 errors, 0 undefined citations/references |
| **Supplementary Materials** | `writing/supplementary_materials.pdf` | 17 | ✅ 0 errors, 0 undefined citations/references |
| **Submission Cover Letter** | `submission_aaiml/cover_letter.pdf` | 2 | ✅ Signed, formatted for AAIML Editor-in-Chief |
| **Reproducibility Bundle** | `submission_aaiml/supplementary_materials.zip` | — | ✅ Complete `src/`, `tests/`, `figures/`, `data/` |

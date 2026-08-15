===============================================================================
                    H-BAR MODEL - ARXIV SUBMISSION PACKAGE
===============================================================================

Title: The H-Bar Model: Schema-Coherence Suppression as the Origin of
       Compositional Generalization Failure

Subtitle: A Pre-Registered Dynamical-Systems Framework

Author: Basyirin Amsyar bin Basri
        Independent Researcher, Petaling Jaya, Malaysia
        Email: basyirin.basri@gmail.com

Version: 3.0+ (Full Reconstruction)
Date: March 2026

===============================================================================
                              PACKAGE CONTENTS
===============================================================================

This submission package contains the following files:

MAIN DOCUMENT:
  manuscript.tex           - Main LaTeX source file
  bibliography.bib      - Bibliography database (521 entries)

FIGURES:
  figures/figure1-framework.tex              - The H-Bar Conceptual Framework
  figures/figure2-phases.tex            - The Five-Phase Training Arc
  figures/figure3-coupled-system.tex           - Coupled Dynamical System Architecture
  figures/figure4-diagnostic.tex        - The Compositional Generalization Failure Mode
  figures/figure5-protocol.tex          - Benchmark Protocol Diagram
  figures/figure6-main-results.png      - Main experimental results
  figures/figure7-prediction6.png - Prediction 6 model comparison
  figures/figure8-prediction9.png - Prediction 9 phase transition

DOCUMENTATION:
  ARXIV_SUBMISSION_GUIDE.md - Detailed submission instructions

===============================================================================
                              COMPILATION
===============================================================================

To compile this document locally, you need:
  - TeX Live 2024 or later (or equivalent LaTeX distribution)
  - Required packages: amsmath, amssymb, amsthm, mathtools, graphicx,
    natbib, hyperref, cleveref, tikz, pgfplots, enumitem, microtype,
    booktabs, geometry, caption

Compilation commands:

  IMPORTANT: Run these commands from INSIDE the arxiv-submission directory!

  cd arxiv-submission

  # Using latexmk (recommended):
  latexmk -pdf manuscript.tex

  # Manual compilation:
  pdflatex manuscript.tex
  bibtex manuscript.aux
  pdflatex manuscript.tex
  pdflatex manuscript.tex

  # Or from the parent directory:
  cd ..
  latexmk -pdf -output-directory=arxiv-submission arxiv-submission/manuscript.tex

Expected output: paper.pdf (approximately 31 pages)

===============================================================================
                              ABSTRACT
===============================================================================

Current training pipelines optimise parametric depth without formally
targeting schema coherence --- the degree to which an agent's representations
are restructured around deep governing principles rather than surface-
statistical regularities. Existing empirical results on compositional
generalisation benchmarks suggest that agents exhibiting high parametric
depth but low schema coherence tend to fail systematically on out-of-
distribution recombination tasks that standard in-distribution metrics do
not detect.

We introduce the H-Bar Model, a coupled dynamical-systems framework with
three core contributions: (1) The sigma-suppression mechanism proving that
standard SGD dynamics create a stable low-sigma equilibrium (the "sigma-trap"),
(2) A coupled ODE framework with proven local existence/uniqueness, forward
invariance, and bifurcation analysis, and (3) A phase-structured curriculum
derived from the ODE's bifurcation structure.

The framework demonstrates formal correspondence with five cognitive faculty
gaps and enables generation of executable benchmark families for each. Initial
experiments on SCAN/COGS confirm both H-Bar conditions significantly outperform
standard SGD on out-of-distribution accuracy.

===============================================================================
                              ARXIV CATEGORIES
===============================================================================

Primary Category:
  cs.LG - Computer Science > Learning and Generalization

Secondary Categories (optional):
  cs.AI - Computer Science > Artificial Intelligence
  stat.ML - Statistics > Machine Learning
  cs.CL - Computer Science > Computation and Language

===============================================================================
                              LICENSE
===============================================================================

This work is licensed under the Creative Commons Attribution 4.0 International
License (CC BY 4.0). To view a copy of this license, visit:
http://creativecommons.org/licenses/by/4.0/

===============================================================================
                              KEYWORDS
===============================================================================

Compositional Generalization, Schema Coherence, Dynamical Systems,
Out-of-Distribution Generalization, Cognitive AI, Phase Transitions,
Bifurcation Analysis, Pre-Registration, SCAN, COGS

===============================================================================
                              CONTACT
===============================================================================

For questions, comments, or collaboration inquiries, please contact:
  Basyirin Amsyar bin Basri
  Email: basyirin.basri@gmail.com

===============================================================================
                           END OF README
===============================================================================

# Changelog

All notable changes to the H-Bar V3.0+ project.

## [Unreleased]

### Research Preparation (Phase 00_5)
- [A.1] Pfam 38.2 structure notes (`docs/research/pfam-structure-notes.md`) — **done**
- [A.2] Domain grammar literature survey (`docs/research/domain-grammar-literature.md`) — **done**
- [A.3] Pfam ML literature review (`docs/research/pfam-ml-literature.md`) — **done**
- [B.1] ESM-2 training data audit (`docs/research/esm2-audit.md`) — **done**
- [B.2] PLM comparison for domain tasks (`docs/research/plm-comparison.md`) — **done**
- [C.1] Statistical power analysis (N=500) (`docs/research/power-analysis.md`) — **done**
- [C.2] OSF preregistration draft (`docs/research/osf-preregistration-draft.md`) — **done**
- [C.3] Pilot experiment design (`docs/research/pilot-design.md`) — **done**
- [D.1] Existing compositional gen benchmarks (`docs/research/existing-benchmarks.md`) — **done**
- [D.2] Benchmark validation criteria (`docs/research/benchmark-validation-criteria.md`) — **done**
- [E.1/E.2] Kaggle/Colab architecture (`docs/research/kaggle-experiment-architecture.md`) — **done**
- [FIX] Stale reference cleanup: Pfam version references standardised to 38.2 in phases 03/07, threshold fix, permutation count fix — **done**
- [FIX] Claims-registry.md verification command updated for paper-neurips/ — **done**
- [DOC] Created `docs/paper-proposal.md` (narrative arc, figure plan, claim mapping, timeline) — **done**
- [DOC] Added 7 missing citations to `paper-neurips/bibliography.bib` (ProstT5, TAPE, PEER, Pfam 2016, HMMER, SCAN, CFQ) — **done**
- [CC] Cross-cutting compliance: CC.2 (data provenance) + CC.5 (documentation) checks implemented — **done**

### Protein Infrastructure (Phase 00_repo)
- [R.1] Created `code/sigma/proteins/` subpackage stub (7 modules) — **done**
- [R.2] Added biopython==1.87, pyhmmer==0.12.1, fair-esm==2.0.0 deps — **done**
- [R.3] Created pfam experiment configs (base, brittle, grammar, benchmark) — **done**
- [R.4] Created `paper-neurips/` scaffold with Makefile, class stub, bibliography — **done**
- [R.5] Registered claims C-039 to C-050 (6 active + 6 reserved) — **done**
- [R.6] Created `docs/protein-data-registry.md` — **done**
- [R.7] Created `docs/risks/RISK_REGISTER.md` (6 risks, OpenSciRe format) — **done**
- [R.8] Verified opencode.json, MCP servers, updated AGENTS.md — **done**

### Pfam Data Pipeline (Phase 01)
- [P1.1] Stockholm parser (`parse_stockholm`) with gzip support, metadata extraction, `max_records` streaming — **done**
- [P1.2] Domain architecture extraction (`extract_domain_architectures`) with overlap exclusion, length filtering (2–15) — **done**
- [P1.3] Domain vocabulary builder (`build_domain_vocab`) with special tokens and clan mapping — **done**
- [P1.4] HMMER bit score similarity (`compute_domain_similarity`, `precompute_similarity_matrix`) with emitted-sequence hmmscan, symmetrisation, self-score normalisation — **done**
- [P1.5] Fold compatibility tiering (`compute_fold_compatibility`) — clan binary tier (0.9/0.1); PDB stubbed — **done**
- [P1.6] Compositional splits (`make_compositional_splits`) — Type A/B/C with seed reproducibility, family/clan hold-out — **done**
- [P1.7] Recombination distance (`recombination_distance`) = 1 − mean psi_geometric(sim) — **done**
- [P1.8] Pipeline integration script (`scripts/verify_pfam_pipeline.py`) with `--quick`, `--full`, `--cache` — **done**
- [P1.9] Full Pfam 38.2 processed (30 134 records → 133 290 architectures, 13 368 families, 23 MB cache) — **done**
- [P1.10] Cached artifacts: `architectures.pt`, `vocab.json`, `clan_map.json`, `splits.pt`, `split_stats.json` — **done**
- [P1.11] 53 module tests (33 data + 20 splits) + 84 total project tests — **done**
- [P1.12] Cross-cutting compliance: CC.1.1/1.2/1.3 (seeding), CC.1.4 (explicit seed params), CC.1.6 (env logging), CC.5.1 (docstrings), CC.5.3 (notebook headers) — **done**

### Infrastructure
- [I-01] Added Kaggle path detection fallback in notebooks (H) — **open**
- [I-02] Moved SCANDataset from notebook to `code/hbar/utils/data.py` (M) — **open**
- [I-03] Dynamic `num_workers` for DataLoader (L) — **open**
- [I-04] Added seaborn ^0.13 to pyproject.toml (L) — **open**
- [W3.1] Fixed LaTeX build pipeline: added fontspec/unicode-math, newunicodechar for Greek/checkmarks, Lua filter for \tag→\qquad conversion, switched pdflatex→lualatex, added none counter, tightlist command — **done**

### Tooling
- [T-01] Publication monitor HTTP retry with exponential backoff — **open**
- [T-03] Unit tests for ODE solver and config loading — **open**
- [T-04] Local smoke test script — **open**
- [T-02] Expanded keyword clusters for publication monitor — **open**

### Code Quality
- [C-01] Fixed 39 ruff lint errors (unused imports, naming, line length) — **done**
- [C-02] Missing seaborn dependency — **open**

### Paper
- [P-01] Integrate 5 new paper citations/addresses — **open**
- [P-02] Refresh gap_conflict_map.md with 5 new papers — **open**
- [P-03] Integrate Kaggle results post-June 1 2026 — **pending**
- [W1.2] Added 15 missing CLAIM anchors to paper.md — **done**
- [M4.4] Bibliography hygiene verified (521 lines, 41 arXiv, 29 DOI) — **done**
- [M3.1] Paper PDF build pipeline fixed (pandoc + lualatex) — **done**

### Workflow
- [D1-D7] Full daily workflow executed: publication monitor, errata log, import smoke test, ruff lint, git hygiene, config sanity, dataset integrity — **done**
- [W1-W4] Full weekly workflow executed: claims anchor sweep, payload inspection, dependency audit, figure pipeline fix, ODE cross-referencing, documentation consistency, unit test gap identified, errata reconciliation — **done**
- [M1-M4] Full monthly workflow executed: statistical re-evaluation, conference norm review, framework compatibility, verification sweep, integration map, bibliography hygiene, issue register refresh — **done**

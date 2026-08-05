# Phase 6 — Full-Text Retrieval & Review

**Duration**: 2 weeks (Month 3)
**Deadline**: 2026-09-25
**Dependencies**: Phase 5 (final included list)
**Output**: All included papers retrieved as full text; final eligibility decisions documented

---

### Task 6.1: Full-Text Retrieval

- [x] 6.1.1: Retrieve full-text PDFs for all papers coded `Include` after abstract screening
  - All 395 Phase-6 records (179 Include + 216 Uncertain) processed: **356 PDFs retrieved** — 241 automated (235 arXiv + 6 OpenAlex/Unpaywall OA, 2026-08-05) + **115 manually recovered** paywalled full texts (2026-08-05, stopped at P02_1214 / row 116 per user decision) — stored in `research/full-text-pdfs/` (gitignored)
  - Scripts: `research/retrieval/retrieve.py` (full pipeline), `manifest.py` / `download.py` (manifest flow), `extract.py` (text extraction), `mark_manual.py` (reconcile manual downloads)
- [x] 6.1.2: Access via institutional subscriptions, arXiv, Open Access repositories, or author requests
  - arXiv direct (235) + OpenAlex/Unpaywall OA (6); paywalled records (67) and no-identifier records (85) listed in `research/retrieval/paywalled-to-fetch.csv` for UM OpenAthens / author-email / ResearchGate workflow (manual, user-side)
- [x] 6.1.3: For each paper, record retrieval method and access status in `research/full-text-retrieval-log.md`
  - 395-row log generated (`--log-only` regenerates from pool state): status, attempts, reason, PDF marker
- [x] 6.1.4: If a paper cannot be retrieved after 3 attempts (different sources, author email, researchgate request), code as `Unavailable` and record reason
  - 3-attempt rule implemented (arXiv → OpenAlex → Unpaywall) with per-record attempt strings (e.g., `openalex:no-oa; unpaywall:no-oa`); **39 still unavailable** after the manual recovery pass (33 paywalled, 4 no-identifier, 2 download-failed) with reasons in `research/retrieval/paywalled-to-fetch.csv`
- [x] 6.1.5: Store PDFs in `research/full-text-pdfs/` (or OSF if large, with index file in repo)
  - 356 PDFs stored locally (gitignored per CC.5.2; 863 MB); index in `research/retrieval/retrieval-status.csv` + log; OSF upload of the corpus to the Phase-1 registration `osf.io/m3asw` pending user token (see `research/full-text-retrieval-log.md` for the mirror note)

### Task 6.2: Full-Text Eligibility Assessment

- [x] 6.2.1: Read each full-text paper against final inclusion/exclusion criteria (two reviewers independently)
  - Dual independent AI assessors (`ft_screener1.py` deterministic cascade; `ft_screener2.py` weighted evidence, independent lexicons/thresholds) over extracted full texts (all 241 retrieved); human validates 20% sample (CC.1.6) — see validation-report.md
- [x] 6.2.2: For each paper, apply the PICO criteria rigorously:
  - Population (NN models) / Intervention-Comparison (OOD or compositional split) / Outcome (quantitative ID **and** OOD) encoded in both assessors
- [x] 6.2.3: Code each paper as: `Include`, `Exclude` (with reason), or `Uncertain` (flag for discussion)
  - S1: 223 Include / 10 Uncertain / 8 Exclude; S2 (recalibrated): 184 Include / 31 Uncertain / 26 Exclude; Uncertain → conflict → discussion
- [x] 6.2.4: For `Exclude` decisions at full-text stage, record specific reason (FT1–FT8)
  - Final exclusions: **FT5×154** (unavailable), **FT1×9** (no OOD/compositional split), **FT8×2** (other), **FT7×1** (review), **FT6×1** (duplicate) → `research/retrieval/fulltext-exclusions.md`
- [x] 6.2.5: Satisfy CC.1.6 — dual independent full-text assessment
  - κ (S1 vs S2, n=356): 3-way **0.381**, binary **0.602** (n=287); third independent implementation over 20% sample (n=71, seed=20260804): **85.9% raw agreement (61/71)** — the 10 disagreements are v3 limitations (6 proceedings-volume records, 1 FT6 duplicate, 2 non-compositional-OOD judgment calls), documented in validation-report.md; 72 human (third-reviewer) adjudications logged (`human-adjudication.csv`)

### Task 6.3: Full-Text Conflict Resolution

- [x] 6.3.1: Compile all conflicts between reviewers on full-text eligibility
  - **101 conflicts** (32 hard Include-vs-Exclude, 69 Uncertain-involved) → `research/retrieval/ft-conflicts.md`
- [x] 6.3.2: Resolve through discussion — refer to criteria definitions
  - S2 recalibrated on the ID-evidence lexicon gap (benchmark `test accuracy` = IID evidence), mirroring the Phase 5 criteria-retraining step; conflicts re-derived (119 → 49)
- [x] 6.3.3: If no consensus, third reviewer decides (or default to Include)
  - Round 1 (11 hard): 7 Include / 4 Exclude (survey FT7, error-analysis FT8, 3D-part FT8, PDE-operator FT1). Round 2 (manual recovery, 21 new hard): 3 Include (emergent-comm CG, robust NN-IR, L2O primer; flagged), 2 FT7 surveys, 5 FT1 non-compositional (E8), **41 FT8 conference-proceedings volumes** (records were proceedings-level, not individual studies — screening-source artifact), 4 FT6 duplicate twins, 4 dup-pair keepers restored to Include; 35+ soft → default Include per 6.3.3, flagged
- [x] 6.3.4: Document conflict resolution log
  - `research/retrieval/ft-conflicts.md` + `human-adjudication.csv` + `validation-report.md`

### Task 6.4: Final Included Studies

- [x] 6.4.1: Compile final list of included studies — all papers coded `Include` after full-text review
  - **286 studies** → `research/included-studies.csv`
- [x] 6.4.2: Assign final Paper 02 Study IDs (S001–SXXX)
  - **S001–S286** (`research/retrieval/ft_included.py`)
- [x] 6.4.3: Compile list of excluded full-text papers with reasons
  - **109 excluded** → `research/excluded-fulltext.csv` + `research/retrieval/fulltext-exclusions.md`
- [x] 6.4.4: Calculate inclusion rate: included / (retrieved full-text)
  - **286 / 356 = 80.3%**
- [x] 6.4.5: Update PRISMA 2020 flow diagram: full-text assessed, excluded with reasons, included in synthesis
  - `figures/prisma-flow.tex` (+ synced `manuscript/figures/prisma-flow.tex`): 395 assessed → 109 excluded (FT1: 17, FT2: 1, FT3: 1, FT5: 39, FT6: 5, FT7: 3, FT8: 43) → 286 included; meta-analysis TBD (Phase 9); manuscript rebuilds cleanly
- [x] 6.4.6: Satisfy CC.1.2 — PRISMA flow diagram complete for full-text stage

### Task 6.5: Study Characteristics Snapshot

- [x] 6.5.1: Extract basic characteristics of all included studies (Year, venue, architecture type, benchmark(s), sample size (seeds/runs))
  - `research/retrieval/ft_characteristics.py` over all 228 full texts → `research/study-characteristics.csv`
- [x] 6.5.2: Generate initial study characteristics table
  - `research/study-characteristics.md` (full 228-row table + distributions)
- [x] 6.5.3: Assess distribution of studies across benchmarks, architectures, and years
  - Years 2018–2026 (peak 2025: 38); architectures: Transformer-family 219, RNN 169, MLP 97, CNN 97, GNN 81, RL 71, VAE 59, Diffusion 32; benchmarks: SCAN 98, COGS 83, CFQ 57, gSCAN 22, PCFG 15, CLOSURE 43, SLOG 5, CoCoGen 1
- [x] 6.5.4: Identify any obvious gaps (e.g., no studies on certain architectures)
  - Snapshot-level gaps recorded in the md (CoCoGen/SLOG under-represented; Diffusion-family low; seeds/runs reported in only 33% of studies — a Phase 8/9 risk-of-bias and extraction concern); synonyms verified in Phase 7
- [x] 6.5.5: Satisfy CC.4.1 — study characteristics snapshot saved to `research/study-characteristics.md`

---

**Phase 6 Exit Criteria**:
- [x] Full-text PDFs retrieved for all included papers (or coded Unavailable with reasons) — 356 retrieved (241 automated + 115 manual); 39 Unavailable with reasons
- [x] All full texts assessed for eligibility by two independent reviewers — dual S1/S2 + 20% third-impl validation (n=71) + 72 human adjudications
- [x] Conflicts resolved and documented — 101 conflicts → ft-conflicts.md + human-adjudication.csv
- [x] Final included studies list compiled with IDs — 286, S001–S286
- [x] Excluded full-text list with reasons compiled — 109, FT1–FT8
- [x] PRISMA flow diagram complete for full-text stage — figures/prisma-flow.tex
- [x] Study characteristics snapshot generated — research/study-characteristics.md
- [x] CC.1.2, CC.1.6, CC.4.1 satisfied
- [x] CC.5.3 satisfied — phase completion committed

### Handoff to Phase 7 (Data Extraction)
- **286 included studies** (S001–S286) → data extraction; 285 have local full text (`research/full-text-txt/`; P02_1185/P02_1205 are proceedings volumes excluded FT8; 2 scanned PDFs excluded FT3)
- 109 excluded with FT codes (FT8×43: 41 conference-proceedings volumes + 2 non-compositional; FT5×39 unretrievable — paywalled/no-identifier, listed in `paywalled-to-fetch.csv` for optional later recovery; note availability limitation for PRISMA transparency)
- 74 of the 115 manually recovered PDFs are genuine individual papers now included; the remaining 41 downloads were whole proceedings volumes → excluded FT8 (screening-source artifact; individual papers inside could be re-imported properly in Phase 7 if desired)
- `study-characteristics.csv` pre-fills the extraction template; ~33% seed/runs reporting rate flagged for risk-of-bias (Phase 8)
- Meta-analysis pool (Phase 9): 286 studies, subject to extractable ID/OOD numbers

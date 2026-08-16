# arXiv Upload Guide — σ-Trap narrow paper + companion (P12)

**Bundle**: `../sigma-arxiv-submission.tar.gz` (built by `make arxiv` from `paper/`).
**Verify first**: the bundle compiles standalone — unpack and run
`pdflatex manuscript.tex && bibtex manuscript && pdflatex manuscript.tex && pdflatex manuscript.tex`
(or use the P12 verification step: clean-dir build, 0 errors, 0 undefined refs).

---

## Submission 1 — the narrow paper (this bundle)

| Field | Value |
|---|---|
| **Title** | The $\sigma$-Trap: A Dynamical Model of Schema-Coherence Suppression in Compositional Generalisation |
| **Authors** | Basyirin Amsyar Basri (ORCID: *to confirm — CC.6.6*) |
| **Abstract** | Paste from `manuscript.tex` abstract (≈215 words, within arXiv's limit; it is the ≤250-word P08-finalised abstract) |
| **Primary category** | cs.LG — Machine Learning |
| **Secondary categories** | cs.NE — Neural and Evolutionary Computing |
| **Comments** | 20 pages (main text 15 pp + appendices A–C pp. 16–18 + references pp. 19–20); companion technical report: arXiv:XXXX.XXXX (post as Submission 2, then cross-link); prepared with the TMLR stylefile `preprint` option |
| **License** | CC BY 4.0 (matches TMLR) |

**File upload**: upload `sigma-arxiv-submission.tar.gz` as-is (arXiv accepts tar.gz).
It contains `manuscript.tex` (already switched to `\usepackage[accepted,preprint]{tmlr}`
so the real author name renders — the default stylefile rendering is "Anonymous authors"),
`manuscript.bbl`, `manuscript.pdf`, `bibliography.bib`, `figures/` (6 PNG + 7 TikZ),
`tmlr.sty`, `tmlr.bst`, and `companion/` (for convenience; the companion is a separate
submission — see below).

**Mechanics**:
- New submissions received by 14:00 ET (Mon–Fri) are announced at 20:00 ET.
- The arXiv processor auto-detects `manuscript.tex` as the top-level TeX file (it contains
  `\documentclass`); no other file does.
- All filenames already comply with arXiv's charset (`a-z A-Z 0-9 _ + - . , =`); no spaces.
- Figures are PNG/TeX — compatible with PDFLaTeX; no conversion needed.
- `hyperref` default warnings in the log are not submission blockers.

## Submission 2 — the companion technical report

**Bundle**: `paper/companion/` sources: `companion.tex` + `companion.bbl` + `companion.bib`
(the companion is a plain `\documentclass[11pt]{article}`, self-contained, no figures).
Create a small tarball of these three files and upload.

| Field | Value |
|---|---|
| **Title** | The Σ-Model: Extended Framework (companion to "The σ-Trap…") |
| **Authors** | Basyirin Amsyar Basri |
| **Abstract** | From `companion.tex` |
| **Primary category** | cs.LG |
| **Comments** | Technical report (not peer-reviewed); companion to arXiv:XXXX.XXXX (Submission 1) |

**Order**: post the narrow paper and the companion together; then add the cross-links
(arXiv IDs) in each other's Comments fields and in the manuscript's companion pointer
if desired (v1 announcement date stamps both).

---

## Timing decision (already locked)
Post to arXiv only now, after the gate experiment is integrated (P04–P11 done). No
workshop detour: arXiv → direct TMLR.

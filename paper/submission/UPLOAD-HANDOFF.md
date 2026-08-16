# P12 Upload Handoff — arXiv + TMLR

Everything is prepared and verified. You (the user) perform the uploads; the files below are upload-ready.

## 1. arXiv (2 submissions, real identity)

Follow `arxiv-submission/README-upload.md`.

| Submission | Upload file | Contents | Metadata |
|---|---|---|---|
| 1 — Narrow paper | `sigma-arxiv-submission.tar.gz` (repo root) | manuscript.tex (preprint option, author name renders), .bbl, .pdf, figures/, tmlr.sty/bst, bibliography.bib | Title: *The σ-Trap…*; cs.LG (primary), cs.NE; abstract ≈215 words; author name + ORCID (to confirm) |
| 2 — Companion | `paper/companion/companion.{tex,bbl,bib}` (tar them) | standalone article class, 24 pp | Title: *The Σ-Model: Extended Framework…*; cs.LG |

Sequence: post both, then cross-link the arXiv IDs in the Comments fields. Cutoff 14:00 ET for same-day announcement.

## 2. TMLR (OpenReview, anonymous)

Follow `paper/submission/compliance-checklist.md` (Section B = your 8 tasks).

| Item | File |
|---|---|
| Main PDF | `paper/submission/manuscript.pdf` (20 pp, "Anonymous authors / Paper under double-blind review", LLM footnote on p.1) |
| Abstract field | paste from manuscript abstract (≈215 words) |
| Supplementary 1 | `paper/submission/supplementary/companion.pdf` (24 pp, self-citations anonymized) |
| Supplementary 2 | `paper/submission/supplementary/sigma-trap-code-data.zip` (849 KB: H-Bar code + gate config + 60-run data) |
| Recommended AEs | 2–4 with expertise in dynamical systems for ML / compositional generalization / learning theory |

Supporting docs (for you, not uploaded): `cover-letter.md` (JAIR narrative), `reviewer-summary.md` (one-page "How the paper changed"), `compliance-checklist.md`.

**Do not** link the arXiv version from the TMLR submission (double-blind; the named arXiv preprints exist, but the submission must not point to them).

## 3. Verified status (final)

- arXiv bundle: clean-dir standalone build, 0 errors, 0 undefined refs, 20 pp, author name on p.1.
- Companion (arXiv variant): 24 pp, 0 errors/undefined.
- TMLR PDF: 0 errors/undefined, 20 pp, "Anonymous authors", no name/ORCID/path/hash anywhere in the package.
- Supplementary: anonymized, scanned clean, 24 pp + 849 KB zip.

## 4. Files tracked in git (the reproducible source of everything above)

- `paper/Makefile` (arxiv target), `.gitignore`
- `paper/submission/manuscript.tex` (anonymized), `supplementary/companion.tex`, `supplementary/companion.bib`, `supplementary/README.md`
- `paper/submission/cover-letter.md`, `reviewer-summary.md`, `compliance-checklist.md`
- `arxiv-submission/README-upload.md`

Regenerate any derived output: `cd paper && make arxiv` (bundle), compile `paper/submission/manuscript.tex` for the TMLR PDF, re-zip `paper/submission/supplementary/` if needed.

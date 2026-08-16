# TMLR Submission — Compliance Checklist & OpenReview Tasks

**Manuscript**: The $\sigma$-Trap: A Dynamical Model of Schema-Coherence Suppression in Compositional Generalisation
**Status**: Package prepared in `paper/submission/` — user executes the OpenReview steps.

---

## A. TMLR compliance checklist (verified)

| Requirement | Status | Evidence |
|---|---|---|
| Official TMLR stylefile/template, unmodified | ✅ | `paper/tmlr.sty` tracked and unchanged in this branch (no edits since P09); no formatting/font/layout alterations |
| PDF generated from the stylefile | ✅ | `paper/submission/manuscript.pdf` (20 pp), compiled from `paper/submission/manuscript.tex` with `tmlr.sty` |
| Double-blind: anonymized PDF | ✅ | Page 1 renders "Anonymous authors / Paper under double-blind review"; `\author{Anonymous}`; full-PDF grep for author name — zero hits |
| No link to a named version | ✅ | No arXiv ID/URL in the anonymized manuscript or supplementary; the companion pointer is prose only |
| LLM-use disclosure footnote on page 1 | ✅ | "This submission was prepared with the assistance of large language models used as general-purpose assistive tools…" (required by the TMLR LLM-use policy) |
| Broader Impact statement | ✅ | Present (dual-use discussion: a curriculum that suppresses coherence could be reversed); no additional ethics obligations (no human data, no IRB) |
| Originality / dual-submission policy | ✅ | No reuse of text/figures/results from published peer-reviewed work; arXiv preprints are explicitly permitted (FAQ); companion is an arXiv technical report, not peer-reviewed |
| Supplementary material: PDF/ZIP, ≤ 100 MB, anonymized | ✅ | `supplementary/companion.pdf` (24 pp, anonymized self-citations) + `supplementary/sigma-trap-code-data.zip` (849 KB: H-Bar code, gate config, 60-run data, README); zip contents scanned for identity/paths — clean |
| Main-text length | ✅ (noted) | 15 pp before references (> 12 → longer review timescale, accepted by the authors) |
| Ethics / Code of Conduct | ✅ | No harmful-application risk beyond the dual-use note; no human-derived data; no authorship-dispute issues (single author) |

## B. OpenReview submission tasks (user — cannot be done by the agent)

1. **Profiles**: complete, active OpenReview profile(s) with affiliations, publication history, and conflicts (domain + personal). All authors must satisfy the TMLR authorship criteria (the submission's authors testify to awareness, responsibility, and originality).
2. **Authorship budget**: check the Generalized Harmonic Quota budget (all authors have sufficient remaining quota for the year) — reviewers/AEs get doubled quotas if applicable.
3. **Upload**: submit the anonymized PDF (`paper/submission/manuscript.pdf`); paste the abstract into the metadata field (≈215 words).
4. **Supplementary**: attach `paper/submission/supplementary/companion.pdf` and `sigma-trap-code-data.zip` (both anonymized; ≤ 100 MB).
5. **Recommended action editors**: recommend 2–4 AEs with relevant expertise (dynamical systems for ML, compositional generalization, learning theory).
6. **Disclosures**: IRB (not applicable — no human subjects), funding, competing interests, and any conflicts not covered by the institutional history — entered in the form, not the PDF (they stay hidden from reviewers).
7. **Do NOT** link the arXiv version in the submission (double-blind maintained; reviewers must not be able to reach a named version from the submission). Post arXiv (per `arxiv-submission/README-upload.md`) with the real identity — that is a separate, permitted preprint.
8. **After submission**: the email will ask for AE recommendations; respond. Watch for the public-availability phase; respond to reviews within ~2 weeks of the 3rd review if revisions are requested.

## C. Package contents (`paper/submission/`)

- `manuscript.tex` (+ `.pdf`, `.bbl`, figures, `tmlr.sty`, `tmlr.bst`) — anonymized submission source/PDF
- `supplementary/companion.tex/.bib` (+ `.pdf`) — anonymized companion technical report
- `supplementary/sigma-trap-code-data.zip` — code + config + raw data
- `cover-letter.md` — JAIR desk-rejection narrative (anonymized)
- `reviewer-summary.md` — one-page "How the paper changed"
- `compliance-checklist.md` — this document

**Note**: the anonymized sources (`manuscript.tex`, `supplementary/companion.tex`, `supplementary/companion.bib`, `supplementary/README.md`, the three docs) are tracked in git; compiled PDFs, the zip, and derived copies are gitignored.

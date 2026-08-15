# JAIR Submission Guide — Σ-Model Paper

## 1. Prerequisites

- **JAIR account:** Register at <https://jair.org/index.php/jair/user/register>
- **Paper readiness:** See `documentation/verification_report.md` (6/6 conditions met)
- **LaTeX:** TeX Live 2024+ with `latexmk`
- **Venv:** `source hbar_env/bin/activate`

## 2. Pre-Submission Checklist

Check each before uploading:

- [ ] **Double-blind:** Author block = `\author{Anonymous Author(s)}`, `\email{---}`, dummy affiliation (lines 77–85), PDF metadata `pdfauthor={Anonymous}`
- [ ] **Reproducibility checklist:** Filled in Appendix §D (lines 2821–2954). **Mandatory — desk reject if missing.**
- [ ] **Structured abstract:** Present (Problem/Method/Results/Conclusion). Encouraged, not mandatory.
- [ ] **No ACM CCS Concepts or Keywords** (JAIR forbids them)
- [ ] **No identifying self-citations** ("our previous work", "forthcoming")
- [ ] **Figures readable in grayscale** (Okabe-Ito palette used throughout)
- [ ] **No AI tools cited as authors** (policy requires human authorship only)
- [ ] **Originality:** Work not published/submitted elsewhere (conference extension OK — disclose at submission)

## 3. Build the Submission PDF

```bash
source hbar_env/bin/activate
cd paper/
make clean
make pdf
```

Verify: `manuscript.pdf` — 47 pages, ~2 MB, no errors in log.

## 4. Submission Wizard

Navigate to <https://jair.org/index.php/jair/submission/wizard>. 5 steps:

### Step 1 — Start
- Select Section: **Articles** (default)

### Step 2 — Upload Submission
- Upload `paper/manuscript.pdf`

### Step 3 — Enter Metadata
- **Title:** The Σ-Model: Schema-Coherence Suppression as the Origin of Compositional Generalisation Failure — A Dynamical-Systems Framework for Generalisation Failure
- **Abstract:** Paste from `manuscript.tex` (structured: Problem, Method, Results, Conclusion)
- **List of Contributors:** 1 author
  - Given Name: Basri
  - Family Name: Amsyar
  - Preferred Public Name: Basyirin Amsyar Basri
  - Email: basyirin.basri@gmail.com
  - Affiliation: Independent Researcher
  - Country: Malaysia
  - Bio: Independent Researcher, Malaysia
  - ORCID iD: (optional)
- **Categories:** Primary — `cs.LG`; Secondary — `cs.AI`, `q-bio.NC`
- **Keywords:** compositional generalisation, schema coherence, neural ODEs, dynamical systems, curriculum learning
- **References:** Leave blank (bibliography embedded in PDF, not re-entered)

### Step 4 — Confirm Declarations
Check all boxes confirming:
- [ ] Work is original and not under review elsewhere
- [ ] If extending a conference paper, the JAIR version contains significant new material
- [ ] AI tools used only as assistants, not as authors
- [ ] Reproducibility checklist is completed
- [ ] Compliance with JAIR's ethical guidelines

### Step 5 — Survey Questions (Mandatory)
Three survey questions about the submission (topic area, special track interest, etc.). Answer truthfully. Submission cannot proceed without these.

### Finalize
Click **Submit**. You'll receive a confirmation email with a submission ID.

## 5. Post-Submission

- **Track status:** Dashboard at <https://jair.org/index.php/jair/author/submissions>
- **Response time:** JAIR targets quick turnaround. Decisions within weeks to months.
- **Resubmission:** If asked for major revision, submit as new via the wizard (not directly to editor). Reference the original submission ID in the cover letter.
- **Contact:** For submission issues — use the dashboard messaging system. For template/style questions — `editors@jair.org`.

## 6. Camera-Ready (If Accepted)

Once accepted, you have **2 months** to submit final files.

### Changes to `manuscript.tex`

| Item | Submission | Camera-Ready |
|------|-----------|--------------|
| Document class | `\documentclass[manuscript,screen,review]{jair}` | `\documentclass[]{jair}` |
| Author block | Anonymous | Real name + affiliation |
| DOI | `\acmDOI{10.1613/jair.1.xxxxx}` | Update with actual DOI from JAIR |
| Volume/Article | Placeholder | Update from editor |
| `\JAIRAE{}` | Not present | Add `\JAIRAE{Assigned Editor Name}` |
| `\received{}` | Not present | Add `\received{DD Month YYYY}`, `\received[accepted]{DD Month YYYY}` |
| Reproducibility checklist | Included as appendix | **Remove** (review only) |

### Files to Upload
1. **PDF** — `manuscript.pdf` (final formatted)
2. **Source archive** — tar.gz containing:
   - `manuscript.tex`
   - `bibliography.bib`
   - `figures/*` (all 10 figure files)
   - `jair.cls`, `acmart.cls`, `ACM-Reference-Format.bst`
3. **Online appendices** (optional) — source code, extended results, data

Generate the source archive:
```bash
cd paper/ && make arxiv
# Output: ../arxiv-submission/sigma-arxiv-submission.tar.gz
```

Upload via the JAIR dashboard: add a Discussion item and attach files.

### Final Checks Before Upload
- [ ] Copyright footer correct (`\setcopyright{cc}` — CC BY 4.0)
- [ ] Proofread once more
- [ ] Section titles capitalized
- [ ] No `\vspace` for spacing adjustment (JAIR style disallows)
- [ ] Source code release form signed (if applicable)

## 7. Resources

| Resource | URL |
|----------|-----|
| JAIR submission page | <https://jair.org/index.php/jair/submission/wizard> |
| JAIR author instructions | <https://jair.org/index.php/jair/authorinstrs> |
| JAIR submission requirements | <https://jair.org/index.php/jair/about/submissions> |
| JAIR FAQ | <https://jair.org/index.php/jair/faq> |
| JAIR template (Overleaf) | <https://www.overleaf.com/latex/templates/jair-journal-of-artificial-intelligence-research/xzmcgtqdjftf> |
| Verification report | `documentation/verification_report.md` |
| Claims registry | `docs/claims-registry.md` |
| Contact for this paper | `basyirin.basri@gmail.com` |

---

**Last updated:** 2026-06-24

**Paper:** Σ-Model v3.0+ — JAIR submission

# Phase 11 — Pre-Submission Packaging & Meta-Documentation

**RPF v2.0:** Git tag `p11-packaged` · Duration 1–2d · GPU 0 · RACI: Agent **R** / PI **A** (48h gate) · Abort: venue format fails ×2 → escalate · Acceptance: Zenodo DOI + Software Heritage identifier, submission checklist 0 unchecked, plain-language summary ≤500 words, standards Deltas updated · *Pending.*

**Phase ID:** P11  
**Phase Title:** Anonymized Supplementary Packaging, Open-Source Release Preparation, and Meta-Documentation Refresh  
**Status:** Pending  
**Duration:** 1 Day  
**Dependencies:** P10 (GO directive required)  
**Executor:** Agent (85%) / Human-Gate (15%)  
**Deliverables:** `paper/writing/supplementary/paper-code-data.zip`, updated `paper/meta/*`, `paper/decisions/ADR-011_presubmission_package.md`

---

## 1. Purpose & Scope
Package all external deliverables for conference submission (camera-ready PDF, anonymized code and data ZIP, data cards, cover letter), conduct double-blind anonymization audits, and refresh the project's meta-documentation.

---

## 2. Exhaustive Tasks & Subtasks

### Task 11.1: Anonymized Supplementary Code & Data Packaging
1. **Prepare Anonymized Code Bundle:**
   - Copy `paper/src/`, `paper/experiments/configs/`, `paper/Makefile`, and reproduction scripts into a staging directory.
   - Run anonymization linter:
     - Strip author names, affiliations, GitHub usernames, and absolute filesystem paths (`/home/bigbasy/...`).
     - Replace repository URLs with generic placeholders (`https://anonymous.4open.science/r/...`).
2. **Package Sample Data & Checkpoints:**
   - Include processed tidy data tables (`data/processed/`) and a minimal subset of raw evaluation checkpoints for quick verification.
   - Include `README_reproduce.md` with 3-line reproduction instructions.
3. **Compress to Supplementary Archive:**
   - Create `paper/writing/supplementary/paper-code-data.zip` (verify size $\le 100$ MB).

### Task 11.2: Double-Blind Anonymity Compliance Audit (CC.5.2)
1. Run automated string scanner on `paper/writing/manuscript.pdf` and `paper-code-data.zip`:
   - Assert zero matches for author name, institution name, grant numbers, or private repository URLs.
2. Confirm that all self-citations are referenced in third person ("Prior work in [1] showed..." rather than "In our previous work [1]...").

### Task 11.3: Meta-Documentation & Standards Deltas Refresh
1. Update `paper/meta/README.md` with complete abstract, headline findings, and public reproduction commands.
2. Update `paper/planning/standards.md` Deltas section recording final lessons learned and rule outcomes.
3. Emit `paper/decisions/ADR-011_presubmission_package.md`.

---

## 3. Human Gates
- `[HUMAN-GATE]` Principal Investigator reviews the final PDF and unzips and tests the anonymized supplementary bundle on a clean machine before submission.

---

## 4. Machine-Checkable Exit Criteria
- [ ] `paper/writing/supplementary/paper-code-data.zip` exists and unzips cleanly.
- [ ] Anonymization scanner reports 0 violations in PDF and code bundle.
- [ ] `paper/meta/README.md` updated.
- [ ] `paper/decisions/ADR-011_presubmission_package.md` committed.
- [ ] `[HUMAN-GATE]` Package approved.

---

## 5. Deliverables & Artifacts
- Supplementary bundle: `paper/writing/supplementary/paper-code-data.zip`
- Updated meta docs: `paper/meta/README.md`, `paper/meta/ENVIRONMENT.md`
- Decision record: `paper/decisions/ADR-011_presubmission_package.md`

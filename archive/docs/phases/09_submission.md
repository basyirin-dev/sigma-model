# Phase 09 — Submission, Rebuttal & Release

**Deadline**: 1 Aug 2027
**Dependencies**: Phase 08 (paper draft)
**Output**: NeurIPS submission, reviews addressed, PfamCG-1.0 released, code released

---

### Task 9.1: NeurIPS submission

- [ ] 9.1.1: Verify NeurIPS 2027 formatting requirements:
  - 8-page limit (plus unlimited references)
  - Anonymous submission (double-blind review)
  - NeurIPS style file: `neurips_2027.sty`
  - No author names in PDF metadata
  - Supplementary material: PDF only (no code in supplementary for initial submission)
- [ ] 9.1.2: Final proofread:
  - Spell-check entire manuscript
  - Verify all figure references are correct (Figure 1–6)
  - Verify all claim anchors are present
  - Verify bibliography completeness (all cited works in bib file, no dangling references)
- [ ] 9.1.3: Upload to NeurIPS CMT (Conference Management Toolkit):
  - Title: "The Sigma Model on Natural Data: Compositional Generalisation Failure in Protein Domain Architectures"
  - Abstract (250 words max)
  - Subject areas: [ML: Deep Learning Architectures], [ML: Applications: Life Sciences]
  - Keywords: compositional generalisation, protein domains, schema coherence, bifurcation
- [ ] 9.1.4: Submit supplementary material (PDF, ≤ 10MB)
- [ ] 9.1.5: Confirm submission: download PDF from CMT, verify it renders correctly

### Task 9.2: Rebuttal preparation

- [ ] 9.2.1: Monitor reviews (Jun–Jul 2027):
  - NeurIPS reviews typically arrive 4–6 weeks after deadline
  - Read each review carefully; categorise issues:
    - **Clarity issues**: sections that confused reviewers → revise prose
    - **Technical issues**: methodological concerns → prepare technical response with additional analysis
    - **Missing experiments**: reviewer requests → prioritise for rebuttal
    - **Comparison with baselines**: add comparisons if missing
- [ ] 9.2.2: Prepare rebuttal document:
  - Address each reviewer point by point
  - For clarity issues: paste revised text
  - For technical issues: provide additional analysis or proof
  - For missing experiments: run quick additional experiments if feasible (1–2 weeks)
  - Maximum 1 page (NeurIPS rebuttal limit)
- [ ] 9.2.3: If additional experiments are needed:
  - Priority order: (1) baseline comparisons, (2) ablation studies, (3) additional statistical tests
  - Use existing infrastructure from Phases 04–07 to run quickly

### Task 9.3: Benchmark release

- [ ] 9.3.1: Release PfamCG-1.0 benchmark:
  - Create GitHub release in this repo (tag: `pfamcg-1.0`)
  - Include: data files, evaluation script, baseline scores, README
  - DOI via Zenodo (using existing DOI infrastructure from CITATION.cff)
- [ ] 9.3.2: Upload to HuggingFace Datasets:
  - Repository: `https://huggingface.co/datasets/basyirin-dev/PfamCG`
  - Include dataset card, evaluation script, baseline scores
  - Make public after paper acceptance (or at paper public release)

### Task 9.4: Code release

- [ ] 9.4.1: Prepare code for public release:
  - Verify no hardcoded paths (Kaggle-specific paths should be auto-detected or configurable)
  - Add installation instructions to `AGENTS.md` (protein-specific setup)
  - Verify all tests pass on a clean environment
  - Add example notebook: `experiments/pfam-reproduction.ipynb` — miniature version that runs in 1 hour
- [ ] 9.4.2: Update CITATION.cff for the NeurIPS paper:
  - Add second entry with paper DOI and venue
  - Keep the JAIR paper as primary citation
- [ ] 9.4.3: Update CHANGELOG.md with Phase 00–09 completion notes

### Task 9.5: Post-acceptance (contingent)

- [ ] 9.5.1: If accepted to NeurIPS:
  - Prepare camera-ready version (fix minor formatting issues, add acknowledgements)
  - Upload final version to CMT
  - Register for conference (virtual or in-person)
  - Prepare poster/presentation
- [ ] 9.5.2: If rejected:
  - Analyse reviews: are the issues fixable with 1–2 months of work?
  - Target venues in order: ICML 2028 → PLOS Computational Biology → Nature Machine Intelligence
  - For ICML 2028: add more baselines, strengthen the PfamCG-1.0 contribution
  - For PLOS Comp Bio: reframe as biological methodology paper
  - For Nat Mach Intell: require breakthrough results (may not be appropriate)
- [ ] 9.5.3: If invited to revise (NeurIPS "revise and resubmit" track):
  - Address specific revision requests point by point
  - Resubmit within the revision window

### Task 9.6: Programme-level documentation

- [ ] 9.6.1: Write post-mortem document `docs/lab-notebooks/2027-08-protein-paper-postmortem.md`:
  - What worked: which phases completed on time, which tasks were underestimated
  - What didn't: unexpected blockers, null results, Kaggle limitations
  - Lessons for Paper 3 (training algorithm, venue TBD)
- [ ] 9.6.2: Update `phase-roadmap.md` with actual completion dates
- [ ] 9.6.3: Clean up: archive intermediate results, remove temporary files

---

**Phase 09 Exit Criteria**:
- [ ] NeurIPS 2027 paper submitted (or alternative venue if deferred)
- [ ] Reviews received and rebuttal submitted
- [ ] PfamCG-1.0 benchmark released on GitHub and HuggingFace
- [ ] Code released with reproduction notebook
- [ ] Post-mortem written
- [ ] `phase-roadmap.md` updated with actual status

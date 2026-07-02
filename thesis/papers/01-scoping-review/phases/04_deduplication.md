# Phase 4 — Deduplication & Reference Management

**Duration**: 1 week (Month 2)
**Deadline**: 2026-08-20
**Dependencies**: Phase 3 (all search results collected)
**Output**: Deduplicated, curated library ready for screening

---

### Task 4.1: Import and Merge

- [ ] 4.1.1: Import all search results into reference manager (Zotero or manual BibTeX management)
- [ ] 4.1.2: Merge results from all databases into a single library
- [ ] 4.1.3: Tag each entry with source database name
- [ ] 4.1.4: Export unified library as `.bib` and `.csv` for reproducibility

### Task 4.2: Automated Deduplication

- [ ] 4.2.1: Run automated deduplication on title match (case-insensitive)
- [ ] 4.2.2: Run automated deduplication on DOI match
- [ ] 4.2.3: Flag near-duplicates (title similarity > 0.9) for manual review
- [ ] 4.2.4: Record deduplication statistics: total before, duplicates removed, total after

### Task 4.3: Manual Deduplication Review

- [ ] 4.3.1: Review flagged near-duplicates, manually resolve each
- [ ] 4.3.2: Check for multi-database entries of same paper (same paper in Scopus + WoS + arXiv)
- [ ] 4.3.3: For preprints later published in peer-reviewed venues: keep the more complete version, note the preprint in a tag
- [ ] 4.3.4: Record manual deduplication decisions

### Task 4.4: Reference Cleanup

- [ ] 4.4.1: Check all entries for missing required fields (title, year, author, source)
- [ ] 4.4.2: Check for encoding errors in titles/abstracts (especially from RIS imports)
- [ ] 4.4.3: Standardize field formatting (e.g., page numbers, DOI format)
- [ ] 4.4.4: Tag entries with their source database
- [ ] 4.4.5: Export cleaned, deduplicated library as `research/clean-library.bib` and `research/clean-library.csv`

### Task 4.5: Screening Infrastructure

- [ ] 4.5.1: Set up screening workflow (spreadsheet, Python script, or screening tool)
- [ ] 4.5.2: Create screening columns: title, abstract, decision (include/exclude/unsure), reason, notes
- [ ] 4.5.3: Create CSV export with all deduplicated papers for Phase 5 screening
- [ ] 4.5.4: Satisfy CC.4.2 — screening data structure ready

---

**Phase 4 Exit Criteria**:
- [ ] All database results merged and deduplicated
- [ ] Deduplication statistics recorded
- [ ] Clean library exported as `.bib` and `.csv`
- [ ] Screening infrastructure set up
- [ ] CC.4.1, CC.4.2 satisfied
- [ ] CC.5.3 satisfied — phase completion committed

# Phase 4 — Deduplication & Reference Management

**Duration**: 1 week (Month 2)
**Deadline**: 2026-08-21
**Dependencies**: Phase 3 (raw search results collected)
**Output**: Clean, deduplicated reference library ready for screening

---

### Task 4.1: Import and Merge

- [ ] 4.1.1: Import all search results into reference management software (Zotero or Mendeley)
- [ ] 4.1.2: Create a dedicated Paper 02 collection / group library
- [ ] 4.1.3: Merge all database results into a single master library
- [ ] 4.1.4: Record total number of records imported

### Task 4.2: Automated Deduplication

- [ ] 4.2.1: Run automated deduplication in reference manager (match on title, DOI, author-year)
- [ ] 4.2.2: Review the duplicate candidates — confirm true duplicates vs near-matches
- [ ] 4.2.3: Remove confirmed duplicates, keeping the most complete record
- [ ] 4.2.4: Record deduplication statistics: total records before, duplicates removed, records after
- [ ] 4.2.5: Satisfy CC.4.1 — deduplication log stored in `research/deduplication-log.md`

### Task 4.3: Manual Deduplication

- [ ] 4.3.1: Sort by title and manually scan for near-duplicates missed by automated tool (e.g., arXiv preprint + published version)
- [ ] 4.3.2: For arXiv preprint + peer-reviewed paper: keep the peer-reviewed version; tag the preprint as "superseded"
- [ ] 4.3.3: For identical content in multiple databases: keep one entry, note the databases of origin
- [ ] 4.3.4: Record all manual deduplication decisions

### Task 4.4: Reference Standardization

- [ ] 4.4.1: Standardize field formatting (journal names, author names, publication types)
- [ ] 4.4.2: Check for missing DOIs — retrieve via Crossref API if missing
- [ ] 4.4.3: Check for missing abstracts — retrieve if possible
- [ ] 4.4.4: Tag each record with its source database(s) for PRISMA flow diagram
- [ ] 4.4.5: Assign a unique Paper 02 ID to each record (P0001–PXXXX) for tracking across phases

### Task 4.5: Export for Screening

- [ ] 4.5.1: Export deduplicated library as CSV with fields: ID, title, abstract, authors, year, journal, DOI, keywords, source databases
- [ ] 4.5.2: Export as RIS for import into screening tool (Rayyan, Covidence, or custom Python script)
- [ ] 4.5.3: Archive clean library in `research/clean-library/`
- [ ] 4.5.4: Update PRISMA flow diagram initial numbers: records identified, duplicates removed, records for screening
- [ ] 4.5.5: Satisfy CC.4.1 — clean library committed; OSF backup if file size > 50 MB

---

**Phase 4 Exit Criteria**:
- [ ] All records imported and merged into master library
- [ ] Automated deduplication completed with log
- [ ] Manual deduplication completed with decisions recorded
- [ ] Reference fields standardized (DOIs, abstracts, formats)
- [ ] Each record tagged with source database(s)
- [ ] CSV and RIS exports prepared for screening
- [ ] PRISMA flow diagram initial numbers recorded
- [ ] CC.4.1 satisfied
- [ ] CC.5.3 satisfied — phase completion committed

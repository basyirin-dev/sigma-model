# Phase 1 — Research Question & Protocol

**Duration**: 1 week (Month 1–2)
**Deadline**: 2026-07-30
**Dependencies**: Phase 0.5 (research artifacts completed)
**Output**: Registered protocol on OSF with finalized research question, objectives, and inclusion/exclusion criteria

---

### Task 1.1: Finalize Research Question

- [x] 1.1.1: Review Phase 0.5 research outputs — especially `research/landscape-boundary.md` and `research/gap-analysis.md`
- [x] 1.1.2: Refine the overarching research question using PCC (Population, Concept, Context) framework:
  - Population: AI/AGI research community
  - Concept: AGI safety frameworks, approaches, and failure modes
  - Context: Peer-reviewed and grey literature 2015–2026
  - **Final RQ**: "How is the landscape of AGI safety research structured in terms of subdomains, formal methods, and the treatment of internal representation structure, and what gaps exist that a schema-coherence framework could address?"
- [x] 1.1.3: Define 3-5 sub-questions (SQ1: subdomain taxonomy, SQ2: formal methods distribution, SQ3: internal representation structure in safety, SQ4: CG-alignment relationship, SQ5: schema-coherence gaps)
- [x] 1.1.4: Draft explicit objectives using SMART framework (5 objectives: O1 taxonomy, O2 methods catalogue, O3 structure-safety map, O4 gap analysis, O5 thesis-aligned evidence map)
- [x] 1.1.5: Satisfy CC.1.4 — inclusion/exclusion criteria drafted concurrently with question (see `01_protocol_draft.md` §5)

### Task 1.2: Define Inclusion/Exclusion Criteria

- [x] 1.2.1: Inclusion criteria:
  - I1: English (justified per `research/publication-venues.md`)
  - I2: 2015–March 2026 (justified per `research/chronological-development.md`; captures 3 waves, 81.58% of papers)
  - I3: Addresses ≥1 AGI safety subdomain (21-term vocabulary; justified per `research/existing-reviews.md` scope fragmentation)
  - I4: Peer-reviewed article, arXiv preprint, technical report, or substantive blog/forum post (justified per `research/quality-criteria.md`; ~50% preprint rate; Gyevnar 2025 limitation)
  - I5: Relevance to structural AGI safety (justified per `research/landscape-boundary.md` structural vs narrow boundary)
- [x] 1.2.2: Exclusion criteria:
  - E1: Narrow AI safety only (well-covered by existing reviews)
  - E2: Not in English
  - E3: Pure opinion without substantive scholarly content
  - E4: Duplicate/overlapping publications (keep most complete)
  - E5: Pure capability development without safety framing
  - E6: Predatory or questionable venues (per quality-criteria.md D1 negative filter)
- [x] 1.2.3: Justify each criterion with reference to Phase 0.5 findings — completed in `01_protocol_draft.md` §5 with direct citations to `research/existing-reviews.md`, `research/landscape-boundary.md`, `research/quality-criteria.md`, `research/chronological-development.md`, `research/master-summary.md`, `research/publication-venues.md`, and `research/schema-coherence-mapping.md`
- [x] 1.2.4: Satisfy CC.1.4 — criteria explicitly stated in `01_protocol_draft.md` §5.1–5.2 before screening phase

### Task 1.3: Write Protocol

- [x] 1.3.1: Draft protocol following PRISMA-ScR guidelines — completed in `01_protocol_draft.md`:
  - Title (§1) and abstract (§2)
  - Introduction / rationale (§3)
  - Research question(s) and objectives (§4)
  - Eligibility criteria (§5)
  - Search strategy (§6 — databases, date limits, query strings)
  - Study selection process (§7)
  - Data charting process (§8)
  - Synthesis approach (§9)
- [x] 1.3.2: Staged search approach selected — iterative (Scopus→arXiv→WoS→ACM/IEEE→PhilPapers→grey), see `01_protocol_draft.md` §6.4 and `research/search-terms.md` §4
- [x] 1.3.3: Protocol length: ~3,800 words (~8 pages) — within 5–10 page target
- [x] 1.3.4: Satisfy CC.1.7 — protocol PDF generated at `phases/01_protocol_draft.pdf`; see `01_osf_registration.md` for OSF registration steps

### Task 1.4: Pilot Search Test

- [x] 1.4.1: Choose one representative database (Scopus unavailable — no institutional access). Dual-database strategy: arXiv (grey lit) + OpenAlex (peer-reviewed proxy)
- [x] 1.4.2: Execute preliminary search with draft terms from `research/search-terms.md` — arXiv F2 (safety ∩ generalisation, 30 results) + OpenAlex F2 (deceptive alignment/mesa-opt/CG × safety, ~40 results)
- [x] 1.4.3: Review results to verify sensitivity/specificity — 7/8 known key papers retrieved; false positives manageable (multimodal "alignment" uses); specificity acceptable
- [x] 1.4.4: Adjust inclusion/exclusion criteria — no changes needed; existing I3/I5 correctly exclude observed false positives
- [x] 1.4.5: Record pilot search details — logged at `01_pilot_results.md` (databases, dates, strings, yield, adjustments)
- [x] 1.4.6: Satisfy CC.1.5 — extraction template piloted on 3 papers (Hubinger 2019, Pepin Lehalleur 2025, Siddiqui 2026); 3 template adjustments applied (developmental interpretability added; `structure_safety_link` refined; `relevance_to_review` guidance added)

### Task 1.5: Protocol Registration

- [x] 1.5.1: Create OSF project for Paper 01 — https://osf.io/ntuh2/
- [x] 1.5.2: Upload protocol document (`01_protocol_draft.pdf`)
- [x] 1.5.3: Make protocol publicly viewable — Generalized Systematic Review Registration template
- [x] 1.5.4: Record OSF link in `README.md`
- [x] 1.5.5: Satisfy CC.1.3 — protocol registered prior to formal search

---

**Phase 1 Exit Criteria**:
- [x] Research question finalized with PCC framework (see `01_protocol_draft.md` §4)
- [x] Inclusion/exclusion criteria explicitly stated (see `01_protocol_draft.md` §5)
- [x] Protocol registered on OSF with public link — https://osf.io/ntuh2/
- [x] Pilot search executed and results reviewed (see `01_pilot_results.md`)
- [x] CC.1.4 satisfied (I/E criteria stated before screening)
- [x] CC.1.3 — search strategy reported (see `01_protocol_draft.md` §6 and `research/search-terms.md`)
- [x] CC.1.5 — data charting form developed and piloted (see `research/extraction-template.md`; 3 test papers, 3 adjustments applied)
- [x] CC.1.7 — OSF registration complete (https://osf.io/ntuh2/)
- [x] CC.5.3 satisfied — phase completion committed

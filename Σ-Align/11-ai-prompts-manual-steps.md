# AI Prompts for the Manual Steps — Σ-Align Phase 12 prep

Each prompt is self-contained (context + task + constraints + output). Replace `<...>` with your details. File paths are relative to the repo root.

---

## P1. Stranger-test voice audit (substitute for a human stranger)

```
You are an independent manuscript editor who knows NOTHING about the Σ-Align thesis,
the σ-trap hypothesis, or its author. Do not assume any background beyond the text.

Read thesis/publications/01-scoping-review/manuscript.tex in full.

Answer ONLY these three questions, each with a yes/no and a quoted example:
1. Does this read like an objective map of the AI-safety field, or like an argument
   for a specific theory? If any sentence argues for schema-coherence or the σ-trap
   as a conclusion (rather than using it as a search lens), quote it.
2. Would a reviewer suspect the author has a stake in a framework being validated?
   Flag any wording that sells a hypothesis (e.g. "confirms", "demonstrates that X
   is the cause", "the optimal path") rather than reports evidence.
3. Is the author's positionality disclosed where a reader first needs it?

Then list every sentence that fails the standalone-voice test with its section,
and rewrite each in neutral voice. Do NOT change any numbers or citations.
```

---

## P2. Venue fit analysis (substitute for the venue decision)

```
You are a scholarly-publishing strategist. The manuscript is a PRISMA-ScR scoping
review of the AGI-safety literature: 1,268 studies, 6 databases + grey literature,
21 pages, ~7,900 words, 50 references, 3 figures + 5 tables, ACM acmart class.
Its headline finding is a "credibility inversion": the largest empirical strand
(evaluation, 281 studies) has the lowest credibility (17.8% tier A+B) while the
most credible strands (governance, formal theory) are the least empirical.
Prior reviews (Triantafyllopoulos 83 studies, Shen 400+, Gyevnar 383, McLean 16,
Slattery 777) each map only part of this space; no prior review covers subdomains +
methods/formalism census + internal-representation treatment together.

Evaluate fit (fit score /10 + one-paragraph rationale each) for:
1. ACM Computing Surveys
2. Artificial Intelligence Review
3. Journal of AI Research
4. AI & Society / AI and Ethics
5. ACM/IMS Transactions on Data Science
6. TMLR

Consider: scope match, desk-rejection risk, timeline, solo-author + LLM-assisted
pipeline disclosure, and the credibility-inversion novelty. Rank the top 3 and
state which single venue you would submit to first and why.
```

---

## P3. Draft the submission cover letter

```
You are drafting a submission cover letter for a journal editor. Use ONLY the
bullet points in thesis/chapters/02-agi-safety-landscape/phases/12_paper_extraction.md (section
"Cover-letter bullet points") and the manuscript title/abstract. Do NOT invent
facts, do NOT mention any thesis, thesis-by-publication, 9-paper arc, or future
papers, and do NOT mention the author's other research programme.

Cover letter structure: (1) what is being submitted + venue; (2) the contribution
in 3-4 sentences (scale, first credibility-stratified map, credibility-inversion
finding); (3) fit with the journal's scope; (4) transparency paragraph (OSF
registration, PRISMA-ScR, hybrid extraction with human-adjudicated spot-check at
80-93% agreement, search-sensitivity analysis); (5) statement of originality and
no-conflict. Max 500 words. End with 5 explicit claims in the letter that you
could not verify and should be double-checked by the author.
```

---

## P4. Preprint-abstract consistency check

```
Read thesis/publications/01-scoping-review/manuscript.tex (the structured
abstract) and the file <your-abstract.txt> (the abstract you intend to post on
arXiv/SSRN). Compare them and report:
1. Word count of each (the journal limit is 250).
2. Any sentence in the preprint version that frames the work as a thesis chapter,
   part of a larger programme, or preliminary ("first step toward", "Chapter 1").
3. Any factual discrepancy in numbers (study counts, percentages, years).
4. A single unified abstract text (<= 250 words) that is identical in substance
   to the journal version and safe to post as a preprint.
```

---

## P5. Supplementary-data quality audit (pre-package check)

```
You are a data-quality auditor. Load thesis/chapters/02-agi-safety-landscape/research/
charted-data.csv and quality-scores.csv (1,268 rows each).

Audit and report:
1. Row count and unique study_id count in each (must both be 1,268).
2. Duplicate paper_id/study_id rows; duplicate titles (case-insensitive).
3. Column-level fill rates; list any column below 50% fill.
4. Value-consistency checks: every publication-type value is in the allowed set;
   every subdomain value is in the allowed set; year values are integers 2015-2026
   or empty; quality tiers are A-E and composite scores within 1.0-4.0.
5. Join integrity: all study_ids in quality-scores.csv exist in charted-data.csv
   and vice versa.
6. Anomaly list: top 10 rows most likely to contain extraction errors.
Output a PASS/FAIL per check with counts. Do NOT modify the files; produce a
report I can paste into the supplementary README.
```

---

## P6. DOI/URL verification pass

```
You have web access. Read the reference list in
thesis/publications/01-scoping-review/manuscript.tex (the bibliography is
compiled from thesis/bibliography.bib + research/included-studies.bib; the cited
keys are the ~50 entries with \cite commands).

For every reference that carries a DOI or URL:
1. Fetch the DOI via https://doi.org/<doi> (or the URL) and record HTTP status.
2. If it resolves, confirm the title/author/year match the bib entry; flag any
   mismatch.
3. If it does NOT resolve, suggest the correct DOI/URL from a search, and mark it
   'UNRESOLVED' if you cannot confirm.
Output a table: key | DOI/URL | status (OK/MISMATCH/UNRESOLVED) | corrected value.
Do not edit the bib files; produce the table only.
```

---

## P7. Paper 06 revision plan (JAIR desk rejection → next step)

```
You are a research strategist. Read Σ-Align/10-jair-desk-rejection-response.md
(the JAIR desk-rejection analysis: grounds = unclear exposition/notation, overbroad
claims, insufficient breadth-of-significance) and skim the manuscript under
paper/manuscript.tex.

Produce a revision plan with two options:
A. Revise for resubmission to JAIR (or another strong AI journal).
B. Pivot to TMLR (fast, certified review) — adjusting scope expectations.
For each option: (1) the 3-5 highest-leverage changes that directly address the
three rejection grounds; (2) an estimate of the revision effort in weeks (solo
author); (3) which sections to cut or split into a separate paper; (4) a
recommended target length and abstract rewrite (< 200 words).
Then recommend ONE option with a one-paragraph justification, considering the
thesis timeline (Empirical #1 is complete; the roadmap now treats Paper 06 as
'🟠 Revising').
```

---

## P8. University thesis-submission rules lookup

```
You have web access. The author is a pre-university foundation (PASUM) student
aged 18 planning an independent research thesis-by-publication over ~36 months,
affiliated with <your institution, e.g. Universiti Malaya> (confirm the actual
affiliation).

Research and report:
1. Does <institution> allow a thesis-by-publication / compilation format? Quote
   the governing rule or document with a link.
2. For that format: the minimum number of papers, and whether 'under review' or
   preprint papers count toward the thesis at submission.
3. For the MONOGRAPH format at the same institution: page/word norms and whether
   published papers can be embedded as chapters.
4. Any age/entry requirements that would affect a non-degree student submitting
   independent research (if none found, say so explicitly).
5. A one-paragraph recommendation: which format the author should plan for, with
   the evidence.
Mark any claim you could not verify as UNVERIFIED. Cite every source with a URL.
```

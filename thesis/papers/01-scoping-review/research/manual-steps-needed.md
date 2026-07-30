# Paper 01 Phase 3 — Manual Steps Required

**Today's date**: 2026-07-30 (use this as reference; fill in your actual execution date for each step below)
**Protocol reference**: See `thesis/papers/01-scoping-review/research/search-terms.md` for full string variants
**Output directory**: `research/search-results/`
**Log file**: `research/search-logs.md`

---

## Quick Reference: Recommended Execution Order

| Order | Database | String | Expected hits | Est. time |
|:-----:|:---------|:-------|:-------------:|:---------:|
| 1 | Scopus | F2 (+ F1, F3 optional) | 30-80 | 15 min |
| 2 | Web of Science | F2 (+ F1, F3 optional) | 20-50 | 10 min |
| 3 | ACM Digital Library | F2 | 15-40 | 10 min |
| 4 | IEEE Xplore | F2 | 10-25 | 10 min |
| 5 | PhilPapers | F3 (then F1, F2) | 5-20 | 10 min |
| 6 | Google Scholar | Top keywords | ~200 | 20 min |
| 7 | Grey literature | 8 sources | varies | 1-2 hrs |
| 8 | Remaining seed citations | 5 papers | varies | 30 min |
| 9 | Log & archive updates | — | — | 10 min |

**Total manual time**: approximately 3-4 hours in one sitting.

---

## Step 1: Scopus

**URL**: https://scopus.com
**Access**: UM OpenAthens (log in via institutional access)
**Output file**: `research/search-results/scopus-2026-XX-XX.ris`

### What to do

1. Open Scopus in your browser. Click "Sign in" → "Other institution login" → search for "University of Melbourne" → authenticate via UM OpenAthens.

2. Go to the **Advanced Search** tab (next to the basic search bar).

3. **Primary query (F2 — recommended extraction)** — paste this into the query box:
   ```
   TITLE-ABS-KEY( "AI alignment" OR "AGI safety" OR "mesa-optimization" OR "deceptive alignment" OR "inner alignment" OR "corrigibility" OR "reward hacking" OR "value alignment" )
   AND
   TITLE-ABS-KEY( "compositional generalization" OR "compositional generalisation" OR "systematic generalization" OR "compositional learning" OR "out-of-distribution generalization" OR "distribution shift" )
   ```

4. Click **Search**. Record the **number of results** shown (expected: 30-80).

5. **Export F2 results**:
   - Select all results (check the box at the top of the results list)
   - Click **Export** (top of results list)
   - Format: **RIS format** (Mendeley, EndNote, Zotero — all use the same `.ris`)
   - Select which fields to export: choose **"All available information"** or at minimum: Author(s), Title, Year, Source title, Volume/Issue, Pages, DOI, Abstract, Author Keywords, Link
   - Click **Export** and save the file as `scopus-2026-XX-XX.ris` in `research/search-results/`

6. **(Optional) F1 calibration** — run this separately and record the result count only (don't export unless < 500):
   ```
   TITLE-ABS-KEY( "AI alignment" OR "artificial intelligence alignment" OR "AGI safety"
   OR "value alignment" OR "mesa-optimization" OR "mesa-optimisation" OR "deceptive alignment"
   OR "inner alignment" OR "outer alignment" OR "corrigibility" OR "reward hacking"
   OR "specification gaming" OR "coherent extrapolated volition" OR "indirect normativity" )
   ```
   Expected: 1,500-2,500. Just record the number — too broad to screen.

7. **(Optional) F3 narrow** — run this and export if results > 0:
   ```
   TITLE-ABS-KEY( "AI alignment" OR "mesa-optimization" OR "deceptive alignment"
   OR "inner alignment" OR "goal misgeneralization" OR "value alignment" OR "corrigibility" )
   AND
   TITLE-ABS-KEY( "compositional generalization" OR "compositional generalisation" OR "systematic generalization"
   OR "compositional learning" OR "schema" OR "schematic" OR "representational structure"
   OR "latent structure" OR "internal representation" )
   AND
   TITLE-ABS-KEY( "safety" OR "alignment" OR "robustness" OR "interpretability" )
   ```
   Expected: 5-20. This is the **target thesis intersection** — if any results appear, they're high-value.

8. **Log results**: Open `research/search-logs.md`, find the Scopus section (§1.1), replace `(manual)` and `(pending)` with your date and result count.

---

## Step 2: Web of Science

**URL**: https://webofscience.com
**Access**: UM OpenAthens
**Output file**: `research/search-results/wos-2026-XX-XX.ris`

### What to do

1. Log in via UM OpenAthens. Select **Web of Science Core Collection**.

2. Click **Advanced Search**.

3. **Primary query (F2)** — paste the two `TS=` clauses on separate lines:
   ```
   TS=(( "AI alignment" OR "AGI safety" OR "mesa-optimization" OR "deceptive alignment" OR "inner alignment" OR "corrigibility" OR "reward hacking" ))
   AND
   TS=(( "compositional generalization" OR "compositional generalisation" OR "systematic generalization" OR "out-of-distribution generalization" OR "distribution shift" ))
   ```

4. **Important**: Make sure each `TS=(...)` group has double parentheses — `TS=((...))` not `TS=(...)`. WoS requires this for nested ORs.

5. Click **Search**. Record the result count (expected: 20-50).

6. **Export**:
   - Select all results
   - Click **Export** → **RIS (EndNote)** 
   - Choose: **Full Record + Cited References** (to get abstracts and DOIs)
   - Click **Export** and save as `wos-2026-XX-XX.ris`

7. **(Optional) F1 and F3** — same recommendation as Scopus. F1 for calibration, F3 if you want high-precision results. Strings are in `search-terms.md` Module 2.

8. **Log results**: Update the WoS section (§1.2) in `research/search-logs.md`.

---

## Step 3: ACM Digital Library

**URL**: https://dl.acm.org
**Access**: UM OpenAthens
**Output file**: `research/search-results/acm-2026-XX-XX.ris`

### What to do

1. Log in via UM OpenAthens. You may need to click "Institutional Sign In" and find "University of Melbourne".

2. Click **Advanced Search** (under the search bar).

3. **Primary query (F2)** — paste:
   ```
   [[Abstract: "AI alignment" OR "mesa-optimization" OR "deceptive alignment" OR "inner alignment" OR "corrigibility" OR "reward hacking"]]
   AND
   [[Abstract: "compositional generalization" OR "compositional generalisation" OR "systematic generalization" OR "compositional learning" OR "out-of-distribution generalization"]]
   ```

4. **ACM syntax note**: The `[[...]]` brackets are ACM's field syntax. Type or paste carefully — the brackets must be matched. Set the search scope to **"The ACM Full-Text Collection"**.

5. Click **Search**. Record results (expected: 15-40).

6. **Export**:
   - Select results (checkbox at top of list)
   - Click **Export** → choose **RIS**
   - Save as `acm-2026-XX-XX.ris`

7. **Log results**: Update ACM section (§1.3) in `research/search-logs.md`.

---

## Step 4: IEEE Xplore

**URL**: https://ieeexplore.ieee.org
**Access**: UM OpenAthens
**Output file**: `research/search-results/ieee-2026-XX-XX.ris`

### What to do

1. Log in via UM OpenAthens. Click "My Settings" → "Sign In" → "Institutional Sign In".

2. Click **Search** in the top navigation, then click **Command Search** (below the search bar — a link, easy to miss).

3. **Primary query (F2)** — paste into the Command Search box:
   ```
   ("Abstract":"AI alignment" OR "Abstract":"mesa-optimization" OR "Abstract":"deceptive alignment" OR "Abstract":"inner alignment")
   AND
   ("Abstract":"compositional generalization" OR "Abstract":"compositional generalisation" OR "Abstract":"systematic generalization" OR "Abstract":"out-of-distribution generalization")
   ```

4. **⚠️ 25-term clause limit**: IEEE imposes a **maximum of 25 terms per clause**. The F2 string above has exactly 4 terms in the first block and 4 in the second — well within the limit. **Do not add extra terms** to these clauses without counting. If you run F3 (which has more terms), split it into sub-queries.

5. Click **Search**. Record results (expected: 10-25).

6. **Export**:
   - Select all results
   - Click **Export** → choose **RIS** (labeled "Citations" → "RIS format")
   - Save as `ieee-2026-XX-XX.ris`

7. **Log results**: Update IEEE section (§1.4) in `research/search-logs.md`.

---

## Step 5: PhilPapers

**URL**: https://philpapers.org
**Access**: Open access (no login needed)
**Output file**: `research/search-results/philpapers-2026-XX-XX.txt`

### What to do

1. Go to https://philpapers.org.

2. **Find the category filter**: Look for a "Categories" dropdown or browse to "Philosophy of Artificial Intelligence" (the site's category hierarchy: Metaphysics and Epistemology → Philosophy of Science → Philosophy of AI, or just search for the category).

3. **Primary query (F3 — category-restricted)** — this is the most efficient:
   - Select category: **Philosophy of Artificial Intelligence**
   - Search box: `("alignment" OR "value" OR "corrigibility" OR "volition" OR "normativity")`
   - Record results (expected: 5-20)

4. **(Optional) F2** — run separately without category filter:
   ```
   ("AI alignment" OR "mesa-optimization" OR "deceptive alignment" OR "value alignment" OR "corrigibility")
   AND
   ("compositional generalization" OR "compositional generalisation" OR "systematic generalization" OR "schema" OR "representation")
   ```
   Expected: 1-5. Note the low yield — this intersection barely exists in philosophy.

5. **Export**: PhilPapers has limited export options. Use one of:
   - **Best**: Copy-paste results into a plain text file with titles, authors, and URLs
   - **Alternative**: Use PhilPapers' "Cite" feature for each relevant result
   - Save as `philpapers-2026-XX-XX.txt`

6. **Log results**: Update PhilPapers section (§1.6) in `research/search-logs.md`.

---

## Step 6: Google Scholar

**URL**: https://scholar.google.com
**Access**: Open access
**Output file**: `research/search-results/google-scholar-2026-XX-XX.csv`

### What to do

1. Open Google Scholar in your browser. **Do not log in** with a personal account (this can bias results based on your search history). Use an incognito/private window.

2. **Search queries** (run each separately, record results, collect top ~200 total):

   | Query | Purpose |
   |:------|:--------|
   | `"AI alignment" "compositional generalization"` | Core intersection |
   | `"AI alignment" "schema coherence"` | Schema link |
   | `"AGI safety" "compositional generalization"` | Safety + CG |
   | `"deceptive alignment" "compositional generalization"` | Narrow target |
   | `"mesa-optimization" "generalization"` | Mesa-opt link |

3. **Paging**: For each query, scroll through results until you hit ~200 total unique results across all queries. Scholar typically shows ~10 per page.

4. **Export method**:
   - **Option A (recommended)**: Use the **'Cite'** link under each result for ones you want to keep, or use a browser extension like **Zotero** connector — click the Zotero icon while on Scholar to batch-import results into a collection, then export from Zotero as RIS/CSV.
   - **Option B**: Manually copy titles, authors, year, and URL into a CSV with columns: `title, authors, year, url, abstract`
   - Save as `google-scholar-2026-XX-XX.csv`

5. **Log results**: Update Google Scholar section (§2.3) in `research/search-logs.md`.

---

## Step 7: Grey Literature Collection

For each source, spend 10-15 minutes browsing and collecting relevant items. Focus on **2022-2026** as the primary window.

### Source-by-source instructions

#### 7a. DeepMind Safety → https://deepmindsafetyresearch.com/
- Browse by topic: **Alignment**, **Safety**
- Look for technical reports on: reward hacking, specification gaming, goal misgeneralization, interpretability
- Download PDFs into `research/search-results/grey/` (create this directory if needed)
- Record: title, date, URL, brief relevance note

#### 7b. Anthropic → https://www.anthropic.com/research
- Filter by topic: **Safety**, **Interpretability**, **Alignment**
- Key papers to check: anything on "sleeper agents", "alignment faking", "superposition", "mechanistic interpretability"
- Download relevant PDFs

#### 7c. OpenAI → https://openai.com/safety/
- Check: safety research posts, preparedness framework, "weak-to-strong generalization"
- OpenAI publishes some work as blog posts that never appear in peer-reviewed databases

#### 7d. MIRI → https://intelligence.org/research/
- Focus on: corrigibility, value learning, logical uncertainty, decision theory
- Many foundational alignment papers live here and **never** got arXiv IDs
- **Important**: This is where Yudkowsky (2004) CEV and Soares et al. (2015) corrigibility live

#### 7e. ARC → https://evals.alignment.org/
- Collect: evaluation frameworks, dangerous-capability benchmarks
- Check for: scheming AIs evaluations, power-seeking benchmarks

#### 7f. AI Alignment Forum → https://www.alignmentforum.org/
- Search terms (use site search): `"compositional generalization"`, `"schema coherence"`, `"deceptive alignment"`, `"reward hacking"`
- Forum posts often contain substantive technical discussion that never becomes a paper
- For each found post: record URL, title, author, date

#### 7g. LessWrong → https://www.lesswrong.com/
- Search terms: `"schema coherence"`, `"alignment"`, `"compositional generalization"`, `"CEV"`
- Many foundational alignment concepts were first articulated here
- **Yudkowsky (2004)** CEV post search: search "coherent extrapolated volition" → find the original post

#### 7h. EA Forum → https://forum.effectivealtruism.org/
- Focus on: AI safety strategy, funding landscape, risk analysis
- Less technical, more strategic — useful for the discussion section of your review

#### 7i. Workshop proceedings → SafeAI, AISafety, ML Safety Workshops
- NeurIPS 2020-2025 Safety Workshop proceedings
- ICML 2020-2025 Alignment Workshop proceedings
- AAAI 2020-2025 AI Ethics and Safety tracks
- Access: Google "NeurIPS SafeAI workshop proceedings 202X" — most are open access on the workshop websites or CEUR-WS

### Grey literature recording format
For each item you collect, add a row to the grey literature table in `research/search-logs.md` (§3):
```
| Source | Title/Item | Date | URL | Status |
```

---

## Step 8: Manual Citation Chaining for Remaining Seeds

The following 5 seed papers could not be chained automatically. Do this for each:

1. **Yudkowsky (2004) — CEV**
   - Find at: https://www.lesswrong.com/tag/coherent-extrapolated-volition
   - Manual action: Scroll to bottom of the post/article, copy all reference links
   - Record in: `research/citation-chaining-log.md`

2. **Soares et al. (2015) — Corrigibility**
   - Try: Search Semantic Scholar (in browser) for "Soares corrigibility 2015"
   - If found: Use Semantic Scholar's "Citations" tab to see citing and cited papers
   - Copy the DOIs/arXiv IDs of the most relevant (~10 per paper)

3. **Hadfield-Menell et al. (2016) — Cooperative Inverse RL**
   - Try: Search Semantic Scholar or Google Scholar for the exact title
   - Same manual citation graph browsing as above

4. **Carlsmith (2023) — Existential Risk from Deceptive Alignment**
   - Open Philanthropy essay: Google "Carlsmith existential risk deceptive alignment"
   - Check footnotes/references for key citations

5. **Pepin Lehalleur et al. (2025) — Schemas** and **Wang & Murfet (2026) — SLT**
   - These are thesis-specific papers, likely unpublished or under review
   - Check whether they've been posted to arXiv since this session; if not, note them for manual reference extraction when they become available

---

## Step 9: Finalizing the Search Log

After completing all manual steps above:

1. **Open** `research/search-logs.md`

2. **For each database section**, verify:
   - `Date executed` is filled in (not `(manual)`)
   - `Results returned` has the actual number
   - `Export file` has the correct filename

3. **Verify the Summary Table** (§5):
   - Row 1 (Scopus): Date, hits, filename filled
   - Row 2 (WoS): same
   - Row 3 (ACM): same
   - Row 4 (IEEE): same
   - Row 6 (PhilPapers): same
   - Row 9 (Google Scholar): same
   - Row 10 (Grey literature): date and file count filled

4. **Calculate total unique hits** (approximate):
   - Sum all result counts from F2 queries across databases
   - Add grey literature items found
   - Add manual citation chaining candidates
   - Record this as the pre-deduplication total

5. **Calculate approximate total pool**:
   - Automated (arXiv + OpenAlex + citation chaining): **~1,200+ papers**
   - Manual (Scopus, WoS, ACM, IEEE, PhilPapers): **~80-200 more**
   - Grey literature: **~20-50 items**
   - **Estimated final pool**: **~1,300-1,500 records before deduplication**

6. **Git commit** (when ready):
   ```bash
   git add research/search-logs.md research/search-results/ research/citation-chaining-log.md
   git commit -m "[R][L][Δ] Phase 3: complete database search execution for Paper 01"
   ```

---

## Appendix: Pitfalls to Avoid

| Database | Common Pitfall | What to Do Instead |
|:---------|:---------------|:-------------------|
| Scopus | Precedence change: `AND` before `OR` in new Scopus (2025-) | Use parentheses liberally to force evaluation order |
| WoS | Double-parens required: `TS=((a OR b))` not `TS=(a OR b)` | Always use `TS=((...))` |
| ACM | `[[...]]` syntax is case-sensitive and browser-dependent | Copy-paste the exact string; verify brackets match |
| IEEE | 25-term clause limit — easy to exceed with F1 or F3 | Count terms before running; split into sub-queries if needed |
| PhilPapers | Category filter resets after each search | Re-apply "Philosophy of AI" category before each query |
| Google Scholar | Personal account biases results | Use incognito/private browsing window |
| Grey lit | Skimming too fast; missing key forum posts | Search each forum with at least 3 different query terms |

---

**Once all manual steps are complete, the Phase 3 exit criteria will be fully satisfied, and you can proceed to Phase 4 (Deduplication).**

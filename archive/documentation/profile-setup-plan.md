# Profile & Submission Plan: ORCID + Zenodo + GitHub + LinkedIn + OpenReview

---

## 1. Zenodo — New Manuscript Record

Create a **new** Zenodo record on your **ORCID-linked account**. Do NOT reuse the old software DOI (10.5281/zenodo.19495977) — that record is on an unmanaged account.

### Basic info

| Field | Value |
|-------|-------|
| Resource type | **Publication → Preprint** |
| DOI | Press **Reserve DOI** (answer "No" to "already have a DOI") |
| Title | The Σ-Model: Schema-Coherence Suppression as the Origin of Compositional Generalisation Failure — A Dynamical-Systems Framework for Generalisation Failure |
| Authors — Given name | (leave empty) |
| Authors — Family name | `Basyirin Amsyar Basri` |
| Authors — ORCID | `0009-0004-2159-9371` |
| Authors — Affiliations | `Independent Researcher` |
| Authors — Role | **Leave empty** (no dropdown available) |
| Description | (paste abstract below) |
| License | Creative Commons Attribution 4.0 (CC-BY) |
| Copyright | © 2026 Basyirin Amsyar Basri. Licensed under Creative Commons Attribution 4.0 International |

### Abstract (copy-paste)

**Problem:** Standard gradient-based training pipelines optimise parametric depth without targeting schema coherence — an agent's internal organisation around governing principles rather than surface statistics. High-depth, low-coherence agents fail on OOD recombination that ID metrics miss. Existing frameworks do not specify how schema coherence forms, what suppresses it, or how it drives attentional allocation.

**Method:** We introduce the Σ-Model, a coupled dynamical-systems framework with three contributions: (i) the σ-suppression mechanism — SGD creates a stable low-coherence equilibrium ("σ-trap"), explaining high-ID/low-OOD agents (Proposition 4.1); (ii) a grounded ODE system (Eqs. 14, 28, 29) with local existence, invariance, and bifurcation analysis (Propositions 3.1–4.4); (iii) a five-phase training arc with empirically detectable Phase-2 entry (Prediction 9). The framework formalises five cognitive faculty gaps with executable benchmarks and covers attentional fidelity, executive control, metacognition, social cognition, and multimodal transfer.

**Results:** Pilot experiments (n = 15 per condition) confirm additive and multiplicative coupling significantly outperform naive SGD on OOD accuracy (d = 9.08, 7.57; p < 0.0001), with Phase 2 entry detected early in training.

**Conclusion:** σ-suppression is the mechanistic origin of compositional failure. Capable-agent training must target dynamics explicitly — not merely scale or curriculum ordering.

### Additional fields

| Field | Value |
|-------|-------|
| Keywords | compositional generalisation, schema coherence, dynamical systems, neural ODEs, bifurcation, curriculum learning, cognitive evaluation |
| Contributors | (none — sole author) |
| Languages | English |
| Dates | Type=`Created`, Date=`2026-06-16`, Description=`Preprint completed` |
| Publication date | `2026-06-16` (required; this is the preprint publication date) |
| Version | **Leave empty** (this is a preprint, not software) |
| Related works | **Skip** (old software DOI on unmanaged account — do not reference) |
| References | **Leave empty** |
| Repository URL | `https://github.com/basyirin-dev/hbar-v3` |
| Alternate identifiers | **Skip** |
| Awards/Grants | **Leave empty** |
| Programming language | **Leave empty** |
| Development status | **Leave empty** |
| Publishing info | **Leave empty** |
| Conference | **Leave empty** |
| Domain specific | **Leave empty** |

After creation → copy the **new DOI** for the ORCID step below.

---

## 2. ORCID (orcid.org/0009-0004-2159-9371)

### Biography

> Independent AI researcher developing formal dynamical-systems theories of neural agent learning. Creator of the Σ-Model, a coupled ODE framework that identifies schema coherence suppression — not capacity or data — as the mechanistic origin of compositional generalisation failure in deep learning. Framework validated with 45 experimental runs (Cohen's d > 7.5), supported by 16 complete mathematical proofs.

### Keywords
`compositional generalisation`, `schema coherence`, `dynamical systems`, `neural ODEs`, `curriculum learning`, `cognitive science`, `deep learning theory`, `bifurcation analysis`

### Education / Employment
**Leave empty.** No entries needed — ORCID profile stands on biography + published work alone.

### Add Work

| Field | Value |
|-------|-------|
| Citation type | APA |
| Citation | Basyirin Amsyar Basri (2026). *The Σ-Model: Schema-Coherence Suppression as the Origin of Compositional Generalisation Failure: A Dynamical-Systems Framework for Generalisation Failure*. Preprint. https://doi.org/10.5281/zenodo.20714248 |
| Citation description | APA 7th edition — Malay name without patronymic (bin omitted per APA guidelines) |
| Work identifiers | DOI: 10.5281/zenodo.20714248 |
| Contributors (Given name) | (leave empty) |
| Contributors (Family name) | Basyirin Amsyar Basri |
| Contributors (displayed) | Basyirin Amsyar Basri (sole author; ORCID: 0009-0004-2159-9371) |
| Your contributions (CRediT) | **Conceptualization**, **Formal Analysis**, **Software**, **Methodology**, **Writing - Original Draft** (select all 5) |
| Language | English |
| Country/Location | (leave blank — preprint) |
| Visibility | Public |

---

## 3. GitHub Profile README

### Step 1
Create a new public repository named `basyirin-dev` with a README.

### Step 2
Paste the following as `README.md`:

```markdown
# Hi, I'm Basyirin Amsyar Basri 👋

Independent AI researcher building formal theories of how neural agents learn — and why they fail at systematic composition.

---

## 🔬 Featured Research

### [Σ-Model V3.0+](https://github.com/basyirin-dev/hbar-v3)

A coupled dynamical-systems framework proving that **compositional generalisation failure is a bifurcation phenomenon** — not a capacity or data problem.

| Aspect | Detail |
|--------|--------|
| Core finding | SGD creates a stable low-coherence equilibrium ("σ-trap") that standard training cannot escape |
| Status | Preprint (preparing for peer review) |
| Validation | 45 experimental runs, Cohen's d = 9.08 (additive), 7.57 (multiplicative), p < 0.0001 |
| Theory | 16 complete mathematical proofs (existence, invariance, bifurcation, consistency) |
| Stack | Python, PyTorch, NumPy, SciPy |

**Key predictions:**
- Depth without coherence produces brittle generalisation
- Curriculum must target σ-dynamics, not just δ-accumulation
- Nine falsifiable predictions distinguishable from depth-only accounts

## 🛠 Core Stack

| Area | Technologies |
|------|-------------|
| AI/ML | PyTorch, NumPy, SciPy, scikit-learn |
| Theory | Dynamical systems, bifurcation analysis, singular perturbation |
| Dev | Python, Jupyter, Docker, Git |

## 📫 Links

- [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20714248.svg)](https://doi.org/10.5281/zenodo.20714248)
- ORCID: [orcid.org/0009-0004-2159-9371](https://orcid.org/0009-0004-2159-9371)
- LinkedIn: [linkedin.com/in/basyirin-amsyar](https://www.linkedin.com/in/basyirin-amsyar/)
- GitHub: [github.com/basyirin-dev](https://github.com/basyirin-dev)
```

### Step 3
- Pin the `hbar-v3` repository to your profile top
- Add topics to the `hbar-v3` repo:
  - `schema-coherence`
  - `compositional-generalisation`
  - `dynamical-systems`
  - `neural-odes`
  - `pytorch`
  - `curriculum-learning`
  - `bifurcation-analysis`
  - `cognitive-evaluation`

---

## 4. LinkedIn

### Headline
> Independent AI Researcher — Dynamical Systems & Compositional Generalisation

### About section

> I work at the intersection of deep learning theory and dynamical systems, with a focus on understanding why neural agents fail at compositional generalisation — and how to fix it.
>
> My primary project, the **Σ-Model V3.0+**, is a coupled ODE framework that formalises schema coherence as an independently necessary training variable. The core finding: standard SGD creates a stable low-coherence equilibrium ("σ-trap") that produces agents with high in-distribution accuracy but catastrophic out-of-distribution failure. This reframes compositional failure as a bifurcation phenomenon rather than a capacity or data problem.
>
> The framework includes 16 full proofs (local existence, forward invariance, Fenichel decomposition, transcritical bifurcation, estimator consistency), 9 falsifiable predictions, and validation across 45 experimental runs (Cohen's d > 7.5). The manuscript is currently available as a preprint.
>
> **Research interests:** dynamical systems theory, compositional generalisation, neural ODEs, curriculum learning, cognitive evaluation of AI systems.

### Notes
- **Education:** Leave empty
- **Experience:** Leave empty
- LinkedIn profiles work fine with just About + Headline + Featured

### Featured
Pin the repo link: `https://github.com/basyirin-dev/hbar-v3`

### Projects (if section available)
Add "Σ-Model V3.0+" with repo link and brief description.

### Skills to add
`Machine Learning`, `PyTorch`, `Dynamical Systems`, `Neural Networks`, `Cognitive Science`, `Deep Learning`, `Python`, `Research`

---

## 5. Post-OpenReview Update

Once the paper is submitted to TMLR on OpenReview:

| Platform | Field | Update |
|----------|-------|--------|
| ORCID | Work status | Change "Preprint" to "Submitted to Transactions on Machine Learning Research" |
| GitHub | README table | Change "Preprint (preparing for peer review)" to "Under review at *Transactions on Machine Learning Research*" |
| LinkedIn | About | Change "The manuscript is currently available as a preprint" to "The manuscript is currently under review at *Transactions on Machine Learning Research*" |

---

## 6. OpenReview + Zenodo Submission Guide

### Overview

Two parallel tracks:
1. **OpenReview** — for peer-reviewed venue submission (no endorsement required)
2. **Zenodo** — for obtaining a persistent DOI for the paper

Both use the same `make pdf` output. The paper uses `article` + `tmlr.sty` (TMLR format).

### 6.1 Generate the Paper PDF

```bash
source hbar_env/bin/activate
cd paper/
make pdf
```

Expected output: `manuscript.pdf` (48 pages, 0 errors, 0 warnings).

### 6.2 OpenReview Submission

#### Why OpenReview over arXiv

| Feature | arXiv | OpenReview |
|---------|-------|------------|
| Endorsement required | Yes (new authors) | **No** |
| Peer review | No (preprint only) | Via hosted venues |
| Cost | Free | Free |
| Versioning | Yes | Yes |
| DOI | arXiv ID | Via Zenodo (below) |

#### Option A: Submit to TMLR (Rolling, No Deadline)

TMLR is the best-fit venue. Steps:

1. Create account at [openreview.net](https://openreview.net)
2. Navigate to TMLR submission page
3. Upload `paper/manuscript.pdf`
4. Fill metadata (title, abstract, authors, keywords)
5. Select license (CC-BY 4.0 recommended)
6. Submit supplementary material: `docs/proof-reconstruction/main.pdf` (optional but recommended)

#### Option B: Post as OpenReview Preprint (No Review)

1. Log in to OpenReview
2. Go to "Venues" → "Preprint"
3. Upload PDF + metadata

#### Option C: Both (Recommended Path)

1. **Now**: Post as OpenReview Preprint (5 min, instant URL)
2. **Same day**: Submit to TMLR (uses the same PDF)
3. **Later**: If TMLR accepts, the preprint page links to the peer-reviewed version

### 6.3 Zenodo DOI

#### Existing Zenodo DOI

- **DOI**: `10.5281/zenodo.19495977` — software, not the paper
- **Version**: v1.0.0 (April 2026)

#### Getting a Paper DOI

Two options:

**Option A: Manual upload (fastest, ~5 min)**
1. Go to [zenodo.org](https://zenodo.org) and log in
2. Click "Upload"
3. Fill in fields as specified in §1 above
4. Upload `paper/manuscript.pdf`
5. Also upload `docs/proof-reconstruction/main.pdf` as additional file
6. Click "Publish" → Zenodo issues a new DOI

**Option B: GitHub release (automated)**
1. Create a GitHub release with tag (e.g., `v2.0.0-paper`)
2. Link your Zenodo account to GitHub (Settings → GitHub)
3. Zenodo auto-archives the release and mints a DOI
4. Then manually upload the paper PDF with a note linking to the release

**Recommendation**: Use Option A first (instant DOI), then set up Option B for future updates.

### 6.4 Submission Metadata

**Title**:
```
The Σ-Model: Schema-Coherence Suppression as the Origin of Compositional Generalisation Failure
```

**Authors**: `Basyirin Amsyar Basri`

**Abstract**: Use the abstract from `paper/manuscript.tex` lines 67-98.

**Subject / Categories**:
- Primary: Dynamical Systems (Mathematics > Dynamical Systems)
- Secondary: Machine Learning (Computer Science > Learning)

**Keywords**: `compositional generalisation, schema coherence, neural ODEs, dynamical systems, curriculum learning, cognitive evaluation`

**License**: CC-BY 4.0 (Creative Commons Attribution 4.0 International)

### 6.5 Post-Submission Checklist

- [ ] PDF compiles with 0 errors: `make pdf`
- [ ] All figures render correctly (7 TikZ + 3 PNG)
- [ ] CLAIM tags are `%`-commented (invisible in PDF)
- [ ] README updated (done: "OpenReview preprint")
- [ ] `\received` dates removed (done)
- [ ] Supplementary proofs PDF available at `docs/proof-reconstruction/main.pdf`
- [ ] Zenodo DOI minted for paper PDF
- [ ] OpenReview preprint URL (or TMLR submission URL) obtained
- [ ] Software DOI `10.5281/zenodo.19495977` included in paper's data availability section
- [ ] Update README with OpenReview URL + new Zenodo DOI after submission

### 6.6 Timeline Estimate

| Step | Time | Cost |
|------|------|------|
| Generate PDF | 30s | $0 |
| OpenReview Preprint | 5 min | $0 |
| TMLR submission | 15 min | $0 |
| Zenodo DOI (manual) | 5 min | $0 |
| Total | ~25 min | $0 |

### 6.7 File Checklist

| File | Purpose |
|------|---------|
| `paper/manuscript.pdf` | Main paper (48 pages) |
| `docs/proof-reconstruction/main.pdf` | Supplementary proofs (16 reconstructed proofs) |
| `README.md` | Repository README (status already updated) |
| `results/canonical/all_results.pkl` | Experimental data |
| `scripts/generate_figures.py` | Figure regeneration script |

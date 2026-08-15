# Kaggle Experiment Architecture

> **Source**: Research output using AI Deep Research (Jun 2026)
> **Purpose**: Feasibility check and execution architecture for N=500 Kaggle training runs; platform comparison for Phase 03 execution plan
> **Target paper**: `paper-neurips/main.tex` (feeds into §3 Experimental Design, Methods supplement)

---

## Platform Comparison

| Criteria | Kaggle (Free) | Kaggle (Paid) | Google Colab Pro+ | Local GPU (1× RTX 3090/4090) |
|----------|---------------|---------------|-------------------|-------------------------------|
| **Cost (166 GPU hrs)** | $0 (30 hr/wk quota) | ~$85 (compute units) | ~$50–$100 (subscription + compute) | $0 sunk cost + electricity |
| **Session limit** | 30 hr | 30 hr | 12–24 hr (unreliable) | Unlimited |
| **Disk space** | 30 GB ephemeral + 100 GB Datasets | 30 GB ephemeral + 100 GB Datasets | ~100 GB ephemeral + 15 GB Drive | Unlimited |
| **Data bandwidth** | ~1 GB/s (Dataset mount) | ~1 GB/s (Dataset mount) | Slow (Drive download) | ~3–5 GB/s (local NVMe) |
| **GPU availability** | High (T4 constant) | High (T4 constant) | Moderate (A100 restricted) | 100% guaranteed |
| **Reproducibility** | High (Dockerized) | High (Dockerized) | Low (env changes) | Absolute (conda/Docker) |
| **Parallel sessions** | 1–2 concurrent | Up to 10+ | 1–2 concurrent | 1 per GPU |
| **Result collection** | Kaggle API versioning | Kaggle API versioning | Google Drive direct write | Local file system |

**Winner: Kaggle** — T4 is sufficient for a 4-layer transformer (d_model=256), 30 hr sessions allow ~70 runs per session (best in class), and Dataset mounting makes data loading instant. Colab's session drops and env instability make it unsuitable as primary platform.

---

## Overview

Executing 500 independent training runs on Kaggle requires a disciplined, automated pipeline. Kaggle sessions are ephemeral and stateless — every session must act as an independent worker that pulls a job, executes it, and pushes results to persistent storage.

The experiment trains a transformer with d_model=256, nhead=8, num_layers=4, vocab_size=22,000 — small enough to fit comfortably on a Tesla T4 (16 GB VRAM). Estimated wall time per run: ~20 minutes.

---

## 1. Job Distribution

**Strategy: Job Queue CSV**

Create a `jobs.csv` hosted as a Kaggle Dataset (`pfam-sigma-results`) that serves as the shared job queue across all sessions.

```
run_id,seed,condition,status,id_acc,ood_acc,delta_cg,sigma_proxy
0,42,familiar_combos,pending,,,,
1,85,familiar_combos,pending,,,,
...
```

- **~50 runs per session** (20 min each → ~17 hrs of training, leaving 13 hrs buffer for eval, upload, setup)
- **~10 sessions** total to clear 500 runs
- Each notebook pulls the next `pending` job, updates status to `running`, executes, then sets `done` or `failed`

---

## 2. Checkpointing

**Strategy: Per-Run Checkpoint with Skip-if-Exists**

```
/kaggle/working/checkpoints/
  run_0_final.pt
  run_1_final.pt
  ...
```

- At start of each run: check if `/kaggle/working/checkpoints/run_{id}_final.pt` exists
- If yes: skip training, load checkpoint, proceed to evaluation
- If no: train, save checkpoint every 5 epochs
- After successful API upload: delete local checkpoint to free disk space

This guarantees resilience against Kaggle session interruption (notes can lose kernel state at 30 hr cap).

---

## 3. Result Aggregation

**Strategy: Kaggle Dataset Versioning (Metrics) + Optional GCS/S3 (Weights)**

**Metrics (free, always used):** Use the Kaggle Python API to upload results as dataset versions.

```python
def push_metrics_to_kaggle(run_id, metrics_dict):
    import json, os
    path = f'/kaggle/working/metrics_{run_id}.json'
    with open(path, 'w') as f:
        json.dump(metrics_dict, f)
    os.system('kaggle datasets init -p /kaggle/working')
    os.system(f'kaggle datasets version -p /kaggle/working -m "run {run_id}"')
```

Each version appends one run's metrics. All 500 versions accumulate on the `pfam-sigma-results` dataset. Cost: $0.

**Model weights (optional, ~$0–$3 if using GCS):** If weight archiving is needed, upload to GCS/S3 using pre-configured API credentials stored as Kaggle Secrets. The small free tiers (5 GB) cover ~25–50 model checkpoints; for all 500, expect ~$0.50.

**Staggering for parallel safety:** When multiple notebooks upload concurrently, add `time.sleep(random.uniform(5, 30))` before the `kaggle datasets version` call to avoid version conflicts.

---

## 4. Dataset Caching

**Strategy: Pre-Processed Kaggle Dataset**

- **Step 1** (one-time, local or setup notebook): Download Pfam 38.2, tokenize domain architecture sequences, save as PyTorch tensors (`.pt`) or Parquet files
- **Step 2**: Upload processed data as Kaggle Dataset `pfam-processed-data`
- **Step 3**: In execution notebook, attach `pfam-processed-data` as input → mounts instantly at `/kaggle/input/pfam-processed-data/` with zero download

No re-downloading, no Drive bandwidth bottleneck, no per-session processing overhead.

---

## 5. Parallel Execution

**Strategy: Partitioned Job Pools**

With paid tier (up to 10 concurrent notebooks):

| Notebook | Runs (run_id) |
|----------|---------------|
| Worker 0 | run_id % 10 == 0 |
| Worker 1 | run_id % 10 == 1 |
| ... | ... |
| Worker 9 | run_id % 10 == 9 |

Each notebook pulls from `jobs.csv`, picks its partition, and executes sequentially within its 30 hr session.

**Upload conflict avoidance:** Staggered `time.sleep(random.uniform(5, 30))` before each dataset version push (see §3).

---

## 6. API Orchestration

**Strategy: Local Conductor Script**

Do not click "Run" manually 10 times. Write a local Python script that automates everything:

```python
# conductor.py — runs on local machine, orchestrates Kaggle sessions
import subprocess, time

NOTEBOOK_DIR = "/path/to/kaggle-notebook"
KAGGLE_USER = "pfam-user"
NOTEBOOK_SLUG = "pfam-execution-notebook"

for session in range(12):
    # Push notebook to Kaggle
    subprocess.run(["kaggle", "kernels", "push", "-p", NOTEBOOK_DIR], check=True)

    # Poll until complete
    while True:
        status = subprocess.run(
            ["kaggle", "kernels", "status", f"{KAGGLE_USER}/{NOTEBOOK_SLUG}"],
            capture_output=True, text=True
        )
        if "complete" in status.stdout.lower():
            break
        elif "error" in status.stdout.lower() or "failed" in status.stdout.lower():
            raise RuntimeError(f"Session {session} failed")
        time.sleep(120)  # poll every 2 minutes
```

---

## 7. Progress Monitoring

**Strategy: Scheduled Dashboard Notebook**

Create a separate Kaggle notebook that:

- Runs on a cron schedule (Kaggle supports scheduled notebook execution)
- Pulls the latest version of `pfam-sigma-results`
- Reads all metrics JSON files
- Generates:
  - **Run completion count**: bar chart of pending / running / done / failed
  - **σ_A vs OOD accuracy scatter**: updates live as runs complete
  - **Failed runs list**: run IDs requiring manual inspection
  - **Time estimate**: runs/hr throughput, projected completion date

Output is viewable directly in the Kaggle notebook browser — no external dashboard needed.

---

## 8. Cost Estimate

| Item | Calculation | Cost |
|------|-------------|------|
| GPU compute | 500 runs × 20 min = 10,000 min = **166.6 GPU hrs** | ~$83 (paid, $0.50/hr) or $0 (free, 30 hr/wk) |
| Overhead (setup, eval, upload) | +15% = ~25 GPU hrs | ~$12.50 paid, $0 free |
| **Total paid** | | **~$96** |
| **Total free** | | **$0, ~6 weeks** (30 hr/wk quota) |
| GCS/S3 model weights (optional) | ~500 MB–100 GB depending on archiving | ~$0–$3 |

**Recommendation:** Start with free tier ($0, ~6 weeks). If time-constrained, upgrade to ~$96 paid compute units and finish in a weekend.

---

## 9. Hybrid Architecture Recommendation

The research output suggests a **hybrid local-conductor + Kaggle-worker** architecture as the most robust approach:

```
┌──────────────────────┐     ┌──────────────────────┐
│   Conductor (Local)  │────▶│   Kaggle Worker 1    │
│   - jobs.csv master  │     │   (50 runs, T4 GPU)  │
│   - pushes notebook  │     └──────────┬───────────┘
│   - polls status     │                │
│   - spawns workers   │     ┌──────────▼───────────┐
│                      │────▶│   Kaggle Worker 2    │
│   Optional:          │     │   (50 runs, T4 GPU)  │
│   - local GPU worker │     └──────────┬───────────┘
│   - Colab fallback   │                │
└──────────────────────┘     ┌──────────▼───────────┐
        │                    │   Persistent Storage  │
        │                    │   (Kaggle Dataset     │
        │                    │    for metrics)       │
        └────────────────────┴──────────────────────┘
```

**Why this wins over pure-Kaggle or pure-Colab:**

| Risk | Mitigation |
|------|------------|
| Kaggle session crash at hr 29 | Checkpoint per run → resume on re-push |
| Kaggle quota exhausted (30 hr/wk) | Conductor switches to local GPU or Colab |
| Dataset version conflicts | Staggered uploads + GCS fallback for weights |
| Colab disconnection | Not primary — backup only |
| Reproducibility drift | Conductor pins exact notebook version per push |

**The conductor is the single source of truth** — it holds `jobs.csv` locally, never loses state, and can switch between worker backends transparently.

---

## 10. Summary Recommendation

1. **Primary platform**: Kaggle (T4, 30 hr sessions, instant data mounting)
2. **Result storage**: Kaggle Dataset versioning for metrics ($0); GCS/S3 optional for model weights (~$0–$3)
3. **Orchestration**: Local conductor script (POSIX, < 50 lines of Python)
4. **Colab**: Backup only — not reliable enough for primary execution
5. **Local GPU**: Optional — conductor can assign runs to local GPU simultaneously
6. **Total cost**: $0 (free tier, ~6 weeks) or ~$96 (paid, weekend)
7. **Architecture**: Write all code to be cloud-agnostic; data loads from Kaggle Dataset mount, results upload to Kaggle Dataset API. Conductor manages all state.

---

## Cross-References

- `docs/phases/03_brittle_domain.md` — Tasks 3.3 (notebook implementation), 3.5 (N=500 execution). Update to use the job queue pattern and conductor script documented here.
- `docs/research/osf-preregistration-draft.md` — Seed formula (`run_id * 42 + 7`), Pfam 38.2 version, condition definitions.
- `docs/research/pilot-design.md` — N=15 pilot runs before full N=500 (test on Kaggle infrastructure first).

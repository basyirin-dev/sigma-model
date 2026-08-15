# Σ-Model Environment Drift Log

Track environmental changes that may require future adaptive action.

## Entry: 2026-06-09 — Initial Audit

### Security

| Package | Old Version | New Version | CVEs Fixed |
|---------|-------------|-------------|------------|
| aiohttp | 3.13.4 | 3.14.1 | CVE-2026-34993, CVE-2026-47265 |
| cryptography | 46.0.6 | 48.0.0 | PYSEC-2026-36 |
| idna | 3.11 | 3.18 | CVE-2026-45409 |
| jupyter-server | 2.17.0 | 2.19.0 | PYSEC-2026-67/68/69, CVE-2026-40110 |
| jupyterlab | 4.5.6 | 4.5.8 | PYSEC-2026-164, CVE-2026-42557 |
| mistune | 3.2.0 | 3.2.1 | PYSEC-2026-168, CVE-2026-33079/44708/44897 |
| nbconvert | 7.17.0 | 7.17.1 | CVE-2026-39377/39378 |
| notebook | 7.5.5 | 7.5.7 | CVE-2026-40171 |
| pillow | 12.1.1 | 12.2.0 | PYSEC-2026-165, CVE-2026-40192/42309/42310/42311 |
| pip | 26.0.1 | 26.1.2 | PYSEC-2026-196, CVE-2026-3219/6357 |
| pygments | 2.19.2 | 2.20.0 | CVE-2026-4539 |
| urllib3 | 2.6.3 | 2.7.0 | PYSEC-2026-141/142 |

**Total: 33 CVEs fixed across 12 packages.**

### Numerical Patches

| Package | Old Version | New Version | Risk | Notes |
|---------|-------------|-------------|------|-------|
| numpy | 2.4.3 | 2.4.6 | LOW | Patch-only; no numerical behavior changes |
| matplotlib | 3.10.8 | 3.10.9 | LOW | Security patch; axes.prop_cycle restriction |

### Version Pins Tightened

| Package | Old Pin | New Pin | Reason |
|---------|---------|---------|--------|
| datasets | `>=2.20` (no upper) | `>=2.20,<3.0` | Prevent accidental jump to 5.0.0 (3 major versions, breaking: removed builder scripts, Sequence→List, TorchCodec) |
| pandas | `>=2.0,<4.0` | `>=2.0,<3.0` | Prevent jump to 3.0.x (breaking: StringDtype default, Series.values returns ExtensionArray, copy-on-write permanent) |

### Installed Versions (Current)

| Package | Installed | Upper Bound | Margin |
|---------|-----------|-------------|--------|
| numpy | 2.4.6 | <3.0 | 0.54 |
| scipy | 1.17.1 | <2.0 | 0.83 |
| torch | 2.12.0 | <3.0 | 0.88 |
| matplotlib | 3.10.9 | <4.0 | 0.89 |
| pandas | 2.3.3 | <3.0 | 0.67 |
| datasets | 2.21.0 | <3.0 | 0.79 |
| pyarrow | 23.0.1 | (no upper) | — |
| triton | 3.7.0 | (no upper) | — |
| tikzplotlib | 0.10.1 | (no upper) | — |
| seaborn | 0.13.2 | (no upper) | — |

### Runtime Environment

| Property | Value |
|----------|-------|
| Python | 3.14.5 |
| GPU | None (CPU-only) |
| CUDA | N/A |
| OS | Linux |
| PyTorch | 2.12.0 (CPU) |

### Cloud APIs

| Service | Status |
|---------|--------|
| OpenAI | Not used |
| Anthropic | Not used |
| Weights & Biases | Not used |
| TensorBoard | Not used |
| MLflow | Not used |
| AWS (boto3) | Not used |
| Google Cloud | Not used |
| Twitter/X | Stub only (requires TWITTER_BEARER_TOKEN env var) |

### Risks to Monitor

| # | Risk | Severity | Trigger | Action When Triggered |
|---|------|----------|---------|----------------------|
| 1 | `datasets` 3.0 released | HIGH | PyPI shows datasets 3.0+ | Test migration; pin `<3.0` is already in place |
| 2 | `pandas` 3.x released | MEDIUM | PyPI shows pandas 3.0+ | Already pinned `<3.0`; audit code when ready to migrate |
| 3 | `torch` CUDA linalg backend change | LOW | Running on GPU | MAGMA→cuSolver switch may affect numerical results on CUDA |
| 4 | `triton` Python 3.14 compat | LOW | GPU environment needed | Currently non-functional without GPU; check compat when GPU added |
| 5 | `tikzplotlib` deprecation | MEDIUM | matplotlib 4.0 release | tikzplotlib 0.10.1 may break; monitor for alternatives |
| 6 | `datasets==2.21.0` on Python 3.14 | LOW | Runtime errors | Works via ABI compat; upgrade to 3.x if issues arise |

### Future Actions

- [ ] Re-run `pip-audit` monthly
- [ ] Monitor `datasets` 3.x migration path when ready
- [ ] Monitor `pandas` 3.x migration path when ready
- [ ] Add GPU environment for CUDA-specific testing when available
- [ ] Check `tikzplotlib` compatibility before matplotlib 4.0
- [ ] Loosen `pyarrow` upper bound from `<24` to `<25` if/when 23.1.0+ released

## Entry: 2026-06-10 — Pre-Push Environment Audit

### Security

pip-audit re-run: 1 new CVE found.

| Package | Old Version | New Version | CVE |
|---------|-------------|-------------|-----|
| pip | 26.1.1 | 26.1.2 | PYSEC-2026-196 |

**0 remaining vulnerabilities in auditable packages.**

### CUDA / Runtime

| Property | Value |
|----------|-------|
| GPU | None (CPU-only) — unchanged |
| CUDA | N/A — unchanged |
| PyTorch | 2.12.0+cu130 (CUDA 13.0 libs installed, inactive) |

### Cloud APIs

No changes since 2026-06-09. All endpoints stable:
- OpenAI, Anthropic, W&B, TensorBoard, MLflow: still unused
- arXiv, PyPI, GitHub, Reddit, HN: stable, public, no-auth
- Twitter/X: stub only (unchanged)

### Package Versions

No version changes since 2026-06-09. All within `pyproject.toml` bounds.

| Package | Version | Upper Bound | Margin |
|---------|---------|-------------|--------|
| numpy | 2.4.6 | <3.0 | 0.54 |
| scipy | 1.17.1 | <2.0 | 0.83 |
| torch | 2.12.0 | <3.0 | 0.88 |
| matplotlib | 3.10.9 | <4.0 | 0.89 |
| pandas | 2.3.3 | <3.0 | 0.67 |
| datasets | 2.21.0 | <3.0 | 0.79 |
| pyarrow | 23.0.1 | <24 | **0.04** ⚠️ |
| triton | 3.7.0 | (none) | — |

### New Risks

| # | Risk | Severity | Trigger | Action When Triggered |
|---|------|----------|---------|----------------------|
| 7 | `pyarrow` upper bound collision | MEDIUM | PyPI shows pyarrow 23.1.0+ | Pin loosened: `<24` → `<25` in `pyproject.toml` (2026-06-10) |

## Entry: 2026-06-10 — pyarrow Pin Loosening

### Action

Loosened `pyarrow` upper bound in `pyproject.toml`:

| Before | After | Reason |
|--------|-------|--------|
| `pyarrow>=14,<24` | `pyarrow>=14,<25` | pyarrow 24.0.0 exists on PyPI; `<24` blocks future pip operations |

### Local State Preserved

| Package | Version | Status |
|---------|---------|--------|
| pyarrow | **23.0.1** | Intentionally NOT upgraded to 24.0.0 |

**Rationale:** Local environment is the verified audit environment that produced canonical `all_results.pkl` (92 KB, Table 5 15/15 PASS). Upgrading a C-extension library (Parquet serialization, datasets compatibility) introduces non-zero risk of silent breakage before arXiv submission. Stability over novelty.

### Risk #7 Status: ✅ Mitigated

Structural constraint relaxed. Local pin remains at 23.0.1 for provenance. Next `pip install` or `pip sync` will allow 24.x if/when needed.

### Future Actions Updated

- [x] Loosen `pyarrow` upper bound from `<24` to `<25` if/when 23.1.0+ released *(Completed 2026-06-10)*

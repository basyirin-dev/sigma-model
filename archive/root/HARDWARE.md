# Hardware Requirements & Runtime Profiling

## Verified Configuration

| Component | Specification |
|-----------|---------------|
| **GPU** | NVIDIA T4 (16 GB VRAM) |
| **CPU** | 8 vCPUs (x86_64) |
| **RAM** | 16 GB system memory |
| **OS** | Linux (Ubuntu 22.04) |
| **CUDA** | 12.x |

## Resource Usage (Pilot: 45 runs, 3 conditions × 15 runs, 2000 steps each)

| Metric | Value |
|--------|-------|
| Peak VRAM | ~2.1 GB (batch=64, d_model=128) |
| Total wall time | ~43 min on T4 |
| Per-run time | ~57 s |
| CPU-only (fallback) | ~3-4× slower (est. 2.5-3 h total) |
| Minimum system RAM | 8 GB |
| Recommended | 16 GB + T4-equivalent GPU |

## CPU Fallback

The codebase runs fully on CPU when no GPU is available. The ODE solver
(`sigma/ode/solver.py`) is pure NumPy and does not require a GPU. The
training loop (`sigma/models/training.py`) detects CUDA availability via
`torch.cuda.is_available()` and falls back to CPU automatically.

## Docker

For fully reproducible environments, use the provided Dockerfile:
```bash
docker build -t sigma .
docker run --gpus all sigma make test
```

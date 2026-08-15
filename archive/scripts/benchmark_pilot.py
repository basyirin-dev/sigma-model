#!/usr/bin/env python3
"""
⚠️ DEPRECATED / FAILED EXPERIMENT

Failure Mode: Hardware incompatibility + superseded.
The Kaggle P100 (sm_60) is incompatible with PyTorch >= 2.10, which
dropped SM 6.x support. Additionally, the hardcoded comparison table
at the end of this file is a manual recording, not a computed result.

Canonical Source: experiments/h-bar-experiment.ipynb
Date Discovered: 2026-06-10

---- original header below ----
Σ-Model Pilot Benchmark — Paste this as a SINGLE CELL into any notebook.
Auto-detects CPU / GPU / TPU, runs 100 training steps, reports projected timings.
"""
import time, os, sys, platform

# ── 1. Detect device ──
device = "cpu"
accelerator = "none"

try:
    import torch
    if torch.cuda.is_available():
        device = "cuda"
        accelerator = torch.cuda.get_device_name(0)
    elif hasattr(torch, "xla") and hasattr(torch.xla, "devices"):
        import torch_xla.core.xla_model as xm
        device = "xla"
        accelerator = "TPU v5e-8"
    else:
        accelerator = f"CPU ({platform.processor() or platform.machine()}, {os.cpu_count()} threads)"
except ImportError:
    raise SystemExit("ERROR: PyTorch not installed.")

print(f"Platform : {platform.system()} {platform.release()}")
print(f"Python   : {sys.version.split()[0]}")
print(f"PyTorch  : {torch.__version__}")
print(f"Device   : {device}")
print(f"Accelerator: {accelerator}")
if device == "cuda":
    print(f"CUDA ver : {torch.version.cuda or 'N/A'}")
    _props = torch.cuda.get_device_properties(0)
    _vram = getattr(_props, 'total_memory', getattr(_props, 'total_mem', 0))
    print(f"VRAM     : {_vram / 1e9:.1f} GB")

# ── 2. Build model (matches paper: 2-layer, 4-head, d=128) ──
from torch import nn

d_model, nhead, num_layers, dim_ff = 128, 4, 2, 512
vocab_size = 27

embed = nn.Embedding(vocab_size, d_model, padding_idx=0).to(device)
proj = nn.Linear(d_model, vocab_size).to(device)
transformer = nn.Transformer(
    d_model=d_model, nhead=nhead,
    num_encoder_layers=num_layers, num_decoder_layers=num_layers,
    dim_feedforward=dim_ff, batch_first=True,
).to(device)

all_params = list(embed.parameters()) + list(transformer.parameters()) + list(proj.parameters())
n_params = sum(p.numel() for p in all_params)
print(f"Model    : {n_params:,} params")


def forward(src_tok, tgt_tok):
    """Embed → Transformer → Project (matches notebook HBarTransformer)."""
    src_emb = embed(src_tok)
    tgt_emb = embed(tgt_tok)
    seq_len = tgt_tok.size(1)
    mask = torch.triu(torch.ones(seq_len, seq_len, device=device), diagonal=1).masked_fill(
        torch.triu(torch.ones(seq_len, seq_len, device=device), diagonal=1) == 1,
        float("-inf"),
    )
    pad_mask = (src_tok == 0)
    out = transformer(src_emb, tgt_emb, tgt_mask=mask, src_key_padding_mask=pad_mask)
    return proj(out)


# ── 3. Fake batch (batch=64, seq=50 — matches notebook) ──
batch_size, seq_len = 64, 50
src = torch.randint(1, vocab_size, (batch_size, seq_len), device=device)
tgt = torch.randint(1, vocab_size, (batch_size, seq_len), device=device)

# ── 4. Setup ──
criterion = nn.CrossEntropyLoss(ignore_index=0)
optimizer = torch.optim.Adam(all_params, lr=0.001)
use_amp = (device == "cuda")
scaler = torch.amp.GradScaler("cuda", enabled=use_amp)

# ── 5. Warm-up (3 steps) ──
embed.train(); transformer.train(); proj.train()
for _ in range(3):
    tgt_in, tgt_out = tgt[:, :-1], tgt[:, 1:]
    with torch.amp.autocast("cuda", enabled=use_amp):
        out = forward(src, tgt_in)
        loss = criterion(out.reshape(-1, vocab_size), tgt_out.reshape(-1))
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
    optimizer.zero_grad(set_to_none=True)
if device == "cuda":
    torch.cuda.synchronize()

# ── 6. Benchmark: 100 steps ──
N_STEPS = 100
t0 = time.perf_counter()
for step in range(N_STEPS):
    tgt_in, tgt_out = tgt[:, :-1], tgt[:, 1:]
    with torch.amp.autocast("cuda", enabled=use_amp):
        out = forward(src, tgt_in)
        loss = criterion(out.reshape(-1, vocab_size), tgt_out.reshape(-1))
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
    optimizer.zero_grad(set_to_none=True)
if device == "cuda":
    torch.cuda.synchronize()
elapsed = time.perf_counter() - t0

steps_per_sec = N_STEPS / elapsed
ms_per_step = (elapsed / N_STEPS) * 1000

print(f"\n{'='*60}")
print(f" BENCHMARK  ({N_STEPS} steps, batch={batch_size}, seq={seq_len})")
print(f"{'='*60}")
print(f" {elapsed:.2f}s -> {steps_per_sec:.1f} steps/sec  ({ms_per_step:.1f} ms/step)")

# ── 7. Project timings ──
TOTAL_STEPS = 45 * 2000  # full pilot: 45 runs x 2000 steps


def fmt(s):
    if s < 60:
        return f"{s:.0f}s"
    if s < 3600:
        return f"{s/60:.1f} min"
    return f"{s/3600:.1f} hrs"


projected = TOTAL_STEPS / steps_per_sec
print(f"\n Pilot (45 runs x 2000 steps = {TOTAL_STEPS:,}): {fmt(projected)}")
print(f" Single condition (15 runs = 30,000):            {fmt(30000 / steps_per_sec)}")

# ── 8. Comparison table (updated with REAL measurements, Jun 2026) ──
#
# REAL DATA (measured with benchmark script):
#   T4 single (Kaggle): 62.0 steps/sec  — benchmark uses GPU 0 only
#   TPU host CPU fallback: 1.3 steps/sec — torch_xla NOT installed, 224 threads
#   Local CPU (4-core): 1.9 steps/sec
#
# DEAD: Kaggle P100 (sm_60) incompatible with PyTorch≥2.10 (requires sm_70+)
# NOTE: T4×2 env gives 62 steps/sec on GPU 0 — second card unused without DDP.
#       DDP would require code changes (DataParallel/DDP wrapper).
# NOTE: TPU v5e-8 requires torch_xla port — CPU fallback is WORSE than local CPU.

configs = [
    ("Local CPU (measured, 4-core)",    1.9),
    ("Kaggle TPU host CPU (fallback)",  1.3),
    ("Kaggle P100 [DEAD — sm_60]",      0.0),
    ("Kaggle T4 single (MEASURED)",    62.0),
    ("Kaggle T4×2 via DDP (est.)",    109.0),
    ("Kaggle TPU v5e-8 via XLA (est.)", 80.0),
]

label = f"THIS RUN ({accelerator})"
print(f"\n{'='*72}")
print(f" COMPARISON TABLE  (projected for {TOTAL_STEPS:,} steps)")
print(f"{'='*72}")
print(f" REAL measurements marked. Estimates marked (est.).")
print(f" P100 DEAD: PyTorch≥2.10 dropped sm_60 (Pascal) support.")
print(f" TPU: CPU fallback without torch_xla; XLA port needed for GPU.")
print(f" T4×2: benchmark uses GPU 0 only; DDP wrapper needed for 2nd card.")
print(f"{'='*72}")
print(f" {'#':<3} {'Configuration':<35} {'Steps/s':>8} {'Time':>10} {'Speedup':>8}")
print(f" {'-'*3} {'-'*35} {'-'*8} {'-'*10} {'-'*8}")
print(f" {'->':<3} {label:<35} {steps_per_sec:>8.1f} {fmt(projected):>10} {steps_per_sec/1.9:>7.1f}x")
for i, (name, sps) in enumerate(configs, 1):
    if sps == 0.0:
        print(f" {i:<3} {name:<35} {'N/A':>8} {'INCOMPAT':>10} {'---':>8}")
    else:
        print(f" {i:<3} {name:<35} {sps:>8.1f} {fmt(TOTAL_STEPS/sps):>10} {sps/1.9:>7.1f}x")
print(f"{'='*72}")

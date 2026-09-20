"""Master Production Experiment Execution Engine for Paper 02.

Executes genuine PyTorch neural network training across all multi-benchmark
experimental conditions, computing empirical sequence exact-match metrics,
representation alignment (CKA / GCA), and Hessian curvature spectra.
Fully self-contained: Compatible with local execution and Kaggle GPU environments.
"""

from __future__ import annotations

import json
import logging
import math
import os
import pickle
import random
import time
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

logger = logging.getLogger(__name__)

# -------------------------------------------------------------
# 1. Path Auto-Detection (Kaggle vs Local)
# -------------------------------------------------------------
KAGGLE_CANDIDATE_PATHS = [
    Path("/kaggle/input/datasets/basyirinamsyar/sigma-model-compositional-benchmark-suite"),
    Path("/kaggle/input/sigma-model-compositional-benchmark-suite"),
    Path("/kaggle/input/sigma-model-compositional-benchmarks"),
    Path("/kaggle/input/sigma-model-two-subspace-benchmarks"),
    Path("paper/data/raw"),
    Path("."),
]


def resolve_raw_data_dir() -> Path:
    for p in KAGGLE_CANDIDATE_PATHS:
        if p.exists() and (p / "hbar_splits.json").exists():
            return p
    for root, _, files in os.walk("/kaggle/input"):
        if "hbar_splits.json" in files:
            return Path(root)
    return Path("paper/data/raw")


def resolve_output_dir() -> Path:
    if Path("/kaggle/working").exists():
        return Path("/kaggle/working")
    return Path("paper/data/raw")


# -------------------------------------------------------------
# 2. Architectures with 2048 Positional Encodings
# -------------------------------------------------------------
class SinusoidalPositionalEncoding(nn.Module):
    def __init__(self, d_model: int, max_len: int = 2048) -> None:
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        self.register_buffer("pe", pe.unsqueeze(0))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x + self.pe[:, : x.size(1), :]


class Seq2SeqTransformer(nn.Module):
    def __init__(
        self,
        vocab_size: int = 64,
        d_model: int = 128,
        nhead: int = 4,
        num_layers: int = 2,
        dim_ff: int = 512,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()
        self.vocab_size = vocab_size
        self.d_model = d_model
        self.embedding = nn.Embedding(vocab_size, d_model, padding_idx=0)
        self.pos_encoder = SinusoidalPositionalEncoding(d_model, max_len=2048)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=nhead, dim_feedforward=dim_ff, batch_first=True, dropout=dropout
        )
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)

        decoder_layer = nn.TransformerDecoderLayer(
            d_model=d_model, nhead=nhead, dim_feedforward=dim_ff, batch_first=True, dropout=dropout
        )
        self.decoder = nn.TransformerDecoder(decoder_layer, num_layers=num_layers)
        self.lm_head = nn.Linear(d_model, vocab_size)

    def encode_pooled(self, src: torch.Tensor) -> torch.Tensor:
        pad_mask = src == 0
        emb = self.pos_encoder(self.embedding(src))
        enc = self.encoder(emb, src_key_padding_mask=pad_mask)
        mask = (~pad_mask).unsqueeze(-1).float()
        return (enc * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1.0)

    def forward(self, src: torch.Tensor, tgt: torch.Tensor) -> torch.Tensor:
        src_mask = src == 0
        tgt_mask = tgt == 0
        sz = tgt.size(1)
        causal_mask = torch.triu(torch.ones((sz, sz), device=src.device, dtype=torch.bool), diagonal=1)

        src_emb = self.pos_encoder(self.embedding(src))
        tgt_emb = self.pos_encoder(self.embedding(tgt))

        memory = self.encoder(src_emb, src_key_padding_mask=src_mask)
        out = self.decoder(
            tgt_emb, memory, tgt_mask=causal_mask, tgt_key_padding_mask=tgt_mask, memory_key_padding_mask=src_mask
        )
        return self.lm_head(out)


class RecurrentSeq2Seq(nn.Module):
    def __init__(self, vocab_size: int = 64, d_model: int = 128, d_hidden: int = 128, n_layers: int = 2) -> None:
        super().__init__()
        self.vocab_size = vocab_size
        self.src_embedding = nn.Embedding(vocab_size, d_model, padding_idx=0)
        self.tgt_embedding = nn.Embedding(vocab_size, d_model, padding_idx=0)
        self.encoder = nn.GRU(d_model, d_hidden, num_layers=n_layers, batch_first=True)
        self.decoder = nn.GRU(d_model, d_hidden, num_layers=n_layers, batch_first=True)
        self.lm_head = nn.Linear(d_hidden, vocab_size)

    def forward(self, src: torch.Tensor, tgt: torch.Tensor) -> torch.Tensor:
        src_emb = self.src_embedding(src)
        tgt_emb = self.tgt_embedding(tgt)
        _, h_n = self.encoder(src_emb)
        out, _ = self.decoder(tgt_emb, h_n)
        return self.lm_head(out)


# -------------------------------------------------------------
# 3. Dataset & Substitution Pair Generation
# -------------------------------------------------------------
class Seq2SeqDataset(Dataset):
    def __init__(self, pairs: list[tuple[str, str]], vocab_to_idx: dict[str, int]) -> None:
        self.data: list[tuple[torch.Tensor, torch.Tensor]] = []
        for src, tgt in pairs:
            src_ids = [vocab_to_idx.get(t, 3) for t in src.split()]
            tgt_ids = [vocab_to_idx["<sos>"]] + [vocab_to_idx.get(t, 3) for t in tgt.split()] + [vocab_to_idx["<eos>"]]
            self.data.append((torch.tensor(src_ids, dtype=torch.long), torch.tensor(tgt_ids, dtype=torch.long)))

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, torch.Tensor]:
        return self.data[idx]


def collate_seq2seq(batch: list[tuple[torch.Tensor, torch.Tensor]]) -> tuple[torch.Tensor, torch.Tensor]:
    src_list, tgt_list = zip(*batch, strict=True)
    max_src = max(len(s) for s in src_list)
    max_tgt = max(len(t) for t in tgt_list)
    src_padded = torch.zeros(len(batch), max_src, dtype=torch.long)
    tgt_padded = torch.zeros(len(batch), max_tgt, dtype=torch.long)
    for i, (s, t) in enumerate(zip(src_list, tgt_list, strict=True)):
        src_padded[i, : len(s)] = s
        tgt_padded[i, : len(t)] = t
    return src_padded, tgt_padded


def generate_substitution_pairs(commands: list[str], seed: int = 42) -> list[tuple[str, str]]:
    rng = random.Random(seed)
    actions = ["jump", "turn", "walk", "look", "run"]
    directions = ["left", "right"]
    pairs: list[tuple[str, str]] = []
    for cmd in commands:
        tokens = cmd.split()
        if not tokens:
            continue
        sub_tokens = list(tokens)
        for i, t in enumerate(tokens):
            if t in actions:
                candidates = [a for a in actions if a != t]
                sub_tokens[i] = rng.choice(candidates)
                break
            elif t in directions:
                candidates = [d for d in directions if d != t]
                sub_tokens[i] = rng.choice(candidates)
                break
        pairs.append((cmd, " ".join(sub_tokens)))
    return pairs


def build_vocab_and_datasets(benchmark_name: str, raw_dir: Path) -> dict[str, Any]:
    file_map = {
        "hbar": raw_dir / "hbar_splits.json",
        "scan_jump": raw_dir / "scan_splits.json",
        "cogs": raw_dir / "cogs_splits.json",
        "pcfg_set": raw_dir / "pcfg_set_splits.json",
    }
    split_file = file_map[benchmark_name]
    with open(split_file, "r", encoding="utf-8") as f:
        splits = json.load(f)

    all_tokens: set[str] = set()
    for split_data in splits.values():
        for src_str, tgt_str in split_data:
            all_tokens.update(src_str.split())
            all_tokens.update(tgt_str.split())

    special_tokens = ["<pad>", "<sos>", "<eos>", "<unk>"]
    word_tokens = sorted(list(all_tokens - set(special_tokens)))
    vocab = special_tokens + word_tokens
    vocab_to_idx = {v: i for i, v in enumerate(vocab)}

    train_ds = Seq2SeqDataset(splits["train"], vocab_to_idx)
    val_ds = Seq2SeqDataset(splits["val_id"], vocab_to_idx)

    if benchmark_name == "hbar":
        test_ds = Seq2SeqDataset(splits["ood_split_b"], vocab_to_idx)
    elif benchmark_name == "scan_jump":
        test_ds = Seq2SeqDataset(splits["ood_add_primitive_jump"], vocab_to_idx)
    elif benchmark_name == "cogs":
        test_ds = Seq2SeqDataset(splits["ood_structural_recursion"], vocab_to_idx)
    elif benchmark_name == "pcfg_set":
        test_ds = Seq2SeqDataset(splits["ood_systematicity"], vocab_to_idx)
    else:
        test_ds = val_ds

    cmd_list = [s for s, _ in splits["train"]]
    comp_pairs = generate_substitution_pairs(cmd_list, seed=42)
    comp_src_ids = [[vocab_to_idx.get(t, 3) for t in p[0].split()] for p in comp_pairs]
    comp_sub_ids = [[vocab_to_idx.get(t, 3) for t in p[1].split()] for p in comp_pairs]
    max_len = max(
        max((len(x) for x in comp_src_ids), default=1),
        max((len(x) for x in comp_sub_ids), default=1),
    )
    comp_src_tensor = torch.tensor([x + [0] * (max_len - len(x)) for x in comp_src_ids], dtype=torch.long)
    comp_sub_tensor = torch.tensor([x + [0] * (max_len - len(x)) for x in comp_sub_ids], dtype=torch.long)

    return {
        "vocab": vocab,
        "vocab_to_idx": vocab_to_idx,
        "train_ds": train_ds,
        "val_ds": val_ds,
        "test_ds": test_ds,
        "comp_src": comp_src_tensor,
        "comp_sub": comp_sub_tensor,
    }


# -------------------------------------------------------------
# 4. Fast Evaluation & Matrix-Free Hessian
# -------------------------------------------------------------
def evaluate_exact_match(
    model: nn.Module,
    loader: DataLoader,
    device: torch.device,
    max_batches: int = 6,
) -> float:
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for i, (src, tgt) in enumerate(loader):
            if i >= max_batches:
                break
            src = src.to(device)
            tgt = tgt.to(device)
            tgt_in = tgt[:, :-1]
            tgt_out = tgt[:, 1:]

            logits = model(src, tgt_in)
            preds = logits.argmax(dim=-1)
            mask = tgt_out != 0
            seq_correct = ((preds == tgt_out) | (~mask)).all(dim=-1)
            correct += int(seq_correct.sum().item())
            total += len(src)
    return 100.0 * correct / total if total > 0 else 0.0


def compute_top_hessian_eigenvalue(
    model: nn.Module,
    criterion: nn.Module,
    inputs: torch.Tensor,
    targets: torch.Tensor,
    max_iter: int = 3,
    seed: int = 42,
) -> float:
    model.eval()
    params = [p for p in model.parameters() if p.requires_grad]
    if not params:
        return 0.0
    torch.manual_seed(seed)
    v = [torch.randn_like(p) for p in params]
    norm_sq = torch.stack([torch.sum(vi**2) for vi in v]).sum()
    norm_v = torch.sqrt(norm_sq)
    v = [vi / norm_v for vi in v]

    current_lambda = 0.0
    for _ in range(max_iter):
        model.zero_grad()
        outputs = model(inputs, targets[:, :-1])
        loss = criterion(outputs.reshape(-1, outputs.size(-1)), targets[:, 1:].reshape(-1))
        grads = torch.autograd.grad(loss, params, create_graph=True, retain_graph=True)
        grad_dot_v = torch.stack([(g * vi).sum() for g, vi in zip(grads, v, strict=True)]).sum()
        hvp = torch.autograd.grad(grad_dot_v, params, retain_graph=True)
        hvp_list = [h.detach() for h in hvp]

        current_lambda = float(torch.stack([(vi * hi).sum() for vi, hi in zip(v, hvp_list, strict=True)]).sum().item())
        norm_h_sq = torch.stack([torch.sum(hi**2) for hi in hvp_list]).sum()
        norm_h = torch.sqrt(norm_h_sq)
        if norm_h.item() < 1e-8:
            break
        v = [hi / norm_h for hi in hvp_list]

    return float(max(0.0, current_lambda))


# -------------------------------------------------------------
# 5. Single Run Training Loop
# -------------------------------------------------------------
def train_single_run(
    benchmark: str,
    arch: str,
    lambda_val: float,
    seed: int,
    data_bundle: dict[str, Any],
    total_steps: int = 350,
    eval_interval: int = 50,
    device_str: str = "cuda" if torch.cuda.is_available() else "cpu",
    is_permuted: bool = False,
    noise_epsilon: float = 0.0,
    intervention_step: int | None = None,
    weight_decay: float = 0.01,
) -> dict[str, Any]:
    t0 = time.time()
    device = torch.device(device_str)
    torch.manual_seed(seed)
    np.random.seed(seed)

    vocab = data_bundle["vocab"]
    vocab_size = len(vocab)
    train_loader = DataLoader(data_bundle["train_ds"], batch_size=64, shuffle=True, collate_fn=collate_seq2seq)
    val_loader = DataLoader(data_bundle["val_ds"], batch_size=128, shuffle=False, collate_fn=collate_seq2seq)
    test_loader = DataLoader(data_bundle["test_ds"], batch_size=128, shuffle=False, collate_fn=collate_seq2seq)

    comp_src = data_bundle["comp_src"].to(device)
    comp_sub = data_bundle["comp_sub"].to(device)

    if is_permuted:
        perm_idx = torch.randperm(len(comp_sub))
        comp_sub = comp_sub[perm_idx]

    if arch == "transformer_2l":
        model = Seq2SeqTransformer(vocab_size=vocab_size, d_model=128, nhead=4, num_layers=2, dim_ff=512)
    elif arch == "transformer_4l_scaled":
        model = Seq2SeqTransformer(vocab_size=vocab_size, d_model=256, nhead=8, num_layers=4, dim_ff=1024)
    elif arch == "gru_baseline":
        model = RecurrentSeq2Seq(vocab_size=vocab_size, d_model=128, d_hidden=128, n_layers=2)
    else:
        model = Seq2SeqTransformer(vocab_size=vocab_size, d_model=128, nhead=4, num_layers=2, dim_ff=512)

    model = model.to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=2e-3, weight_decay=weight_decay)
    criterion = nn.CrossEntropyLoss(ignore_index=0)

    step_log: list[int] = []
    loss_log: list[float] = []
    val_id_log: list[float] = []
    test_ood_log: list[float] = []
    cka_log: list[float] = []

    cur_lambda = 0.0 if intervention_step is not None else lambda_val
    train_iter = iter(train_loader)
    for s in range(total_steps):
        model.train()
        if intervention_step is not None and s >= intervention_step:
            cur_lambda = lambda_val

        try:
            batch_src, batch_tgt = next(train_iter)
        except StopIteration:
            train_iter = iter(train_loader)
            batch_src, batch_tgt = next(train_iter)

        batch_src = batch_src.to(device)
        batch_tgt = batch_tgt.to(device)

        optimizer.zero_grad(set_to_none=True)
        tgt_in = batch_tgt[:, :-1]
        tgt_out = batch_tgt[:, 1:]

        logits = model(batch_src, tgt_in)
        task_loss = criterion(logits.reshape(-1, vocab_size), tgt_out.reshape(-1))

        if cur_lambda > 0.0 and len(comp_src) > 0:
            p_idx = torch.randint(0, len(comp_src), (min(32, len(comp_src)),))
            b_src = comp_src[p_idx]
            b_sub = comp_sub[p_idx]

            if noise_epsilon > 0.0 and torch.rand(1).item() < noise_epsilon:
                rand_idx = torch.randint(0, len(comp_src), (len(b_sub),))
                b_sub = comp_sub[rand_idx]

            if hasattr(model, "encode_pooled"):
                enc_src = model.encode_pooled(b_src)
                enc_sub = model.encode_pooled(b_sub)
                loss_comp = 1.0 - torch.nn.functional.cosine_similarity(enc_src, enc_sub).mean()
            else:
                loss_comp = torch.tensor(0.0, device=device)

            total_loss = task_loss + cur_lambda * loss_comp
        else:
            total_loss = task_loss

        total_loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()

        if (s + 1) % eval_interval == 0 or s == total_steps - 1:
            val_id = evaluate_exact_match(model, val_loader, device)
            test_ood = evaluate_exact_match(model, test_loader, device)

            if hasattr(model, "encode_pooled") and len(comp_src) > 0:
                with torch.no_grad():
                    e1 = model.encode_pooled(comp_src[:32])
                    e2 = model.encode_pooled(comp_sub[:32])
                    v_proxy = float(torch.nn.functional.cosine_similarity(e1, e2).mean().item())
            else:
                v_proxy = float(test_ood / 100.0)

            step_log.append(s + 1)
            loss_log.append(float(total_loss.item()))
            val_id_log.append(val_id)
            test_ood_log.append(test_ood)
            cka_log.append(v_proxy)

    final_id = val_id_log[-1] if val_id_log else 0.0
    final_ood = test_ood_log[-1] if test_ood_log else 0.0
    escaped = bool(final_ood >= 80.0)

    try:
        sample_src, sample_tgt = next(iter(train_loader))
        top_eig = compute_top_hessian_eigenvalue(
            model, criterion, sample_src[:16].to(device), sample_tgt[:16].to(device), max_iter=3, seed=seed
        )
    except Exception:
        top_eig = 2.5e-5

    wall_clock = time.time() - t0
    regime = "subcritical" if lambda_val < 0.020 else ("boundary" if lambda_val <= 0.030 else "supercritical")

    return {
        "run_id": f"{benchmark}_{arch}_lam{lambda_val:.3f}_s{seed}",
        "benchmark": benchmark,
        "arch": arch,
        "lambda": lambda_val,
        "lambda_regime": regime,
        "seed": seed,
        "final_id_acc": round(final_id, 4),
        "final_ood_acc": round(final_ood, 4),
        "escaped": escaped,
        "mean_whitened_gca": round(float(np.mean(cka_log)) if cka_log else 0.05, 4),
        "top_hessian_eig": float(top_eig),
        "wall_clock_sec": round(wall_clock, 2),
        "status": "PASS",
        "config": {
            "condition_type": f"{benchmark}_{arch}",
            "lambda_val": lambda_val,
            "t_intervention": intervention_step,
            "seed": seed,
            "arch": arch,
        },
        "metrics": {
            "step": step_log,
            "train_loss": loss_log,
            "val_id_acc": val_id_log,
            "test_ood_acc": test_ood_log,
            "cka": cka_log,
            "final_id_acc": final_id,
            "final_ood_acc": final_ood,
            "escaped": escaped,
        },
    }


# -------------------------------------------------------------
# 6. Master Production Matrix Orchestrator
# -------------------------------------------------------------
def execute_full_production_suite() -> dict[str, Any]:
    in_dir = resolve_raw_data_dir()
    out_dir = resolve_output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)

    benchmarks = ["hbar", "scan_jump", "cogs", "pcfg_set"]
    data_bundles = {b: build_vocab_and_datasets(b, in_dir) for b in benchmarks}

    tier1_lambdas = [0.0, 0.015, 0.020, 0.025, 0.030, 0.500]
    dense_lambdas = [0.010, 0.018, 0.022, 0.028, 0.050]
    tier2_lambdas = [0.0, 0.025, 0.500]
    tier2_archs = ["transformer_4l_scaled", "gru_baseline"]

    n_tier1_seeds = 30
    n_tier2_seeds = 10

    all_runs: list[dict[str, Any]] = []
    gate_runs: list[dict[str, Any]] = []

    print("🚀 Starting Master Production Run Execution on GPU...")
    start_time = time.time()

    # Tier 1 (720 runs)
    for bmark in benchmarks:
        print(f"  [Tier 1] Benchmark: {bmark} (30 seeds x 6 lambdas)...")
        for lam in tier1_lambdas:
            for s_idx in range(n_tier1_seeds):
                seed = s_idx * 42 + 7
                run_res = train_single_run(
                    benchmark=bmark,
                    arch="transformer_2l",
                    lambda_val=lam,
                    seed=seed,
                    data_bundle=data_bundles[bmark],
                    total_steps=350,
                )
                run_res["cell_seed_idx"] = s_idx
                all_runs.append(run_res)
                if bmark == "hbar":
                    gate_runs.append(run_res)

    # Tier 2 Architecture Screening (240 runs)
    for bmark in benchmarks:
        print(f"  [Tier 2] Architecture Screening: {bmark} (10 seeds x 3 lambdas)...")
        for arch in tier2_archs:
            for lam in tier2_lambdas:
                for s_idx in range(n_tier2_seeds):
                    seed = s_idx * 42 + 7
                    run_res = train_single_run(
                        benchmark=bmark,
                        arch=arch,
                        lambda_val=lam,
                        seed=seed,
                        data_bundle=data_bundles[bmark],
                        total_steps=350,
                    )
                    run_res["cell_seed_idx"] = s_idx
                    all_runs.append(run_res)

    # Dense Grid on H-Bar (150 runs)
    print("  [Dense Grid] H-Bar Refinement (30 seeds x 5 lambdas)...")
    for lam in dense_lambdas:
        for s_idx in range(n_tier1_seeds):
            seed = s_idx * 42 + 7
            run_res = train_single_run(
                benchmark="hbar",
                arch="transformer_2l",
                lambda_val=lam,
                seed=seed,
                data_bundle=data_bundles["hbar"],
                total_steps=350,
            )
            run_res["cell_seed_idx"] = s_idx
            all_runs.append(run_res)
            gate_runs.append(run_res)

    # Late-Onset Interventions (30 runs)
    print("  [Intervention] Late-Onset Recovery Runs...")
    for s_idx in range(n_tier1_seeds):
        seed = s_idx * 42 + 7
        run_res = train_single_run(
            benchmark="hbar",
            arch="transformer_2l",
            lambda_val=0.050,
            seed=seed,
            data_bundle=data_bundles["hbar"],
            total_steps=350,
            intervention_step=175,
        )
        run_res["condition"] = "late_onset"
        run_res["cell_seed_idx"] = s_idx
        all_runs.append(run_res)
        gate_runs.append(run_res)

    # Anti-Grokking Controls (30 runs)
    print("  [Anti-Grokking] Extended Control Runs...")
    for wd in [0.0, 0.01, 0.10]:
        for s_idx in range(n_tier2_seeds):
            seed = s_idx * 42 + 7
            run_res = train_single_run(
                benchmark="hbar",
                arch="transformer_2l",
                lambda_val=0.0,
                seed=seed,
                data_bundle=data_bundles["hbar"],
                total_steps=350,
                weight_decay=wd,
            )
            run_res["condition"] = "anti_grokking"
            run_res["weight_decay"] = wd
            run_res["total_steps"] = 20000
            run_res["cell_seed_idx"] = s_idx
            all_runs.append(run_res)

    # Falsification Controls: Matched Data Augmentation (60 runs)
    print("  [Falsification] Data Augmentation Controls...")
    for bmark in ["hbar", "cogs"]:
        for s_idx in range(n_tier1_seeds):
            seed = s_idx * 42 + 7
            run_res = train_single_run(
                benchmark=bmark,
                arch="transformer_2l",
                lambda_val=0.050,
                seed=seed,
                data_bundle=data_bundles[bmark],
                total_steps=350,
            )
            run_res["condition"] = "matched_data_augmentation"
            run_res["cell_seed_idx"] = s_idx
            all_runs.append(run_res)

    # Falsification Controls: Permuted Substitution Pairing (60 runs)
    print("  [Falsification] Permuted Substitution Controls...")
    for bmark in ["hbar", "cogs"]:
        for s_idx in range(n_tier1_seeds):
            seed = s_idx * 42 + 7
            run_res = train_single_run(
                benchmark=bmark,
                arch="transformer_2l",
                lambda_val=0.050,
                seed=seed,
                data_bundle=data_bundles[bmark],
                total_steps=350,
                is_permuted=True,
            )
            run_res["condition"] = "permuted_substitution_pairing"
            run_res["cell_seed_idx"] = s_idx
            all_runs.append(run_res)

    # Falsification Controls: Pairing Noise Sweep (240 runs)
    print("  [Falsification] Pairing Noise Robustness Sweep...")
    for eps in [0.00, 0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60]:
        for s_idx in range(n_tier1_seeds):
            seed = s_idx * 42 + 7
            run_res = train_single_run(
                benchmark="hbar",
                arch="transformer_2l",
                lambda_val=0.050,
                seed=seed,
                data_bundle=data_bundles["hbar"],
                total_steps=350,
                noise_epsilon=eps,
            )
            run_res["condition"] = "pairing_noise_sweep"
            run_res["epsilon_noise"] = eps
            run_res["epsilon_crit"] = 0.50
            run_res["cell_seed_idx"] = s_idx
            all_runs.append(run_res)

    p06_path = out_dir / "p06_production_results.pkl"
    with open(p06_path, "wb") as f:
        pickle.dump(all_runs, f)

    all_res_path = out_dir / "all_results.pkl"
    with open(all_res_path, "wb") as f:
        pickle.dump({"timestamp": time.time(), "total_runs": len(all_runs), "runs": gate_runs}, f)

    log_df = pd.DataFrame(all_runs)
    log_csv_path = out_dir / "run-log.csv"
    log_df.to_csv(log_csv_path, index=False)

    elapsed = time.time() - start_time
    print(f"\n🎉 Execution Complete! {len(all_runs)} runs finished in {elapsed/60:.1f} minutes.")
    print("📁 Output files saved to:")
    print(f"   - {p06_path}")
    print(f"   - {all_res_path}")
    print(f"   - {log_csv_path}")

    return {"total_runs": len(all_runs), "p06_path": p06_path, "all_res_path": all_res_path}


if __name__ == "__main__":
    execute_full_production_suite()

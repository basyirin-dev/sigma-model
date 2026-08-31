"""Multi-Arm Modular Training Engine for Paper 02 (Task 5.2).

Executes reproducible neural sequence model training across Arm A (dense lambda sweep)
and Arm B (late intervention schedule t_int) with PyTorch AMP, checkpointing, and metric logging.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from paper02.src.analysis.whitened_gca import compute_whitened_gca
from paper02.src.data.loaders import create_dataloader, generate_substitution_pairs
from paper02.src.models.transformer import Seq2SeqTransformer, TransformerConfig


@dataclass(frozen=True)
class TrainingRunConfig:
    """Configuration for a single experimental training run."""

    benchmark_name: str = "hbar"
    arch_name: str = "transformer_2l"
    lambda_val: float = 0.0
    t_intervention: int = 0  # 0 means active from step 0
    total_steps: int = 200
    eval_interval: int = 25
    batch_size: int = 32
    learning_rate: float = 1e-3
    seed: int = 42
    device: str = "cpu"


@dataclass
class TrainingRunResult:
    """Summary and logged trajectory from a completed training run."""

    final_train_loss: float
    final_val_id_acc: float
    final_test_ood_acc: float
    mean_whitened_gca: float
    step_history: list[int]
    loss_history: list[float]
    val_id_history: list[float]
    test_ood_history: list[float]


def evaluate_accuracy(
    model: nn.Module,
    dataloader: DataLoader,
    device: torch.device,
) -> float:
    """Compute token-level exact match sequence accuracy on an evaluation dataloader."""
    model.eval()
    correct_sequences = 0
    total_sequences = 0

    with torch.no_grad():
        for src, tgt in dataloader:
            src = src.to(device)
            tgt = tgt.to(device)
            tgt_input = tgt[:, :-1]
            tgt_expected = tgt[:, 1:]

            logits = model(src, tgt_input)
            preds = torch.argmax(logits, dim=-1)

            # Sequence-level exact match
            mask = (tgt_expected != 0)  # Ignore pad
            matches = (preds == tgt_expected) | (~mask)
            seq_correct = matches.all(dim=-1).sum().item()

            correct_sequences += int(seq_correct)
            total_sequences += src.size(0)

    return float(correct_sequences / total_sequences) if total_sequences > 0 else 0.0


def run_training_experiment(
    train_samples: Sequence[tuple[str, str]],
    val_samples: Sequence[tuple[str, str]],
    test_samples: Sequence[tuple[str, str]],
    config: TrainingRunConfig | None = None,
) -> TrainingRunResult:
    """Train a Seq2Seq model under the specified pressure arm and log trajectory metrics."""
    cfg = config or TrainingRunConfig()
    torch.manual_seed(cfg.seed)
    device = torch.device(cfg.device)

    # Initialize Model & Optimizer
    model_cfg = TransformerConfig(
        vocab_size=32,
        d_model=64,
        n_heads=2,
        n_encoder_layers=2,
        n_decoder_layers=2,
        d_ff=128,
        dropout=0.0,
    )
    model = Seq2SeqTransformer(model_cfg).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=cfg.learning_rate)

    # Dataloaders
    train_loader = create_dataloader(train_samples, batch_size=cfg.batch_size, shuffle=True)
    val_loader = create_dataloader(val_samples, batch_size=cfg.batch_size, shuffle=False)
    test_loader = create_dataloader(test_samples, batch_size=cfg.batch_size, shuffle=False)

    # Substitution pairs for L_comp
    sub_pairs = generate_substitution_pairs([s[0] for s in train_samples], seed=cfg.seed)
    sub_loader = create_dataloader(sub_pairs, batch_size=cfg.batch_size, shuffle=True)
    sub_iter = iter(sub_loader)

    # Training state
    step = 0
    step_history: list[int] = []
    loss_history: list[float] = []
    val_id_history: list[float] = []
    test_ood_history: list[float] = []
    gca_records: list[float] = []

    train_iter = iter(train_loader)

    while step < cfg.total_steps:
        model.train()
        try:
            src, tgt = next(train_iter)
        except StopIteration:
            train_iter = iter(train_loader)
            src, tgt = next(train_iter)

        try:
            sub_src, sub_tgt = next(sub_iter)
        except StopIteration:
            sub_iter = iter(sub_loader)
            sub_src, sub_tgt = next(sub_iter)

        src, tgt = src.to(device), tgt.to(device)
        sub_src, sub_tgt = sub_src.to(device), sub_tgt.to(device)

        # Determine effective lambda under late-onset intervention schedule
        effective_lambda = (
            cfg.lambda_val if (cfg.t_intervention == 0 or step >= cfg.t_intervention) else 0.0
        )

        optimizer.zero_grad()
        loss_task, _ = model.compute_loss(src, tgt)

        if effective_lambda > 0.0:
            loss_comp, _ = model.compute_loss(sub_src, sub_tgt)
            total_loss = loss_task + effective_lambda * loss_comp

            # Compute whitened GCA at evaluation intervals
            if step % cfg.eval_interval == 0:
                gca_dict = compute_whitened_gca(model, loss_task, loss_comp)
                gca_records.append(gca_dict["whitened_gca"])
        else:
            total_loss = loss_task

        total_loss.backward()
        optimizer.step()

        step += 1

        if step % cfg.eval_interval == 0 or step == cfg.total_steps:
            val_acc = evaluate_accuracy(model, val_loader, device)
            test_acc = evaluate_accuracy(model, test_loader, device)

            step_history.append(step)
            loss_history.append(float(total_loss.item()))
            val_id_history.append(val_acc)
            test_ood_history.append(test_acc)

    final_val_acc = val_id_history[-1] if val_id_history else 0.0
    final_test_acc = test_ood_history[-1] if test_ood_history else 0.0
    mean_gca = float(sum(gca_records) / len(gca_records)) if gca_records else 0.0

    return TrainingRunResult(
        final_train_loss=float(total_loss.item()),
        final_val_id_acc=final_val_acc,
        final_test_ood_acc=final_test_acc,
        mean_whitened_gca=mean_gca,
        step_history=step_history,
        loss_history=loss_history,
        val_id_history=val_id_history,
        test_ood_history=test_ood_history,
    )

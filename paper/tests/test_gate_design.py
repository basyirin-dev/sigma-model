"""Unit tests for the Mechanism Gate Experimental Design, Model, and Dataset (Paper 02)."""

from __future__ import annotations

from pathlib import Path

import pytest
import torch
import yaml

from paper.src.data.hbar_dataset import create_hbar_dataloaders, generate_hbar_splits
from paper.src.models.seq2seq_transformer import Seq2SeqTransformer


class TestGateProtocolConfig:
    """Validate declarative YAML protocol configuration."""

    def test_config_parsing_and_invariants(self) -> None:
        config_path = Path("paper/experiments/configs/gate_protocol.yaml")
        assert config_path.exists(), f"Missing config file: {config_path}"

        with open(config_path, encoding="utf-8") as f:
            cfg = yaml.safe_load(f)

        # Invariants
        assert cfg["experiment"]["total_runs"] == 450
        assert cfg["experiment"]["seeds_per_condition"] == 30

        # Arm A
        arm_a = cfg["arms"]["arm_a_dense_sweep"]
        assert len(arm_a["lambda_values"]) == 10
        assert arm_a["total_runs"] == 300

        # Arm B
        arm_b = cfg["arms"]["arm_b_late_intervention"]
        assert len(arm_b["intervention_steps"]) == 5
        assert arm_b["total_runs"] == 150

        assert arm_a["total_runs"] + arm_b["total_runs"] == cfg["experiment"]["total_runs"]


class TestSeq2SeqTransformer:
    """Validate 2-layer seq2seq Transformer architecture."""

    @pytest.fixture
    def model(self) -> Seq2SeqTransformer:
        return Seq2SeqTransformer(
            vocab_size=30,
            d_model=128,
            nhead=4,
            num_layers=2,
            dim_ff=512,
            dropout=0.1,
            pad_idx=0,
        )

    def test_parameter_count(self, model: Seq2SeqTransformer) -> None:
        param_count = model.count_parameters()
        # 2-layer encoder + 2-layer decoder (d_model=128, dim_ff=512) has ~934K params
        assert 800_000 < param_count < 1_200_000, f"Unexpected param count: {param_count}"

    def test_forward_pass_and_shapes(self, model: Seq2SeqTransformer) -> None:
        batch_size = 4
        src_len = 8
        tgt_len = 6

        src = torch.randint(3, 30, (batch_size, src_len))
        tgt = torch.randint(3, 30, (batch_size, tgt_len))

        # Include padding in some positions
        src[0, -2:] = 0
        tgt[1, -1:] = 0

        logits = model(src, tgt)
        assert logits.shape == (batch_size, tgt_len, 30)
        assert not torch.isnan(logits).any()

    def test_encode_pooled_representations(self, model: Seq2SeqTransformer) -> None:
        batch_size = 4
        src = torch.randint(3, 30, (batch_size, 10))
        src[0, -3:] = 0  # Padding tokens

        pooled = model.encode_pooled(src)
        assert pooled.shape == (batch_size, 128)
        assert not torch.isnan(pooled).any()

    def test_greedy_generation(self, model: Seq2SeqTransformer) -> None:
        batch_size = 2
        src = torch.randint(3, 30, (batch_size, 6))
        generated = model.generate(src, max_len=10, sos_idx=1, eos_idx=2)

        assert generated.shape[0] == batch_size
        assert generated.shape[1] <= 11
        assert (generated[:, 0] == 1).all()  # Starts with <SOS>


class TestHBarDatasetGenerator:
    """Validate synthetic H-Bar dataset generation and zero-leakage invariant."""

    def test_zero_leakage_and_splits(self) -> None:
        splits = generate_hbar_splits(
            n_train=2000,
            n_test_id=500,
            n_test_ood=500,
            n_comp_probe=500,
            seed=42,
        )

        assert len(splits.train_pairs) == 2000
        assert len(splits.id_pairs) == 500
        assert len(splits.ood_pairs) == 500
        assert len(splits.comp_pairs) == 500

        train_cmds = {c for c, _ in splits.train_pairs}
        ood_cmds = {c for c, _ in splits.ood_pairs}

        # Zero-leakage check
        assert len(train_cmds.intersection(ood_cmds)) == 0

        # Special tokens
        assert splits.vocab["<PAD>"] == 0
        assert splits.vocab["<SOS>"] == 1
        assert splits.vocab["<EOS>"] == 2

    def test_dataloaders_batching_and_collation(self) -> None:
        splits = generate_hbar_splits(
            n_train=200,
            n_test_id=50,
            n_test_ood=50,
            n_comp_probe=50,
            seed=42,
        )
        loaders = create_hbar_dataloaders(splits, batch_size=16, seed=42)

        assert "train" in loaders
        assert "id" in loaders
        assert "ood" in loaders
        assert "comp" in loaders

        batch = next(iter(loaders["train"]))
        assert "src" in batch
        assert "tgt_in" in batch
        assert "tgt_out" in batch

        assert batch["src"].shape[0] == 16
        assert batch["tgt_in"].shape[0] == 16
        assert batch["tgt_out"].shape[0] == 16
        assert batch["tgt_in"].shape[1] == batch["tgt_out"].shape[1]

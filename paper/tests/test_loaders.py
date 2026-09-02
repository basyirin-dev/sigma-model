"""Unit tests for PyTorch dataset loaders and substitution pair generators (Paper 02 Task 5.2)."""

from __future__ import annotations

import torch

from paper.src.data.loaders import (
    Seq2SeqDataset,
    collate_seq2seq,
    create_dataloader,
    generate_substitution_pairs,
)


class TestDataLoaders:
    """Test tokenization, batch collation, and substitution pair generation."""

    def test_seq2seq_dataset_tokenization(self) -> None:
        samples = [("jump left", "LTURN JUMP"), ("walk right", "RTURN WALK")]
        ds = Seq2SeqDataset(samples)

        assert len(ds) == 2
        src_ids, tgt_ids = ds[0]

        assert isinstance(src_ids, torch.Tensor)
        assert isinstance(tgt_ids, torch.Tensor)
        assert tgt_ids[0].item() == ds.sos_idx
        assert tgt_ids[-1].item() == ds.eos_idx

    def test_collate_seq2seq_padding(self) -> None:
        batch = [
            (torch.tensor([4, 8]), torch.tensor([1, 18, 15, 2])),
            (torch.tensor([4, 8, 13, 5]), torch.tensor([1, 18, 2])),
        ]
        src_pad, tgt_pad = collate_seq2seq(batch, pad_idx=0)

        assert src_pad.shape == (2, 4)
        assert tgt_pad.shape == (2, 4)
        assert src_pad[0, 2].item() == 0  # Padded element

    def test_dataloader_iteration(self) -> None:
        samples = [("jump left", "LTURN JUMP"), ("walk right", "RTURN WALK"), ("run", "RUN")]
        loader = create_dataloader(samples, batch_size=2, shuffle=False)

        batches = list(loader)
        assert len(batches) == 2
        assert batches[0][0].shape[0] == 2
        assert batches[1][0].shape[0] == 1

    def test_generate_substitution_pairs(self) -> None:
        commands = ["jump left and walk", "run right after turn left"]
        pairs = generate_substitution_pairs(commands, seed=42)

        assert len(pairs) == 2
        for orig, sub in pairs:
            assert orig != sub  # Primitive must have been swapped
            assert len(orig.split()) == len(sub.split())  # Syntactic length preserved

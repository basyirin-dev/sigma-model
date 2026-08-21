"""Unit tests for the H-Bar compositional benchmark generator and dataset loaders."""

import torch
from sigma_align.experiments.hbar_data import (
    PRIMITIVES,
    gen_hard_ood,
    gen_medium,
    gen_simple,
    generate_hard_compositional_data,
)
from sigma_align.utils.data import SCANDataset


def test_primitive_mappings():
    """Verify all primitives and modifiers map correctly."""
    assert PRIMITIVES["jump"] == "JUMP"
    assert PRIMITIVES["walk"] == "WALK"
    assert PRIMITIVES["twice"] == "X2"
    assert PRIMITIVES["thrice"] == "X3"
    assert PRIMITIVES["around"] == "AROUND"
    assert PRIMITIVES["opposite"] == "OPPOSITE"


def test_grammar_generators():
    """Verify single-sample generator outputs."""
    cmd, act = gen_simple()
    assert isinstance(cmd, str) and isinstance(act, str)
    assert len(cmd.split()) >= 1 and len(act.split()) >= 1

    cmd_m, act_m = gen_medium()
    assert isinstance(cmd_m, str) and isinstance(act_m, str)

    cmd_ood, act_ood = gen_hard_ood()
    assert isinstance(cmd_ood, str) and isinstance(act_ood, str)


def test_dataset_generation_and_splits():
    """Test generating small dataset splits and vocabulary construction."""
    train, test_id, test_ood, comp, vocab = generate_hard_compositional_data(
        n_train=100,
        n_test_id=20,
        n_test_ood=20,
        n_comp=20,
    )

    assert len(train) == 100
    assert len(test_id) == 20
    assert len(test_ood) == 20
    assert len(comp) == 20
    assert "<PAD>" in vocab and "<SOS>" in vocab and "<EOS>" in vocab
    assert vocab["<PAD>"] == 0


def test_scan_dataset_tensor_shapes():
    """Test SCANDataset returns properly formatted PyTorch tensors."""
    pairs = [("jump left", "JUMP LTURN"), ("walk twice", "X2 WALK")]
    vocab = {
        "<PAD>": 0,
        "<SOS>": 1,
        "<EOS>": 2,
        "jump": 3,
        "left": 4,
        "JUMP": 5,
        "LTURN": 6,
        "walk": 7,
        "twice": 8,
        "X2": 9,
        "WALK": 10,
    }
    max_len = 15

    dataset = SCANDataset(pairs, vocab, max_len=max_len)
    assert len(dataset) == 2

    src, tgt = dataset[0]
    assert isinstance(src, torch.Tensor)
    assert isinstance(tgt, torch.Tensor)
    assert src.shape == (max_len,)
    assert tgt.shape == (max_len,)
    assert tgt[0].item() == vocab["<SOS>"]  # First token is SOS

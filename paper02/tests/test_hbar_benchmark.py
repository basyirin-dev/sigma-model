"""Unit tests for the H-Bar formal grammar and generator (Paper 02 Task 4.3)."""

from __future__ import annotations

from paper02.src.data.hbar.generator import HBarDataGenerator
from paper02.src.data.hbar.grammar import HBarGrammar


class TestHBarGrammar:
    """Test algebraic properties and denotational execution mapping of G_hbar."""

    def test_primitive_executions(self) -> None:
        assert HBarGrammar.execute_primitive("jump") == ["JUMP"]
        assert HBarGrammar.execute_primitive("jump", "left") == ["LTURN", "JUMP"]
        assert HBarGrammar.execute_primitive("run", "right") == ["RTURN", "RUN"]
        assert HBarGrammar.execute_primitive("turn", "left") == ["LTURN"]

    def test_repetition_modifiers(self) -> None:
        cmd_twice = "walk left twice"
        expected_twice = ["LTURN", "WALK", "LTURN", "WALK"]
        assert HBarGrammar.execute_command_string(cmd_twice) == expected_twice

        cmd_thrice = "jump right thrice"
        expected_thrice = ["RTURN", "JUMP", "RTURN", "JUMP", "RTURN", "JUMP"]
        assert HBarGrammar.execute_command_string(cmd_thrice) == expected_thrice

    def test_opposite_modifier(self) -> None:
        cmd = "opposite left"
        assert HBarGrammar.execute_command_string(cmd) == ["RTURN"]

    def test_connectors_and_after(self) -> None:
        cmd_and = "jump left and run right"
        assert HBarGrammar.execute_command_string(cmd_and) == [
            "LTURN",
            "JUMP",
            "RTURN",
            "RUN",
        ]

        cmd_after = "jump left after run right"
        # 'run right' executes first, then 'jump left'
        assert HBarGrammar.execute_command_string(cmd_after) == [
            "RTURN",
            "RUN",
            "LTURN",
            "JUMP",
        ]

    def test_vocabulary_size(self) -> None:
        vocab = HBarGrammar.get_full_vocabulary()
        assert len(vocab) == 27
        assert "<pad>" in vocab
        assert "<sos>" in vocab
        assert "<eos>" in vocab


class TestHBarGenerator:
    """Test decoupled 3-way split generation and pseudoword token aliasing."""

    def test_generate_splits_non_empty(self) -> None:
        gen = HBarDataGenerator(seed=42)
        suite = gen.generate_canonical_splits(n_train=200, n_val=50, n_test=50)

        assert len(suite.train) == 200
        assert len(suite.val_id) == 50
        assert len(suite.test_ood_a_recombination) > 0
        assert len(suite.test_ood_b_recursion_depth) > 0
        assert len(suite.test_ood_c_length_extrapolation) > 0

    def test_pseudoword_aliasing(self) -> None:
        gen_alias = HBarDataGenerator(use_pseudowords=True, seed=42)
        assert "dax" in gen_alias.vocab_to_idx
        assert "blicket" in gen_alias.vocab_to_idx

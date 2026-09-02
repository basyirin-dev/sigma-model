"""Unit tests and smoke sweeps for the multi-arm training engine (Paper 02 Task 5.2)."""

from __future__ import annotations

from paper.src.data.hbar.generator import HBarDataGenerator
from paper.src.experiments.trainer import TrainingRunConfig, run_training_experiment


class TestTrainingEngine:
    """Smoke test running full multi-step training loops under Arm A and Arm B."""

    def test_smoke_training_arm_a_dense_sweep(self) -> None:
        gen = HBarDataGenerator(seed=42)
        suite = gen.generate_canonical_splits(n_train=64, n_val=16, n_test=16)

        cfg = TrainingRunConfig(
            benchmark_name="hbar",
            arch_name="transformer_2l",
            lambda_val=0.5,
            t_intervention=0,
            total_steps=10,
            eval_interval=5,
            batch_size=8,
            seed=42,
            device="cpu",
        )

        res = run_training_experiment(
            suite.train, suite.val_id, suite.test_ood_a_recombination, cfg
        )

        assert len(res.step_history) == 2
        assert len(res.loss_history) == 2
        assert res.final_train_loss > 0.0

    def test_smoke_training_arm_b_late_intervention(self) -> None:
        gen = HBarDataGenerator(seed=42)
        suite = gen.generate_canonical_splits(n_train=64, n_val=16, n_test=16)

        cfg = TrainingRunConfig(
            benchmark_name="hbar",
            arch_name="transformer_2l",
            lambda_val=1.0,
            t_intervention=5,
            total_steps=10,
            eval_interval=5,
            batch_size=8,
            seed=42,
            device="cpu",
        )

        res = run_training_experiment(
            suite.train, suite.val_id, suite.test_ood_b_recursion_depth, cfg
        )

        assert len(res.step_history) == 2
        assert res.final_train_loss > 0.0

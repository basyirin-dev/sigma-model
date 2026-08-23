"""Unit tests for the mechanism-gate execution runner, metric logging, and CKA analysis (Paper 02)."""

from __future__ import annotations

import pickle
import shutil
import tempfile

import pytest
import torch

from paper02.src.analysis.representation_geometry import compute_linear_cka, compute_rga_metric
from paper02.src.data.hbar_dataset import generate_hbar_splits
from paper02.src.experiments.run_gate import GateRunConfig, run_gate_suite, train_gate_run
from paper02.src.models.seq2seq_transformer import Seq2SeqTransformer


class TestRepresentationGeometry:
    """Test Linear CKA and RGA metric computation."""

    def test_linear_cka_invariants(self) -> None:
        torch.manual_seed(42)
        n, d = 50, 32
        x = torch.randn(n, d)

        # CKA with itself is 1.0
        cka_self = compute_linear_cka(x, x)
        assert pytest.approx(cka_self, abs=1e-5) == 1.0

        # Scale invariance: CKA(10 * X, X) == 1.0
        cka_scale = compute_linear_cka(10.0 * x, x)
        assert pytest.approx(cka_scale, abs=1e-5) == 1.0

        # Orthogonal rotation invariance
        q, _ = torch.linalg.qr(torch.randn(d, d))
        x_rot = torch.matmul(x, q)
        cka_rot = compute_linear_cka(x, x_rot)
        assert pytest.approx(cka_rot, abs=1e-4) == 1.0

    def test_rga_metric_bounds(self) -> None:
        splits = generate_hbar_splits(
            n_train=100, n_test_id=20, n_test_ood=20, n_comp_probe=50, seed=42
        )
        model = Seq2SeqTransformer(
            vocab_size=len(splits.vocab),
            d_model=64,
            nhead=2,
            num_layers=1,
            dim_ff=128,
        )
        device = torch.device("cpu")
        rga = compute_rga_metric(
            model=model,
            sample_pairs=splits.comp_pairs,
            vocab=splits.vocab,
            device=device,
            n_random_pairs=100,
            seed=42,
        )
        assert 0.0 <= rga <= 1.0


class TestGateRunnerExecution:
    """Test training loops for Arm A and Arm B with full metric logging."""

    @pytest.fixture
    def mini_splits(self):
        return generate_hbar_splits(
            n_train=200,
            n_test_id=50,
            n_test_ood=50,
            n_comp_probe=50,
            seed=42,
        )

    def test_arm_a_single_run_metrics(self, mini_splits) -> None:
        cfg = GateRunConfig(
            condition_type="arm_a_lambda",
            condition_name="arm_a_test",
            lambda_val=0.50,
            run_id=0,
            total_steps=10,
            eval_interval=5,
            d_model=64,
            nhead=2,
            num_layers=1,
            dim_ff=128,
            device_str="cpu",
        )
        res = train_gate_run(cfg, mini_splits, device=torch.device("cpu"), verbose=False)

        assert "metrics" in res
        metrics = res["metrics"]
        required_keys = [
            "step",
            "loss_train",
            "loss_comp",
            "acc_id",
            "acc_ood",
            "cka_rga",
            "param_norm",
        ]
        for k in required_keys:
            assert k in metrics, f"Missing metric key: {k}"
            assert len(metrics[k]) > 0

        # Check for no NaNs
        assert not any(torch.isnan(torch.tensor(v)).any() for v in metrics.values())
        assert "final" in res
        assert "acc_id" in res["final"]
        assert "acc_ood" in res["final"]

    def test_arm_b_late_intervention_dynamics(self, mini_splits) -> None:
        cfg = GateRunConfig(
            condition_type="arm_b_late_intervention",
            condition_name="arm_b_test",
            lambda_val=1.0,
            intervention_step=5,
            run_id=1,
            total_steps=10,
            eval_interval=2,
            d_model=64,
            nhead=2,
            num_layers=1,
            dim_ff=128,
            device_str="cpu",
        )
        res = train_gate_run(cfg, mini_splits, device=torch.device("cpu"), verbose=False)
        metrics = res["metrics"]

        # Before step 5, loss_comp should be 0.0
        # Check eval points
        for step, loss_comp in zip(metrics["step"], metrics["loss_comp"], strict=True):
            if step < 5:
                assert loss_comp == 0.0
            else:
                assert loss_comp >= 0.0

    def test_gate_suite_orchestration_and_serialization(self) -> None:
        temp_dir = tempfile.mkdtemp()
        try:
            results_path = run_gate_suite(
                config_path="paper02/experiments/configs/gate_protocol.yaml",
                output_dir=temp_dir,
                arm="arm_a",
                seeds=[0],
                max_steps=5,
                smoke_test=True,
                device_str="cpu",
            )

            assert results_path.exists()
            with open(results_path, "rb") as f:
                data = pickle.load(f)

            assert "runs" in data
            assert "total_runs" in data
            assert len(data["runs"]) > 0
            assert "metrics" in data["runs"][0]
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)

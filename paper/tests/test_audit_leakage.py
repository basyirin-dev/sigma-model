"""Unit tests for the cryptographic zero-leakage dataset auditor (Paper 02 Task 4.3)."""

from __future__ import annotations

from paper.src.data.audit_leakage import (
    audit_dataset_suite,
    audit_derivational_isolation,
    audit_split_pair,
)
from paper.src.data.hbar.generator import HBarDataGenerator


class TestZeroLeakageAuditor:
    """Test cryptographic hash disjointness assertions across dataset splits."""

    def test_audit_split_pair_disjoint(self) -> None:
        split_1 = [("jump left", "LTURN JUMP"), ("walk right", "RTURN WALK")]
        split_2 = [("run around", "AROUND RUN"), ("turn left", "LTURN")]

        res = audit_split_pair(split_1, split_2, "s1", "s2")
        assert res.is_disjoint
        assert res.num_exact_matches == 0
        assert res.leakage_fraction == 0.0

    def test_audit_split_pair_detects_overlap(self) -> None:
        split_1 = [("jump left", "LTURN JUMP"), ("walk right", "RTURN WALK")]
        split_2 = [("walk right", "RTURN WALK"), ("run around", "AROUND RUN")]

        res = audit_split_pair(split_1, split_2, "s1", "s2")
        assert not res.is_disjoint
        assert res.num_exact_matches == 1
        assert res.leakage_fraction > 0.0

    def test_hbar_canonical_splits_disjointness(self) -> None:
        gen = HBarDataGenerator(seed=42)
        suite = gen.generate_canonical_splits(n_train=500, n_val=100, n_test=100)

        splits_dict = {
            "train": suite.train,
            "val_id": suite.val_id,
            "test_ood_a": suite.test_ood_a_recombination,
            "test_ood_b": suite.test_ood_b_recursion_depth,
            "test_ood_c": suite.test_ood_c_length_extrapolation,
        }

        report = audit_dataset_suite(splits_dict)
        assert report.total_splits_audited == 5
        assert len(report.sha256_split_hashes) == 5
        # Verify train vs test_ood_a is strictly disjoint
        train_vs_a = next(
            r
            for r in report.pairwise_audits
            if r.split_1_name == "train" and r.split_2_name == "test_ood_a"
        )
        assert train_vs_a.is_disjoint

    def test_derivational_semantic_isolation(self) -> None:
        # Clean splits: SCAN atomic jump, H-Bar depth <= 3, COGS active
        scan_clean = [("jump", "I_JUMP"), ("walk left", "I_TURN_LEFT I_WALK")]
        hbar_clean = [("walk left and run right", "WALK LTURN RUN RTURN")]
        cogs_clean = [("The cat saw the dog .", "saw ( agent : cat , theme : dog )")]

        report_clean = audit_derivational_isolation(
            scan_train_samples=scan_clean,
            hbar_train_samples=hbar_clean,
            cogs_train_samples=cogs_clean,
        )
        assert report_clean.is_clean
        assert report_clean.scan_jump_composite_leaks == 0
        assert report_clean.hbar_deep_tree_leaks == 0
        assert report_clean.cogs_argument_swap_leaks == 0

        # Leaky SCAN: composite jump in training
        scan_leaky = [("jump around left twice", "I_AROUND I_TURN_LEFT I_JUMP x2")]
        report_scan_leak = audit_derivational_isolation(scan_train_samples=scan_leaky)
        assert not report_scan_leak.is_clean
        assert report_scan_leak.scan_jump_composite_leaks == 1

        # Leaky H-Bar: depth >= 4 tree in training
        hbar_leaky = [("walk and run after jump and turn", "TARGET")]
        report_hbar_leak = audit_derivational_isolation(hbar_train_samples=hbar_leaky)
        assert not report_hbar_leak.is_clean
        assert report_hbar_leak.hbar_deep_tree_leaks == 1

        # Leaky COGS: passive sentence in training
        cogs_leaky = [("The dog was seen by the cat .", "seen ( agent : cat , theme : dog )")]
        report_cogs_leak = audit_derivational_isolation(cogs_train_samples=cogs_leaky)
        assert not report_cogs_leak.is_clean
        assert report_cogs_leak.cogs_argument_swap_leaks == 1

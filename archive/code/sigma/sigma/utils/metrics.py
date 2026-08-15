import numpy as np
from scipy.stats import pearsonr


def compute_reliability(model_runs: list[float]) -> float:
    scores = np.array(model_runs)
    if np.mean(scores) == 0:
        return 0.0
    cv_squared = np.var(scores, ddof=0) / (np.mean(scores) ** 2)
    return 1.0 / (1.0 + cv_squared)


def compute_construct_isolation(
    target_scores: list[float],
    target_proxy_vals: list[float],
    confound_vals: list[float],
) -> float:
    corr_target, _ = pearsonr(target_scores, target_proxy_vals)
    corr_confound, _ = pearsonr(target_scores, confound_vals)
    if corr_confound == 0 or np.isnan(corr_confound):
        return 1.0
    return min(1.0, abs(corr_target) / abs(corr_confound))


def ood_ratio(acc_ood: float, acc_id: float) -> float:
    if acc_id == 0:
        return 0.0
    return acc_ood / acc_id

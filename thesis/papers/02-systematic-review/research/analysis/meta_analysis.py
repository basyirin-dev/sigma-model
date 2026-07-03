import numpy as np
from scipy import stats
from typing import Optional


def meta_fixed(effects: np.ndarray, variances: np.ndarray) -> dict:
    w = 1.0 / variances
    est = np.sum(w * effects) / np.sum(w)
    se = np.sqrt(1.0 / np.sum(w))
    z = est / se
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    q = float(np.sum(w * (effects - est) ** 2))
    df = len(effects) - 1
    i2 = max(0.0, (q - df) / q * 100) if q > 0 else 0.0
    return {
        "est": est, "se": se,
        "ci_lower": est - 1.96 * se, "ci_upper": est + 1.96 * se,
        "z": z, "p": p, "Q": q, "I2": i2, "df": df,
    }


def meta_random(effects: np.ndarray, variances: np.ndarray) -> dict:
    w = 1.0 / variances
    est_fe = np.sum(w * effects) / np.sum(w)
    q = float(np.sum(w * (effects - est_fe) ** 2))
    df = len(effects) - 1
    c = np.sum(w) - np.sum(w**2) / np.sum(w)
    tau2 = max(0.0, (q - df) / c)
    v_star = variances + tau2
    w_star = 1.0 / v_star
    est = np.sum(w_star * effects) / np.sum(w_star)
    se = np.sqrt(1.0 / np.sum(w_star))
    z = est / se
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    mean_v = float(np.mean(variances))
    i2 = tau2 / (tau2 + mean_v) * 100 if (tau2 + mean_v) > 0 else 0.0
    return {
        "est": est, "se": se,
        "ci_lower": est - 1.96 * se, "ci_upper": est + 1.96 * se,
        "z": z, "p": p, "Q": q, "I2": i2, "tau2": tau2, "df": df,
    }

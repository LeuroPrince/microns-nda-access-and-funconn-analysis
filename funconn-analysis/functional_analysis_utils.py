from __future__ import annotations

from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


SESSION = 7
SCAN_IDX = 4
RUN_DATE = "2026-05-03"


def find_workspace(start: Path | None = None) -> Path:
    """Find the nearest workspace that contains outputs_v1_col_7_4."""
    start = Path.cwd() if start is None else Path(start).resolve()
    candidates = [start, *start.parents]
    module_parent = Path(__file__).resolve().parent.parent
    candidates.extend([module_parent, *module_parent.parents])
    for candidate in candidates:
        if (candidate / "outputs_v1_col_7_4").exists():
            return candidate
    raise FileNotFoundError("Could not find outputs_v1_col_7_4 from the current workspace or module path.")


def functional_paths(start: Path | None = None, run_date: str = RUN_DATE) -> dict[str, Path]:
    """Return the standard functional-analysis output directories."""
    workspace = find_workspace(start)
    outdir = workspace / "outputs_v1_col_7_4"
    functional_base = outdir / "functional_correlation" / run_date
    paths = {
        "workspace": workspace,
        "outdir": outdir,
        "functional_base": functional_base,
        "example": functional_base / "example",
        "correlation": functional_base / "correlation",
        "coupling_eigen": functional_base / "coupling-eigen",
        "layer_annotation": functional_base / "layer_annotation",
    }
    for key in ["example", "correlation", "coupling_eigen", "layer_annotation"]:
        paths[key].mkdir(parents=True, exist_ok=True)
    return paths


def require_file(path: Path) -> Path:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Required input file not found: {path}")
    return path


def read_matrix_csv(path: Path, as_int_labels: bool = True) -> pd.DataFrame:
    """Read a square matrix CSV with row labels in the first column."""
    df = pd.read_csv(require_file(path), index_col=0)
    if as_int_labels:
        df.index = df.index.astype(int)
        df.columns = df.columns.astype(int)
    return df


def save_matrix(df: pd.DataFrame, csv_path: Path) -> None:
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(csv_path)


def validate_square_matrix(matrix: np.ndarray, label: str) -> np.ndarray:
    matrix = np.asarray(matrix, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError(f"{label} must be a square matrix, got shape {matrix.shape}.")
    if not np.isfinite(matrix).all():
        raise ValueError(f"{label} contains non-finite values.")
    return matrix


def matrix_abs_limit(matrix: np.ndarray, percentile: float = 99.0, fallback: float = 1.0) -> float:
    matrix = np.asarray(matrix, dtype=float)
    limit = np.nanpercentile(np.abs(matrix), percentile)
    if not np.isfinite(limit) or limit <= 0:
        limit = np.nanmax(np.abs(matrix))
    if not np.isfinite(limit) or limit <= 0:
        limit = fallback
    return float(limit)


def eigenspectrum_desc(matrix: np.ndarray) -> np.ndarray:
    matrix = validate_square_matrix(matrix, "matrix")
    return np.sort(np.linalg.eigvalsh(matrix))[::-1]


def fit_power_law_positive(eigenvalues: np.ndarray, num_top_eigenvalues: int = 100) -> dict[str, np.ndarray | float] | None:
    evals = np.sort(np.asarray(eigenvalues, dtype=float))[::-1]
    positive_positions = np.flatnonzero(evals > 0)
    n_fit = min(num_top_eigenvalues, len(positive_positions))
    if n_fit < 2:
        return None
    fit_positions = positive_positions[:n_fit]
    top_evals = evals[fit_positions]
    normalized_ranks = (fit_positions + 1) / len(evals)
    log_x = np.log(normalized_ranks)
    log_y = np.log(top_evals)
    slope, intercept = np.polyfit(log_x, log_y, 1)
    fitted_y = np.exp(slope * log_x + intercept)
    r_squared = np.corrcoef(log_x, log_y)[0, 1] ** 2
    return {
        "slope": float(slope),
        "intercept": float(intercept),
        "exponent": float(-slope),
        "r_squared": float(r_squared),
        "data_x": normalized_ranks,
        "data_y": top_evals,
        "fitted_y": fitted_y,
    }


def save_eigenspectrum_csv(eigenvalues: np.ndarray, output_path: Path, value_column: str = "eigenvalue") -> pd.DataFrame:
    eigenvalues = np.asarray(eigenvalues, dtype=float)
    ranks = np.arange(1, len(eigenvalues) + 1)
    df = pd.DataFrame(
        {
            "rank": ranks,
            "rank_normalized": ranks / len(eigenvalues),
            value_column: eigenvalues,
        }
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print("Saved:", output_path)
    return df


def sorted_diagonal_spectrum(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    matrix = validate_square_matrix(matrix, "matrix")
    diagonal = np.sort(np.diag(matrix))[::-1]
    ranks = (np.arange(len(diagonal)) + 1) / len(diagonal)
    return ranks, diagonal


def get_subsampled_eigenspectrum(matrix: np.ndarray, k_fraction: float, n_iter: int = 50, seed: int | None = None):
    """Randomly subsample K = round(N * k_fraction) neurons and average eigenspectrums."""
    matrix = validate_square_matrix(matrix, "matrix")
    N = matrix.shape[0]
    K = int(np.round(N * k_fraction))
    if K < 2:
        raise ValueError("Subsample size K must be at least 2.")
    rng = np.random.default_rng(seed)
    all_evals = []
    for _ in range(n_iter):
        inds = rng.choice(N, K, replace=False)
        submatrix = matrix[np.ix_(inds, inds)]
        evals = np.linalg.eigvalsh(submatrix)
        all_evals.append(np.sort(evals)[::-1])
    all_evals = np.asarray(all_evals)
    return all_evals.mean(axis=0), all_evals.std(axis=0), all_evals


def plot_positive_eigenvalues(axis, eigenvalues: np.ndarray, label: str, color: str, linewidth: float = 1.5):
    eigenvalues = np.asarray(eigenvalues, dtype=float)
    ranks = (np.arange(len(eigenvalues)) + 1) / len(eigenvalues)
    positive = np.isfinite(eigenvalues) & (eigenvalues > 0)
    axis.loglog(ranks[positive], eigenvalues[positive], color=color, linewidth=linewidth, label=label)


def plot_power_law_fit(axis, fit: dict[str, np.ndarray | float] | None, label_prefix: str, color: str, linewidth: float = 1.2):
    if fit is None:
        return
    axis.loglog(
        fit["data_x"],
        fit["fitted_y"],
        "--",
        color=color,
        linewidth=linewidth,
        label="{} alpha={:.2f}, R2={:.2f}".format(label_prefix, fit["exponent"], fit["r_squared"]),
    )


def plot_subsampled_eigenspectrum(
    axis,
    matrix: np.ndarray,
    title: str,
    k_fractions: Iterable[float],
    n_iter: int = 50,
    seed: int = 43,
    original_label: str | None = None,
) -> pd.DataFrame:
    matrix = validate_square_matrix(matrix, title)
    original_evals = eigenspectrum_desc(matrix)
    original_ranks = (np.arange(len(original_evals)) + 1) / len(original_evals)
    original_positive = np.isfinite(original_evals) & (original_evals > 0)
    axis.loglog(
        original_ranks[original_positive],
        original_evals[original_positive],
        color="black",
        linewidth=1.6,
        label=original_label or "Original N={}".format(matrix.shape[0]),
    )

    k_fractions = list(k_fractions)
    colors_sub = plt.cm.viridis(np.linspace(0, 0.82, len(k_fractions)))
    summary_rows = []
    for idx, k_fraction in enumerate(k_fractions):
        mean_evals, std_evals, _ = get_subsampled_eigenspectrum(
            matrix,
            k_fraction=k_fraction,
            n_iter=n_iter,
            seed=seed + idx,
        )
        K = len(mean_evals)
        ranks = (np.arange(K) + 1) / K
        upper = mean_evals + std_evals
        lower = mean_evals - std_evals
        positive = (
            np.isfinite(mean_evals)
            & (mean_evals > 0)
            & np.isfinite(upper)
            & (upper > 0)
        )
        if positive.any():
            safe_lower = np.maximum(lower[positive], np.finfo(float).tiny)
            axis.loglog(
                ranks[positive],
                mean_evals[positive],
                color=colors_sub[idx],
                linewidth=1.4,
                label="k={:.3g}, K={}".format(k_fraction, K),
            )
            axis.fill_between(
                ranks[positive],
                safe_lower,
                upper[positive],
                color=colors_sub[idx],
                alpha=0.18,
                linewidth=0,
            )
        for rank_idx, eigenvalue in enumerate(mean_evals, start=1):
            summary_rows.append(
                {
                    "k_fraction": k_fraction,
                    "K": K,
                    "rank": rank_idx,
                    "rank_normalized": rank_idx / K,
                    "mean_eigenvalue": eigenvalue,
                    "std_eigenvalue": std_evals[rank_idx - 1],
                }
            )

    axis.set_title(title)
    axis.set_xlabel("Rank (r/K)")
    axis.set_ylabel("Eigenvalue")
    axis.grid(True, which="both", linestyle="--", linewidth=0.5)
    axis.legend(frameon=False, fontsize=6)
    return pd.DataFrame(summary_rows)


def eigenspectrum_summary(label: str, evals: np.ndarray, fit: dict[str, np.ndarray | float] | None) -> dict[str, float | str | int]:
    evals = np.asarray(evals, dtype=float)
    total = float(np.sum(evals))
    squared = float(np.sum(evals**2))
    participation_ratio = total**2 / squared if squared > 0 else np.nan
    return {
        "spectrum": label,
        "N": len(evals),
        "trace": total,
        "mean_eigenvalue": total / len(evals),
        "alpha": np.nan if fit is None else fit["exponent"],
        "r_squared": np.nan if fit is None else fit["r_squared"],
        "top1_fraction": evals[:1].sum() / total,
        "top5_fraction": evals[: min(5, len(evals))].sum() / total,
        "top10_fraction": evals[: min(10, len(evals))].sum() / total,
        "participation_ratio": participation_ratio,
        "participation_ratio_over_N": participation_ratio / len(evals),
    }

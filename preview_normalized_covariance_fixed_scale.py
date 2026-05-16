from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


BASE_DIR = Path("outputs_v1_col_7_4/functional_correlation/2026-05-03/correlation")
MATRIX_CSV = BASE_DIR / "V1_col_7_4_activity_normalized_covariance_matrix_allen_layer_sorted.csv"
if not MATRIX_CSV.exists():
    MATRIX_CSV = BASE_DIR / "V1_col_7_4_activity_normalized_covariance_matrix.csv"

OUT_PNG = BASE_DIR / "V1_col_7_4_activity_normalized_covariance_heatmap_fixed_minus1_1_test.png"


def main():
    cov_df = pd.read_csv(MATRIX_CSV, index_col=0)
    cov = cov_df.to_numpy(dtype=float)

    diag = np.diag(cov)
    offdiag = cov[~np.eye(cov.shape[0], dtype=bool)]

    sns.set_theme(style="white", context="notebook")
    fig, ax = plt.subplots(figsize=(8, 7), dpi=150)
    sns.heatmap(
        cov_df,
        cmap="vlag",
        center=0,
        vmin=-1,
        vmax=1,
        xticklabels=False,
        yticklabels=False,
        square=True,
        cbar_kws={"label": "Normalized activity covariance, fixed scale [-1, 1]"},
        ax=ax,
    )
    ax.set_title("V1_col_7_4 Normalized Activity Covariance, fixed scale [-1, 1]")
    ax.set_xlabel("unit_id")
    ax.set_ylabel("unit_id")
    fig.tight_layout()
    fig.savefig(OUT_PNG, bbox_inches="tight")
    plt.close(fig)

    print(f"Read matrix: {MATRIX_CSV}")
    print(f"Saved preview: {OUT_PNG}")
    print(f"Shape: {cov.shape}")
    print(f"Tr(C) / N: {np.trace(cov) / cov.shape[0]:.6f}")
    print(
        "Diagonal min/median/mean/max: "
        f"{np.nanmin(diag):.6f}, {np.nanmedian(diag):.6f}, "
        f"{np.nanmean(diag):.6f}, {np.nanmax(diag):.6f}"
    )
    print(
        "Off-diagonal min/median/mean/max: "
        f"{np.nanmin(offdiag):.6f}, {np.nanmedian(offdiag):.6f}, "
        f"{np.nanmean(offdiag):.6f}, {np.nanmax(offdiag):.6f}"
    )
    print(f"Off-diagonal fraction within [-0.1, 0.1]: {np.mean((offdiag >= -0.1) & (offdiag <= 0.1)):.6f}")


if __name__ == "__main__":
    main()

# Project Context For Codex

This file is the compact entry point for future model sessions. Read it before scanning notebooks or generated outputs.

## Purpose

This repository is based on `microns-nda-access` and is being used to analyze MICrONS V1 functional and structural data for session `7`, scan `4`, dataset label `V1_col_7_4`.

The current analysis focuses on a matched set of 126 functional units with `unit_id` and CAVE `pt_root_id` mappings. The main scientific outputs are functional activity correlation/covariance matrices, structural synapse/coupling matrices, coupling-derived correlations, Allen layer annotations, and eigenspectrum comparisons.

## How To Orient Quickly

Start with these files:

- `PROJECT_CONTEXT_FOR_CODEX.md`: this compact overview.
- `README.md`: original database/Docker/DataJoint setup instructions.
- `outputs_v1_col_7_4/README.md`: detailed inventory of generated outputs.
- `funconn-analysis/functional_correlation_analysis_V1_col_7_4.ipynb`: active functional analysis notebook.
- `funconn-analysis/structural_correlation_analysis_V1_col_7_4.ipynb`: structural coupling notebook.
- `preview_normalized_covariance_fixed_scale.py`: small helper script for plotting normalized covariance with fixed scale `[-1, 1]`.

Avoid reading generated matrices, `.npy` files, figures, executed tutorial notebooks, or notebook output transcripts unless the user specifically asks.

## Environment

The repo is designed for the MICrONS NDA/DataJoint Docker workflow.

Important local files:

- `.env`: local DataJoint/Docker configuration and possible credentials. Do not read or include in model context.
- `docker-compose.yml`, `Dockerfile`: container setup.
- `README.md`: records default database setup and access workflow.

Typical notebook path inside the container is `/notebooks/workspace`; some saved outputs may show `/notebooks/outputs_v1_col_7_4` depending on when the notebook was run.

## Project Structure

```text
.
├── README.md
├── Dockerfile
├── docker-compose.yml
├── preview_normalized_covariance_fixed_scale.py
├── funconn-analysis/
│   ├── functional_correlation_analysis_V1_col_7_4.ipynb
│   ├── structural_correlation_analysis_V1_col_7_4.ipynb
│   ├── VSCode_Docker_Workflow_cd.md
│   ├── cache/
│   │   ├── df_coreg_ext_sorted.csv
│   │   └── df_max_num_scan.csv
│   └── structural-coupling-alignment/
│       ├── functional_data_access_and_analysis.py
│       └── subsampling.py
├── outputs_v1_col_7_4/
│   ├── README.md
│   ├── functional_correlation/2026-05-03/
│   └── structural_coupling/2026-05-03/
└── tutorial/
```

## Main Notebooks

### Functional Analysis

`funconn-analysis/functional_correlation_analysis_V1_col_7_4.ipynb`

Main responsibilities:

- Select session `7`, scan `4` units.
- Use functional traces from `nda.Activity.trace`.
- Save the 126-unit mapping to `outputs_v1_col_7_4/functional_correlation/2026-05-03/correlation/V1_col_7_4_units_used.csv`.
- Compute Pearson activity correlation.
- Compute activity covariance and normalized activity covariance.
- Save sorted versions using Allen layer annotations.
- Compute eigenspectrums and subsampled eigenspectrum summaries.
- Compare full normalized covariance with the Allen slanted L2/3 subset.

Recent additions in this notebook include normalized covariance, fixed-scale heatmaps, Allen layer sorting, layer annotation summaries, and L2/3 normalized covariance eigenspectrum comparison.

### Structural Analysis

`funconn-analysis/structural_correlation_analysis_V1_col_7_4.ipynb`

Main responsibilities:

- Read `V1_col_7_4_units_used.csv` from the functional analysis to preserve neuron order.
- Fetch or load internal synapses among the same 126 `pt_root_id`s.
- Construct `W_syn`, where rows are postsynaptic units and columns are presynaptic units.
- Remove self-connections.
- Save raw and incoming-normalized synapse weight matrices.
- Compute structural coupling matrix from incoming-normalized `W_syn` via trace-normalized `W_norm.T @ W_norm`.
- Compute coupling-derived correlation and eigenspectrums.

## Output Directories

Base output directory:

```text
outputs_v1_col_7_4/
```

Current run date:

```text
2026-05-03
```

Functional outputs:

```text
outputs_v1_col_7_4/functional_correlation/2026-05-03/
├── example/
├── correlation/
├── coupling-eigen/
└── layer_annotation/
```

Structural outputs:

```text
outputs_v1_col_7_4/structural_coupling/2026-05-03/
├── correlation/
├── coupling-eigen/
└── legacy_failed_cache/
```

`legacy_failed_cache/` is old provenance from a failed all-incoming-synapse query path and is not used by the current notebooks.

## Key Data Files

High-signal CSVs worth reading when needed:

- `outputs_v1_col_7_4/functional_correlation/2026-05-03/correlation/V1_col_7_4_units_used.csv`: 126 functional units, including `session`, `scan_idx`, `unit_id`, `pt_root_id`, positions, and matching metadata.
- `outputs_v1_col_7_4/functional_correlation/2026-05-03/correlation/V1_col_7_4_activity_nonzero_mean_scaling_summary.csv`: per-unit scaling factors used before normalized covariance.
- `outputs_v1_col_7_4/functional_correlation/2026-05-03/layer_annotation/V1_col_7_4_layer_annotation_summary.csv`: compact counts/fractions for V1 area and Allen slanted layer/cell-type labels.
- `outputs_v1_col_7_4/functional_correlation/2026-05-03/layer_annotation/V1_col_7_4_root_id_layer_annotations.csv`: per-root layer annotation table.
- `outputs_v1_col_7_4/functional_correlation/2026-05-03/coupling-eigen/V1_col_7_4_activity_normalized_covariance_L23_vs_full_eigenspectrum_summary.csv`: full vs L2/3 eigenspectrum summary.

Generated matrices and plots are documented but should not be loaded by default:

- `*_matrix.csv`, `*_matrix.npy`
- `*_heatmap.png`
- `*_eigenspectrum.png`
- `*_subsampled_eigenspectrum.csv` unless the user asks about the spectrum values.

## Functional Matrix Definitions

- Activity correlation: Pearson correlation of `nda.Activity.trace` signals for the 126 selected units.
- Activity covariance: covariance of activity traces after the notebook's preprocessing.
- Normalized activity covariance: covariance after scaling each unit by the nonzero-frame mean; the summary file records `nonzero_frame_fraction`, `nonzero_mean_before_scaling`, `scale_factor`, and `nonzero_mean_after_scaling`.
- Functional network off-diagonal matrix: empirical Pearson correlation matrix with diagonal set to 0.
- Functional coupling correlation: trace-normalized `W_func.T @ W_func` from the empirical functional network matrix. It is not a structural model output.

## Structural Matrix Definitions

- `W_syn`: internal synapse count/weight matrix among the same 126 units; row = post, column = pre.
- Incoming-normalized `W_syn`: each postsynaptic row is normalized to sum to 1 when it has internal incoming synapses.
- Structural coupling matrix: trace-normalized `W_norm.T @ W_norm`.
- Coupling-derived correlation: model correlation generated from the structural coupling matrix.

## Layer Annotation Context

The layer annotation outputs indicate all 126 units are in V1 by `nucleus_functional_area_assignment`.

Allen slanted layer/cell-type summary currently includes:

- `23P`: 60 units, fraction about `0.476`.
- `4P`: 35 units, fraction about `0.278`.
- `5P-PT`: 15 units, fraction about `0.119`.

The L2/3 eigenspectrum comparison uses the 60 Allen slanted `L2/3` / `23P` units from the normalized covariance matrix.

The latest visible L2/3 summary from the notebook output:

- Full normalized covariance: `N = 126`, trace about `126`, trace per neuron about `1.0`, fitted alpha about `0.468735`.
- L2/3 normalized covariance: `N = 60`, trace about `69.246746`, trace per neuron about `1.154112`, fitted alpha about `0.531700`.

## Token-Saving Rules For Future Sessions

1. Read this file first.
2. Then read `outputs_v1_col_7_4/README.md` if output inventory matters.
3. Read only the specific notebook being edited.
4. Prefer reading notebook source around relevant markdown headings or code cells instead of loading the whole `.ipynb`.
5. Do not read `.env`, logs, `.git`, generated `.npy`, image files, or large matrix CSVs unless explicitly requested.
6. If a user asks about data values, start with the small summary CSVs listed above.

## Maintenance Rule

Keep this file synchronized with the project. Any change that affects a future model's understanding should update this document in the same commit or work session.

Update this file when any of these change:

- Main analysis notebooks are added, renamed, deleted, or reorganized.
- The selected dataset/session/scan, unit count, unit identity, or `pt_root_id` mapping changes.
- Output directories, run dates, or file naming conventions change.
- Matrix definitions, normalization formulas, preprocessing steps, or eigenspectrum methods change.
- New high-signal summary CSVs are created, or old ones stop being authoritative.
- Important interpretation changes, such as layer counts, L2/3 subset size, fitted alpha values, or structural/functional matrix definitions.
- `.codexignore` changes in a way that hides or exposes important context.

Before ending a model-assisted coding session, check:

- Does `PROJECT_CONTEXT_FOR_CODEX.md` still describe the active notebooks and outputs?
- Are new generated files documented in `outputs_v1_col_7_4/README.md` or summarized here?
- Are large or sensitive files still excluded by `.codexignore`?
- Can a future model answer "what is this project doing?" by reading this file plus the output README?

## Current Ignore Policy

`.codexignore` intentionally hides:

- Local credentials/config such as `.env`.
- Logs and runtime caches.
- `.git` internals.
- Python/Jupyter caches.
- Generated `.npy` and image outputs.
- Executed/tutorial notebooks and large notebook output transcripts.
- Large generated matrices and pairwise tables.

It keeps compact context files and small metadata/summary CSVs available so the model can understand the project without rereading the full analysis history.

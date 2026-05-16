# V1_col_7_4 Outputs

This folder is organized by analysis type, run date, and output role.

## functional_correlation/2026-05-03/example

Presentation/example figures derived from `example.ipynb`:

- `V1_col_7_4_activity_trace_heatmap.png`: heatmap of the 126 `nda.Activity.trace` signals after row-wise z-scoring and time binning.
- `V1_col_7_4_activity_trace_raw_heatmap.png`: heatmap of the same 126 `nda.Activity.trace` signals after time binning only, without row-wise z-scoring.
- `V1_col_7_4_single_unit_activity_trace_example.png`: one example neuron's `nda.Activity.trace`.
- `V1_col_7_4_calcium_activity_trace_heatmap.png`: older presentation heatmap kept for provenance.

## functional_correlation/2026-05-03/correlation

Empirical functional correlation outputs from `nda.Activity.trace`:

- `V1_col_7_4_units_used.csv`: the 126 functional units and their matched `pt_root_id`.
- `V1_col_7_4_activity_correlation_matrix.csv/.npy`: Pearson activity correlation matrix.
- `V1_col_7_4_activity_correlation_matrix_rerun.csv/.npy`: later rerun of the same activity correlation matrix with a shorter filename.
- `V1_col_7_4_pairwise_activity_correlations.csv`: upper-triangle long table of pairwise Pearson correlations.
- `V1_col_7_4_activity_correlation_heatmap.png`: empirical correlation heatmap.
- `V1_col_7_4_activity_correlation_distribution.png`: pairwise correlation distribution.

## functional_correlation/2026-05-03/coupling-eigen

Functional coupling correlation and eigenspectrum outputs derived directly from the empirical activity correlation matrix:

- `V1_col_7_4_functional_network_offdiag_matrix.csv/.npy`: empirical Pearson correlation matrix with the diagonal set to 0.
- `V1_col_7_4_functional_coupling_correlation_matrix.csv/.npy`: trace-normalized `W_func.T @ W_func`; this is not a coupling-derived/model-generated correlation matrix.
- `V1_col_7_4_functional_coupling_correlation_heatmap.png`: heatmap of the functional coupling correlation matrix.
- `V1_col_7_4_activity_correlation_eigenspectrum.csv/.png`: eigenspectrum of the empirical activity correlation matrix.
- `V1_col_7_4_functional_coupling_correlation_eigenspectrum.csv`: eigenspectrum of the functional coupling correlation matrix.
- `V1_col_7_4_activity_correlation_subsampled_eigenspectrum.csv`: subsampled eigenspectrum summary for the empirical activity correlation matrix.
- `V1_col_7_4_functional_coupling_correlation_subsampled_eigenspectrum.csv`: subsampled eigenspectrum summary for the functional coupling correlation matrix.
- `V1_col_7_4_functional_subsampled_eigenspectrums.png`: original and subsampled functional eigenspectrums at multiple `k_fraction` values.
- `V1_col_7_4_functional_correlation_and_coupling_eigenspectrums.png`: overlay comparing empirical correlation and functional coupling correlation eigenspectrums.

## structural_coupling/2026-05-03/correlation

Structural synapse/connectivity outputs:

- `V1_col_7_4_internal_synapses.csv`: internal synapses among the 126 matched neurons after removing self-connections.
- `V1_col_7_4_synapse_weight_matrix_root_ids.csv`: `W_syn`, row = post root id, column = pre root id.
- `V1_col_7_4_synapse_weight_matrix_unit_ids.csv`: `W_syn`, row = post unit id, column = pre unit id.
- `V1_col_7_4_synapse_weight_matrix.npy`: numpy copy of `W_syn`.
- `V1_col_7_4_synapse_weight_matrix_heatmap.png`: LogNorm heatmap of raw `W_syn`.
- `V1_col_7_4_synapse_weight_matrix_incoming_norm_unit_ids.csv`: row-normalized `W_syn`; each `post_unit_id` row sums to 1 when it has internal incoming synapses.
- `V1_col_7_4_synapse_weight_matrix_incoming_norm.npy`: numpy copy of the incoming-normalized matrix.
- `V1_col_7_4_synapse_weight_matrix_incoming_norm_heatmap.png`: LogNorm heatmap of the incoming-normalized matrix.

## structural_coupling/2026-05-03/coupling-eigen

Structural coupling, coupling-derived correlation, and eigenspectrum outputs:

- `V1_col_7_4_coupling_matrix_incoming_norm.csv/.npy`: trace-normalized `W_norm.T @ W_norm`, where `W_norm` is incoming-normalized by `post_unit_id`.
- `V1_col_7_4_coupling_derived_correlation_matrix_incoming_norm.csv/.npy`: model correlation generated from the incoming-normalized coupling matrix.
- `V1_col_7_4_coupling_matrix_incoming_norm_heatmap.png`: LogNorm heatmap of the incoming-normalized structural coupling matrix.
- `V1_col_7_4_coupling_derived_correlation_heatmap_incoming_norm.png`: heatmap of the incoming-normalized coupling-derived correlation matrix.
- `V1_col_7_4_coupling_derived_correlation_eigenspectrum_incoming_norm.csv`: eigenspectrum of the incoming-normalized coupling-derived correlation matrix.
- `V1_col_7_4_coupling_matrix_eigenspectrum_incoming_norm.csv`: eigenspectrum of the incoming-normalized coupling matrix.
- `V1_col_7_4_coupling_eigenspectrums_incoming_norm.png`: eigenspectrum plot for incoming-normalized structural coupling.
- Files without `_incoming_norm` are older raw-coupling outputs kept for provenance.

## structural_coupling/2026-05-03/legacy_failed_cache

Contains the old 1-byte `synapses_in_by_post_root` cache produced by the earlier failed all-incoming-synapse query path. It is kept only as provenance and is not used by the current notebook.

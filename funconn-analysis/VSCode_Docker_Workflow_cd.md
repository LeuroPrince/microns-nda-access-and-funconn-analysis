# MICrONS NDA VS Code Docker Workflow cd

This is a compact handoff note for future Codex sessions. The user's current
goal is to analyze MICrONS in vivo functional data using the Docker environment,
while keeping notebooks and results visible on the local Windows host.

## Current Intent

Focus only on in vivo functional data. Do not shift to digital twin data unless
the user explicitly asks.

Scientific goal:

1. Use the user's target neurons and scan IDs.
2. Retrieve matched MICrONS functional data.
3. Convert neural responses into analyzable response matrices.
4. Compute meaningful functional correlation matrices and heatmaps.
5. Keep cross-layer, cross-area, and cross-stimulus comparisons scientifically
   valid by using comparable response features.

Use these current defaults:

```text
materialize.version = 1718
coregistration table = coregistration_manual_v4
```

Do not silently revert to tutorial defaults:

```text
version 661
coregistration_manual_v3
```

## Key Paths

Docker compose repo:

```text
D:\microns_nda_v8_cd\microns-nda-access
```

Local notebook workspace:

```text
D:\microns_nda_v8_cd\microns-nda-access\notebooks
```

Same workspace inside Docker:

```text
/notebooks/workspace
```

Earlier project workspace:

```text
D:\neuroscience\WenLab\Functional_data_access\microns-funconn-2025-1.1.0
```

Manual SQL ingest note:

```text
D:\neuroscience\WenLab\Functional_data_access\microns-funconn-2025-1.1.0\microns_nda_manual_sql_ingest_cd.md
```

## Completed Work

Local Docker images are present and have run successfully:

```text
microns-phase3-nda-database:latest
microns-phase3-nda-notebook:latest
```

The database image tar file was deleted only after explicit user confirmation.
Do not delete other large files, containers, images, or caches without asking.

The notebook image was built successfully after patching Debian buster apt
sources to archive repositories.

The CAVE token was saved inside the running notebook container in an earlier
session. Treat it as secret. Do not print or write it into files.

Tutorial outputs already produced:

```text
D:\microns_nda_v8_cd\microns-nda-access\notebooks\Using_DataJoint_to_Access_Functional_Data.executed.ipynb
D:\microns_nda_v8_cd\microns-nda-access\notebooks\Matched_Cell_Functional_Data_v1718_v4.ipynb
D:\microns_nda_v8_cd\microns-nda-access\notebooks\Matched_Cell_Functional_Data_v1718_v4.executed.ipynb
D:\microns_nda_v8_cd\microns-nda-access\notebooks\notebook_cell_outputs_v1718_v4_cd.md
```

Current analysis-related files:

```text
D:\microns_nda_v8_cd\microns-nda-access\notebooks\functional_data_access_and_analysis.py
D:\microns_nda_v8_cd\microns-nda-access\notebooks\session7_scan4_functional_correlation_analysis.ipynb
D:\microns_nda_v8_cd\microns-nda-access\notebooks\outputs_session7scan4_v1_column_126
D:\microns_nda_v8_cd\microns-nda-access\notebooks\cache
```

## Start In VS Code

From PowerShell:

```powershell
cd D:\microns_nda_v8_cd\microns-nda-access
docker compose start database notebook
code D:\microns_nda_v8_cd\microns-nda-access
```

In VS Code:

1. Run `Dev Containers: Reopen in Container`.
2. Open `/notebooks/workspace`.
3. Open one of these notebooks:

```text
Matched_Cell_Functional_Data_v1718_v4.ipynb
session7_scan4_functional_correlation_analysis.ipynb
```

4. Confirm the notebook kernel is the Docker Python:

```python
import sys
print(sys.executable)
```

Expected:

```text
/usr/local/bin/python
```

If the kernel path starts with `C:\`, it is using the wrong Python.

## Stop

When finished:

```powershell
cd D:\microns_nda_v8_cd\microns-nda-access
docker compose stop notebook database
```

Stopping containers reduces memory pressure and avoids unnecessary database
writable-layer growth.

## Safety Constraints

Disk safety matters. Docker previously caused severe D drive pressure.

Previously observed large storage items:

```text
microns-phase3-nda-database image: 208 GB unique
notebook image: 5 GB
database container writable layer: 70 GB
```

Before any large action, check D drive free space:

```powershell
Get-PSDrive -Name D | Select-Object Name, @{Name='FreeGB';Expression={[math]::Round($_.Free/1GB,2)}}
```

Ask before:

```text
docker compose down
docker system prune
docker builder prune
deleting containers
deleting images
deleting downloaded data
pulling or building large images
running long database-mutating operations
```

The user previously asked to stop and ask if D drive free space falls below
100 GB. Later work continued only after caution around 70 GB.

## Useful Checks

Check containers:

```powershell
cd D:\microns_nda_v8_cd\microns-nda-access
docker compose ps -a
```

Check Docker disk usage:

```powershell
docker system df -v
```

Check Python environment inside notebook container:

```powershell
cd D:\microns_nda_v8_cd\microns-nda-access
@'
import sys
import datajoint as dj
import caveclient
import numpy
import pandas

print("python", sys.executable)
print("datajoint", dj.__version__)
print("caveclient", caveclient.__version__)
print("numpy", numpy.__version__)
print("pandas", pandas.__version__)
'@ | docker compose exec -T notebook python -
```

Expected from successful runs:

```text
python /usr/local/bin/python
datajoint 0.12.9
caveclient 7.3.1
numpy 1.24.3
pandas 2.0.2
```

List mounted workspace from inside Docker:

```powershell
cd D:\microns_nda_v8_cd\microns-nda-access
docker compose exec -T notebook ls -lah /notebooks/workspace
```

## Tutorial Status

`Using_DataJoint_to_Access_Functional_Data.ipynb`:

```text
status: executed successfully
role: verifies local DataJoint functional database access
outputs: scans, fields, trials, movie data, pupil, treadmill, masks, traces,
stack registration, Neuroglancer links
```

`Matched_Cell_Functional_Data_v1718_v4.ipynb`:

```text
status: executed successfully
version: 1718
table: coregistration_manual_v4
role: verifies CAVE/coregistration query and matched functional cell access
```

Observed notes from the successful run:

```text
CAVE token-acquisition text appeared while execution continued.
A non-pandas CAVE query compatibility warning appeared while execution continued.
```

## Scientific Analysis Direction

Do not correlate arbitrary raw responses across unmatched visual stimuli.
Create a comparable representation first.

Definitions:

```text
signal correlation: similarity of stimulus-driven tuning or mean responses
noise correlation: shared trial-to-trial variability after condition means are removed
```

For cross-layer or cross-area comparisons, normalize within session/scan where
appropriate and compare matched feature spaces.

## Continuation Entry Points

Continue from these files:

```text
D:\microns_nda_v8_cd\microns-nda-access\notebooks\session7_scan4_functional_correlation_analysis.ipynb
D:\microns_nda_v8_cd\microns-nda-access\notebooks\functional_data_access_and_analysis.py
D:\microns_nda_v8_cd\microns-nda-access\notebooks\outputs_session7scan4_v1_column_126
```

Before large analysis, check disk space and container status.

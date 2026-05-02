# Notebook Cell Outputs

Generated from executed notebooks. Long text/html and image payloads are summarized; full outputs remain in the executed `.ipynb` files.

## Using_DataJoint_to_Access_Functional_Data.executed.ipynb

### Code cell 1 (notebook cell 3, execution_count=1)

**Source**
```python
import datajoint as dj
```

**Output**

_No output_

### Code cell 2 (notebook cell 6, execution_count=2)

**Source**
```python
from microns_phase3 import nda, utils
```

**Output**

Output 1 (stream):
```text
Connecting root@database:3306
```

### Code cell 3 (notebook cell 9, execution_count=3)

**Source**
```python
dj.ERD(nda) # View schema ERD
```

**Output**

Output 1 (execute_result):
```text
<datajoint.diagram.Diagram at 0x7879e07eb220>
```

### Code cell 4 (notebook cell 14, execution_count=4)

**Source**
```python
nda.Scan()
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    nframes     nfields     fps       
+---------+ +----------+ +---------+ +---------+ +--------+
4           7            40000       8           6.3009    
4           9            35112       8           6.3009    
4           10           40000       8           6.3009    
5           3            40000       8           6.3009    
5           6            40000       8           6.3009    
5           7            40000       8           6.3009    
6           2            40000       8           6.3009    
6           4            40000       8           6.3009    
6           6            40000       8           6.3009    
6           7            40000       8           6.3009    
7           3            40000       8           6.3009    
7           4            40000       8           6.3009    
   ...
 (Total: 19)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } Information on completed scan session Session ID scan_idx Scan ID nframes number of frames per scan nfields number of fields per scan fps frames per second (Hz) 4 7 40000 8 6.3009 4 9 35112 8 6.3009 4 10 40000 8 6.3009 5 3 40000 8 6.3009 5 6 40000 8 6.3009 5 7 40000 8 6.3009 6 2 40000 8 6.3009 6 4 40000 8 6.3009 6 6 40000 8 6.3009 6 7 40000 8 6.3009 7 3 40000 8 6.3009 7 4 40000 8 6.3009 ... Total: 19
```

### Code cell 5 (notebook cell 17, execution_count=5)

**Source**
```python
[*nda.Scan.heading.primary_key] # primary keys
```

**Output**

Output 1 (execute_result):
```text
['session', 'scan_idx']
```

### Code cell 6 (notebook cell 20, execution_count=6)

**Source**
```python
scan_key = {'session': 4, 'scan_idx': 7}
```

**Output**

_No output_

### Code cell 7 (notebook cell 21, execution_count=7)

**Source**
```python
nda.Scan & scan_key
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    nframes     nfields     fps       
+---------+ +----------+ +---------+ +---------+ +--------+
4           7            40000       8           6.3009    
 (Total: 1)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } Information on completed scan session Session ID scan_idx Scan ID nframes number of frames per scan nfields number of fields per scan fps frames per second (Hz) 4 7 40000 8 6.3009 Total: 1
```

### Code cell 8 (notebook cell 24, execution_count=8)

**Source**
```python
scan_keys = [{'session': 4, 'scan_idx': 7}, {'session': 5, 'scan_idx': 3}]
```

**Output**

_No output_

### Code cell 9 (notebook cell 25, execution_count=9)

**Source**
```python
nda.Scan & scan_keys
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    nframes     nfields     fps       
+---------+ +----------+ +---------+ +---------+ +--------+
4           7            40000       8           6.3009    
5           3            40000       8           6.3009    
 (Total: 2)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } Information on completed scan session Session ID scan_idx Scan ID nframes number of frames per scan nfields number of fields per scan fps frames per second (Hz) 4 7 40000 8 6.3009 5 3 40000 8 6.3009 Total: 2
```

### Code cell 10 (notebook cell 28, execution_count=10)

**Source**
```python
nframes, nfields = (nda.Scan & scan_key).fetch1('nframes', 'nfields')
print(f'number of frames in this scan: {nframes}, number of imaging fields in this scan: {nfields}')
```

**Output**

Output 1 (stream):
```text
number of frames in this scan: 40000, number of imaging fields in this scan: 8
```

### Code cell 11 (notebook cell 31, execution_count=11)

**Source**
```python
nframes, nfields = (nda.Scan & scan_keys).fetch('nframes', 'nfields')
print(f'number of frames in these scans: {nframes}, number of fields in these scans: {nfields}')
```

**Output**

Output 1 (stream):
```text
number of frames in these scans: [40000 40000], number of fields in these scans: [8 8]
```

### Code cell 12 (notebook cell 34, execution_count=12)

**Source**
```python
nda.Scan.fetch('KEY')
```

**Output**

Output 1 (execute_result):
```text
[{'session': 4, 'scan_idx': 7},
 {'session': 4, 'scan_idx': 9},
 {'session': 4, 'scan_idx': 10},
 {'session': 5, 'scan_idx': 3},
 {'session': 5, 'scan_idx': 6},
 {'session': 5, 'scan_idx': 7},
 {'session': 6, 'scan_idx': 2},
 {'session': 6, 'scan_idx': 4},
 {'session': 6, 'scan_idx': 6},
 {'session': 6, 'scan_idx': 7},
 {'session': 7, 'scan_idx': 3},
 {'session': 7, 'scan_idx': 4},
 {'session': 7, 'scan_idx': 5},
 {'session': 8, 'scan_idx': 5},
 {'session': 8, 'scan_idx': 7},
 {'session': 8, 'scan_idx': 9},
 {'session': 9, 'scan_idx': 3},
 {'session': 9, 'scan_idx': 4},
 {'session': 9, 'scan_idx': 6}]
```

### Code cell 13 (notebook cell 36, execution_count=13)

**Source**
```python
(nda.Scan & scan_key).fetch1('KEY')
```

**Output**

Output 1 (execute_result):
```text
{'session': 4, 'scan_idx': 7}
```

### Code cell 14 (notebook cell 39, execution_count=14)

**Source**
```python
nda.Scan & nda.ScanInclude
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    nframes     nfields     fps        
+---------+ +----------+ +---------+ +---------+ +---------+
4           7            40000       8           6.3009     
5           6            40000       8           6.3009     
5           7            40000       8           6.3009     
6           2            40000       8           6.3009     
6           4            40000       8           6.3009     
6           6            40000       8           6.3009     
6           7            40000       8           6.3009     
7           3            40000       8           6.3009     
7           4            40000       8           6.3009     
7           5            40000       8           6.3009     
8           5            40000       8           6.3009     
9           3            50000       6           8.61754    
   ...
 (Total: 14)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } Information on completed scan session Session ID scan_idx Scan ID nframes number of frames per scan nfields number of fields per scan fps frames per second (Hz) 4 7 40000 8 6.3009 5 6 40000 8 6.3009 5 7 40000 8 6.3009 6 2 40000 8 6.3009 6 4 40000 8 6.3009 6 6 40000 8 6.3009 6 7 40000 8 6.3009 7 3 40000 8 6.3009 7 4 40000 8 6.3009 7 5 40000 8 6.3009 8 5 40000 8 6.3009 9 3 50000 6 8.61754 ... Total: 14
```

### Code cell 15 (notebook cell 42, execution_count=15)

**Source**
```python
nda.Field & scan_key
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    *field    px_width     px_height     um_width     um_height     field_x     field_y     field_z    
+---------+ +----------+ +-------+ +----------+ +-----------+ +----------+ +-----------+ +---------+ +---------+ +---------+
4           7            1         248          440           620.0        1100.0        -485.0      -235.0      80.0       
4           7            2         248          440           620.0        1100.0        95.0        -235.0      80.0       
4           7            3         248          440           620.0        1100.0        -485.0      -235.0      220.0      
4           7            4         248          440           620.0        1100.0        95.0        -235.0      220.0      
4           7            5         248          440           620.0        1100.0        -485.0      -235.0      360.0      
4           7            6         248          440           620.0        1100.0        95.0        -235.0      360.0      
4           7            7         248          440           620.0        1100.0        -485.0      -235.0      500.0      
4           7            8         248          440           620.0        1100.0        95.0        -235.0      500.0      
 (Total: 8)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } Individual fields of scans session Session ID scan_idx Scan ID field Field Number px_width field pixels per line px_height lines per field um_width field width (microns) um_height field height (microns) field_x field x motor coordinates (microns) field_y field y motor coordinates (microns) field_z field z motor coordinates (microns) 4 7 1 248 440 620.0 1100.0 -485.0 -235.0 80.0 4 7 2 248 440 620.0 1100.0 95.0 -235.0 80.0 4 7 3 248 440 620.0 1100.0 -485.0 -235.0 220.0 4 7 4 248 440 620.0 1100.0 95.0 -235.0 220.0 4 7 5 248 440 620.0 1100.0 -485.0 -235.0 360.0 4 7 6 248 440 620.0 1100.0 95.0 -235.0 360.0 4 7 7 248 440 620.0 1100.0 -485.0 -235.0 500.0 4 7 8 248 440 620.0 1100.0 95.0 -235.0 500.0 Total: 8
```

### Code cell 16 (notebook cell 44, execution_count=16)

**Source**
```python
field_key = {'session': 4, 'scan_idx': 7, 'field': 4}
```

**Output**

_No output_

### Code cell 17 (notebook cell 45, execution_count=17)

**Source**
```python
nda.Field & field_key
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    *field    px_width     px_height     um_width     um_height     field_x     field_y     field_z    
+---------+ +----------+ +-------+ +----------+ +-----------+ +----------+ +-----------+ +---------+ +---------+ +---------+
4           7            4         248          440           620.0        1100.0        95.0        -235.0      220.0      
 (Total: 1)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } Individual fields of scans session Session ID scan_idx Scan ID field Field Number px_width field pixels per line px_height lines per field um_width field width (microns) um_height field height (microns) field_x field x motor coordinates (microns) field_y field y motor coordinates (microns) field_z field z motor coordinates (microns) 4 7 4 248 440 620.0 1100.0 95.0 -235.0 220.0 Total: 1
```

### Code cell 18 (notebook cell 47, execution_count=18)

**Source**
```python
import numpy as np
```

**Output**

_No output_

### Code cell 19 (notebook cell 49, execution_count=19)

**Source**
```python
nda.ScanTimes & scan_key
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    frame_time ndepths    
+---------+ +----------+ +--------+ +---------+
4           7            =BLOB=     4          
 (Total: 1)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } scan times per frame (in seconds, relative to the start of the scan) session Session ID scan_idx Scan ID frame_times stimulus frame times for field 1 of each scan, (len = nframes) ndepths number of imaging depths recorded for each scan 4 7 =BLOB= 4 Total: 1
```

### Code cell 20 (notebook cell 51, execution_count=20)

**Source**
```python
frame_times = (nda.ScanTimes & scan_key).fetch1('frame_times')
len(frame_times)
```

**Output**

Output 1 (execute_result):
```text
40000
```

### Code cell 21 (notebook cell 53, execution_count=21)

**Source**
```python
nda.Field & scan_key
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    *field    px_width     px_height     um_width     um_height     field_x     field_y     field_z    
+---------+ +----------+ +-------+ +----------+ +-----------+ +----------+ +-----------+ +---------+ +---------+ +---------+
4           7            1         248          440           620.0        1100.0        -485.0      -235.0      80.0       
4           7            2         248          440           620.0        1100.0        95.0        -235.0      80.0       
4           7            3         248          440           620.0        1100.0        -485.0      -235.0      220.0      
4           7            4         248          440           620.0        1100.0        95.0        -235.0      220.0      
4           7            5         248          440           620.0        1100.0        -485.0      -235.0      360.0      
4           7            6         248          440           620.0        1100.0        95.0        -235.0      360.0      
4           7            7         248          440           620.0        1100.0        -485.0      -235.0      500.0      
4           7            8         248          440           620.0        1100.0        95.0        -235.0      500.0      
 (Total: 8)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } Individual fields of scans session Session ID scan_idx Scan ID field Field Number px_width field pixels per line px_height lines per field um_width field width (microns) um_height field height (microns) field_x field x motor coordinates (microns) field_y field y motor coordinates (microns) field_z field z motor coordinates (microns) 4 7 1 248 440 620.0 1100.0 -485.0 -235.0 80.0 4 7 2 248 440 620.0 1100.0 95.0 -235.0 80.0 4 7 3 248 440 620.0 1100.0 -485.0 -235.0 220.0 4 7 4 248 440 620.0 1100.0 95.0 -235.0 220.0 4 7 5 248 440 620.0 1100.0 -485.0 -235.0 360.0 4 7 6 248 440 620.0 1100.0 95.0 -235.0 360.0 4 7 7 248 440 620.0 1100.0 -485.0 -235.0 500.0 4 7 8 248 440 620.0 1100.0 95.0 -235.0 500.0 Total: 8
```

### Code cell 22 (notebook cell 54, execution_count=22)

**Source**
```python
unique_field_depths = dj.U('field_z') & (nda.Field & scan_key)
print(f'The number of unique depths is: {len(unique_field_depths)}')

unique_field_depths
```

**Output**

Output 1 (stream):
```text
The number of unique depths is: 4
```

Output 2 (execute_result):
```text
*field_z   
+---------+
80.0       
220.0      
360.0      
500.0      
 (Total: 4)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } field_z field z motor coordinates (microns) 80.0 220.0 360.0 500.0 Total: 4
```

### Code cell 23 (notebook cell 56, execution_count=23)

**Source**
```python
fps = (nda.Scan & scan_key).fetch1('fps')
fps
```

**Output**

Output 1 (execute_result):
```text
6.3009
```

### Code cell 24 (notebook cell 57, execution_count=24)

**Source**
```python
(1 / np.diff(frame_times)).mean() # average frequency of timestamps
```

**Output**

Output 1 (execute_result):
```text
6.29845481738058
```

### Code cell 25 (notebook cell 59, execution_count=25)

**Source**
```python
import matplotlib.pyplot as plt
```

**Output**

_No output_

### Code cell 26 (notebook cell 61, execution_count=26)

**Source**
```python
nda.Stimulus & scan_key
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    movie     
+---------+ +----------+ +--------+
4           7            =BLOB=    
 (Total: 1)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } Stimulus presented session Session ID scan_idx Scan ID movie stimulus images synchronized with field 1 frame times (H x W X F matrix) 4 7 =BLOB= Total: 1
```

### Code cell 27 (notebook cell 62, execution_count=27)

**Source**
```python
movie = (nda.Stimulus & scan_key).fetch1('movie') # stimulus images synchronized with nda.ScanTimes
movie.shape #(height x width x frames)
```

**Output**

Output 1 (execute_result):
```text
(90, 160, 40000)
```

### Code cell 28 (notebook cell 63, execution_count=28)

**Source**
```python
movie_times = (nda.ScanTimes() & scan_key).fetch1('frame_times') # timestamps of stimulus images
movie_times.shape
```

**Output**

Output 1 (execute_result):
```text
(40000,)
```

### Code cell 29 (notebook cell 66, execution_count=29)

**Source**
```python
nda.Trial & scan_key
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    *trial_idx    type           start_idx     end_idx     start_frame_ti end_frame_time stim_times condition_hash
+---------+ +----------+ +-----------+ +------------+ +-----------+ +---------+ +------------+ +------------+ +--------+ +------------+
4           7            0             stimulus.Clip  55            117         8.703050851821 18.66956400871 =BLOB=     JEL5/i5FccX4yk
4           7            1             stimulus.Clip  118           181         18.76955008506 28.73606181144 =BLOB=     AAQ1HNKGrg1cIX
4           7            2             stimulus.Clip  182           244         28.83605670928 38.80255699157 =BLOB=     ksTS42zV+O0YJq
4           7            3             stimulus.Clip  245           308         38.90255165100 48.86905622482 =BLOB=     m5JLObtSRnbRKw
4           7            4             stimulus.Clip  309           371         48.96904659271 58.93554878234 =BLOB=     L8Z/mji+v1Wipu
4           7            5             stimulus.Clip  372           434         59.03554868698 69.00203704833 =BLOB=     3+VHi96yg36hu1
4           7            6             stimulus.Monet 435           529         69.11870193481 84.10179495811 =BLOB=     DKYV7TrfEl+C8n
4           7            7             stimulus.Monet 530           624         84.18511772155 99.16820192337 =BLOB=     +rgSVBVRE8Ij1W
4           7            8             stimulus.Monet 625           719         99.25153255462 114.2346186637 =BLOB=     GHn0W57E+2PS+Q
4           7            9             stimulus.Monet 720           814         114.3179526329 129.3010439872 =BLOB=     u0ftbdrw9UHzSH
4           7            10            stimulus.Clip  815           878         129.3843677043 139.3508741855 =BLOB=     JOYs8Wny1GJlw6
4           7            11            stimulus.Clip  879           941         139.4508776664 149.4173760414 =BLOB=     mG4xsIyTTnaRWK
   ...
 (Total: 464)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } Information for each Trial session Session ID scan_idx Scan ID trial_idx index of trial within stimulus type type of stimulus trial start_idx index of field 1 scan fram
... [output truncated in report; full output in executed notebook]
```

### Code cell 30 (notebook cell 68, execution_count=30)

**Source**
```python
trial_key = {'session': 4, 'scan_idx': 7, 'trial_idx': 8}
```

**Output**

_No output_

### Code cell 31 (notebook cell 69, execution_count=31)

**Source**
```python
trial_info = nda.Trial & trial_key
trial_info
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    *trial_idx    type           start_idx     end_idx     start_frame_ti end_frame_time stim_times condition_hash
+---------+ +----------+ +-----------+ +------------+ +-----------+ +---------+ +------------+ +------------+ +--------+ +------------+
4           7            8             stimulus.Monet 625           719         99.25153255462 114.2346186637 =BLOB=     GHn0W57E+2PS+Q
 (Total: 1)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } Information for each Trial session Session ID scan_idx Scan ID trial_idx index of trial within stimulus type type of stimulus trial start_idx index of field 1 scan frame at start of trial end_idx index of field 1 scan frame at end of trial start_frame_time start time of stimulus frame relative to scan start (seconds) end_frame_time end time of stimulus frame relative to scan start (seconds) stim_times full vector of stimulus frame times relative to scan start (seconds) condition_hash 120-bit hash (The first 20 chars of MD5 in base64) 4 7 8 stimulus.Monet2 625 719 99.25153255462646 114.23461866378784 =BLOB= GHn0W57E+2PS+Qr5yD2r Total: 1
```

### Code cell 32 (notebook cell 71, execution_count=32)

**Source**
```python
trial_info * nda.Monet2
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    *trial_idx    *condition_has type           start_idx     end_idx     start_frame_ti end_frame_time stim_times fps        duration     rng_seed     blue_green_sat pattern_width  pattern_aspect temp_kernel    temp_bandwidth ori_coherence  ori_fraction   ori_mix     n_dirs     speed     directions onsets     movie     
+---------+ +----------+ +-----------+ +------------+ +------------+ +-----------+ +---------+ +------------+ +------------+ +--------+ +--------+ +----------+ +----------+ +------------+ +------------+ +------------+ +------------+ +------------+ +------------+ +------------+ +---------+ +--------+ +-------+ +--------+ +--------+ +--------+
4           7            8             GHn0W57E+2PS+Q stimulus.Monet 625           719         99.25153255462 114.2346186637 =BLOB=     60.000     15.000       8.0          0.000          72             1.7            hamming        4.00           2.50           1.0            1.0         16         0.2       =BLOB=     =BLOB=     =BLOB=    
 (Total: 1)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } session Session ID scan_idx Scan ID trial_idx index of trial within stimulus condition_hash 120-bit hash (The first 20 chars of MD5 in base64) type type of stimulus trial start_idx index of field 1 scan frame at start of trial end_idx index of field 1 scan frame at end of trial start_frame_time start time of stimulus frame relative to scan start (seconds) end_frame_time end time of stimulus frame relative to scan start (seconds) stim_times full vector of stimulus frame times relative to scan start (seconds) fps display refresh rate duration (s) trial duration rng_seed random number generator seed blue_green_saturation 0 = grayscale, 1=blue/green pattern_width width of generated pattern pattern_aspect the aspect ratio of generated pattern temp_kernel temporal kernel type (hamming, half-hamming) temp_bandwidth (Hz) temporal bandwidth of the stimulus ori_coherence 1=unoriented noise. pi/ori_coherence = bandwidth of orientations. ori_fraction fraction of stimulus with coherent orientation vs unoriented ori_mix mixin-coefficient of orient
... [output truncated in report; full output in executed notebook]
```

### Code cell 33 (notebook cell 73, execution_count=33)

**Source**
```python
start, end = (trial_info * nda.Monet2).fetch1('start_idx', 'end_idx') # Fetch indices of trial
print(f'Trial starts at index: {start} and ends at index {end}')
```

**Output**

Output 1 (stream):
```text
Trial starts at index: 625 and ends at index 719
```

### Code cell 34 (notebook cell 74, execution_count=34)

**Source**
```python
stimulus_trial_slice = movie[:,:,slice(start, end)] # slice movie according to indices of trial
stimulus_trial_slice.shape
```

**Output**

Output 1 (execute_result):
```text
(90, 160, 94)
```

### Code cell 35 (notebook cell 75, execution_count=35)

**Source**
```python
fig, axs = plt.subplots(1, 2, dpi=150) # view first and last frame of movie slice
axs[0].imshow(stimulus_trial_slice[:,:,0], cmap='gray')
axs[0].set_title(f'frame: {start}')
axs[1].imshow(stimulus_trial_slice[:,:,-1], cmap='gray')
axs[1].set_title(f'frame: {end}')
[ax.axis('off') for ax in axs];
```

**Output**

Output 1 (display_data):
```text
<Figure size 960x720 with 2 Axes>
[image/png output, base64 length=119988]
```

### Code cell 36 (notebook cell 77, execution_count=36)

**Source**
```python
import requests
import skvideo.io
```

**Output**

_No output_

### Code cell 37 (notebook cell 78, execution_count=37)

**Source**
```python
base_url = 'https://bossdb-open-data.s3.amazonaws.com/iarpa_microns/minnie/functional_data/stimulus_movies'
```

**Output**

_No output_

### Code cell 38 (notebook cell 79, execution_count=38)

**Source**
```python
filename = f'stimulus_17797_{scan_key["session"]}_{scan_key["scan_idx"]}_v4.avi'
```

**Output**

_No output_

### Code cell 39 (notebook cell 80, execution_count=39)

**Source**
```python
url = base_url + '/' + filename
url
```

**Output**

Output 1 (execute_result):
```text
'https://bossdb-open-data.s3.amazonaws.com/iarpa_microns/minnie/functional_data/stimulus_movies/stimulus_17797_4_7_v4.avi'
```

### Code cell 40 (notebook cell 81, execution_count=40)

**Source**
```python
# movie_aws = requests.get(url) # uncomment this cell to download movie. each movie is approx 9.8 GB movie

# with open(filename, 'wb') as f:
#     f.write(movie_aws.content) # will write to current directory as avi
```

**Output**

_No output_

### Code cell 41 (notebook cell 84, execution_count=41)

**Source**
```python
nda.RawManualPupil() & scan_key
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    pupil_min_ pupil_maj_ pupil_x    pupil_y    pupil_time
+---------+ +----------+ +--------+ +--------+ +--------+ +--------+ +--------+
4           7            =BLOB=     =BLOB=     =BLOB=     =BLOB=     =BLOB=    
 (Total: 1)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } Pupil traces session Session ID scan_idx Scan ID pupil_min_r vector of pupil minor radii (pixels) pupil_maj_r vector of pupil major radii (pixels) pupil_x vector of pupil x positions (pixels) pupil_y vector of pupil y positions (pixels) pupil_times vector of times relative to scan start (seconds) 4 7 =BLOB= =BLOB= =BLOB= =BLOB= =BLOB= Total: 1
```

### Code cell 42 (notebook cell 85, execution_count=42)

**Source**
```python
nda.ManualPupil & scan_key
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    pupil_min_ pupil_maj_ pupil_x    pupil_y   
+---------+ +----------+ +--------+ +--------+ +--------+ +--------+
4           7            =BLOB=     =BLOB=     =BLOB=     =BLOB=    
 (Total: 1)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } Pupil traces session Session ID scan_idx Scan ID pupil_min_r vector of pupil minor radii synchronized with field 1 frame times (pixels) pupil_maj_r vector of pupil major radii synchronized with field 1 frame times (pixels) pupil_x vector of pupil x positions synchronized with field 1 frame times (pixels) pupil_y vector of pupil y positions synchronized with field 1 frame times (pixels) 4 7 =BLOB= =BLOB= =BLOB= =BLOB= Total: 1
```

### Code cell 43 (notebook cell 87, execution_count=43)

**Source**
```python
nda.RawTreadmill & scan_key
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    treadmill_ treadmill_
+---------+ +----------+ +--------+ +--------+
4           7            =BLOB=     =BLOB=    
 (Total: 1)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } Treadmill traces session Session ID scan_idx Scan ID treadmill_velocity vector of treadmill velocities (cm/s) treadmill_timestamps vector of times relative to scan start (seconds) 4 7 =BLOB= =BLOB= Total: 1
```

### Code cell 44 (notebook cell 88, execution_count=44)

**Source**
```python
nda.Treadmill & scan_key
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    treadmill_
+---------+ +----------+ +--------+
4           7            =BLOB=    
 (Total: 1)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } Treadmill traces session Session ID scan_idx Scan ID treadmill_velocity vector of treadmill velocities synchronized with field 1 frame times (cm/s) 4 7 =BLOB= Total: 1
```

### Code cell 45 (notebook cell 91, execution_count=45)

**Source**
```python
nda.SummaryImages & field_key
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    *field    correlatio average   
+---------+ +----------+ +-------+ +--------+ +--------+
4           7            4         =BLOB=     =BLOB=    
 (Total: 1)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } session Session ID scan_idx Scan ID field Field Number correlation correlation image average average image 4 7 4 =BLOB= =BLOB= Total: 1
```

### Code cell 46 (notebook cell 93, execution_count=46)

**Source**
```python
corr, avg = (nda.SummaryImages & field_key).fetch1('correlation', 'average')
```

**Output**

_No output_

### Code cell 47 (notebook cell 94, execution_count=47)

**Source**
```python
fig, axs = plt.subplots(1, 3, figsize=(10,6), dpi=200)
axs[0].imshow(corr)
axs[0].set_title('correlation image')
axs[1].imshow(avg)
axs[1].set_title('average image')
axs[2].imshow(corr*avg) # gives a good view of the cell bodies and darkens vessels
axs[2].set_title('correlation * average image')
[ax.axis('off') for ax in axs];
[ax.set_aspect('auto') for ax in axs];
```

**Output**

Output 1 (display_data):
```text
<Figure size 2000x1200 with 3 Axes>
[image/png output, base64 length=1817040]
```

### Code cell 48 (notebook cell 97, execution_count=48)

**Source**
```python
intensities = (nda.MeanIntensity & field_key).fetch1('intensities')
```

**Output**

_No output_

### Code cell 49 (notebook cell 98, execution_count=49)

**Source**
```python
fig, ax = plt.subplots(figsize=(10, 3), dpi=150)
ax.plot(intensities, c='b', alpha=0.5)
ax.set_xlabel('Frames')
ax.set_ylabel('Field Mean Intensity')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
```

**Output**

Output 1 (display_data):
```text
<Figure size 1500x450 with 1 Axes>
[image/png output, base64 length=68628]
```

### Code cell 50 (notebook cell 101, execution_count=50)

**Source**
```python
nda.Segmentation * nda.MaskClassification & field_key
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    *field    *mask_id    pixels     weights    mask_type    
+---------+ +----------+ +-------+ +---------+ +--------+ +--------+ +-----------+
4           7            4         1           =BLOB=     =BLOB=     artifact     
4           7            4         2           =BLOB=     =BLOB=     soma         
4           7            4         3           =BLOB=     =BLOB=     soma         
4           7            4         4           =BLOB=     =BLOB=     artifact     
4           7            4         5           =BLOB=     =BLOB=     soma         
4           7            4         6           =BLOB=     =BLOB=     soma         
4           7            4         7           =BLOB=     =BLOB=     soma         
4           7            4         8           =BLOB=     =BLOB=     soma         
4           7            4         9           =BLOB=     =BLOB=     artifact     
4           7            4         10          =BLOB=     =BLOB=     artifact     
4           7            4         11          =BLOB=     =BLOB=     artifact     
4           7            4         12          =BLOB=     =BLOB=     soma         
   ...
 (Total: 1389)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } session Session ID scan_idx Scan ID field Field Number mask_id mask ID, unique per field pixels indices into the image in column major (Fortran) order weights weights of the mask at the indices above mask_type classification of mask as soma or artifact 4 7 4 1 =BLOB= =BLOB= artifact 4 7 4 2 =BLOB= =BLOB= soma 4 7 4 3 =BLOB= =BLOB= soma 4 7 4 4 =BLOB= =BLOB= artifact 4 7 4 5 =BLOB= =BLOB= soma 4 7 4 6 =BLOB= =BLOB= soma 4 7 4 7 =BLOB= =BLOB= soma 4 7 4 8 =BLOB= =BLOB= soma 4 7 4 9 =BLOB= =BLOB= artifact 4 7 4 10 =BLOB= =BLOB= artifact 4 7 4 11 =BLOB= =BLOB= artifact 4 7 4 12 =BLOB= =BLOB= soma ... Total: 1389
```

### Code cell 51 (notebook cell 103, execution_count=51)

**Source**
```python
masks = utils.get_all_masks(field_key, mask_type='soma', plot=True) # function that will retrieve masks in convenient format and optionally plot
```

**Output**

Output 1 (display_data):
```text
<Figure size 700x1241.94 with 1 Axes>
[image/png output, base64 length=1216172]
```

### Code cell 52 (notebook cell 106, execution_count=52)

**Source**
```python
calcium_trace = (nda.Fluorescence() & field_key & {'mask_id': 500}).fetch1('trace')
```

**Output**

_No output_

### Code cell 53 (notebook cell 107, execution_count=53)

**Source**
```python
fig, ax = plt.subplots(figsize=(10, 3), dpi=150)
ax.plot(calcium_trace, c='g')
ax.set_xlabel('Frames')
ax.set_ylabel('Fluorescence')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
```

**Output**

Output 1 (display_data):
```text
<Figure size 1500x450 with 1 Axes>
[image/png output, base64 length=68060]
```

### Code cell 54 (notebook cell 110, execution_count=54)

**Source**
```python
# unit coordinates (`um_x`, `um_y`, `um_z`) are in microns and in the original motor reference frame (see technical documentation for more info)
# unit coordinate (`px_x` and `px_y` are the unit coordinates in image pixels)
# this table can also be used to relate `unit_id's` and `mask_id's` that are used in nda.Segmentation and nda.Fluorescence
nda.ScanUnit() & scan_key
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    *unit_id    field     mask_id     um_x     um_y     um_z     px_x     px_y     ms_delay    
+---------+ +----------+ +---------+ +-------+ +---------+ +------+ +------+ +------+ +------+ +------+ +----------+
4           7            1           1         1           -778     -771     80       7        5        0           
4           7            2           1         2           -741     -766     80       22       7        0           
4           7            3           1         3           -691     -776     80       41       3        0           
4           7            4           1         4           -691     -766     80       42       8        0           
4           7            5           1         5           -702     -767     80       37       7        0           
4           7            6           1         6           -646     -764     80       60       8        0           
4           7            7           1         7           -553     -770     80       97       6        0           
4           7            8           1         8           -534     -758     80       105      11       0           
4           7            9           1         9           -499     -760     80       119      10       0           
4           7            10          1         10          -460     -768     80       134      7        0           
4           7            11          1         11          -362     -772     80       173      5        0           
4           7            12          1         12          -442     -675     80       141      44       2           
   ...
 (Total: 8395)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } single unit in the scan session Session ID scan_idx Scan ID unit_id unique per scan field Field Number mask_id mask ID, unique per field um_x centroid x motor coordinates (microns) um_y centroid y motor coordinates (microns) um_z centroid z motor coordinates (microns) px_x centroid x pixel coordinate in field (pixels px_y centroid y pixel coordinate in field (pixels ms_delay delay from start of frame (field 1 pixel 1) to recordin
... [output truncated in report; full output in executed notebook]
```

### Code cell 55 (notebook cell 113, execution_count=55)

**Source**
```python
oracles = (nda.Oracle & scan_key).fetch('pearson')
```

**Output**

_No output_

### Code cell 56 (notebook cell 114, execution_count=56)

**Source**
```python
fig, ax = plt.subplots()
ax.hist(oracles, bins=50, color='k');
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
```

**Output**

Output 1 (display_data):
```text
<Figure size 640x480 with 1 Axes>
[image/png output, base64 length=11248]
```

### Code cell 57 (notebook cell 115, execution_count=57)

**Source**
```python
high_oracle_percentile = np.percentile(oracles, 99)
```

**Output**

_No output_

### Code cell 58 (notebook cell 117, execution_count=58)

**Source**
```python
high_oracle_table = nda.Oracle & scan_key & f'pearson>{high_oracle_percentile}'
high_oracle_table
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    *unit_id    trials     pearson     
+---------+ +----------+ +---------+ +--------+ +----------+
4           7            130         60         0.623745    
4           7            327         60         0.61131     
4           7            493         60         0.54457     
4           7            688         60         0.561252    
4           7            756         60         0.617953    
4           7            775         60         0.638734    
4           7            795         60         0.613519    
4           7            907         60         0.574646    
4           7            1070        60         0.553697    
4           7            1177        60         0.57389     
4           7            1262        60         0.594857    
4           7            1552        60         0.593425    
   ...
 (Total: 75)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } Leave-one-out correlation for repeated videos in stimulus. session Session ID scan_idx Scan ID unit_id unique per scan trials number of trials used pearson per unit oracle pearson correlation over all movies 4 7 130 60 0.623745 4 7 327 60 0.61131 4 7 493 60 0.54457 4 7 688 60 0.561252 4 7 756 60 0.617953 4 7 775 60 0.638734 4 7 795 60 0.613519 4 7 907 60 0.574646 4 7 1070 60 0.553697 4 7 1177 60 0.57389 4 7 1262 60 0.594857 4 7 1552 60 0.593425 ... Total: 75
```

### Code cell 59 (notebook cell 119, execution_count=59)

**Source**
```python
unit_key = high_oracle_table.fetch('KEY', offset=10, limit=1)[0]
unit_key
```

**Output**

Output 1 (execute_result):
```text
{'session': 4, 'scan_idx': 7, 'unit_id': 1262}
```

### Code cell 60 (notebook cell 122, execution_count=60)

**Source**
```python
oracle_traces, score = utils.fetch_oracle_raster(unit_key)
```

**Output**

_No output_

### Code cell 61 (notebook cell 123, execution_count=61)

**Source**
```python
fig,axes = plt.subplots(1,6, figsize=(6,1),dpi=300)
for col,clip_trace in zip(axes,np.moveaxis(oracle_traces,1,0)):
    col.imshow(clip_trace,cmap='binary', interpolation='nearest')
    col.set_aspect('auto')
    col.set_xticks([])
    col.set_yticks([])
axes[0].set_ylabel(f'oracle score: {score:.2f}', fontsize=5)
fig.subplots_adjust(wspace=.05)
[ax.set_title(f'oracle clip {i+1}', fontsize=6) for i, ax in enumerate(axes)];
fig.suptitle(f'session: {unit_key["session"]}, scan_idx: {unit_key["scan_
... [source truncated]
```

**Output**

Output 1 (execute_result):
```text
Text(0.5, 1.2, 'session: 4, scan_idx: 7, unit_id: 1262')
```

Output 2 (display_data):
```text
<Figure size 1800x300 with 6 Axes>
[image/png output, base64 length=38420]
```

### Code cell 62 (notebook cell 126, execution_count=62)

**Source**
```python
nda.AreaMembership()
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    *unit_id    brain_area    
+---------+ +----------+ +---------+ +------------+
4           7            1           LM            
4           7            2           LM            
4           7            3           LM            
4           7            4           LM            
4           7            5           LM            
4           7            6           LM            
4           7            7           LM            
4           7            8           LM            
4           7            9           LM            
4           7            10          LM            
4           7            11          LM            
4           7            12          LM            
   ...
 (Total: 168971)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } session Session ID scan_idx Scan ID unit_id unique per scan brain_area Visual area membership of unit 4 7 1 LM 4 7 2 LM 4 7 3 LM 4 7 4 LM 4 7 5 LM 4 7 6 LM 4 7 7 LM 4 7 8 LM 4 7 9 LM 4 7 10 LM 4 7 11 LM 4 7 12 LM ... Total: 168971
```

### Code cell 63 (notebook cell 129, execution_count=63)

**Source**
```python
nda.Activity() & unit_key
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    *unit_id    trace     
+---------+ +----------+ +---------+ +--------+
4           7            1262        =BLOB=    
 (Total: 1)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } activity inferred from fluorescence traces session Session ID scan_idx Scan ID unit_id unique per scan trace spike trace 4 7 1262 =BLOB= Total: 1
```

### Code cell 64 (notebook cell 130, execution_count=64)

**Source**
```python
spike_trace = (nda.Activity() & unit_key).fetch1('trace')
```

**Output**

_No output_

### Code cell 65 (notebook cell 131, execution_count=65)

**Source**
```python
fig, ax = plt.subplots(figsize=(10, 3), dpi=150)
ax.plot(spike_trace, c='k')
ax.set_xlabel('Frames')
ax.set_ylabel('Spike trace')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
```

**Output**

Output 1 (display_data):
```text
<Figure size 1500x450 with 1 Axes>
[image/png output, base64 length=50836]
```

### Code cell 66 (notebook cell 134, execution_count=66)

**Source**
```python
nda.Fluorescence & (nda.ScanUnit & unit_key)
```

**Output**

Output 1 (execute_result):
```text
*session    *scan_idx    *field    *mask_id    trace     
+---------+ +----------+ +-------+ +---------+ +--------+
4           7            3         167         =BLOB=    
 (Total: 1)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } fluorescence traces before spike extraction or filtering session Session ID scan_idx Scan ID field Field Number mask_id mask ID, unique per field trace fluorescence trace 4 7 3 167 =BLOB= Total: 1
```

### Code cell 67 (notebook cell 135, execution_count=67)

**Source**
```python
calcium_trace = (nda.Fluorescence & (nda.ScanUnit & unit_key)).fetch1('trace')
```

**Output**

_No output_

### Code cell 68 (notebook cell 136, execution_count=68)

**Source**
```python
fig, ax = plt.subplots(figsize=(10, 3), dpi=150)
ax.plot(calcium_trace/ np.max(calcium_trace), c='g', alpha=0.5, label='calcium')
ax.plot(spike_trace/ np.max(spike_trace), c='k', label='spike', alpha=0.5)
ax.set_xlabel('Frames')
ax.legend()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
```

**Output**

Output 1 (display_data):
```text
<Figure size 1500x450 with 1 Axes>
[image/png output, base64 length=84756]
```

### Code cell 69 (notebook cell 141, execution_count=69)

**Source**
```python
nda.Stack()
```

**Output**

Output 1 (execute_result):
```text
*stack_session *stack_idx    motor_z     motor_y      motor_x     px_depth     px_height     px_width     um_depth     um_height     um_width     surf_z    
+------------+ +-----------+ +---------+ +----------+ +---------+ +----------+ +-----------+ +----------+ +----------+ +-----------+ +----------+ +--------+
9              19            314.0       -173.688     -236.91     335          661           706          670.0        1322.0        1412.0       -21.0     
 (Total: 1)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } all slices of each stack after corrections. stack_session session index for the mouse stack_idx id of the stack motor_z center of volume in the motor coordinate system (microns, cortex is at 0) motor_y center of volume in the motor coordinate system (microns) motor_x center of volume in the motor coordinate system (microns) px_depth number of slices px_height lines per frame px_width pixels per line um_depth depth (microns) um_height height (microns) um_width width (microns) surf_z depth of first slice - half a z step (microns,cortex is at z=0) 9 19 314.0 -173.688 -236.91 335 661 706 670.0 1322.0 1412.0 -21.0 Total: 1
```

### Code cell 70 (notebook cell 144, execution_count=70)

**Source**
```python
# affine matrix parameters for each field registered into the stack
nda.Registration & field_key
```

**Output**

Output 1 (execute_result):
```text
*stack_session *stack_idx    *session    *scan_idx    *field    a11         a21            a31           a12            a22          a32            reg_x       reg_y        reg_z       score        reg_field 
+------------+ +-----------+ +---------+ +----------+ +-------+ +---------+ +------------+ +-----------+ +------------+ +----------+ +------------+ +---------+ +----------+ +---------+ +----------+ +--------+
9              19            4           7            4         1.00784     -0.00337667    -0.017749     -0.0231734     0.994399     0.00351191     94.7115     -276.434     217.736     0.646221     =BLOB=    
 (Total: 1)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } align a 2-d scan field to a stack with affine matrix learned via gradient ascent stack_session session index for the mouse stack_idx id of the stack session Session ID scan_idx Scan ID field Field Number a11 row 1, column 1 of the affine matrix (microns) a21 row 2, column 1 of the affine matrix (microns) a31 row 3, column 1 of the affine matrix (microns) a12 row 1, column 2 of the affine matrix (microns) a22 row 2, column 2 of the affine matrix (microns) a32 row 3, column 2 of the affine matrix (microns) reg_x z translation (microns) reg_y y translation (microns) reg_z z translation (microns) score cross-correlation score (-1 to 1) reg_field extracted field from the stack in the specified position 9 19 4 7 4 1.00784 -0.00337667 -0.017749 -0.0231734 0.994399 0.00351191 94.7115 -276.434 217.736 0.646221 =BLOB= Total: 1
```

### Code cell 71 (notebook cell 145, execution_count=71)

**Source**
```python
reg_field = (nda.Registration & field_key).fetch1('reg_field')
```

**Output**

_No output_

### Code cell 72 (notebook cell 147, execution_count=72)

**Source**
```python
fig, axs = plt.subplots(1, 2, figsize=(6,4), dpi=150)
axs[0].imshow(avg)
axs[0].set_title('Field average image')
axs[1].imshow(reg_field)
axs[1].set_title('Extracted stack field image')
[ax.axis('off') for ax in axs];
```

**Output**

Output 1 (display_data):
```text
<Figure size 900x600 with 2 Axes>
[image/png output, base64 length=393364]
```

### Code cell 73 (notebook cell 150, execution_count=73)

**Source**
```python
grid = utils.get_grid(field_key) # fetch registered grid in motor reference frame at 1um/ pixel resolution
grid.shape
```

**Output**

Output 1 (execute_result):
```text
(1100, 620, 3)
```

### Code cell 74 (notebook cell 152, execution_count=74)

**Source**
```python
center_x, center_y, center_z = nda.Stack.fetch1('motor_x', 'motor_y', 'motor_z') # get stack center in um
length_x, length_y, length_z = nda.Stack.fetch1('um_width', 'um_height', 'um_depth') # get stack dimensions in um

np_grid = grid - np.array([center_x, center_y, center_z]) + np.array([length_x, length_y, length_z]) / 2 # convert grid to the stack reference frame

np_grid.shape
```

**Output**

Output 1 (execute_result):
```text
(1100, 620, 3)
```

### Code cell 75 (notebook cell 155, execution_count=75)

**Source**
```python
nda.Coregistration()
```

**Output**

Output 1 (execute_result):
```text
*stack_session *stack_idx    *transform_id  version     direction     transform_type transform_ transform_
+------------+ +-----------+ +------------+ +---------+ +-----------+ +------------+ +--------+ +--------+
9              19            1              phase2      2PEM          spline         =BLOB=     =BLOB=    
9              19            2              phase2      EM2P          spline         =BLOB=     =BLOB=    
9              19            3              phase2      2PEM          linear         =BLOB=     =BLOB=    
9              19            4              phase2      EM2P          linear         =BLOB=     =BLOB=    
9              19            5              phase3      2PEM          spline         =BLOB=     =BLOB=    
9              19            6              phase3      EM2P          spline         =BLOB=     =BLOB=    
9              19            7              phase3      2PEM          linear         =BLOB=     =BLOB=    
9              19            8              phase3      EM2P          linear         =BLOB=     =BLOB=    
 (Total: 8)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltiptext { visibility: visible; } transformation solutions between 2P stack and EM stack and vice versa from the Allen Institute stack_session session index for the mouse stack_idx id of the stack transform_id id of the transform version coordinate framework direction direction of the transform (EMTP: EM -> 2P, TPEM: 2P -> EM) transform_type linear (more rigid) or spline (more nonrigid) transform_args parameters of the transform transform_solution transform solution 9 19 1 phase2 2PEM spline =BLOB= =BLOB= 9 19 2 phase2 EM2P spline =BLOB= =BLOB= 9 19 3 phase2 2PEM linear =BLOB= =BLOB= 9 19 4 phase2 EM2P linear =BLOB= =BLOB= 9 19 5 phase3 2PEM spline =BLOB= =BLOB= 9 19 6 phase3 EM2P spline =BLOB= =BLOB= 9 19 7 phase3 2PEM linear =BLOB= =BLOB= 9 19 8 phase3 EM2P linear =BLOB= =BLOB= Total: 8
```

### Code cell 76 (notebook cell 157, execution_count=76)

**Source**
```python
transform_params = utils.fetch_coreg(transform_id=5) # phase3 "spline" 2P -> #EM transform
```

**Output**

_No output_

### Code cell 77 (notebook cell 159, execution_count=77)

**Source**
```python
reshaped_grid = np_grid.reshape(-1, 3) # reshape grid to n X 3

em_grid = utils.coreg_transform(reshaped_grid[::200], **transform_params) # pass in array of coordinates and transform parameters
```

**Output**

_No output_

### Code cell 78 (notebook cell 160, execution_count=78)

**Source**
```python
em_grid.shape
```

**Output**

Output 1 (execute_result):
```text
(3410, 3)
```

### Code cell 79 (notebook cell 164, execution_count=79)

**Source**
```python
import pandas as pd
from caveclient import CAVEclient

# generate links in Seung lab a custom Neuroglancer deployment called Neuromancer
from nglui import statebuilder, EasyViewer
```

**Output**

_No output_

### Code cell 80 (notebook cell 166, execution_count=80)

**Source**
```python
# client = CAVEclient()
# client.auth.get_new_token()
```

**Output**

_No output_

### Code cell 81 (notebook cell 168, execution_count=81)

**Source**
```python
# this is the datastack name of the public release
# passing it will auto-configure many of the services
client = CAVEclient('minnie65_public')
```

**Output**

_No output_

### Code cell 82 (notebook cell 171, execution_count=82)

**Source**
```python
client.materialize.version = 661
```

**Output**

_No output_

### Code cell 83 (notebook cell 173, execution_count=83)

**Source**
```python
# sample every 200th grid point for viewing in Neuroglancer
grid_df = pd.DataFrame([[[e[0],e[1],e[2]]] 
                        for e in em_grid]).rename(columns={0:'grid_xyz'})
```

**Output**

_No output_

### Code cell 84 (notebook cell 175, execution_count=84)

**Source**
```python
viewer = EasyViewer()
viewer.set_resolution((4,4,40))

# public em source
em_layer = statebuilder.ImageLayerConfig(client.info.image_source()) 

# public segmentation source
seg_layer = statebuilder.SegmentationLayerConfig(client.info.segmentation_source(), 
                                                 name='seg') 

# annotation layer for grid 
anno_layer = statebuilder.AnnotationLayerConfig(name='field-grid', 
                                                mapping_rules=statebuilder.PointM
... [source truncated]
```

**Output**

Output 1 (execute_result):
```text
<IPython.core.display.HTML object>
[text/html] Neuroglancer Link
```

### Code cell 85 (notebook cell 178, execution_count=85)

**Source**
```python
nda.StackUnit() & field_key
```

**Output**

Output 1 (execute_result):
```text
*stack_session *stack_idx    *session    *scan_idx    *field    *unit_id    motor_x      motor_y      motor_z     stack_x     stack_y     stack_z    
+------------+ +-----------+ +---------+ +----------+ +-------+ +---------+ +----------+ +----------+ +---------+ +---------+ +---------+ +---------+
9              19            4           7            4         2551        -168.584     -816.214     220.685     774.33      18.47       241.69     
9              19            4           7            4         2552        -98.5568     -794.077     219.522     844.35      40.61       240.52     
9              19            4           7            4         2553        -10.5446     -786.914     217.995     932.37      47.77       239.0      
9              19            4           7            4         2554        29.4794      -774.619     217.329     972.39      60.07       238.33     
9              19            4           7            4         2555        60.0042      -787.15      216.753     1002.91     47.54       237.75     
9              19            4           7            4         2556        100.434      -792.257     216.025     1043.34     42.43       237.03     
9              19            4           7            4         2557        112.974      -789.814     215.812     1055.88     44.87       236.81     
9              19            4           7            4         2558        138.112      -787.412     215.377     1081.02     47.28       236.38     
9              19            4           7            4         2559        151.0        -799.884     215.111     1093.91     34.8        236.11     
9              19            4           7            4         2560        131.306      -819.705     215.396     1074.22     14.98       236.4      
9              19            4           7            4         2561        176.543      -814.885     214.615     1119.45     19.8        235.61     
9              19            4           7            4         2562        180.945      -787.556     214.623     1123.86     47.13       235.62     
   ...
 (Total: 1389)
[text/html] .Relation{ border-collapse:collapse; } .Relation th{ background: #A0A0A0; color: #ffffff; padding:4px; border:#f0e0e0 1px solid; font-weight: normal; font-family: monospace; font-size: 100%; } .Relation td{ padding:4px; border:#f0e0e0 1px solid; font-size:100%; } .Relation tr:nth-child(odd){ background: #ffffff; } .Relation tr:nth-child(even){ background: #f3f1ff; } /* Tooltip container */ .djtooltip { } /* Tooltip text */ .djtooltip .djtooltiptext { visibility: hidden; width: 120px; background-color: black; color: #fff; text-align: center; padding: 5px 0; border-radius: 6px; /* Position the tooltip text - see examples below! */ position: absolute; z-index: 1; } #primary { font-weight: bold; color: black; } #nonprimary { font-weight: normal; color: white; } /* Show the tooltip text when you mouse over the tooltip container */ .djtooltip:hover .djtooltipt
... [output truncated in report; full output in executed notebook]
```

### Code cell 86 (notebook cell 180, execution_count=86)

**Source**
```python
unit_xyz_2P = np.stack((nda.StackUnit() & field_key).fetch('stack_x', 'stack_y', 'stack_z'), -1)
```

**Output**

_No output_

### Code cell 87 (notebook cell 181, execution_count=87)

**Source**
```python
unit_xyz_2P.shape
```

**Output**

Output 1 (execute_result):
```text
(1389, 3)
```

### Code cell 88 (notebook cell 183, execution_count=88)

**Source**
```python
unit_xyz_em = utils.coreg_transform(unit_xyz_2P, transform_id=5)
```

**Output**

_No output_

### Code cell 89 (notebook cell 184, execution_count=89)

**Source**
```python
unit_xyz_em_df = pd.DataFrame([[[e[0],e[1],e[2]]] for e in unit_xyz_em]).rename(columns={0:'unit_xyz_em'})
```

**Output**

_No output_

### Code cell 90 (notebook cell 186, execution_count=90)

**Source**
```python
viewer = EasyViewer()
viewer.set_resolution((4,4,40))

# public em source
em_layer = statebuilder.ImageLayerConfig(client.info.image_source()) 

# public segmentation source
seg_layer = statebuilder.SegmentationLayerConfig(client.info.segmentation_source(), 
                                                 name='seg') 

# annotation layer for grid 
anno_layer = statebuilder.AnnotationLayerConfig(name='field-units', 
                                                mapping_rules=statebuilder.Point
... [source truncated]
```

**Output**

Output 1 (execute_result):
```text
<IPython.core.display.HTML object>
[text/html] Neuroglancer Link
```

### Code cell 91 (notebook cell 189, execution_count=91)

**Source**
```python
area, x, y = (nda.AreaMembership * nda.StackUnit).fetch('brain_area', 'stack_x', 'stack_y')
```

**Output**

_No output_

### Code cell 92 (notebook cell 190, execution_count=92)

**Source**
```python
color_dict = {'LM':'blue', 'AL': 'green', 'RL': 'purple', 'V1': 'red'}
```

**Output**

_No output_

### Code cell 93 (notebook cell 191, execution_count=93)

**Source**
```python
fig, ax = plt.subplots(dpi=200)
ax.scatter(x, y, color=[color_dict[a] for a in area], s=1)
ax.set_aspect('equal')
ax.invert_yaxis()
ax.set_xlabel('2P stack x-axis')
ax.set_ylabel('2P stack y-axis')
ax.annotate('LM', (500, 300))
ax.annotate('AL', (900, 150))
ax.annotate('RL', (1100, 350))
ax.annotate('V1', (800, 600))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
```

**Output**

Output 1 (display_data):
```text
<Figure size 1280x960 with 1 Axes>
[image/png output, base64 length=197788]
```

## Matched_Cell_Functional_Data_v1718_v4.executed.ipynb

### Code cell 1 (notebook cell 4, execution_count=1)

**Source**
```python
from caveclient import CAVEclient
```

**Output**

_No output_

### Code cell 2 (notebook cell 6, execution_count=2)

**Source**
```python
client = CAVEclient()
client.auth.get_new_token()
```

**Output**

Output 1 (stream):
```text
New Tokens need to be acquired by hand. Please follow the following steps:
                1) Go to: https://global.daf-apis.com/auth/api/v1/create_token to create a new token.
                2) Log in with your Google credentials and copy the token shown afterward.
                3a) Save it to your computer with: client.auth.save_token(token="PASTE_YOUR_TOKEN_HERE")
                or
                3b) Set it for the current session only with client.auth.token = "PASTE_YOUR_TOKEN_HERE"
                Note: If you need to save or load multiple tokens, please read the documentation for details.
                Warning! Creating a new token by finishing step 2 will invalidate the previous token!
```

### Code cell 3 (notebook cell 8, execution_count=3)

**Source**
```python
# this is the datastack name of the public release
# passing it will auto-configure many of the services
client = CAVEclient('minnie65_public')
```

**Output**

_No output_

### Code cell 4 (notebook cell 11, execution_count=4)

**Source**
```python
client.materialize.version = 1718
```

**Output**

_No output_

### Code cell 5 (notebook cell 13, execution_count=5)

**Source**
```python
client.materialize.get_tables()
```

**Output**

Output 1 (execute_result):
```text
['synapses_pni_2',
 'nucleus_detection_v0',
 'vortex_manual_nodes_of_ranvier',
 'bodor_pt_target_proofread',
 'baylor_gnn_cell_type_fine_model_v2',
 'nucleus_alternative_points',
 'nucleus_functional_area_assignment',
 'coregistration_auto_phase3_fwd_apl_vess_combined_v2',
 'aibs_metamodel_mtypes_v661_v2_corrections',
 'vortex_thalamic_proofreading_status',
 'allen_column_mtypes_v2',
 'proofreading_status_and_strategy',
 'bodor_pt_cells',
 'aibs_metamodel_mtypes_v661_v2',
 'aibs_metamodel_celltypes_v661_corrections',
 'vortex_microglia_proofreading_status',
 'allen_v1_column_types_slanted_ref',
 'multi_input_spine_predictions_ssa',
 'aibs_column_nonneuronal_ref',
 'nucleus_ref_neuron_svm',
 'synapse_target_structure',
 'myelin_auto_tags_2points',
 'apl_functional_coreg_vess_fwd',
 'vortex_axon_backtrace_column',
 'cell_type_multifeature_combo',
 'vortex_compartment_targets',
 'baylor_log_reg_cell_type_coarse_v1',
 'vortex_synapse_reattachment',
 'coregistration_auto_phase3_fwd_v2',
 'synapse_target_predictions_ssa_v2',
 'gamlin_2023_mcs',
 'l5et_column',
 'pt_synapse_targets',
 'vortex_peptidergic_proofreading_status',
 'coregistration_manual_v4',
 'cg_cell_type_calls',
 'digital_twin_properties_bcm_coreg_v4',
 'synapse_spine_mapping_v2',
 'vortex_astrocyte_proofreading_status',
 'digital_twin_properties_bcm_coreg_auto_phase3_fwd_v2',
 'digital_twin_properties_bcm_coreg_apl_vess_fwd',
 'gamlin_2023_mcs_met_types',
 'vortex_manual_myelination_v0',
 'synapse_target_predictions_ssa',
 'aibs_metamodel_celltypes_v661']
```

### Code cell 6 (notebook cell 15, execution_count=6)

**Source**
```python
import pandas as pd
```

**Output**

_No output_

### Code cell 7 (notebook cell 16, execution_count=7)

**Source**
```python
matched_df = client.materialize.query_table('coregistration_manual_v4')
matched_df
```

**Output**

Output 1 (stream):
```text
Using non-pandas query execution is deprecated as it can mangle types, please upgrade caveclient to >=8.0.0 to use pandas for improved type handling.
```

Output 2 (execute_result):
```text
id                          created valid  target_id  session  \
0       5491 2024-05-21 18:38:25.372047+00:00     t     335649        6   
1      12542 2024-05-21 18:42:40.285576+00:00     t     194144        7   
2      15097 2024-05-21 18:42:41.703496+00:00     t     194144        8   
3      12829 2024-05-21 18:42:40.443453+00:00     t     517966        7   
4      10490 2024-05-21 18:42:39.170710+00:00     t     224395        7   
...      ...                              ...   ...        ...      ...   
19176   9135 2024-05-21 18:42:31.481457+00:00     t     328140        6   
19177  11239 2024-05-21 18:42:39.579247+00:00     t     432639        7   
19178   4356 2024-05-21 18:38:24.733806+00:00     t     269593        5   
19179  10086 2024-05-21 18:42:38.950318+00:00     t     269402        6   
19180    286 2024-05-21 18:38:22.461029+00:00     t     328579        4   

       scan_idx  unit_id  field  residual     score  id_ref  \
0             2     6883      6   7.41244   2.60806  335649   
1             4     9575      6   8.55708  -0.71490  194144   
2             5     8632      6   4.25055   7.87525  194144   
3             5     1526      2   5.82370   4.16608  517966   
4             3     2398      2   7.02217  -1.39408  224395   
...         ...      ...    ...       ...       ...     ...   
19176         7     3661      4   6.42422   7.30218  328140   
19177         3     9049      8   3.66317   8.00223  432639   
19178         7     8524      8   6.45214   9.54236  269593   
19179         7     8235      8   7.12704  12.27556  269402   
19180         7     3091      4   1.54712   9.23168  328579   

                           created_ref valid_ref      volume  \
0     2020-09-28 22:41:20.303372+00:00         t  295.861125   
1     2020-09-28 22:42:01.511773+00:00         t  213.307228   
2     2020-09-28 22:42:01.511773+00:00         t  213.307228   
3     2020-09-28 22:41:48.288009+00:00         t  313.318932   
4     2020-09-28 22:41:32.572651+00:00         t  329.448325   
...                                ...       ...         ...   
19176 2020-09-28 22:43:27.427858+00:00         t  111.254241   
19177 2020-09-28 22:45:25.114887+00:00         t  471.135846   
19178 2020-09-28 22:43:30.133113+00:00         t  317.925458   
19179 2020-09-28 22:41:42.679084+00:00         t  311.959552   
19180 2020-09-28 22:44:41.629225+00:00         t  273.746657   

         pt_supervoxel_id          pt_root_id              pt_position  \
0       93747454767483710  864691135702330235  [210784, 182032, 22673]   
1       83542405709639148  864691135614842827  [136400, 170640, 17951]   
2       83542405709639148  864691135614842827  [136400, 170640, 17951]   
3      107530794289274882  864691136966116814  [310944, 115888, 16752]   
4       85366977140498420  864691135686521271  [149840, 133152, 22592]   
...                   ...                 ...                      ...   
19176   93460413110868831  864691135698390426  [208704, 140592, 1
... [output truncated in report; full output in executed notebook]
```

### Code cell 8 (notebook cell 19, execution_count=8)

**Source**
```python
entry = matched_df.sample(1)
entry
```

**Output**

Output 1 (execute_result):
```text
id                          created valid  target_id  session  \
14079  13586 2024-05-21 18:42:40.864742+00:00     t     493095        7   

       scan_idx  unit_id  field  residual    score  id_ref  \
14079         5     7430      6   2.74568  6.65897  493095   

                           created_ref valid_ref      volume  \
14079 2020-09-28 22:44:52.030552+00:00         t  291.881779   

         pt_supervoxel_id          pt_root_id              pt_position  \
14079  104159279791435539  864691135762720822  [286528, 161712, 20332]   

      bb_start_position  bb_end_position  
14079   [nan, nan, nan]  [nan, nan, nan]
[text/html] .dataframe tbody tr th:only-of-type { vertical-align: middle; } .dataframe tbody tr th { vertical-align: top; } .dataframe thead th { text-align: right; } id created valid target_id session scan_idx unit_id field residual score id_ref created_ref valid_ref volume pt_supervoxel_id pt_root_id pt_position bb_start_position bb_end_position 14079 13586 2024-05-21 18:42:40.864742+00:00 t 493095 7 5 7430 6 2.74568 6.65897 493095 2020-09-28 22:44:52.030552+00:00 t 291.881779 104159279791435539 864691135762720822 [286528, 161712, 20332] [nan, nan, nan] [nan, nan, nan]
```

### Code cell 9 (notebook cell 20, execution_count=9)

**Source**
```python
segment = entry.pt_root_id.values[0] # get ID of segment to visualize
centroid = entry.pt_position.values[0] # get centroid of segment
```

**Output**

_No output_

### Code cell 10 (notebook cell 23, execution_count=10)

**Source**
```python
# generate links in Seung lab a custom Neuroglancer deployment called Neuromancer
from nglui import statebuilder, EasyViewer 

viewer = EasyViewer()
viewer.set_resolution((4,4,40))

em_layer = statebuilder.ImageLayerConfig(client.info.image_source(), 
                                         contrast_controls=True, black=0.35, white=0.7) # set EM layer 
seg_layer =  statebuilder.SegmentationLayerConfig(client.info.segmentation_source(),  
                                                  name='s
... [source truncated]
```

**Output**

Output 1 (execute_result):
```text
<IPython.core.display.HTML object>
[text/html] Neuroglancer Link
```

### Code cell 11 (notebook cell 26, execution_count=11)

**Source**
```python
from microns_phase3 import nda, utils
import numpy as np
import matplotlib.pyplot as plt
```

**Output**

Output 1 (stream):
```text
Connecting root@database:3306
```

### Code cell 12 (notebook cell 29, execution_count=12)

**Source**
```python
unit_key = entry[['session', 'scan_idx', 'unit_id']].to_dict(orient='records')[0]
unit_key
```

**Output**

Output 1 (execute_result):
```text
{'session': 7, 'scan_idx': 5, 'unit_id': 7430}
```

### Code cell 13 (notebook cell 32, execution_count=13)

**Source**
```python
nframes, fps = (nda.Scan & unit_key).fetch1('nframes', 'fps')  # fetch # frames and fps
time_axis = np.arange(nframes)/ fps # create time axis (seconds)
spike_trace = (nda.Activity & unit_key).fetch1('trace') # fetch spike trace
calcium_trace = (nda.ScanUnit * nda.Fluorescence & unit_key).fetch1('trace') # fetch calcium fluorescence trace
pupil_radius = (nda.ManualPupil & unit_key).fetch1('pupil_maj_r') # fetch manually segmented pupil trace 
treadmill = (nda.Treadmill & unit_key).fetch1('treadm
... [source truncated]
```

**Output**

_No output_

### Code cell 14 (notebook cell 33, execution_count=14)

**Source**
```python
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15, 8), sharex=True)
ax1.plot(time_axis, calcium_trace, color='g', alpha=0.3, label='calcium trace')
ax1.plot(time_axis, spike_trace, color='k', label='spike trace')
ax2.plot(time_axis, pupil_radius, color='k')
ax3.plot(time_axis, treadmill, color='k')
ax3.set_xlim(3000, 4000) 
ax1.set_ylabel('response magnitude')
ax1.legend()
ax2.set_ylabel('pupil radius')
ax3.set_ylabel('treadmill speed')
fig.suptitle(f'session: {unit_key["session"]}, scan_idx
... [source truncated]
```

**Output**

Output 1 (display_data):
```text
<Figure size 1500x800 with 3 Axes>
[image/png output, base64 length=150952]
```

### Code cell 15 (notebook cell 36, execution_count=15)

**Source**
```python
oracle_traces, score = utils.fetch_oracle_raster(unit_key)
```

**Output**

_No output_

### Code cell 16 (notebook cell 37, execution_count=16)

**Source**
```python
fig,axes = plt.subplots(1,6, figsize=(6,1),dpi=300)
for col,clip_trace in zip(axes,np.moveaxis(oracle_traces,1,0)):
    col.imshow(clip_trace,cmap='binary', interpolation='nearest')
    col.set_aspect('auto')
    col.set_xticks([])
    col.set_yticks([])
axes[0].set_ylabel(f'oracle score: {score:.2f}', fontsize=5)
fig.subplots_adjust(wspace=.05)
[ax.set_title(f'oracle clip {i+1}', fontsize=6) for i, ax in enumerate(axes)];
fig.suptitle(f'session: {unit_key["session"]}, scan_idx: {unit_key["scan_
... [source truncated]
```

**Output**

Output 1 (execute_result):
```text
Text(0.5, 1.2, 'session: 7, scan_idx: 5, unit_id: 7430')
```

Output 2 (display_data):
```text
<Figure size 1800x300 with 6 Axes>
[image/png output, base64 length=37552]
```

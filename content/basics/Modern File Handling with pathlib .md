---
title: Modern File Handling With Pathlib 
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from pathlib import Path

file_path = Path("source.txt")

file_path.write_text("Using pathlib module")
print(file_path.read_text())

print(file_path.exists())
print(file_path.parent)
```

    Using pathlib module
    True
    .



```python

```


---
**Score: 0**
---
title: Using Strptime() For File Data Processing
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from datetime import datetime

log_entry = "2025-11-24 10:15:00 - Server Started"
timestamp = log_entry.split(" - ")[0]

dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
print(dt)
```

    2025-11-24 10:15:00



```python

```


---
**Score: 0**
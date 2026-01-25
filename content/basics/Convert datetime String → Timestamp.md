---
title: Convert Datetime String → Timestamp
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from datetime import datetime

date_string = "2025-11-24 14:30:00"
dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
timestamp = dt.timestamp()

print(timestamp)
```

    1763974800.0



```python

```


---
**Score: 0**
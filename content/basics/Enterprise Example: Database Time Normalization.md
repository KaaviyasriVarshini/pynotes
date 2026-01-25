---
title: Enterprise Example: Database Time Normalization
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from datetime import datetime

def normalize_timestamp(input_value):
    if isinstance(input_value, (int, float)):
        return datetime.fromtimestamp(input_value)
    elif isinstance(input_value, str):
        dt = datetime.strptime(input_value, "%Y-%m-%d %H:%M:%S")
        return dt.timestamp()

print(normalize_timestamp(1732452305))
print(normalize_timestamp("2025-11-24 14:30:00"))
```

    2024-11-24 18:15:05
    1763974800.0



```python

```


---
**Score: 0**
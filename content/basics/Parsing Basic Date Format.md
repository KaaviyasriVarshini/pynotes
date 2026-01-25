---
title: Parsing Basic Date Format
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from datetime import datetime

date_string = "24/11/2025"
parsed = datetime.strptime(date_string, "%d/%m/%Y")
print(parsed)
```

    2025-11-24 00:00:00



```python

```


---
**Score: 0**
---
title: Combining Strptime() And Strftime()
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from datetime import datetime

raw = "2025/11/24"
dt = datetime.strptime(raw, "%Y/%m/%d")
formatted = dt.strftime("%d-%m-%Y")

print(formatted)  # 24-11-2025
```

    24-11-2025



```python

```


---
**Score: 0**
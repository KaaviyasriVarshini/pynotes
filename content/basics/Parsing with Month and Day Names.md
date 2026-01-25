---
title: Parsing With Month And Day Names
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from datetime import datetime

date_string = "Monday, November 24 2026"
dt = datetime.strptime(date_string, "%A, %B %d %Y")
print(dt)
```

    2026-11-24 00:00:00



```python

```


---
**Score: 0**
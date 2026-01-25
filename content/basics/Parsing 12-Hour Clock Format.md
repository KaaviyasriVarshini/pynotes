---
title: Parsing 12-Hour Clock Format
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from datetime import datetime

time_string = "07:30 PM"
dt = datetime.strptime(time_string, "%I:%M %p")
print(dt.time())
```

    19:30:00



```python

```


---
**Score: 0**
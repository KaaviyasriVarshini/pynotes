---
title: Enterprise Logging Example
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from datetime import datetime

def log_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {event}")

log_event("Server Started")
log_event("User Login Successful")
```

    [2026-01-17 20:23:12] Server Started
    [2026-01-17 20:23:12] User Login Successful



```python

```


---
**Score: 0**
---
title: Enterprise Use Case: Log Timestamp  
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from datetime import datetime

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

log_message("Server started")
log_message("User authenticated")
```

    [2026-01-17 19:30:12] Server started
    [2026-01-17 19:30:12] User authenticated



```python

```


---
**Score: 0**
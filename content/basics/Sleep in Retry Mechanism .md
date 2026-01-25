---
title: Sleep In Retry Mechanism 
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import time

def retry_operation():
    for attempt in range(3):
        print("Attempt", attempt + 1)
        time.sleep(2)

retry_operation()
```

    Attempt 1
    Attempt 2
    Attempt 3



```python

```


---
**Score: 0**
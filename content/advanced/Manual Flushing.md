---
title: Manual Flushing
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import sys, time

for i in range(5):
    sys.stdout.write(f"Step {i}\n")
    sys.stdout.flush()
    time.sleep(1)
```

    Step 0
    Step 1
    Step 2
    Step 3
    Step 4



```python

```


---
**Score: 0**
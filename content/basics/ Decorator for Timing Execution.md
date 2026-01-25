---
title:  Decorator For Timing Execution
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Execution Time:", time.time() - start)
        return result
    return wrapper

@timer
def process():
    for _ in range(1000000):
        pass

process()
```

    Execution Time: 0.014469146728515625



```python

```


---
**Score: 0**
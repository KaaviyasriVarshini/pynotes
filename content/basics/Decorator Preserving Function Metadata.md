---
title: Decorator Preserving Function Metadata
date: 2026-03-04
author: Your Name
cell_count: 2
score: 0
---

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```


```python

```


---
**Score: 0**
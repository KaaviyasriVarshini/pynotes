---
title: Optimizing Recursion With Memoization
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(30))  # Optimized recursion
```

    832040



```python

```


---
**Score: 0**
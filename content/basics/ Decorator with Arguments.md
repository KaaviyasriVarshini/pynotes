---
title:  Decorator With Arguments
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def add(a, b):
    return a + b

print(add(5, 3))
```

    Arguments: (5, 3) {}
    8



```python

```


---
**Score: 0**
---
title: Class-Based Decorator
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Calling function...")
        return self.func(*args, **kwargs)

@Logger
def show():
    print("Processing data")

show()
```

    Calling function...
    Processing data



```python

```


---
**Score: 0**
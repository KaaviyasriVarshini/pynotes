---
title: Decorator With Parameters 
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello")

greet()
```

    Hello
    Hello
    Hello



```python

```


---
**Score: 0**
---
title: Decorator With Return Value
date: 2026-03-04
author: Your Name
cell_count: 2
score: 0
---

```python
def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase
def message():
    return "hello world"

print(message())
```

    HELLO WORLD



```python

```


---
**Score: 0**
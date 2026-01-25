---
title:  Inspecting Closure Variables
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def outer():
    value = 42

    def inner():
        return value

    return inner

func = outer()
print(func.__closure__[0].cell_contents)  # 42

```

    42



```python

```


---
**Score: 0**
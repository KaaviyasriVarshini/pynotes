---
title: Legb Rule (Scope Resolution Order)
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print(x)

    inner()

outer()
```

    Local



```python

```


---
**Score: 0**
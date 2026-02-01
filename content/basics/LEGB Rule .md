---
title: Legb Rule 
date: 2026-02-01
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
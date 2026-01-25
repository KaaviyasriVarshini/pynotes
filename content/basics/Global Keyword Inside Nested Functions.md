---
title: Global Keyword Inside Nested Functions
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
x = 100

def outer():
    def inner():
        global x
        x = 200

    inner()

outer()
print(x)  # Output: 200
```

    200



```python

```


---
**Score: 0**
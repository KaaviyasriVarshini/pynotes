---
title: Using The Nonlocal Keyword
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)

    inner()
    inner()

outer()
```

    1
    2



```python

```


---
**Score: 0**
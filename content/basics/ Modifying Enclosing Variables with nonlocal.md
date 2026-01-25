---
title:  Modifying Enclosing Variables With Nonlocal
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def counter():
    value = 0
    def increment():
        nonlocal value
        value += 1
        return value
    return increment

count = counter()
print(count())
print(count())
```

    1
    2



```python

```


---
**Score: 0**
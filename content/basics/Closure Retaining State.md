---
title: Closure Retaining State
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = counter()
print(c())  # 1
print(c())  # 2
```

    1
    2



```python

```


---
**Score: 0**
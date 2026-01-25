---
title: Argument Unpacking
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def multiply(a, b, c):
    return a * b * c

values = (2, 3, 4)
print(multiply(*values))  # Output: 24

data = {"a": 1, "b": 2, "c": 3}
print(multiply(**data))   # Output: 6
```

    24
    6



```python

```


---
**Score: 0**
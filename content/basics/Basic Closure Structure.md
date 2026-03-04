---
title: Basic Closure Structure
date: 2026-03-04
author: Your Name
cell_count: 2
score: 0
---

```python
def multiplier(x):
    def multiply(y):
        return x * y
    return multiply

times2 = multiplier(2)
print(times2(5))  # Output: 10
```

    10



```python

```


---
**Score: 0**
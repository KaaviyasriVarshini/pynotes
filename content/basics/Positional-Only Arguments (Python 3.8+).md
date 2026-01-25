---
title: Positional-Only Arguments (Python 3.8+)
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def divide(a, b, /):
    return a / b

print(divide(10, 2))
# divide(a=10, b=2)  # Raises TypeError

```

    5.0



```python

```


---
**Score: 0**
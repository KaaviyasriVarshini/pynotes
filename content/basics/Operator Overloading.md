---
title: Operator Overloading
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Vector:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Vector(self.x + other.x)

v1 = Vector(10)
v2 = Vector(20)
v3 = v1 + v2

print(v3.x)  # Output: 30
```

    30



```python

```


---
**Score: 0**
---
title: Overloading Division Operator
date: 2026-02-01
author: Your Name
cell_count: 2
score: 0
---

```python
class Calculator:
    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        return self.value / other.value

c1 = Calculator(100)
c2 = Calculator(4)

print(c1 / c2)  # Output: 25.0
```

    25.0



```python

```


---
**Score: 0**
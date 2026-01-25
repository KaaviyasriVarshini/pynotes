---
title: Overloading In-Place Operators (+=)
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Counter:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other
        return self

c = Counter(10)
c += 5
print(c.value)  # Output: 15
```

    15



```python

```


---
**Score: 0**
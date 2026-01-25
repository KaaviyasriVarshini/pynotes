---
title: Read-Only Property
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.area)
```

    78.5



```python

```


---
**Score: 0**
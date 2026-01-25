---
title: Computed Property Example 
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

rect = Rectangle(10, 5)
print(rect.area)  # 50
```

    50



```python

```


---
**Score: 0**
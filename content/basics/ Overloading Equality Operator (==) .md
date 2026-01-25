---
title:  Overloading Equality Operator (==) 
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Point:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

p1 = Point(5)
p2 = Point(5)

print(p1 == p2)  # True
```

    True



```python

```


---
**Score: 0**
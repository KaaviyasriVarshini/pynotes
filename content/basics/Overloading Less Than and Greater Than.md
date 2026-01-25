---
title: Overloading Less Than And Greater Than
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Score:
    def __init__(self, marks):
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __gt__(self, other):
        return self.marks > other.marks

s1 = Score(85)
s2 = Score(70)

print(s1 > s2)  # True
```

    True



```python

```


---
**Score: 0**
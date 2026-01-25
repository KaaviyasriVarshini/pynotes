---
title: What Is Operator Overloading
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)  # Output: 30
```

    30



```python

```


---
**Score: 0**
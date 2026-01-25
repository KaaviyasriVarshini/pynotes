---
title: Comprehensive Operator Overloading Example
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class ComplexNumber:
    def __init__(self, real):
        self.real = real

    def __add__(self, other):
        return ComplexNumber(self.real + other.real)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real)

    def __str__(self):
        return str(self.real)

c1 = ComplexNumber(10)
c2 = ComplexNumber(3)

print(c1 + c2)  # 13
print(c1 - c2)  # 7
```

    13
    7



```python

```


---
**Score: 0**
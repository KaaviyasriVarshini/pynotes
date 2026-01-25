---
title: Method Overloading Via Default Arguments
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Calculator:
    def multiply(self, a, b=1):
        return a * b

calc = Calculator()
print(calc.multiply(5))     # 5
print(calc.multiply(5, 3))  # 15
```

    5
    15



```python

```


---
**Score: 0**
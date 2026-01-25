---
title: Nonlocal In Closures 
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def power(base):
    exponent = 2

    def calculate():
        nonlocal exponent
        exponent += 1
        return base ** exponent

    return calculate

p = power(2)
print(p())
print(p())
```

    8
    16



```python

```


---
**Score: 0**
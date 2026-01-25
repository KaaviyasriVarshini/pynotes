---
title: Practical Example Of Scope Management
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
total = 100

def calculate():
    total = 50

    def adjust():
        nonlocal total
        total += 10

    adjust()
    return total

print(calculate())  # Output: 60
print(total)        # Output: 100
```

    60
    100



```python

```


---
**Score: 0**
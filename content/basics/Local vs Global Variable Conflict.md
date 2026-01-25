---
title: Local Vs Global Variable Conflict
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
value = 50

def update():
    value = 10  # Local variable shadows global
    print("Inside function:", value)

update()
print("Outside function:", value)
```

    Inside function: 10
    Outside function: 50



```python

```


---
**Score: 0**
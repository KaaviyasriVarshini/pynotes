---
title: Difference Between Global And Nonlocal
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
x = 50

def outer():
    x = 10
    
    def inner():
        global x
        x = 99

    inner()
    print("Outer x:", x)

outer()
print("Global x:", x)
```

    Outer x: 10
    Global x: 99



```python

```


---
**Score: 0**
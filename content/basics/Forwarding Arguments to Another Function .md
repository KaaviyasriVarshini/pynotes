---
title: Forwarding Arguments To Another Function 
date: 2026-02-11
author: Your Name
cell_count: 2
score: 0
---

```python
def wrapper(*args, **kwargs):
    return calculate(*args, **kwargs)

def calculate(a, b):
    return a + b

print(wrapper(5, 10))
```

    15



```python

```


---
**Score: 0**
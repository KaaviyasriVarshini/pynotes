---
title: Closure Vs Global Variable
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
factor = 10

def using_global():
    return lambda x: x * factor

def using_closure():
    factor = 10
    return lambda x: x * factor

print(using_closure()(5))
```

    50



```python

```


---
**Score: 0**
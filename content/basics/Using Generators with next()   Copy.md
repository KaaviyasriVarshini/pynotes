---
title: Using Generators With Next()   Copy
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def alpha_generator():
    yield "A"
    yield "B"
    yield "C"

gen = alpha_generator()
print(next(gen))
print(next(gen))
```

    A
    B



```python

```


---
**Score: 0**
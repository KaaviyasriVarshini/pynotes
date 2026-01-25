---
title: Generator Vs Normal Function
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def normal_function():
    return 10
    return 20

def generator_function():
    yield 10
    yield 20

print(normal_function())          # 10
print(list(generator_function())) # [10, 20]
```

    10
    [10, 20]



```python

```


---
**Score: 0**
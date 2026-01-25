---
title: Memory Efficiency Of Generators
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def large_numbers():
    for i in range(1000000):
        yield i

gen = large_numbers()
print(next(gen))
print(next(gen))
```

    0
    1



```python

```


---
**Score: 0**
---
title: Generator State Preservation
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def demo():
    print("Start")
    yield 1
    print("Resume")
    yield 2

g = demo()
print(next(g))
print(next(g))
```

    Start
    1
    Resume
    2



```python

```


---
**Score: 0**
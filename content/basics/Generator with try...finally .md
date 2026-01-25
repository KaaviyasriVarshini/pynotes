---
title: Generator With Try...Finally 
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def resource_handler():
    try:
        yield "Using resource"
    finally:
        print("Resource released")

gen = resource_handler()
print(next(gen))
#gen.close()
```

    Using resource



```python

```


---
**Score: 0**
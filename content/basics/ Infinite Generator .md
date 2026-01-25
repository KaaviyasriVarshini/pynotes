---
title:  Infinite Generator 
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1

counter = infinite_counter()
print(next(counter))
print(next(counter))
```

    1
    2



```python

```


---
**Score: 0**
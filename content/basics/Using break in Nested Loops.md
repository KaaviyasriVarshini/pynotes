---
title: Using Break In Nested Loops
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
for i in range(3):
    for j in range(5):
        if j == 2:
            break
        print(f"i={i}, j={j}")
```

    i=0, j=0
    i=0, j=1
    i=1, j=0
    i=1, j=1
    i=2, j=0
    i=2, j=1



```python

```


---
**Score: 0**
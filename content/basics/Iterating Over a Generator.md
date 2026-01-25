---
title: Iterating Over A Generator
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def count_up(n):
    for i in range(1, n + 1):
        yield i

for num in count_up(5):
    print(num)
```

    1
    2
    3
    4
    5



```python

```


---
**Score: 0**
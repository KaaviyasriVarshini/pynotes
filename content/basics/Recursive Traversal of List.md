---
title: Recursive Traversal Of List
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def print_list(lst):
    if not lst:
        return
    print(lst[0])
    print_list(lst[1:])

print_list([1, 2, 3, 4])

```

    1
    2
    3
    4



```python

```


---
**Score: 0**
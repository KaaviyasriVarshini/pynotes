---
title: Lambda In List Comprehension Context 
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
multipliers = [(lambda x: x * n) for n in range(1, 4)]

print(multipliers)  # Output: 5
print(multipliers)  # Output: 10
```

    [<function <listcomp>.<lambda> at 0x7fb240369f80>, <function <listcomp>.<lambda> at 0x7fb24036a020>, <function <listcomp>.<lambda> at 0x7fb24036a0c0>]
    [<function <listcomp>.<lambda> at 0x7fb240369f80>, <function <listcomp>.<lambda> at 0x7fb24036a020>, <function <listcomp>.<lambda> at 0x7fb24036a0c0>]



```python

```


---
**Score: 0**
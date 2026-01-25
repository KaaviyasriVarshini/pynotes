---
title: **Keyword Variable-Length Arguments (Kwargs)
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def display_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_profile(name="Alice", role="Engineer")
```

    name: Alice
    role: Engineer



```python

```


---
**Score: 0**
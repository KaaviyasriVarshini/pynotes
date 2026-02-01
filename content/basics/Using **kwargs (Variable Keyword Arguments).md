---
title: Using **Kwargs (Variable Keyword Arguments)
date: 2026-02-01
author: Your Name
cell_count: 2
score: 0
---

```python
def display_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_profile(name="Alice", role="Engineer", location="Toronto")
```

    name: Alice
    role: Engineer
    location: Toronto



```python

```


---
**Score: 0**
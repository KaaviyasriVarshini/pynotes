---
title: Enclosing Scope (Nested Functions)
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def outer():
    message = "Hello"

    def inner():
        print(message)  # Accessing enclosing variable

    inner()

outer()
```

    Hello



```python

```


---
**Score: 0**
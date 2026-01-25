---
title: Nested Exception Handling
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
try:
    try:
        x = int("abc")
    except ValueError:
        print("Inner exception handled")
except Exception:
    print("Outer exception handler")
```

    Inner exception handled



```python

```


---
**Score: 0**
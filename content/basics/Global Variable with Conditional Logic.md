---
title: Global Variable With Conditional Logic
date: 2026-03-04
author: Your Name
cell_count: 2
score: 0
---

```python
mode = "light"

def toggle_mode():
    global mode
    if mode == "light":
        mode = "dark"
    else:
        mode = "light"

toggle_mode()
print(mode)  # Output: dark
```

    dark



```python

```


---
**Score: 0**
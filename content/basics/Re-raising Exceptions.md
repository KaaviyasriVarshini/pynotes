---
title: Re-Raising Exceptions
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
try:
    value = int("xyz")
except ValueError:
    print("Logging error before re-raising")
    raise
```

    Logging error before re-raising



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[3], line 2
          1 try:
    ----> 2     value = int("xyz")
          3 except ValueError:
          4     print("Logging error before re-raising")


    ValueError: invalid literal for int() with base 10: 'xyz'



```python

```


---
**Score: 0**
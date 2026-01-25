---
title: Assertions Vs Exception Handling
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
# Assertion
assert x != 0, "x must not be zero"

# Exception
if x == 0:
    raise ValueError("x must not be zero")
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[1], line 2
          1 # Assertion
    ----> 2 assert x != 0, "x must not be zero"
          4 # Exception
          5 if x == 0:


    NameError: name 'x' is not defined



```python

```


---
**Score: 0**
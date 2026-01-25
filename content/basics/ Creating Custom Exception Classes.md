---
title:  Creating Custom Exception Classes
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class NegativeNumberError(Exception):
    pass

def check_number(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed")

check_number(-3)
```


    ---------------------------------------------------------------------------

    NegativeNumberError                       Traceback (most recent call last)

    Cell In[3], line 8
          5     if n < 0:
          6         raise NegativeNumberError("Negative numbers are not allowed")
    ----> 8 check_number(-3)


    Cell In[3], line 6, in check_number(n)
          4 def check_number(n):
          5     if n < 0:
    ----> 6         raise NegativeNumberError("Negative numbers are not allowed")


    NegativeNumberError: Negative numbers are not allowed



```python

```


---
**Score: 0**
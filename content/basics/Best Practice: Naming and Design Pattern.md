---
title: Best Practice: Naming And Design Pattern
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class InvalidOrderStateError(Exception):
    """Raised when an order is in an invalid processing state"""
    pass

def process_order(status):
    if status != "confirmed":
        raise InvalidOrderStateError("Order must be confirmed before processing")

process_order("draft")
```


    ---------------------------------------------------------------------------

    InvalidOrderStateError                    Traceback (most recent call last)

    Cell In[1], line 9
          6     if status != "confirmed":
          7         raise InvalidOrderStateError("Order must be confirmed before processing")
    ----> 9 process_order("draft")


    Cell In[1], line 7, in process_order(status)
          5 def process_order(status):
          6     if status != "confirmed":
    ----> 7         raise InvalidOrderStateError("Order must be confirmed before processing")


    InvalidOrderStateError: Order must be confirmed before processing



```python

```


---
**Score: 0**
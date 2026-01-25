---
title: Custom Exception With Additional Attributes
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class TransactionError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(f"[{code}] {message}")

raise TransactionError(403, "Unauthorized action")
```


    ---------------------------------------------------------------------------

    TransactionError                          Traceback (most recent call last)

    Cell In[1], line 7
          4         self.message = message
          5         super().__init__(f"[{code}] {message}")
    ----> 7 raise TransactionError(403, "Unauthorized action")


    TransactionError: [403] Unauthorized action



```python

```


---
**Score: 0**
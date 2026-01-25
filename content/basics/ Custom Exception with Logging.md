---
title:  Custom Exception With Logging
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class DataValidationError(Exception):
    pass

try:
    raise DataValidationError("Invalid CSV column format")
except DataValidationError as e:
    print("Validation Error Logged:", e)
```

    Validation Error Logged: Invalid CSV column format



```python

```


---
**Score: 0**
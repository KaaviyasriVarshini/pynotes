---
title: Creating Hierarchy Of Custom Exceptions
date: 2026-02-01
author: Your Name
cell_count: 2
score: 0
---

```python
class ApplicationError(Exception):
    pass

class DatabaseError(ApplicationError):
    pass

class NetworkError(ApplicationError):
    pass
```


```python

```


---
**Score: 0**
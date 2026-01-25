---
title:  Catching Custom Exceptions
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class AuthenticationError(Exception):
    pass

try:
    raise AuthenticationError("Invalid credentials")
except AuthenticationError as e:
    print("Login failed:", e)
```

    Login failed: Invalid credentials



```python

```


---
**Score: 0**
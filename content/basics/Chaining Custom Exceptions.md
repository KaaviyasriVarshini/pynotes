---
title: Chaining Custom Exceptions
date: 2026-02-01
author: Your Name
cell_count: 2
score: 0
---

```python
class InitialError(Exception):
    pass

class DerivedError(Exception):
    pass

try:
    try:
        raise InitialError("Initial failure")
    except InitialError as e:
        raise DerivedError("Follow-up failure") from e
except DerivedError as final_error:
    print(final_error)
```

    Follow-up failure



```python

```


---
**Score: 0**
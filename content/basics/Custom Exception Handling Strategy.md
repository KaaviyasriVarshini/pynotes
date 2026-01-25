---
title: Custom Exception Handling Strategy
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")

try:
    validate_age(16)
except InvalidAgeError as e:
    print(e)
```

    Age must be 18 or above



```python

```


---
**Score: 0**
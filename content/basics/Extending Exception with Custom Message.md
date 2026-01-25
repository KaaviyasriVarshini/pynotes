---
title: Extending Exception With Custom Message
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class AgeLimitError(Exception):
    def __init__(self, age):
        super().__init__(f"Age {age} is below allowed limit")

def validate_age(age):
    if age < 18:
        raise AgeLimitError(age)

validate_age(15)
```


    ---------------------------------------------------------------------------

    AgeLimitError                             Traceback (most recent call last)

    Cell In[1], line 9
          6     if age < 18:
          7         raise AgeLimitError(age)
    ----> 9 validate_age(15)


    Cell In[1], line 7, in validate_age(age)
          5 def validate_age(age):
          6     if age < 18:
    ----> 7         raise AgeLimitError(age)


    AgeLimitError: Age 15 is below allowed limit



```python

```


---
**Score: 0**
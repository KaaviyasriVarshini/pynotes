---
title: Raising Custom Exceptions
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

validate_age(-5)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[4], line 5
          2     if age < 0:
          3         raise ValueError("Age cannot be negative")
    ----> 5 validate_age(-5)


    Cell In[4], line 3, in validate_age(age)
          1 def validate_age(age):
          2     if age < 0:
    ----> 3         raise ValueError("Age cannot be negative")


    ValueError: Age cannot be negative



```python

```


---
**Score: 0**
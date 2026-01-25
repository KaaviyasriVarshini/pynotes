---
title: Best Practice: Structured Exception Handling
date: 2026-01-25
author: Your Name
cell_count: 3
score: 0
---

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero error"
    except TypeError:
        return "Invalid input type"

print(divide(10, 0))
```

    Division by zero error



```python

```


```python

```


---
**Score: 0**
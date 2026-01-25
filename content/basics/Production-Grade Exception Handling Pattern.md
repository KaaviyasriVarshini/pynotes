---
title: Production-Grade Exception Handling Pattern
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"
    finally:
        print("Operation attempted")

print(safe_divide(10, 0))
```

    Operation attempted
    Error: division by zero



```python

```


---
**Score: 0**
---
title: Converting User Input Safely
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from datetime import datetime

user_input = "15-06-2025"

try:
    parsed_date = datetime.strptime(user_input, "%d-%m-%Y")
    print("Valid date:", parsed_date)
except ValueError:
    print("Invalid date format")
```

    Valid date: 2025-06-15 00:00:00



```python

```


---
**Score: 0**
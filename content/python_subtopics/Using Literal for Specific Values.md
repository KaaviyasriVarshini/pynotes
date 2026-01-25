---
title: Using Literal For Specific Values
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from typing import Literal

def choose_plan(plan: Literal["free", "premium", "enterprise"]) -> str:
    return f"You selected the {plan} plan."

print(choose_plan("premium"))  # Output: You selected the premium plan.
```

    You selected the premium plan.



```python

```


---
**Score: 0**
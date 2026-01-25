---
title:  Type Hint For Dictionaries
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from typing import Dict

def count_fruits(fruit_counts: Dict[str, int]) -> int:
    return sum(fruit_counts.values())

fruits = {"apple": 5, "banana": 3, "orange": 2}
print(count_fruits(fruits))  # Output: 10
```

    10



```python

```


---
**Score: 0**
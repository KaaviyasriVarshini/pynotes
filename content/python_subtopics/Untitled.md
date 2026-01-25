---
title: Untitled
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from typing import Union

def square_or_length(value: Union[int, str]) -> int:
    if isinstance(value, int):
        return value ** 2
    return len(value)

print(square_or_length(4))       # Output: 16
print(square_or_length("test"))  # Output: 4
```

    16
    4



```python

```


---
**Score: 0**
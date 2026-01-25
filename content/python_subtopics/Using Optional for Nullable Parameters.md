---
title: Using Optional For Nullable Parameters
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if name:
        return f"Hello, {name}!"
    return "Hello, Guest!"

print(greet())           # Output: Hello, Guest!
print(greet("Alice"))    # Output: Hello, Alice!
```

    Hello, Guest!
    Hello, Alice!



```python

```


---
**Score: 0**
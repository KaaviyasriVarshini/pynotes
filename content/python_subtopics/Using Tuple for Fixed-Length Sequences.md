---
title: Using Tuple For Fixed-Length Sequences
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from typing import Tuple

def process_coordinates(coords: Tuple[float, float]) -> str:
    return f"Latitude: {coords[0]}, Longitude: {coords[1]}"

print(process_coordinates((40.7128, -74.0060)))
# Output: Latitude: 40.7128, Longitude: -74.006
```

    Latitude: 40.7128, Longitude: -74.006



```python

```


---
**Score: 0**
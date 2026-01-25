---
title:  Lambda With Reduce()
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from functools import reduce

numbers = [1, 2, 3, 4]

total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 10
```

    10



```python

```


---
**Score: 0**
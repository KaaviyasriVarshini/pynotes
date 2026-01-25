---
title: Best Practice: Encapsulation Instead Of Global
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

counter = Counter()
counter.increment()
print(counter.value)  # Output: 1
```

    1



```python

```


---
**Score: 0**
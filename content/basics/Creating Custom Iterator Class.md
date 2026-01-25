---
title: Creating Custom Iterator Class
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class CountUp:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        raise StopIteration

counter = CountUp(3)

for number in counter:
    print(number)
```

    1
    2
    3



```python

```


---
**Score: 0**
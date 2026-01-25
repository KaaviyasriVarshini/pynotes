---
title:  Infinite Iterator Example
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class InfiniteNumbers:
    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        self.num += 1
        return self.num
```


```python

```


---
**Score: 0**
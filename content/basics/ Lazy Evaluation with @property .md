---
title:  Lazy Evaluation With @Property 
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class DataLoader:
    def __init__(self):
        self._data = None

    @property
    def data(self):
        if self._data is None:
            print("Loading data...")
            self._data = [1, 2, 3]
        return self._data

loader = DataLoader()
print(loader.data)
print(loader.data)
```

    Loading data...
    [1, 2, 3]
    [1, 2, 3]



```python

```


---
**Score: 0**
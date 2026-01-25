---
title: Order Of Parameters
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def example(a, b, *args, c=10, **kwargs):
    print(a, b, args, c, kwargs)

example(1, 2, 3, 4, key="value")
```

    1 2 (3, 4) 10 {'key': 'value'}



```python

```


---
**Score: 0**
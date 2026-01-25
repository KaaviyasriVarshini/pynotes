---
title: Combining *Args And **Kwargs
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def process_data(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

process_data(10, 20, user="Kaaviya", status="Active")
```

    Positional: (10, 20)
    Keyword: {'user': 'Kaaviya', 'status': 'Active'}



```python

```


---
**Score: 0**
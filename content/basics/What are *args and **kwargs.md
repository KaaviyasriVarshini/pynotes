---
title: What Are *Args And **Kwargs
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def demo(*args, **kwargs):
    print(args)
    print(kwargs)

demo(1, 2, 3, name="Alice", age=30)
```

    (1, 2, 3)
    {'name': 'Alice', 'age': 30}



```python

```


---
**Score: 0**
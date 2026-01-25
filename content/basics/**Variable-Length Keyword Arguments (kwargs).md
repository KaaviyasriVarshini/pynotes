---
title: **Variable-Length Keyword Arguments (Kwargs)
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def user_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

user_profile(name="Alice", role="Developer", level="Senior")
```

    name: Alice
    role: Developer
    level: Senior



```python

```


---
**Score: 0**
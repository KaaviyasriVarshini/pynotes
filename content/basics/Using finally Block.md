---
title: Using Finally Block
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")
```

    File not found
    Execution completed



```python

```


---
**Score: 0**
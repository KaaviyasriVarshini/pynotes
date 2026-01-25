---
title:  Using Try...Except...Finally
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
    print("Cleanup operations executed")
```

    File not found
    Cleanup operations executed



```python

```


---
**Score: 0**
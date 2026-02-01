---
title: Tracking State Using Global Variable
date: 2026-02-01
author: Your Name
cell_count: 2
score: 0
---

```python
requests = 0

def handle_request():
    global requests
    requests += 1

handle_request()
handle_request()
print(requests)  # Output: 2
```

    2



```python

```


---
**Score: 0**
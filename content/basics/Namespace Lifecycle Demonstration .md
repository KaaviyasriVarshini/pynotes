---
title: Namespace Lifecycle Demonstration 
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
x = "Global"

def test():
    x = "Local"
    print("Inside:", x)

test()
print("Outside:", x)
```

    Inside: Local
    Outside: Global



```python

```


---
**Score: 0**
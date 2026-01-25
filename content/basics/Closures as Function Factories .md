---
title: Closures As Function Factories 
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def logger(prefix):
    def log(message):
        print(f"{prefix}: {message}")
    return log

info_logger = logger("INFO")
error_logger = logger("ERROR")

info_logger("System started")
error_logger("System failed")
```

    INFO: System started
    ERROR: System failed



```python

```


---
**Score: 0**
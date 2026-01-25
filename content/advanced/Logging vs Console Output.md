---
title: Logging Vs Console Output
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import logging, sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

logging.info("Starting job")
print("result-data-json-here")  # Data to stdout
```

    INFO:root:Starting job


    result-data-json-here



```python

```


---
**Score: 0**
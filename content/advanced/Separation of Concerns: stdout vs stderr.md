---
title: Separation Of Concerns: Stdout Vs Stderr
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import sys

def main():
    for line in sys.stdin:
        # business output
        sys.stdout.write(line.upper())
    sys.stderr.write("Processing complete\n")
```


```python

```


---
**Score: 0**
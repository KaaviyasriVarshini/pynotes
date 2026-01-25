---
title: Replacing And Wrapping Sys.Stdout  Sys.Stdin
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import sys
from io import TextIOBase

class PrefixWriter(TextIOBase):
    def __init__(self, original, prefix):
        self.original = original
        self.prefix = prefix

    def write(self, s):
        return self.original.write(self.prefix + s)

sys.stdout = PrefixWriter(sys.stdout, "[APP] ")
print("Started")  # Outputs: [APP] Started
```

    [APP] Started[APP] 



```python

```


---
**Score: 0**
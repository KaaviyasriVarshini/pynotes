---
title: Testing Console I-O
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def process_stream(inp, out):
    for line in inp:
        out.write(line.upper())

# In production
import sys
process_stream(sys.stdin, sys.stdout)

# In tests
from io import StringIO
inp = StringIO("hello\nworld\n")
out = StringIO()
process_stream(inp, out)
assert out.getvalue() == "HELLO\nWORLD\n"
```


```python

```


---
**Score: 0**
---
title: Metacharacters And Special Sequences
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import re

text = "Email: test123@gmail.com"
pattern = r"\w+@\w+\.\w+"

match = re.search(pattern, text)
print(match.group())
```

    test123@gmail.com



```python

```


---
**Score: 0**
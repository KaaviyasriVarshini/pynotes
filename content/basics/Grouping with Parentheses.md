---
title: Grouping With Parentheses
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import re

text = "John Doe"
pattern = r"(John) (Doe)"

match = re.search(pattern, text)
print(match.groups())  # ('John', 'Doe')
```

    ('John', 'Doe')



```python

```


---
**Score: 0**
---
title: Recursive String Reversal
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def reverse_string(text):
    if len(text) == 0:
        return text
    return reverse_string(text[1:]) + text[0]

print(reverse_string("Python"))  # Output: nohtyP
```

    nohtyP



```python

```


---
**Score: 0**
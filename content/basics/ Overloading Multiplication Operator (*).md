---
title:  Overloading Multiplication Operator (*)
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Repeater:
    def __init__(self, text):
        self.text = text

    def __mul__(self, times):
        return self.text * times

r = Repeater("AI ")
print(r * 3)  # Output: AI AI AI 
```

    AI AI AI 



```python

```


---
**Score: 0**
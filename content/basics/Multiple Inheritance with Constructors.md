---
title: Multiple Inheritance With Constructors
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class A:
    def __init__(self):
        print("Constructor A")

class B:
    def __init__(self):
        print("Constructor B")

class C(A, B):
    def __init__(self):
        super().__init__()

c = C()
```

    Constructor A



```python

```


---
**Score: 0**
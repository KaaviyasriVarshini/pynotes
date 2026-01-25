---
title: Cooperative Multiple Inheritance Using Super()
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class A:
    def __init__(self):
        print("A init")
        super().__init__()

class B:
    def __init__(self):
        print("B init")
        super().__init__()

class C(A, B):
    def __init__(self):
        print("C init")
        super().__init__()

c = C()
```

    C init
    A init
    B init



```python

```


---
**Score: 0**
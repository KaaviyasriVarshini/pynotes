---
title: Understanding Method Resolution Order (Mro)
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

print(C.mro())
```

    [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]



```python

```


---
**Score: 0**
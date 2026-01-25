---
title:  Method Resolution Order (Mro)
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(B):
    pass

c = C()
c.show()
print(C.mro())
```

    B
    [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]



```python

```


---
**Score: 0**
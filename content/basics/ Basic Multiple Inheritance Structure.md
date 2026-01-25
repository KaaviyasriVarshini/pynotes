---
title:  Basic Multiple Inheritance Structure
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class A:
    def show_a(self):
        print("Class A")

class B:
    def show_b(self):
        print("Class B")

class C(A, B):
    pass

obj = C()
obj.show_a()
obj.show_b()
```

    Class A
    Class B



```python

```


---
**Score: 0**
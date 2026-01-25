---
title: Multilevel Inheritance
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Grandparent:
    def feature(self):
        print("Grandparent feature")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

c = Child()
c.feature()
```

    Grandparent feature



```python

```


---
**Score: 0**
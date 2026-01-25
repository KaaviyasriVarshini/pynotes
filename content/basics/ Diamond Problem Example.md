---
title:  Diamond Problem Example
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Grandparent:
    def greet(self):
        print("Hello from Grandparent")

class Parent1(Grandparent):
    pass

class Parent2(Grandparent):
    pass

class Child(Parent1, Parent2):
    pass

c = Child()
c.greet()
```

    Hello from Grandparent



```python

```


---
**Score: 0**
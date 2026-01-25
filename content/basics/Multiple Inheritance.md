---
title: Multiple Inheritance
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Father:
    def skill(self):
        print("Driving")

class Mother:
    def talent(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill()
c.talent()
```

    Driving
    Cooking



```python

```


---
**Score: 0**
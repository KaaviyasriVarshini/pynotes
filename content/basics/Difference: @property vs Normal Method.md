---
title: Difference: @Property Vs Normal Method
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class User:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    @property
    def name(self):
        return self._name

u = User("Bob")
print(u.get_name())  # Method call
print(u.name)        # Property access
```

    Bob
    Bob



```python

```


---
**Score: 0**
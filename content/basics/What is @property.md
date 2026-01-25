---
title: What Is @Property
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

p = Person("Alice")
print(p.name)  # Alice
```

    Alice



```python

```


---
**Score: 0**
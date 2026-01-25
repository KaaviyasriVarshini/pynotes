---
title: Constructor Inheritance
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

c = Child("Alice", 25)
print(c.name, c.age)
```

    Alice 25



```python

```


---
**Score: 0**
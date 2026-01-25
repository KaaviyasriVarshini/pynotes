---
title: Abstract Base Class Polymorphism
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return 10 * 5

shape = Rectangle()
print(shape.area())
```

    50



```python

```


---
**Score: 0**
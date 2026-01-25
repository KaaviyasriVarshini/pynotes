---
title: Using @Property With Setter
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

e = Employee(5000)
e.salary = 6000
print(e.salary)
```

    6000



```python

```


---
**Score: 0**
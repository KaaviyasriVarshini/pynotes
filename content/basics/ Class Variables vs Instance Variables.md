---
title:  Class Variables Vs Instance Variables
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Student:
    school = "Global Academy"  # Class variable

    def __init__(self, name):
        self.name = name        # Instance variable

s1 = Student("Alice")
s2 = Student("Bob")

print(f'{s1.name} is from {s1.school}')
print(s2.school)
print(s2.name)

```

    Alice is from Global Academy
    Global Academy
    Bob



```python

```


---
**Score: 0**
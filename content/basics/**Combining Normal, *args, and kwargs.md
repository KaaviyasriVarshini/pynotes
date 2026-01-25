---
title: **Combining Normal, *Args, And Kwargs
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def full_profile(name, *skills, **info):
    print("Name:", name)
    print("Skills:", skills)
    print("Details:", info)

full_profile("Alice", "Python", "ML", age=30, city="Toronto")
```

    Name: Alice
    Skills: ('Python', 'ML')
    Details: {'age': 30, 'city': 'Toronto'}



```python

```


---
**Score: 0**
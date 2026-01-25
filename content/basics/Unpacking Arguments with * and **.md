---
title: Unpacking Arguments With * And **
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def greet(name, age):
    print(f"{name} is {age} years old")

data = ("Alice", 30)
greet(*data)

info = {"name": "Bob", "age": 25}
greet(**info)
```

    Alice is 30 years old
    Bob is 25 years old



```python

```


---
**Score: 0**
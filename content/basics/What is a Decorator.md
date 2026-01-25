---
title: What Is A Decorator
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()
```

    Before function execution
    Hello
    After function execution



```python

```


---
**Score: 0**
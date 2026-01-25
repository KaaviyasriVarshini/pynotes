---
title: What Is A Closure
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def outer():
    message = "Hello"
    
    def inner():
        return message

    return inner

func = outer()
print(func())  # Output: Hello
```

    Hello



```python

```


---
**Score: 0**
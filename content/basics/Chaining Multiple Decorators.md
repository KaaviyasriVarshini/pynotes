---
title: Chaining Multiple Decorators
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def bold(func):
    def wrapper():
        print("<b>")
        func()
        print("</b>")
    return wrapper

def italic(func):
    def wrapper():
        print("<i>")
        func()
        print("</i>")
    return wrapper

@bold
@italic
def display():
    print("Text")

display()
```

    <b>
    <i>
    Text
    </i>
    </b>



```python

```


---
**Score: 0**
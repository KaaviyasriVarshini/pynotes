---
title: Visualizing The Inheritance Hierarchy
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class X:
    pass

class Y(X):
    pass

class Z(X):
    pass

class W(Y, Z):
    pass

print(W.mro())
```

    [<class '__main__.W'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.X'>, <class 'object'>]



```python

```


---
**Score: 0**
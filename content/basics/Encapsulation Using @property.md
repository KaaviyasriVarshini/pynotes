---
title: Encapsulation Using @Property
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

item = Product(100)
print(item.price)
```

    100



```python

```


---
**Score: 0**
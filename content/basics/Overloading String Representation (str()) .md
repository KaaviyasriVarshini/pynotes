---
title: Overloading String Representation (Str()) 
date: 2026-02-01
author: Your Name
cell_count: 2
score: 0
---

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs ${self.price}"

p = Product("Laptop", 1200)
print(p)  # Laptop costs $1200
```

    Laptop costs $1200



```python

```


---
**Score: 0**
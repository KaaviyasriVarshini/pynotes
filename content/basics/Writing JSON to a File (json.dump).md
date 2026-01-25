---
title: Writing Json To A File (Json.Dump)
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import json

data = {
    "product": "Laptop",
    "price": 1200,
    "in_stock": True
}

with open("product.json", "w") as file:
    json.dump(data, file)
```


```python

```


---
**Score: 0**
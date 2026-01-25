---
title:  Enterprise Use Case: Defensive Programming  
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def process_order(order):
    assert "id" in order, "Order must contain ID"
    assert order["amount"] > 0, "Order amount must be positive"
    return "Order Processed"

order = {"id": 101, "amount": 250}
print(process_order(order))
```

    Order Processed



```python

```


---
**Score: 0**
---
title:  @Property With Deleter
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.deleter
    def balance(self):
        del self._balance

acc = Account(1000)
del acc.balance
```


```python

```


---
**Score: 0**
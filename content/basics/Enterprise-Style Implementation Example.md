---
title: Enterprise-Style Implementation Example
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount

account = BankAccount("Alice", 1000)
account.balance = 1500
print(account.balance)
```

    1500



```python

```


---
**Score: 0**
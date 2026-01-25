---
title:  Real-World Class Example
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.balance)  # Output: 1500
```

    1500



```python

```


---
**Score: 0**
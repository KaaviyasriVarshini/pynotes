---
title: Assertions For Invariant Checks
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def withdraw(balance, amount):
    assert amount <= balance, "Insufficient balance"
    return balance - amount

print(withdraw(500, 600))
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    Cell In[1], line 5
          2     assert amount <= balance, "Insufficient balance"
          3     return balance - amount
    ----> 5 print(withdraw(500, 600))


    Cell In[1], line 2, in withdraw(balance, amount)
          1 def withdraw(balance, amount):
    ----> 2     assert amount <= balance, "Insufficient balance"
          3     return balance - amount


    AssertionError: Insufficient balance



```python

```


---
**Score: 0**
---
title: Multiple Closures From Same Function
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add5 = make_adder(5)
add10 = make_adder(10)

print(add5(3))    # 8
print(add10(3))   # 13
```

    8
    13



```python

```


---
**Score: 0**
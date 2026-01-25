---
title: Fibonacci Numbers
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
#4. Write a Python script that:

#Uses a while loop to print the first 10 Fibonacci numbers.


num = 0
num1 = 1
count = 0
lst = []

while count < 10:
    lst.append(num)
    num, num1 = num1, num + num1
    count += 1
print(lst)
```

    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]



```python

```


---
**Score: 0**
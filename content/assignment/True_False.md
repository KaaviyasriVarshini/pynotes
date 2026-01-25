---
title: True False
date: 2026-01-25
author: Your Name
cell_count: 1
score: 0
---

```python
#2. Write a Python function named is_even() that:

#Accepts a number as input.

#Returns True if the number is even, False if odd.
#Call this function with several test values and print the results.
#Focus: Functions, return value, modular arithmetic.


def even_number(num):
    result = True if num % 2 == 0 else False
    
    return result

num = int(input("Enter a number:"))
print(even_number(num))
```

    Enter a number: 5


    False



---
**Score: 0**
---
title: List
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
#5. Write a Python program that:

#Creates a list of at least 10 numbers.
#Removes any numbers that are divisible by 3.
#Prints the new list and its length.

even_numbers = [x for x in range(10)]
print(even_numbers)

even_numbers = [x for x in range(10) if x % 3 != 0]
print(even_numbers)
print(len(even_numbers))
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [1, 2, 4, 5, 7, 8]
    6



```python

```


---
**Score: 0**
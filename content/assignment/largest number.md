---
title: Largest Number
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
#9. Write a program that:
#Takes three numbers as input.
#Finds and prints the largest number.
#Do not use max()

numbers = input("Enter three numbers: ").split()

num1 = int(numbers[0])
num2 = int(numbers[1])
num3 = int(numbers[2])

if num1 > num2:
    
    if num1 > num3:
        print(f"{num1} is the largest number")
    else:
        pass
        
elif num2 > num3:

    if num2 > num1:
        print(f"{num2} is the largest number")
    else:
        pass
else:
    print(f"{num3} is the largest")
```

    Enter three numbers:  2 5 3


    5 is the largest number



```python

```


---
**Score: 0**
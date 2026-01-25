---
title: Creating And Using A Custom Module
date: 2026-01-25
author: Your Name
cell_count: 3
score: 0
---

```python
# file: calculator.py
def multiply(a, b):
    return a * b
```


```python
# main.py
import calculator

print(calculator.multiply(4, 5))  # Output: 20
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    Cell In[4], line 2
          1 # main.py
    ----> 2 import calculator
          4 print(calculator.multiply(4, 5))  # Output: 20


    ModuleNotFoundError: No module named 'calculator'



```python

```


---
**Score: 0**
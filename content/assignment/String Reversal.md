---
title: String Reversal
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
#6. Write a Python function that:
#Takes a string input from the user.
#Reverses the string and prints both the original and reversed string.


def reverse_string(text):
    if len(text) == 0:
        return text
    return reverse_string(text[1:]) + text[0]

string = input("Enter a string:")
print(reverse_string(string))
```

    Enter a string: PYTHON


    NOHTYP



```python

```


---
**Score: 0**
---
title: Palindrome
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
#10. Write a Python program that:
#Takes a string input.
#Checks whether the string is a palindrome.



def reverse_string(reverse):
    if len(reverse) == 0:
        return reverse
    return reverse_string(reverse[1:]) + reverse[0]

text = input("Enter a string:")
print(reverse_string(text))



if (reverse_string(text)) == text:
    print("The given string is a plindrom")
else:
    print("The given string is not a palindrom")
    
    


```

    Enter a string: malayalam


    malayalam
    The given string is a plindrom



```python

```


---
**Score: 0**
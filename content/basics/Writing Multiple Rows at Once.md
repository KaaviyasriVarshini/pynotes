---
title: Writing Multiple Rows At Once
date: 2026-01-25
author: Your Name
cell_count: 3
score: 0
---

```python
import csv

data = [
    ["John", 28, "Toronto"],
    ["Emma", 35, "Berlin"]
]

with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
    
```


```python

```


```python

```


---
**Score: 0**
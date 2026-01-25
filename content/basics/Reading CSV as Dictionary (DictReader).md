---
title: Reading Csv As Dictionary (Dictreader)
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```

    {'Name': 'Alice', 'Age': '23', 'Role': 'Engineer'}
    {'Name': 'Bob', 'Age': '30', 'Role': 'Designer'}



```python

```


---
**Score: 0**
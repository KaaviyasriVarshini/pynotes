---
title: Validating Data Before Writing
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import csv

def validate_row(row):
    return all(row)

data = [
    ["John", 28, "Toronto"],
    ["", 35, "Berlin"]
]

with open("validated.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in data:
        if validate_row(row):
            writer.writerow(row)
```


```python

```


---
**Score: 0**
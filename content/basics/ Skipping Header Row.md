---
title:  Skipping Header Row
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)
```

    Header: ['Name', 'Age', 'Role']
    ['Alice', '23', 'Engineer']
    ['Bob', '30', 'Designer']



```python

```


---
**Score: 0**
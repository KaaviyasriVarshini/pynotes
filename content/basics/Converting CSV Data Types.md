---
title: Converting Csv Data Types
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
        age = int(row["Age"])
        role = str(row["Role"])
        print(age, role)
```

    23 Engineer
    30 Designer



```python

```


---
**Score: 0**
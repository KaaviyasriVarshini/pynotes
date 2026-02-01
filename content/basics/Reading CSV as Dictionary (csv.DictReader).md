---
title: Reading Csv As Dictionary (Csv.Dictreader)
date: 2026-02-01
author: Your Name
cell_count: 2
score: 0
---

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["Age"])
```

    Alice 23
    Bob 30



```python

```


---
**Score: 0**
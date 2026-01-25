---
title: Generating Csv From List Of Dictionaries
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import csv

records = [
    {"name": "Alice", "age": 25, "city": "Rome"},
    {"name": "Bob", "age": 30, "city": "Madrid"}
]

with open("records.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)
```


```python

```


---
**Score: 0**
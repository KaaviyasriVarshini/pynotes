---
title: Appending Data To An Existing Csv
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import csv

with open("people.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Charlie", 40, "USA"])
```


```python

```


---
**Score: 0**
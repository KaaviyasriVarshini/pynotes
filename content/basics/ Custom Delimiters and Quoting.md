---
title:  Custom Delimiters And Quoting
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import csv

with open("custom.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter="|")
    writer.writerow(["Name", "Age", "Country"])
    writer.writerow(["Alice", 25, "India"])
```


```python

```


---
**Score: 0**
---
title: Writing Csv With Custom Delimiter
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import csv

with open("data_pipe.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter="|")
    writer.writerow(["Name", "Age", "Country"])
    writer.writerow(["John", 35, "India"])
```


```python

```


---
**Score: 0**
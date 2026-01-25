---
title: Basic Csv Writing With Csv.Writer
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import csv

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "city"])
    writer.writerow(["Alice", 25, "New York"])
```


```python

```


---
**Score: 0**
---
title: Writing Csv With Utf-8 Encoding
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import csv

with open("unicode.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "City"])
    writer.writerow(["José", "München"])
```


```python

```


---
**Score: 0**
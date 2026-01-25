---
title: Writing Dictionaries Using Csv.Dictwriter
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import csv

fieldnames = ["name", "age", "city"]

with open("users.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    
    writer.writerow({"name": "Alice", "age": 25, "city": "Paris"})
    writer.writerow({"name": "Bob", "age": 30, "city": "Rome"})
```


```python

```


---
**Score: 0**
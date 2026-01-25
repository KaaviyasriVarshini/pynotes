---
title: Reading A Csv File Using Csv.Reader
date: 2026-01-25
author: Your Name
cell_count: 3
score: 0
---

```python
import csv

with open("data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Age", "Role"])
    writer.writerow(["Alice", 23, "Engineer"])
    writer.writerow(["Bob", 30, "Designer"])

```


```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

    ['Name', 'Age', 'Role']
    ['Alice', '23', 'Engineer']
    ['Bob', '30', 'Designer']



```python

```


---
**Score: 0**
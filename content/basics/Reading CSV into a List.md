---
title: Reading Csv Into A List
date: 2026-02-11
author: Your Name
cell_count: 3
score: 0
---

```python
import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

print(data)
```

    [['Name', 'Age', 'Role'], ['Alice', '23', 'Engineer'], ['Bob', '30', 'Designer']]



```python

```


```python

```


---
**Score: 0**
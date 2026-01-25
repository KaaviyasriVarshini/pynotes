---
title: Real-World Generator Example (Streaming Data)
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def read_large_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

for line in read_large_file("data.csv"):
    print(line)
```

    name,age,city
    Alice,25,Paris
    Bob,30,London



```python

```


---
**Score: 0**
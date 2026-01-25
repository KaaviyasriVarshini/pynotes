---
title: Reading Csv Using Pandas (Structured Approach)
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df)
print(df["Name"])
```

        Name  Age      Role
    0  Alice   23  Engineer
    1    Bob   30  Designer
    0    Alice
    1      Bob
    Name: Name, dtype: object



```python

```


---
**Score: 0**
---
title: Real-World Iterator Example 
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class FileLineReader:
    def __init__(self, filename):
        self.file = open(filename, "r")

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line:
            return line.strip()
        self.file.close()
        raise StopIteration

for line in FileLineReader("data.csv"):
    print(line)
```

    name,age,city
    Alice,25,Paris
    Bob,30,London



```python

```


---
**Score: 0**
---
title: Calling Parent Methods Explicitly
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class A:
    def process(self):
        print("Process A")

class B:
    def process(self):
        print("Process B")

class C(A, B):
    def process(self):
        A.process(self)
        B.process(self)

c = C()
c.process()
```

    Process A
    Process B



```python

```


---
**Score: 0**
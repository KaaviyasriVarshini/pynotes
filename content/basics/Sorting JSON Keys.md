---
title: Sorting Json Keys
date: 2026-02-01
author: Your Name
cell_count: 2
score: 0
---

```python
import json

data = {"b": 2, "a": 1, "c": 3}
sorted_json = json.dumps(data, sort_keys=True)

print(sorted_json)
```

    {"a": 1, "b": 2, "c": 3}



```python

```


---
**Score: 0**
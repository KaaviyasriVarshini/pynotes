---
title: Convert Json String → Python Object (Json.Loads)
date: 2026-03-04
author: Your Name
cell_count: 2
score: 0
---

```python
import json

json_text = '{"name": "Bob", "age": 25}'
python_obj = json.loads(json_text)

print(python_obj)
print(type(python_obj))  # dict
```

    {'name': 'Bob', 'age': 25}
    <class 'dict'>



```python

```


---
**Score: 0**
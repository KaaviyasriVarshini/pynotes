---
title: Enterprise Example: Api Response Handling
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import json

def parse_api_response(response):
    try:
        data = json.loads(response)
        return data.get("status"), data.get("payload")
    except json.JSONDecodeError:
        return "error", None

response = '{"status": "success", "payload": {"id": 101}}'
print(parse_api_response(response))
```

    ('success', {'id': 101})



```python

```


---
**Score: 0**
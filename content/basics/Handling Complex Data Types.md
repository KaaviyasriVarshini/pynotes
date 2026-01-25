---
title: Handling Complex Data Types
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import json
from datetime import datetime

data = {"event": "login", "time": str(datetime.now())}

json_string = json.dumps(data)
print(json_string)
```

    {"event": "login", "time": "2026-01-17 22:20:43.872983"}



```python

```


---
**Score: 0**
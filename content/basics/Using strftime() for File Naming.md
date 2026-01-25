---
title: Using Strftime() For File Naming
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from datetime import datetime

filename = "file_datetime" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".zip"
print(filename)
```

    file_datetime20260117_192758.zip



```python

```


---
**Score: 0**
---
title: Time Formatting
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from datetime import datetime

now = datetime.now()

print(now.strftime("%H:%M:%S"))  # 24-hour format
print(now.strftime("%I:%M %p"))  # 12-hour format with AM/PM
```

    19:24:16
    07:24 PM



```python

```


---
**Score: 0**
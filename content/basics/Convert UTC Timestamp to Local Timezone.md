---
title: Convert Utc Timestamp To Local Timezone
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from datetime import datetime
from zoneinfo import ZoneInfo

timestamp = 1732452305

utc = datetime.fromtimestamp(timestamp, ZoneInfo("UTC"))
local = utc.astimezone(ZoneInfo("Asia/Kolkata"))

print("UTC:", utc)
print("Local:", local)
```

    UTC: 2024-11-24 12:45:05+00:00
    Local: 2024-11-24 18:15:05+05:30



```python

```


---
**Score: 0**
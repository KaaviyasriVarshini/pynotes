---
title: Timezone Handling With Zoneinfo
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
from datetime import datetime
from zoneinfo import ZoneInfo

ny_time = datetime.now(ZoneInfo("America/New_York"))
tokyo_time = datetime.now(ZoneInfo("Asia/Tokyo"))

print("New York:", ny_time)
print("Tokyo:", tokyo_time)
```

    New York: 2026-01-17 08:27:42.196164-05:00
    Tokyo: 2026-01-17 22:27:42.196647+09:00



```python

```


---
**Score: 0**
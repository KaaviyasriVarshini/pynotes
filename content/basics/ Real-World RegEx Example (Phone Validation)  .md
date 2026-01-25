---
title:  Real-World Regex Example (Phone Validation)  
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
import re

def validate_phone(phone):
    pattern = r"^\+?\d{10,13}$"
    return bool(re.match(pattern, phone))

print(validate_phone("+911234567890"))  # True
print(validate_phone("12345"))          # False
```

    True
    False



```python

```


---
**Score: 0**
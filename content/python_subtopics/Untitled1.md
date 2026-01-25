---
title: Untitled1
date: 2026-01-25
author: Your Name
cell_count: 1
score: 0
---

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    email: str

def display_user(user: User) -> str:
    return f"{user['name']} ({user['age']}) can be reached at {user['email']}."

user = {"name": "Alice", "age": 30, "email": "alice@example.com"}
print(display_user(user))
# Output: Alice (30) can be reached at alice@example.com.
```


---
**Score: 0**
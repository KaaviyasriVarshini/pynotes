---
title: Real-World Decorator Example (Authentication)
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
def require_login(func):
    def wrapper(user):
        if not user.get("authenticated"):
            return "Access Denied"
        return func(user)
    return wrapper

@require_login
def view_profile(user):
    return f"Welcome {user['name']}"

user = {"name": "Alice", "authenticated": True}
print(view_profile(user))
```

    Welcome Alice



```python

```


---
**Score: 0**
---
title: Custom Type Conversion Via   Str   And   Int  
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Score:
    def __init__(self, points: int):
        self.points = points

    def __str__(self) -> str:
        return f"Score: {self.points}"

    def __int__(self) -> int:
        return self.points

player_score = Score(95)

print(str(player_score))  # Output: Score: 95
print(int(player_score))  # Output: 95
```

    Score: 95
    95



```python

```


---
**Score: 0**
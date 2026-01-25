---
title: Enforcing Data Integrity 
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
```


```python

```


---
**Score: 0**
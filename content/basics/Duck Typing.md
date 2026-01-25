---
title: Duck Typing
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Car:
    def move(self):
        print("Car moving")

class Boat:
    def move(self):
        print("Boat sailing")

def start(vehicle):
    vehicle.move()

start(Car())
start(Boat())
```

    Car moving
    Boat sailing



```python

```


---
**Score: 0**
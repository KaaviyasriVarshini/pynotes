---
title: Real-World Inheritance Example
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")

car = Car()
bike = Bike()

car.start()
car.drive()

bike.start()
bike.ride()
```

    Vehicle started
    Car is driving
    Vehicle started
    Bike is riding



```python

```


---
**Score: 0**
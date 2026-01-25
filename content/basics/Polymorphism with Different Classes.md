---
title: Polymorphism With Different Classes
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

def make_sound(animal):
    animal.sound()

make_sound(Cat())
make_sound(Dog())
```

    Meow
    Bark



```python

```


---
**Score: 0**
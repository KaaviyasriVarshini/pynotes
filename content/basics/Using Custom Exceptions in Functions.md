---
title: Using Custom Exceptions In Functions
date: 2026-01-25
author: Your Name
cell_count: 2
score: 0
---

```python
class FileMissingError(Exception):
    pass

def load_config(filename):
    if not filename.endswith(".json"):
        raise FileMissingError("Only JSON configuration files supported")

load_config("config.txt")
```


    ---------------------------------------------------------------------------

    FileMissingError                          Traceback (most recent call last)

    Cell In[3], line 8
          5     if not filename.endswith(".json"):
          6         raise FileMissingError("Only JSON configuration files supported")
    ----> 8 load_config("config.txt")


    Cell In[3], line 6, in load_config(filename)
          4 def load_config(filename):
          5     if not filename.endswith(".json"):
    ----> 6         raise FileMissingError("Only JSON configuration files supported")


    FileMissingError: Only JSON configuration files supported



```python

```


---
**Score: 0**
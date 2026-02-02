---
title: Fastapi
date: 2026-02-01
author: Your Name
cell_count: 8
score: 5
---

```python
#main.py vs Modular Applications
from fastapi import FastAPI
from app.routes import users

app = FastAPI()
app.include_router(users.router)
```


```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    return item
```


```python
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup():
    print("Starting application")

@app.on_event("shutdown")
async def shutdown():
    print("Shutting down application")
```

    /tmp/ipykernel_15028/329738538.py:5: DeprecationWarning: 
            on_event is deprecated, use lifespan event handlers instead.
    
            Read more about it in the
            [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
            
      @app.on_event("startup")
    /tmp/ipykernel_15028/329738538.py:9: DeprecationWarning: 
            on_event is deprecated, use lifespan event handlers instead.
    
            Read more about it in the
            [FastAPI docs for Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
            
      @app.on_event("shutdown")



```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Service"
    debug: bool = False

settings = Settings()
```


    ---------------------------------------------------------------------------

    PydanticImportError                       Traceback (most recent call last)

    Cell In[6], line 1
    ----> 1 from pydantic import BaseSettings
          3 class Settings(BaseSettings):
          4     app_name: str = "FastAPI Service"


    File ~/miniconda3/envs/py311/lib/python3.11/site-packages/pydantic/__init__.py:437, in __getattr__(attr_name)
        435 dynamic_attr = _dynamic_imports.get(attr_name)
        436 if dynamic_attr is None:
    --> 437     return _getattr_migration(attr_name)
        439 package, module_name = dynamic_attr
        441 if module_name == '__module__':


    File ~/miniconda3/envs/py311/lib/python3.11/site-packages/pydantic/_migration.py:304, in getattr_migration.<locals>.wrapper(name)
        302     return import_string(REDIRECT_TO_V1[import_path])
        303 if import_path == 'pydantic:BaseSettings':
    --> 304     raise PydanticImportError(
        305         '`BaseSettings` has been moved to the `pydantic-settings` package. '
        306         f'See https://docs.pydantic.dev/{version_short()}/migration/#basesettings-has-moved-to-pydantic-settings '
        307         'for more details.'
        308     )
        309 if import_path in REMOVED_IN_V2:
        310     raise PydanticImportError(f'`{import_path}` has been removed in V2.')


    PydanticImportError: `BaseSettings` has been moved to the `pydantic-settings` package. See https://docs.pydantic.dev/2.12/migration/#basesettings-has-moved-to-pydantic-settings for more details.
    
    For further information visit https://errors.pydantic.dev/2.12/u/import-error



```python
#Strong Typing for Path Parameters
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```


```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def list_items(category: str | None = None, limit: int = 10):
    return {"category": category, "limit": limit}
```


```python

```


```python

```


---
**Score: 5**
---
title: Project Setup & First Execution
date: 2026-01-25
author: Your Name
cell_count: 6
score: 5
---

```python
#Load the API Key in Python

from dotenv import load_dotenv
load_dotenv()
```




    True




```python
#Verify the Key Is Loaded
import os
print(os.getenv("GOOGLE_API_KEY")[:5])
```

    AIzaS



```python
#First LLM Call (Gemini)

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=api_key,
    temperature=0.2
)

response = model.invoke(
    "Explain artificial intelligence in one sentence."
)

print(response.content)
```

    Artificial intelligence is the development of computer systems that can perform tasks typically requiring human intelligence, such as learning, reasoning, and problem-solving.



```python
response.content
```




    'Artificial intelligence is the development of computer systems that can perform tasks typically requiring human intelligence, such as learning, reasoning, and problem-solving.'




```python
#LangChain Hub Usage
from langchain_classic import hub

# Get the latest version of a prompt
prompt = hub.pull("rlm/rag-prompt")
```


```python

```


---
**Score: 5**
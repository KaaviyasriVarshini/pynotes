---
title: Project Setup & First Execution
date: 2026-02-01
author: Your Name
cell_count: 11
score: 10
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

print(prompt)
```

    input_variables=['context', 'question'] input_types={} partial_variables={} metadata={'lc_hub_owner': 'rlm', 'lc_hub_repo': 'rag-prompt', 'lc_hub_commit_hash': '50442af133e61576e74536c6556cefe1fac147cad032f4377b60c436e6cdcb6e'} messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['context', 'question'], input_types={}, partial_variables={}, template="You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.\nQuestion: {question} \nContext: {context} \nAnswer:"), additional_kwargs={})]



```python
#Version Pinning (Historical Practice)
prompt = hub.pull("rlm/rag-prompt:50442af1")
```


```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "Summarize the following text. "
    "Write the summary.\n\n"
    "CONTEXT:\n{context}\n\nSUMMARY:"
)
```


```python
#Personalized Summary Prompt for Stuff Documents

from langchain_core.prompts import PromptTemplate
from langchainhub import Client


prompt_title = "summary-stuff-documents"

prompt_template = """Please summarize the content according to the following rules.

REQUEST:
1. Summarize the main points in bullet points.
2. Each bullet must start with an emoji that matches its meaning.
3. Use varied emojis.
4. Do NOT include unnecessary information.
5. Write the summary in FINNISH.

CONTEXT:
{context}

SUMMARY:
"""
prompt = PromptTemplate.from_template(prompt_template)


hub = Client()
prompt = hub.pull("rlm/rag-prompt")

print(prompt)

#hub.push(f"{PROMPT_OWNER}/{prompt_title}", prompt)
```

    /tmp/ipykernel_26277/825896933.py:25: DeprecationWarning: The `langchainhub sdk` is deprecated.
    Please use the `langsmith sdk` instead:
      pip install langsmith
    Use the `pull_prompt` method.
      prompt = hub.pull("rlm/rag-prompt")


    {"id": ["langchain", "prompts", "chat", "ChatPromptTemplate"], "lc": 1, "type": "constructor", "kwargs": {"messages": [{"id": ["langchain", "prompts", "chat", "HumanMessagePromptTemplate"], "lc": 1, "type": "constructor", "kwargs": {"prompt": {"id": ["langchain", "prompts", "prompt", "PromptTemplate"], "lc": 1, "type": "constructor", "kwargs": {"template": "You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.\nQuestion: {question} \nContext: {context} \nAnswer:", "input_variables": ["question", "context"], "template_format": "f-string"}}}}], "input_variables": ["question", "context"]}}



```python
#Chain-of-Density Personalized Prompts

from langchain_core.prompts import ChatPromptTemplate

prompt_title = "chain-of-density-finnish"

prompt = ChatPromptTemplate.from_template(
    """Article: {ARTICLE}

Generate increasingly concise, entity-dense summaries.
Repeat the process 5 times.

Return the result in JSON with keys:
- Missing_Entities
- Denser_Summary

Use only FINNISH language."""
)


hub.push(f"{PROMPT_OWNER}/{prompt_title}", prompt)

```


```python
#Personalized RAG Prompt for Finnish QA

from langchain_classic.prompts import ChatPromptTemplate

prompt_title = "rag-prompt-finnish"

system = """You are a question-answering assistant.
Answer using ONLY the provided context.
If the answer cannot be found, say so clearly.
Reply in FINNISH."""
human = """Question:
{question}

Context:
{context}

Answer:"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system),
    ("human", human),
])

from langchain_classic import hub
hub.push(f"{PROMPT_OWNER}/{prompt_title}", prompt)
```


```python

```


---
**Score: 10**
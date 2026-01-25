---
title: Prompting Fundamentals
date: 2026-01-25
author: Your Name
cell_count: 9
score: 5
---

```python
#Initialize the Gemini Model

Copy

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
)
response = llm.invoke("What is the capital of Canada?")
print(response.content)
```

    The capital of Canada is **Ottawa**.



```python
#Defining Few-Shot Examples
examples = [
    {
        "question": "Who lived longer, Steve Jobs or Albert Einstein?",
        "answer": """Do we need additional questions? Yes.
Steve Jobs died at age 56.
Albert Einstein died at age 76.
Final answer: Albert Einstein."""
    },
    {
        "question": "When was Google's founder born?",
        "answer": """Do we need additional questions? Yes.
Google was founded by Larry Page.
Larry Page was born on March 26, 1973.
Final answer: March 26, 1973."""
    },
]
```


```python
#Defining the Example Format

from langchain_core.prompts import PromptTemplate

example_prompt = PromptTemplate.from_template(
    "Question:\n{question}\nAnswer:\n{answer}"
)
```


```python
#Creating the FewShotPromptTemplate

from langchain_core.prompts.few_shot import FewShotPromptTemplate

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question:\n{question}\nAnswer:",
    input_variables=["question"],
)
```


```python
#Executing the Prompt via a Chain

from langchain_core.output_parsers import StrOutputParser

chain = prompt | llm | StrOutputParser()

result = chain.invoke({
    "question": "How old was Bill Gates when Microsoft was founded?"
})

print(result)
```

    Do we need additional questions? Yes.
    Bill Gates was born on October 28, 1955.
    Microsoft was founded on April 4, 1975.
    From October 28, 1955, to April 4, 1975, Bill Gates was 19 years old.
    Final answer: 19 years old.



```python
#Semantic Similarity Example Selector (Gemini Embeddings)

from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001"
)

example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples=examples,          # list of dicts
    embeddings=embeddings,      # embedding function
    vectorstore_cls=Chroma,     # ✅ THIS is required
    k=1,
)
```


```python
#Final Chat Prompt Composition
final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        few_shot_prompt,
        ("human", "{instruction}\n{input}"),
    ]
)
```


```python
#Running the Chat Few-Shot Chain
chain = final_prompt | llm

response = chain.invoke({
    "instruction": "Please write meeting minutes",
    "input": "On December 26, the product team reviewed project progress..."
})

print(response.content)
```

    Okay, I can help you write meeting minutes based on that starting point. To make them comprehensive, I'll make some reasonable assumptions about the meeting details. Feel free to adjust any of the assumed information.
    
    ---
    
    **MEETING MINUTES**
    
    **Meeting Title:** Product Team Project Progress Review
    **Date:** December 26, 2023
    **Time:** 10:00 AM - 11:00 AM PST
    **Location:** Virtual Meeting (Zoom)
    
    **Attendees:**
    *   Sarah Chen (Product Manager - Chair)
    *   David Lee (Lead Developer)
    *   Maria Rodriguez (UX Designer)
    *   Tom Wilson (Marketing Liaison)
    *   Emily White (QA Lead - Minute Taker)
    
    **Absentees:** None
    
    ---
    
    **1. Review of Project Alpha: "New Feature Rollout"**
    *   **Discussion:** Sarah opened the discussion by noting Project Alpha is largely on track for its upcoming beta. David confirmed backend stability and reported that all core functionalities are implemented. Maria presented minor UI feedback received from internal testing, suggesting a few tweaks for improved user experience and accessibility. Tom provided an update on marketing material preparation, confirming it's aligned with the beta launch date. Emily reported no critical bugs found in recent QA cycles, but highlighted a few minor UI inconsistencies.
    *   **Decisions:**
        *   Prioritize the suggested UI tweaks for Project Alpha before the beta launch.
        *   Marketing materials to be finalized by end of week.
    
    **2. Review of Project Beta: "Platform Integration"**
    *   **Discussion:** David reported that backend development for Project Beta is slightly behind schedule due to unexpected complexities in database integration with the legacy system. He estimates a 3-day delay. Maria confirmed frontend development is progressing well and is ahead of schedule, with 80% of the UI complete. Emily highlighted potential risks if the backend delays impact the overall integration timeline, especially concerning end-to-end testing. Tom noted that the marketing team is ready to start drafting communications once a firm launch date is established.
    *   **Decisions:**
        *   Allocate additional development resources to accelerate Project Beta backend work.
        *   Schedule a dedicated technical sync to address database integration challenges and identify potential solutions.
    
    **3. Upcoming Milestones & Blockers**
    *   **Discussion:**
        *   Project Alpha Beta Launch: Confirmed for January 10, 2024.
        *   Project Beta Internal Demo: Tentatively scheduled for January 5, 2024, but subject to backend progress.
        *   Primary Blocker: Project Beta database integration complexity and associated delay.
    
    **4. Open Discussion & Next Steps**
    *   General agreement that Project Alpha is in good shape and focus needs to shift to mitigating risks for Project Beta. Sarah emphasized the importance of clear communication regarding any further delays for Project Beta.
    
    ---
    
    **ACTION ITEMS:**
    
    | Who             | What                                                              | Due Date        |
    | :-------------- | :---------------------------------------------------------------- | :-------------- |
    | Maria Rodriguez | Finalize UI mockups for Project Alpha tweaks                      | December 28, 2023 |
    | David Lee       | Reassign John (Developer) to Project Beta backend development     | December 27, 2023 |
    | David Lee       | Schedule technical sync for Project Beta database integration     | December 27, 2023 |
    | Sarah Chen      | Follow up with Marketing on final Project Alpha beta launch materials | December 29, 2023 |
    | Emily White     | Prepare a brief risk assessment for Project Beta integration delays | January 3, 2024   |
    
    ---
    
    **Next Meeting:**
    **Date:** January 9, 2024
    **Time:** 10:00 AM - 11:00 AM PST
    **Purpose:** Project Alpha Beta Readiness & Project Beta Integration Update
    
    ---
    **Minutes Recorded By:** Emily White
    **Approved By:** Sarah Chen (Product Manager)
    ---



```python

```


---
**Score: 5**
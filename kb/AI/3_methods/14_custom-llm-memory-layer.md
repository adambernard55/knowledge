---
title: "How to Build a Custom LLM Memory Layer"
id: "KB/AI/M-12"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-02-06"
status: "Active"
doc_type: "Reference"
summary: "A step-by-step guide to building a custom, persistent memory layer for LLM agents from scratch using DSPy and a vector database like QDrant."
tags:
  - "ai"
  - "llm"
  - "memory"
  - "context-engineering"
  - "dspy"
  - "qdrant"
  - "agentic-architecture"
  - "rag"
relations:
  - "kb/AI/3_methods/11_agentic-context-engineering.md"
  - "kb/AI/2_agents/06_building-an-ai-agent-with-dual-memory.md"
aliases:
  - "LLM Memory Layer"
  - "Custom AI Memory"
  - "Building LLM Memory"

# --- AI & RAG Enhancement ---
semantic_summary: >
  This document provides a technical walkthrough for creating a custom memory layer for LLMs, addressing their stateless nature. It covers the four key stages: extracting atomic memories from conversations using DSPy, embedding them into a vector DB (QDrant), retrieving relevant memories via tool-calling, and maintaining memory state (add, update, delete) with a ReAct agent. The architecture treats memory as a context engineering problem, enabling personalized and stateful AI agent interactions.
synthetic_questions:
  - "How can I give an LLM persistent memory across sessions?"
  - "What is the architecture for an LLM memory system?"
  - "How do you use DSPy to extract structured memories from a conversation?"
  - "What is the role of a vector database like QDrant in an LLM memory layer?"
  - "How does a ReAct agent maintain and update LLM memories?"
key_concepts:
  - "LLM Memory"
  - "Context Engineering"
  - "DSPy"
  - "QDrant"
  - "Vector Database"
  - "ReAct Agent"
  - "Tool Calling"
  - "Stateful AI"
---


# How to Build a Custom LLM Memory Layer from Scratch

Every LLM call is a fresh start. Unless you explicitly supply information from previous sessions, the model has no built‑in sense of continuity across requests or sessions. This stateless design is great for parallelism and safety, but it poses a huge challenge for applications that require user-level personalization. This guide provides a step-by-step process for building a simple, persistent memory system from scratch.

## 1. Memory as a Context Engineering Problem

Context Engineering is the technique of filling in the context of an LLM with all the relevant information it needs to complete a task. Memory is one of the hardest and most interesting context engineering problems.

![Diagram showing that LLMs do not come with memory](https://contributor.insightmediagroup.io/wp-content/uploads/2026/01/Slide5-1024x576.jpeg)

Tackling memory introduces several critical techniques required in most context engineering problems:
1.  Extracting structured information from raw text streams
2.  Summarization
3.  Vector databases
4.  Query generation and similarity search
5.  Query post-processing and re-ranking
6.  Agentic tool calling

## 2. High‑Level Architecture

At a glance, the system must perform four functions: **extract**, **embed**, **retrieve**, and **maintain**.

-   **Extraction**: Extracts candidate atomic memories from the current user-assistant messages.
-   **Vector DB**: Embeds the extracted factoids into continuous vectors and stores them in a vector database.
-   **Retrieval**: When the user asks a question, generate a query with an LLM and retrieve memories similar to that query.
-   **Maintenance**: Using a ReAct (Reasoning and Acting) loop, the agent decides whether to add, update, delete, or do nothing based on the conversation and contradictions with existing facts.

![Diagram of the Mem0 architecture](https://contributor.insightmediagroup.io/wp-content/uploads/2026/01/CleanShot-2026-01-12-at-02.11.15@2x-1024x523.png)

Crucially, every step should be optional. If the agent does not need memory to answer a question, it should not search the vector database. The strategy is to provide the LLM with the necessary tools and rely on its intelligence to use them autonomously.

## 3. Memory Extraction with DSPy

The first step is to convert conversation transcripts into atomic, categorized factoids. A "good" memory is a short, self-contained fact that can be embedded and retrieved with high precision.

With DSPy, we can define a signature to extract a list of string factoids from a transcript.

```python
import dspy
from pydantic import BaseModel

class MemoryExtract(dspy.Signature):
    """
Extract relevant information from the conversation. 
Memories are atomic independent factoids that we must learn about the user.
If transcript does not contain any information worth extracting, return empty list.
"""
    transcript: str = dspy.InputField()
    memories: list[str] = dspy.OutputField()

memory_extractor = dspy.Predict(MemoryExtract)
````

The signature's docstring acts as the system prompt. We can then call this predictor with the conversation history to extract the memories.

## 4. Embedding and Storing Memories

Once memories are extracted, they must be embedded and stored in a vector database. This guide uses **QDrant** for its speed and hybrid filtering capabilities.

![Diagram showing memories being uploaded to a vector database](https://contributor.insightmediagroup.io/wp-content/uploads/2026/01/image-3-1024x576.jpeg)

We use `text-embedding-3-small` for its balance of cost, speed, and quality on short texts. After generating embeddings, we can create helper functions to insert, delete, update, and search for memories in our QDrant collection, filtering by `user_id` to ensure data isolation.

## 5. Memory Retrieval via Tool Calling

To retrieve memories, we create a tool-calling agent. Instead of always searching for memories, the agent decides when it's necessary. We provide the agent a `fetch_similar_memories` tool, which it can invoke when it lacks the context to answer a user's question.

In DSPy, a tool is a simple Python function with a docstring that the LLM uses to understand its purpose.

```python
async def fetch_similar_memories(search_text: str):
    """
Search memories from vector database if conversation requires additional context.

Args:
- search_text : The string to embed and do vector similarity search
    """
    # ... implementation ...
```

We then wrap our response generation logic in a `dspy.ReAct` agent, giving it access to this tool. The ReAct (Reasoning and Acting) agent will observe the conversation, reason about the next step, and then act—either by generating an answer directly or by calling the tool to retrieve memories first.

![Diagram of the memory retrieval process](https://contributor.insightmediagroup.io/wp-content/uploads/2026/01/image-6-1024x576.jpeg)

The agent also determines if the latest interaction contains new information that should be saved to the memory layer.

## 6. Memory Maintenance

Memory is not a static log; it must evolve. When the agent decides to save a new memory, a separate maintenance agent determines how to integrate it.

![Diagram showing the memory update decision process](https://contributor.insightmediagroup.io/wp-content/uploads/2026/01/image-1-1024x576.jpeg)

This maintenance agent has four possible actions, implemented as tools:

- **`add_memory(text)`**: Inserts a new fact.
- **`update_memory(id, updated_text)`**: Corrects or refines an existing memory.
- **`delete_memories(ids)`**: Removes obsolete or contradictory memories.
- **`no_op()`**: Does nothing if the new information is irrelevant or already captured.

This agentic loop ensures the memory remains accurate and relevant over time, allowing the primary agent to deliver increasingly personalized and context-aware responses.

## 7. Further Expansion

This guide covers the building blocks of a memory system. The concept can be expanded with more advanced techniques:

- **Graph Memory System**: Store memories as triplets in a graph database instead of a vector DB.
- **Metadata Filtering**: Add category tags (e.g., "food," "hobbies") to memories to allow for more targeted queries.
- **System Prompt Injection**: Automatically inject critical user information from memory directly into the system prompt for every session.


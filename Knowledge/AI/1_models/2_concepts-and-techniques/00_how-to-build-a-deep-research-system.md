---
title: How to Build a Deep Research System
summary: Explains the architecture and implementation of a deep research system, an advanced alternative to RAG that uses an orchestrator LLM and sub-agents to perform comprehensive analysis across large document sets.
category: AI Concepts & Techniques
difficulty: Advanced
last_updated: 2025-11-10
kb_status: published
tags:
  - ai
  - rag
  - agentic-workflow
  - research-system
  - llm-architecture
related_topics:
  - ai-models
  - vector-databases
aliases:
  - Deep Research System
  - Agentic Research System
---

# How to Build a Deep Research System

A **Deep Research System** is an advanced AI architecture designed to answer complex queries by performing a comprehensive, multi-step analysis of a large corpus of documents. Unlike simpler retrieval methods, it mimics a human research process by planning, delegating tasks to specialized sub-agents, and synthesizing findings into a detailed answer. This approach powers the "deep research" features found in applications like [[1_chatgpt]] and [[2_gemini]].

## When to Use a Deep Research System

While powerful, a deep research system is not always necessary. Simpler alternatives should be preferred when they are sufficient for the task.

-   **Direct LLM Input:** Ideal if all your information fits within the model's context window (e.g., under 1 million tokens).
-   **Standard RAG (Retrieval-Augmented Generation):** Effective for answering questions that rely on retrieving specific facts or text chunks via vector similarity.
-   **Keyword Search:** Useful when you are familiar with the dataset and know which specific terms to search for.

A deep research system is justified when these methods fail—for instance, when you need to analyze and synthesize information from many different sources, the answer isn't contained in a single chunk, or you are unfamiliar with the document corpus.

## System Architecture

A deep research system typically consists of an orchestrator agent that manages multiple sub-agents, each equipped with a set of tools to interact with the data.

1.  **Orchestrator Agent:** The "brain" of the system. It receives the user's query, creates a research plan, dispatches tasks to sub-agents, evaluates the information they return, and synthesizes the final, comprehensive answer.
2.  **Sub-Agents:** Specialized "worker" agents that execute specific, narrow tasks assigned by the orchestrator, such as performing a keyword search, summarizing a document, or extracting key figures.
3.  **Tool Library:** A collection of functions that agents can use to gather information.
4.  **Document Corpus & Indices:** The knowledge base, which must be indexed for efficient retrieval. This includes:
    *   **Keyword Index:** For literal term matching (e.g., using BM25).
    *   **Vector Index:** For semantic similarity search, created by chunking, embedding, and storing documents in a vector database.

## Implementation Steps

### 1. Data Aggregation and Indexing

First, gather all information from sources like Google Drive, Notion, or Salesforce. Once aggregated (e.g., as PDFs in a single folder), create two primary indices:
-   **Keyword Search Index:** Allows for searching specific terms, names, or titles.
-   **Vector Similarity Index:** Involves chunking documents, creating embeddings for each chunk, and storing them in a vector database for semantic search.

### 2. Tool Development

Create a library of functions (tools) that the agents can call. These functions should be simple and reliable.

````markdown
```python
@tool 
def keyword_search(query: str) -> str:
    """Searches the document corpus for specific keywords and returns matching text."""
    results = perform_keyword_search(query)
    # Format results for the LLM
    formatted_results = "\n".join([f"Source: {res['file_name']}\nContent: {res['content']}" for res in results])
    return formatted_results

@tool
def vector_search(query: str) -> str:
    """Performs a semantic search on the document corpus to find conceptually similar text."""
    results = perform_vector_search(query)
    # Format results for the LLM
    formatted_results = "\n".join([f"Source: {res['file_name']}\nContent: {res['content']}" for res in results])
    return formatted_results
````

Other useful tools could include `internet_search`, `filename_search`, or custom functions for accessing specific databases.

### 3. Agentic Workflow

The system operates in a loop managed by the orchestrator:

1. **Plan:** The **Orchestrator Agent** receives the user query and may ask a clarifying question to narrow the scope. It then formulates a multi-step research plan.
2. **Delegate:** The orchestrator dispatches **Sub-Agents** to execute the first steps of the plan, providing them with the necessary tools and instructions.
3. **Execute & Summarize:** Sub-agents use the tools to find information, summarize their findings, and report back to the orchestrator.
4. **Aggregate & Iterate:** The orchestrator gathers all the summaries. It then determines if the information is sufficient to answer the query. If not, it refines the plan and delegates new tasks, looping back to step 2.
5. **Synthesize:** Once enough information is gathered, the orchestrator synthesizes all the findings into a single, coherent, and well-supported answer for the user.

### 4. Model Selection

The choice of models is crucial for balancing performance and cost.

- **Orchestrator Agent:** Requires a high-capability model with strong reasoning skills, such as **Claude 4 Opus** or a premium **GPT-4.1** tier.
- **Sub-Agents:** Can use faster, more cost-effective models like **Claude 4 Sonnet** or **gpt-4.1-mini**, as their tasks are more focused.  
    (See [00_ai-models](obsidian://open?file=Knowledge%2FAI%2F4_models%2F00_ai-models.md) for a detailed comparison).

## Conclusion & Trade-Offs

The primary advantage of a deep research system is its ability to deliver high-quality, comprehensive answers by analyzing a document corpus more thoroughly than standard RAG. This significantly reduces the chance of missing critical information.

However, this comes at the cost of **increased latency and complexity**. The system is inherently slower due to its multi-step, iterative nature. It is best suited for high-stakes scenarios where the quality and depth of the answer are more important than the speed of the response.
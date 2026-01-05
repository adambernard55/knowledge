---
title: "Architecting a Deep Research System: An Agentic Alternative to RAG"
id: "SIE/REF/Deep-Research-Arch"
version: "2.0"
steward: "Adam Bernard"
updated: "2026-01-05"
status: "Active"
doc_type: "Reference"
summary: "Provides a technical blueprint for building a deep research system using an orchestrator and sub-agents, offering a more comprehensive alternative to standard RAG for complex queries."
tags:
  - deep-research
  - agentic-workflow
  - rag-alternative
  - llm-architecture
  - orchestrator-pattern
relations:
  - "SIE/REF/ChatGPT-Models-Compare"
  - "SIE/REF/Claude-Models-Compare"
  - "SIE/REF/Gemini-Models-Compare"
aliases:
  - "Deep Research System"
  - "Agentic Research System"

# --- AI & RAG Enhancement ---
semantic_summary: "This document details the architecture for a deep research system, an advanced agentic workflow that surpasses standard RAG. It explains the roles of an orchestrator LLM and specialized sub-agents in planning, executing, and synthesizing research from large document corpora, providing a framework for answering complex, multi-source queries."
synthetic_questions:
  - "How do you build a research system more advanced than RAG?"
  - "What is the difference between a deep research system and standard RAG?"
  - "What is the role of an orchestrator agent in an AI research system?"
key_concepts:
  - "Orchestrator Agent"
  - "Sub-Agents"
  - "Agentic Workflow"
  - "Retrieval-Augmented Generation (RAG)"
  - "Keyword Index"
  - "Vector Index"

# --- SEO & Publication ---
primary_keyword: "deep research system"
seo_title: "How to Build a Deep Research System: An Advanced Guide"
meta_description: "Learn to architect a deep research system using agentic workflows. A technical guide on moving beyond RAG with orchestrators and sub-agents for complex analysis."
excerpt: "Move beyond standard RAG. This guide provides a technical blueprint for building a deep research system with an orchestrator and sub-agents to answer complex, multi-source questions."
cover_image: ""
---

# Architecting a Deep Research System

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
```

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

- **Orchestrator Agent:** Requires a high-capability model with strong reasoning skills, such as **Claude Opus 4.1** or the **OpenAI o1-series**.
- **Sub-Agents:** Can use faster, more cost-effective models like **Claude Sonnet 4.5**, **Gemini 1.5 Flash**, or **GPT-4o mini**, as their tasks are more focused.

(See [1_chatgpt](obsidian://open?file=kb%2FAI%2F1_models%2F1_specific-models%2F1_chatgpt.md), [2_gemini](obsidian://open?file=kb%2FAI%2F1_models%2F1_specific-models%2F2_gemini.md), and [3_claude](obsidian://open?file=kb%2FAI%2F1_models%2F1_specific-models%2F3_claude.md) for detailed model comparisons).

## Conclusion & Trade-Offs

The primary advantage of a deep research system is its ability to deliver high-quality, comprehensive answers by analyzing a document corpus more thoroughly than standard RAG. This significantly reduces the chance of missing critical information.

However, this comes at the cost of **increased latency and complexity**. The system is inherently slower due to its multi-step, iterative nature. It is best suited for high-stakes scenarios where the quality and depth of the answer are more important than the speed of the response.
---
title: "Retrieval-Augmented Generation (RAG)"
id: "kb/CORE/concepts/rag"
version: "1.0"
steward: "Adam Bernard"
updated: "2025-11-28"
status: "Active"
doc_type: "reference_document"
summary: "Explains Retrieval-Augmented Generation (RAG), the core technique used by the Strategic Intelligence Engine (SIE) to provide agents with real-time, factual context from the Master Hub, enhancing the accuracy and relevance of their outputs."
tags:
  - rag
  - retrieval
  - ai-agents
  - sie-engine
  - knowledge-base
  - llm
  - vector-search
relations:
  - "kb/CORE/00_anatomy"
  - "kb/CORE/concepts/advanced-retrieval"
aliases:
  - RAG
  - Retrieval Augmented Generation
---

# Retrieval-Augmented Generation (RAG)

**Retrieval-Augmented Generation (RAG)** is the primary technique the **Strategic Intelligence Engine (SIE)** uses to connect its AI agents to the real-time, factual knowledge stored in a client's **Master Hub**. It is a method that enhances the capabilities of Large Language Models (LLMs) by providing them with relevant, external information *at the moment they need it*, rather than relying solely on their pre-trained data.

RAG is the solution to two fundamental limitations of LLMs: their knowledge being frozen at a specific point in time (knowledge cutoff) and their tendency to "hallucinate" or invent facts. By grounding the model with verifiable data, RAG makes the SIE's outputs more accurate, trustworthy, and relevant.

## How RAG Works in the SIE

When an SIE agent is given a task, it follows a precise RAG workflow to leverage the Master Hub:

1.  **Query:** The agent's task or a user's question is formulated as a query (e.g., "What were the key findings from our Q3 customer feedback?").
2.  **Embedding:** The query is converted into a vector embedding—a numerical representation of its semantic meaning.
3.  **Vector Search:** This embedding is used to search the Master Hub's vector database. The database returns the chunks of text (e.g., paragraphs from Q3 reports, summaries of feedback sessions) that are most semantically similar to the query.
4.  **Context Augmentation:** The most relevant text chunks are retrieved and combined with the original query to form an "augmented prompt." This new prompt effectively says: "Using only the following information [...retrieved text...], answer this question: 'What were the key findings from our Q3 customer feedback?'"
5.  **Generation:** The augmented prompt is sent to the LLM.
6.  **Grounded Response:** The LLM generates a response that is directly based on the provided, factual context from the Master Hub, ensuring the answer is accurate and specific to the client's data.

## Why RAG is Foundational for the SIE

-   **Factual Accuracy:** It dramatically reduces hallucinations by forcing the agent to base its response on the curated truth of the Master Hub.
-   **Real-Time Knowledge:** The SIE can act on the most current information as soon as it's added to the Master Hub, without the need for costly and time-consuming model retraining.
-   **Transparency and Trust:** Because the source of the information is known, responses can be traced back to the specific documents used, allowing for verification.
-   **Cost-Effectiveness:** RAG is far more efficient than fine-tuning a model every time new knowledge is introduced.

## RAG vs. Fine-Tuning

It is crucial to distinguish RAG from fine-tuning:

-   **Fine-Tuning** teaches a model a new *skill, style, or behavior*. It alters the model's internal weights. (e.g., teaching a model to write in a specific brand's voice).
-   **RAG** provides a model with new *knowledge*. It gives the model external facts to work with for a specific task.

An effective SIE uses both: fine-tuning to ensure agents adhere to a client's style and RAG to ensure they operate with the client's facts. For more complex scenarios, the SIE employs methods beyond standard RAG, as detailed in [[Advanced Retrieval Techniques for AI Agents]].

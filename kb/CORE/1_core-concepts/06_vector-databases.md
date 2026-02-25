---
title: "Vector Databases"
id: "kb/CORE/concepts/vector-databases"
version: "2.0"
steward: "Adam Bernard"
updated: "2026-02-22"
status: "Active"
doc_type: "Reference"
summary: "Explains what Vector Databases are, their indexing strategies, and their critical role in enabling semantic and hybrid search for the SIE's RAG pipelines."
tags:
  - vector-database
  - embeddings
  - semantic-search
  - rag
  - ai-infrastructure
  - sie-engine
relations:
  - "kb/CORE/1_core-concepts/00_anatomy"
  - "kb/CORE/1_core-concepts/05_retrieval-augmented-generation-rag"
  - "kb/AI/3_methods/mcp/06_mcp-best-practices-for-rag-pipelines"
aliases:
  - Vector DB
  - Embedding Database

# --- AI & RAG Enhancement ---
semantic_summary: >
  Vector databases store high-dimensional embeddings to enable semantic search. They are a core component of the SIE's Knowledge Pipeline, utilizing indexing strategies like HNSW and IVF, and supporting hybrid search to power Retrieval-Augmented Generation (RAG). Advanced implementations use pgvector for secure, multi-tenant data isolation.
synthetic_questions:
  - "What is a vector database?"
  - "How do vector databases support RAG pipelines?"
  - "What is the difference between Flat, IVF, and HNSW vector indexes?"
  - "Why use pgvector for multi-tenant AI applications?"
  - "What is hybrid search in the context of vector databases?"
key_concepts:
  - "Vector Embeddings"
  - "Semantic Search"
  - "Hybrid Search"
  - "HNSW Indexing"
  - "pgvector"

# --- SEO & Publication ---
primary_keyword: "Vector Databases"
seo_title: "Vector Databases: Powering Semantic Search for AI Agents"
meta_description: "Learn what a vector database is and how it stores embeddings to power semantic search, hybrid retrieval, and RAG pipelines for AI systems."
excerpt: "Traditional databases find keywords; Vector Databases find meaning. Learn how vector embeddings enable semantic search and power the Strategic Intelligence Engine."
cover_image: "assets/images/vector-database-cover.png"
---

# Vector Databases

A **Vector Database** is a specialized database designed to store, manage, and search through high-dimensional data points called **vector embeddings**. It is a core infrastructural component of the Strategic Intelligence Engine's (SIE) Master Hub.

Unlike a traditional database that searches for exact matches based on keywords (e.g., finding the word "car"), a vector database enables **semantic search**. Semantic search finds information based on conceptual meaning and context (e.g., finding documents about "automobiles," "vehicles," and "EVs" when you search for "car").

## How Vector Databases Work

The vector search process is the foundation of the "Retrieval" step in [[05_retrieval-augmented-generation-rag|Retrieval-Augmented Generation (RAG)]]:

1. **Creating Embeddings:** All data ingested into the Master Hub is first passed through an embedding model. This model converts chunks of text into vector embeddings—long lists of numbers that represent the text's semantic meaning. 
2. **Storing Vectors:** The vector database stores these numerical vectors, each linked back to its original source text and enriched with descriptive metadata (e.g., source URL, date) to allow for pre-filtering and post-filtering [1]
3. **Searching with Vectors:** When an SIE agent receives a query, the query itself is converted into a vector embedding using the same model.
4. **Finding Nearest Neighbors:** The database performs a "nearest neighbor" search using mathematical calculations, such as cosine similarity or dot product, to find the vectors closest to the query vector on the conceptual map [1]
5. **Returning Context:** The database returns the original text chunks associated with these "closest" vectors to augment the AI agent's prompt.

## Indexing Strategies for Scale

To manage massive datasets efficiently, vector databases utilize specific indexing strategies to balance speed and accuracy [2]:

- **Flat Index (L2 distance):** Used for small databases where high precision is the absolute priority, as it compares the query against every single vector.
- **IVF (Inverted File Index):** Combines a flat index with quantization to group similar vectors into clusters, prioritizing optimization and speed for large databases.
- **HNSW (Hierarchical Navigable Small World):** The **Heuristic** standard for enterprise RAG. HNSW provides robust recall by utilizing multi-layered graph structures to quickly navigate to the nearest neighbors.

## Advanced Retrieval: Hybrid Search & Security

Relying solely on semantic meaning can sometimes miss highly specific technical terms. Modern vector databases (like Pinecone, Milvus, and FAISS) support **Hybrid Search**, which combines vector search with traditional keyword search to capture both high-level semantic matches and precise nomenclature [1]

Furthermore, for systems requiring strict multi-tenant data isolation, the SIE utilizes PostgreSQL with the `pgvector` extension. This architecture allows for transaction-safe linkage between relational metadata (like user access groups) and vector embeddings, ensuring agents only retrieve documents the user is explicitly authorized to view [3]

## Why Vector Databases are Essential for the SIE

- **They Power RAG:** A vector database is the engine that makes RAG possible. It allows an SIE agent to retrieve the most relevant facts from the Master Hub before generating a response, ensuring accuracy and reducing the Human Correction Tax.
- **They Understand Nuance:** By searching based on meaning, vector databases allow agents to find information that is contextually relevant but may not share any of the same keywords as the original query. 
- **They are Highly Scalable:** They are purpose-built to handle the massive scale required by modern AI systems, capable of searching through millions of vectors with incredible speed.

<br/>
<details class="copilot-sources"><summary class="copilot-sources__summary">Sources</summary>
<ul class="copilot-sources__list">
<li class="copilot-sources__item"><span class="copilot-sources__index">[1]</span><span class="copilot-sources__text"><a href="obsidian://open?file=kb%2FAI%2F3_methods%2Fmcp%2F06_mcp-best-practices-for-rag-pipelines.md">06_mcp-best-practices-for-rag-pipelines</a></span></li>
<li class="copilot-sources__item"><span class="copilot-sources__index">[2]</span><span class="copilot-sources__text"><a href="obsidian://open?file=kb%2FAI%2F3_methods%2Fmcp%2F07_mcp-rag-with-nvidia.md">07_mcp-rag-with-nvidia</a></span></li>
<li class="copilot-sources__item"><span class="copilot-sources__index">[3]</span><span class="copilot-sources__text"><a href="obsidian://open?file=kb%2FAI%2F2_agents%2F10_architecting-a-private-multi-user-rag-agent.md">10_architecting-a-private-multi-user-rag-agent</a></span></li>
</ul>
</details>
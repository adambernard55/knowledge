---
title: "Perplexity Search API"
id: 20251003221140
version: 2
Author: Adam Bernard
steward:
date: 2025-12-10
category: AI
category_id:
Excerpt: A technical overview of the Perplexity Search API, designed to provide developers with real-time, reliable, and fine-grained web search results for building AI agents and RAG pipelines.
Meta Description: Technical reference on the Perplexity Search API, detailing its features, comparison to the Sonar API, performance benchmarks, and developer resources.
Primary_Keyword: Perplexity Search API
Featured_Image:
doc_type: reference
relations:
aliases:
  - Perplexity API
  - Perplexity Search
last_updated: 2025-12-10
tags:
  - AI
  - API
  - Perplexity
  - search-api
  - agentic-ai
  - RAG
---

# Reference: Perplexity Search API

## 1. Overview

Perplexity has launched its Search API, providing developers with direct access to the core search infrastructure that powers its public answer engine. The API is designed to deliver real-time, reliable, and fine-grained search results from an index of hundreds of billions of webpages, specifically for powering AI agents, applications, and Retrieval-Augmented Generation (RAG) pipelines.

## 2. Key Features & Differentiators

- **Fine-Grained Snippets:** Unlike traditional search APIs that return full documents, the Search API delivers pre-ranked snippets. This reduces the need for developers to perform additional chunking and preprocessing.
- **Real-Time Freshness:** The indexing system is built for speed, updating tens of thousands of documents per second to ensure results are timely and reduce the risk of grounding LLMs on stale data.
- **AI-Powered Content Parsing:** An internal AI module parses and understands unstructured web data in real time, delivering clean, structured results.
- **High Performance:** The infrastructure is optimized for AI-heavy workloads, claiming high scores on both quality and latency.

## 3. Comparison: Search API vs. Sonar API

Perplexity offers two distinct APIs for different use cases:

- **Search API (New):**
    - **Output:** Provides raw, ranked web results and snippets.
    - **Use Case:** Intended for developers who need to ground other models, build custom agents, or integrate directly into RAG pipelines. It provides the source material, not the final answer.

- **Sonar API (Existing):**
    - **Output:** Returns synthesized, conversational answers.
    - **Use Case:** Best for applications that require a complete, ready-to-display answer, similar to the experience on the Perplexity website.

## 4. Performance and Evaluation

- **`search_evals` Framework:** Perplexity has open-sourced an evaluation framework to allow developers to test and compare the performance of different search APIs.
- **Performance Claims:** In its own benchmarks, Perplexity reports that the Search API outperforms competitors on both single-step queries and complex, multi-step agentic research tasks.
- **Cost Efficiency:** The company claims that infrastructure efficiencies allow it to offer this performance at a lower cost than competing services.

## 5. Developer Resources

To support integration, Perplexity provides a suite of tools for developers:
- **Developer Console:** For API key management and monitoring.
- **Documentation:** Comprehensive guides and API references.
- **Search SDK:** A software development kit designed to enable rapid prototyping and integration.

## 6. Strategic Importance

The Perplexity Search API positions itself as a critical infrastructure component for the growing field of agentic AI. By providing fresh, accurate, and raw web data, it serves as a foundational layer for developers building applications that require reliable, real-time information, filling a gap left by other retired or closed search APIs.
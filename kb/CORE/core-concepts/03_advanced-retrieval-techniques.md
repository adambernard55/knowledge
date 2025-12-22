---
title: "Advanced Retrieval Techniques for AI Agents"
id: "kb/CORE/concepts/advanced-retrieval"
version: "1.0"
steward: "Adam Bernard"
updated: "2025-11-27"
status: "Active"
doc_type: "reference_document"
summary: "Explores advanced methods beyond standard RAG for providing AI agents with precise, governed, and contextually-aware information from a knowledge base, enhancing their reasoning and decision-making capabilities."
meta_description: "Explore advanced retrieval techniques beyond standard RAG, including RAG on the Wire and hierarchical search, to enhance AI agent accuracy, governance, and reasoning."
keyword: "Advanced Retrieval Techniques"
excerpt: "While standard RAG is foundational, advanced retrieval techniques are crucial for building truly intelligent and trustworthy AI agents. This document explores methods like 'RAG on the Wire' for enforcing governance, 'Hierarchical Search' for precision, and the use of 'Negative Examples' to create behavioral guardrails. Learn how these strategies move beyond simple data lookup to provide the nuanced, context-aware information required by the Strategic Intelligence Engine (SIE)."
tags:
  - retrieval
  - rag
  - ai-agents
  - knowledge-base
  - sie-engine
  - rag-on-the-wire
  - hierarchical-search
relations:
  - "kb/CORE/00_anatomy"
aliases:
  - Advanced RAG
  - Agent Retrieval Strategies
---

# Advanced Retrieval Techniques for AI Agents

While standard Retrieval-Augmented Generation (RAG) and GraphRAG are foundational methods for connecting AI agents to a knowledge base, several advanced techniques offer greater control, efficiency, and nuance. As outlined in [[Fueling the SIE: Anatomy of an Agent Knowledge Base]], a multi-modal retrieval strategy is key to high performance. This document details some of the advanced techniques employed by the Strategic Intelligence Engine (SIE) to ensure its agents operate with the highest degree of accuracy and governance.

These methods are not replacements for RAG but are powerful enhancements that address specific challenges in providing context to agents.

## RAG on the Wire

"RAG on the Wire" is an architectural pattern where an intermediary service, or "agent gateway," sits between the application making an LLM call and the LLM itself. This gateway intercepts the request, performs a RAG-style lookup against the Master Hub, injects the retrieved context, and then forwards the augmented prompt to the LLM.

-   **How it Works:** The agent or user application makes a standard API call. The gateway intercepts it, enriches it with governed data, and then passes it on. The original application is often unaware this enrichment is happening.
-   **Strategic Value for SIE:** This is a powerful mechanism for enforcing governance. It ensures that no matter which agent or service is operating, it automatically adheres to the Master Hub's rules and conventions. It centralizes the logic for context injection, making the system more secure and maintainable.

## Hierarchical Search

Hierarchical search is a retrieval method that refines a query in stages, moving from broad categories to specific details. Instead of performing a single, massive semantic search across the entire knowledge base, the agent narrows the search space step-by-step.

-   **How it Works:** An agent tasked with "summarize last quarter's marketing performance" might first identify the "Quarterly Reports" category, then filter for "Marketing," then search within those documents for "performance metrics" and "key takeaways."
-   **Strategic Value for SIE:** This technique significantly improves both the speed and relevance of information retrieval. It mimics human expert reasoning, preventing the agent from being overwhelmed by irrelevant data and allowing it to find the precise information needed for a complex task.

## Negative Examples & Decision Trees

These techniques focus on providing explicit behavioral guardrails for an agent, moving beyond just providing factual knowledge.

-   **Negative Examples:** This involves explicitly programming what an agent **should not** say or do. This information is stored in the Master Hub and retrieved as part of the agent's system prompt or operational context. For example:
    -   *Content Agent:* "Do not use these 10 industry jargon terms."
    -   *Support Agent:* "Never promise a specific release date for a new feature."

-   **Decision Trees:** These are structured, machine-readable workflows that guide an agent through complex, multi-step processes or edge cases. They provide clear `IF-THEN` logic for navigating situations that require specific handling. For example:
    -   *Sales Agent:* "IF a lead's company size is >500 employees AND their industry is 'Finance', THEN retrieve the 'Enterprise Security Whitepaper' and use the 'Formal Outreach' communication template."

-   **Strategic Value for SIE:** Together, these techniques are critical for ensuring agent actions are safe, compliant, and aligned with brand strategy. They reduce the risk of hallucinations or incorrect actions in high-stakes scenarios, making the agents more reliable and trustworthy.
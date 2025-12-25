---
title: "Architecting a Private, Multi-User Agentic RAG System"
id: 202512250804
version: 1
Author: Adam Bernard
steward: Adam Bernard
date: 2025-12-25
category: AI Agents
Primary_Keyword: "self-hosted AI agent"
Meta Description: "A practical blueprint for building a secure, self-hosted, multi-user agentic chatbot using local LLMs, vector search, and a modular architecture for complete data privacy and control."
Excerpt: "Learn how to architect and build a private, multi-tenant agentic RAG system. This guide covers the components, data flows, and security principles for creating a self-hosted chatbot that provides personalized, secure access to user-specific documents."
tags:
  - ai-agent
  - rag
  - self-hosted
  - ollama
  - langgraph
  - multi-tenant
  - system-architecture
  - data-privacy
  - vector-search
---

# Architecting a Private, Multi-User Agentic RAG System

This document provides a practical blueprint for building a self-hosted, end-to-end platform that gives each user a personal, agentic chatbot. The system is designed for 100% privacy and full user control, leveraging local LLMs to eliminate external dependencies and token costs. The agent can autonomously perform vector searches on a secure knowledge base, accessing only the files that a user explicitly has permission to view.

## Core Architectural Principles

The system is designed around three primary operational flows, supported by a modular, six-component architecture.

1.  **User File Management:** Authenticated users can upload, delete, and manage access permissions for their documents.
2.  **Asynchronous Embedding & Storage:** Uploaded files are processed in the background to be chunked, embedded, and stored securely in a vector database, ensuring that access controls are maintained at the data level.
3.  **Agentic Chat & Retrieval:** A user interacts with their private agent, which uses tools like vector search to retrieve relevant information from authorized documents to inform its responses.

## System Components

The architecture consists of six key, loosely-coupled components:

- **1. Application Server (Python):** The core of the system, exposing API endpoints for the front-end and managing communication with the message queue.
- **2. Front-End (Streamlit/Angular):** The user interface for authentication, file management, and chat. Streamlit is effective for rapid prototyping, while a framework like Angular is suitable for a production-grade application.
- **3. Blob Storage (Minio):** A high-performance, S3-compatible object storage system for securely storing the original uploaded files.
- **4. Vector Database (PostgreSQL + pgvector):** A single database solution handling both relational data (users, metadata, access groups) and vector embeddings. The `pgvector` extension allows for powerful, permission-aware vector searches by joining tables, which is critical for enforcing multi-tenant data isolation.
- **5. LLM Host (Ollama):** A local service for running and managing open-source LLMs. This setup typically uses two models: a lightweight model for generating text embeddings and a more powerful model for chat and reasoning.
- **6. Message Queue (RabbitMQ):** An intermediary that decouples the front-end from heavy background processing. When a file is uploaded, a message is sent to the queue, allowing for an immediate response to the user while workers process the file asynchronously. This design enhances responsiveness and enables horizontal scaling.

## Operational Flows

### Flow 1: File Submission and Management

1.  A user authenticates via the front-end, receiving a token for API calls.
2.  The user uploads a file and assigns it to one or more access groups.
3.  The API validates the user token and sends the file to the Blob Storage.
4.  The file's metadata (including its storage location and access group information) is saved in the PostgreSQL database.
5.  A message containing the `file_id` is published to the RabbitMQ message queue.
6.  The API returns a success response to the user, while the embedding process is queued for background execution.

### Flow 2: Asynchronous Document Processing & Embedding

1.  A worker service consumes a message from the queue.
2.  It uses the `file_id` to retrieve the document's metadata and storage location from the database.
3.  The worker downloads the file from Blob Storage.
4.  The file content is extracted, split into smaller text chunks, and each chunk is converted into a numerical vector (embedding) via the local Ollama embedding model.
5.  The text chunks and their corresponding vectors are written to the PostgreSQL database, linked to the file's access-control information.

### Flow 3: Agentic Chat & Secure Retrieval

1.  A user sends a prompt to their private agent through the API.
2.  The system retrieves the recent conversation history to provide context.
3.  The agent's reasoning process, defined by a **LangGraph** workflow, is invoked.
4.  The LLM determines if it needs more information and decides whether to call a tool.
5.  If required, it executes the `vector-search` tool. The search query is filtered at the database level to only include document chunks the user is permitted to access.
6.  The retrieved context is incorporated into the LLM's reasoning process.
7.  The final, context-aware answer is generated and streamed back to the user.

## Key Technical Learnings & Best Practices

- **Integrated Vector Storage:** Using PostgreSQL with the `pgvector` extension simplifies the architecture by eliminating the need for a separate vector database. It allows for robust, transaction-safe linkage between relational metadata and vector embeddings, which is ideal for enforcing multi-tenant security.
- **Agentic Workflows with LangGraph:** LangGraph provides a clear and powerful way to define an agent's behavior as a state machine or graph, allowing it to autonomously decide when to use tools to answer a user's query.
- **Feasibility of Local Agents:** With tools like Ollama, running high-performance, private, and fully self-hosted agentic systems on commodity hardware is entirely feasible.
- **Loose Coupling for Scalability:** The use of a message queue and distinct components makes the system resilient and scalable. Individual parts (like embedding workers) can be scaled independently to handle increased load.
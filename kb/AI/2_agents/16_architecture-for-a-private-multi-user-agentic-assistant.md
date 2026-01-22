---
title: "Architecture for a Private, Multi-User Agentic Assistant"
id: "kb/AI/2_agents/16"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-01-22"
status: "Active"
doc_type: "Reference"
summary: "Provides a technical blueprint for a self-hosted, multi-tenant platform that gives each user a private, agentic chatbot with secure, permission-based document retrieval."
tags:
  - "ai"
  - "agentic-rag"
  - "system-architecture"
  - "self-hosted"
  - "multi-tenant"
  - "langgraph"
  - "ollama"
  - "security"
relations:
  - "kb/AI/2_agents/index.md"
  - "kb/AI/2_agents/13_reference-architecture-for-trustworthy-agentic-ai.md"
aliases:
  - "Private Agentic RAG"
  - "Multi-User Chatbot Architecture"
semantic_summary: "This document details the architecture for a self-hosted, multi-tenant agentic assistant. It uses a privacy-first stack including Ollama for local LLMs, Minio for blob storage, and Postgres with pgvector for permission-based vector search. The system's workflows for file management, asynchronous embedding, and agentic chat are orchestrated via a RabbitMQ message queue and a LangGraph agent."
synthetic_questions:
  - "How can you build a multi-tenant RAG system with per-user data isolation?"
  - "What is a good architecture for a self-hosted AI agent platform?"
  - "How does LangGraph fit into an agentic chat workflow?"
key_concepts:
  - "Multi-Tenancy"
  - "Agentic RAG"
  - "Self-Hosted AI"
  - "LangGraph"
  - "Ollama"
  - "pgvector"
  - "Permission-Based Retrieval"
  - "Asynchronous Embedding"
primary_keyword: "agentic assistant architecture"
meta_description: "Technical reference detailing the architecture, components, and workflows for building a secure, self-hosted, multi-user agentic RAG system."
---

# Architecture for a Private, Multi-User Agentic Assistant

## 1. System Overview

This document outlines the architecture for a self-hosted, end-to-end platform that provides each user with a personal, agentic chatbot. The system is designed to be secure, private, and multi-tenant, allowing the agent to autonomously perform vector searches on a per-user, permission-based set of documents.

### Key Principles
- **Privacy-First:** All components, including LLMs, are self-hosted to prevent data leaks and eliminate external dependencies.
- **Multi-Tenancy:** The system supports multiple users, each with their own private agent and isolated data.
- **Agentic RAG:** The chatbot is an agent equipped with tools (e.g., vector search) that it can autonomously decide to use to answer user queries.
- **Scalability:** The architecture uses a message queue for asynchronous processing, enabling horizontal scaling of worker nodes.

## 2. System Architecture

The system is composed of six key components that support three primary workflows: file management, document embedding, and chat.

### 2.1. Core Components

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **App** | Python (e.g., FastAPI) | The core application logic. Exposes APIs for the front-end and orchestrates background tasks via the message queue. |
| **Front-End** | Streamlit (Prototype) | User interface for authentication, file management (upload/delete), and chat interaction. |
| **Blob Storage** | Minio | An S3-compatible object storage system for securely storing raw user-uploaded files. |
| **(Vector) Database** | Postgres + `pgvector` | Manages relational data (users, groups, document metadata) and vector embeddings in a single system, enabling powerful, permission-based queries. |
| **LLM Host** | Ollama | Serves local language models for both text embeddings and chat generation, ensuring data privacy. |
| **Message Queue** | RabbitMQ | Decouples the API from heavy processing. Manages a queue of tasks (e.g., file embedding) for background workers, ensuring responsiveness and scalability. |

## 3. Core Workflows

### 3.1. Flow 1: User File Management

This flow describes the process of a user uploading a file and assigning access permissions.

1.  **Authentication:** User logs into the front-end and receives a JWT token for authenticating subsequent API calls.
2.  **File Upload:** User uploads a file and assigns it to one or more access groups.
3.  **API Request:** The front-end sends the file, group assignments, and token to the App's API.
4.  **Store File:** The App saves the raw file to Blob Storage (Minio).
5.  **Store Metadata:** The App records the file's metadata (name, storage location, owner, group permissions) in the Postgres database.
6.  **Queue Task:** The App publishes a message containing the `file_id` to the Message Queue (RabbitMQ) for background processing.
7.  **API Response:** The API immediately returns a success response to the user, ensuring the UI remains responsive.

### 3.2. Flow 2: Asynchronous Document Embedding

This background process is triggered by a message in the queue and makes the document's content searchable.

1.  **Consume Message:** A worker node retrieves a message with a `file_id` from the queue.
2.  **Fetch Metadata:** The worker queries the Postgres database for the document's metadata using the `file_id`.
3.  **Retrieve File:** The worker downloads the file from Blob Storage.
4.  **Process & Chunk:** The file's text content is extracted and split into smaller, semantically relevant chunks.
5.  **Generate Embeddings:** Each chunk is sent to the local Ollama embedding model to be converted into a numerical vector.
6.  **Store Chunks & Vectors:** The text chunks and their corresponding vectors are saved to the `pgvector` table in Postgres, linked to the original file's metadata and access control information.

### 3.3. Flow 3: Agentic Chat & Retrieval

This flow describes how a user interacts with their agent to get answers based on their private documents.

1.  **User Prompt:** The user sends a message through the front-end to the App's chat API.
2.  **Authentication:** The user's token is validated.
3.  **Context Retrieval:** The App retrieves the recent conversation history to provide context for the agent.
4.  **Invoke Agent:** The LangGraph agent is invoked with the user's prompt and conversation history.
5.  **Agent Reasoning:** The Ollama chat model reasons about the prompt and inspects its available tools. It determines if a tool call (e.g., vector search) is necessary.
6.  **Tool Execution (Vector Search):** If needed, the agent calls the vector search tool. The search query is executed against the Postgres database, **filtered to only include document chunks the current user has permission to access**.
7.  **Synthesize Response:** The agent incorporates the retrieved information into its reasoning and generates a final answer.
8.  **Stream Response:** The generated answer is streamed back to the user's front-end for a real-time experience.

## 4. Agent Logic & Tooling (LangGraph)

The agent's behavior is defined as a graph using LangGraph. This graph dictates the agent's reasoning loop.

-   **Graph Structure:** A simple loop where the LLM first reasons about the user's input.
-   **Tool Node:** If the LLM decides a tool is needed, the graph transitions to a tool execution node (e.g., calling the vector search function).
-   **Looping:** The output of the tool is passed back to the LLM, which re-evaluates if it has enough information to respond or if another tool call is needed.
-   **Final Response:** Once the LLM determines no more tools are required, it generates the final answer for the user.

## 5. Potential Enhancements

-   **Incremental Re-embedding:** Update embeddings for documents that change over time (e.g., for integrating an Obsidian vault).
-   **Citations:** Provide source information (file, page, chunk) for retrieved context to improve trust and explainability.
-   **Expanded Toolset:** Equip the agent with more tools, such as structured summarizers, SQL database access, or knowledge graph querying.
-   **Improved Frontend:** Replace the prototype UI with a more robust solution for better file management and user experience.
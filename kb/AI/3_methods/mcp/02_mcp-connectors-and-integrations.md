---
title: "MCP Connectors and Integrations: A Technical Guide"
id: "KB/AI/M-MCP-02"
version: "1.1"
steward: "Adam Bernard"
updated: "2026-02-07"
status: "Active"
doc_type: "Reference"
summary: "Explains how Model Context Protocol (MCP) connectors link AI agents to external systems like databases, APIs, and developer tools, enabling practical agentic workflows."
tags:
  - "mcp"
  - "model-context-protocol"
  - "ai-agents"
  - "integration"
  - "connectors"
  - "sdk"
  - "api"
relations:
  - "kb/AI/3_methods/mcp/01_mcp-foundations-and-architecture.md"
  - "kb/AI/2_agents/01_ai-agents-running-workflows.md"
aliases:
  - "MCP Connectors"
  - "AI Agent Integrations"

# --- AI & RAG Enhancement ---
semantic_summary: >
  This document details how Model Context Protocol (MCP) connectors serve as the bridge between AI agents and external systems. It covers the architecture, common integration patterns (local vs. remote), and provides examples of connectors for databases (Supabase), developer tools (Chrome DevTools), and platforms (WordPress). The guide also outlines best practices for security, discovery, and development using various SDKs.
synthetic_questions:
  - "What are MCP connectors and how do they work?"
  - "What are the different types of MCP connectors?"
  - "How do you integrate an AI agent with a database like Supabase using MCP?"
  - "What is the difference between local (stdio) and remote (HTTP) integration patterns?"
key_concepts:
  - "Model Context Protocol (MCP)"
  - "MCP Connectors"
  - "Agentic Integration"
  - "Tool Discovery"
  - "JSON-RPC"
  - "Supabase MCP"
  - "Chrome DevTools MCP"

# --- SEO & Publication ---
primary_keyword: "mcp connectors"
seo_title: "MCP Connectors: A Guide to AI Agent Integrations"
meta_description: "Learn how MCP connectors link AI agents to external systems like databases and APIs. This technical guide covers architecture, patterns, and examples."
excerpt: "Discover how Model Context Protocol (MCP) connectors work. This guide explains the architecture, integration patterns, and best practices for linking AI agents to real-world data and tools."
cover_image: ""
---

# MCP Connectors and Integrations

## 1. What Are MCP Connectors?

**Model Context Protocol (MCP)** connectors are the structured interfaces that link AI agents to outside applications and data. A connector exposes a catalog of **tools**, **resources**, and **prompts**, each with a clearly defined schema that allows an agent to discover and safely execute actions on external systems without needing direct API logic or credentials.

Connectors can be built for local utilities (files, databases) or remote platforms (Supabase, GitHub, WordPress), forming the web of interactivity that makes agentic AI practical.

## 2. Connector Architecture

| Layer | Purpose | Examples |
| :--- | :--- | :--- |
| **Server Layer** | Implements MCP spec endpoints and defines tools/resources. | `supabase-mcp`, `chrome-devtools-mcp` |
| **Descriptor (JSON)** | Declares the entry-point so the client knows how to invoke the server. | `mcp.json`, `~/.client/mcp_servers.json` |
| **Transport** | How messages flow: `stdio` for local CLI/IDE or `HTTP` for remote cloud servers. | `npx @supabase/mcp` or `https://mcp.supabase.com/mcp` |
| **Host Integration** | How the user’s AI environment registers and uses the connector. | Claude Desktop config, Cursor IDE settings |

All communication occurs via **JSON-RPC 2.0 requests** (`tools/call`, `resources/read`) and structured JSON schemas, ensuring cross-client compatibility.

## 3. Common Integration Patterns

### 3.1. Local (stdio)
-   **Transport:** `stdio` via a CLI command (`npx`, `uvx`).
-   **Use Case:** Agents running inside local IDEs (e.g., Cursor, LM Studio) that need access to the local filesystem or tools.
-   **Pros:** Full privacy and direct system access.

### 3.2. Remote (HTTP)
-   **Transport:** A public `https://.../mcp` endpoint.
-   **Use Case:** Integrating with cloud services and enterprise APIs.
-   **Pros:** Broad client compatibility (ChatGPT, Claude, Gemini).

## 4. Leading Example Connectors

| Connector                    | Purpose                                                                    | Key Integration Notes                                                                             |
| :--------------------------- | :------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------ |
| **Supabase MCP**             | Remote database and auth integration for agents.                           | Supports OAuth 2, Remote HTTP, and feature groups.                                                |
| **Chrome DevTools MCP**      | Gives AI direct browser debugging and performance analysis capabilities.   | Uses Puppeteer and DevTools protocol; ideal for developer agents.                                 |
| **WordPress.com Connector**  | Connects Claude to WordPress.com site data.                                | Official integration, uses OAuth 2.1 for secure, read-only access.                                |
| **Context7 Memory MCP**      | Persistent agent memory and RAG context service.                           | Supports multi-agent context sharing and vector store queries.                                    |
| **Google Dev Knowledge MCP** | Provides AI agents with access to official Google developer documentation. | Covers Firebase, Android, Google Cloud. Requires a Google Cloud API key and gcloud CLI for setup. |

## 5. SDKs for Connector Development

| SDK | Language | Description |
| :--- | :--- | :--- |
| **FastMCP** | Python | Lightweight framework for rapid prototyping of MCP servers. |
| **MCP PHP SDK** | PHP | Official, framework-agnostic SDK from the PHP Foundation and Symfony. |
| **ModelContextProtocol JS SDK** | TypeScript | Used to build npm-published servers like the Chrome DevTools MCP. |

These SDKs abstract the JSON-RPC boilerplate and provide helpers for tool declaration, schema validation, and server lifecycle management.

## 6. Security and Discovery

-   **Discovery:** Clients dynamically query servers using `tools/list` and `resources/list` to see available capabilities.
-   **Authentication:** Remote servers must use OAuth 2.1 with scopes. Local servers operate within the system user's trust boundary.
-   **Auditing:** Hosts should record full JSON-RPC exchanges for security and governance.

## 7. Best Practices for Integration Design

1.  **Atomic Scope:** Limit exposed tools to a single, clear domain (e.g., analytics, CMS).
2.  **Versioning:** Use semantic versioning for servers and tools to manage breaking changes.
3.  **Clear Schemas:** Provide explicit types and descriptions to improve agent performance.
4.  **Graceful Failure:** Return structured errors with codes to help agents self-correct.
5.  **Read-Only by Default:** Mark tools as `readonly` whenever possible to enhance safety.
6.  **Human-in-the-Loop:** Implement confirmation steps for any state-changing operations.

---
### See Also
-   [[kb/AI/3_methods/mcp/01_mcp-foundations-and-architecture|MCP Foundations and Architecture]]
-   [[kb/AI/1_models/1_specific-models/claude/03_claude-connector-for-wordpress|Claude Connector for WordPress.com]]
- 
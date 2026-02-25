---
title: "Model Context Protocol (MCP)"
id: "kb/CORE/concepts/mcp"
version: "2.0"
steward: "Adam Bernard"
updated: "2026-02-22"
status: "Active"
doc_type: "Reference"
summary: "Defines the Model Context Protocol (MCP) as the universal standard for AI agent communication, detailing its architecture, security, and role in the SIE."
tags:
  - mcp
  - ai-agents
  - interoperability
  - api-standard
  - sie-engine
  - knowledge-base
relations:
  - "kb/CORE/00_anatomy"
  - "kb/AI/3_methods/mcp/01_mcp-foundations-and-architecture"
  - "kb/AI/3_methods/mcp/02_mcp-connectors-and-integrations"
aliases:
  - MCP
  - Agent Communication Standard

# --- AI & RAG Enhancement ---
semantic_summary: >
  The Model Context Protocol (MCP) is an open standard using JSON-RPC 2.0 that standardizes how AI agents connect to data sources and tools. It utilizes a three-component architecture (Host, Client, Server) to replace custom API integrations, enabling dynamic context discovery and radical scalability for systems like the Strategic Intelligence Engine (SIE).
synthetic_questions:
  - "What is the Model Context Protocol (MCP)?"
  - "How does MCP differ from traditional custom APIs?"
  - "What are the three components of the MCP architecture?"
  - "How does MCP solve the token context problem for AI agents?"
  - "How does MCP work with Retrieval-Augmented Generation (RAG)?"
key_concepts:
  - "JSON-RPC 2.0"
  - "Host-Client-Server Architecture"
  - "Dynamic Context Discovery"
  - "Universal Agent Interoperability"

# --- SEO & Publication ---
primary_keyword: "Model Context Protocol"
seo_title: "Model Context Protocol (MCP): The Universal Standard for AI Agents"
meta_description: "Learn how the Model Context Protocol (MCP) standardizes AI agent communication, enabling radical scalability and interoperability for systems like the SIE."
excerpt: "The Model Context Protocol (MCP) is an emerging universal standard that acts as a 'universal translator' for AI agents, replacing custom API integrations with a single, scalable connection."
cover_image: "assets/images/mcp-architecture-cover.png"
---

# Model Context Protocol (MCP)

The Model Context Protocol (MCP) is an emerging universal standard designed to govern how AI agents interact with tools, data, and other agents. Think of it as a "universal translator" for agentic systems. Instead of building dozens of custom, one-off integrations, an agent or knowledge source can become "MCP-compliant," allowing it to communicate seamlessly with any other system that speaks the same language.

As noted in [[00_anatomy|Anatomy of a Knowledge Core]], MCP is poised to become the leading standard for agentic connections, fundamentally changing how systems like the Strategic Intelligence Engine (SIE) are built and scaled.

## Core Architectural Model

MCP defines a three‑component architecture built around clarity, portability, and separation of responsibilities [1]:

1. **Host:** The environment where users interact with the AI application (e.g., Claude Desktop, Cursor IDE). It manages sessions, user input, and consent.
2. **Client:** The logic component that translates the AI model's intentions into MCP protocol actions, managing the message exchange loop.
3. **Server:** A wrapper around real‑world resources (databases, APIs, files) that exposes a structured, discoverable interface to clients.

All communication between the client and server follows a defined **JSON‑RPC 2.0** pattern over approved transports, such as `stdio` for local, private access or `HTTP` for remote cloud integrations [1]

## Why is MCP Important for the SIE?

For the Strategic Intelligence Engine, adopting a standard like MCP is a critical strategic advantage. It directly addresses the challenges of scalability and integration that are central to the SIE's mission.

- **Radical Scalability:** The SIE's purpose is to activate a client's Master Hub, which often involves connecting to diverse data sources. With MCP, the SIE only needs to build one MCP-compliant connector, which can then interact with any MCP-compliant data source (like WordPress, Supabase, or GitHub) [2] This drastically reduces engineering overhead.
- **Dynamic Context Discovery:** Traditional integrations load all tool schemas upfront, which can consume massive amounts of an LLM's context window (the "Context Problem"). MCP enables dynamic discovery—agents query what tools exist and pull in only the parameters they need at the exact moment of execution, reducing token usage by up to 99% [3]
- **Interoperability:** MCP allows SIE agents to plug into any compatible system, future-proofing the engine and ensuring it can participate in a broader ecosystem of AI-powered tools without being locked into a proprietary architecture.

## Security by Design

MCP enforces security through strict architectural boundaries. Every component must act as a security boundary and validate all protocol exchanges independently [4]:
- **Hosts** manage user consent and session isolation.
- **Clients** enforce policies per server and manage credential storage.
- **Servers** handle tool execution, authentication (e.g., OAuth 2.1 for remote servers), and sandboxing. 

Unrecognized or unauthenticated calls are silently dropped and logged, ensuring that every MCP request fails securely [4]

## How MCP Differs from APIs and RAG

It's important to distinguish MCP from related concepts:

- **MCP vs. Custom APIs:** A traditional API is like a specific dialect with its own unique grammar. MCP is like a universal language. It's a standardized specification that sits *on top of* or *replaces* the need for custom API integrations. While traditional APIs require manual integration and custom HTTP calls, MCP offers standardized discovery (`tools/list`) and scoped permissions [1]
- **MCP vs. RAG (Retrieval-Augmented Generation):** RAG is a *technique*—a pattern for how an agent uses information. The agent *retrieves* data, *augments* its prompt, and *generates* a response. MCP is a *protocol* that standardizes the **retrieve** step of that process. An SIE agent uses the RAG pattern, but it makes its retrieval request *via the MCP protocol* to an MCP-compliant Master Hub. 

<br/>
<details class="copilot-sources"><summary class="copilot-sources__summary">Sources</summary>
<ul class="copilot-sources__list">
<li class="copilot-sources__item"><span class="copilot-sources__index">[1]</span><span class="copilot-sources__text"><a href="obsidian://open?file=kb%2FAI%2F3_methods%2Fmcp%2F01_mcp-foundations-and-architecture.md">01_mcp-foundations-and-architecture</a></span></li>
<li class="copilot-sources__item"><span class="copilot-sources__index">[2]</span><span class="copilot-sources__text"><a href="obsidian://open?file=kb%2FAI%2F3_methods%2Fmcp%2F02_mcp-connectors-and-integrations.md">02_mcp-connectors-and-integrations</a></span></li>
<li class="copilot-sources__item"><span class="copilot-sources__index">[3]</span><span class="copilot-sources__text"><a href="obsidian://open?file=kb%2FAI%2F3_methods%2Fmcp%2F11_introducing-mcp-cli.md">11_introducing-mcp-cli</a></span></li>
<li class="copilot-sources__item"><span class="copilot-sources__index">[4]</span><span class="copilot-sources__text"><a href="obsidian://open?file=kb%2FAI%2F3_methods%2Fmcp%2F04_mcp-security-and-compliance.md">04_mcp-security-and-compliance</a></span></li>
</ul>
</details>
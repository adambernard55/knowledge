---
title: "OpenAI Codex App Server Architecture"
id: "kb/AI/2_agents/23_openai-codex-app-server-architecture"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-02-23"
status: Active
doc_type: Reference
summary: "Technical reference on the Codex App Server, a bidirectional protocol decoupling AI agent logic from client surfaces via JSON-RPC."
tags: ["openai", "codex", "architecture", "agents", "protocol", "json-rpc"]
relations: 
  - "kb/AI/2_agents/index"
  - "kb/AI/3_methods/mcp/index"
  - "kb/AI/2_agents/13_reference-architecture-for-trustworthy-agentic-ai"
aliases: ["Codex App Server", "Codex Protocol"]

# AI & RAG Enhancement
semantic_summary: >
  The Codex App Server is a bidirectional JSON-RPC protocol that decouples the Codex 
  coding agent from client surfaces (CLI, IDE, Web). It introduces three conversation 
  primitives (Item, Turn, Thread) to manage state and rejects the Model Context Protocol (MCP) 
  in favor of richer session semantics required for IDE interactions like streaming diffs.
synthetic_questions:
  - "What is the OpenAI Codex App Server architecture?"
  - "Why did OpenAI reject MCP for the Codex App Server?"
  - "What are the conversation primitives in the Codex protocol?"
  - "How does the Codex App Server handle server-initiated requests?"
key_concepts:
  - "Codex App Server"
  - "Bidirectional JSON-RPC"
  - "Conversation Primitives (Item, Turn, Thread)"
  - "Agent Client Protocol (ACP)"

# Retrieval Optimization
primary_keyword: "Codex App Server Architecture"
seo_title: "OpenAI Codex App Server: Architecture and Protocol Reference"
meta_description: "A technical deep dive into OpenAI's Codex App Server, the bidirectional protocol powering Codex agents, and why it differs from MCP."
excerpt: "OpenAI's Codex App Server decouples agent logic from UI using a bidirectional JSON-RPC protocol. Learn about its core primitives and why it diverges from MCP."
cover_image: ""

# Access Control
target_audience: AI_Engineering
security_level: Internal
owner_team: AI_Engineering
---

# OpenAI Codex App Server Architecture

## 1. Architecture Overview
The **Codex App Server** is a bidirectional protocol designed to decouple the Codex coding agent's core logic from its various client surfaces (CLI, VS Code, Web, Xcode). It solves the "N-to-1" problem of agent integration by exposing a single, stable API that powers all experiences.

Unlike simple request/response models, the App Server manages complex, stateful agent interactions where a single user request unfolds into a structured sequence of actions, artifacts, and incremental progress updates.

## 2. Conversation Primitives
To model agentic workflows faithfully, the architecture defines three core primitives:

| Primitive | Definition | Lifecycle |
| :--- | :--- | :--- |
| **Item** | The atomic unit of input or output (User message, Agent message, Tool execution, Diff). | `started` → `delta` (streaming) → `completed` |
| **Turn** | A grouped sequence of Items produced by a single unit of agent work, initiated by user input. | Initiated by User → Concluded by Agent |
| **Thread** | The durable container for an ongoing session. Supports creation, resumption, forking, and archival. | Persisted event history for reconnection. |

## 3. Protocol Mechanics
The system uses **JSON-RPC** streamed as **JSONL** (JSON Lines) over `stdio`.

### 3.1 Server-Initiated Requests (Approval Flows)
A key differentiator of this protocol is support for server-initiated requests.
*   **Scenario:** The agent needs permission to execute a destructive command.
*   **Flow:** The server sends a request to the client → The Turn pauses → The Client responds with `allow` or `deny` → The Turn resumes.

## 4. Comparison with Model Context Protocol (MCP)
OpenAI explicitly evaluated and **rejected** the [[kb/AI/3_methods/mcp/index|Model Context Protocol (MCP)]] for the Codex App Server.

*   **The Limitation:** MCP's tool-oriented model could not cleanly map the rich session semantics required for a coding IDE.
*   **Specific Gaps:** MCP struggled to handle **streaming diffs**, complex **approval flows**, and **thread persistence** in a way that felt native to VS Code.
*   **Coexistence:** OpenAI still supports MCP for simpler, tool-based workflows but recommends the App Server for full-fidelity agent integrations.

## 5. Deployment Patterns
Clients embed the App Server using three primary patterns:

1.  **Local Child Process:** (VS Code, Desktop App) The client bundles a platform-specific binary and communicates via bidirectional `stdio`.
2.  **Decoupled Binary:** (Xcode) The client points to a separately updated App Server binary, allowing logic updates without client releases.
3.  **Remote Container:** (Web Runtime) A worker provisions a container with the App Server; the browser communicates via HTTP/SSE, keeping the UI lightweight while the server manages state.

## 6. Industry Context: App Server vs. ACP
The App Server exists alongside the **Agent Client Protocol (ACP)** (supported by Zed and JetBrains).
*   **Codex App Server:** Specific to the Codex harness and OpenAI ecosystem.
*   **ACP:** Aims to be the "Language Server Protocol (LSP)" for agents—a universal standard connecting *any* agent to *any* editor.

<br/>
<details class="copilot-sources"><summary class="copilot-sources__summary">Sources</summary>
<ul class="copilot-sources__list">
<li class="copilot-sources__item"><span class="copilot-sources__index">[1]</span><span class="copilot-sources__text">[[23_openai-codex-app-server-architecture]]</span></li>
</ul>
</details>
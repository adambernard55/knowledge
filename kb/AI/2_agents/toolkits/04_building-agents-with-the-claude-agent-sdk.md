---
title: "Building Agents with the Claude Agent SDK"
id: "KB/AI/A-T-04"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-02-07"
status: "Active"
doc_type: "Reference"
summary: "A practical guide to developing AI agents with the Claude Agent SDK, covering core principles like the agentic feedback loop, subagents, tool design, and verification."
tags:
  - "ai"
  - "claude"
  - "anthropic"
  - "sdk"
  - "agentic-workflow"
  - "developer-tools"
  - "mcp"
  - "context-engineering"
relations:
  - "kb/AI/1_models/1_specific-models/3_claude.md"
  - "kb/AI/1_models/1_specific-models/claude/01_creator-of-claude-code.md"
  - "kb/AI/2_agents/00_introduction-to-ai-agents.md"
aliases:
  - "Claude Agent SDK"
  - "Anthropic Agent SDK"
  - "Claude Agent Design"

# --- AI & RAG Enhancement ---
semantic_summary: >
  This document is a technical guide to the Claude Agent SDK, which enables LLMs to function as tool-using software agents. It details the core 'agentic feedback loop' (Gather, Act, Verify), and key architectural components including context management via a filesystem, the use of subagents for parallelism, and the design of effective tools (Bash, Code, MCP). The guide emphasizes building reliable agents through verification loops and provides best practices for production-grade agentic systems.
synthetic_questions:
  - "What is the Claude Agent SDK and what is its purpose?"
  - "What is the 'agentic feedback loop' in the Claude Agent SDK?"
  - "How do subagents work in the Claude ecosystem?"
  - "What are the best practices for designing tools for Claude agents?"
  - "How does the Claude Agent SDK handle verification and self-correction?"
key_concepts:
  - "Claude Agent SDK"
  - "Agentic Feedback Loop"
  - "Subagents"
  - "Model Context Protocol (MCP)"
  - "Verification Loops"
  - "Tool Design"
  - "Context Management"
---
# Building Agents with the Claude Agent SDK

## Executive Overview

The **Claude Agent SDK** transforms Large Language Models (LLMs) like Claude into capable, tool-using software agents. It extends a model’s reasoning by granting it access to a computer-like environment, giving it permission to run code, search files, and orchestrate multi-step workflows. Originally developed for **Claude Code**, the SDK is now a general-purpose foundation for agentic design.

This guide covers the core design patterns for developing reliable agents, including the agentic feedback loop, subagents, tool design, and output verification.

## 1. Core Principle: The Agentic Feedback Loop

Every Claude agent operates on a closed feedback loop of reasoning and verification, which minimizes errors and encourages adaptive self-correction.

`Gather context → Take action → Verify work → Repeat`

| Phase | Objective | Core Functions |
| :--- | :--- | :--- |
| **Gather Context** | Collect relevant data and history. | File search, semantic search, API retrieval. |
| **Take Action** | Execute reasoning and compute tasks. | Run tools, bash scripts, or generate code. |
| **Verify Work** | Evaluate or self-check outputs. | Use rules, visual feedback, or judge models. |

The agent persists in this loop until it achieves a verifiable outcome aligned with its task parameters.

## 2. Key Architectural Components

### 2.1. Context Management: The Agent's "Computer"

Providing Claude with access to system-level tools is the key to unlocking its autonomy. The SDK facilitates this by managing different types of context.

-   **File System Access:** Allows the agent to directly read, create, edit, and organize files, creating a form of persistent memory.
-   **Context Folders:** Structured directories can serve as dedicated knowledge stores (e.g., `conversations/`, `logs/`).
-   **Agentic Search:** Uses system utilities like `grep` and `tail` for efficient, transparent scanning of large files, which is often more precise than semantic search for specific data retrieval.

### 2.2. Subagents: Parallelism and Context Isolation

**Subagents** are lightweight child processes launched by a parent agent to handle specific, isolated tasks. They offer two main advantages:

1.  **Parallelization:** Run multiple search, analysis, or data processing tasks concurrently.
2.  **Context Isolation:** Each subagent has its own memory. Only the essential results are returned to the parent, preventing context window bloat and improving focus.

This modular approach is foundational for building complex, multi-agent ecosystems.

### 2.3. Tools & Actions: Code, Bash, and MCP

Agents act through "tools"—explicit, well-defined capabilities registered in the SDK.

-   **Custom Tools:** Design atomic, single-responsibility functions with clear documentation and input validation.
-   **Bash & Scripting:** Allow the agent to run sandboxed system commands (`grep`, `python`, etc.) for flexible data parsing, testing, and file transformations.
-   **Code Generation:** Tasking the agent to generate and execute code (Python, SQL) makes its actions deterministic, auditable, and verifiable through standard logic like return codes and assertions.
-   **Model Context Protocol (MCP):** MCP provides standardized connectors to external systems (Slack, GitHub, Asana), handling authentication and API calls automatically. This allows developers to integrate complex services as simple tools.

### 2.4. Verification Loops: Building Self-Checking Agents

Verification closes the feedback loop, enabling agents to detect and fix their own errors.

-   **Rule-Based Evaluation:** Define validation logic (like linting) to check outputs against a schema or format rules. The agent receives specific error feedback upon failure, allowing it to self-correct.
-   **Visual Feedback:** For UI tasks, agents can use tools like Playwright to render HTML, capture screenshots, and visually compare the output against a desired state.
-   **LLM-as-Judge:** A secondary "judge" agent can be used to review an output for qualitative aspects like tone, style, or reasoning integrity.

## 3. Implementation Best Practices

| Domain | Recommendation |
| :--- | :--- |
| **Tool Design** | Define minimal, composable tool actions. Avoid overlapping responsibilities. |
| **Context Management** | Enable automatic summarization or offloading when the context window approaches its limit. |
| **Parallelization** | Use subagents for long or repetitive subtasks to conserve the parent agent's context. |
| **Security** | Always sandbox code execution and restrict system/network access to only what is necessary. |
| **Testing & Governance** | Run regular evaluation scripts ("evals") to monitor task success rates, self-correction cycles, and tool accuracy. |

## 4. Getting Started

1.  **Install the SDK:** `pip install claude-agent-sdk`
2.  **Define Tools and Memory:** Register the agent's core capabilities and persistent storage.
3.  **Implement the Feedback Loop:** Structure the agent's logic around the Gather -> Act -> Verify cycle.
4.  **Add MCP Integrations:** Connect to external services like GitHub or Slack.
5.  **Iterate and Evaluate:** Use automated tests and logs to monitor and improve agent performance.

---
## See Also
-   [[kb/AI/2_agents/00_introduction-to-ai-agents|Introduction to AI Agents]]
-   [[kb/AI/1_models/1_specific-models/claude/01_creator-of-claude-code|The Workflow of Claude Code's Creator]]
-   [[kb/AI/3_methods/11_agentic-context-engineering|Agentic Context Engineering]]

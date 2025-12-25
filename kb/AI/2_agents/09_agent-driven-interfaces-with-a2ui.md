---
title: Agent-Driven Interfaces with A2UI
summary: An overview of Google's A2UI, an open-source protocol that allows AI agents to securely and declaratively describe user interfaces in a JSON format, which client applications can render using their own native components.
seo_category: agents
difficulty: intermediate
last_updated: 2025-12-25
kb_status: draft
tags:
  - ai-agents
  - a2ui
  - user-interface
  - agent-development
  - google
  - protocol
related_topics:
  - "[[00_introduction-to-ai-agents]]"
  - "[[02_how-to-build-fullstack-agent-applications]]"
  - "[[08_designing-effective-agent-tools]]"
primary_keyword: "A2UI protocol"
meta_description: "Learn about Google's A2UI, an open-source protocol that enables AI agents to securely describe user interfaces as declarative JSON, allowing for rich, native, and framework-agnostic agent-driven applications."
excerpt: "A2UI (Agent-to-User Interface) is an open-source protocol from Google that allows AI agents to 'speak UI.' It enables agents to request and describe interactive user interfaces using a secure, declarative JSON format, which client applications then render with their own native components."
---

# Agent-Driven Interfaces with A2UI

A2UI (Agent-to-User Interface) is an open-source specification and library set introduced by Google. It establishes a standard protocol for AI agents to "speak UI"—that is, to request and describe interactive user interfaces without sending executable code. This allows for richer, more secure, and more efficient user interactions compared to traditional text-only responses.

### The Problem A2UI Solves

Most chat-based agents are limited to text-based conversations. For complex tasks like booking an appointment or filling out a form, this results in a slow, multi-turn dialogue. The ideal user experience would be a native form with interactive elements like date pickers and buttons.

A2UI solves this by allowing the agent to send a structured, declarative JSON payload that describes the desired UI. The client application then interprets this payload and renders it using its own native UI components (e.g., React, Angular, SwiftUI, Flutter).

This approach addresses several key challenges:
- **Security:** By sending data (JSON) instead of executable code (HTML/JavaScript), A2UI prevents UI injection attacks and eliminates the risks associated with running arbitrary code from a remote source.
- **Consistency:** The client application controls the final rendering, ensuring the UI is visually consistent with the host application's branding and design system.
- **Portability:** A single agent can power interfaces across multiple platforms (web, mobile, desktop) because the A2UI payload is framework-agnostic.

### Core Design Principles

A2UI is built on three core principles:

1.  **Security First:** The protocol is declarative. The agent can only request UI components from a pre-approved catalog maintained by the client. This ensures the host application retains full control.
2.  **LLM-Friendly Representation:** The UI is described as a flat list of components with identifier references. This structure is easier for LLMs to generate, stream, and update incrementally, allowing for progressive rendering as the agent works.
3.  **Framework Agnostic:** The agent describes the UI's structure and data model, not its implementation. The client is responsible for mapping this description to its native widgets, enabling broad compatibility.

### How It Works: Architecture and Data Flow

1.  A user interacts with an agent.
2.  The agent's LLM generates an A2UI response—a JSON payload describing the required UI components, layout, and data bindings.
3.  This payload is streamed to the client application.
4.  The client's A2UI renderer library parses the JSON and maps each component to a native widget from its trusted catalog.
5.  The native UI is displayed to the user.
6.  User actions (e.g., button clicks) are sent back to the agent as events, which can trigger further updates to the UI.

This standard provides a critical architectural layer for building sophisticated, interactive, and secure [[AI Agents]].

---

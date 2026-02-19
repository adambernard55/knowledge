---
title: "Google WebMCP: Direct Agent-Website Interaction"
id: "KB/AI/MCP/16"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-02-16"
status: "Active"
doc_type: "Reference"
summary: "Overview of Google's Web Model Context Protocol (WebMCP), enabling websites to expose structured tools to AI agents via Chrome."
tags:
  - "mcp"
  - "google"
  - "ai-agents"
  - "web-standards"
  - "chrome"
relations:
  - "kb/AI/3_methods/mcp/05_mcp-reference-and-use-cases"
  - "kb/AI/3_methods/mcp/15_google-developer-knowledge-api-mcp"
aliases:
  - "WebMCP"
  - "Chrome Agent Tools"
target_audience: "Engineering"
security_level: "Public"
owner_team: "Engineering"
semantic_summary: "Google's Web Model Context Protocol (WebMCP) allows websites to expose structured tools directly to AI agents via Chrome. It offers two integration paths: a Declarative HTML API for simple forms and an Imperative JavaScript API for complex workflows, significantly improving agent reliability over screen scraping."
synthetic_questions:
  - "What is Google WebMCP?"
  - "How does WebMCP differ from screen scraping for AI agents?"
  - "How do I implement WebMCP on my website?"
key_concepts:
  - "Web Model Context Protocol"
  - "Declarative API"
  - "Imperative API"
  - "navigator.modelContext"
primary_keyword: "Google WebMCP"
seo_title: "Google WebMCP: Standardizing AI Agent-Website Interactions"
meta_description: "Learn about Google's Web Model Context Protocol (WebMCP), a new standard enabling direct, structured interactions between AI agents and websites via Chrome."
excerpt: "Google's WebMCP transforms Chrome into an agent platform, allowing websites to expose structured tools via HTML and JS, replacing fragile screen scraping."
cover_image: ""
---

# Google WebMCP: Direct Agent-Website Interaction

Google is officially turning Chrome into a playground for AI agents with the **Web Model Context Protocol (WebMCP)**. Announced alongside the **Early Preview Program (EPP)**, this protocol allows websites to communicate directly to AI models. Instead of the AI "guessing" how to use a site via screen scraping, the site explicitly tells the AI exactly what tools are available.

## 1. The Problem: Screen Scraping vs. Structured Context

Current AI agents often treat the web like a picture (Vision-Language Models). They "look" at the UI and try to find the "Submit" button. If the button moves 5 pixels or changes color, the agent might fail. This method is slow, breaks easily, and consumes massive amounts of compute.

**WebMCP** replaces this guesswork with structured data. It turns a website into a set of **capabilities**. For developers, this means you no longer have to worry about an AI breaking your frontend. You simply define what the AI can do, and Chrome handles the communication.

## 2. How WebMCP Works: 2 Integration Paths

Developers can choose between two ways to make a site "agent-ready."

### 2.1 The Declarative Approach (HTML)
This is the simplest method. You can expose a website’s functions by adding new attributes to standard HTML tags.

-   **Attributes:** Use `toolname` and `tooldescription` inside `<form>` tags.
-   **The Benefit:** Chrome automatically reads these tags and creates a schema for the AI. If you have a "Book Flight" form, the AI sees it as a structured tool with specific inputs.
-   **Event Handling:** When an AI fills the form, it triggers a `SubmitEvent.agentInvoked`. This allows your backend to distinguish between human and machine requests.

### 2.2 The Imperative Approach (JavaScript)
For complex Single Page Applications (SPAs), the Imperative API provides deeper control.

-   **The Method:** Use `navigator.modelContext.registerTool()`.
-   **The Logic:** You define a tool name, a description, and a JSON schema for inputs.
-   **Real-time Execution:** When the AI agent wants to "Add to Cart," it calls your registered JavaScript function. This happens within the user’s current session, meaning the AI doesn’t need to re-login or bypass security headers.

## 3. The Technical Stack: `navigator.modelContext`

For AI developers, the core of this update lives in the new `modelContext` object in the browser API.

| Method | Purpose |
| :--- | :--- |
| `registerTool()` | Makes a function visible to the AI agent. |
| `unregisterTool()` | Removes a function from the AI’s reach. |
| `provideContext()` | Sends extra metadata (like user preferences) to the agent. |
| `clearContext()` | Wipes the shared data to ensure privacy. |

## 4. Performance and Efficiency

Moving from vision-based browsing to WebMCP-based interaction offers three key improvements:

1.  **Lower Latency:** No waiting for screenshots to upload and be processed by a vision model.
2.  **Higher Accuracy:** Models interact with structured JSON data, reducing hallucination and click errors.
3.  **Reduced Costs:** Sending text-based schemas is significantly cheaper than processing high-resolution video/images.

## 5. Security First

WebMCP is designed as a "permission-first" protocol. The AI agent cannot execute a tool without the browser acting as a mediator. In many cases, Chrome will prompt the user (e.g., "Allow AI to book this flight?") before the final action is taken. This keeps the user in control while allowing the agent to do the heavy lifting.

---

### See Also
-   [[kb/AI/3_methods/mcp/05_mcp-reference-and-use-cases|MCP Reference and Use Cases]]
-   [[kb/AI/3_methods/mcp/15_google-developer-knowledge-api-mcp|Google Developer Knowledge API & MCP]]
---
title: "Google Developer Knowledge API & MCP Server"
id: "KB/AI/M-MCP-15"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-02-07"
status: "Active"
doc_type: "Reference"
summary: "A guide to Google's Developer Knowledge API and official MCP server, which provide programmatic access to Google's developer documentation for AI agents."
tags:
  - "mcp"
  - "google"
  - "api"
  - "developer-tools"
  - "documentation"
  - "agentic-integration"
  - "knowledge-api"
relations:
  - "kb/AI/3_methods/mcp/01_mcp-foundations-and-architecture.md"
  - "kb/AI/3_methods/mcp/02_mcp-connectors-and-integrations.md"
aliases:
  - "Google Developer Knowledge API"
  - "Google MCP Server"

# --- AI & RAG Enhancement ---
semantic_summary: >
  This document details the Google Developer Knowledge API and its official Model Context Protocol (MCP) server. These tools provide a canonical, machine-readable gateway to Google's public developer documentation for platforms like Firebase, Android, and Google Cloud. By connecting to the MCP server, AI assistants can retrieve fresh, accurate documentation as Markdown, enabling more reliable implementation guidance and troubleshooting.
synthetic_questions:
  - "What is the Google Developer Knowledge API?"
  - "How does the Google Developer Knowledge MCP server work?"
  - "How can I give my AI agent access to official Google developer documentation?"
  - "What are the steps to enable the Developer Knowledge MCP server?"
key_concepts:
  - "Developer Knowledge API"
  - "Model Context Protocol (MCP)"
  - "Google Cloud"
  - "Firebase"
  - "Android"
  - "Agentic Tools"
  - "Documentation API"
---

# Google Developer Knowledge API and MCP Server

Google has released the public preview of the **Developer Knowledge API** and an associated **Model Context Protocol (MCP) server**. These tools provide a canonical, machine-readable gateway to Google’s official developer documentation, ensuring AI agents and developer tools have access to the most accurate and up-to-date information.

## 1. The Developer Knowledge API

The [Developer Knowledge API](https://console.cloud.google.com/start/api?id=developerknowledge.googleapis.com) is designed to be the programmatic source of truth for Google’s public documentation. Instead of relying on outdated training data or fragile web-scraping, developers can search and retrieve official documentation pages as Markdown.

### Key Features
-   **Comprehensive Coverage:** Access documentation from Firebase, Android, Google Cloud, and more.
-   **Search and Retrieve:** Find relevant documentation pages and then retrieve the full Markdown content.
-   **Freshness:** During the public preview, documentation is re-indexed within 24 hours of an update.

## 2. The Official MCP Server

Alongside the API, Google has released an official MCP server. By connecting this server to a compatible IDE or AI assistant, developers can empower the agent to "read" Google’s documentation in real-time.

This enables more reliable agentic workflows, such as:
-   **Implementation Guidance:** "What is the best way to implement push notifications in Firebase?"
-   **Troubleshooting:** "Check the docs to find out how to fix the ApiNotActivatedMapError in the Maps API."
-   **Comparative Analysis:** "Compare Google Cloud Run and Cloud Functions for this specific use case."

## 3. Getting Started

1.  **Create an API Key:** Generate and restrict an API key for the Developer Knowledge API in your Google Cloud project's [Credentials page](https://console.cloud.google.com/apis/credentials).
2.  **Enable the MCP Server:** Using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk), run the following command:
    ```bash
    gcloud beta services mcp enable developerknowledge.googleapis.com --project=PROJECT_ID
    ```
3.  **Configure Your Tool:** Update your AI assistant's configuration file (e.g., `mcp_config.json`) to include the server. Detailed steps are available in the [official documentation](https://developers.google.com/knowledge/mcp#config-api).

## 4. Future Roadmap

While the preview focuses on providing unstructured Markdown, future plans include support for structured content like code sample objects and API reference entities, as well as expanding the documentation corpus and reducing re-indexing latency.

---

### See Also
-   [[kb/AI/3_methods/mcp/02_mcp-connectors-and-integrations|MCP Connectors and Integrations]]

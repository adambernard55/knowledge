---
title: "Claude Connector for WordPress.com"
id: "KB/AI/M-CL-03"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-02-07"
status: "Active"
doc_type: "Reference"
summary: "Guide to the official WordPress.com connector for Claude, enabling secure, read-only access to site data via the Model Context Protocol (MCP) and OAuth 2.1."
tags:
  - "claude"
  - "wordpress"
  - "mcp"
  - "connector"
  - "integration"
  - "anthropic"
  - "oauth"
relations:
  - "kb/AI/1_models/1_specific-models/3_claude.md"
  - "kb/AI/3_methods/mcp/02_mcp-connectors-and-integrations.md"
aliases:
  - "WordPress Claude Connector"
  - "Claude WordPress Integration"

# --- AI & RAG Enhancement ---
semantic_summary: >
  This document details the official WordPress.com connector for Claude, the first of its kind for a WordPress host. Built on the Model Context Protocol (MCP) and secured with OAuth 2.1, the connector allows users to grant Claude read-only access to their site's data. This enables Claude to answer questions and provide insights based on real site traffic, comments, and content history directly within the Claude interface.
synthetic_questions:
  - "How do I connect Claude to my WordPress.com site?"
  - "What can the WordPress.com Claude Connector do?"
  - "Is the Claude Connector for WordPress.com secure?"
  - "What is the Model Context Protocol (MCP) used for in the WordPress connector?"
key_concepts:
  - "Claude Connector"
  - "WordPress.com"
  - "Model Context Protocol (MCP)"
  - "OAuth 2.1"
  - "AI Integration"
  - "Site Analytics"
---

# Official Claude Connector for WordPress.com

WordPress.com has launched an official, supported connector for Claude, allowing users to safely connect the AI agent to their site's real-time data. This partnership builds on WordPress.com's existing Model Context Protocol (MCP) infrastructure and OAuth 2.1 support to provide a secure, easy-to-use integration.

The connector is available in Claude’s official connectors directory, removing setup friction and providing clear, revocable permissions.

![A screenshot of the WordPress.com Connector in the Claude connectors directory](https://en-blog.files.wordpress.com/2026/02/claude-connector-wordpress-com-2.png)

## How to Connect

Setting up the connector requires a few simple steps:

1.  **Enable MCP:** Ensure MCP is enabled on your WordPress.com account (available on paid plans).
2.  **Configure Tools:** Specify which tools you want to make available to Claude via the MCP settings.
3.  **Add Connector in Claude:** In Claude's settings, browse the connectors directory, search for "WordPress.com," and click to connect.
4.  **Authorize Access:** You will be prompted to log in to WordPress.com and grant secured, read-only access to your sites via OAuth 2.1.

![The grant access modal in Claude for the WordPress.com connector](https://en-blog.files.wordpress.com/2026/02/wordpress-com-claude-connector-authorization.png)

This connection gives Claude **read-only access** to your site content; it cannot create, delete, or update posts. Access can be revoked at any time from either platform.

## Key Capabilities & Use Cases

Once connected, Claude can answer questions using your site's live data, not generic information. This unlocks powerful, natural language queries for site analysis.

**Example Prompts:**

-   `"Show me my site’s traffic for the last 30 days."`
-   `"Summarize recent comments across my site."`
-   `"Which posts haven’t been updated in over a year?"`
-   `"Show me pages with high traffic but low engagement."`

These prompts leverage the same data and tools available in the WordPress.com dashboard, but are surfaced through an intuitive conversational interface.

![An example prompt in Claude using the WordPress.com connector](https://en-blog.files.wordpress.com/2026/02/claude-connector-prompt-example-wordpress-com.png)

This official partnership ensures the connector will evolve alongside both platforms, providing a stable and increasingly capable integration for WordPress.com users.


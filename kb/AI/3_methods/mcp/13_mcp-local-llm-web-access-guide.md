---
title: "Connecting Local LLMs to the Web with MCP"
id: "kb/AI/mcp/13"
version: "1.0"
steward: "Adam Bernard"
updated: 2026-01-10
status: "Active"
doc_type: "Reference"
summary: "A practical guide on how to give local LLMs real-time web access using the Model Context Protocol (MCP) and open-source search tools."
tags:
  - "mcp"
  - "local-llm"
  - "web-access"
  - "lm-studio"
  - "tutorial"
  - "brave-search"
  - "tavily"
relations:
  - "kb/AI/3_methods/mcp/08_using-mcp-servers-with-local-llms.md"
  - "kb/AI/3_methods/mcp/12_building-a-local-mcp-client.md"
aliases:
  - "MCP Web Access Guide"
  - "Local LLM Web Browsing"
semantic_summary: "This tutorial provides step-by-step instructions for connecting locally-run large language models (LLMs) to the internet using the Model Context Protocol (MCP). It covers the configuration of tools like Brave Search, Tavily, and DuckDuckGo within applications like LM Studio to enable private, real-time web browsing and data fetching without relying on major corporate APIs."
synthetic_questions:
  - "How to give a local LLM web access?"
  - "How to use MCP servers in LM Studio?"
  - "How to set up Brave Search with a local AI?"
  - "How can I make my local LLM browse the web privately?"
key_concepts:
  - "MCP servers"
  - "local LLM"
  - "tool calling"
  - "web browsing"
  - "LM Studio"
  - "data privacy"
primary_keyword: "MCP web access"
seo_title: "How to Give Local LLMs Web Access with MCP: A Complete Guide"
meta_description: "Learn how to give your local AI models real-time web browsing powers using the Model Context Protocol (MCP). A step-by-step guide for LM Studio."
excerpt: "A complete guide to giving local LLMs web access with MCP. Configure Brave Search, Tavily, and more in LM Studio for private, real-time browsing."
cover_image: ""
---

# The Complete Guide to MCP: Giving Your AI Web Superpowers

With Model Context Protocol (MCP) servers, you can give even lightweight, locally-run models the ability to search the web, analyze articles, and access real-time data—all while maintaining complete privacy and without API fees.

Tools like Brave Search, Tavily, and DuckDuckGo offer generous free tiers, making it possible to create a private "SearchGPT" on your own machine.

### Core Concepts

- **Model Context Protocol (MCP):** An open standard that allows AI models to connect with external tools and data sources. Instead of a rigid API call, MCP allows the model to determine which tool to use to fulfill a user's need.
- **Tool Calling (Function Calling):** The mechanism that enables an AI model to recognize when it needs external information and invoke the appropriate function (or MCP tool) to get it. Without tool-calling support, a model is limited to its training data.

Here’s how to give these superpowers to your local model.

## Technical Requirements and Setup

- **Node.js:** Must be installed on your computer.
- **Python:** Should be installed.
- **Local AI Application:** An application that supports MCP, such as **LM Studio** (version 0.3.17+), Claude Desktop, or Cursor IDE.
- **Tool-Calling Model:** A local model with tool-calling capabilities.

Good examples of local models that support tool-calling include GPT-oss, DeepSeek R1, Jan-v1-4b, and Llama-3.2 Instruct. In LM Studio, these models are often marked with a hammer icon.

## Setting Up Search Engines

Configuration is managed through a single `mcp.json` file. In LM Studio, you can access this via the settings interface. Each MCP server entry requires a name, the command to run it, and any environment variables (like API keys).

### DuckDuckGo (Easiest Setup)

1.  Go to [lmstudio.ai/danielsig/duckduckgo](https://lmstudio.ai/danielsig/duckduckgo) and click "Run in LM Studio."
2.  Go to [lmstudio.ai/danielsig/visit-website](https://lmstudio.ai/danielsig/visit-website) and do the same.

Your model now has basic web search and page-reading capabilities.

### Brave Search (Privacy-Focused)

Brave Search runs on an independent index and offers 2,000 free queries per month.

1.  Sign up at [brave.com/search/api](https://brave.com/search/api) to get your API key.
2.  In LM Studio, go to Settings (wrench icon) > Program > Edit mcp.json.
3.  Paste the following configuration, replacing the placeholder with your API key:

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your_brave_api_key_here"
      }
    }
  }
}
```

### Tavily (Versatile Search)

Tavily provides 1,000 free credits per month and offers specialized search for news, code, and images.

1. Create an account at [app.tavily.com](https://app.tavily.com/) and generate your API key.
2. Paste the following into your `mcp.json`, replacing the placeholder with your key:

```json
{
  "mcpServers": {
    "tavily-remote": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.tavily.com/mcp/?tavilyApiKey=YOUR_API_KEY_HERE"]
    }
  }
}
```

## Reading and Interacting with Websites

### MCP Fetch (Reading Full Articles)

Search engines return snippets, but MCP Fetch retrieves the complete content of a webpage and converts it to AI-friendly markdown.

1. Install `uvx`, a Python package installer: `pip install uvx`.
2. Add this configuration to your `mcp.json`:

```json
{
  "mcpServers": {
    "fetch": {
      "command": "uvx",
      "args": [
        "mcp-server-fetch"
      ]
    }
  }
}
```

You can now ask your model to summarize or analyze entire articles by providing a URL.

### MCP Browser (Full Interaction)

Tools like [MCP Browser](https://browsermcp.io/) or Playwright allow the model to interact with websites, including filling forms and navigating JavaScript-heavy pages.

## The Complete Configuration

Here is a complete `mcp.json` file integrating all the services mentioned. Replace the API key placeholders, save the file, and restart your AI application.

```json
{
  "mcpServers": {
    "fetch": {
      "command": "uvx",
      "args": [
        "mcp-server-fetch"
      ]
    },
    "brave-search": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-brave-search"
      ],
      "env": {
        "BRAVE_API_KEY": "YOUR_BRAVE_API_KEY_HERE"
      }
    },
    "browsermcp": {
      "command": "npx",
      "args": [
        "@browsermcp/mcp@latest"
      ]
    },
    "tavily-remote": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.tavily.com/mcp/?tavilyApiKey=YOUR_TAVILY_API_KEY_HERE"
      ]
    }
  }
}
```

This configuration provides robust, private, and free web access for your local models.
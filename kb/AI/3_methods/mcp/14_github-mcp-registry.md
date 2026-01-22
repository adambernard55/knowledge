---
title: "GitHub MCP Registry"
id: "kb/AI/3_methods/mcp/14"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-01-22"
status: "Active"
doc_type: "Reference"
summary: "A technical guide on using the GitHub MCP Registry to discover, install, publish, and manage Model Context Protocol (MCP) servers for AI development."
tags:
  - "ai"
  - "mcp"
  - "github"
  - "agentic-ai"
  - "developer-tools"
  - "governance"
relations:
  - "kb/AI/3_methods/mcp/index.md"
aliases:
  - "MCP Registry"
  - "Model Context Protocol Registry"
semantic_summary: "This document describes the GitHub MCP Registry, a central hub for discovering, installing, publishing, and managing MCP servers. It covers the `mcp-publisher` CLI for publishing, automated workflows with GitHub Actions, and enterprise governance features like allow lists for secure tool usage in AI development."
synthetic_questions:
  - "What is the GitHub MCP Registry and what is its purpose?"
  - "How do you publish a new MCP server to the GitHub registry?"
  - "How can an enterprise control which MCP servers its developers use?"
  - "What is the process for installing an MCP server from the registry into VS Code?"
key_concepts:
  - "GitHub MCP Registry"
  - "Model Context Protocol (MCP)"
  - "MCP Server"
  - "mcp-publisher CLI"
  - "Enterprise Governance"
  - "Developer Tools"
  - "Agentic AI"
primary_keyword: "GitHub MCP Registry"
meta_description: "Technical reference for developers and administrators on finding, installing,publishing, and governing MCP servers using the GitHub MCP Registry and CLI."
---

# GitHub MCP Registry

## 1. Overview

The GitHub MCP Registry is a centralized, canonical source for discovering, installing, and managing Model Context Protocol (MCP) servers. MCP is a standard for connecting tools, APIs, and workflows to AI systems. The registry provides a structured and secure ecosystem for developers to find and use MCP servers, and for organizations to govern their usage.

## 2. Finding and Installing MCP Servers

### 2.1. Discovering Servers
The registry hosts a growing list of MCP servers, including official tools like Playwright and the GitHub MCP server, as well as partner servers from companies like Notion, Stripe, and Unity. Servers can be browsed and filtered by tags, popularity, or GitHub stars.

### 2.2. One-Click Installation
Installation is streamlined for VS Code and VS Code Insiders.

**Example: Installing the Playwright MCP Server**
1.  Navigate to the Playwright MCP server page in the GitHub MCP Registry.
2.  Click the **Install in VS Code** button.
3.  VS Code will launch with a pre-filled configuration.
4.  Accept or modify any optional parameters.
5.  The server is now installed and ready for use in agentic workflows. Remote servers like GitHub's use OAuth for authentication, eliminating manual token management.

## 3. Publishing an MCP Server

Developers can publish their own MCP servers to the registry using the `mcp-publisher` CLI.

### 3.1. Step 1: Install the CLI
```bash
# macOS/Linux/WSL (Homebrew)
brew install mcp-publisher

# macOS/Linux/WSL (Binary)
curl -L "https://github.com/modelcontextprotocol/registry/releases/download/latest/mcp-publisher_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/x86_64/amd64/;s/aarch64/arm64/').tar.gz" | tar xz mcp-publisher && sudo mv mcp-publisher /usr/local/bin/
```

### 3.2. Step 2: Initialize `server.json`

In your server's source directory, run:

```bash
mcp-publisher init
```

This creates a `server.json` manifest file. Configure the name, description, version, and package details.

### 3.3. Step 3: Prove Package Ownership

Add a metadata field to your package to link it to your MCP server name.

- **NPM (`package.json`):** `"mcpName": "io.github.username/server-name"`
- **PyPI/NuGet (`README`):** `mcp-name: io.github.username/server-name`
- **Docker (`Dockerfile`):** `LABEL io.modelcontextprotocol.server.name="io.github.username/server-name"`

### 3.4. Step 4: Authenticate

For GitHub namespaces (`io.github.*`), authenticate via OAuth:

```bash
mcp-publisher login github
```

For custom domains, follow the DNS verification instructions in the official documentation.

### 3.5. Step 5: Publish

```bash
mcp-publisher publish
```

After a successful publish, your server will be discoverable in the registry.

### 3.6. Automating Publishing with GitHub Actions

You can automate the publishing process on every tagged release. Create a workflow file at `.github/workflows/publish-mcp.yml`:

```yaml
name: Publish to MCP Registry
on:
  push:
    tags: ["v*"]

jobs:
  publish:
    runs-on: ubuntu-latest
    permissions:
      id-token: write  # Required for OIDC
      contents: read

    steps:
      - uses: actions/checkout@v5

      # Add steps to build and publish to your package manager (e.g., npm)
      - name: Publish to npm
        run: npm publish
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}

      # MCP publishing steps
      - name: Download MCP Publisher
        run: |
          curl -L "https://github.com/modelcontextprotocol/registry/releases/download/latest/mcp-publisher_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/x86_64/amd64/;s/aarch64/arm64/').tar.gz" | tar xz mcp-publisher
      - name: Publish to MCP Registry
        run: |
          ./mcp-publisher login github-oidc
          ./mcp-publisher publish
```

## 4. Enterprise Governance

For organizations requiring control over MCP usage, GitHub Enterprise supports registry allow lists.

### 4.1. How It Works

1. **Set Up an Internal Registry:** An administrator deploys an internal registry that conforms to the MCP API specification.
2. **Create an Allow List:** The internal registry is populated with a list of vetted internal and external MCP servers.
3. **Configure GitHub Enterprise:** The GitHub Enterprise instance is configured to point to the internal registry's endpoint.
4. **Enforce Policy:** MCP-aware tools like VS Code will automatically query the internal registry and only permit the installation of servers on the allow list.

This model enables organizations to enforce security and compliance policies while providing developers with a curated set of approved tools.

## 5. Advanced Usage and Future Roadmap

### 5.1. Power User Tips

- **Assess Quality:** Use GitHub stars and verified organization badges to quickly evaluate the legitimacy of a server.
- **Local Testing:** Use the **MCP Inspector** to test servers locally before publishing.
- **Semantic Tool Lookups:** VS Code is implementing semantic lookups to surface only the most relevant tools from large MCP servers based on the user's prompt, reducing context overload.

### 5.2. Future Developments

- **Self-Publication:** Soon, developers will be able to publish directly to the registry without manual approval, accelerating community growth.
- **Broader IDE Support:** MCP installation will be integrated into more IDEs.
- **Enhanced Enterprise Features:** More advanced governance and compliance workflows are planned for regulated industries.
- **Agentic Workflows:** The GitHub MCP server will bundle tools into use-case-driven flows (e.g., "analyze repo and create PR") for easier orchestration.
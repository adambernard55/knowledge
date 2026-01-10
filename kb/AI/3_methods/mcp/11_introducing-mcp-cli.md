---
title: "MCP CLI: Dynamic Tool Discovery for AI Agents"
id: "kb/AI/mcp/11"
version: "1.0"
steward: "Adam Bernard"
updated: 2026-01-10
status: "Active"
doc_type: "Reference"
summary: "A guide to using the MCP CLI, a command-line tool for dynamically discovering and interacting with MCP servers to reduce context window usage for AI agents."
tags:
  - "mcp"
  - "cli"
  - "tooling"
  - "agentic-ai"
  - "dynamic-discovery"
  - "context-window"
relations:
  - "kb/AI/mcp/09_open-source-mcp-projects-and-tools.md"
  - "kb/AI/mcp/08_using-mcp-servers-with-local-llms.md"
  - "kb/AI/mcp/02_mcp-connectors-and-integrations.md"
aliases:
  - "mcp-cli"
  - "Model Context Protocol CLI"
semantic_summary: "The MCP CLI is a lightweight command-line interface designed to solve the context window bloat problem in agentic AI systems. It enables dynamic, just-in-time discovery of MCP server tools, drastically reducing token consumption compared to static schema loading. This guide covers installation, configuration, and integration patterns for AI agents."
synthetic_questions:
  - "How to reduce token usage with MCP?"
  - "What is the MCP CLI?"
  - "How do I use the mcp-cli tool with an AI agent?"
  - "What is dynamic context discovery for MCP?"
key_concepts:
  - "dynamic context discovery"
  - "context window optimization"
  - "agentic tooling"
  - "command-line interface"
  - "MCP servers"
primary_keyword: "MCP CLI"
seo_title: "MCP CLI: A Guide to Dynamic AI Tool Discovery"
meta_description: "Learn how to use the MCP CLI to reduce token usage and improve AI agent efficiency with dynamic discovery of Model Context Protocol tools. Installation and examples included."
excerpt: "The MCP CLI is a lightweight tool that solves context window bloat by enabling dynamic discovery of MCP servers, reducing token consumption by up to 99%."
cover_image: ""
---

# Introducing MCP CLI: A Way to Call MCP Servers Efficiently

The Model Context Protocol (MCP) is an open standard for connecting AI agents to external tools, APIs, and data sources. However, as the ecosystem grows with more powerful MCP servers, developers and agent builders are hitting a scaling bottleneck: context window bloat.

**mcp-cli** is a lightweight CLI that allows dynamic discovery of MCP, reducing token consumption while making tool interactions more efficient for AI coding agents.

### Key Features:
- 🪶 Built on Bun, mcp-cli compiles to a single standalone binary.
- 🔌 Works with both stdio (local) and HTTP (remote) MCP servers.
- 🔍 Glob-based search across all servers `mcp-cli grep *mail* -d`.
- 🤖 Designed for AI coding agents (Gemini CLI, Claude Code, etc.).
- 💡 Structured error messages with recovery suggestions.

### The Context Problem
Every MCP server comes with tool definitions schemas describing what each tool does, its parameters, types, and descriptions. Traditional MCP integration loads all of these schemas upfront into the agent's context window.

Here's what that looks like in practice:

| Setup | Tokens Used |
| :--- | :--- |
| 6 MCP servers, 60 tools | ~47,000 tokens |
| After dynamic discovery | ~400 tokens |

That is a **99% reduction** in MCP-related token usage for this scenario.

When working with multiple MCP servers (GitHub, databases, browser automation—tool), definitions quickly consume a third or more of the effective context. This leads to:
- Reduced effective context length for actual reasoning and code generation.
- More frequent context compactions interrupting flow.
- Hard limits on the number of simultaneous MCP servers you can use.
- Higher API costs due to input token overhead.

### Dynamic Context Discovery
The solution is dynamic context discovery. Instead of loading everything upfront (static context), agents pull in only the information they need, when they need it.

`mcp-cli` implements this pattern for MCP:
1.  **Step 1: "What servers exist?"** → `mcp-cli`
2.  **Step 2: "What are the params for tool X?"** → `mcp-cli github/search`
3.  **Step 3: Execute** → `mcp-cli github/search '{"path": "README.md"}'`

Most Interactions only use a handful of tools, yet static loading consumes tokens for every tool definition. Dynamic discovery inverts this, you pay only for what you use.

### Quick start
`mcp-cli` allows dynamic discovery of MCP while making tool interactions more efficient for AI coding agents.

**1. Installation**
```bash
# binary install
curl -fsSL https://raw.githubusercontent.com/philschmid/mcp-cli/main/install.sh | bash 
# requires bun install
bun install -g https://github.com/philschmid/mcp-cli

**2. Create a config file**  
Create `mcp_servers.json` in your current directory or `~/.config/mcp/`:
```

```json
{  
  "mcpServers": {    
    "filesystem": {      
      "command": "npx",      
      "args": [        
        "-y",        
        "@modelcontextprotocol/server-filesystem",        
        "."      
      ]    
    },    
    "deepwiki": {      
      "url": "https://mcp.deepwiki.com/mcp"    
    }  
  }
}
```

**3. Discover available tools**

```bash
# List all servers and tools
mcp-cli
# deepwiki
#  • read_wiki_structure
#  • read_wiki_contents
#  • ask_question
## filesystem
#  • read_file
#  • read_text_file
#  • read_media_file
#  • read_multiple_files
# ... 

# With descriptions
# mcp-cli -d
```

**4. Call a tool**

```bash
# View tool schema first
mcp-cli filesystem/read_file
# Tool: read_file
# Server: filesystem
## Description:
#  Read the complete contents of a file as text. DEPRECATED: Use read_text_file instead.
## Input Schema:
# {
#  "type": "object",
#  "properties": {
# ...
```

**5. Execute the tool**

```bash
# Call the tool
mcp-cli filesystem/read_file '{"path": "./README.md"}'
```

**6. Complex commands**  
MCP CLI allows the model to generate commands that chain multiple tool calls together.

```bash
# Using a heredoc (recommended for complex JSON)
mcp-cli server/tool <<EOF
{"content": "Text with 'single quotes' and \"double quotes\""}
EOF 

# Using a variable
JSON='{"message": "Hello, it'\''s a test"}'
echo "$JSON" | mcp-cli server/tool 

# From a file
cat args.json | mcp-cli server/tool 

# Using jq to build complex JSON
jq -n '{query: "mcp", filters: ["active", "starred"]}' | mcp-cli github/search 

# Find all TypeScript files and read the first one
mcp-cli filesystem/search_files '{"path": "src/", "pattern": "*.ts"}' --json | jq -r '.content[0].text' | head -1 | xargs -I {} sh -c 'mcp-cli filesystem/read_file "{\"path\": \"{}\"}"'
```

### Integrating with AI Agents

`mcp-cli` is designed to be used with AI Agents and bash tools. There are two main ways to integrate it:

#### Option 1: System Instructions Integration

Add this to your AI agent's system prompt for direct CLI access:

````
## MCP Servers 
You have access to MCP (Model Context Protocol) servers via the `mcp-cli` cli.
MCP provides tools for interacting with external systems like GitHub, databases, and APIs. 

Available Commands: 
```bash
mcp-cli                              # List all servers and tool names
mcp-cli <server>                     # Show server tools and parameters
mcp-cli <server>/<tool>              # Get tool JSON schema and descriptions
mcp-cli <server>/<tool> '<json>'     # Call tool with JSON arguments
mcp-cli grep "<pattern>"             # Search tools by name (glob pattern)
````

**Add `-d` to include tool descriptions** (e.g., `mcp-cli <server> -d`)

Workflow:

1. **Discover**: Run `mcp-cli` to see available servers and tools or `mcp-cli grep "<pattern>"` to search for tools by name (glob pattern)
2. **Inspect**: Run `mcp-cli <server> -d` or `mcp-cli <server>/<tool>` to get the full JSON input schema if required context is missing. If there are more than 5 mcp servers defined don't use -d as it will print all tool descriptions and might exceed the context window.
3. **Execute**: Run `mcp-cli <server>/<tool> '<json>'` with correct arguments

### Examples

```bash
# With inline JSON
$ mcp-cli github/search_repositories '{"query": "mcp server", "per_page": 5}' 

# From stdin (pipe)
$ echo '{"query": "mcp"}' | mcp-cli github/search_repositories 

# Using a heredoc (recommended for complex JSON)
mcp-cli server/tool <<EOF
{"content": "Text with 'single quotes' and \"double quotes\""}
EOF 

# Find all TypeScript files and read the first one
mcp-cli filesystem/search_files '{"path": "src/", "pattern": "*.ts"}' --json | jq -r '.content[0].text' | head -1 | xargs -I {} sh -c 'mcp-cli filesystem/read_file "{\"path\": \"{}\"}"'
```

### Rules

1. **Always check schema first**: Run `mcp-cli <server> -d or` mcp-cli /` before calling any tool
2. **Quote JSON arguments**: Wrap JSON in single quotes to prevent shell interpretation

#### Option 2: Agent Skills
For AI agents that support Agent Skills an upcoming standard for extending coding agents. `mcp-cli` ships with a ready-to-use skill definition.

Create `mcp-cli/SKILL.md` in your agent's skills directory:
```markdown
---
name: mcp-cli
description: Interface for MCP (Model Context Protocol) servers via CLI. Use when you need to interact with external tools, APIs, or data sources through MCP servers.
--- 
# MCP-CLI 
Access MCP servers through the command line. MCP enables interaction with external systems like GitHub, filesystems, databases, and APIs. 

## Commands 
| Command | Output |
|---------|--------|
| `mcp-cli` | List all servers and tool names |
| `mcp-cli <server>` | Show tools with parameters |
| `mcp-cli <server>/<tool>` | Get tool JSON schema |
| `mcp-cli <server>/<tool> '<json>'` | Call tool with arguments |
| `mcp-cli grep "<glob>"` | Search tools by name | 

**Add `-d` to include descriptions** (e.g., `mcp-cli filesystem -d`) 

## Workflow 
1. **Discover**: `mcp-cli` → see available servers and tools
2. **Explore**: `mcp-cli <server>` → see tools with parameters
3. **Inspect**: `mcp-cli <server>/<tool>` → get full JSON input schema
4. **Execute**: `mcp-cli <server>/<tool> '<json>'` → run with arguments 

## Examples 
```bash
# List all servers and tool names
mcp-cli 

# See all tools with parameters
mcp-cli filesystem 

# With descriptions (more verbose)
mcp-cli filesystem -d 

# Get JSON schema for specific tool
mcp-cli filesystem/read_file 

# Call the tool
mcp-cli filesystem/read_file '{"path": "./README.md"}' 

# Search for tools
mcp-cli grep "*file*" 

# JSON output for parsing
mcp-cli filesystem/read_file '{"path": "./README.md"}' --json 

# Complex JSON with quotes (use heredoc or stdin)
mcp-cli server/tool <<EOF
{"content": "Text with 'quotes' inside"}
EOF 

# Or pipe from a file/command
cat args.json | mcp-cli server/tool 

# Find all TypeScript files and read the first one
mcp-cli filesystem/search_files '{"path": "src/", "pattern": "*.ts"}' --json | jq -r '.content[0].text' | head -1 | xargs -I {} sh -c 'mcp-cli filesystem/read_file "{\"path\": \"{}\"}"'
````

## Options

|Flag|Purpose|
|---|---|
|`-j, --json`|JSON output for scripting|
|`-r, --raw`|Raw text content|
|`-d`|Include descriptions|

## Exit Codes

- `0`: Success
- `1`: Client error (bad args, missing config)
- `2`: Server error (tool failed)
- `3`: Network error


### Conclusion
The AI Agent space is moving incredibly fast. `mcp-cli` tries to solve context tool discovery problem turning it into an iterative, just-in-time process. It allows agents to access a massive ecosystem of shared capabilities without the context bloat of static integration. Whether used within a Skill or as a standalone utility, it ensures your agent spends its tokens on reasoning, not configuration.

The project is open source and designed to fit into existing workflows. Give it a try and contribute at github.com/philschmid/mcp-cli.

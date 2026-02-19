---
title: "Claude Cowork: Desktop Agent Architecture"
id: "kb/AI/claude/05_claude-cowork-desktop-agent"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-02-12"
status: "Active"
doc_type: "Reference"
summary: "Technical overview of Claude Cowork, Anthropic's desktop AI agent for Windows and macOS, featuring file system access, MCP integration, and enterprise security sandboxing."
tags:
  - "claude"
  - "agentic-ai"
  - "desktop-automation"
  - "windows"
  - "microsoft"
relations:
  - "kb/AI/1_models/1_specific-models/claude/02_integrating-claude-code-with-obsidian"
  - "kb/AI/3_methods/mcp/05_mcp-reference-and-use-cases"
aliases:
  - "Claude Cowork"
  - "Claude Desktop App"

# --- AI & RAG Enhancement ---
semantic_summary: "Claude Cowork is a desktop-based AI agent available on Windows and macOS. It features full file system access, multi-step task execution, and Model Context Protocol (MCP) support. It runs in a sandboxed virtual machine environment and is currently integrated into Microsoft's internal engineering workflows."
synthetic_questions:
  - "What is Claude Cowork and how does it differ from Claude Code?"
  - "Is Claude Cowork available on Windows?"
  - "How does Claude Cowork handle security and file access?"
  - "What is the pricing for Claude Cowork?"
key_concepts:
  - "Desktop Agent"
  - "VM Sandboxing"
  - "MCP Connectors"
  - "Microsoft Partnership"

# --- SEO & Publication ---
primary_keyword: "Claude Cowork Windows"
seo_title: "Claude Cowork Desktop Agent: Features, Security & Pricing"
meta_description: "A technical guide to Claude Cowork for Windows and macOS. Explore its agentic capabilities, MCP integrations, and security architecture."
excerpt: "Claude Cowork brings agentic AI to the desktop with full file access and MCP integration. Learn how it automates workflows while maintaining security via VM sandboxing."
cover_image: ""
---

# Claude Cowork: Desktop Agent Architecture

**Claude Cowork** is Anthropic's dedicated desktop agent software, designed to automate knowledge work by interacting directly with a user's local file system and applications. Following its initial macOS debut, the software is now available on Windows, bringing agentic capabilities to the majority of the enterprise desktop market [1]

## 1. Core Capabilities

Unlike the standard web-based chat interface, Cowork is an **agentic tool** capable of planning and executing multi-step workflows.

### 1.1 Feature Parity (Windows & macOS)
The Windows release maintains full feature parity with the macOS version, including:
*   **Local File Access:** The ability to read, write, and manage files directly on the host machine [1]
*   **Multi-Step Execution:** Planning complex tasks that require a sequence of actions (e.g., "Analyze these spreadsheets and draft a summary report").
*   **Global Instructions:** Users can set global and folder-specific context rules that persist across sessions [1]

### 1.2 Connectivity & Plugins
Cowork serves as a host for the **Model Context Protocol (MCP)**, allowing it to connect to external data sources and tools.
*   **MCP Connectors:** Integrates with external services (GitHub, Google Drive, Slack) to fetch context.
*   **Agentic Plugins:** Supports open-source plugins for sales, legal, finance, and data analysis workflows [1]

## 2. Strategic Context: The Microsoft Partnership

Despite Microsoft's major investment in OpenAI, the company has aggressively adopted Claude Cowork internally.
*   **Internal Adoption:** Microsoft's CoreAI team and Business Copilot teams are utilizing Claude Code and Cowork for engineering tasks [1]
*   **Azure Integration:** Microsoft has integrated **Claude Opus 4.6** into Microsoft Foundry, positioning it as a premium option for complex, long-context enterprise tasks [1]
*   **Incentive Structure:** Microsoft has reportedly begun counting Anthropic model sales toward Azure sales quotas, a privilege usually reserved for first-party or OpenAI products [1]

## 3. Security Architecture

Granting an AI agent access to local files introduces significant risk. Anthropic mitigates this through a strict sandboxing architecture.

*   **VM Sandboxing:** The agent operates within a virtual machine under the hood. It cannot "see" or access any folder that has not been explicitly allow-listed by the user [1]
*   **Folder Restrictions:** On Windows, the agent is restricted to the user's personal folder by default, preventing access to sensitive system directories or root-level repositories (e.g., `C:\git`) without explicit configuration [1]
*   **Prompt Injection Defense:** The system includes safeguards against "prompt injection" attacks, where hidden text in a document could theoretically hijack the agent's instructions [1]

## 4. Pricing & Availability

Cowork is positioned as a premium productivity tool.

*   **Licensing:** Available to all paid subscribers (Pro, Team, Enterprise).
*   **Cost:** Starts at **$20/month** (Pro tier) [1]
*   **Status:** Currently in "Research Preview" [1]

## 5. Market Impact

The release of Cowork has signaled a shift in the software market, threatening SaaS tools that rely on simple task automation. The ability of a desktop agent to orchestrate workflows across different applications challenges the value proposition of standalone project management and data analysis tools [1]

<br/>
<details class="copilot-sources"><summary class="copilot-sources__summary">Sources</summary>
<ul class="copilot-sources__list">
<li class="copilot-sources__item"><span class="copilot-sources__index">[1]</span><span class="copilot-sources__text"><a href="obsidian://open?file=kb%2FAI%2F1_models%2F1_specific-models%2Fclaude%2FAnthropic%E2%80%99s%20Claude%20Cowork%20finally%20lands%20on%20Windows.md">Anthropic’s Claude Cowork finally lands on Windows</a></span></li>
</ul>
</details>


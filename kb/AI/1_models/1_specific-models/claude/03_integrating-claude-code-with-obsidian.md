---
title: "Integrating Claude Code with Obsidian"
id: "kb/AI/claude/02_integrating-claude-code-with-obsidian"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-02-12"
status: "Active"
doc_type: "Reference"
summary: "Guide on integrating Anthropic's Claude Code CLI into Obsidian using the Terminal plugin and Agent Skills for autonomous vault management."
tags:
  - "claude"
  - "obsidian"
  - "agentic-workflow"
  - "cli"
relations:
  - "REF/Obsidian/made Obsidian smarter with 3 simple plugins"
  - "kb/AI/3_methods/mcp/16_practical-local-mcp-use-cases"
aliases:
  - "Claude Code in Obsidian"
  - "Obsidian Agent Skills"

# --- AI & RAG Enhancement ---
semantic_summary: "This document details the setup of Claude Code (CLI) within Obsidian using a Terminal plugin. It covers the installation of 'Agent Skills' (JSON Canvas, Markdown specs) into a .claude folder and the initialization of CLAUDE.md for context-aware vault management."
synthetic_questions:
  - "How do I run Claude Code inside Obsidian?"
  - "What are Obsidian Agent Skills for Claude?"
  - "How can I give Claude Code access to my Obsidian vault context?"
key_concepts:
  - "Claude Code CLI"
  - "Obsidian Terminal Plugin"
  - "Agent Skills"
  - "CLAUDE.md Context"
---

# Integrating Claude Code with Obsidian

This guide outlines how to embed **Claude Code** (Anthropic's agentic CLI tool) directly into Obsidian to act as an intelligent vault manager and research assistant.

## 1. The Concept
By running Claude Code inside an integrated terminal within Obsidian, you create an agent that can:
1.  **See your context:** It operates within the vault's root directory.
2.  **Manage files:** It can create folders, refactor notes, and generate content using Obsidian-specific formats.
3.  **Maintain memory:** It uses a `CLAUDE.md` file to store project-specific context and conventions.

## 2. Prerequisites
*   **Claude Code:** The CLI tool must be installed on your system (requires Anthropic API access).
*   **Obsidian Terminal Plugin:** A community plugin (e.g., "Terminal") to run shell commands inside the Obsidian interface.

## 3. Setup Process

### Step 1: Install Agent Skills
To ensure Claude understands Obsidian's specific formats (Markdown, Canvas, Frontmatter), you need to provide it with "Agent Skills".

1.  Create a hidden folder named `.claude` in the root of your Obsidian Vault.
2.  Download the **Obsidian Agent Skills** (often available from the `obsidian-skills` GitHub repo or similar sources).
3.  Place the skill definitions (usually JSON or Markdown specs defining file types) into the `.claude` folder.

### Step 2: Initialize Context
1.  Open the Terminal inside Obsidian.
2.  Navigate to your vault root.
3.  Run the initialization command:
    ```bash
    claude init
    ```
4.  This creates a `CLAUDE.md` file in your root. This file acts as the "System Prompt" or long-term memory for the agent in this specific vault. You can edit this file to define rules (e.g., "Always use H1 for titles," "Link to existing nodes where possible").

## 4. Workflow Examples

### The "Visual" Terminal
Instead of alt-tabbing to a separate terminal window, the embedded terminal allows you to see your file explorer and the agent's output simultaneously.

**Example Prompt:**
> "Create a minimal folder structure for a software developer who takes daily notes. Use the PARA method."

Because Claude Code has file system access, it will physically create the folders (`01_Projects`, `02_Areas`, etc.) rather than just listing them in text.

### Research & Synthesis
If you use the **Obsidian Web Clipper** to save articles:
1.  Clip an article to your `Inbox`.
2.  Ask Claude in the terminal: "Read the last 3 files in Inbox and summarize the connection to my 'Home Lab' project."
3.  Claude reads the actual files and generates a summary note.

## 5. Why This Works
Standard LLM chat interfaces (like the web app) lack **context**. They don't know your folder structure or existing notes unless you manually upload them.

Claude Code, running locally in the vault:
1.  **Has direct I/O access:** It can read every file.
2.  **Follows constraints:** The `CLAUDE.md` and Agent Skills ensure it generates valid Obsidian syntax (e.g., `[[WikiLinks]]` instead of `[Markdown](links)`).
---
title: "Reference Architecture for Building Trustworthy Agentic AI Systems"
id: "kb/AI/2_agents/07_reference-architecture-for-trustworthy-agentic-ai"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-01-15"
status: "Active"
doc_type: "Reference"
summary: "Provides a reference architecture for building and using trustworthy agentic AI systems, focusing on CLI agents, planning styles (ReAct vs. plan-and-execute), and safety guardrails."
tags:
  - agentic-ai
  - reference-architecture
  - cli-agents
  - llm
  - mcp
  - safety
  - governance
relations:
  - "kb/AI/2_agents/00_introduction-to-ai-agents"
  - "kb/AI/3_methods/10_agentic-architectures-and-frameworks"
  - "kb/AI/3_methods/mcp/index"
aliases:
  - "Trustworthy Agentic AI"
  - "CLI Agent Architecture"
security_level: "Internal"
semantic_summary: "This document details a reference architecture for trustworthy agentic AI systems, specifically focusing on command-line interface (CLI) agents. It contrasts planning styles like ReAct and plan-and-execute, explains the role of the Model Context Protocol (MCP) for tooling, and outlines essential safety guardrails like sandboxing and human-in-the-loop approvals for reliable operation."
synthetic_questions:
  - "What is the architecture of an agentic CLI tool?"
  - "What is the difference between ReAct and plan-and-execute planning styles for AI agents?"
  - "How does the Model Context Protocol (MCP) work with agentic tools?"
  - "What are the key safety guardrails for building trustworthy AI agents?"
key_concepts:
  - "Agentic AI"
  - "CLI Agents"
  - "ReAct"
  - "Plan-and-Execute"
  - "Model Context Protocol (MCP)"
  - "Human-in-the-Loop"
  - "Sandboxing"
  - "Context Engine"
primary_keyword: "agentic ai architecture"
seo_title: "A Reference Architecture for Building Trustworthy Agentic AI Systems"
meta_description: "Explore a complete reference architecture for building trustworthy agentic AI systems, focusing on CLI agents, planning styles, and safety guardrails."
excerpt: "This guide provides a detailed reference architecture for trustworthy agentic AI, covering CLI agents, planning styles like ReAct, and the Model Context Protocol (MCP)."
cover_image: ""
---

# Reference Architecture for Building Trustworthy Agentic AI Systems

## Agentic Terminal - How Your Terminal Comes Alive with CLI Agents

### Key Takeaways
- The terminal is becoming agentic: Instead of only imperative commands, developers can state goals while the agent plans, calls tools, iterates, and asks for approval.
- Regardless of the vendor, most tools follow a similar architectural pattern: intent capture, context assembly (via a context engine), planning, tool execution with guardrails, and finally, rendering or pull requests. This common structure can be fine-tuned to suit specific needs.
- Planning styles differ –  reason and act (Gemini) for exploratory agility, plan-and-execute (Claude) for predictable multi-step work, and JSON runners (Auto-GPT) for scripted, machine-readable pipelines – and teams should choose by task, not brand.
- Success depends on contracts and scoping as much as the LLM: versioned context files (GEMINI.md/CLAUDE.md), explicit path scopes, and sandboxing.
- Agentic workflows will increasingly integrate with IDEs/OSes to be more fundamental for all users and be extendable through plugin ecosystems.

## Why the Command Line Is Becoming Agentic
Traditionally, the terminal or shell has been an imperative tool, relying on predefined commands like ls, grep, and git to execute specific instructions.

However, recent advancements in agentic command-line tools, such as Gemini CLI, Claude Code and AutoGPT have transformed this simple utility into a more dynamic and intelligent assistant.

These agentic CLI tools allow users to describe higher-level goals or tasks in natural language, bringing the humble shell to life.

They can plan steps, utilize various tools for different tasks (such as file handling, code execution, and web search), reason over outputs, and act as a co-pilot to help complete the tasks.

This significantly reduces mental thrashing for the user and minimizes context switching between multiple tools. Crucially, users maintain control by approving or guiding the agent's processes, ensuring a balance between automation and user oversight.

In this article, we will explore the architecture of these agentic tools, contrasting different planning styles like ReAct and plan-and-execute.

We will also examine the practical lifecycle of an agentic workflow, from intent capture to execution, and discuss the critical safety guardrails required for reliable daily use.

## End-to-End Agentic Terminal Lifecycle: One Prompt, Three Agents
While the rise of AI in development is often associated with Chat interfaces (like ChatGPT) and Agentic IDEs (like Cursor), the Agentic CLI occupies a distinct niche. IDE-based agents excel at code-centric tasks with rich visual context, but they are often confined to the editor’s window.

The CLI meets developers where they manage infrastructure and git workflows: the shell. This headless, composable nature allows it to chain tools and system commands in ways a GUI-bound agent cannot. However, note that this distinction is blurring as agents like Gemini CLI can now integrate with IDEs like VSCode to provide diff views for their suggestions.

To elaborate on the power of agentic terminal tools, let’s discuss a running example.

Consider a common scenario where a developer needs to bootstrap a new repository with standard documentation and automation scripts. Instead of manually creating each file and writing boilerplate code, an agentic CLI can handle the entire process from a single high-level instruction, ensuring consistency and saving valuable time.

**Input Prompt:**

> Add a CONTRIBUTING.md, a PULL_REQUEST_TEMPLATE.md, and a scripts/smoke-check.sh that runs a configurable command and exits non-zero on failure; update the README to document both, and open a PR.

To understand how this instruction transforms into action, we will dissect the agent’s workflow into its component stages. We begin with Intent Capture, where the agent grounds itself in the project's specific context, before moving to Planning Styles to contrast how different models architecture their reasoning. Subsequent sections will detail the Tool Execution loops that perform the actual work and the critical Safety Guardrails that prevent autonomous accidents. Finally, we will look at how the results are rendered back to the user, illustrating that beneath the varying brand names, most agentic tools share a common architectural DNA.

### Stage 1: Intent Capture and Context Formation
To ensure a high-quality prompt for the LLM, the agent first gathers all necessary information before planning or execution. This approach involves several steps: linking the task to the current working directory, managing session state, and saving per-project configurations in dotfolders (e.g., `/.gemini` and `/.claude`). This approach eliminates the need to repeatedly use flags for recurring tasks.

Additionally, instructions are sourced implicitly from various locations. Here are some of the primary signals the CLI agent sources from apart from the user’s prompt:

**Folder-specific Context Files**

These are markdown files that encapsulate facts about how your repo is built and tested, plus your conventions for docs and scripts. They essentially act as onboarding docs for your agent. As an example, the file for Gemini CLI is called `Gemini.md`. Claude Code tool also uses a similar convention.

```markdown
# GEMINI.md (excerpt)
## 1. Project Philosophy
This is a High-Performance SaaS Backend.
* **Core Principle:** Readability over cleverness. Explicit is better than implicit.
* **Architecture:** Hexagonal Architecture (Ports & Adapters).
* **Safety:** Zero-trust security model. All inputs must be validated via Pydantic.
## 2. Tech Stack & Standards
* **Language:** Python 3.11+ (Strict Typing required).
* **Framework:** FastAPI (Async default).
* **Database:** PostgreSQL (via SQLAlchemy 2.0 async session).
* **Testing:** Pytest (Coverage must remain >90%).
```

  **Skills**

A major limitation of early agents was the need to stuff all instructions into the context window. Anthropic’s Claude Code introduced the concept of Skills that builds on the above idea of markdown files, modular packages of expertise (e.g., PDF manipulation, Data Analysis, and React Best Practices) that exist as folders containing a `SKILL.md`.

This inclusion enables Progressive Disclosure: The agent initially sees only the names/descriptions of available skills (consuming minimal tokens). It then dynamically installs or reads the full `SKILL.md` instruction set only if the user's task requires it. This approach allows agents to be generalists by default but specialists on demand.

**Codebase Signals**

The CLI may scan for existing `scripts/`, `.github/`, and pick up file artifacts like `README.md` if you have already provided these files. Based on typical conventions for languages like Python, it could also look at artifacts like `pyproject.toml` files for a high-level overview.

**IDE Focus**

This is an optional step that can be used to open files and selections if you are connected to a code editor like VSCode or Cursor.

### Stage 2: Planning Styles

With context loaded, each tool starts its control loop:

- **Gemini (ReAct style)** thinks, calls a tool, observes, and repeats, which is great for discovering missing folders or policies. This iterative approach allows Gemini to adapt to new information and adjust its strategy dynamically, making it effective for tasks that require flexible problem-solving and exploration.
- **Claude (plan-and-execute)** proposes a checklist you can approve, then executes the plans step-by-step with policy hooks. This method offers a higher degree of control and transparency, because users can review and modify the plan before execution, ensuring adherence to specific policies or preferences.
- **Auto-GPT** emits thoughts plus a command in JSON that a runner executes every cycle. This structured output facilitates automation and integration with other systems, because the JSON format provides a clear and machine-readable representation of the agent's intentions and actions.

The following examples illustrate how different agents approach this planning phase. Claude presents a human-readable checklist for user approval, while Auto-GPT generates structured JSON output designed for automated execution.

**Claude – Plan Preview**

```
Plan:
1. Create scripts/smoke-check.sh (POSIX sh; reads CMD from env; exits non-zero on failure)
2. Create CONTRIBUTING.md (how to run smoke check locally)
3. Create .github/PULL_REQUEST_TEMPLATE.md (checklist includes smoke check)
4. Update README.md with scripts/ and PR template instructions
5. Run smoke-check; commit; open PR
Approve? [y/n]
```

**Auto-GPT – Explicit JSON With Thoughts and Commands**

```json
{
  "thoughts": {"text": "Create smoke-check, docs, template; update README; run script; commit/PR"},
  "command": {"name": "write_file", "args": {"path": "scripts/smoke-check.sh", "content": "#!/bin/sh\n: \"${CMD:=echo ok}\" \n$CMD || { echo \"smoke failed\" >&2; exit 1; }\necho \"ok\""}}
}
```

### Stage 3: Tool Calls

At this stage, the agent uses the tools in its arsenal to suggest changes based on its tasks. For example, this can involve showing a diff within the IDE using a file-edit tool.

Tooling has evolved from proprietary implementations to an open standard: the **Model Context Protocol (MCP)**. Supported by Anthropic, Google, and other organizations, MCP acts like a USB-C port for AI applications. Instead of hardcoding integrations for every database or API, developers run local MCP Servers (e.g., for PostgreSQL, Slack, or GitHub). The CLI agent automatically discovers these resources upon startup, allowing a single agent to query your production database, read your linear tickets, and edit code all in one seamless workflow.

**Example Diff for Smoke Script**

```diff
*** scripts/smoke-check.sh
+#!/bin/sh
+set -eu
+# CMD can be overridden: CMD="make test" ./scripts/smoke-check.sh
+: "${CMD:=printf ok}"
+$CMD >/dev/null 2>&1 || { echo "smoke failed" >&2; exit 1; }
+echo "ok"
```

Claude’s hooks are a clean way to make policy explicit – restrict write paths, auto-chmod scripts, run lint/tests after writes – without stuffing it into prompts. Gemini gets similar leverage via extensions and MCP: different knobs, similar outcomes.

### Stage 4: Human-in-the-Loop Safety and Guardrails

You retain control over risky actions. Gemini requires your approval before executing writes or shell commands that have side effects. Claude offers confirmations and hooks, allowing you to block policy-violating writes or automatically run checks before proceeding. Auto-GPT pauses for a yes/no confirmation unless continuous mode is enabled. For exploration, activate a containerized sandbox to isolate the file system and processes.

### Stage 5: Execution and Iteration: The Loop That Actually Gets Work Done

Once files are created, the agent executes the script and adjusts based on the outcome. For instance, if the `scripts` directory is missing, Gemini will create it and attempt the operation again. Should the script lack executable permissions, Claude's integrated hook automatically applies the `chmod +x` command.

The script executes in a continuous loop of observation, reasoning, and action. This cycle repeats until local execution is successful and the documentation is complete.

### Stage 6: Rendering Results and Stopping Conditions

The CLI presents a clear, syntax-highlighted view of tool calls and file differences. Users can open these diffs in their editor to make adjustments manually or instructing the agent to make appropriate changes. Approvals are most efficient when batched, such as by reviewing all scripts and documentation together before a single approval.

Upon a successful smoke check, with approved diffs, the agent will create a new branch, commit the changes, and open a draft PR.

## How to Leverage Agentic CLIs in Your Workflows

Here are some practical tips to make the most of these tools in your workflow:

**Treat context files like build assets**  
Maintain `GEMINI.md` and `CLAUDE.md` files alongside your `README` file. These files should be concise and focused on specific details, including build and test procedures, configuration locations, any repository-specific gotchas, and directories safe for editing. You can even use the agents to generate initial drafts. Consider these files as a way to program the environment for the agent, rather than as another prompt requiring constant oversight.

**Scope aggressively**  
Point the agent at the folder that actually matters (for example `services/payments/`, not the whole monorepo) and pass explicit `@file` hints for hot spots. Tighter scope implies tighter diffs, fewer creative hallucinations, and faster iterations. If the task truly spans multiple packages, enumerate them in your prompt to prevent the agent from doing exhaustive scans.

**Use sandboxes to avoid accidental changes to environments**

- **Gemini CLI** offers a sandbox mode for ephemeral, containerized execution of shell/file tools.
- **Claude Code** typically runs within containerized dev environments (Dev Container/Docker) or uses plugins/hooks to route shell/file actions through a containerized runner.
- **Auto-GPT** does not have a dedicated sandbox mode flag, but it is strongly recommended to run it within a Docker container.

**Use the tool that matches your needs**

- **Gemini CLI:** Ideal for users in the Google ecosystem for discovery-heavy, generalist tasks.
- **Claude Code:** Best for tasks requiring concrete plans, robust coding, and policy enforcement.
- **GitHub Copilot CLI:** Designed for rapid, repository-aware natural language-to-shell assistance.
- **Other Tools (Aider, Open Interpreter):** For users needing local LLMs, tight Git ergonomics, or an unrestricted shell.

**Prompt like an engineer, don’t write essays**  
Good prompting is mostly about crisp contracts. Use a four-part prompt: high-level goal, constraints, needed artifacts, and success checks.

**Instrument Like Any Other Automation**  
Monitor metrics like PR cycle time, size of agent-generated diffs, and rework percentage to optimize agent performance and your operational contracts.

## What’s Next

Agentic CLIs are evolving from simple shell helpers into the connective tissue that unifies your work tools, operating system, and cloud infrastructure. Key trends include:

- **Unified Agent Surfaces:** Merging IDEs and operating systems (e.g., Windsurf, Cursor).
- **Persistent Background Services:** Proactive daemon agents that monitor and fix errors.
- **Extension Ecosystems:** "App Stores" for agent capabilities, blurring the line between generalist and specialist agents.

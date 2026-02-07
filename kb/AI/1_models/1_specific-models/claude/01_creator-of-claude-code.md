---
title: "The Workflow of Claude Code's Creator: A Deep Dive"
id: "KB/AI/M-CL-01"
version: "1.1"
steward: "Adam Bernard"
updated: "2026-02-07"
status: "Active"
doc_type: "Reference"
summary: "An analysis of the high-efficiency, multi-agent workflow used by Boris Cherny, the creator and head of Claude Code at Anthropic, which treats development as an orchestration task."
tags:
  - "claude"
  - "anthropic"
  - "agentic-workflow"
  - "developer-tools"
  - "fleet-commander-model"
  - "claude-code"
relations:
  - "kb/AI/1_models/1_specific-models/3_claude.md"
  - "kb/AI/1_models/1_specific-models/claude/02_oh-my-claude-code.md"
aliases:
  - "Boris Cherny Workflow"
  - "Claude Code Workflow"
  - "Fleet Commander Development"

# --- AI & RAG Enhancement ---
semantic_summary: >
  This document analyzes the viral workflow of Boris Cherny, creator of Claude Code. It details his 'fleet commander' approach, where he runs multiple Claude agents in parallel to manage different development streams simultaneously. Key principles include using the smartest model (Opus) to minimize human correction, maintaining a shared `CLAUDE.md` file for continuous agent learning, and using verification loops to ensure AI-generated code is functional. This methodology shifts the developer's role from a coder to an orchestrator of an autonomous workforce.
synthetic_questions:
  - "What is the workflow of Boris Cherny, the creator of Claude Code?"
  - "How does the 'fleet commander' model work in software development?"
  - "Why is using a slower, smarter AI model often faster in the long run?"
  - "How can an AI agent be trained on a team's specific coding standards?"
key_concepts:
  - "Fleet Commander Model"
  - "Agent Orchestration"
  - "Human Correction Tax"
  - "Verification Loops"
  - "Continuous Agent Learning"
  - "Claude Code"

# --- SEO & Publication ---
primary_keyword: "claude code workflow"
seo_title: "Claude Code Creator's Workflow: A Deep Dive into Agentic Development"
meta_description: "An inside look at the viral workflow of Claude Code's creator, Boris Cherny. Learn how he uses a 'fleet commander' model to multiply his productivity."
excerpt: "Discover the game-changing workflow of Claude Code's creator. It's not about coding faster; it's about orchestrating a fleet of AI agents to do the work for you."
cover_image: ""
---
# The Workflow of Claude Code's Creator: A Deep Dive

An analysis of a viral thread from Boris Cherny, the creator and head of Claude Code at Anthropic, reveals a workflow that is reshaping how modern software gets built. His methodology allows a single human to operate with the output capacity of a small engineering department by shifting the developer's role from a hands-on coder to a "fleet commander" of autonomous AI agents.

This document breaks down the core principles of this highly efficient, multi-agent workflow.

## 1. The Fleet Commander Model: Parallel Agent Orchestration

The most significant departure from traditional development is the rejection of a linear workflow. Instead of writing and testing code sequentially, Cherny runs multiple Claude instances in parallel, each handling a distinct task.

-   **Parallel Work Streams:** He uses up to five Claude agents simultaneously in his terminal, managing them with system notifications to know when an agent requires input.
-   **Role of the Human:** The developer acts as a commander, assigning missions (e.g., run a test suite, refactor a module, draft documentation) and managing the parallel execution. This transforms coding from a typing task into a real-time strategy exercise.

This approach validates the strategy of achieving exponential productivity gains through superior orchestration of existing models, rather than simply waiting for faster or more powerful ones.

## 2. The Smartest Model Imperative: Reducing the Correction Tax

Counterintuitively, Cherny exclusively uses Anthropic's heaviest and slowest model, Opus. He argues that while faster models like Sonnet or Haiku have lower latency per generation, they require more human guidance and correction.

The key insight is that the true bottleneck in AI-assisted development is not token generation speed but the **human time spent correcting the AI's mistakes**. By using the most intelligent model upfront, the "compute tax" is higher, but the "human correction tax" is significantly lower, leading to a faster net completion time for complex tasks.

## 3. The Living Rulebook: `CLAUDE.md` for Continuous Learning

To solve the problem of AI "amnesia" between sessions, Cherny's team maintains a single file named `CLAUDE.md` in their git repository. This file serves as a persistent, evolving set of instructions for the AI agent.

Whenever a developer observes the AI making a mistake or deviating from a team-specific coding standard, they add a corrective rule to `CLAUDE.md`. This practice ensures that every human correction becomes a permanent lesson for the agent, making it progressively smarter and more aligned with the project's specific context over time.

## 4. Automation and Sub-Agents

Repetitive and bureaucratic tasks are heavily automated using slash commands and specialized sub-agents.

-   **Slash Commands:** Custom shortcuts, checked into the repository, handle multi-step operations like `git commit`, `git push`, and opening a pull request with a single command (`/commit-push-pr`).
-   **Sub-Agents:** Specialized AI personas are deployed for specific phases of development, such as a `code-simplifier` for refactoring or a `verify-app` agent for end-to-end testing.

## 5. The Verification Loop: The Key to Quality

The most critical component of the workflow is the verification loop. The AI is not just tasked with writing code; it is required to **prove the code works**.

Cherny gives his Claude agents the ability to test their own changes by running test suites, executing bash commands, or even using a Chrome extension to interact with a web UI. This feedback loop forces the agent to iterate and self-correct until the code is not only written but also functional and meets quality standards. This practice is reported to improve the final quality of AI-generated code by 2-3x.

---
## Practical Implementation: Oh My Claude Code

The "fleet commander" workflow described by Boris Cherny has been productized and automated in a popular open-source plugin called **Oh My Claude Code (OMC)**. This tool provides a structured framework for running multiple specialized agents in parallel, complete with different execution modes and smart model routing.

It serves as a practical, real-world implementation of the high-efficiency, multi-agent orchestration philosophy.

-   **See the full guide:** [[kb/AI/1_models/1_specific-models/claude/02_oh-my-claude-code|Oh My Claude Code (OMC): Agent Swarm Orchestration]]

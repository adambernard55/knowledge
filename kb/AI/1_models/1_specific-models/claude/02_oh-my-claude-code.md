---
title: "Oh My Claude Code (OMC): Agent Swarm Orchestration"
id: "KB/AI/M-CL-02"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-02-07"
status: "Active"
doc_type: "Reference"
summary: "A guide to 'Oh My Claude Code' (OMC), a plugin that transforms the Claude Code terminal into a multi-agent orchestration system with specialized agents and automated workflows."
tags:
  - "ai"
  - "claude"
  - "anthropic"
  - "agent-swarm"
  - "orchestration"
  - "claude-code"
  - "omc"
  - "developer-tools"
relations:
  - "kb/AI/1_models/1_specific-models/claude/01_creator-of-claude-code.md"
  - "kb/AI/1_models/1_specific-models/3_claude.md"
aliases:
  - "OMC"
  - "Oh My Claude Code"
  - "Claude Agent Swarm"

# --- AI & RAG Enhancement ---
semantic_summary: >
  This document reviews 'Oh My Claude Code' (OMC), a powerful plugin that provides multi-agent swarm orchestration for the Claude Code terminal. OMC features five execution modes (Autopilot, Ultrapilot, Swarm, Pipeline, Ecomode), 32 specialized agents, and smart model routing between Haiku, Sonnet, and Opus to optimize performance and cost. It enables developers to manage complex tasks using natural language, shifting from manual coding to orchestrating a team of autonomous AI agents.
synthetic_questions:
  - "What is Oh My Claude Code (OMC)?"
  - "What are the five execution modes of Oh My Claude Code?"
  - "How does OMC use different Claude models like Haiku, Sonnet, and Opus?"
  - "How does OMC simplify multi-agent orchestration for developers?"
key_concepts:
  - "Oh My Claude Code (OMC)"
  - "Agent Swarm Orchestration"
  - "Claude Code"
  - "Autopilot Mode"
  - "Smart Model Routing"
  - "Specialized Agents"
  - "Developer Productivity"
---
# Oh My Claude Code: The Agent Swarm Orchestration You Need

"Oh My Claude Code" (OMC) is a plugin for the Claude Code terminal that transforms the standard request-response workflow into a sophisticated multi-agent orchestration system. Inspired by the simplicity of tools like `oh-my-zsh`, OMC provides a zero-learning-curve framework with 32 specialized agents and 40 skills, allowing developers to manage complex software development tasks using natural language.

The core value proposition is a shift from manual coding to orchestrating a swarm of autonomous agents, dramatically increasing efficiency.

## Key Features & Execution Modes

OMC is built around five distinct execution modes, each designed for different scenarios, from fully autonomous builds to budget-conscious optimization.

### 1. Autopilot — Full Autonomous Execution
The flagship mode where a user describes a high-level goal, and OMC handles the entire lifecycle: planning, parallel execution with specialized agents, continuous testing, and self-correction until the task is complete.

### 2. Ultrapilot — Parallel Autopilot (3–5x Faster)
This mode enhances Autopilot by using up to five concurrent workers. It automatically decomposes large tasks into parallelizable sub-tasks, making it ideal for large refactoring jobs or building applications with multiple independent components.

### 3. Swarm — Coordinated Agent Teams
Swarm mode spawns a specified number of agents that pull from a shared task pool. Each agent claims an atomic task, executes it, and marks it as complete, preventing duplicate work. This mimics a development team working through a sprint backlog.

### 4. Pipeline — Sequential Agent Chaining
For workflows that require a specific order of operations, Pipeline chains agents in sequence, passing the output of one stage as the input to the next. It includes built-in presets for common tasks like `review`, `implement`, and `debug`.

### 5. Ecomode — Token-Efficient Parallelism
Ecomode provides parallel execution while optimizing for cost, achieving 30–50% token savings. It uses smart model routing to delegate tasks to the most cost-effective model capable of handling the complexity:
- **Simple tasks:** Haiku
- **Standard work:** Sonnet
- **Complex reasoning:** Opus

## Smart Delegation and Control

A key feature of OMC is its ability to interpret natural language to activate modes and delegate tasks, minimizing the need for users to memorize specific commands. For example, including "don't stop until done" in a prompt activates a persistence mode.

It also routes tasks to the appropriate specialized agent automatically. A request to "fix the UI colors" is delegated to a `designer` agent, while "debug this crash" is sent to an `architect` agent. This ensures the right level of reasoning (and the right model) is applied to each task.

## Final Assessment

OMC successfully delivers on its promise of making multi-agent orchestration accessible. It formalizes and automates the "fleet commander" workflow, allowing a single developer to achieve the output of a small team. Its smart model routing is a critical feature for managing costs on large projects, while its natural language interface makes it intuitive for everyday use. For any developer using Claude Code for more than simple prompts, OMC is a significant force multiplier.

---
title: Agent Skills for Context Engineering
id: SIE/REF/AI-07
version: "1.0"
steward: Adam Bernard
updated: 2026-02-03
status: Active
doc_type: Reference
summary: A reference guide on Context Engineering for AI agents, detailing the principles of managing a language model's context window to maximize effectiveness. It covers foundational skills, architectural patterns, and operational best practices.
tags:
  - context-engineering
  - ai-agents
  - llm
  - prompt-engineering
  - agent-skills
relations:
  - "[[Introduction to AI Agents]]"
  - "[[Agentic Workflows]]"
aliases:
  - Context Engineering
  - AI Agent Context Skills
semantic_summary: This document defines Context Engineering as the discipline of curating all information within an LLM's context window, including prompts, tools, and history, to mitigate degradation patterns like 'lost-in-the-middle'. It provides a structured collection of skills covering foundational concepts, multi-agent architectures, memory systems, and evaluation techniques to build production-grade AI agent systems.
synthetic_questions:
  - What is context engineering?
  - How do I improve the reliability of my AI agent?
  - What are the best practices for designing agent tools and memory?
key_concepts:
  - Context Engineering
  - Context Window
  - Lost-in-the-Middle
  - Multi-Agent Patterns
  - Memory Systems
  - LLM-as-a-Judge
primary_keyword: context engineering
---

# Agent Skills for Context Engineering

This document provides a comprehensive collection of Agent Skills focused on context engineering principles for building production-grade AI agent systems. These skills teach the art and science of curating context to maximize agent effectiveness across any platform.

## 1. What is Context Engineering?

Context engineering is the discipline of managing the language model's context window. Unlike prompt engineering, which focuses on crafting effective instructions, context engineering addresses the holistic curation of all information that enters the model's limited attention budget: system prompts, tool definitions, retrieved documents, message history, and tool outputs.

The fundamental challenge is that context windows are constrained not by raw token capacity but by attention mechanics. As context length increases, models exhibit predictable degradation patterns: the "lost-in-the-middle" phenomenon, U-shaped attention curves, and attention scarcity. Effective context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of desired outcomes.

## 2. Skills Overview

### 2.1. Foundational Skills
These skills establish the foundational understanding required for all subsequent context engineering work.

| Skill | Description |
| :--- | :--- |
| `context-fundamentals` | Understand what context is, why it matters, and the anatomy of context in agent systems. |
| `context-degradation` | Recognize patterns of context failure: lost-in-middle, poisoning, distraction, and clash. |
| `context-compression` | Design and evaluate compression strategies for long-running sessions. |

### 2.2. Architectural Skills
These skills cover the patterns and structures for building effective agent systems.

| Skill | Description |
| :--- | :--- |
| `multi-agent-patterns` | Master orchestrator, peer-to-peer, and hierarchical multi-agent architectures. |
| `memory-systems` | Design short-term, long-term, and graph-based memory architectures. |
| `tool-design` | Build tools that agents can use effectively. |

### 2.3. Operational Skills
These skills address the ongoing operation and optimization of agent systems.

| Skill | Description |
| :--- | :--- |
| `context-optimization` | Apply compaction, masking, and caching strategies. |
| `evaluation` | Build evaluation frameworks for agent systems. |
| `advanced-evaluation` | Master LLM-as-a-Judge techniques: direct scoring, pairwise comparison, rubric generation, and bias mitigation. |

### 2.4. Development Methodology
These skills cover the meta-level practices for building LLM-powered projects.

| Skill | Description |
| :--- | :--- |
| `project-development` | Design and build LLM projects from ideation through deployment, including task-model fit analysis, pipeline architecture, and structured output design. |

## 3. Design Philosophy

-   **Progressive Disclosure:** Each skill is structured for efficient context use. At startup, agents load only skill names and descriptions. Full content loads only when a skill is activated for relevant tasks.
-   **Platform Agnosticism:** These skills focus on transferable principles rather than vendor-specific implementations. The patterns work across Claude Code, Cursor, and any agent platform that supports skills or allows custom instructions.
-   **Conceptual Foundation with Practical Examples:** Scripts and examples demonstrate concepts using Python pseudocode that works across environments without requiring specific dependency installations.

## 4. Usage & Examples

The `examples` folder contains complete system designs that demonstrate how multiple skills work together in practice.

| Example | Description | Skills Applied |
| :--- | :--- | :--- |
| `digital-brain-skill` | Personal operating system for founders. Complete Claude Code skill with 6 modules and 4 automation scripts. | `context-fundamentals`, `context-optimization`, `memory-systems`, `tool-design`, `multi-agent-patterns`, `evaluation`, `project-development` |
| `x-to-book-system` | Multi-agent system that monitors X accounts and generates daily synthesized books. | `multi-agent-patterns`, `memory-systems`, `context-optimization`, `tool-design`, `evaluation` |
| `llm-as-judge-skills` | Production-ready LLM evaluation tools with TypeScript implementation. | `advanced-evaluation`, `tool-design`, `context-fundamentals`, `evaluation` |
| `book-sft-pipeline` | Train models to write in any author's style. Includes Gertrude Stein case study. | `project-development`, `context-compression`, `multi-agent-patterns`, `evaluation` |

Each example includes a complete PRD, skills mapping, and implementation guidance.
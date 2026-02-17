---
title: AI Agents Knowledge Base Index
id: kb/AI/2_agents/index
version: "1.1"
steward: Adam Bernard
updated: 2026-01-15
status: Active
doc_type: kb_index
semantic_summary: Central navigation hub for the AI Agents knowledge base, linking to core concepts, architectural patterns, and specific toolkits for building and deploying autonomous systems.
tags:
  - index
  - ai
  - agents
  - knowledge-base
  - navigation
relations:
  - kb/AI/index
aliases:
  - AI Agents Index
  - Agent KB
---
# AI Agents

This section covers the design, architecture, and implementation of AI agents. It moves beyond simple chat interfaces to explore how agents can plan, call tools, and execute complex, multi-step workflows autonomously.

---

## Contents

- **[[00_introduction-to-ai-agents|Introduction to AI Agents]]** — This document provides a foundational overview of AI agents, defining them as autonomous, goal-oriented systems that leverage LLMs, tools, and memory. It contrasts agents with reactive chatbots, outlines their strategic business purpose in reducing cognitive load via a 'Fleet Commander Model,' details the ReAct architecture, classifies autonomy levels using frameworks from other industries, and discusses key challenges like defining a digital ODD.
- **[[01_ai-agents-running-workflows|AI Agents Running Workflows: From Automation to Autonomous Orchestration]]** — Learn how AI agents execute multi-step workflows using a reasoning loop (ReAct). This guide covers the architecture, best practices, and the critical role of well-designed tools for building autonomous systems.
- **[[02_how-to-build-fullstack-agent-applications|How to Build Full-Stack Agent Applications]]** — This document provides a technology-agnostic architectural pattern for building interactive, full-stack AI agent applications. It covers the essential components: the front-end UI, the back-end API server, and the core agentic reasoning engine.
- **[[03_build-an-ai-desktop-automation-agent|Framework for Building an AI Desktop Automation Agent]]**
- **[[04_agentic-reinforcement-learning|Agentic Reinforcement Learning (Agentic RL): A Technical Overview]]**
- **[[05_agentic-vs-automation-platforms|Agentic vs. Automation Platforms: A Comparison of OpenAI AgentKit, n8n, and Make]]**
- **[[06_building-an-ai-agent-with-dual-memory|Building an AI Agent with Dual-Memory Architecture]]** — This document outlines a blueprint for building stateful AI agents by implementing a dual-memory architecture. It addresses the challenge of 'agent amnesia' by separating memory into two components: a rolling summary for short-term conversational context and a vector database for long-term, semantically searchable knowledge. The guide details the implementation of each memory type and describes the integrated reasoning loop where the agent combines both to generate context-aware responses.
- **[[07_vector-databases|Vector Databases]]** — An overview of vector databases, which are specialized systems designed for efficient similarity searches in high-dimensional spaces. Covers core algorithms like HNSW and IVF, the recall-latency trade-off, and their critical role in applications like RAG and semantic search.
- **[[08_designing-effective-agent-tools|Designing Effective Tools for AI Agents]]** — Learn the core principles for designing, defining, and implementing robust tools for AI agents, focusing on clarity, specificity, and error handling to maximize performance and reliability.
- **[[09_agent-driven-interfaces-with-a2ui|Agent-Driven Interfaces with A2UI]]** — An overview of Google's A2UI, an open-source protocol that allows AI agents to securely and declaratively describe user interfaces in a JSON format, which client applications can render using their own native components.
- **[[10_architecting-a-private-multi-user-rag-agent|Architecting a Private, Multi-User Agentic RAG System]]** — Learn how to architect and build a private, multi-tenant agentic RAG system. This guide covers the components, data flows, and security principles for creating a self-hosted chatbot that provides personalized, secure access to user-specific documents.
- **[[11_designing-effective-agent-tools|Designing Effective Tools for AI Agents]]** — Learn the core principles for designing, defining, and implementing robust tools for AI agents, focusing on clarity, specificity, and error handling to maximize performance and reliability.
- **[[12_agentic-workflows-research-analyst-editor|Agentic Workflows: How Research, Analyst, and Editor Agents Collaborate]]** — This document details the agentic workflow model, a structured methodology for producing strategic intelligence. It breaks down the distinct roles of the Research Agent (data gathering), Analyst Agent (synthesis and insight), and Editor Agent (quality control and governance), explaining how their collaboration forms a repeatable production line for decision-ready outcomes.
- **[[13_reference-architecture-for-trustworthy-agentic-ai|Reference Architecture for Building Trustworthy Agentic AI Systems]]** — This document details a reference architecture for trustworthy agentic AI systems, specifically focusing on command-line interface (CLI) agents. It contrasts planning styles like ReAct and plan-and-execute, explains the role of the Model Context Protocol (MCP) for tooling, and outlines essential safety guardrails like sandboxing and human-in-the-loop approvals for reliable operation.
- **[[14_building-your-first-personal-ai-agent|Building Your First Personal AI Agent]]** — This guide provides a step-by-step framework for building a personal AI agent. It covers core components like LLMs, tools, and memory; compares no-code (Make, Zapier) and code-based (OpenAI SDK, LangChain) approaches; outlines a development process from use case definition to deployment; and details common pitfalls such as vague prompts and poor error handling.
- **[[15_blueprint-for-an-enterprise-ai-assistant|Blueprint for an Enterprise AI Assistant]]** — This document provides a technical blueprint for building a secure Enterprise AI Assistant using open-source models. It details a RAG architecture with components like FLAN-T5 for generation, MiniLM for embeddings, and FAISS for vector search, while enforcing security through custom policy guardrails for data redaction and access control.
- **[[16_architecture-for-a-private-multi-user-agentic-assistant|Architecture for a Private, Multi-User Agentic Assistant]]** — This document details the architecture for a self-hosted, multi-tenant agentic assistant. It uses a privacy-first stack including Ollama for local LLMs, Minio for blob storage, and Postgres with pgvector for permission-based vector search. The system's workflows for file management, asynchronous embedding, and agentic chat are orchestrated via a RabbitMQ message queue and a LangGraph agent.
- **[[17_building-with-deep-agents|Building Multi-Agent Applications with Deep Agents]]** — This document explains how to build multi-agent applications using the Deep Agents framework. It introduces two core primitives: 'subagents,' which are isolated agents used to prevent context bloat and enable specialization, and 'skills,' which allow for the progressive disclosure of agent capabilities from SKILL.md files. The guide provides code examples, best practices for designing subagents and skills, and a decision framework for choosing between the two patterns.
- **[[18_open-coding-agents-sera|Open Coding Agents (SERA): An Accessible Framework for Specializing Code Agents]]** — This document introduces Open Coding Agents and the SERA model family, an open-source framework designed for creating and fine-tuning coding agents on custom repositories. It details the 'Soft-verified generation' (SVG) method, which significantly reduces training costs, and presents benchmarks showing SERA's competitive performance against models like Devstral Small 2. The guide also covers its compatibility with Claude Code and optimizations for NVIDIA hardware.
- **[[19_agent-skills-for-context-engineering|Agent Skills for Context Engineering]]** — This document defines Context Engineering as the discipline of curating all information within an LLM's context window, including prompts, tools, and history, to mitigate degradation patterns like 'lost-in-the-middle'. It provides a structured collection of skills covering foundational concepts, multi-agent architectures, memory systems, and evaluation techniques to build production-grade AI agent systems.
- **[[20_moltworker-a-self-hosted-personal-ai-agent|Moltworker: A Self-Hosted Personal AI Agent on Cloudflare]]** — This document details Moltworker, a proof-of-concept for running the Moltbot personal AI agent on Cloudflare's serverless infrastructure. It outlines an architecture using Cloudflare Workers, Sandbox SDK for isolated code execution, R2 for persistent storage, Browser Rendering for web automation, and AI Gateway for model management, presenting a viable alternative to running the agent on dedicated local hardware like a Mac mini.
- **[[21_context-management-for-deep-agents|Context Management for Deep Agents: A Technical Guide]]** — This document details the context management strategies within the LangChain Deep Agents SDK, designed to prevent 'context rot' in long-running tasks. It covers three primary context compression techniques: offloading large tool results to a filesystem, offloading large tool inputs (write/edit arguments) when context exceeds a threshold, and finally, summarizing the conversation history while preserving the full transcript on the filesystem for later retrieval. The guide also discusses evaluation methods, such as 'needle-in-the-haystack' tests, to ensure information recoverability and prevent goal drift.
- **[[22_designing-effective-multi-agent-architectures.md|Designing Effective Multi-Agent Architectures]]** — This document argues that agentic failures are often architectural rather than prompt-based.  It details four core collaboration patterns (Supervisor, Blackboard, P2P, Swarms) and provides  a framework for "hiring" models based on architectural personality (Decoder, Encoder, MoE, Reasoning).
- **[[standards/index|Standards]]**
- **[[toolkits/index|Toolkits]]**

TABLE WITHOUT ID

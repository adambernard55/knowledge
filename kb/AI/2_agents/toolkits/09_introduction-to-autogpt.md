---
title: "Introduction to AutoGPT: Build, Deploy, and Run AI Agents"
id: "kb/AI/toolkits/autogpt"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-01-20"
status: "Active"
doc_type: "Reference"
summary: "A technical overview of the AutoGPT platform, an open-source framework for creating, deploying, and managing continuous AI agents that automate complex workflows."
tags:
  - autogpt
  - ai-agents
  - toolkits
  - autonomous-agents
  - agent-framework
  - open-source
relations:
  - "kb/AI/2_agents/00_introduction-to-ai-agents"
  - "kb/AI/2_agents/01_ai-agents-running-workflows"
  - "kb/AI/2_agents/toolkits/index"
aliases:
  - "AutoGPT"
  - "Auto-GPT"
target_audience: "Developer"
security_level: "Public"
owner_team: "Knowledge"
semantic_summary: "This document provides a comprehensive guide to AutoGPT, an open-source platform for building and running autonomous AI agents. It covers the core components (Frontend, Server), self-hosting requirements using Docker, and the classic toolset including Forge for agent creation and Benchmark for performance evaluation. The licensing model, which combines Polyform Shield and MIT licenses, is also explained."
synthetic_questions:
  - "What is AutoGPT and what is its primary purpose?"
  - "How can I self-host the AutoGPT platform?"
  - "What are the core components of the AutoGPT platform?"
  - "What is AutoGPT Forge and how is it used?"
  - "What is the licensing model for AutoGPT?"
key_concepts:
  - "AutoGPT"
  - "Autonomous AI Agents"
  - "Agent Framework"
  - "Self-Hosting"
  - "Docker"
  - "AutoGPT Forge"
  - "Agent Benchmark"
  - "Agent Protocol"
primary_keyword: "AutoGPT"
seo_title: "A Developer's Guide to AutoGPT: Build & Deploy AI Agents"
meta_description: "Learn how to build, deploy, and run autonomous AI agents with this technical guide to the AutoGPT platform, covering self-hosting, core components, and classic tools."
excerpt: "Explore the AutoGPT platform, an open-source framework for creating autonomous AI agents. This guide covers self-hosting, core components like Forge and Benchmark, and how to get started building complex workflows."
---

# Introduction to AutoGPT: Build, Deploy, and Run AI Agents

AutoGPT is an open-source platform designed for creating, deploying, and managing continuous AI agents that can automate complex, multi-step workflows. It provides the tools to move beyond simple prompt-and-response interactions to building autonomous systems that can achieve specific goals.

## Platform Overview

The modern AutoGPT platform is composed of two primary components: a user-facing frontend and a backend server that executes the agentic workflows.

### AutoGPT Frontend

The frontend is the primary interface for interacting with the platform. Its key features include:

-   **Agent Builder:** An intuitive, low-code interface for designing and configuring custom AI agents by connecting functional blocks.
-   **Workflow Management:** Tools to build, modify, and optimize automation workflows.
-   **Pre-configured Agents:** A library of ready-to-use agents for common tasks.
-   **Monitoring and Analytics:** Dashboards to track agent performance and gain insights.

### AutoGPT Server

The server is the engine of the platform where agents run. Once deployed, agents can be triggered by external sources and operate continuously. It contains the core logic, infrastructure, and a marketplace for discovering pre-built agents.

## Self-Hosting Guide

Setting up and hosting the AutoGPT platform is a technical process that requires familiarity with Docker and the command line.

### System Requirements

-   **CPU:** 4+ cores
-   **RAM:** 8GB minimum (16GB recommended)
-   **Storage:** 10GB+ free space
-   **OS:** Linux (Ubuntu 20.04+), macOS (10.15+), or Windows 10/11 with WSL2
-   **Software:** Docker Engine, Docker Compose, Git, Node.js (16.x+), npm (8.x+)

### Quick Setup Script

The recommended method for local hosting is the one-line setup script, which handles dependencies, configures Docker, and launches the instance.

**For macOS/Linux:**

```bash
curl -fsSL https://setup.agpt.co/install.sh -o install.sh && bash install.sh
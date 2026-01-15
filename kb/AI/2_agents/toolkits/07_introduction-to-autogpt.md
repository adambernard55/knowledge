---
title: "Introduction to AutoGPT"
id: "kb/AI/2_agents/toolkits/07_introduction-to-autogpt"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-01-15"
status: "Active"
doc_type: "Reference"
summary: "A reference guide for the AutoGPT platform, covering self-hosting, core components (Frontend, Server), and related tools like Forge and agbenchmark."
tags:
  - autogpt
  - ai-agents
  - toolkit
  - framework
  - open-source
  - self-hosting
relations:
  - "kb/AI/2_agents/toolkits/index"
  - "kb/AI/2_agents/00_introduction-to-ai-agents"
aliases:
  - "AutoGPT Guide"
  - "AutoGPT Platform"
target_audience: "All_Staff"
security_level: "Internal"
owner_team: "Engineering"
semantic_summary: "This document provides a guide to the AutoGPT platform, an open-source tool for creating and deploying autonomous AI agents. It details system requirements for self-hosting, explains the roles of the AutoGPT Frontend and Server, and introduces associated projects like Forge for building custom agents and agbenchmark for performance testing."
synthetic_questions:
  - "How do you self-host the AutoGPT platform?"
  - "What are the core components of AutoGPT?"
  - "What is AutoGPT Forge used for?"
  - "How does the AutoGPT license work?"
key_concepts:
  - "AutoGPT"
  - "Agent Builder"
  - "Self-Hosting"
  - "Forge"
  - "agbenchmark"
  - "Agent Protocol"
primary_keyword: "autogpt"
seo_title: "What is AutoGPT? A Guide to the AI Agent Platform"
meta_description: "Learn about AutoGPT, an open-source platform to build, deploy, and run autonomous AI agents. Covers self-hosting, Forge, and more."
excerpt: "A complete guide to the AutoGPT platform, an open-source tool for creating autonomous AI agents. Learn how to self-host, build with Forge, and benchmark performance."
cover_image: ""
---

# AutoGPT: Build, Deploy, and Run AI Agents

AutoGPT is a powerful platform that allows you to create, deploy, and manage continuous AI agents that automate complex workflows.

## How to Self-Host the AutoGPT Platform

Setting up and hosting the AutoGPT Platform yourself is a technical process. If you'd rather something that just works, we recommend joining the waitlist for the cloud-hosted beta.

### System Requirements
Before proceeding with the installation, ensure your system meets the following requirements:

**Hardware Requirements**
- CPU: 4+ cores recommended
- RAM: Minimum 8GB, 16GB recommended
- Storage: At least 10GB of free space

**Software Requirements**
- Operating Systems:
  - Linux (Ubuntu 20.04 or newer recommended)
  - macOS (10.15 or newer)
  - Windows 10/11 with WSL2
- Required Software (with minimum versions):
  - Docker Engine (20.10.0 or newer)
  - Docker Compose (2.0.0 or newer)
  - Git (2.30 or newer)
  - Node.js (16.x or newer)
  - npm (8.x or newer)
  - VSCode (1.60 or newer) or any modern code editor

**Network Requirements**
- Stable internet connection
- Access to required ports (will be configured in Docker)
- Ability to make outbound HTTPS connections

### Setup Instructions
We've moved to a fully maintained and regularly updated documentation site.

👉 **Follow the official self-hosting guide here**

This tutorial assumes you have Docker, VSCode, git and npm installed.

#### ⚡ Quick Setup with One-Line Script (Recommended for Local Hosting)
Skip the manual steps and get started in minutes using our automatic setup script.

**For macOS/Linux:**
```bash
curl -fsSL https://setup.agpt.co/install.sh -o install.sh && bash install.sh
```

This will install dependencies, configure Docker, and launch your local instance — all in one go.

## 🧱 AutoGPT Frontend

The AutoGPT frontend is where users interact with our powerful AI automation platform. It offers multiple ways to engage with and leverage our AI agents. This is the interface where you'll bring your AI automation ideas to life:

- **Agent Builder:** For those who want to customize, our intuitive, low-code interface allows you to design and configure your own AI agents.
- **Workflow Management:** Build, modify, and optimize your automation workflows with ease. You build your agent by connecting blocks, where each block performs a single action.
- **Deployment Controls:** Manage the lifecycle of your agents, from testing to production.
- **Ready-to-Use Agents:** Don't want to build? Simply select from our library of pre-configured agents and put them to work immediately.
- **Agent Interaction:** Whether you've built your own or are using pre-configured agents, easily run and interact with them through our user-friendly interface.
- **Monitoring and Analytics:** Keep track of your agents' performance and gain insights to continually improve your automation processes.

## 💽 AutoGPT Server

The AutoGPT Server is the powerhouse of our platform. This is where your agents run. Once deployed, agents can be triggered by external sources and can operate continuously. It contains all the essential components that make AutoGPT run smoothly.

- **Source Code:** The core logic that drives our agents and automation processes.
- **Infrastructure:** Robust systems that ensure reliable and scalable performance.
- **Marketplace:** A comprehensive marketplace where you can find and deploy a wide range of pre-built agents.

## 🐙 Example Agents

Here are two examples of what you can do with AutoGPT:

**Generate Viral Videos from Trending Topics**

- This agent reads topics on Reddit.
- It identifies trending topics.
- It then automatically creates a short-form video based on the content.

**Identify Top Quotes from Videos for Social Media**

- This agent subscribes to your YouTube channel.
- When you post a new video, it transcribes it.
- It uses AI to identify the most impactful quotes to generate a summary.
- Then, it writes a post to automatically publish to your social media.

## License Overview

- **🛡️ Polyform Shield License:** All code and content within the `autogpt_platform` folder is licensed under the Polyform Shield License.
- **🦉 MIT License:** All other portions of the AutoGPT repository (i.e., everything outside the `autogpt_platform` folder) are licensed under the MIT License. This includes the original stand-alone AutoGPT Agent, along with projects such as Forge, agbenchmark and the AutoGPT Classic GUI.

## 🤖 AutoGPT Classic & Related Tools

### 🏗️ Forge

Forge is a ready-to-go toolkit to build your own agent application. It handles most of the boilerplate code, letting you channel all your creativity into the things that set your agent apart.

### 🎯 Benchmark (agbenchmark)

The `agbenchmark` can be used with any agent that supports the agent protocol. The benchmark offers a stringent testing environment, allowing for autonomous, objective performance evaluations to ensure your agents are primed for real-world action.

### 💻 UI

The frontend gives you a user-friendly interface to control and monitor your agents. It connects to agents through the agent protocol, ensuring compatibility with many agents.

### ⌨️ CLI

A command-line interface is included at the root of the repo to make it easy to use all the tools. After cloning, you can install dependencies with `./run setup`.
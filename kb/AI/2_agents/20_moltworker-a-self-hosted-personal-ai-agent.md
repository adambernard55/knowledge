---
title: "Moltworker: A Self-Hosted Personal AI Agent on Cloudflare"
id: SIE/REF/AI-20
version: "1.0"
steward: Adam Bernard
updated: 2026-02-03
status: Active
doc_type: Reference
summary: A reference guide on Moltworker, an open-source project that adapts the Moltbot personal AI agent to run on Cloudflare's developer platform instead of dedicated local hardware.
tags:
  - ai-agents
  - self-hosting
  - cloudflare
  - moltbot
  - serverless
  - proof-of-concept
relations:
  - "[[14_building-your-first-personal-ai-agent]]"
  - "[[16_architecture-for-a-private-multi-user-agentic-assistant]]"
aliases:
  - Moltworker
  - Cloudflare AI Agent
semantic_summary: "This document details Moltworker, a proof-of-concept for running the Moltbot personal AI agent on Cloudflare's serverless infrastructure. It outlines an architecture using Cloudflare Workers, Sandbox SDK for isolated code execution, R2 for persistent storage, Browser Rendering for web automation, and AI Gateway for model management, presenting a viable alternative to running the agent on dedicated local hardware like a Mac mini."
synthetic_questions:
  - "How can I self-host the Moltbot AI agent without dedicated hardware?"
  - "What is Moltworker and how does it work?"
  - "What Cloudflare services are used to run the Moltworker AI agent?"
key_concepts:
  - Moltworker
  - Moltbot
  - Self-Hosted AI Agent
  - Cloudflare Workers
  - Sandbox SDK
  - Browser Rendering
  - R2 Storage
  - AI Gateway
primary_keyword: "Moltworker"
---

# Moltworker: A Self-Hosted Personal AI Agent

## 1. Overview

Moltworker is an open-source, self-hosted personal AI agent designed as an alternative to running Moltbot on dedicated local hardware (like a Mac mini). It is a middleware and set of adapted scripts that allows the Moltbot agent to run efficiently and securely on Cloudflare's Developer Platform, leveraging a suite of serverless products.

While the original Moltbot is designed for local hardware, Moltworker demonstrates how a complex, stateful AI agent can be deployed in the cloud, controlled remotely, and integrated with popular messaging apps to act as a personal assistant for tasks related to finance, social media, and daily organization.

## 2. Core Architecture

Moltworker combines several Cloudflare services to replicate the functionality of a local server environment.

-   **Cloudflare Workers:** Acts as the entrypoint, API router, and proxy between Cloudflare's APIs and the isolated agent environment. It also serves the administration UI.
-   **Sandboxes (Sandbox SDK):** Provides a secure, isolated environment to run the untrusted code of the Moltbot service. The Sandbox SDK offers a developer-friendly API to execute commands, manage files, and run background processes within a container without needing to manage the container's lifecycle directly.
-   **R2 Storage:** Solves the problem of ephemeral container storage. An R2 bucket is mounted as a filesystem partition within the Sandbox, allowing Moltbot to store session memory, conversation history, and other assets persistently.
-   **Browser Rendering:** Replaces the need for a local Chromium instance for web automation tasks. Moltworker uses a thin CDP (Chrome DevTools Protocol) proxy to connect the agent's runtime to Cloudflare's headless browser instances, allowing it to navigate websites, fill forms, and take screenshots via API.
-   **AI Gateway:** Acts as a proxy between the agent and the underlying AI model provider (e.g., Anthropic). This provides centralized control, observability, logging, and cost management. It also allows for easy model switching and provider fallbacks without changing the agent's code.
-   **Zero Trust Access:** Secures the agent's APIs and admin UI with authentication policies and login methods, protecting them from unauthorized access.

![High-level architecture diagram of Moltworker.](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/3OD2oHgy5ilHpQO2GJvcLU/836a55b67a626d2cd378a654ad47901d/newdiagram.png)

## 3. How to Deploy

The implementation is open-sourced and available on GitHub for users to deploy their own instance.

-   **Repository:** [https://github.com/cloudflare/moltworker](https://github.com/cloudflare/moltworker)
-   **Requirements:** A Cloudflare account with a paid Workers plan is required to use Sandbox Containers. Other services like AI Gateway and R2 have generous free tiers.

**Note:** Moltworker is presented as a proof of concept to showcase the capabilities of the Cloudflare Developer Platform for running AI agents, not as an official Cloudflare product.

## 4. Use Case Examples

-   **Information Retrieval:** Asking the agent to find directions on Google Maps and take a screenshot.
-   **Web Automation:** Instructing the agent to find local restaurants, browse menus, and provide recommendations.
-   **Content Creation:** Tasking the agent with creating a video by browsing a website, capturing frames, and compiling them using `ffmpeg` within the Sandbox environment.
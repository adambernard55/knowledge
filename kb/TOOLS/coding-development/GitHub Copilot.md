---
title: GitHub Copilot
id: 20251209052545
version: 1
Author: Adam Bernard
steward:
date: 2025-12-09
tool_name: "GitHub Copilot"
tool_category: ["Coding & Development"]
primary_function: "An AI pair programmer that offers autocomplete-style suggestions as you code."
ai_type: ["Code Generation", "Code Completion"]
pricing_model: "Subscription"
difficulty: "Beginner"
website: "https://github.com/features/copilot"
Excerpt: "GitHub Copilot is the industry-standard AI pair programmer that integrates directly into your code editor to provide real-time code suggestions, generate entire functions from comments, and accelerate the development process."
Meta Description: "Learn about GitHub Copilot, the AI-powered code completion tool from GitHub and OpenAI. Speed up your programming workflow with intelligent suggestions in VS Code, JetBrains, and more."
Primary_Keyword: "GitHub Copilot"
relations:
aliases:
last_updated: 2025-12-09
tags: ["tool", "ai", "coding", "development", "github"]
---

# [[GitHub Copilot]]

## What It Is

GitHub Copilot is the industry-leading AI developer platform that integrates directly into the software development lifecycle. Originally just a "pair programmer" for code completion, it has evolved into a comprehensive suite of AI tools powered by a "multi-model" approach. Developers can now choose their underlying LLM (e.g., Anthropic’s **Claude 3.7 Sonnet**, Google’s **Gemini 1.5 Pro**, or OpenAI’s **o3-mini**) to best suit their specific task, whether it's fast reasoning, large context windows, or creative generation.

## Core Features

### 1. Multi-Model Choice

- **Model Switching:** Developers are no longer locked into a single model. You can toggle between different AI models in Copilot Chat depending on the need—using **Claude 3.5/3.7 Sonnet** for complex coding tasks, **Gemini 1.5 Pro** for massive context windows (up to 2M tokens), or **OpenAI’s o3-mini** for high-speed reasoning.
    

### 2. Copilot Workspace (Agentic Workflow)

- **Issue-to-PR Agent:** A task-centric environment that allows developers to go from a GitHub Issue to a Pull Request in one flow. Copilot Workspace analyzes the issue, proposes a plan (in natural language), generates a "spec," and then implements the code across multiple files automatically.
    
- **Natural Language Steering:** If the plan isn't quite right, you can edit the natural language steps, and the AI will regenerate the code implementation to match.
    

### 3. Advanced Context & Completion

- **Next Edit Suggestions (NES):** Beyond just completing the current line, Copilot now predicts _where_ you are likely to edit next and suggests changes for that location, speeding up refactoring tasks.
    
- **Repository Indexing:** For Enterprise users, Copilot indexes the entire organization's codebase, allowing it to answer questions ("How does our authentication service talk to the billing service?") with deep understanding of proprietary libraries and legacy code.
    

### 4. Copilot Chat & Extensions

- **Extensions Platform:** Copilot Chat now supports third-party extensions. You can query external tools directly from your IDE—for example, asking Copilot to "Check Sentry for recent errors in this function" or "Deploy this to Azure."
    
- **Inline Chat:** Highlight code and ask Copilot to refactor, debug, or explain it without leaving the editor window.
    

### 5. Copilot Autofix

- **Security Remediation:** Integrated with GitHub Advanced Security, this feature detects vulnerabilities in code (like SQL injection or XSS) and automatically generates a pull request to fix them.
    

## Supported Environments

- **IDEs:** Visual Studio Code, Visual Studio (2022/2026), JetBrains IDEs (IntelliJ, PyCharm), and **Xcode** (now with full Chat support).
    
- **CLI:** A "gh copilot" extension for the command line that helps generate shell commands and explain terminal outputs.
    
- **Mobile:** Access to Copilot Chat and agent sessions via the GitHub mobile app.
    

## Use Cases

- **Legacy Code Modernization:** Using Copilot Workspace to safely refactor large, brittle legacy files by describing the desired architectural changes in plain English.
    
- **Incident Response:** Using Copilot Extensions to pull logs from monitoring tools (like Datadog or Sentry) and ask the AI to identify the root cause of a bug directly in the chat interface.
    
- **Test-Driven Development (TDD):** Writing a test file first, then using Copilot to generate the implementation code that satisfies those tests.
    
- **Cross-Language Translation:** rapidly porting functions or entire classes from one language (e.g., Java) to another (e.g., Go) while adhering to the idioms of the target language.
---
title: Building Multi-Agent Applications with Deep Agents
id: kb/AI/2_agents/deep-agents-multi-agent-apps
version: "1.0"
steward: Adam Bernard
updated: 2026-01-23
status: Active
doc_type: Reference
summary: A technical guide on using the Deep Agents framework to build multi-agent AI systems, detailing the use of 'subagents' for context isolation and 'skills' for progressive disclosure.
tags:
  - multi-agent-systems
  - agentic-architecture
  - deep-agents
  - context-management
  - ai-framework
relations:
  - "kb/AI/2_agents/00_introduction-to-ai-agents.md"
aliases:
  - "Deep Agents Guide"
  - "Multi-Agent Systems with Deep Agents"
semantic_summary: >
  This document explains how to build multi-agent applications using the Deep Agents framework. It introduces two core primitives: 'subagents,' which are isolated agents used to prevent context bloat and enable specialization, and 'skills,' which allow for the progressive disclosure of agent capabilities from SKILL.md files. The guide provides code examples, best practices for designing subagents and skills, and a decision framework for choosing between the two patterns.
synthetic_questions:
  - "How do you build multi-agent systems with Deep Agents?"
  - "What is the difference between subagents and skills in Deep Agents?"
  - "How do subagents help with context bloat in AI agents?"
key_concepts:
  - "Deep Agents"
  - "Subagents"
  - "Skills (AI Agents)"
  - "Multi-Agent Systems"
  - "Context Isolation"
  - "Progressive Disclosure"
---

# Building Multi-Agent Applications with Deep Agents

Breaking down complex tasks across specialized agents is one of the most effective approaches to building capable AI systems. Deep Agents makes this easy with two first-class primitives:

- **subagents:** delegating to isolated agents
- **skills:** progressively disclosing capabilities

In this post, we'll show you how to build multi-agent systems with Deep Agents.

### Using Subagents: Specialized, Isolated Workers

Subagents tackle a fundamental problem in agent engineering: **context bloat**. This is when an agent’s context window becomes close to full as it works on a task.

Models struggle to complete tasks as their context window gets filled. Subagents isolate context from the main agent to help avoid quickly entering this "dumb zone". When your agent makes dozens of web searches or file reads, the context window fills with intermediate results. Subagents isolate work by running with their own context window, so the main agent only gets the final result, not the 20 tool calls that produced it.

Here’s a look at the basic subagents architecture:

![Basic subagents architecture](https://deepagents.com/images/subagents-architecture.png)

#### When to Use Subagents

- **Context Preservation:** A task requiring multiple steps can clutter the main agent's context (ex: codebase exploration).
- **Specialization:** Use domain-specific instructions or tools. Subagents developed by distinct teams can specialize in different verticals.
- **Multi-Model:** Subagents can use different models than the main agent. For example, choosing a smaller model for lower latency.
- **Parallelization:** Subagents can run simultaneously and return their outputs to the main agent. This reduces latency.

#### Creating Subagents

Define subagents as dictionaries and pass them to `create_deep_agent()`:

```python
from deepagents import create_deep_agent

research_subagent = {
    "name": "research-agent",
    "description": "Used to research more in depth questions",
    "system_prompt": "You are a great researcher",
    "tools": [internet_search],
    "model": "openai:gpt-4o",  # Optional: override main agent model
}

agent = create_deep_agent(
    model="claude-sonnet-4-5-20250929",
    subagents=[research_subagent]
)
```

#### The General-Purpose Subagent

Deep Agents include a built-in general-purpose subagent that mirrors your main agent's capabilities. It has the same system prompt, tools, and model. This is perfect for context isolation without specialized behavior.

**Example:** Instead of your main agent making 10 web searches and filling its context, it can delegate to the general-purpose subagent with `task(name="general-purpose", task="Research quantum computing trends")`. The subagent performs all searches internally and returns only a summary.

#### Best Practices for Subagents

- **Write clear descriptions.** Your main agent uses descriptions to decide which subagent to call:
    
    - ✅ **Good:** "Analyzes financial data and generates investment insights with confidence scores"
    - ❌ **Bad:** "Does finance stuff"
- **Keep system prompts detailed.** Include tool usage guidance and output format requirements:
    

```python
research_subagent = {
    "name": "research-agent",
    "description": "Conducts in-depth research using web search and synthesizes findings",
    "system_prompt": """You are a thorough researcher. Your job is to:

    1. Break down the research question into searchable queries
    2. Use internet_search to find relevant information
    3. Synthesize findings into a comprehensive but concise summary
    4. Cite sources when making claims

    Output format:
    - Summary (2-3 paragraphs)
    - Key findings (bullet points)
    - Sources (with URLs)

    Keep your response under 500 words to maintain clean context.""",
    "tools": [internet_search],
}
```

- **Minimize tool sets.** Only give subagents the tools they need:

```python
# ✅ Good: Focused tool set
email_agent = {
    "name": "email-sender",
    # Only email-related
    "tools": [send_email, validate_email],
}

# ❌ Bad: Too many tools
email_agent = {
    "name": "email-sender",
    # Unfocused
    "tools": [send_email, web_search, database_query, file_upload],
}
```

### Using Skills: Progressive Disclosure of Capabilities

Skills provide a different pattern: **progressive disclosure**. Instead of giving your agent dozens of tools upfront, you define specialized capabilities in `SKILL.md` files. Your agent sees skill names and descriptions, then reads the full instructions only when needed.

![Skill disclosure flow](https://deepagents.com/images/skills-flow.png)  
_Skill descriptions are pre-loaded into the context window. The skill body is only loaded when the agent decides the skill is needed based on the description and previous context._

#### Setting Up Skills

Skills use the `agentskills.io` spec. Here's the structure:

```
.deepagents/skills/
├── deploy/SKILL.md
└── review-pr/SKILL.md
```

Each `SKILL.md` file has YAML frontmatter with metadata and a main body:

```markdown
---
name: deploy
description: Deploy to production
version: 1.0.0  # Optional
tags: [deployment, production]  # Optional
---

# Deploy to Production

When the user asks to deploy, follow these steps:

1. Run tests: `npm test`
2. Build the application: `npm run build`
3. Deploy to production: `npm run deploy:prod`
4. Verify deployment: Check the health endpoint

Always confirm with the user before deploying to production.
```

#### Adding Skills to Your Agent

Use the `skills` argument to `create_deep_agent` to load skills from the filesystem:

```python
from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend

agent = create_deep_agent(
    model="claude-sonnet-4-5-20250929",
    backend=FilesystemBackend(root_dir="/"),
    skills=[".deepagents/skills"],
)
```

### Choosing the Right Pattern

Here’s a quick set of questions to guide you:

|When you need to...|Use...|Both?|
|:--|:--|:--|
|Delegate complex, multi-step work|Subagents for context isolation||
|Reuse procedures or instructions|Skills for progressive disclosure||
|Provide specialized tools for specific tasks|Subagents with focused tool sets|✅|
|Share capabilities across multiple agents|Skills (they’re just files)|✅|
|Work with large tool sets|Skills to avoid token bloat||

Many systems use both. Skills define procedures; subagents execute complex multi-step work. Your subagents can use skills to effectively manage their context windows.

### Next Steps

The key insight: multi-agent patterns don't have to be complicated. With the right abstractions, they become simple building blocks you can compose into capable, sophisticated systems. Start with subagents for context management, add skills for progressive disclosure, and build from there.

---
## Managing Long-Running Tasks: Context Compression

A core challenge in complex agentic tasks is managing the model's finite context window. Deep Agents includes a sophisticated, built-in system for **context compression** to prevent context rot and ensure the agent can run for extended periods. This system uses a combination of filesystem offloading and summarization.

For a detailed technical breakdown of these mechanisms and how to evaluate them, see the full guide:
-   **[[kb/AI/2_agents/21_context-management-for-deep-agents|Context Management for Deep Agents: A Technical Guide]]**

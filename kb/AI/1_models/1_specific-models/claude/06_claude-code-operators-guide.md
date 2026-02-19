---
title: "Claude Code Operator’s Guide"
id: "KB/AI/Claude/Ops-Guide"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-02-16"
status: "Active"
doc_type: "Reference"
summary: "A comprehensive guide to configuring and using Claude Code for agentic software development, covering project memory (CLAUDE.md), multi-agent patterns, and TDD workflows."
tags:
  - "claude-code"
  - "ai-agents"
  - "dev-workflow"
  - "anthropic"
  - "tdd"
relations:
  - "kb/AI/1_models/1_specific-models/claude/02_oh-my-claude-code"
  - "SIE/04_Engine/LOOP/The Agent Loop"
aliases:
  - "Claude Code Guide"
  - "CLAUDE.md Guide"
target_audience: "Engineering"
security_level: "Internal"
owner_team: "Engineering"
semantic_summary: "This guide outlines the operational best practices for Claude Code, Anthropic's agentic CLI. It details how to establish 'Project Memory' via CLAUDE.md, configure safety permissions, implement a 'Plan-First' architecture, and utilize specialized sub-agents (Planner, Implementer, Reviewer) for robust software development."
synthetic_questions:
  - "How do I set up CLAUDE.md for a project?"
  - "What are the best practices for using Claude Code?"
  - "How do I configure permissions for Claude Code?"
  - "How can I use multi-agent workflows with Claude Code?"
key_concepts:
  - "Project Memory"
  - "CLAUDE.md"
  - "Agentic Workflow"
  - "Plan-First Development"
  - "Quality Gates"
primary_keyword: "Claude Code workflow"
seo_title: "Claude Code Operator’s Guide: Agentic Workflows & Best Practices"
meta_description: "Master Claude Code with this operator's guide. Learn to configure CLAUDE.md, manage permissions, and deploy multi-agent workflows for AI-assisted development."
excerpt: "A complete operator's guide for Claude Code, covering project memory setup, permission management, and multi-agent orchestration patterns."
cover_image: ""
---

# The Complete Claude Code Operator’s Guide

The future of software development isn’t about replacing developers with AI — it’s about amplifying human creativity and judgment with intelligent automation. **Claude Code**, Anthropic’s agentic command-line tool, represents a significant leap forward in this vision, enabling developers to delegate complex coding tasks directly from their terminal while maintaining control and quality.

This guide distills effective patterns into a comprehensive operator’s manual. Whether you’re a solo developer or leading an engineering team, these practices will help you harness Claude Code’s full potential while avoiding common pitfalls.

## Why This Matters Now

Traditional development workflows are hitting friction points: context switching between tools, repetitive boilerplate generation, manual test writing, and the cognitive overhead of maintaining large codebases. Claude Code addresses these pain points by acting as an intelligent pair programmer that can understand your entire project context, follow your coding standards, and execute complex multi-file changes safely.

**Crucial Insight:** The tool is only as good as how you use it. The difference between frustrating AI experiences and transformative ones lies in the systematic approach to prompting, project setup, and workflow design.

## The Foundation: Architecture-First Development

### 1. Project Memory That Actually Works

The first step is giving Claude stable “project memory” through a well-structured `CLAUDE.md` file. Think of this as your project's AI constitution — it defines standards, constraints, and navigation aids that persist across sessions.

**Initialization:**
```bash
npm install -g @anthropic-ai/claude-code  
cd your-project  
claude  
> /init
```

**Structure your `CLAUDE.md` like this:**

```markdown
# Project Overview  
- One-liner: "TypeScript API for real-time collaboration"  
- Architecture: Event-driven with Redis pub/sub  
- Domain: Users, Documents, Permissions

# How to Run  
- Build: npm run build  
- Test: npm run test  
- Typecheck: npm run typecheck

# Coding Standards  
- TypeScript strict mode, no `any` types  
- API errors use Result<T, E> pattern  
- All functions must have unit tests

# Docs Map  
- /docs/architecture/system-design.md  
- /docs/specs/api-v1-spec.md  
- /docs/plans/current-sprint-plan.md

# Anti-patterns (DO NOT)  
- No nested ternaries beyond 2 levels  
- No copy-paste of type definitions  
- No direct database queries in controllers
```

> **Pro tip**: Use memory imports to modularize large projects. Reference external files with `@docs/...` syntax to keep your main memory file focused.

### 2. Smart Permissions and Safety Rails

One of Claude Code’s strengths is its permission system, but the default settings can create approval fatigue. Configure `.claude/settings.json` to reduce friction while maintaining safety:

```json
{  
  "permissions": {  
    "allow": [  
      "Bash(npm run test:*)",  
      "Bash(git diff:*)",  
      "Read(~/.zshrc)"  
    ],  
    "deny": ["Bash(curl:*)"]  
  },  
  "defaultMode": "acceptEdits",  
  "model": "claude-sonnet-4-20250514"  
}
```

For prototyping, use auto-accept mode with clean git checkpoints for quick rollbacks. For production code, maintain synchronous supervision with stepwise execution.

## The Planning Revolution

### Plan-First, Then Build

The most transformative practice is adopting a plan-first approach. Every significant feature starts with a written plan that both you and Claude can follow. This prevents scope creep and creates clear checkpoints for quality control.

**Standardized Planning Template:**

```markdown
# Feature: User Authentication — Plan

## Goal  
Implement JWT-based auth with refresh tokens

## Non-Functional Requirements  
- 15min access tokens, 7-day refresh  
- Redis for token storage  
- Rate limiting: 5 requests/minute per IP

## Impacted Areas  
- /src/auth/ (new module)  
- /src/middleware/auth.ts  
- /tests/auth/

## Steps  
- [ ] S1: Create types and interfaces  
- [ ] S2: Implement JWT service  
- [ ] S3: Add auth middleware  
- [ ] S4: Write integration tests

## Risks & Rollback  
- Risk: Token storage race conditions  
- Rollback: Revert to stateless JWT if Redis fails

## Done Definition  
- All tests passing  
- Security review complete  
- Documentation updated
```

**Execution Workflow:**

```text
> read @docs/plans/auth-feature.md  
> critique this plan; propose safer, smaller steps  
> execute S1 only; show diff; run tests  
> if tests pass, proceed to S2
```

## The Multi-Agent Advantage

### Specialized AI Agents for Different Roles

One of Claude Code’s most powerful features is sub-agents — specialized AI assistants with focused roles and separate context windows. This prevents the “jack of all trades, master of none” problem.

Create four core agents in `.claude/agents/`:

**1. Planner Agent (`planner.md`)**

```markdown
---  
name: planner  
description: Architecture-first planner. Produces minimal, verifiable steps.  
tools: Read  
---  
You create: scope definition, constraints, file impact analysis,   
stepwise implementation plan, risk assessment, and test strategy.  
Never proceed to implementation — planning only.
```

**2. Implementer Agent (`implementer.md`)**

```markdown
---  
name: implementer  
description: Executes approved plans with small commits and continuous testing.  
tools: Read, Edit, Write, Bash  
---  
Follow plan checkboxes strictly. After each step: run tests,   
summarize changes, note any blockers. No architectural decisions.
```

**3. Reviewer Agent (`reviewer.md`)**

```markdown
---  
name: reviewer  
description: Security and quality review after implementation steps.  
tools: Read, Grep, Bash  
---  
Security checklist: injection attacks, secrets exposure,   
authentication/authorization, error handling, performance, test coverage.  
Provide concrete fix suggestions only.
```

**4. Researcher Agent (`researcher.md`)**

```markdown
---  
name: researcher  
description: Low-context research for library comparisons and trade-offs.  
tools: Read  
---  
Research libraries, patterns, and best practices. Return concise   
findings with recommendations and trade-off analysis. Cite sources.
```

**Usage Strategy:**

```text
> use the planner agent to design the auth system  
> use the implementer agent to execute step 1 of the plan  
> use the reviewer agent to check for security issues
```

## Test-Driven Development on Steroids

### Making AI Verify Its Own Work

Claude Code excels at test-first development because it can write tests, run them, analyze failures, fix code, and iterate until green — all in a single session.

**The Loop:**

```text
> find functions in AuthService.ts not covered by tests  
> add comprehensive tests for AuthService including edge cases  
> run the new tests and fix any failures  
> add integration tests for the auth endpoints  
> run all tests and ensure 100% pass rate
```

### Quality Gates as Code

Encode your quality standards as reusable slash commands:

**`.claude/commands/quality-gate.md`**

```markdown
---  
description: Run tests, check coverage, fix failures until green  
allowed-tools: Bash(npm run test:*)  
---  
Run all tests and fix failures. Ensure >90% coverage.   
Keep diffs minimal and explain root causes of failures.
```

**Usage:**

```text
> /quality-gate
```

## Advanced Patterns That Scale

### 1. Slash Commands for Team Workflows

Transform repetitive prompts into reusable commands that capture institutional knowledge.

**`.claude/commands/deploy-checklist.md`**

```markdown
Review code for:  
- Environment variable usage  
- Database migration safety  
- Breaking API changes  
- Performance impact  
Then generate deployment notes.
```

### 2. Model Context Protocol (MCP) Integration

For teams with complex toolchains, MCP servers can expose external systems safely:

```json
{  
  "enabledMcpjsonServers": ["github", "filesystem", "postgres"],  
  "mcpSettings": {  
    "github": {  
      "permissions": ["read_repos", "create_prs"]  
    }  
  }  
}
```

### 3. Parallel Work with Git Worktrees

For complex features requiring long-running AI sessions:

```bash
git worktree add ../feature-auth feature/auth  
cd ../feature-auth  
claude --resume auth-session-id
```

## Daily Workflow Patterns

### The Four-Phase Development Loop

1. **Explore & Plan:** Analyze architecture, identify files, propose plan, write to `@docs/plans/`.
2. **Execute Small Steps:** Read plan, execute Step 1, show diff, run tests. **Do NOT proceed until approved.**
3. **Review & Integrate:** Use Reviewer agent, run full suite, create PR.
4. **Resume & Iterate:** `claude --continue` to pick up context.

## Quality Control That Actually Works

The key to successful AI-assisted development is maintaining human judgment while leveraging AI execution speed:

1. **Checkpoint-driven development**: Keep changes small and git history clean.
2. **Automated verification**: Let AI run tests and fix issues, but review architectural decisions.
3. **Review gates**: Use sub-agents for security and quality checks after each major change.
4. **Rollback readiness**: Maintain clean git state for quick reverts.

## Getting Started

1. **Install:** `npm install -g @anthropic-ai/claude-code`
2. **Set up Memory:** Create `CLAUDE.md` with standards.
3. **Configure:** Balance safety/speed in `.claude/settings.json`.
4. **Plan:** Write one feature plan and execute it step-by-step.
5. **Specialize:** Create a reviewer agent for quality control.
---
title: "Deep Research Solution with Microsoft Agent Framework"
id: "KB/AI/Methods/MAF-Deep-Research"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-02-16"
status: "Active"
doc_type: "Reference"
summary: "A technical guide for building a local, privacy-first Deep Research agent workflow using Microsoft Foundry Local and the Agent Framework (MAF)."
tags:
  - "ai-agents"
  - "microsoft-foundry"
  - "deep-research"
  - "local-llm"
  - "red-teaming"
  - "workflow-orchestration"
relations:
  - "kb/AI/1_models/2_concepts-and-techniques/00_how-to-build-a-deep-research-system"
  - "kb/AI/3_methods/mcp/08_using-mcp-servers-with-local-llms"
  - "kb/AI/2_agents/13_reference-architecture-for-trustworthy-agentic-ai"
aliases:
  - "MAF Deep Research Guide"
  - "Microsoft Agent Framework Tutorial"
target_audience: "Manager"
security_level: "Internal"
owner_team: "Engineering"
semantic_summary: "This guide details the implementation of a Deep Research agent using Microsoft Foundry Local and Agent Framework. It covers the 'research-judge-research' loop, Red Team safety evaluation, DevUI debugging, and performance optimization with .NET Aspire."
synthetic_questions:
  - "How do I build a local deep research agent with Microsoft tools?"
  - "How does Microsoft Agent Framework handle Red Teaming?"
  - "What is the workflow for a deep research agent?"
key_concepts:
  - "Microsoft Foundry Local"
  - "Agent Framework"
  - "Deep Research Loop"
  - "Red Teaming"
  - "DevUI"
primary_keyword: "Microsoft Agent Framework Deep Research"
seo_title: "Building a Deep Research Agent with Microsoft Foundry Local"
meta_description: "Learn to build a privacy-first Deep Research agent using Microsoft Foundry Local and Agent Framework, featuring Red Teaming and workflow orchestration."
excerpt: "A complete guide to building local Deep Research agents using Microsoft's Agent Framework, covering security evaluation, workflow design, and performance optimization."
cover_image: ""
---

# From Local Models to Agent Workflows: Building a Deep Research Solution with Microsoft Agent Framework

## Introduction: A New Paradigm for AI Application Development

In enterprise AI application development, we often face this dilemma: while cloud-based large language models are powerful, issues such as data privacy, network latency, and cost control make many scenarios difficult to implement. Traditional local small models, although lightweight, lack complete development, evaluation, and orchestration frameworks.

The combination of **Microsoft Foundry Local** and **Agent Framework (MAF)** provides an elegant solution to this dilemma. This article guides you from zero to one in building a complete Deep Research agent workflow, covering the entire pipeline from model safety evaluation and workflow orchestration to interactive debugging and performance optimization.

## Why Choose Foundry Local?

Foundry Local is not just a local model runtime, but an extension of Microsoft’s AI ecosystem to the edge:

- **Privacy First**: All data and inference processes are completed locally, meeting strict compliance requirements.
- **Zero Latency**: No network round trips required, suitable for real-time interactive scenarios.
- **Cost Control**: Avoid cloud API call fees, suitable for high-frequency calling scenarios.
- **Rapid Iteration**: Local development and debugging, shortening feedback cycles.

Combined with the Microsoft Agent Framework, you can build complex agent applications just like using Azure OpenAI.

### Example Code

```python
agent = FoundryLocalClient(model_id="qwen2.5-1.5b-instruct-generic-cpu:4").as_agent(
    name="LocalAgent",
    instructions="""You are an assistant.

Your responsibilities:
- Answering questions and providing professional advice
- Helping users understand concepts
- Offering users different suggestions
""",
)
```

## How to Evaluate an Agent?

Based on the Agent Framework evaluation samples, here are three complementary evaluation methods:

1. **Red Teaming (Security and Robustness)**
    - **Purpose:** Use systematic adversarial prompts to cover high-risk content and test the agent’s security boundaries.
    - **Method:** Execute multiple attack strategies against the target agent, covering risk categories such as violence, hate/unfairness, sexual content, and self-harm.
2. **Self-Reflection (Quality Verification)**
    - **Purpose:** Let the agent perform secondary review of its own output, checking factual consistency, coverage, citation completeness, and answer structure.
    - **Method:** Add a “reflection round” after task output, where the agent provides self-assessment and improvement suggestions based on fixed dimensions, producing a revised version.
3. **Observability (Performance Metrics)**
    - **Purpose:** Measure end-to-end latency, stage-wise time consumption, and tool invocation overhead using metrics and distributed tracing.
    - **Method:** Enable OpenTelemetry to report workflow execution processes and tool invocations.

## Complete Development Process: From Security to Production

### Step 1: Red Team Evaluation – Securing the Safety Baseline

Before putting any model into production, security evaluation is an essential step. MAF provides out-of-the-box Red Teaming capabilities, combined with Microsoft Foundry to complete Red Team evaluation:

```python
# 01.foundrylocal_maf_evaluation.py
from azure.ai.evaluation.red_team import AttackStrategy, RedTeam, RiskCategory
from azure.identity import AzureCliCredential
from agent_framework_foundry_local import FoundryLocalClient

credential = AzureCliCredential()
agent = FoundryLocalClient(model_id="qwen2.5-1.5b-instruct-generic-cpu:4").as_agent(
    name="LocalAgent",
    instructions="""You are an assistant...""",
)

def agent_callback(query: str) -> str:
    async def _run():
        return await agent.run(query)
    response = asyncio.get_event_loop().run_until_complete(_run())
    return response.text

red_team = RedTeam(
    azure_ai_project=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=credential,
    risk_categories=[
        RiskCategory.Violence,
        RiskCategory.HateUnfairness,
        RiskCategory.Sexual,
        RiskCategory.SelfHarm,
    ],
    num_objectives=2,
)

results = await red_team.scan(
    target=agent_callback,
    scan_name="Qwen2.5-1.5B-Agent",
    attack_strategies=[
        AttackStrategy.EASY,
        AttackStrategy.MODERATE,
        AttackStrategy.CharacterSpace,
        AttackStrategy.ROT13,
        # ... other strategies
    ],
    output_path="Qwen2.5-1.5B-Redteam-Results.json",
)
```

**Evaluation Dimensions**:

- **Risk Categories**: Violence, hate/unfairness, sexual content, self-harm
- **Attack Strategies**: Encoding obfuscation, character substitution, prompt injection, etc.
- **Output Analysis**: Generate detailed risk scorecards and response samples

### Step 2: Deep Research Workflow Design – Multi-Round Iterative Intelligence

The core of Deep Research is the “research-judge-research again” iterative loop. MAF Workflows makes this complex logic clear and maintainable.

**Key Components**:

1. **Research Agent**
    - Equipped with `search_web` tool for real-time external information retrieval.
    - Generates summaries and identifies knowledge gaps in each round.
    - Accumulates context to avoid redundant searches.
2. **Iteration Controller**
    - Evaluates current information completeness.
    - Decision-making: Continue deeper vs Generate report.
    - Prevents infinite loops (sets maximum rounds).
3. **Final Reporter**
    - Integrates findings from all iterations.
    - Generates structured reports with citations.

**Code Implementation** (simplified):

```python
from agent_framework import WorkflowBuilder
from agent_framework_foundry_local import FoundryLocalClient

workflow_builder = WorkflowBuilder(
    name="Deep Research Workflow",
    description="Multi-agent deep research workflow with iterative web search"
)

workflow_builder.register_executor(lambda: StartExecutor(state=state), name="start_executor")
workflow_builder.register_executor(lambda: ResearchAgentExecutor(), name="research_executor")
workflow_builder.register_executor(lambda: iteration_control, name="iteration_control")
workflow_builder.register_executor(lambda: FinalReportExecutor(), name="final_report")
workflow_builder.register_executor(lambda: OutputExecutor(), name="output_executor")

# ... Register agents and add edges ...

workflow_builder.add_edge(
    "iteration_control",
    "research_executor",
    condition=lambda decision: decision.signal == ResearchSignal.CONTINUE,
)
workflow_builder.add_edge(
    "iteration_control",
    "final_report",
    condition=lambda decision: decision.signal == ResearchSignal.COMPLETE,
)
```

### Step 3: DevUI Interactive Debugging – Making Workflows Visible

Traditional agent debugging is often a “black box” experience. MAF DevUI visualizes the entire execution process:

```bash
python 02.foundrylocal_maf_workflow_deep_research_devui.py
# DevUI starts at http://localhost:8093
```

**DevUI Provides**:

- **Workflow Topology Diagram**: Intuitively see node and edge relationships.
- **Step-by-Step Execution**: View input, output, and status of each node.
- **Real-time Injection**: Dynamically modify input parameters to test different scenarios.
- **Log Aggregation**: Unified view of all agent logs and tool invocations.

### Step 4: Performance Evaluation and Optimization – .NET Aspire Integration

In production environments, performance is a dimension that cannot be ignored. MAF’s integration with .NET Aspire provides enterprise-grade observability.

**Enable Telemetry**:

```bash
# Configure OpenTelemetry
export OTLP_ENDPOINT="http://localhost:4317"
```

**Key Metrics**:

- **End-to-End Latency**: Time from user input to final report.
- **Model Inference Time**: Response speed of local model.
- **Tool Invocation Overhead**: Impact of external APIs (such as search).
- **Memory Usage**: Context accumulation across multiple iterations.

## Conclusion: The Infinite Possibilities of Localized AI

The combination of Microsoft Foundry Local + Agent Framework proves that local small models can also build production-grade intelligent applications. Through this Deep Research case, we see:

- **Security and Control**: Red Team evaluation ensures model behavior meets expectations.
- **Efficient Orchestration**: Workflows make complex logic clear and maintainable.
- **Rapid Iteration**: DevUI provides instant feedback, shortening development cycles.
- **Performance Transparency**: Aspire integration makes optimization evidence-based.

---

**Related Resources**:

- [How to Build a Deep Research System (Concept)](app://obsidian.md/kb/AI/1_models/2_concepts-and-techniques/00_how-to-build-a-deep-research-system)
- [Using MCP Servers with Local LLMs](app://obsidian.md/kb/AI/3_methods/mcp/08_using-mcp-servers-with-local-llms)
---
title: "The Agent Loop: Autonomous Intelligence Layer"
id: SIE/KPL-02
version: "1.0"
steward: Adam Bernard
updated: 2025-12-14
status: "Planned"
doc_type: "technical_architecture"
summary: "Defines the Agent Loop system that extends the proven Knowledge Pipeline with autonomous intelligence, enabling the SIE to perform continuous monitoring, research, and content optimization while maintaining human oversight and governance compliance."
tags: 
  - agent-loop
  - automation
  - ai-agents
  - crewai
  - phase-2
  - kpl-extension
  - autonomous-intelligence
relations:
  - "SIE/E-00"
  - "SIE/E-01"
  - "SIE/04_KPL/index"
  - "SIE/04_KPL/SIE KPL - Setup from Scratch"
dependencies:
  - "Knowledge Pipeline (KPL) v1.0 operational"
  - "Pinecone vector store with embeddings"
  - "WordPress REST API access"
  - "Schema validation system active"
aliases:
  - Agent Loop
  - Autonomous Intelligence Layer
  - SIE Phase 2
  - Agent Orchestration System
---

# 🤖 The Agent Loop: Autonomous Intelligence Layer

## Executive Summary

The **Agent Loop** represents Phase 2 of the Strategic Intelligence Engine, transforming the proven **Knowledge Pipeline** from a one-way publishing system into an autonomous intelligence layer capable of continuous learning, monitoring, and content optimization.

**What Changes:**
- From **Manual → Automated** content enrichment
- From **Reactive → Proactive** knowledge maintenance  
- From **Static → Dynamic** semantic relationships
- From **Human-driven → AI-assisted** strategic insights

**What Stays:**
- ✅ Human oversight and approval (Rule G-04)
- ✅ Knowledge Core as source of truth (Rule G-01)
- ✅ Complete audit logging (Rule G-03)
- ✅ Schema validation (Rule I-02)

---

## 1. Strategic Context

### Building on Proven Foundation

The **Knowledge Pipeline (KPL)** successfully validates the SIE's core architecture:

**KPL v1.0 Capabilities (Proven):**
- ✅ Structured knowledge ingestion (Obsidian → GitHub → WordPress)
- ✅ Vector embeddings for semantic search (Pinecone)
- ✅ Automated publishing with audit trails
- ✅ Schema-driven content architecture
- ✅ Cross-platform synchronization

**Agent Loop Additions (Planned):**
- 🎯 Autonomous monitoring and research
- 🎯 Proactive content enrichment and updates
- 🎯 Strategic insight generation from vector analysis
- 🎯 Continuous knowledge quality improvement
- 🎯 Semantic relationship discovery and linking

### Alignment with Core Functions

This implements two key functions defined in [[SIE/01_Core/00_core-purpose|the SIE Core Purpose]]:

**Function 3: Automate & Execute**
> Use the intelligence within the Knowledge Core to perform specific, high-value tasks.

The Agent Loop automates content research, enrichment, maintenance, and semantic linking—tasks that currently require manual execution.

**Function 4: Analyze & Synthesize**
> Learn from new and updated information... identify patterns, gaps, and opportunities... generate strategic insights.

Agents continuously analyze the vector space, detect knowledge gaps, monitor for outdated information, and surface strategic recommendations.

---

## 2. System Architecture

### The Complete Stack

```
┌─────────────────────────────────────────────────────────────┐
│              PROVEN FOUNDATION (KPL v1.0)                   │
│                                                             │
│    Obsidian → GitHub → WordPress → AI Engine → Pinecone    │
│                                                             │
│    ✓ Manual content authoring                              │
│    ✓ Automated publishing pipeline                         │
│    ✓ Vector embeddings generated                           │
│    ✓ Change logs maintained                                │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────┐
│           AGENT LOOP MIDDLEWARE (Phase 2)                   │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │         Agent Orchestrator (CrewAI Framework)         │ │
│  │                                                       │ │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐    │ │
│  │  │ Research   │  │  Analyst   │  │  Editor    │    │ │
│  │  │  Agent     │  │   Agent    │  │   Agent    │    │ │
│  │  └─────┬──────┘  └─────┬──────┘  └─────┬──────┘    │ │
│  │        │                │                │          │ │
│  │        │    Shared Agent Memory (Redis)  │          │ │
│  │        │                │                │          │ │
│  └────────┼────────────────┼────────────────┼──────────┘ │
│           │                │                │            │
│      ┌────▼─────┐    ┌─────▼────┐    ┌─────▼─────┐     │
│      │ Pinecone │    │   Web    │    │ WordPress │     │
│      │  Query   │    │  Search  │    │ REST API  │     │
│      │   Tool   │    │   Tool   │    │   Tool    │     │
│      └──────────┘    └──────────┘    └───────────┘     │
│                                                         │
│  Governance Layer:                                      │
│  • Schema Validation  • Logging  • Human Approval      │
└─────────────────────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                  TRIGGER SOURCES                            │
│                                                             │
│  • WordPress Webhooks (on_save_post, on_publish)           │
│  • Scheduled Cron Jobs (content monitoring, gap analysis)  │
│  • Manual API Calls (on-demand enrichment)                 │
│  • GitHub Actions (post-KPL sync)                          │
└─────────────────────────────────────────────────────────────┘
```

### Workflow Transformation

**Before Agent Loop (KPL v1.0):**
```
Human writes → Git commit → GitHub Action → WordPress → Done
```

**After Agent Loop (KPL v2.0):**
```
Human writes → Git commit → GitHub Action → WordPress
                                               ↓
                                         Webhook triggers
                                               ↓
                                         Agent analyzes
                                               ↓
                                    Enrichment suggestions
                                               ↓
                                    Human reviews/approves
                                               ↓
                                    WP updated (if approved)
```

---

## 3. Governance & Safety Framework

All Agent Loop operations comply with established SIE governance rules:

### Rule G-01: Knowledge Core Precedence
**Implementation:**
- Agents **query** Pinecone as the authoritative source of truth
- External research supplements existing knowledge, never contradicts
- Conflicts between internal knowledge and external sources are **flagged for human review**
- Decision logic: `if confidence(pinecone) > confidence(web) → use_pinecone; else → flag_for_review`

### Rule G-03: Mandatory Logging
**Implementation:**
- All agent actions logged to `SIE/09_Logs/agent-actions.md`
- Log format: `[ISO_timestamp] [agent_role] [action] [confidence_score] [reasoning] [outcome]`
- Integrated with existing KPL change logs
- Separate error log: `SIE/09_Logs/agent-errors.md`

**Example Log Entry:**
```
2025-12-14T14:30:22Z | Research_Agent | web_search | confidence:0.87 | 
Searched "semantic depth SEO 2025" → Found 3 newer sources | 
Flagged for Analyst review
```

### Rule G-04: Human-in-the-Loop
**Implementation:**
- **Draft Mode Only:** Agents write to `post_status: draft` (never `publish`)
- **Review Queue:** Human approval required before any publication
- **Confidence Threshold:** Outputs below 0.75 confidence automatically flagged
- **Approval Metadata:** All agent suggestions include:
  - `agent_reasoning: [explanation]`
  - `confidence_score: [0.0-1.0]`
  - `sources_used: [list]`
  - `human_review_required: [true/false]`

### Rule I-02: Schema Adherence
**Implementation:**
- Agent-generated content validated against schema **before** WordPress sync
- Required metadata completeness check (title, excerpt, tags, primary_keyword)
- Invalid outputs quarantined to `SIE/09_Logs/schema-violations/`
- Human notified via webhook to Discord/email

---

## 4. Agent Definitions

### Agent A: The Research Agent
**Role:** External intelligence gatherer  
**Personality:** Curious, thorough, fact-focused  
**Capabilities:**
- Web search via Tavily API (optimized for LLM consumption)
- Content scraping via Firecrawl (clean extraction)
- RSS feed monitoring for industry updates
- Competitive content analysis

**Primary Tools:**
- `web_search(query: str, recency: str) → SearchResults`
- `scrape_url(url: str) → CleanContent`
- `check_source_credibility(domain: str) → CredibilityScore`

**Example Task:**
> "Research the latest developments in 'semantic depth' from authoritative SEO sources published in the last 6 months. Return top 5 findings with citations."

---

### Agent B: The Analyst Agent
**Role:** Knowledge synthesis and gap detection  
**Personality:** Strategic, pattern-recognition focused  
**Capabilities:**
- Vector similarity queries (Pinecone)
- Knowledge gap identification
- Content freshness scoring
- Semantic relationship mapping
- Trend analysis across knowledge base

**Primary Tools:**
- `query_knowledge_core(query: str, top_k: int) → SimilarDocs`
- `detect_knowledge_gaps(topic: str) → GapAnalysis`
- `calculate_content_freshness(post_id: int) → FreshnessScore`
- `find_semantic_links(post_id: int, threshold: float) → LinkSuggestions`

**Example Task:**
> "Analyze our Knowledge Core for articles related to 'content clustering.' Identify gaps where we lack coverage compared to top-ranking competitors."

---

### Agent C: The Editor Agent
**Role:** Content generation and WordPress integration  
**Personality:** Precise, detail-oriented, schema-aware  
**Capabilities:**
- Markdown content generation
- Schema validation
- WordPress REST API integration
- Internal linking insertion
- Metadata enrichment

**Primary Tools:**
- `generate_content(outline: str, style: str) → Markdown`
- `validate_schema(content: dict) → ValidationResult`
- `update_wordpress_post(post_id: int, content: dict, status: str) → WPResponse`
- `insert_internal_links(content: str, suggestions: list) → UpdatedContent`

**Example Task:**
> "Take this bullet-point outline and expand it into a 1200-word article following our schema. Include 3-5 internal links to related KB articles. Save as Draft with all required metadata."

---

## 5. Implementation Roadmap

### Phase 2A: Single-Agent Foundation (Month 1)
**Goal:** Prove agent → WordPress integration with one use case

**Deliverables:**
- [ ] Python middleware server (FastAPI + CrewAI)
- [ ] Webhook endpoint receiving WordPress events
- [ ] Single "Draft Enrichment" agent operational
- [ ] Pinecone query tool working
- [ ] Draft-only output (no auto-publish)
- [ ] Basic logging to `09_Logs/agent-actions.md`
- [ ] Schema validation integrated

**Success Metric:** Agent enriches 1 draft post per day with 80% human approval rate

**Infrastructure:**
- DigitalOcean Droplet ($12/month)
- Redis container (state management)
- FastAPI server (webhook listener)
- CrewAI + OpenAI GPT-4

---

### Phase 2B: Multi-Agent Orchestration (Months 2-3)
**Goal:** Three-agent crew handling end-to-end workflows

**Deliverables:**
- [ ] Research Agent (web search + scraping)
- [ ] Analyst Agent (vector similarity + gap analysis)
- [ ] Editor Agent (content generation + WP sync)
- [ ] Inter-agent communication via CrewAI tasks
- [ ] Confidence scoring system
- [ ] Advanced logging with reasoning chains
- [ ] Human review dashboard (simple Flask app)

**Success Metric:** Agent crew produces 3 publication-ready drafts per week

**New Tools Integrated:**
- Tavily API (web search)
- Firecrawl (content scraping)
- Enhanced Pinecone queries

---

### Phase 2C: Autonomous Monitoring (Months 4-6)
**Goal:** Self-directed, scheduled knowledge maintenance

**Deliverables:**
- [ ] Scheduled cron jobs (daily, weekly, monthly)
- [ ] "Content Watchdog" detecting stale articles
- [ ] Automated update suggestions
- [ ] Vector-based semantic linking engine
- [ ] Monthly "intelligence reports" on knowledge gaps
- [ ] Full integration with KPL change logs
- [ ] Performance analytics dashboard

**Success Metric:** System autonomously maintains 50+ KB articles with <5% false positive rate

**Monitoring Capabilities:**
- Content freshness scoring
- Broken link detection
- Competitive content tracking
- Trending topic identification

---

## 6. Technical Stack

### Core Infrastructure

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Agent Framework** | CrewAI | Role-based agent orchestration |
| **LLM Provider** | OpenAI GPT-4 | Primary reasoning engine |
| **Middleware** | Python 3.11 + FastAPI | Webhook listener and agent server |
| **State Management** | Redis | Agent memory and caching |
| **Deployment** | Docker on DigitalOcean | Containerized, scalable infrastructure |
| **Monitoring** | Langfuse | LLM observability and tracing |

### Required Integrations

| Tool | Purpose | Cost Estimate |
|------|---------|---------------|
| Pinecone | Knowledge Core vector queries | $0 (existing) |
| Tavily API | LLM-optimized web search | $50-100/mo |
| Firecrawl | Clean content extraction | $30-50/mo |
| WordPress REST API | Content CRUD operations | $0 (existing) |
| OpenAI API | GPT-4 inference | $200-400/mo |
| DigitalOcean | Server hosting | $12-24/mo |
| Redis Cloud | Agent state storage | $0-20/mo |

**Total Estimated Monthly Cost:** $292-594

**Break-even Analysis:**
- Assuming 15 hours/month saved on content work
- At $100/hr consultant rate = $1,500/month value
- **ROI: 250-515%**

---

## 7. Priority Use Cases

### Use Case 1: "Knowledge Enrichment Agent"
**Business Value:** Reduce content creation time by 60%

**Trigger:** User saves draft with bullet points in Obsidian  
**Workflow:**
1. **Research Agent:** Queries Pinecone for related existing content (vector similarity)
2. **Research Agent:** Searches web for recent data/statistics on topic
3. **Analyst Agent:** Identifies coverage gaps and opportunities
4. **Analyst Agent:** Finds 5-7 related articles for internal linking
5. **Editor Agent:** Expands bullets into full sections (1000-1500 words)
6. **Editor Agent:** Inserts internal links with contextual anchor text
7. **Editor Agent:** Validates schema and saves to WordPress as Draft

**Output Metadata:**
```yaml
agent_confidence: 0.87
human_review_required: true
agent_reasoning: "Expanded 6 bullet points into 1200 words. Added 4 internal links to related KB articles. Found 3 recent statistics from authoritative sources."
sources_used:
  - https://moz.com/blog/semantic-seo-2024
  - https://backlinko.com/hub/seo/topical-authority
  - internal://kb/semantic-depth-in-seo
review_focus: "Verify statistics accuracy and internal link relevance"
```

**Human Review Process:**
1. Notification sent via Discord webhook
2. Human reviews draft in WordPress
3. Approves/edits/rejects
4. If approved → publishes and logs to change log
5. If rejected → agent learns from feedback for next iteration

---

### Use Case 2: "Content Watchdog"
**Business Value:** Maintain knowledge currency without manual audits

**Trigger:** Scheduled cron job every Monday at 6:00 AM  
**Workflow:**
1. **Monitor Agent:** Queries WordPress for articles >6 months old
2. **Monitor Agent:** Selects 5 oldest published KB articles
3. **Research Agent:** Checks for newer information on each topic
4. **Analyst Agent:** Runs vector similarity to find related internal updates
5. **Analyst Agent:** Calculates "freshness score" (0-100)

**Decision Tree:**
- Score >80 → Log "Content Fresh" to `agent-actions.md`
- Score 50-80 → Create "Suggested Updates" draft
- Score <50 → Flag as "Urgent Update Required" with reasoning

**Example Output (Low Freshness):**
```yaml
article: "Introduction to Content Clustering"
post_id: 1234
freshness_score: 42
issues_detected:
  - "Last updated 18 months ago"
  - "Missing coverage of 'topical authority' (trending topic)"
  - "Competitor content now includes case studies (we don't)"
  - "Internal link to outdated 'keyword research' article"
suggested_updates:
  - "Add section on topical authority and E-E-A-T"
  - "Include 2024 case study examples"
  - "Update internal link to new 'semantic keyword research' article"
priority: high
human_review_required: true
```

---

### Use Case 3: "Semantic Linking Engine"
**Business Value:** Automated internal linking improves SEO and knowledge discoverability

**Trigger:** New article published to WordPress via KPL  
**Workflow:**
1. **Webhook:** WordPress sends `post_published` event
2. **Analyst Agent:** Generates embedding for new article content
3. **Analyst Agent:** Queries Pinecone for top 10 semantically similar articles (cosine similarity >0.75)
4. **Editor Agent:** Analyzes context for natural anchor text opportunities
5. **Editor Agent:** Inserts 3-5 contextual internal links in new article
6. **Editor Agent:** Updates related articles with reciprocal links to new content
7. **Editor Agent:** Logs all linking decisions for review

**Validation Rules:**
- Maximum 5 internal links per article
- No self-links
- Anchor text must be contextually relevant (not forced)
- Link placement must feel natural in sentence flow

**Example Linking Decision:**
```
New Article: "Advanced SEO Strategies for 2025"
Related Articles Found:
  1. "Semantic Depth in SEO" (similarity: 0.89)
  2. "Content Clustering Guide" (similarity: 0.84)
  3. "E-E-A-T and Topical Authority" (similarity: 0.78)

Links Inserted:
  - "Understanding semantic depth is crucial for..." → Semantic Depth in SEO
  - "This approach aligns with content clustering principles..." → Content Clustering Guide
  - "Building topical authority through E-E-A-T..." → E-E-A-T Guide

Reciprocal Links Added:
  - Added link from "Semantic Depth in SEO" → "Advanced SEO Strategies"
  - Added link from "Content Clustering Guide" → "Advanced SEO Strategies"

Confidence: 0.91
Human Review: Optional (high confidence)
```

---

## 8. Monitoring & Observability

### Logging Strategy

**Agent Action Log (`SIE/09_Logs/agent-actions.md`):**
```markdown
## 2025-12-14

### 14:30:22 - Research Agent - Web Search
- **Query:** "semantic depth SEO 2025"
- **Confidence:** 0.87
- **Results:** 3 authoritative sources found
- **Reasoning:** User draft mentions semantic depth but lacks recent statistics
- **Outcome:** Flagged for Analyst review

### 14:32:15 - Analyst Agent - Knowledge Gap Analysis
- **Topic:** Semantic depth
- **Internal Coverage:** 2 existing articles (last updated 2024-03)
- **Gap Detected:** Missing coverage of "semantic clustering" and "entity relationships"
- **Recommendation:** Create new dedicated article
- **Confidence:** 0.79
- **Outcome:** Draft outline created for human review
```

**Error Log (`SIE/09_Logs/agent-errors.md`):**
```markdown
## 2025-12-14

### 14:35:10 - Editor Agent - Schema Validation Failed
- **Post ID:** Draft-1234
- **Error:** Missing required field `primary_keyword`
- **Content:** "Advanced SEO Strategies"
- **Action:** Draft quarantined to schema-violations/
- **Human Notified:** Yes (Discord webhook)
- **Resolution:** Pending human intervention
```

### Performance Metrics Dashboard

**Key Metrics to Track:**
- Agent actions per day/week/month
- Human approval rate (%)
- Average confidence score
- Content freshness improvement (before/after)
- Internal links added per article
- Knowledge gap closure rate
- Cost per agent action (LLM API usage)
- Error rate (schema violations, API failures)

**Monitoring Tools:**
- **Langfuse:** LLM observability (prompt tracking, token usage, latency)
- **Simple Flask Dashboard:** Real-time agent activity feed
- **Discord Webhooks:** Instant notifications for high-priority flags
- **Weekly Email Report:** Summary of agent activities and recommendations

---

## 9. Security & Privacy Considerations

### Data Protection
- **PII Handling:** Agents never process personally identifiable information
- **API Keys:** Stored in environment variables, never logged
- **Redis State:** Encrypted at rest
- **WordPress Access:** Limited to draft/publish permissions only
- **Audit Trail:** All actions traceable to specific agent and timestamp

### Rate Limiting
- **OpenAI API:** 10 requests per minute
- **WordPress REST API:** 60 requests per hour
- **Tavily Search:** 100 queries per day
- **Graceful Degradation:** Queue overflow requests for human review

### Failure Modes
- **LLM API Down:** Fall back to human notification, queue tasks
- **Pinecone Unavailable:** Use cached embeddings (stale data warning)
- **WordPress Unreachable:** Store drafts locally, retry on reconnection
- **Schema Validation Failure:** Quarantine content, alert human immediately
- **Agent Hallucination:** Confidence score below 0.5 triggers automatic rejection

---

## 10. Development Environment Setup

### Local Development Stack

**Prerequisites:**
```bash
# Install Python 3.11+
python3 --version

# Install Docker
docker --version

# Install Redis locally (for testing)
docker run -d -p 6379:6379 redis:alpine

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install crewai fastapi uvicorn redis python-dotenv requests
pip install langchain langchain-openai pinecone-client
```

**Environment Variables (`.env`):**
```bash
# LLM Provider
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4-turbo-preview

# WordPress
WP_SITE_URL=https://your-site.com
WP_USERNAME=agent_user
WP_APP_PASSWORD=xxxx xxxx xxxx xxxx

# Pinecone
PINECONE_API_KEY=...
PINECONE_ENVIRONMENT=us-west1-gcp
PINECONE_INDEX_NAME=sie-knowledge-core

# External Tools
TAVILY_API_KEY=tvly-...
FIRECRAWL_API_KEY=fc-...

# Agent Configuration
AGENT_LOG_PATH=../SIE/09_Logs/agent-actions.md
CONFIDENCE_THRESHOLD=0.75
MAX_DRAFT_RETRIES=3
```

### Project Structure

```
sie-agent-loop/
├── .env
├── .gitignore
├── requirements.txt
├── docker-compose.yml
├── README.md
│
├── agents/
│   ├── __init__.py
│   ├── research_agent.py
│   ├── analyst_agent.py
│   └── editor_agent.py
│
├── tools/
│   ├── __init__.py
│   ├── pinecone_tool.py
│   ├── web_search_tool.py
│   ├── wordpress_tool.py
│   └── schema_validator.py
│
├── server/
│   ├── __init__.py
│   ├── main.py              # FastAPI webhook server
│   ├── agent_orchestrator.py
│   └── logging_middleware.py
│
├── config/
│   ├── __init__.py
│   ├── agent_config.yaml
│   └── governance_rules.py
│
└── tests/
    ├── test_agents.py
    ├── test_tools.py
    └── test_governance.py
```

---

## 11. Code Examples

### Example 1: Pinecone Query Tool (CrewAI)

```python
from crewai_tools import tool
from pinecone import Pinecone
import os

@tool("Query Knowledge Core")
def query_knowledge_core(query: str, top_k: int = 5) -> str:
    """
    Searches the Knowledge Core (Pinecone vector store) for semantically 
    similar articles. Use this to check what we already know about a topic.
    
    Args:
        query: The search query or topic
        top_k: Number of results to return (default: 5)
    
    Returns:
        Formatted string with article titles, excerpts, and similarity scores
    """
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index = pc.Index(os.getenv("PINECONE_INDEX_NAME"))
    
    # Generate embedding for query (using OpenAI)
    from openai import OpenAI
    client = OpenAI()
    
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )
    query_embedding = response.data[0].embedding
    
    # Search Pinecone
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )
    
    # Format results
    formatted_results = []
    for match in results['matches']:
        formatted_results.append(
            f"**{match['metadata'].get('title', 'Untitled')}** "
            f"(similarity: {match['score']:.2f})\n"
            f"Excerpt: {match['metadata'].get('excerpt', 'No excerpt available')}\n"
            f"URL: {match['metadata'].get('url', 'N/A')}\n"
        )
    
    return "\n---\n".join(formatted_results)
```

### Example 2: WordPress Update Tool

```python
from crewai_tools import tool
import requests
import os
from typing import Dict, Optional

@tool("Update WordPress Post")
def update_wordpress_post(
    post_id: int,
    content: str,
    status: str = "draft",
    metadata: Optional[Dict] = None
) -> str:
    """
    Updates a WordPress post via REST API. Always saves as 'draft' by default
    to enforce human review (Rule G-04).
    
    Args:
        post_id: WordPress post ID
        content: Full HTML content of the post
        status: Post status ('draft' or 'pending') - never 'publish'
        metadata: Optional dict with agent_confidence, reasoning, sources
    
    Returns:
        Success message with post URL or error details
    """
    if status == "publish":
        return "ERROR: Agents cannot publish directly. Set status='draft' and flag for human review."
    
    url = f"{os.getenv('WP_SITE_URL')}/wp-json/wp/v2/posts/{post_id}"
    auth = (os.getenv('WP_USERNAME'), os.getenv('WP_APP_PASSWORD'))
    
    payload = {
        'content': content,
        'status': status,
        'meta': {
            'agent_modified': True,
            'agent_timestamp': datetime.now().isoformat(),
            'agent_confidence': metadata.get('confidence', 0.0) if metadata else 0.0,
            'agent_reasoning': metadata.get('reasoning', '') if metadata else '',
            'sources_used': metadata.get('sources', []) if metadata else []
        }
    }
    
    try:
        response = requests.post(url, json=payload, auth=auth, timeout=30)
        response.raise_for_status()
        
        post_url = response.json().get('link', '')
        return f"✓ Post updated successfully: {post_url}\nStatus: {status} (awaiting human review)"
    
    except requests.exceptions.RequestException as e:
        return f"✗ WordPress API Error: {str(e)}"
```

### Example 3: Draft Enrichment Agent (CrewAI)

```python
from crewai import Agent, Task, Crew
from tools.pinecone_tool import query_knowledge_core
from tools.web_search_tool import web_search
from tools.wordpress_tool import update_wordpress_post

# Define the Editor Agent
editor_agent = Agent(
    role="Content Editor",
    goal="Expand bullet-point drafts into comprehensive, well-researched articles",
    backstory="""You are an expert content editor with deep knowledge of SEO and 
    content strategy. You specialize in taking rough outlines and transforming them 
    into publication-ready articles by incorporating internal knowledge and external 
    research.""",
    tools=[query_knowledge_core, web_search, update_wordpress_post],
    verbose=True,
    allow_delegation=False
)

# Define the enrichment task
def enrich_draft(post_id: int, draft_content: str, topic: str):
    """
    Takes a bullet-point draft and enriches it into a full article.
    """
    task = Task(
        description=f"""
        You have been given a draft article (Post ID: {post_id}) with the following content:
        
        {draft_content}
        
        Your task:
        1. Query our Knowledge Core for related articles on "{topic}"
        2. Search the web for recent statistics and data (last 6 months)
        3. Expand each bullet point into 2-3 paragraphs (aim for 1200-1500 words total)
        4. Insert 3-5 internal links to related Knowledge Core articles
        5. Add a compelling introduction and conclusion
        6. Include 2-3 authoritative external citations
        7. Validate that all required metadata is present (title, excerpt, tags)
        8. Save to WordPress as 'draft' status
        
        Important: Include confidence score and reasoning in metadata.
        """,
        agent=editor_agent,
        expected_output="""
        A complete article in markdown format with:
        - 1200-1500 words
        - 3-5 internal links
        - 2-3 external citations
        - Metadata: confidence score, reasoning, sources used
        - Status: saved as draft in WordPress
        """
    )
    
    # Create and run the crew
    crew = Crew(
        agents=[editor_agent],
        tasks=[task],
        verbose=2
    )
    
    result = crew.kickoff()
    return result
```

---

## 12. Testing Strategy

### Unit Tests

**Test Agent Tool Functions:**
```python
import pytest
from tools.pinecone_tool import query_knowledge_core

def test_pinecone_query_returns_results():
    results = query_knowledge_core("semantic SEO", top_k=3)
    assert len(results) > 0
    assert "similarity:" in results
    
def test_pinecone_query_handles_empty_results():
    results = query_knowledge_core("xyznonexistentquery123", top_k=5)
    assert "No results found" in results or len(results) == 0
```

**Test Governance Rules:**
```python
def test_agent_cannot_publish_directly():
    from tools.wordpress_tool import update_wordpress_post
    
    result = update_wordpress_post(
        post_id=123,
        content="Test content",
        status="publish"  # Should be blocked
    )
    
    assert "ERROR" in result
    assert "cannot publish directly" in result.lower()
```

### Integration Tests

**End-to-End Workflow Test:**
```python
def test_draft_enrichment_workflow():
    # 1. Create test draft in WordPress
    draft_id = create_test_draft()
    
    # 2. Trigger agent enrichment
    result = enrich_draft(
        post_id=draft_id,
        draft_content="- Point 1\n- Point 2",
        topic="content marketing"
    )
    
    # 3. Verify output
    assert result['status'] == 'draft'
    assert result['word_count'] > 1000
    assert len(result['internal_links']) >= 3
    assert 'agent_confidence' in result['metadata']
    
    # 4. Verify logging
    with open('SIE/09_Logs/agent-actions.md', 'r') as f:
        log = f.read()
        assert f"post_id:{draft_id}" in log
```

---

## 13. Deployment Checklist

### Pre-Launch Validation

- [ ] All governance rules tested and enforced
- [ ] Schema validation working correctly
- [ ] Logging integrated with existing KPL logs
- [ ] Human approval workflow tested
- [ ] Error handling and rollback procedures verified
- [ ] API rate limits configured
- [ ] Security audit completed (no API keys in logs)
- [ ] Webhook endpoints secured with authentication
- [ ] Agent confidence thresholds calibrated
- [ ] Test run with 10+ draft enrichments (80%+ approval rate)

### Production Deployment

```bash
# 1. Build Docker image
docker build -t sie-agent-loop:v1.0 .

# 2. Deploy to DigitalOcean
docker-compose -f docker-compose.prod.yml up -d

# 3. Configure WordPress webhooks
# Navigate to: WP Admin → Settings → Webhooks
# Add endpoint: https://your-droplet-ip:8000/webhooks/post-saved

# 4. Set up monitoring
# Configure Langfuse: https://langfuse.com
# Add Discord webhook for alerts

# 5. Test production environment
curl -X POST https://your-droplet-ip:8000/health
```

### Monitoring & Maintenance

**Weekly Tasks:**
- Review agent approval rates
- Check error logs for patterns
- Audit confidence score distribution
- Verify API usage stays within budget

**Monthly Tasks:**
- Analyze ROI (time saved vs. cost)
- Review and update agent prompts based on feedback
- Retrain confidence threshold based on approval data
- Generate stakeholder report with metrics

---

## 14. Future Enhancements (Phase 3+)

### Advanced Capabilities (6-12 months)

- **Multi-Language Support:** Agents operating on non-English content
- **Image Generation:** Automated featured image creation via DALL-E
- **Competitive Intelligence:** Automated monitoring of competitor content changes
- **Predictive Analytics:** Forecast trending topics before they peak
- **Client-Specific Training:** Fine-tune agents on client's unique voice and style
- **Voice-to-Content:** Audio briefings converted to articles by agents

### Enterprise Features

- **Multi-Tenant Architecture:** Isolate agents per client
- **Custom Agent Roles:** Clients define their own agent specializations
- **White-Label Dashboard:** Client-facing interface for agent management
- **Advanced Analytics:** Predictive content gap analysis
- **Agent Marketplace:** Pre-configured agent workflows for specific industries

---

## 15. Success Metrics & KPIs

### Phase 2A Targets (Month 1)
- ✅ 1 agent operational
- ✅ 80% human approval rate on enrichments
- ✅ <5% schema validation failures
- ✅ 100% governance rule compliance
- ✅ Complete audit trail maintained

### Phase 2B Targets (Months 2-3)
- ✅ 3 agents orchestrated successfully
- ✅ 3 publication-ready drafts per week
- ✅ 90% human approval rate
- ✅ Average confidence score >0.75
- ✅ ROI: 200%+ (time saved vs. cost)

### Phase 2C Targets (Months 4-6)
- ✅ 50+ articles autonomously monitored
- ✅ <5% false positive rate on freshness alerts
- ✅ 20+ semantic links added per week
- ✅ Zero critical errors or security incidents
- ✅ ROI: 400%+ (fully operational system)

---

## Document Control

**Version History:**
- v1.0 (2025-12-14): Initial Agent Loop architecture and implementation plan

**Related Documents:**
- [[SIE/01_Core/00_core-purpose|SIE Core Purpose]]
- [[SIE/01_Core/01_governance-rules|Governance Rules]]
- [[SIE/04_Engine/KPL/index|Knowledge Pipeline Documentation]]
- [[SIE KPL - Setup from Scratch|KPL Setup Guide]]

**Next Steps:**
1. Review and approve architecture with stakeholders
2. Begin Phase 2A development (single-agent foundation)
3. Establish development environment and testing framework
4. Create detailed implementation timeline with milestones

---
title: "Cloudflare Markdown for Agents"
id: "kb/AI/2_agents/standards/01_cloudflare-markdown-for-agents"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-02-15"
status: "Active"
doc_type: "Reference"
summary: "Technical reference for Cloudflare's 'Markdown for Agents' feature, which allows AI crawlers to request Markdown directly via HTTP headers to reduce token usage."
tags:
  - "cloudflare"
  - "web-scraping"
  - "token-optimization"
  - "standards"
  - "http"
relations:
  - "kb/AI/3_methods/mcp/15_google-developer-knowledge-api-mcp"
  - "kb/AI/3_methods/mcp/16_practical-local-mcp-use-cases"
aliases:
  - "Markdown Content Negotiation"
  - "Content Signals"

# --- AI & RAG Enhancement ---
semantic_summary: "Cloudflare's 'Markdown for Agents' enables AI systems to request content in Markdown format using the 'Accept: text/markdown' HTTP header. This reduces token consumption by approximately 80% compared to raw HTML. The response includes 'x-markdown-tokens' for estimation and 'Content-Signal' headers to indicate permitted AI usage (training, search, input)."
synthetic_questions:
  - "How do I request Markdown from Cloudflare-enabled sites?"
  - "What is the token saving of Markdown vs HTML for agents?"
  - "What are Content Signals in HTTP headers?"
key_concepts:
  - "Content Negotiation"
  - "Token Optimization"
  - "Content Signals"
  - "Accept Header"

# --- SEO & Publication ---
primary_keyword: "Markdown for Agents"
seo_title: "Cloudflare Markdown for Agents: HTTP Content Negotiation Standard"
meta_description: "Technical guide to Cloudflare's Markdown for Agents. Learn how to use the Accept: text/markdown header to optimize AI crawler efficiency."
excerpt: "Reduce AI token costs by 80% using Cloudflare's Markdown for Agents. A technical guide to HTTP content negotiation and Content Signals."
cover_image: ""
---

# Cloudflare Markdown for Agents

**Markdown for Agents** is a content negotiation standard implemented by Cloudflare that allows AI agents and crawlers to request a pre-processed Markdown version of a webpage instead of raw HTML. This significantly reduces token usage and parsing complexity for Large Language Models (LLMs).

## 1. The Problem: HTML Token Bloat
Standard web pages are optimized for visual rendering, not semantic processing.
*   **Token Inefficiency:** A simple header like `## About Us` (3 tokens) becomes `<h2 class="section-title" id="about">About Us</h2>` (12-15 tokens) in HTML.
*   **Noise:** `<div>` wrappers, scripts, and navigation bars consume context window space without adding semantic value.
*   **Impact:** Converting HTML to Markdown typically yields an **80% reduction** in token usage [1]

## 2. Implementation: Content Negotiation

The feature utilizes standard HTTP Content Negotiation. Agents express their preference for Markdown using the `Accept` header.

### 2.1 Request Format
To fetch the Markdown version of a supported page, the client must include `text/markdown` in the header.

**cURL Example:**
```bash
curl https://blog.cloudflare.com/markdown-for-agents/ \
  -H "Accept: text/markdown"
```
 
  **TypeScript/Worker Example:**

```javascript
const r = await fetch(
  `https://target-url.com/`,
  {
    headers: {
      Accept: "text/markdown, text/html", // Prefer markdown, fallback to HTML
    },
  },
);
```

### 2.2 Response Headers

The server responds with the Markdown content and specific metadata headers:

|Header|Description|
|:--|:--|
|`content-type`|`text/markdown; charset=utf-8`|
|`x-markdown-tokens`|Estimated number of tokens in the returned document. Useful for context window budgeting.|
|`content-signal`|Permissions for AI usage (see Section 3).|

## 3. Content Signals

Cloudflare includes a `Content-Signal` header to explicitly state how the content provider permits their data to be used by AI systems.

**Example Header:**  
`Content-Signal: ai-train=yes, search=yes, ai-input=yes`

- **ai-train:** Can be used for model training.
- **search:** Can be used for search indexing (RAG).
- **ai-input:** Can be used as direct input for an agentic workflow (e.g., summarization).

## 4. Alternative Conversion Methods

If a source does not support native Markdown negotiation, Cloudflare provides alternative APIs for developers:

- **Workers AI:** `AI.toMarkdown()` supports summarization and conversion of various document types.
- **Browser Rendering:** The `/markdown` REST API can render dynamic JavaScript-heavy pages in a headless browser before converting them to Markdown [1]
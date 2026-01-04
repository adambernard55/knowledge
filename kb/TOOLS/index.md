---
title: "AI & Marketing Tools Knowledge Base"
id: "SIE/REF/Tools-Index-01"
version: "1.1"
steward: "Adam Bernard"
updated: "2026-01-04"
status: "Active"
doc_type: "Reference"
summary: "The master index for the AI & Marketing Tools Knowledge Base, providing an overview of all tool categories and reference guides."
tags:
  - index
  - tools
  - knowledge-base
  - overview
  - marketing-tools
  - ai-tools
relations:
  - "kb/index.md"
aliases:
  - "Tools Index"
  - "Marketing Tools KB"

# --- AI & RAG Enhancement ---
semantic_summary: "This index page serves as the central gateway to the AI & Marketing Tools knowledge base. It categorizes and lists all documented tools, covering areas like analytics, social media, content creation, and SEO, making it easy to find detailed reference guides for each platform."
synthetic_questions:
  - "Where can I find a list of all marketing tools?"
  - "What AI tools are documented in the knowledge base?"
  - "How is the tools knowledge base organized?"
key_concepts:
  - "marketing technology"
  - "ai tools"
  - "saas platforms"
  - "knowledge base"
  - "tool directory"

# --- SEO & Publication ---
primary_keyword: "marketing tools knowledge base"
seo_title: "Marketing Tools Knowledge Base: The Complete Index"
meta_description: "The complete index for our marketing tools knowledge base. Find detailed guides on AI, SEO, analytics, and social media platforms."
excerpt: "Navigate our comprehensive marketing tools knowledge base. This index provides a complete overview of all tool categories and reference guides."
cover_image: ""
---

# AI & Marketing Tools Knowledge Base

Welcome to the central repository for reference guides on the marketing and AI tools that power our strategies. This knowledge base is structured to provide detailed, actionable insights into the capabilities and implementation of each platform.

Each section below represents a core functional category. Use this page as your primary table of contents to navigate the different toolsets.

---

## [[kb/TOOLS/01_applied-ai-use-cases|Applied AI & Playbooks]]

This section provides practical frameworks and playbooks for implementing AI across key marketing functions.

```dataview
TABLE WITHOUT ID
  file.link as "Topic",
  semantic_summary as "Description"
FROM "kb/TOOLS"
WHERE contains(file.name, "applied-ai")
SORT file.name ASC
```

---

## [[kb/TOOLS/ai-foundation-models/index|AI Foundation Models]]

This section explores the core large-scale models that power today's generative and intelligent systems.

```dataview
TABLE WITHOUT ID
  file.link as "Tool",
  semantic_summary as "Description"
FROM "kb/TOOLS/ai-foundation-models"
WHERE file.name != "index.md"
SORT file.name ASC
```

---

## [[kb/TOOLS/analytics-data-insights/index|Analytics & Data Insights]]

This section covers platforms for web analytics, data visualization, and deriving actionable insights from performance data.

```dataview
TABLE WITHOUT ID
  file.link as "Tool",
  semantic_summary as "Description"
FROM "kb/TOOLS/analytics-data-insights"
WHERE file.name != "index.md"
SORT file.name ASC
```

---

## [[kb/TOOLS/coding-development/index|Coding & Development]]

This section highlights AI tools that act as intelligent assistants for the software development lifecycle.

```dataview
TABLE WITHOUT ID
  file.link as "Tool",
  semantic_summary as "Description"
FROM "kb/TOOLS/coding-development"
WHERE file.name != "index.md"
SORT file.name ASC
```

---

## [[kb/TOOLS/content-creation/index|Content Creation]]

This section covers tools for AI-powered content automation, including text, image, video, and audio generation.

```dataview
TABLE WITHOUT ID
  file.link as "Tool",
  semantic_summary as "Description"
FROM "kb/TOOLS/content-creation"
WHERE file.name != "index.md"
SORT file.name ASC
```

---

## [[kb/TOOLS/marketing-automation/index|Marketing Automation]]

This section details platforms for automating multi-channel marketing campaigns, from email to CRM.

```dataview
TABLE WITHOUT ID
  file.link as "Tool",
  semantic_summary as "Description"
FROM "kb/TOOLS/marketing-automation"
WHERE file.name != "index.md"
SORT file.name ASC
```

---

## [[kb/TOOLS/productivity-workflow/index|Productivity & Workflow]]

This section includes tools designed to streamline workflows, manage tasks, and enhance productivity.

```dataview
TABLE WITHOUT ID
  file.link as "Tool",
  semantic_summary as "Description"
FROM "kb/TOOLS/productivity-workflow"
WHERE file.name != "index.md"
SORT file.name ASC
```

---

## [[kb/TOOLS/research-knowledge-agents/index|Research & Knowledge Agents]]

This section focuses on AI agents designed for research, data synthesis, and knowledge management.

```dataview
TABLE WITHOUT ID
  file.link as "Tool",
  semantic_summary as "Description"
FROM "kb/TOOLS/research-knowledge-agents"
WHERE file.name != "index.md"
SORT file.name ASC
```

---

## [[kb/TOOLS/seo/index|SEO & Search Intelligence]]

This section includes platforms for keyword research, rank tracking, technical audits, and competitive analysis.

```dataview
TABLE WITHOUT ID
  file.link as "Tool",
  semantic_summary as "Description"
FROM "kb/TOOLS/seo-optimization"
WHERE file.name != "index.md"
SORT file.name ASC
```

---

## [[kb/TOOLS/social-media/index|Social Media Management]]

This section details tools for social media scheduling, engagement, monitoring, and influencer marketing.

```dataview
TABLE WITHOUT ID
  file.link as "Tool",
  semantic_summary as "Description"
FROM "kb/TOOLS/social-media"
WHERE file.name != "index.md"
SORT file.name ASC
```


---

```dataviewjs 
const allPages = dv.pages('"Knowledge/Tools/content-generation"').array(); const categories = [...new Set(allPages.flatMap(p => p.tool_category || []))].sort(); const pricingModels = [...new Set(allPages.map(p => p.pricing_model).filter(p => p))].sort(); const difficulties = [...new Set(allPages.map(p => p.difficulty).filter(p => p))].sort(); const aiTypes = [...new Set(allPages.flatMap(p => p.ai_type || []))].sort(); const container = dv.el("div", ""); container.innerHTML = ` <div style="background: var(--background-secondary); padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 1px solid var(--background-modifier-border);"> <h3 style="margin-top: 0;">Filter & Sort Tools</h3> <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-bottom: 15px;"> <div> <label style="display: block; margin-bottom: 5px; font-weight: bold;">Category:</label> <select id="categoryFilter" style="width: 100%; padding: 8px; border-radius: 5px; background: var(--background-primary); border: 1px solid var(--background-modifier-border);"> <option value="">All Categories</option> ${categories.map(cat => '<option value="' + cat + '">' + cat + '</option>').join('')} </select> </div> <div> <label style="display: block; margin-bottom: 5px; font-weight: bold;">Pricing:</label> <select id="pricingFilter" style="width: 100%; padding: 8px; border-radius: 5px; background: var(--background-primary); border: 1px solid var(--background-modifier-border);"> <option value="">All Pricing</option> ${pricingModels.map(pm => '<option value="' + pm + '">' + pm + '</option>').join('')} </select> </div> <div> <label style="display: block; margin-bottom: 5px; font-weight: bold;">Difficulty:</label> <select id="difficultyFilter" style="width: 100%; padding: 8px; border-radius: 5px; background: var(--background-primary); border: 1px solid var(--background-modifier-border);"> <option value="">All Levels</option> ${difficulties.map(d => '<option value="' + d + '">' + d + '</option>').join('')} </select> </div> <div> <label style="display: block; margin-bottom: 5px; font-weight: bold;">AI Type:</label> <select id="aiTypeFilter" style="width: 100%; padding: 8px; border-radius: 5px; background: var(--background-primary); border: 1px solid var(--background-modifier-border);"> <option value="">All Types</option> ${aiTypes.map(ai => '<option value="' + ai + '">' + ai + '</option>').join('')} </select> </div> </div> <div style="display: flex; gap: 10px; flex-wrap: wrap; align-items: center;"> <label style="font-weight: bold;">Sort by:</label> <button id="sortName" style="padding: 8px 15px; border-radius: 5px; background: var(--interactive-accent); color: white; border: none; cursor: pointer;">Name</button> <button id="sortUpdated" style="padding: 8px 15px; border-radius: 5px; background: var(--interactive-accent); color: white; border: none; cursor: pointer;">Last Updated</button> <button id="sortDifficulty" style="padding: 8px 15px; border-radius: 5px; background: var(--interactive-accent); color: white; border: none; cursor: pointer;">Difficulty</button> <button id="resetFilters" style="padding: 8px 15px; border-radius: 5px; background: var(--background-modifier-border); border: none; cursor: pointer; margin-left: auto;">Reset All</button> </div> <div id="resultCount" style="margin-top: 15px; font-weight: bold; color: var(--text-muted);"></div> </div> <div id="toolResults"></div> `; function renderTools() { const categoryFilter = container.querySelector('#categoryFilter').value; const pricingFilter = container.querySelector('#pricingFilter').value; const difficultyFilter = container.querySelector('#difficultyFilter').value; const aiTypeFilter = container.querySelector('#aiTypeFilter').value; const toolResults = container.querySelector('#toolResults'); const sortBy = toolResults.dataset.sortBy || 'name'; let filtered = allPages.filter(page => { if (categoryFilter && (!page.tool_category || !page.tool_category.includes(categoryFilter))) return false; if (pricingFilter && page.pricing_model !== pricingFilter) return false; if (difficultyFilter && page.difficulty !== difficultyFilter) return false; if (aiTypeFilter && (!page.ai_type || !page.ai_type.includes(aiTypeFilter))) return false; return true; }); if (sortBy === 'name') { filtered.sort((a, b) => (a.tool_name || a.file.name).localeCompare(b.tool_name || b.file.name)); } else if (sortBy === 'updated') { filtered.sort((a, b) => (b.last_updated || '').localeCompare(a.last_updated || '')); } else if (sortBy === 'difficulty') { const diffOrder = { "Beginner": 1, "Intermediate": 2, "Advanced": 3 }; filtered.sort((a, b) => (diffOrder[a.difficulty] || 999) - (diffOrder[b.difficulty] || 999)); } container.querySelector('#resultCount').textContent = 'Showing ' + filtered.length + ' of ' + allPages.length + ' tools'; const resultsHtml = filtered.map(page => { const tags = page.tags ? page.tags.map(t => '<span style="background: var(--interactive-accent); color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.85em; margin-right: 5px;">' + t + '</span>').join('') : ''; return '<div style="border: 1px solid var(--background-modifier-border); border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: var(--background-secondary); box-shadow: 0 2px 4px rgba(0,0,0,0.1);"><h2 style="margin-top: 0;"><a href="' + page.file.path + '" class="internal-link">' + (page.tool_name || page.file.name) + '</a></h2><p style="color: var(--text-muted); font-style: italic;">' + (page.primary_function || '') + '</p><hr style="border: none; border-top: 1px solid var(--background-modifier-border); margin: 15px 0;"><p><strong>Category:</strong> ' + (page.tool_category || 'N/A') + '</p><p><strong>AI Type:</strong> ' + (page.ai_type || 'N/A') + '</p><p><strong>Pricing:</strong> ' + (page.pricing_model || 'N/A') + '</p><p><strong>Difficulty:</strong> ' + (page.difficulty || 'N/A') + '</p>' + (page.website ? '<p><strong>Website:</strong> <a href="' + page.website + '" target="_blank">Visit →</a></p>' : '') + '<p><strong>Updated:</strong> ' + (page.last_updated || 'N/A') + '</p>' + (tags ? '<div style="margin-top: 10px;">' + tags + '</div>' : '') + '</div>'; }).join(''); toolResults.innerHTML = resultsHtml || '<p style="text-align: center; color: var(--text-muted); padding: 40px;">No tools match your filters.</p>'; } container.querySelector('#categoryFilter').addEventListener('change', renderTools); container.querySelector('#pricingFilter').addEventListener('change', renderTools); container.querySelector('#difficultyFilter').addEventListener('change', renderTools); container.querySelector('#aiTypeFilter').addEventListener('change', renderTools); container.querySelector('#sortName').addEventListener('click', () => { container.querySelector('#toolResults').dataset.sortBy = 'name'; renderTools(); }); container.querySelector('#sortUpdated').addEventListener('click', () => { container.querySelector('#toolResults').dataset.sortBy = 'updated'; renderTools(); }); container.querySelector('#sortDifficulty').addEventListener('click', () => { container.querySelector('#toolResults').dataset.sortBy = 'difficulty'; renderTools(); }); container.querySelector('#resetFilters').addEventListener('click', () => { container.querySelector('#categoryFilter').value = ''; container.querySelector('#pricingFilter').value = ''; container.querySelector('#difficultyFilter').value = ''; container.querySelector('#aiTypeFilter').value = ''; container.querySelector('#toolResults').dataset.sortBy = 'name'; renderTools(); }); renderTools();
```


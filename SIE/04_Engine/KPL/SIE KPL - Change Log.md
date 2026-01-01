---
title: SIE Knowledge Pipeline - Change Log
id: 20251213074000
version: 1
author: Adam Bernard
date: 2025-12-13
category: Systems Integration & Revision History
Excerpt: Historical log of structural, configuration, and workflow updates made to the SIE Knowledge Pipeline (Obsidian → GitHub → WordPress → AI Engine → Pinecone).
meta_description: Track changes and version updates to the SIE Knowledge Pipeline, including folder renames, workflow configuration adjustments, and maintenance notes.
primary_keyword: SIE Knowledge Pipeline changelog
related:
  - SIE KPL Overview
  - SIE KPL - Setup from Scratch
  - SIE KPL - Modify Existing Setup
tags: [knowledge-pipeline, changelog, maintenance, documentation]
---

# 🧾 SIE Knowledge Pipeline - Change Log

This document maintains a running record of **pipeline adjustments, workflow changes, and troubleshooting resolutions** across all system layers.

---

## 2025-12-13 — Rebuild & Alignment ✔️
- Created unified folder structure: `Knowledge/` → `kb/`
- Re-initialized Git repository (`sie-kb`)
- Updated `.gitignore` to maintain Smart Chat compatibility
- Renamed GitHub workflow: `seo-sync.yml` → `kb-sync.yml`
- Verified preservation of WordPress posts (update via slug match)
- Confirmed AI Engine generating Pinecone embeddings automatically
- Added new documentation suite:
  - [[SIE KPL Overview]]
  - [[SIE KPL - Setup from Scratch]]
  - [[SIE KPL - Modify Existing Setup]]

---

## 2025-12-10 — GitHub Actions Workflow Refinement
- Integrated frontmatter extraction and content sanitization in sync script
- Enhanced tag processing to support YAML list format
- Added field-based topic ID overrides
- Added Pandoc error handling during markdown-to-HTML conversion
- Embedded AI Engine vector generation step post-sync

---

## 2025-11-17 — Initial `seo-sync.yml` Deployment 🚀
- Connected Obsidian → GitHub → WordPress pipeline end-to-end
- Established topic and tag hierarchy mapping for `/SEO/`
- Configured `KNOWLEDGE_SEO_TOPIC_ID` default and dynamic category switch
- Tested push and manual (`workflow_dispatch`) run success

---

### Future Log Template
Whenever changes occur, add a new section using the template below:

```markdown
## YYYY-MM-DD — [Short Summary]
- Description of repository, workflow, or plugin changes
- Problem encountered and solution implemented
- Validation outcome and cross-system impact (if any)
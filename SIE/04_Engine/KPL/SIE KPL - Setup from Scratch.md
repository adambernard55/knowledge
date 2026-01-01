---
title: SIE Knowledge Pipeline - Setup from Scratch
id: 20251213073001
version: 1
author: Adam Bernard
date: 2025-12-13
category: Systems Integration & Automation
Excerpt: Step-by-step guide to build the SIE Knowledge Pipeline from scratch, connecting Obsidian to GitHub to WordPress, and syncing content into AI Engine and Pinecone.
meta_description: Learn how to create the SIE Knowledge Pipeline from scratch — configure GitHub Actions, WordPress API integration, and AI Engine embeddings.
primary_keyword: SIE Knowledge Pipeline setup
related:
  - SIE KPL - Modify Existing Setup
  - SIE KPL Overview
tags: [knowledge-pipeline, setup, automation, ai-engine, wordpress, github, obsidian]
---

# 🧩 SIE Knowledge Pipeline - Setup from Scratch

## Purpose
This document provides a **clean installation guide** for a new or rebuilt environment that connects:
**Obsidian → GitHub → WordPress → AI Engine → Pinecone.**

Use this when moving to a new computer, creating a new repository, or establishing the pipeline for the first time.

---

## Step 1: Prerequisites ✅

- Obsidian with Git plugin installed  
- GitHub Desktop (or Git CLI)  
- GitHub account configured  
- WordPress site with a **Custom Post Type** registered (`/kb/`)  
- AI Engine WordPress Plugin active (vector sync enabled)  
- Pinecone database configured within AI Engine  
- WordPress App Password created for the API user

---

## Step 2: Prepare Directories

**Vault Path Example:**

```markdown
## Step 2: Prepare Directories

**Vault Path Example:**
```

SIE/04_Knowledge/kb/

````

This will serve as the publishing source folder.

---

## Step 3: Initialize Git Repository

```bash
cd "C:\Path\To\SIE\04_Knowledge\kb"
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
````

### Add GitHub Remote

```bash
git remote add origin https://github.com/yourusername/sie-kb.git
```

---

## Step 4: Configure `.gitignore`

Exclude clutter (e.g., Smart Connections, .obsidian files):

```bash
# Ignore all except kb folder
/*
!/kb/

# Inside kb, ignore system files
kb/.obsidian/
kb/.trash/
kb/.DS_Store
kb/*.tmp
```

---

## Step 5: Create or Adapt GitHub Actions Workflow

Place the following file inside your repository:

```
.github/workflows/kb-sync.yml
```

### Action File Reference

This workflow converts Markdown → HTML → WordPress (via REST API) and triggers embedding.  
See [seo-sync.yml](app://obsidian.md/seo-sync.yml) for the canonical version.

**Update file path references**:

```yaml
paths:
  - 'kb/**/*.md'
```

---

## Step 6: Configure Repository Secrets (GitHub → WP)

At **GitHub → Settings → Secrets → Actions**, add the following:

|Secret Name|Description|
|---|---|
|`WP_SITE_URL`|WordPress base URL|
|`WP_USERNAME`|WordPress username|
|`WP_APP_PASSWORD`|WordPress app password|
|`AIENGINE_BEARER_TOKEN`|Provided by AI Engine|
|`KNOWLEDGE_SEO_TOPIC_ID`|Default parent topic ID (for /kb)|

---

## Step 7: First Commit and Push

```bash
git add .
git commit -m "Initial setup for SIE Knowledge Pipeline"
git push -u origin main
```

Verify on GitHub that all files including `.github/workflows/kb-sync.yml` exist.

---

## Step 8: Run Workflow

Go to **GitHub → Actions → kb-sync → Run workflow**  
Choose **Manual dispatch** to process all files initially.

### Expected log output:

```
✓ Successfully synced: Semantic Depth in SEO
✓ Embeddings generated and stored in Pinecone
SEO sync completed (manual trigger - processed all files)
```

---

## Step 9: Verify in WordPress Site

- Check **Knowledge Base (/kb/)** for new or updated posts
- Open one article → confirm it contains expected formatting
- AI Engine dashboard → confirm embedding succeeded (linked by Post ID)

---

## Step 10: Optional Obsidian Git Plugin Configuration

Once verified:

1. Re-enable Obsidian’s Git plugin
2. Set:
    - Vault backup interval = `0`
    - Auto pull interval = `0`
    - Disable push = ✅ (manual push preferred via GitHub Desktop)

---

## Verification Summary ✅

|Layer|Expected Behavior|
|---|---|
|Obsidian|Notes commit cleanly from `kb/`|
|GitHub|Workflow triggers under `/kb/**/*.md`|
|WordPress|Existing posts updated or new ones created|
|AI Engine|Embeddings generated in Pinecone|

---

## Notes & References

- [SIE KPL Overview](app://obsidian.md/SIE%20KPL%20Overview)
- [SIE KPL - Modify Existing Setup](app://obsidian.md/SIE%20KPL%20-%20Modify%20Existing%20Setup)
- [seo-sync.yml](app://obsidian.md/seo-sync.yml)
- [[SIE KPL - Change Log]]


---
title: SIE Knowledge Pipeline - Modify Existing Setup
id: 20251213073002
version: 1
author: Adam Bernard
date: 2025-12-13
category: Systems Integration & Maintenance
Excerpt: Guide to safely modify, troubleshoot, or rename components of the SIE Knowledge Pipeline without overwriting existing WordPress posts or AI embeddings.
meta_description: Learn how to modify or repair your existing SIE Knowledge Pipeline safely without deleting posts on WordPress.
primary_keyword: modify existing SIE Knowledge Pipeline
related:
  - SIE KPL - Setup from Scratch
  - SIE KPL Overview
tags: [knowledge-pipeline, troubleshoot, automation, ai-engine, wordpress, github, maintenance]
---

# 🔧 SIE Knowledge Pipeline - Modify Existing Setup

## Purpose
This note provides **modular repair and update procedures** for maintaining a pipeline that already exists, while preserving all content in WordPress and Pinecone.

Use this if:
- You renamed folders or repositories  
- Git was disabled or re-initialized  
- Workflow disappeared from GitHub Actions  
- Smart Chat (Smart Connections) conflicted with Git  
- You’re migrating to a new computer  

---

## Safe Modification Principles ⚙️

1. **Do Not Delete WordPress Posts**  
   The workflow automatically updates existing posts via `slug` matching.  
   Posts are only *updated*, not deleted.

2. **Avoid Re-initializing WordPress Topic IDs**  
   Reuse your existing `KNOWLEDGE_SEO_TOPIC_ID` or equivalent.

3. **If in doubt, trigger manually** with `workflow_dispatch` before merging changes.

---

## 1. Rename Folder or Repository

**Goal:** Rename from obsolete `Knowledge/` → unified `kb/`

### Steps
```bash
cd "SIE/04_Knowledge/"
mv Knowledge kb
````

Update workflow references:

```yaml
paths:
  - 'kb/**/*.md'
```

Update in workflow “find” command:

```bash
find kb -name "*.md" -type f
```

Commit changes:

```bash
git add .
git commit -m "Renamed Knowledge folder to kb"
git push
```

---

## 2. Fix `.gitignore` Conflicts (Smart Chat or Plugins)

When Smart Connections is blocked by `.gitignore`, use this configuration:

```bash
/*
!/kb/

kb/.obsidian/
kb/.trash/
kb/*.tmp
kb/.DS_Store
```

> ✅ Keeps vault plugins untracked while still allowing Git operations on `/kb/`

---

## 3. Rebuild Repository Without Losing Existing Links

If `.git` folder became corrupted:

1. Backup the entire `/kb/` folder
2. Delete only `.git` from local folder
3. Re-initialize:
    
    ```bash
    git init
    git remote add origin https://github.com/yourusername/sie-kb.git
    git fetch origin main
    git reset --hard origin/main
    ```
    
4. Verify `.github/workflows/` exists in main branch.

---

## 4. Workflow Missing in GitHub Actions

**Symptom:** Workflow tab empty after push.  
**Fix:** Confirm:

- Workflow file path = `.github/workflows/kb-sync.yml`
- YAML syntax valid
- Branch = `main` (not `master`)

Trigger once manually under “Actions → Run Workflow.”

---

## 5. Preserve WordPress Posts During Rebuild 🧠

Whenever folder/repos are renamed, **don’t delete WordPress items**.  
Existing posts update as long as markdown titles or frontmatter `title:` fields match previous slugs.

**Workflow logic:**

```bash
existing_post=$(curl -s "$WP_URL/wp-json/wp/v2/knowledge?slug=$slug")
if [ ! -z "$post_id" ]; then
  method="PUT"  # Update
else
  method="POST" # Create new
fi
```

✅ Safe to rebuild local system — posts remain untouched.

---

## 6. Validate AI Engine & Pinecone Sync

After GitHub sync, check:

- **WordPress Dashboard → AI Engine → Vectors**
    - New or updated embeddings appear under same post IDs.

If embeddings fail:

- Verify `BEARER_TOKEN` secret
- Check workflow log for `⚠ Embedding generation failed`

---

## 7. Troubleshooting Quick Fix Reference

|Issue|Solution|
|---|---|
|Workflow not triggering|Check `.yml` indentation, file path, branch, and Actions enabled|
|Smart Chat disabled Git|Update `.gitignore` to ignore `.obsidian/` only|
|Obsidian Git "Not Ready"|Initialize vault-local Git root|
|Existing posts duplicated|Ensure titles/slugs match WordPress records|
|Git refuses push|Check authentication or re-add remote|

---

## 8. Verification Checklist ✅

- [ ] Workflow appears under GitHub → Actions
- [ ] Existing posts update instead of creating duplicates
- [ ] WordPress credentials functional (`curl -u` test passes)
- [ ] AI Engine confirms embeddings created
- [ ] `.gitignore` no longer blocks plugin automation

---

## Notes & References

- [SIE KPL Overview](app://obsidian.md/SIE%20KPL%20Overview)
- [SIE KPL - Setup from Scratch](app://obsidian.md/SIE%20KPL%20-%20Setup%20from%20Scratch)
- [seo-sync.yml](app://obsidian.md/seo-sync.yml)
- [[SIE KPL - Change Log]]

---

> **Maintenance Note:**  
> Keep this document living — add real fixes whenever you resolve issues.  
> The Setup guide should remain static; this one evolves as your system matures.


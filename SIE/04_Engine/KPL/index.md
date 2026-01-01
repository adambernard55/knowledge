---
title: Index of Knowledge Pipeline
id: 20251213082111
version: 1
Author: Adam Bernard
steward:
date: 2025-12-13
category:
category_id:
Excerpt:
doc_type:
relations:
aliases:
last_updated: 2025-12-13
tags:
---

# Knowledge Base Pipeline

The data and publish files for the Knowledge Base Pipeline are located in the kb/

## Contents

```dataview
TABLE WITHOUT ID
  file.link as "Topic",
  Excerpt as "Description",
  tags as "Tags"
FROM "SIE/04_Engine/KPL"
WHERE file.name != "index.md"
SORT file.name ASC
```
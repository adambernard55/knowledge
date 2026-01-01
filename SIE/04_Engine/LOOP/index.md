---
title: Index of Knowledge Loop
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

# Knowledge Base Loop



## Contents

```dataview
TABLE WITHOUT ID
  file.link as "Topic",
  Excerpt as "Description",
  tags as "Tags"
FROM "SIE/04_Engine/LOOP"
WHERE file.name != "index.md"
SORT file.name ASC
```
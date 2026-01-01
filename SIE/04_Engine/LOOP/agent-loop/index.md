---
title: index
id: 20260101075134
version: 1
Author: Adam Bernard
steward:
date: 2026-01-01
category:
category_id:
Excerpt:
Meta Description:
Primary_Keyword:
Featured_Image:
doc_type:
relations:
aliases:
last_updated: 2026-01-01
tags:
---

## Contents

```dataview
TABLE WITHOUT ID
  file.link as "Topic",
  Excerpt as "Description",
  tags as "Tags"
FROM "SIE/04_Engine/LOOP/agent-loop"
WHERE file.name != "index.md"
SORT file.name ASC
```
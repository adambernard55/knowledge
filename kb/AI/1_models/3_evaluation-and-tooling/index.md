---
title: "AI Evaluation & Tooling"
id: "SIE/AI/Eval/Index"
version: "1.0"
steward: "Adam Bernard"
updated: "2026-01-02"
status: "Active"
doc_type: "Reference"
summary: "An index of reference documents covering the 2026 ecosystem for AI evaluation, observability, and tooling."
tags: ["index", "ai", "llm", "evaluation", "observability", "tooling"]
aliases: ["AI Evaluation Index"]
semantic_summary: >
  This index page serves as the gateway to a comprehensive collection of documents on the 2026 AI evaluation and tooling ecosystem. It links to guides on platforms, methodologies like LLM-as-a-judge, advanced benchmarks, agentic tooling, and AI FinOps.
synthetic_questions:
  - "Where can I find all the documents about AI evaluation and tooling?"
  - "What topics are covered in the AI evaluation section?"
# --- SEO & Publication ---
primary_keyword: "ai evaluation"
seo_title: "AI Evaluation and Tooling: The Complete 2026 Guide"
meta_description: "A complete index of guides to the 2026 AI evaluation and tooling ecosystem, covering observability, benchmarks, FinOps, and more."
excerpt: "Explore our complete guide to the 2026 AI evaluation and tooling ecosystem. This index covers everything from platforms and benchmarks to FinOps and compliance."
cover_image: "assets/images/ai-evaluation-index-cover.png"
---

# AI Evaluation & Tooling

This section provides a comprehensive deep-dive into the 2026 AI evaluation and tooling ecosystem. It covers the critical infrastructure required to build, deploy, and monitor reliable large language models (LLMs) and agentic systems. The documents explore the distinction between evaluation-centric and observability-centric platforms, standardized methodologies like "LLM-as-a-Judge," advanced performance benchmarks, and the essential tooling for AI FinOps and security compliance. This collection serves as a strategic guide to the full LLM development lifecycle, from initial dataset creation to continuous production monitoring.

---

## Contents

```dataview
TABLE WITHOUT ID
  file.link as "Topic",
  summary as "Description",
  tags as "Tags"
FROM "kb/AI/1_models/3_evaluation-and-tooling"
WHERE file.name != "index.md"
SORT file.name ASC
```



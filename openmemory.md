---
title: openmemory
id: 20260221150729
version: "1.0"
steward: Adam Bernard
updated: 2026-02-22
status: Active
doc_type:
summary:
tags:
  -
relations:
  -
aliases:
  -
target_audience:
security_level: Internal
owner_team:
semantic_summary: ""
synthetic_questions:
  -
key_concepts:
  -
primary_keyword:
seo_title:
meta_description:
excerpt:
cover_image:
---

# OpenMemory Guide — Knowledge Base Project

## Overview

**Repository:** `adambernard55/knowledge` (GitHub)
**Branch:** `main`
**Local path:** `C:\Users\AdamB\Documents\Brain\Adam\`
**Platform:** Obsidian vault with Templater (stubs use `<% tp.file.cursor() %>`)

The knowledge base (`kb/`) contains structured reference documents covering AI-powered marketing across multiple domains. All content follows the SIE document strategy and master hub schema.

## Architecture

### KB Folder Structure

```
kb/
├── GROWTH/                    # 115 files — AI marketing domains
│   ├── Ads/                   # E-commerce advertising (7 subfolders, 29 files)
│   ├── Email/                 # Email & CRM marketing (5 subfolders, 32 files)
│   ├── Affiliate/             # Affiliate marketing (8 files)
│   ├── Creator/               # Creator marketing (22 files) — renamed from "influencer"
│   ├── Social/                # Social media (5 subfolders, 24 files)
│   ├── index.md               # GROWTH master index
│   ├── GROWTH.md              # GROWTH landing page
│   └── 00-07_*.md             # 10 root reference documents
├── E-COMMERCE/                # 34 files — E-commerce AI buyer journey
│   ├── 1_Strategy/            # AI foundations, STRIVE, tech stack (5 files)
│   ├── 2_Growth/              # Content/SEO, segmentation (3 files)
│   ├── 3_Engagement/          # Recommendations, personalization, chatbots (5 files)
│   ├── 4_Conversion/          # CRO, pricing, checkout (5 files)
│   ├── 5_Retention/           # Post-purchase, loyalty, advocacy (5 files)
│   ├── 6_Future/              # Implementation, ROI, scaling, trends (5 files)
│   ├── 7_Plans/               # Capstone action plans (3 files)
│   ├── 00_E-COMMERCE.md       # Taxonomy document
│   ├── E-COMMERCE.md          # Landing page (has sticker: lucide//shopping-cart)
│   └── index.md               # KB navigation index
└── check-fm.py                # Frontmatter validator (hardcoded to GROWTH)
```

### Standards Documents (read-only references)

- **`SIE/01_Strategy/05_doc-strategy.md`** — Reference doc standards (Fleet Commander voice, 800-1200 words, stand-alone rule, epistemic markers, pre-commit checklist)
- **`SIE/00_Core/03_schema.md`** — Master Hub Schema (required YAML frontmatter properties)

### Document Types

| doc_type | Purpose | Voice | Word Count |
|---|---|---|---|
| `Reference` | Knowledge content | Fleet Commander — authoritative, methodical | 800-1200 |
| `context_index` | Folder navigation/overview | Neutral, navigational | 200-400 |

### Reference Document Rules

- **Stand-Alone Rule:** Every paragraph must make sense in isolation (no dangling pronouns)
- **Epistemic Markers:** Axiomatic / Heuristic / Speculative / Conditional signal phrases
- **Propositions over Narrative:** Break complex ideas into clear logical statements
- **High Scannability:** Tables, bolding, lists
- **Keyword density:** ~1%
- **Strip course scaffolding:** "Welcome to Lesson" intros, Learning Objectives, time estimates, workbook exercises, "Suggested Question for Link" blocks, module transitions

### ID Conventions

| Folder | Pattern | Examples |
|---|---|---|
| GROWTH/Ads | `KB/GROWTH/ADS/[FOLDER]-[SEQ]` | STR-01, ACQ-02, ENG-03 |
| GROWTH/Email | `KB/GROWTH/EMAIL/[FOLDER]-[SEQ]` | STR-01, PER-02, AUT-03 |
| E-COMMERCE | `KB/AI/MKTG/ECOM-[SEQ]` | ECOM-00 through ECOM-24 |
| GROWTH/Creator | `KB/GROWTH/CRE-[SEQ]` | CRE-00 through CRE-23 |
| Folder indexes | `KB/.../[ABBREV]-00` or `KB/.../[ABBREV]-IDX` | ECOM-STR-00, ECOM-FUT-00 |

### Schema-Compliant Frontmatter (all fields required)

```yaml
---
title: ""
id: ""
version: "1.0"
steward: "Adam Bernard"
updated: YYYY-MM-DD
status: Active
doc_type: Reference  # or context_index
summary: ""
tags: []
relations: []
aliases: []
semantic_summary: >
  [2-3 sentences for vector embedding]
synthetic_questions:
  - ""
key_concepts:
  - ""
primary_keyword: ""
seo_title: ""
meta_description: ""  # ≤120 chars
excerpt: ""  # ≤50 words
cover_image: ""
target_audience: All_Staff
security_level: Internal
owner_team: Strategy
---
```

## Tools & Validation

### check-fm.py

- **Location:** `kb/check-fm.py`
- **Limitation:** Hardcoded to scan `GROWTH/` only
- **Windows fix:** Must run with `PYTHONIOENCODING=utf-8` (cp1252 codec crashes on non-breaking hyphens U+2011)
- **For E-COMMERCE or combined scans:** Use inline Python with configurable `Path()` roots
- **Validation criteria:** Checks for `semantic_summary` and `primary_keyword` presence → FULL SCHEMA

### File Naming

- Folder indexes: Keep existing stub filenames (e.g., `1_Strategy.md`, `5_Retention.md`)
- Reference docs: Either keep original names or use kebab-case derived from topic
- Non-breaking hyphens (‑ U+2011) in Email filenames must be preserved exactly in git commands

## Commit History (KB restructuring)

| Commit | Description | Files |
|---|---|---|
| `669b73a` | Restructure 7_marketing to GROWTH with full schema frontmatter | — |
| `9c1b2fc` | Split Ads master files into schema-compliant Reference documents | 29 |
| `9dec0a1` | Rewrite Email lesson files as schema-compliant Reference documents | 32 |
| `88c8ce2` | Rewrite E-COMMERCE course content as schema-compliant Reference documents | 34 |
| `c98337b` | Add schema-compliant frontmatter to 5 GROWTH index files | 5 |
| `1993aed` | Update openmemory.md with KB project context and standards | 1 |
| `0f000a5` | Creator folder: rename influencer→creator, split masters, strip scaffolding | 33 changed (20 add, 11 del, 2 mod) |

**Current state:** ~159 files across GROWTH + E-COMMERCE, all FULL SCHEMA, zero partial, zero missing.

## Patterns & Decisions

- **Duplicate content:** When two files cover the same topic (e.g., 6_4 and 6_5 in E-COMMERCE), merge into one Reference doc and delete the duplicate
- **Taxonomy documents:** Follow the `00_Affiliate.md` pattern — top-level overview with Core Frameworks and Key Capability Areas sections
- **Landing pages:** Minimal content with `sticker:` field preserved, linking to taxonomy and index
- **Root files per folder:** Typically 3 — taxonomy (`00_*.md`), landing page (`FOLDER.md`), and navigation index (`index.md`)
- **Agent batching:** Process 3 folders in parallel per batch to avoid rate limits; agents get ~12 tool uses before hitting limits
- **Linter auto-modifications:** Obsidian linter strips quotes from YAML values and adds `sticker:` field — these are intentional user-side changes
- **Creator terminology rename:** "Influencer" → "creator" in general usage across Creator/ folder. Keep "influencer" in: IRM (Influencer Relationship Management) as established compound term, legal/regulatory references (FTC), historical contexts (pre-creator economy era). ~60% of occurrences replaced.
- **Creator folder structure:** 3 master files (irm-with-ai.md 102KB, influencer-identification.md 46KB, predicting-influencer-performance.md 49KB) split into 12 individual files. 8 files renamed from influencer-* to creator-*. Total: 22 files (20 Reference + 1 taxonomy + 1 index)

## User Defined Namespaces

- [Leave blank - user populates]

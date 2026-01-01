---
title: Master Hub Schema
id: SIE/E-1.2
version: "1.3"
steward: Adam Bernard
updated: 2025-12-29
status: Active
doc_type: system_schema
semantic_summary: Defines the required metadata (YAML frontmatter) and content structure for all documents within the Master Hub. This schema ensures data consistency, operational integrity, AI-readiness, and SEO optimization.
tags:
  - engine
  - schema
  - validation
  - structure
relations:
  - SIE/01 Engine/01_governance-rules.md
  - SIE/02 Strategy/Project Structure Guide.md
aliases:
  - Hub Schema
  - Schema Definition
---

## 0. Preamble

This document defines the official data schema for all Markdown files within a client's **Master Hub**. The **Strategic Intelligence Engine (SIE)** uses this schema to govern, validate, and process information. Adherence to this schema is mandatory to ensure the system can correctly categorize, retrieve, and reason with intelligence assets, as outlined in **Rule I-02**.

## 1. Global Properties (Required in All Files)

Every `.md` file in the Master Hub **must** contain the following properties in its YAML frontmatter.

| Property | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `title` | `String` | The primary, human-readable title of the document. | `"Core Vision & Mission"` |
| `id` | `String` | A unique, machine-readable identifier. Convention: `[System]/[Type]/[Name]` | `"SIE/S-00"` |
| `version` | `String` | The semantic version number of the document (e.g., "1.0", "1.1"). | `"1.0"` |
| `steward` | `String` | The name of the person or system responsible for the document's accuracy. | `"Adam Bernard"` |
| `updated` | `YYYY-MM-DD` | The date the document was last meaningfully updated. | `"2025-12-28"` |
| `status` | `Enum` | The current lifecycle status. Must be one of: `Draft`, `Active`, `Superseded`, `Archived`. | `"Active"` |
| `doc_type` | `Enum` | The type of document. See Section 2 for the approved list. | `"core_strategy"` |
| `summary` | `String` | A concise, one-sentence summary of the document's purpose. | `"Defines the vision for the SIE..."` |
| `tags` | `Array<String>` | A list of keywords for categorization and search. All lowercase. | `["strategy", "vision"]` |
| `relations` | `Array<String>` | A list of `id`s or filenames of directly related documents. | `["SIE/E-01"]` |
| `aliases` | `Array<String>` | A list of alternative names for easier linking and search. | `["SIE Strategy"]` |

## 2. Document Types (`doc_type`)

The `doc_type` property determines which validation rules and specific metadata fields apply.

-   **`core_strategy`**: High-level business, brand, or product strategy documents.
-   **`system_rules`**: Governance, protocols, and operational rules for the Engine.
-   **`product_spec`**: Detailed specifications for a product or service offering.
-   **`SOP`**: Standard Operating Procedures for internal processes.
-   **`Reference`**: Foundational knowledge, glossaries, or fact sheets.
-   **`Meeting_Note`**: Records of strategic meetings or decisions.

## 3. Domain-Specific Properties

Depending on the `doc_type`, additional properties are required to structure the content effectively.

### `doc_type: core_strategy`
-   **Purpose:** Defines the high-level business or product strategy.
-   **Required Sections:**
    -   `## Executive Summary`
    -   `## Section I: Core Identity & Market Position`
    -   `## Section II: The Unfair Advantage`
    -   `## Section III: The Opportunity & Solution`

### `doc_type: system_rules`
-   **Purpose:** Defines operational rules for the Engine.
-   **Required Sections:**
    -   `## 0. Preamble`
    -   `## 1. General Governance Principles`
    -   `## 2. Ingestion & Structuring Rules`

### `doc_type: product_spec`
-   **Purpose:** Describes a product or service offering.
-   **Required Properties (YAML):**
    -   `offering_name: String`
    -   `target_icp: String` (Relates back to ICP definitions)
    -   `price_point: String`
-   **Required Sections:**
    -   `## 1. Offering Summary`
    -   `## 2. Key Features & Benefits`
    -   `## 3. Pricing Details`

## 4. Operational & Access Control Metadata

These properties are recommended for `SOP`, `product_spec`, and `core_strategy` documents to manage visibility and usage.

| Property | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `target_audience` | `Enum` | The intended user. `Executive`, `Manager`, `All_Staff`, `Client`. | `"Executive"` |
| `security_level` | `Enum` | Access control. `Public`, `Internal`, `Confidential`, `Restricted`. | `"Confidential"` |
| `owner_team` | `String` | The specific department or team that owns this asset. | `"Product"` |

## 5. AI & RAG Enhancement Metadata

These optional but highly recommended fields improve the accuracy of AI-powered search, retrieval, and reasoning (RAG).

| Property | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `semantic_summary` | `String` | A 2-3 sentence abstract optimized for vector embedding. | `"This document outlines the pricing tier logic..."` |
| `synthetic_questions` | `Array<String>` | A list of questions this document is designed to answer. | `["How do we price enterprise deals?"]` |
| `key_concepts` | `Array<String>` | Abstract concepts or entities discussed in the document. | `["recurring revenue", "churn"]` |

## 6. SEO & Publication Metadata

These properties are **required** for public-facing documents (e.g., Blog Posts, Public Knowledge Base) and **optional** for internal documentation.

| Property | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `primary_keyword` | `String` | The main search term the document targets. | `"generative ai strategy"` |
| `seo_title` | `String` | Optional override for the HTML title tag. **Must include the `primary_keyword`.** | `"Generative AI Strategy: A Complete Guide"` |
| `meta_description` | `String` | A concise summary for search results. **Max 120 chars. Must include `primary_keyword`.** | `"A complete guide to generative AI strategy for enterprise leaders."` |
| `excerpt` | `String` | A short teaser for blog rolls. **Max 50 words. Must include `primary_keyword`.** | `"Discover the 3 pillars of a successful generative AI strategy..."` |
| `cover_image` | `String` | The file path or URL for the featured image. | `"assets/img/strategy-cover.jpg"` |

### 6.1 SEO Content Standards

For documents intended for public publication, the body content must adhere to the following structural rules to ensure search visibility and engagement.

1.  **Keyword Placement**:
    *   **Title**: The `primary_keyword` must appear in the `seo_title` (or main `title` if no override exists).
    *   **Introduction**: The `primary_keyword` must appear in the first paragraph (beginning of content).
    *   **Headings**: The `primary_keyword` must be used in at least one subheading (H2, H3, or H4).
    *   **Body**: The `primary_keyword` must appear naturally throughout the content.
2.  **Keyword Density**: Aim for approximately **1%** keyword density.
3.  **Length**: Content must be a minimum of **600 words**.
4.  **Linking Strategy**:
    *   **External**: Include DoFollow links pointing to authoritative external resources.
    *   **Internal**: Include links to other relevant documents within the Master Hub.

## 7. Example Implementation

Here is a complete example for a **Product Specification**, demonstrating how the schema properties work together.

```yaml
---
title: "SIE Enterprise Tier Specification"
id: "SIE/Products/P-Ent-01"
version: "2.0"
steward: "Sarah Jenkins"
updated: "2025-10-15"
status: "Active"
doc_type: "product_spec"
summary: "Detailed specification for the Enterprise tier of the Strategic Intelligence Engine."
tags: ["product", "enterprise", "pricing", "specs"]
aliases: ["Enterprise Spec", "Ent Tier"]

# --- Domain Specifics ---
offering_name: "SIE Enterprise"
target_icp: "Fortune 500 CTOs"
price_point: "Custom / Annual Contract"

# --- Operational Metadata ---
target_audience: "Sales_Engineering"
security_level: "Internal"
owner_team: "Product_Mgmt"

# --- AI & RAG Enhancement ---
semantic_summary: >
  The SIE Enterprise Tier includes full API access, unlimited vector storage, 
  and dedicated support. It is designed for organizations requiring custom 
  integrations and high-volume data processing.
  
synthetic_questions:
  - "What features are exclusive to the Enterprise tier?"
  - "Does the Enterprise tier include API access?"
  - "What is the pricing model for Enterprise clients?"

key_concepts:
  - "API Access"
  - "Vector Storage"
  - "SLA"

# --- SEO & Publication ---
primary_keyword: "enterprise ai platform"
seo_title: "Enterprise AI Platform: SIE Tier Specification"
meta_description: "The SIE Enterprise AI platform offers unlimited vector storage and dedicated support for high-volume organizations."
excerpt: "Explore the full capabilities of the SIE Enterprise AI platform, designed for Fortune 500 scale."
cover_image: "assets/images/sie-enterprise-cover.png"
---
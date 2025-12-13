---
title: "SIE: Core Concepts & Engine Architecture"
id: "kb/CORE/index"
version: "1.0"
steward: "Adam Bernard"
updated: "2025-11-28"
status: "Active"
doc_type: "context_index"
summary: "The master index for the CORE knowledge base, which defines the foundational concepts, architecture, and strategic principles of the Strategic Intelligence Engine (SIE)."
tags:
  - index
  - core
  - sie-engine
  - knowledge-base
  - ai-architecture
  - table-of-contents
relations:
  - "SIE/index"
---

# ⚙️ CORE: Engine Architecture & Foundational Concepts

Welcome to the central repository for the foundational documents that define the **Strategic Intelligence Engine (SIE)**. This section contains the technical and strategic pillars that explain how the SIE's knowledge base (the **Master Hub**) is constructed, maintained, and activated.

These documents serve as the primary reference for understanding the "what, why, and how" behind the engine that transforms scattered information into a living, intelligent asset.

---

## Core Concepts

This section details the technical building blocks and fundamental techniques that power the SIE's ability to understand and process information.

```dataview
<dataview_block> <query_type>dataview</query_type> <original_query> TABLE WITHOUT ID file.link as "Topic", summary as "Description" FROM "kb/CORE/Core Concepts" WHERE file.name != "index.md" SORT file.name ASC </original_query> <executed_result>
```

| Topic                                                                     | Description                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[00_anatomy]]                            | Defines the architecture and components of the knowledge base (the Master Hub) that powers the Strategic Intelligence Engine's (SIE) agents, enabling them to perform complex reasoning and automated tasks with high accuracy and context.     |
| [[01_model-context-protocol-mcp]]         | Defines the Model Context Protocol (MCP) as an emerging standard for how AI agents connect to and retrieve information from knowledge sources, tools, and other agents, ensuring interoperability and scalability for the SIE.                  |
| [[02_advanced-retrieval-techniques]]      | Explores advanced methods beyond standard RAG for providing AI agents with precise, governed, and contextually-aware information from a knowledge base, enhancing their reasoning and decision-making capabilities.                             |
| [[03_the-data-moat]]                      | Defines a 'Data Moat' as a defensible competitive advantage built from proprietary data, and explains how the Strategic Intelligence Engine (SIE) is designed to construct and activate this critical asset for clients.                        |
| [[04_retrieval-augmented-generation-rag]] | Explains Retrieval-Augmented Generation (RAG), the core technique used by the Strategic Intelligence Engine (SIE) to provide agents with real-time, factual context from the Master Hub, enhancing the accuracy and relevance of their outputs. |
| [[05_vector-databases]]                   | Explains what Vector Databases are and their critical role in enabling semantic search for the SIE's RAG pipelines, allowing agents to find information based on meaning rather than keywords.                                                  |
</executed_result>
</dataview_block>


---

## Strategy & Application

This section explains how the core concepts are applied strategically to build and leverage the Master Hub as a competitive advantage.

```dataview
<dataview_block>
<query_type>dataview</query_type>
<original_query>
TABLE WITHOUT ID
  file.link as "Topic",
  summary as "Description"
FROM "kb/CORE/Strategy & Application"
WHERE file.name != "index.md"
SORT file.name ASC
</original_query>
<executed_result>
```

| Topic                                     | Description                                                                                                                                                                                                                                 |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[Anatomy of an AI agent knowledge base]] | Defines the architecture and components of the knowledge base (the Master Hub) that powers the Strategic Intelligence Engine's (SIE) agents, enabling them to perform complex reasoning and automated tasks with high accuracy and context. |
</executed_result>
</dataview_block>



```dataviewjs 
const pages = dv.pages('"CORE"')
    .where(p => p.file.name === "index" && p.file.folder !== "kb")
    .sort(p => p.file.folder);

// Group by first-level folder
const grouped = {};
for (let page of pages) {
    const parts = page.file.folder.split('/');
    
    // Skip if deeper than 3 parts
    if (parts.length > 3) continue;
    
    const firstLevel = parts[1];
    
    if (!firstLevel) continue;
    
    if (!grouped[firstLevel]) {
        grouped[firstLevel] = [];
    }
    grouped[firstLevel].push(page);
}

// Display grouped results
let isFirst = true;
for (let [firstLevel, subPages] of Object.entries(grouped).sort()) {
    if (!firstLevel || firstLevel === 'undefined') continue;
    
    // Only display if there's actually a top-level index
    const topLevelIndex = subPages.find(p => p.file.folder === `CORE/${firstLevel}`);
    
    // Skip this entire group if there's no top-level index
    if (!topLevelIndex) continue;
    
    if (!isFirst) {
        dv.el("hr", "");
    }
    isFirst = false;
    
    // Display top-level folder as linked header
    dv.el("h3", dv.fileLink(topLevelIndex.file.path, firstLevel));
    
    // Display ONLY direct subfolders
    const subfolders = subPages.filter(p => {
        const parts = p.file.folder.split('/');
        return parts.length === 3 && parts[2] && p.file.folder !== `CORE/${firstLevel}`;
    });
    
    if (subfolders.length > 0) {
        dv.list(
            subfolders.map(p => {
                const parts = p.file.folder.split('/');
                const folderName = parts[2];
                return dv.fileLink(p.file.path, folderName);
            })
        );
    }
}
```

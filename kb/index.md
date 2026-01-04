---
title: "Strategic Intelligence Engine"
type: cornerstone
status: active
tags: [hub, navigation, root]
description: "Central access point for The Bernard Group's knowledge assets, divided into Cognitive, Visibility, and Operational pillars."
---

# The Intelligence Engine

Welcome to the central nervous system of our operations. This Knowledge Base is organized into four strategic pillars designed to support decision-making, automation, and growth.

## 🧠 Pillar I: Cognitive Architecture (AI)
*Focus: Artificial Intelligence, Agents, and Model Context.*
We are building systems that think. This pillar covers the architecture of our AI agents, safety protocols, and prompt engineering strategies.
- **Key Hub:** [[kb/AI/index|AI & Agentic Systems]]
- **Latest Focus:** [[agentic-ai-safety-playbook]]

## 👁️ Pillar II: Organic Visibility (SEO)
*Focus: Search, Semantics, and GEO.*
We are building systems to be found. This pillar covers the transition from traditional SEO to Generative Engine Optimization.
- **Key Hub:** [[kb/SEO/index|Search & Visibility Strategy]]
- **Latest Focus:** [[geo-playbook]]

## ⚖️ Pillar III: Operational Governance
*Focus: Standards, Ethics, and Law.*
The rules that bind the system. This includes the "Bernard Firm Standards," metadata schemas, and compliance frameworks.
- **Key Hub:** [[kb/Governance/index|Governance & Standards]]
- **Latest Focus:** [[master-hub-schema]]

## 🛠️ Pillar IV: The Tech Stack
*Focus: Tools, Platforms, and Code.*
The instruments of execution. Documentation for Obsidian, WordPress, and our software supply chain.
- **Key Hub:** [[index_old|Technical Documentation]]

---

### 🗄️ Full Directory Access
*Direct access to the file directory structure.*


# Knowledge Base Contents

```dataviewjs
// Get all pages named "index" within the "kb" folder and its subdirectories,
// excluding the current index file itself.
const pages = dv.pages('"kb"')
    .where(p => p.file.name === "index" && p.file.path !== dv.current().file.path)
    .sort(p => p.file.folder);

// Group pages by their top-level category folder (e.g., "AI", "SEO").
const categories = {};
for (let page of pages) {
    // Path parts: e.g., "kb/AI/3_methods" -> ["kb", "AI", "3_methods"]
    const pathParts = page.file.folder.split('/');
    
    // The category is the first folder inside "kb"
    const categoryName = pathParts[1];
    
    if (!categoryName) continue; // Skip if the file is directly in "kb"
    
    if (!categories[categoryName]) {
        categories[categoryName] = [];
    }
    categories[categoryName].push(page);
}

// Render the grouped list.
let isFirstCategory = true;
for (let categoryName of Object.keys(categories).sort()) {
    const subPages = categories[categoryName];
    
    // Find the main index file for this category, e.g., "kb/AI/index.md"
    const categoryIndexPage = subPages.find(p => p.file.folder === `kb/${categoryName}`);
    
    // If a main index file for the category doesn't exist, skip this category.
    if (!categoryIndexPage) continue;
    
    // Add a horizontal rule between categories.
    if (!isFirstCategory) {
        dv.el("hr", "");
    }
    isFirstCategory = false;
    
    // Display the category name as a linked H3 header.
    dv.el("h3", dv.fileLink(categoryIndexPage.file.path, categoryName));
    
    // Find and list the index files of direct subfolders within this category.
    const subfolderPages = subPages.filter(p => {
        const pathParts = p.file.folder.split('/');
        // A subfolder index path will have 3 parts: ["kb", "Category", "Subfolder"]
        return pathParts.length === 3 && p.file.folder !== `kb/${categoryName}`;
    });
    
    if (subfolderPages.length > 0) {
        dv.list(
            subfolderPages.map(p => {
                const subfolderName = p.file.folder.split('/')[2];
                return dv.fileLink(p.file.path, subfolderName);
            })
        );
    }
}
```
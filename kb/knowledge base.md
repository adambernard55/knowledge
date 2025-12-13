---
title: Welcome to Our Knowledge Base
id: 20251206065828
version: 1
Author: Adam Bernard
steward:
date: 2025-12-06
category:
category_id:
Excerpt:
Meta Description:
Primary_Keyword:
Featured_Image:
doc_type: Overview
relations:
aliases:
last_updated: 2025-12-06
tags:
---

# Welcome to Our Knowledge Base

Welcome! This knowledge base is your central hub for information, guides, and resources. We've designed it to be a comprehensive, easy-to-navigate library to help you find the answers you need, quickly and efficiently.

### How to Navigate

Our content is organized into clear, high-level categories. The main sections are listed below, and you can click on any category to explore the specific topics and articles within it. Think of it as a digital library where each main heading is a bookshelf, and the links below it are the books on that shelf.

### What You'll Find Inside

Whether you're looking for step-by-step tutorials, strategic insights, or best practices, you'll find it here. We are constantly updating our articles to ensure you have the most current and relevant information at your fingertips.

Dive in and start exploring the categories below

# Knowledge Base Contents

```dataviewjs 
const pages = dv.pages('"kb"')
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
    const topLevelIndex = subPages.find(p => p.file.folder === `kb/${firstLevel}`);
    
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
        return parts.length === 3 && parts[2] && p.file.folder !== `kb/${firstLevel}`;
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
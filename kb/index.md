
# Welcome to Our Knowledge Base

Welcome! This knowledge base is your central hub for information, guides, and resources. We've designed it to be a comprehensive, easy-to-navigate library to help you find the answers you need, quickly and efficiently.

### How to Navigate

Our content is organized into clear, high-level categories. The main sections are listed below, and you can click on any category to explore the specific topics and articles within it. Think of it as a digital library where each main heading is a bookshelf, and the links below it are the books on that shelf.

### What You'll Find Inside

Whether you're looking for step-by-step tutorials, strategic insights, or best practices, you'll find it here. We are constantly updating our articles to ensure you have the most current and relevant information at your fingertips.

Dive in and start exploring the categories below

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
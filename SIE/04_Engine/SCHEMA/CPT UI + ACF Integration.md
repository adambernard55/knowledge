---
title: CPT UI + ACF Integration
id: 20251229071258
version: 1
Author: Adam Bernard
steward:
date: 2025-12-29
category:
category_id:
Excerpt:
Meta Description:
Primary_Keyword:
Featured_Image:
doc_type:
relations:
aliases:
last_updated: 2025-12-29
tags:
---

## CPT UI + ACF Integration: Existing Infrastructure

**Good news:** CPT UI and ACF are designed to work together seamlessly. They serve complementary roles:

- **CPT UI:** Defines post type structure (slug, labels, capabilities, taxonomies)
- **ACF:** Defines custom field architecture within those post types

Since Avada bundles **ACF Pro**, you already have the complete toolset installed.

---

## Implementation on adambernard.com

### 1. **Field Group Configuration via ACF**

Navigate to: `Custom Fields → Field Groups → Add New`

Create your semantic intelligence field group and set location rules to target your CPT UI post types:

**Location Rules:**

```
Post Type | is equal to | your_cpt_slug
OR
Post Type | is equal to | another_cpt_slug
OR
Post Type | is equal to | post
OR
Post Type | is equal to | page
```

This makes the fields appear on any combination of post types you specify.

---

### 2. **Field Definitions (Using ACF Pro Features)**

Since you have ACF Pro (bundled with Avada), you get these advantages:

**Semantic Summary Field:**

- Field Type: `Textarea`
- Field Name: `semantic_summary` (maps to your YAML)
- Instructions: "AI-generated contextual summary from Obsidian"
- Readonly: Yes (if only synced from GitHub, not manually edited)

**Synthetic Questions Field:**

- Field Type: `Repeater` (Pro feature)
- Field Name: `synthetic_questions`
- Sub-field: Text field named `question`
- Layout: Block or Table
- Min/Max rows: Set based on your typical YAML structure

**Key Concepts Field:**

- Field Type: `Repeater`
- Field Name: `key_concepts`
- Sub-field: Text field named `concept`
- Alternative: Use `Select` with "Allow Multiple" if concepts are from controlled vocabulary

---

### 3. **ACF JSON Sync (Critical for Your Workflow)**

Enable ACF's JSON sync feature to version control your field definitions:

**In your theme or plugin:**

```php
// Add to functions.php or custom plugin
add_filter('acf/settings/save_json', function($path) {
    return get_stylesheet_directory() . '/acf-json';
});

add_filter('acf/settings/load_json', function($paths) {
    unset($paths[0]);
    $paths[] = get_stylesheet_directory() . '/acf-json';
    return $paths;
});
```

**Benefits:**

- Field definitions stored as JSON files in your theme
- Version controlled in Git
- Auto-sync across environments
- Faster field group loading

---

### 4. **REST API Exposure (For GitHub Actions)**

ACF Pro automatically exposes fields in REST API when you enable this:

**Per Field Group Settings:**

- Navigate to field group settings
- Set "Show in REST API" to `Yes`

**Or programmatically:**

```php
add_filter('acf/rest_api/your_field_group_key/get_fields', '__return_true');
```

This makes your semantic fields accessible via:

```
GET /wp-json/wp/v2/your_cpt_slug/123
```

Response includes:

```json
{
  "id": 123,
  "title": {...},
  "content": {...},
  "acf": {
    "semantic_summary": "...",
    "synthetic_questions": [
      {"question": "..."},
      {"question": "..."}
    ],
    "key_concepts": [
      {"concept": "..."},
      {"concept": "..."}
    ]
  }
}
```

---

### 5. **GitHub Actions Update for ACF Structure**

Your sync workflow needs to map YAML arrays to ACF's repeater structure:

```bash
# Transform YAML arrays to ACF repeater format
synthetic_questions=$(yq eval '.synthetic_questions[]' "$file" | jq -R -s -c '
  split("\n")[:-1] | 
  map(select(length > 0)) | 
  map({question: .})
')

key_concepts=$(yq eval '.key_concepts[]' "$file" | jq -R -s -c '
  split("\n")[:-1] | 
  map(select(length > 0)) | 
  map({concept: .})
')

# POST to WordPress REST API
curl -X POST "$WP_URL/wp-json/wp/v2/your_cpt_slug" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"title\": \"$title\",
    \"content\": \"$content\",
    \"acf\": {
      \"semantic_summary\": \"$semantic_summary\",
      \"synthetic_questions\": $synthetic_questions,
      \"key_concepts\": $key_concepts
    }
  }"
```

---

### 6. **Avada-Specific Considerations**

**Fusion Builder Compatibility:**

- ACF fields display in Avada's admin interface without conflicts
- You can use ACF shortcodes in Fusion Builder: `[acf field="semantic_summary"]`
- Create Fusion Builder elements that pull ACF data

**Performance:**

- Avada already loads ACF, no additional overhead
- ACF data cached with Avada's caching system
- No conflicts with Avada's custom fields

---
### Update Note

>> Since you are syncing high-value content like "Semantic Summaries," "Key Concepts," and "Synthetic Questions" from Obsidian, you likely want to display them as special sections on your posts (e.g., a "Key Takeaways" box at the top of an article).

#### Here is how Avada specifically handles this: 

### 1. The "No-Code" Way (Avada Layouts)

You don't actually need to write the PHP code shown in the note if you use Avada's **Layout Builder**.

- **Dynamic Data:** When building a Single Post Layout in Avada, you can add a Text Block or Title element.
- **Connect to ACF:** In the element settings, click the "Dynamic Data" icon (the database stack symbol).
- **Select Field:** Choose **ACF** from the list and select `semantic_summary` or `key_concepts`.
- **Result:** Avada will automatically pull the text from that field and display it on every post that uses that layout.

### 2. The "Shortcode" Way

If you are writing a standard post using the Fusion Builder and want to insert a field in the middle of the content manually, you can use the shortcode:  
`[acf field="semantic_summary"]`

### 3. Hidden Utility (SEO & Schema)

While the section focuses on display, you can also use these fields _without_ displaying them visually, for example:

- **Meta Tags:** Mapping the `semantic_summary` to your SEO plugin's meta description.
- **Schema Markup:** Injecting `key_concepts` into JSON-LD schema for Google to read, even if the user doesn't see a list on the screen.

---

**Theme Integration:** Display semantic fields in your Avada templates:

```php
// In single.php or custom template
<?php if (get_field('semantic_summary')) : ?>
    <div class="semantic-summary">
        <h3>Context Summary</h3>
        <?php the_field('semantic_summary'); ?>
    </div>
<?php endif; ?>

<?php if (have_rows('key_concepts')) : ?>
    <div class="key-concepts">
        <h3>Key Concepts</h3>
        <ul>
        <?php while (have_rows('key_concepts')) : the_row(); ?>
            <li><?php the_sub_field('concept'); ?></li>
        <?php endwhile; ?>
        </ul>
    </div>
<?php endif; ?>
```

---

## Migration Strategy for Existing CPT UI Post Types

### Phase 1: Field Group Setup

1. Create ACF field groups via admin UI
2. Export to JSON for version control
3. Test on staging environment

### Phase 2: Bulk Import Existing Data

```php
// WP-CLI command or admin script
function wpjet_backfill_semantic_fields() {
    $posts = get_posts([
        'post_type' => ['your_cpt_slug', 'post', 'page'],
        'posts_per_page' => -1,
        'post_status' => 'publish'
    ]);
    
    foreach ($posts as $post) {
        // If you have legacy meta or need to regenerate
        // This is where you'd pull from vector DB or re-process
        
        // Example: migrating from old meta keys
        $old_summary = get_post_meta($post->ID, 'old_summary_key', true);
        if ($old_summary) {
            update_field('semantic_summary', $old_summary, $post->ID);
        }
    }
}
```

### Phase 3: Update GitHub Actions

- Modify your workflow to use ACF structure
- Test sync with a few posts
- Enable for full production sync

---

## Operational Checklist

**Immediate Actions:**

- [ ] Document your CPT UI slugs (which post types need these fields?)
- [x] Create ACF field group via admin UI ✅ 2025-12-29
- [x] Enable "Show in REST API" for the field group ✅ 2025-12-29
- [x] Test manual entry of semantic fields on one post ✅ 2025-12-29
- [x] Export ACF JSON to your theme directory ✅ 2025-12-29

**GitHub Workflow Updates:**

- [ ] Update YAML parsing to format for ACF repeater structure
- [ ] Test POST/PUT with new ACF field structure
- [ ] Verify field data appears in WordPress admin
- [ ] Validate REST API response includes ACF data

**Integration Testing:**

- [ ] Confirm fields display in post editor for all targeted post types
- [ ] Test Avada Fusion Builder compatibility
- [ ] Verify no conflicts with existing Avada fields
- [ ] Check page load performance with new fields

---

## Advantages of This Stack

**You're in an optimal position:**

- ACF Pro already licensed through Avada
- CPT UI provides clean, maintainable post type definitions
- Both tools designed for exactly this use case
- REST API integration is built-in
- Field data portable for vector DB ingestion

**No conflicts exist between:**

- CPT UI and ACF
- Avada and ACF (same codebase)
- Your GitHub Actions workflow and this approach

---

Would you like me to:

1. Create the specific ACF field group configuration for your exact YAML structure?
2. Detail the GitHub Actions modifications for your current workflow?
3. Build a migration script for any existing post data?
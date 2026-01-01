---
title: System Architecture
id: 20251229064605
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

## System Architecture for Extended YAML Fields in WordPress

### Core Data Layer: Custom Fields Architecture

You need a unified custom field system that works consistently across all post types. Here are your two primary approaches:

**Option 1: Advanced Custom Fields (ACF) - Recommended for Your Use Case**

Creates a standardized meta field structure that's:

- Query-able via WP_Query and REST API
- Exportable/importable via JSON
- Compatible with your existing GitHub Actions workflow
- Accessible to Rank Math for schema integration

**Option 2: Native Custom Meta Tables**

Direct `wp_postmeta` storage with custom meta boxes. More control, but requires more maintenance code.

---

## Implementation Framework

### 1. **Field Definition Layer**

```php
// Register meta fields for all relevant post types
function wpjet_register_semantic_fields() {
    $post_types = ['post', 'page', 'your_cpt_name'];
    
    foreach ($post_types as $post_type) {
        register_post_meta($post_type, 'semantic_summary', [
            'type' => 'string',
            'description' => 'AI-generated semantic summary',
            'single' => true,
            'show_in_rest' => true,
            'sanitize_callback' => 'sanitize_textarea_field'
        ]);
        
        register_post_meta($post_type, 'synthetic_questions', [
            'type' => 'array',
            'description' => 'Generated questions for context',
            'single' => true,
            'show_in_rest' => [
                'schema' => [
                    'type' => 'array',
                    'items' => ['type' => 'string']
                ]
            ],
            'sanitize_callback' => 'wpjet_sanitize_array'
        ]);
        
        register_post_meta($post_type, 'key_concepts', [
            'type' => 'array',
            'description' => 'Extracted key concepts/entities',
            'single' => true,
            'show_in_rest' => [
                'schema' => [
                    'type' => 'array',
                    'items' => ['type' => 'string']
                ]
            ],
            'sanitize_callback' => 'wpjet_sanitize_array'
        ]);
    }
}
add_action('init', 'wpjet_register_semantic_fields');

function wpjet_sanitize_array($value) {
    if (!is_array($value)) {
        return [];
    }
    return array_map('sanitize_text_field', $value);
}
```

---

### 2. **GitHub Actions Sync Integration Layer**

Extend your existing YAML→WordPress pipeline to parse and map these fields:

```bash
# In your sed processing or YAML parser
# Extract new fields from frontmatter
semantic_summary=$(yq eval '.semantic_summary' "$file")
synthetic_questions=$(yq eval '.synthetic_questions[]' "$file" | jq -R -s -c 'split("\n")[:-1]')
key_concepts=$(yq eval '.key_concepts[]' "$file" | jq -R -s -c 'split("\n")[:-1]')

# Add to your WordPress REST API POST/PUT request
curl -X POST "$WP_URL/wp-json/wp/v2/posts" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"title\": \"$title\",
    \"content\": \"$content\",
    \"meta\": {
      \"semantic_summary\": \"$semantic_summary\",
      \"synthetic_questions\": $synthetic_questions,
      \"key_concepts\": $key_concepts
    }
  }"
```

---

### 3. **Admin Interface Layer (Optional but Recommended)**

ACF Field Group configuration:

```php
// ACF JSON export - place in /acf-json/ folder
{
  "key": "group_semantic_intelligence",
  "title": "Semantic Intelligence Fields",
  "fields": [
    {
      "key": "field_semantic_summary",
      "label": "Semantic Summary",
      "name": "semantic_summary",
      "type": "textarea",
      "instructions": "AI-generated contextual summary"
    },
    {
      "key": "field_synthetic_questions",
      "label": "Synthetic Questions",
      "name": "synthetic_questions",
      "type": "repeater",
      "sub_fields": [
        {
          "key": "field_question",
          "label": "Question",
          "name": "question",
          "type": "text"
        }
      ]
    },
    {
      "key": "field_key_concepts",
      "label": "Key Concepts",
      "name": "key_concepts",
      "type": "repeater",
      "sub_fields": [
        {
          "key": "field_concept",
          "label": "Concept",
          "name": "concept",
          "type": "text"
        }
      ]
    }
  ],
  "location": [
    [
      {
        "param": "post_type",
        "operator": "==",
        "value": "post"
      }
    ],
    [
      {
        "param": "post_type",
        "operator": "==",
        "value": "page"
      }
    ]
  ]
}
```

---

### 4. **Query & Retrieval Layer**

Enable efficient vector database population and semantic search:

```php
// Batch export for vector DB ingestion
function wpjet_export_semantic_data($post_types = ['post', 'page']) {
    $posts = get_posts([
        'post_type' => $post_types,
        'posts_per_page' => -1,
        'post_status' => 'publish'
    ]);
    
    $export = [];
    foreach ($posts as $post) {
        $export[] = [
            'id' => $post->ID,
            'title' => $post->post_title,
            'content' => $post->post_content,
            'semantic_summary' => get_post_meta($post->ID, 'semantic_summary', true),
            'synthetic_questions' => get_post_meta($post->ID, 'synthetic_questions', true),
            'key_concepts' => get_post_meta($post->ID, 'key_concepts', true),
            'url' => get_permalink($post->ID)
        ];
    }
    
    return $export;
}
```

---

### 5. **Schema Markup Integration (Rank Math)**

Add semantic fields to your schema output:

```php
add_filter('rank_math/json_ld', function($data, $jsonld) {
    if (is_singular()) {
        $post_id = get_the_ID();
        $semantic_summary = get_post_meta($post_id, 'semantic_summary', true);
        $key_concepts = get_post_meta($post_id, 'key_concepts', true);
        
        if (!empty($semantic_summary)) {
            $data['description'] = $semantic_summary;
        }
        
        if (!empty($key_concepts)) {
            $data['keywords'] = implode(', ', $key_concepts);
        }
    }
    return $data;
}, 10, 2);
```

---

## Operational Considerations

**Data Integrity:**

- Add validation rules in your GitHub Actions workflow before sync
- Implement rollback mechanism for failed imports
- Log all meta updates for audit trail

**Performance:**

- These fields are indexed automatically via `wp_postmeta`
- For high-volume queries, consider dedicated lookup table
- Cache semantic data in transients for frequently accessed posts

**Migration Path:**

- Export existing posts via WP-CLI: `wp post list --format=json`
- Backfill semantic fields via batch processing
- Maintain backward compatibility with posts lacking these fields

**Monitoring:**

- Track sync success rate in GitHub Actions logs
- Monitor meta query performance via Query Monitor
- Set up alerts for missing semantic data on published posts

---

## Next Steps

1. **Define your post type scope** - Which CPTs need these fields?
2. **Choose ACF vs native** - ACF recommended for UI + REST API integration
3. **Update GitHub Actions workflow** - Extend YAML parsing to include new fields
4. **Test sync pipeline** - Validate YAML → WP meta field mapping
5. **Implement retrieval layer** - Export endpoint for vector DB population

Would you like me to detail any specific component of this architecture, or help you build the GitHub Actions workflow extension?
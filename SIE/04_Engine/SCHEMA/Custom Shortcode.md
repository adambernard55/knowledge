---
title: Custom Shortcode
id: 20251231074531
version: 1
Author: Adam Bernard
steward:
date: 2025-12-31
category:
category_id:
Excerpt:
Meta Description:
Primary_Keyword:
Featured_Image:
doc_type:
relations:
aliases:
last_updated: 2025-12-31
tags:
---

### Custom Shortcode

This two-step process will create a new shortcode `[ai_intelligence_box]` that you can paste anywhere, and it will handle the logic and styling perfectly.

#### Step 1: Add this to your `functions.php`

_You can find this in Appearance > Theme File Editor > functions.php, or use a plugin like "Code Snippets"._

```php
function render_ai_intelligence_box() {
    // Get the current post ID
    $post_id = get_the_ID();

    // Check if the summary exists to avoid printing empty boxes
    if ( ! get_field('semantic_summary', $post_id) ) {
        return ''; 
    }

    ob_start(); // Start recording output
    ?>
    
    <div class="ai-box" style="background-color: #f8f9fa; border: 1px solid #e2e8f0; border-left: 5px solid #2271b1; padding: 25px; border-radius: 4px; margin: 30px 0;">
        <h3 style="margin-top: 0; margin-bottom: 20px; font-size: 1.4em;">🤖 AI Intelligence Brief</h3>

        <!-- Semantic Summary -->
        <div style="margin-bottom: 20px;">
            <h4 style="margin: 0 0 10px 0; font-size: 1.1em;">📝 Context Summary</h4>
            <div style="font-style: italic; line-height: 1.6;">
                <?php echo get_field('semantic_summary', $post_id); ?>
            </div>
        </div>

        <div style="display: flex; flex-wrap: wrap; gap: 20px;">
            
            <!-- Key Concepts -->
            <?php if( have_rows('key_concepts', $post_id) ): ?>
                <div style="flex: 1; min-width: 250px;">
                    <h4 style="margin: 0 0 10px 0; font-size: 1.1em;">🔑 Key Concepts</h4>
                    <ul style="margin: 0; padding-left: 20px;">
                    <?php while( have_rows('key_concepts', $post_id) ): the_row(); ?>
                        <li style="margin-bottom: 5px;"><?php the_sub_field('concept'); ?></li>
                    <?php endwhile; ?>
                    </ul>
                </div>
            <?php endif; ?>

            <!-- Synthetic Questions -->
            <?php if( have_rows('synthetic_questions', $post_id) ): ?>
                <div style="flex: 1; min-width: 250px;">
                    <h4 style="margin: 0 0 10px 0; font-size: 1.1em;">❓ Synthetic Questions</h4>
                    <ul style="margin: 0; padding-left: 20px;">
                    <?php while( have_rows('synthetic_questions', $post_id) ): the_row(); ?>
                        <li style="margin-bottom: 5px;"><?php the_sub_field('question'); ?></li>
                    <?php endwhile; ?>
                    </ul>
                </div>
            <?php endif; ?>
            
        </div>
    </div>

    <?php
    return ob_get_clean(); // Return the recorded output
}
add_shortcode('ai_intelligence_box', 'render_ai_intelligence_box');
```

#### Step 2: Paste this Shortcode on your Page

Now, go back to your Avada Builder (or any page editor) and simply paste this shortcode into a **Text Block** or **Code Block**:

```
[ai_intelligence_box]
```
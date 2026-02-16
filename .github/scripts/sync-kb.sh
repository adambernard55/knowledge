#!/bin/bash
set -e

# Media cache for featured images
declare -A MEDIA_CACHE

# Function: Sideload image from URL to WordPress
sideload_image() {
  local image_url="$1"
  local post_title="$2"
  
  local filename=$(basename "$image_url" | cut -d'?' -f1 | sed 's/[^a-zA-Z0-9._-]/_/g')
  local temp_file="/tmp/wp_sideload_$(date +%s)_$filename"
  
  if ! curl -s -L -f -o "$temp_file" "$image_url" 2>/dev/null; then
    echo "0"
    return 1
  fi
  
  local mime_type=$(file -b --mime-type "$temp_file" 2>/dev/null || echo "image/jpeg")
  
  local response=$(curl -s -X POST \
    -H "Authorization: Basic $auth_header" \
    -H "Content-Type: $mime_type" \
    -H "Content-Disposition: attachment; filename=$filename" \
    --data-binary "@$temp_file" \
    "$WP_URL/wp-json/wp/v2/media")
  
  local media_id=$(echo "$response" | jq -r '.id // empty')
  
  rm -f "$temp_file"
  
  if [ ! -z "$media_id" ] && [ "$media_id" != "null" ]; then
    echo "$media_id"
  else
    echo "0"
  fi
}

# Function: Get files to process based on trigger type
get_files_to_process() {
  if [ "$TRIGGER_EVENT" == "workflow_dispatch" ]; then
    echo "Manual trigger detected - processing ALL files in kb/"
    find kb -name "*.md" -type f
  else
    echo "Push event detected - processing changed files only"
    echo "$CHANGED_FILES" | sed 's/\\n/\n/g'
  fi
}

# Function: Determine topic ID from file path
get_topic_id() {
  local file="$1"
  local topic_id=$DEFAULT_TOPIC_ID
  
  case "$file" in
    *"/AI/0_fundamentals/"*) topic_id=1186 ;;
    *"/AI/1_models/specific-models/"*) topic_id=1779 ;;
    *"/AI/1_models/concepts-and-techniques/"*) topic_id=1780 ;;
    *"/AI/1_models/evaluation-and-tooling/"*) topic_id=1781 ;;
    *"/AI/1_models/comparisons/"*) topic_id=1782 ;;
    *"/AI/1_models/"*) topic_id=1187 ;;
    *"/AI/2_agents/toolkits/"*) topic_id=1783 ;;
    *"/AI/2_agents/"*) topic_id=1188 ;;
    *"/AI/3_methods/mcp/"*) topic_id=1784 ;;
    *"/AI/3_methods/"*) topic_id=1189 ;;
    *"/AI/4_applications/business/"*) topic_id=1785 ;;
    *"/AI/4_applications/"*) topic_id=1190 ;;
    *"/AI/5_ethics-and-governance/"*) topic_id=1191 ;;
    *"/AI/6_future-trends/"*) topic_id=1192 ;;
    *"/AI/7_marketing/Affiliate/"*) topic_id=2268 ;;
    *"/AI/7_marketing/E-commerce/"*) topic_id=2269 ;;
    *"/AI/7_marketing/Influencer/"*) topic_id=2270 ;;
    *"/AI/7_marketing/Social Media/"*) topic_id=2271 ;;
    *"/AI/7_marketing/"*) topic_id=1786 ;;
    *"/AI/"*) topic_id=1159 ;;
    *"/SEO/0_fundamentals/"*) topic_id=1162 ;;
    *"/SEO/1_research-and-strategy/"*) topic_id=1163 ;;
    *"/SEO/2_content-and-on-page/"*) topic_id=1164 ;;
    *"/SEO/3_technical-seo/"*) topic_id=1165 ;;
    *"/SEO/4_ai-and-automation/using-ai-for-seo/"*) topic_id=1787 ;;
    *"/SEO/4_ai-and-automation/optimizing-for-ai/"*) topic_id=1788 ;;
    *"/SEO/4_ai-and-automation/"*) topic_id=1166 ;;
    *"/SEO/5_measurement-and-optimization/"*) topic_id=1167 ;;
    *"/SEO/6_future-trends/"*) topic_id=1168 ;;
    *"/SEO/"*) topic_id=1158 ;;
    *"/TOOLS/marketing-automation/seo-optimization/"*) topic_id=1603 ;;
    *"/TOOLS/ai-foundation-models/"*) topic_id=1596 ;;
    *"/TOOLS/analytics-data-insights/"*) topic_id=1597 ;;
    *"/TOOLS/audio-generation/"*) topic_id=1598 ;;
    *"/TOOLS/coding-development/"*) topic_id=1599 ;;
    *"/TOOLS/content-creation/"*) topic_id=1600 ;;
    *"/TOOLS/image-video-generation/"*) topic_id=1601 ;;
    *"/TOOLS/marketing-automation/"*) topic_id=1602 ;;
    *"/TOOLS/productivity-workflow/"*) topic_id=1604 ;;
    *"/TOOLS/research-knowledge-agents/"*) topic_id=1605 ;;
    *"/TOOLS/social-media/"*) topic_id=1606 ;;
    *"/TOOLS/"*) topic_id=1160 ;;
    *"/CORE/core-concepts/"*) topic_id=1608 ;;
    *"/CORE/strategy-application/"*) topic_id=1609 ;;
    *"/CORE/"*) topic_id=1607 ;;
  esac
  
  echo "$topic_id"
}

# Function: Extract and process frontmatter using yq for proper YAML parsing
extract_frontmatter() {
  local file="$1"
  
  if ! grep -q "^---$" "$file"; then
    return 1
  fi
  
  # Use yq for robust YAML parsing (handles >, |, and all YAML features)
  fm_title=$(yq eval '.title // ""' "$file" 2>/dev/null)
  fm_excerpt=$(yq eval '.excerpt // .summary // ""' "$file" 2>/dev/null)
  fm_keyword=$(yq eval '.keyword // ""' "$file" 2>/dev/null)
  fm_meta_desc=$(yq eval '.meta_description // .meta-description // ""' "$file" 2>/dev/null)
  fm_semantic=$(yq eval '.semantic_summary // ""' "$file" 2>/dev/null)
  fm_image=$(yq eval '.featured_image // .coverimage // ""' "$file" 2>/dev/null)
  fm_updated=$(yq eval '.updated // ""' "$file" 2>/dev/null)
  fm_topic=$(yq eval '.topic // ""' "$file" 2>/dev/null)
  
  # Arrays - synthetic_questions
  if yq eval 'has("synthetic_questions")' "$file" 2>/dev/null | grep -q "true"; then
    fm_questions=$(yq eval '.synthetic_questions' "$file" 2>/dev/null | jq -c 'map({question: .})' 2>/dev/null || echo "[]")
    [ -z "$fm_questions" ] || [ "$fm_questions" = "null" ] && fm_questions="[]"
  else
    fm_questions="[]"
  fi
  
  # Arrays - key_concepts
  if yq eval 'has("key_concepts")' "$file" 2>/dev/null | grep -q "true"; then
    fm_concepts=$(yq eval '.key_concepts' "$file" 2>/dev/null | jq -c 'map({concept: .})' 2>/dev/null || echo "[]")
    [ -z "$fm_concepts" ] || [ "$fm_concepts" = "null" ] && fm_concepts="[]"
  else
    fm_concepts="[]"
  fi
  
  # Tags (can be array or comma-separated string)
  if yq eval 'has("tags")' "$file" 2>/dev/null | grep -q "true"; then
    if yq eval '.tags | type' "$file" 2>/dev/null | grep -q "!!seq"; then
      # It's an array - join with spaces
      fm_tags=$(yq eval '.tags | join(" ")' "$file" 2>/dev/null)
    else
      # It's a string - clean up brackets and commas
      fm_tags=$(yq eval '.tags // ""' "$file" 2>/dev/null | sed 's/[\[\],]/ /g')
    fi
  else
    fm_tags=""
  fi
  
  # Normalize and validate date format
  if [ ! -z "$fm_updated" ] && [ "$fm_updated" != "null" ]; then
    if normalized_date=$(date -d "$fm_updated" -Iseconds 2>/dev/null); then
      fm_updated="$normalized_date"
      # Remove milliseconds for WordPress compatibility
      fm_updated=$(echo "$fm_updated" | sed 's/\.[0-9]*+/+/' | sed 's/\.[0-9]*Z$/Z/')
    else
      echo "⚠ Invalid date format: $fm_updated"
      fm_updated=""
    fi
  else
    fm_updated=""
  fi
  
  # Fallback to git history if no valid frontmatter date
  if [ -z "$fm_updated" ]; then
    fm_updated=$(git log -1 --format="%aI" -- "$file" 2>/dev/null || echo "")
  fi
  
  # Clean up any "null" strings returned by yq
  [ "$fm_title" = "null" ] && fm_title=""
  [ "$fm_excerpt" = "null" ] && fm_excerpt=""
  [ "$fm_keyword" = "null" ] && fm_keyword=""
  [ "$fm_meta_desc" = "null" ] && fm_meta_desc=""
  [ "$fm_semantic" = "null" ] && fm_semantic=""
  [ "$fm_image" = "null" ] && fm_image=""
  [ "$fm_tags" = "null" ] && fm_tags=""
  [ "$fm_topic" = "null" ] && fm_topic=""
  
  return 0
}

# Function: Process tags and return JSON array
process_tags() {
  local tags="$1"
  
  if [ -z "$tags" ]; then
    echo "[]"
    return
  fi
  
  local tag_ids_array=()
  for tag_name in $tags; do
    local tag_slug=$(echo "$tag_name" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9-]/-/g')
    local existing_tag=$(curl -s "$WP_URL/wp-json/wp/v2/knowledge_tag?slug=$tag_slug")
    local tag_id=$(echo "$existing_tag" | jq -r '.[0].id // empty')
    
    if [ -z "$tag_id" ] || [ "$tag_id" = "null" ]; then
      local new_tag=$(curl -s -X POST \
        -H "Authorization: Basic $auth_header" \
        -H "Content-Type: application/json" \
        -d "{\"name\":\"$tag_name\",\"slug\":\"$tag_slug\"}" \
        "$WP_URL/wp-json/wp/v2/knowledge_tag")
      tag_id=$(echo "$new_tag" | jq -r '.id // empty')
    fi
    
    if [ ! -z "$tag_id" ] && [ "$tag_id" != "null" ]; then
      tag_ids_array+=("$tag_id")
    fi
  done
  
  # Build JSON array safely
  if [ ${#tag_ids_array[@]} -gt 0 ]; then
    local json_array="["
    local first=true
    for id in "${tag_ids_array[@]}"; do
      if [ "$first" = true ]; then
        json_array="$json_array$id"
        first=false
      else
        json_array="$json_array,$id"
      fi
    done
    json_array="$json_array]"
    echo "$json_array"
  else
    echo "[]"
  fi
}

# Function: Handle featured image
process_featured_image() {
  local image_url="$1"
  local title="$2"
  
  if [ -z "$image_url" ]; then
    echo ""
    return
  fi
  
  if [[ ! "$image_url" =~ ^https?:// ]]; then
    echo ""
    return
  fi
  
  local http_status=$(curl -s -o /dev/null -w "%{http_code}" -L "$image_url" 2>/dev/null || echo "000")
  
  if [ "$http_status" != "200" ]; then
    echo "⚠ Featured image URL returned HTTP $http_status - skipping" >&2
    echo ""
    return
  fi
  
  local cache_key=$(echo "$image_url" | md5sum | cut -d' ' -f1)
  
  if [ ! -z "${MEDIA_CACHE[$cache_key]}" ]; then
    echo "✓ Using cached media ID: ${MEDIA_CACHE[$cache_key]}" >&2
    echo "${MEDIA_CACHE[$cache_key]}"
    return
  fi
  
  local image_basename=$(basename "$image_url" | cut -d'?' -f1 | sed 's/\.[^.]*$//')
  local existing_media=$(curl -s "$WP_URL/wp-json/wp/v2/media?search=$image_basename&per_page=1")
  local media_id=$(echo "$existing_media" | jq -r '.[0].id // empty')
  
  if [ ! -z "$media_id" ] && [ "$media_id" != "null" ]; then
    echo "✓ Found existing media ID: $media_id" >&2
    MEDIA_CACHE[$cache_key]="$media_id"
    echo "$media_id"
    return
  fi
  
  media_id=$(sideload_image "$image_url" "$title")
  if [ "$media_id" != "0" ]; then
    echo "✓ Uploaded new media ID: $media_id" >&2
    MEDIA_CACHE[$cache_key]="$media_id"
    echo "$media_id"
  else
    echo "⚠ Failed to sideload image" >&2
    echo ""
  fi
}

# Main execution
auth_header=$(echo -n "$WP_USERNAME:$WP_APP_PASSWORD" | base64)

get_files_to_process | while IFS= read -r file; do
  # Skip empty lines and non-markdown files
  [ -z "$file" ] || [[ "$file" != *.md ]] && continue
  
  # Block index.md files
  if [[ "$(basename "$file")" == "index.md" ]]; then
    echo "⊘ Skipping index file: $file"
    continue
  fi
  
  # Block Make.md folder-name files (e.g., folder/folder.md)
  folder_name=$(basename "$(dirname "$file")")
  file_name=$(basename "$file" .md)
  if [[ "$folder_name" == "$file_name" ]]; then
    echo "⊘ Skipping Make.md folder file: $file"
    continue
  fi
  
  echo ""
  echo "============================================"
  echo "Processing: $file"
  echo "============================================"
  
  [ ! -f "$file" ] && echo "⚠ File not found: $file" && continue
  
  # Get topic ID
  TOPIC_ID=$(get_topic_id "$file")
  echo "Assigned to topic ID: $TOPIC_ID"
  
  # Generate title from filename
  filename=$(basename "$file" .md)
  title=$(echo "$filename" | sed 's/^[0-9]*_//' | sed 's/_/ /g' | sed 's/-/ /g' | sed 's/\b\(.\)/\u\1/g')
  title=$(echo "$title" | sed -e 's/\bAi\b/AI/g' -e 's/\bSeo\b/SEO/g' -e 's/\bLlm\b/LLM/g' -e 's/\bNlp\b/NLP/g' -e 's/\bApi\b/API/g' -e 's/\bUi\b/UI/g' -e 's/\bUx\b/UX/g' -e 's/\bMl\b/ML/g' -e 's/\bGpt\b/GPT/g' -e 's/\bRag\b/RAG/g' -e 's/\bHtml\b/HTML/g' -e 's/\bCss\b/CSS/g' -e 's/\bUrl\b/URL/g' -e 's/\bIo\b/IO/g')
  
  # Extract frontmatter
  if extract_frontmatter "$file"; then
    [ ! -z "$fm_title" ] && title="$fm_title"
    [ ! -z "$fm_topic" ] && TOPIC_ID="$fm_topic" && echo "Topic overridden by frontmatter: $TOPIC_ID"
  fi
  
  # Get content (strip frontmatter) - safer approach
  if grep -q "^---$" "$file"; then
    # File has frontmatter - extract content after second ---
    content=$(awk '/^---$/{if(++n==2){flag=1;next}}flag' "$file")
  else
    # No frontmatter - use entire file
    content=$(cat "$file")
  fi
  
  # Skip if no actual content (Make.md metadata files)
  if [ -z "$content" ] || [ "$(echo "$content" | tr -d '[:space:]')" = "" ]; then
    echo "⚠ No body content found (Make.md metadata file?), skipping"
    continue
  fi
  
  # Clean Obsidian syntax
  content=$(echo "$content" | sed -e 's/\[\[\([^]|]*\)|\([^]]*\)\]\]/\1/g' -e 's/\[\[\([^]]*\)\]\]/\1/g')
  content=$(echo "$content" | sed -e 's/!\[\[[^]]*\]\]//g' -e 's/\^[a-zA-Z0-9-]*//g')
  content=$(echo "$content" | sed '/^```dataview$/,/^```$/d')
  
  # Convert to HTML
  echo "$content" > /tmp/content.md
  if ! html_content=$(pandoc -f markdown+smart -t html --wrap=none /tmp/content.md 2>&1); then
    echo "⚠ Pandoc conversion failed: $html_content"
    continue
  fi
  
  if [ -z "$html_content" ] || [ "$(echo "$html_content" | tr -d '[:space:]')" = "" ]; then
    echo "⚠ HTML content is empty after conversion, skipping"
    continue
  fi
  
  # Style tables
  html_content=$(echo "$html_content" | sed -e 's/<table>/<table style="border-collapse:collapse;width:100%;border:1px solid #ddd;">/g' -e 's/<th\([^>]*\)>/<th\1 style="border:1px solid #ddd;padding:8px;background:#f4f4f4;text-align:left;">/g' -e 's/<td\([^>]*\)>/<td\1 style="border:1px solid #ddd;padding:8px;text-align:left;">/g')
  
  # Process tags
  tag_ids=$(process_tags "$fm_tags")
  
  # Process featured image
  featured_media=$(process_featured_image "$fm_image" "$title")
  
  # Build ACF payload
  acf_json="{}"
  has_acf=false
  
  if [ ! -z "$fm_semantic" ]; then
    echo "Setting semantic summary"
    acf_json=$(echo "$acf_json" | jq --arg summary "$fm_semantic" '. + {semantic_summary: $summary}')
    has_acf=true
  fi
  
  if [ "$fm_questions" != "[]" ]; then
    question_count=$(echo "$fm_questions" | jq 'length' 2>/dev/null || echo "0")
    if [ "$question_count" != "0" ]; then
      echo "Setting synthetic questions ($question_count items)"
      acf_json=$(echo "$acf_json" | jq --argjson questions "$fm_questions" '. + {synthetic_questions: $questions}')
      has_acf=true
    fi
  fi
  
  if [ "$fm_concepts" != "[]" ]; then
    concept_count=$(echo "$fm_concepts" | jq 'length' 2>/dev/null || echo "0")
    if [ "$concept_count" != "0" ]; then
      echo "Setting key concepts ($concept_count items)"
      acf_json=$(echo "$acf_json" | jq --argjson concepts "$fm_concepts" '. + {key_concepts: $concepts}')
      has_acf=true
    fi
  fi
  
  # Build meta payload
  meta_json="{}"
  has_meta=false
  
  if [ ! -z "$fm_keyword" ]; then
    echo "Setting focus keyword: $fm_keyword"
    meta_json=$(echo "$meta_json" | jq --arg key "$fm_keyword" '. + {rank_math_focus_keyword: $key}')
    has_meta=true
  fi
  
  if [ ! -z "$fm_meta_desc" ]; then
    echo "Setting meta description: $fm_meta_desc"
    meta_json=$(echo "$meta_json" | jq --arg desc "$fm_meta_desc" '. + {rank_math_description: $desc}')
    has_meta=true
  fi
  
  # Check if post exists
  slug=$(echo "$title" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g' | sed 's/[^a-z0-9-]//g')
  existing_post=$(curl -s "$WP_URL/wp-json/wp/v2/knowledge?slug=$slug")
  post_id=$(echo "$existing_post" | jq -r '.[0].id // empty')
  
  if [ ! -z "$post_id" ] && [ "$post_id" != "null" ]; then
    method="PUT"
    endpoint="$WP_URL/wp-json/wp/v2/knowledge/$post_id"
    echo "Updating existing post (ID: $post_id)"
  else
    method="POST"
    endpoint="$WP_URL/wp-json/wp/v2/knowledge"
    echo "Creating new post"
  fi
  
  # Build JSON payload incrementally
  echo "Building JSON payload..."
  
  # Start with base payload
  json_payload=$(jq -n \
    --arg title "$title" \
    --arg content "$html_content" \
    --argjson topic "$TOPIC_ID" \
    --argjson tags "$tag_ids" \
    '{
      title: $title,
      content: $content,
      status: "publish",
      knowledge_topics: [1158, $topic],
      knowledge_tag: $tags
    }')
  
  # Add optional fields incrementally
  if [ ! -z "$fm_excerpt" ]; then
    json_payload=$(echo "$json_payload" | jq --arg excerpt "$fm_excerpt" '. + {excerpt: $excerpt}')
  fi
  
  if [ ! -z "$fm_updated" ]; then
    json_payload=$(echo "$json_payload" | jq --arg date "$fm_updated" '. + {date: $date}')
  fi
  
  if [ ! -z "$featured_media" ]; then
    json_payload=$(echo "$json_payload" | jq --argjson featured_media "$featured_media" '. + {featured_media: $featured_media}')
  fi
  
  if [ "$has_meta" = "true" ]; then
    json_payload=$(echo "$json_payload" | jq --argjson meta "$meta_json" '. + {meta: $meta}')
  fi
  
  if [ "$has_acf" = "true" ]; then
    json_payload=$(echo "$json_payload" | jq --argjson acf "$acf_json" '. + {acf: $acf}')
  fi
  
  echo "Syncing: $title with Topics: [1158, $TOPIC_ID]"
  
  # Sync to WordPress
  response=$(curl -s -w "\n%{http_code}" -X $method \
    -H "Authorization: Basic $auth_header" \
    -H "Content-Type: application/json" \
    -d "$json_payload" \
    "$endpoint")
  
  http_code=$(echo "$response" | tail -n1)
  body=$(echo "$response" | sed '$d')
  
  if [ "$http_code" -eq 200 ] || [ "$http_code" -eq 201 ]; then
    echo "✓ Successfully synced: $title"
    post_id=$(echo "$body" | jq -r '.id')
    
    # Generate embeddings
    echo "Generating embeddings for Post ID: $post_id"
    embed_payload=$(jq -n --argjson post_id "$post_id" '{postId: $post_id, envId: "default"}')
    embed_response=$(curl -s -w "\n%{http_code}" -X POST \
      -H "Authorization: Bearer $BEARER_TOKEN" \
      -H "Content-Type: application/json" \
      -d "$embed_payload" \
      "$WP_URL/wp-json/mwai/v2/vectors/add")
    
    embed_http_code=$(echo "$embed_response" | tail -n1)
    if [ "$embed_http_code" -eq 200 ]; then
      echo "✓ Embeddings generated successfully."
    else
      echo "⚠ Embedding generation failed (HTTP $embed_http_code)"
    fi
  else
    echo "✗ Failed to sync: $title (HTTP $http_code)"
    echo "$body" | jq '.' 2>/dev/null || echo "$body"
  fi
done

# tools/kb_sync.py
"""
Knowledge Base Sync Tool
Syncs Obsidian markdown files to WordPress and Pinecone.
Replaces: GitHub Actions workflow + AI Engine Pro

Flow: Obsidian (.md) → WordPress (REST API) → Pinecone (embeddings)
"""

import os
import re
import sys
import json
import base64
import requests
from pathlib import Path
from datetime import datetime
from typing import Optional
from dotenv import load_dotenv

# Fix Windows console encoding for Unicode characters
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Load environment variables
load_dotenv()

# Import Pinecone functions
from tools.pinecone_tool import upsert_to_knowledge_core, batch_upsert_to_knowledge_core

# =============================================================================
# Configuration
# =============================================================================

WP_SITE_URL = os.getenv("WP_SITE_URL", "https://adambernard.com")
WP_USERNAME = os.getenv("WP_USERNAME", "adam")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD", "")

# Knowledge base root folder
KB_ROOT = Path(os.getenv("KB_ROOT", r"C:\Users\AdamB\Documents\Brain\Adam\kb"))

# Topic ID mapping (path pattern → WordPress topic ID)
TOPIC_MAPPING = {
    "/AI/0_fundamentals/": 1186,
    "/AI/1_models/specific-models/": 1779,
    "/AI/1_models/concepts-and-techniques/": 1780,
    "/AI/1_models/evaluation-and-tooling/": 1781,
    "/AI/1_models/comparisons/": 1782,
    "/AI/1_models/": 1187,
    "/AI/2_agents/toolkits/": 1783,
    "/AI/2_agents/": 1188,
    "/AI/3_methods/mcp/": 1784,
    "/AI/3_methods/": 1189,
    "/AI/4_applications/business/": 1785,
    "/AI/4_applications/marketing/": 1786,
    "/AI/4_applications/": 1190,
    "/AI/5_ethics-and-governance/": 1191,
    "/AI/6_future-trends/": 1192,
    "/AI/": 1159,
    "/SEO/0_fundamentals/": 1162,
    "/SEO/1_research-and-strategy/": 1163,
    "/SEO/2_content-and-on-page/": 1164,
    "/SEO/3_technical-seo/": 1165,
    "/SEO/4_ai-and-automation/using-ai-for-seo/": 1787,
    "/SEO/4_ai-and-automation/optimizing-for-ai/": 1788,
    "/SEO/4_ai-and-automation/": 1166,
    "/SEO/5_measurement-and-optimization/": 1167,
    "/SEO/6_future-trends/": 1168,
    "/SEO/": 1158,
    "/TOOLS/marketing-automation/seo-optimization/": 1603,
    "/TOOLS/ai-foundation-models/": 1596,
    "/TOOLS/analytics-data-insights/": 1597,
    "/TOOLS/audio-generation/": 1598,
    "/TOOLS/coding-development/": 1599,
    "/TOOLS/content-creation/": 1600,
    "/TOOLS/image-video-generation/": 1601,
    "/TOOLS/marketing-automation/": 1602,
    "/TOOLS/productivity-workflow/": 1604,
    "/TOOLS/research-knowledge-agents/": 1605,
    "/TOOLS/social-media/": 1606,
    "/TOOLS/": 1160,
    "/CORE/core-concepts/": 1608,
    "/CORE/strategy-application/": 1609,
    "/CORE/": 1607,
}

# Parent topic ID (all posts get this + specific topic)
PARENT_TOPIC_ID = 1158

# =============================================================================
# WordPress API Client
# =============================================================================

class WordPressClient:
    def __init__(self, site_url: str, username: str, app_password: str):
        self.site_url = site_url.rstrip("/")
        self.auth_header = base64.b64encode(f"{username}:{app_password}".encode()).decode()
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Basic {self.auth_header}",
            "Content-Type": "application/json"
        })

    def get_post_by_slug(self, slug: str) -> Optional[dict]:
        """Check if a knowledge post exists by slug."""
        url = f"{self.site_url}/wp-json/wp/v2/knowledge"
        response = self.session.get(url, params={"slug": slug})
        if response.status_code == 200:
            posts = response.json()
            return posts[0] if posts else None
        return None

    def create_post(self, payload: dict) -> dict:
        """Create a new knowledge post."""
        url = f"{self.site_url}/wp-json/wp/v2/knowledge"
        response = self.session.post(url, json=payload)
        if response.status_code >= 400:
            raise Exception(f"{response.status_code} Error: {response.text[:500]}")
        return response.json()

    def update_post(self, post_id: int, payload: dict) -> dict:
        """Update an existing knowledge post."""
        url = f"{self.site_url}/wp-json/wp/v2/knowledge/{post_id}"
        response = self.session.put(url, json=payload)
        if response.status_code >= 400:
            raise Exception(f"{response.status_code} Error: {response.text[:500]}")
        return response.json()

    def get_or_create_tag(self, tag_name: str) -> int:
        """Get tag ID or create if doesn't exist."""
        slug = re.sub(r'[^a-z0-9-]', '-', tag_name.lower())

        # Check if tag exists
        url = f"{self.site_url}/wp-json/wp/v2/knowledge_tag"
        response = self.session.get(url, params={"slug": slug})
        if response.status_code == 200:
            tags = response.json()
            if tags:
                return tags[0]["id"]

        # Create new tag
        response = self.session.post(url, json={"name": tag_name, "slug": slug})
        if response.status_code in (200, 201):
            return response.json()["id"]

        return None

    def update_rankmath_meta(self, post_id: int, focus_keyword: str = None, description: str = None) -> bool:
        """Update Rank Math SEO meta using Rank Math's REST API."""
        if not focus_keyword and not description:
            return True

        url = f"{self.site_url}/wp-json/rankmath/v1/updateMeta"

        meta = {}
        if focus_keyword:
            meta["rank_math_focus_keyword"] = focus_keyword
        if description:
            meta["rank_math_description"] = description

        payload = {
            "objectType": "post",
            "objectID": post_id,
            "meta": meta
        }

        try:
            response = self.session.post(url, json=payload)
            return response.status_code == 200
        except Exception:
            return False


# =============================================================================
# Markdown Parser
# =============================================================================

def parse_frontmatter(content: str) -> tuple[dict, str]:
    """
    Parse YAML frontmatter from markdown content.
    Returns (frontmatter_dict, body_content)

    Properly handles --- appearing in YAML comments (e.g., # --- Section ---)
    by only treating --- as a delimiter when it's on its own line.
    """
    import yaml

    lines = content.split('\n')

    # Must start with --- on first line (with optional trailing whitespace)
    if not lines or not re.match(r'^---\s*$', lines[0]):
        return {}, content

    # Find the closing --- (must be on its own line, not in a comment)
    end_index = None
    for i, line in enumerate(lines[1:], start=1):
        if re.match(r'^---\s*$', line):
            end_index = i
            break

    if end_index is None:
        return {}, content

    # Extract frontmatter and body
    frontmatter_lines = lines[1:end_index]
    body_lines = lines[end_index + 1:]

    frontmatter_text = '\n'.join(frontmatter_lines)
    body = '\n'.join(body_lines).strip()

    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        return frontmatter or {}, body
    except yaml.YAMLError as e:
        print(f"    YAML parse error: {e}")
        return {}, content


def markdown_to_html(markdown_content: str) -> str:
    """
    Convert markdown to HTML.
    Uses markdown library with extensions.
    """
    import markdown

    # Clean Obsidian-specific syntax first
    content = clean_obsidian_syntax(markdown_content)

    # Convert to HTML
    md = markdown.Markdown(extensions=[
        'tables',
        'fenced_code',
        'codehilite',
        'toc',
        'smarty'
    ])

    html = md.convert(content)

    # Style tables
    html = style_tables(html)

    # Style code blocks for wrapping
    html = style_code_blocks(html)

    return html


def convert_wikilink_to_url(match: re.Match) -> str:
    """
    Convert an Obsidian wiki-link to a WordPress URL.

    Handles:
    - [[page]] → [Page](/kb/page/)
    - [[page|display]] → [display](/kb/page/)
    - [[page#heading]] → [Page](/kb/page/#heading)
    - [[page#heading|display]] → [display](/kb/page/#heading)
    - [[folder/page]] → [Page](/kb/page/)
    """
    full_match = match.group(1)

    # Split by pipe to get display text
    if '|' in full_match:
        target, display_text = full_match.split('|', 1)
    else:
        target = full_match
        display_text = None

    # Extract heading anchor if present
    heading = None
    if '#' in target:
        target, heading = target.split('#', 1)

    # Get just the filename if it's a path (folder/subfolder/page → page)
    if '/' in target:
        target = target.split('/')[-1]

    # Remove file extension if present
    target = re.sub(r'\.md$', '', target, flags=re.IGNORECASE)

    # Generate slug from target
    slug = target.lower()
    slug = re.sub(r'^[0-9]+[_-]', '', slug)  # Remove numeric prefix
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug.strip('-')

    # Generate display text if not provided
    if not display_text:
        display_text = target.replace('-', ' ').replace('_', ' ')
        # Remove numeric prefix for display
        display_text = re.sub(r'^[0-9]+[_\s-]*', '', display_text)
        # Title case
        display_text = display_text.title()
        # Fix common acronyms
        for acronym in ['AI', 'SEO', 'LLM', 'NLP', 'API', 'UI', 'UX', 'ML', 'GPT', 'RAG', 'MCP']:
            display_text = re.sub(rf'\b{acronym.title()}\b', acronym, display_text, flags=re.IGNORECASE)

    # Build the URL
    url = f"/kb/{slug}/"
    if heading:
        # Convert heading to anchor format
        anchor = heading.lower()
        anchor = re.sub(r'[^a-z0-9\s-]', '', anchor)
        anchor = re.sub(r'\s+', '-', anchor)
        url += f"#{anchor}"

    return f"[{display_text}]({url})"


def clean_obsidian_syntax(content: str) -> str:
    """Convert Obsidian-specific syntax for WordPress."""
    # Convert internal links to WordPress URLs
    # Pattern matches [[...]] but not ![[...]] (images)
    content = re.sub(r'(?<!!)\[\[([^\]]+)\]\]', convert_wikilink_to_url, content)

    # Image embeds: ![[image.png]] → remove (WordPress handles images differently)
    content = re.sub(r'!\[\[[^\]]*\]\]', '', content)

    # Footnote anchors: ^anchor → remove
    content = re.sub(r'\^[a-zA-Z0-9-]+', '', content)

    # Dataview blocks: ```dataview ... ``` → remove
    content = re.sub(r'```dataview[\s\S]*?```', '', content, flags=re.MULTILINE)

    return content


def style_tables(html: str) -> str:
    """Add inline styles to tables for WordPress."""
    html = html.replace(
        '<table>',
        '<table style="border-collapse:collapse;width:100%;border:1px solid #ddd;">'
    )
    html = re.sub(
        r'<th([^>]*)>',
        r'<th\1 style="border:1px solid #ddd;padding:8px;background:#f4f4f4;text-align:left;">',
        html
    )
    html = re.sub(
        r'<td([^>]*)>',
        r'<td\1 style="border:1px solid #ddd;padding:8px;text-align:left;">',
        html
    )
    return html


def style_code_blocks(html: str) -> str:
    """Add inline styles to code blocks for proper wrapping in WordPress."""
    # Style pre blocks (fenced code blocks)
    html = html.replace(
        '<pre>',
        '<pre style="background:#f5f5f5;padding:16px;border-radius:4px;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word;">'
    )
    # Style inline code
    html = re.sub(
        r'<code>(?!</pre>)',  # Inline code (not inside pre)
        '<code style="background:#f5f5f5;padding:2px 6px;border-radius:3px;">',
        html
    )
    return html


def generate_slug(text: str) -> str:
    """Generate URL slug from text (title or filename)."""
    slug = text.lower()
    # Convert various Unicode hyphens/dashes to regular hyphen
    slug = re.sub(r'[\u2010\u2011\u2012\u2013\u2014\u2015\u2212]', '-', slug)
    # Remove non-alphanumeric except spaces and hyphens
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    # Convert spaces and underscores to hyphens
    slug = re.sub(r'[\s_]+', '-', slug)
    # Collapse multiple hyphens
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')


def slug_from_filename(filename: str) -> str:
    """
    Generate URL slug from filename.
    This matches WordPress slugs better than long title-based slugs.

    Example: 02_title-tags-and-meta.md → title-tags-and-meta
    """
    # Remove extension
    name = filename.replace('.md', '')
    # Remove numeric prefix (e.g., 00_, 01_, 02_)
    name = re.sub(r'^[0-9]+[_-]', '', name)
    # Convert to slug format
    return generate_slug(name)


def title_from_filename(filename: str) -> str:
    """Generate title from filename."""
    # Remove numeric prefix and extension
    name = re.sub(r'^[0-9]+_', '', filename)
    name = name.replace('.md', '')

    # Convert to title case
    title = name.replace('_', ' ').replace('-', ' ').title()

    # Fix common acronyms
    acronyms = ['AI', 'SEO', 'LLM', 'NLP', 'API', 'UI', 'UX', 'ML', 'GPT', 'RAG', 'HTML', 'CSS', 'URL', 'IO', 'MCP']
    for acronym in acronyms:
        title = re.sub(rf'\b{acronym.title()}\b', acronym, title, flags=re.IGNORECASE)

    return title


def get_topic_id(file_path: Path, kb_root: Path) -> int:
    """Determine WordPress topic ID from file path."""
    relative_path = str(file_path.relative_to(kb_root)).replace("\\", "/")

    # Check mappings (most specific first - sorted by length descending)
    for pattern, topic_id in sorted(TOPIC_MAPPING.items(), key=lambda x: -len(x[0])):
        if pattern.strip("/") in relative_path:
            return topic_id

    return 1158  # Default to SEO parent topic


# =============================================================================
# Sync Functions
# =============================================================================

def should_sync_file(file_path: Path) -> bool:
    """Check if a file should be synced to WordPress."""
    # Skip index.md files
    if file_path.name == "index.md":
        return False

    # Skip Make.md folder files (folder/folder.md)
    if file_path.stem == file_path.parent.name:
        return False

    # Skip hidden files/folders
    if any(part.startswith('.') for part in file_path.parts):
        return False

    return True


def sync_file(file_path: Path, wp_client: WordPressClient, dry_run: bool = False) -> dict:
    """
    Sync a single markdown file to WordPress and Pinecone.

    Returns dict with status, post_id, and any errors.
    """
    result = {
        "file": str(file_path),
        "status": "pending",
        "post_id": None,
        "pinecone": None,
        "error": None
    }

    try:
        # Read file
        content = file_path.read_text(encoding="utf-8")

        # Parse frontmatter
        frontmatter, body = parse_frontmatter(content)

        # Skip if no body content
        if not body.strip():
            result["status"] = "skipped"
            result["error"] = "No body content"
            return result

        # Extract metadata
        title = frontmatter.get("title") or title_from_filename(file_path.name)
        # Use frontmatter slug if specified, otherwise generate from title
        slug = frontmatter.get("slug") or generate_slug(title)
        excerpt = frontmatter.get("excerpt") or frontmatter.get("summary", "")
        tags = frontmatter.get("tags", [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",")]

        topic_id = frontmatter.get("topic") or get_topic_id(file_path, KB_ROOT)

        # SEO fields
        keyword = frontmatter.get("primary_keyword") or frontmatter.get("keyword", "")
        meta_desc = frontmatter.get("meta_description", "")

        # AI/RAG fields
        semantic_summary = frontmatter.get("semantic_summary", "")
        synthetic_questions = frontmatter.get("synthetic_questions", [])
        key_concepts = frontmatter.get("key_concepts", [])

        # Date - WordPress requires full ISO 8601 with time
        updated = frontmatter.get("updated", "")
        if updated:
            try:
                if isinstance(updated, str):
                    # Handle date-only format (2026-01-15)
                    if len(updated) == 10 and "-" in updated:
                        updated = f"{updated}T00:00:00"
                    updated = datetime.fromisoformat(updated.replace("Z", "+00:00"))
                # Ensure we have a datetime, not just date
                if hasattr(updated, 'isoformat'):
                    updated = updated.isoformat()
                    # Ensure time component exists
                    if "T" not in updated:
                        updated = f"{updated}T00:00:00"
            except:
                updated = None

        # Convert markdown to HTML
        html_content = markdown_to_html(body)

        if dry_run:
            result["status"] = "dry_run"
            result["title"] = title
            result["slug"] = slug
            result["topic_id"] = topic_id
            return result

        # Process tags
        tag_ids = []
        for tag in tags:
            tag_id = wp_client.get_or_create_tag(tag)
            if tag_id:
                tag_ids.append(tag_id)

        # Build WordPress payload
        payload = {
            "title": title,
            "content": html_content,
            "status": "publish",
            "knowledge_topics": [PARENT_TOPIC_ID, topic_id],
            "knowledge_tag": tag_ids
        }

        if excerpt:
            payload["excerpt"] = excerpt

        if updated:
            payload["date"] = updated

        # Note: Rank Math SEO fields are set via dedicated API after post creation

        # ACF fields
        acf = {}
        if semantic_summary:
            acf["semantic_summary"] = semantic_summary
        if synthetic_questions:
            acf["synthetic_questions"] = [{"question": q} for q in synthetic_questions]
        if key_concepts:
            acf["key_concepts"] = [{"concept": c} for c in key_concepts]
        if acf:
            payload["acf"] = acf

        # Check if post exists
        existing = wp_client.get_post_by_slug(slug)

        if existing:
            post = wp_client.update_post(existing["id"], payload)
            result["status"] = "updated"
        else:
            post = wp_client.create_post(payload)
            result["status"] = "created"

        result["post_id"] = post["id"]
        result["url"] = post.get("link", f"{WP_SITE_URL}/kb/{slug}/")
        result["title"] = title

        # Update Rank Math SEO meta (uses dedicated Rank Math API)
        if keyword or meta_desc:
            rankmath_success = wp_client.update_rankmath_meta(
                post_id=post["id"],
                focus_keyword=keyword,
                description=meta_desc
            )
            result["rankmath"] = "updated" if rankmath_success else "failed"

        # Sync to Pinecone
        pinecone_content = f"{title}\n\n{body}"
        if semantic_summary:
            pinecone_content = f"{title}\n\n{semantic_summary}\n\n{body}"

        pinecone_result = upsert_to_knowledge_core(
            content=pinecone_content,
            doc_id=f"kb-{post['id']}",
            title=title,
            source=f"{WP_SITE_URL}/kb/{slug}/",
            date=updated or datetime.now().isoformat(),
            post_type="knowledge_base",
            url=result["url"]
        )
        result["pinecone"] = pinecone_result

    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)

    return result


def sync_all(dry_run: bool = False, filter_path: str = None) -> list[dict]:
    """
    Sync all markdown files in the knowledge base.

    Args:
        dry_run: If True, only show what would be synced
        filter_path: Optional path filter (e.g., "AI/" to only sync AI folder)

    Returns:
        List of sync results
    """
    wp_client = WordPressClient(WP_SITE_URL, WP_USERNAME, WP_APP_PASSWORD)
    results = []

    # Find all markdown files
    for md_file in KB_ROOT.rglob("*.md"):
        # Apply filter if specified
        if filter_path:
            relative = str(md_file.relative_to(KB_ROOT))
            if not relative.startswith(filter_path.replace("/", os.sep)):
                continue

        if not should_sync_file(md_file):
            continue

        print(f"Processing: {md_file.relative_to(KB_ROOT)}")
        result = sync_file(md_file, wp_client, dry_run=dry_run)
        results.append(result)

        status_icon = {
            "created": "[+] Created",
            "updated": "[~] Updated",
            "skipped": "[-] Skipped",
            "error": "[!] Error",
            "dry_run": "[?] Would sync"
        }.get(result["status"], result["status"])

        print(f"  {status_icon}: {result.get('title', md_file.name)}")
        if result.get("error"):
            print(f"    Error: {result['error']}")
        if result.get("pinecone"):
            print(f"    Pinecone: {result['pinecone']}")

    return results


def sync_file_by_path(file_path: str, dry_run: bool = False) -> dict:
    """Sync a single file by path."""
    path = Path(file_path)
    if not path.is_absolute():
        path = KB_ROOT / path

    if not path.exists():
        return {"status": "error", "error": f"File not found: {path}"}

    wp_client = WordPressClient(WP_SITE_URL, WP_USERNAME, WP_APP_PASSWORD)
    return sync_file(path, wp_client, dry_run=dry_run)


def save_mapping_file(results: list[dict]) -> None:
    """
    Save a mapping file connecting Obsidian files to WordPress posts.

    Creates/updates kb_sync_mapping.json in the kb root folder with:
    - Obsidian file path (relative)
    - WordPress post ID
    - WordPress slug
    - WordPress URL
    - Last sync timestamp
    """
    mapping_file = KB_ROOT / "kb_sync_mapping.json"

    # Load existing mapping
    existing_mapping = {}
    if mapping_file.exists():
        try:
            existing_mapping = json.loads(mapping_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existing_mapping = {}

    # Update with new results
    timestamp = datetime.now().isoformat()
    for result in results:
        if result.get("status") in ("created", "updated") and result.get("post_id"):
            # Get relative path from file path
            file_path = result.get("file", "")
            try:
                rel_path = str(Path(file_path).relative_to(KB_ROOT)).replace("\\", "/")
            except ValueError:
                rel_path = file_path

            existing_mapping[rel_path] = {
                "post_id": result.get("post_id"),
                "slug": result.get("url", "").split("/kb/")[-1].rstrip("/") if "/kb/" in result.get("url", "") else "",
                "url": result.get("url"),
                "title": result.get("title", ""),
                "last_synced": timestamp
            }

    # Save updated mapping
    mapping_file.write_text(
        json.dumps(existing_mapping, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )
    print(f"\nMapping saved to: {mapping_file}")


# =============================================================================
# CLI Interface
# =============================================================================

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Sync Knowledge Base to WordPress + Pinecone")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be synced without making changes")
    parser.add_argument("--file", type=str, help="Sync a specific file (relative to kb root)")
    parser.add_argument("--filter", type=str, help="Filter by path prefix (e.g., 'AI/' or 'SEO/')")

    args = parser.parse_args()

    print("=" * 60)
    print("Knowledge Base Sync")
    print(f"Source: {KB_ROOT}")
    print(f"Destination: {WP_SITE_URL}")
    print("=" * 60)

    if args.file:
        result = sync_file_by_path(args.file, dry_run=args.dry_run)
        print(json.dumps(result, indent=2))
    else:
        results = sync_all(dry_run=args.dry_run, filter_path=args.filter)

        # Summary
        print("\n" + "=" * 60)
        print("Summary")
        print("=" * 60)

        created = sum(1 for r in results if r["status"] == "created")
        updated = sum(1 for r in results if r["status"] == "updated")
        skipped = sum(1 for r in results if r["status"] == "skipped")
        errors = sum(1 for r in results if r["status"] == "error")

        print(f"Created: {created}")
        print(f"Updated: {updated}")
        print(f"Skipped: {skipped}")
        print(f"Errors:  {errors}")
        print(f"Total:   {len(results)}")

        # Save mapping file
        save_mapping_file(results)

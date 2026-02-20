#!/usr/bin/env python3
"""Check which files in GROWTH need frontmatter."""
import re
from pathlib import Path

GROWTH = Path(r"C:\Users\AdamB\Documents\Brain\Adam\kb\GROWTH")

has_full = []
has_partial = []
needs_fm = []

for f in sorted(GROWTH.rglob("*.md")):
    if f.name == "index.md":
        continue
    content = f.read_text(encoding='utf-8', errors='replace')
    rel = f.relative_to(GROWTH)

    if not content.startswith('---'):
        needs_fm.append(str(rel))
        continue

    # Check for key schema fields
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        needs_fm.append(str(rel))
        continue

    fm = match.group(1)
    has_semantic = 'semantic_summary' in fm
    has_seo = 'primary_keyword' in fm

    if has_semantic and has_seo:
        has_full.append(str(rel))
    else:
        has_partial.append(str(rel))

print(f"FULL SCHEMA ({len(has_full)}):")
for f in has_full:
    print(f"  {f}")

print(f"\nPARTIAL SCHEMA ({len(has_partial)}):")
for f in has_partial:
    print(f"  {f}")

print(f"\nNO FRONTMATTER ({len(needs_fm)}):")
for f in needs_fm:
    print(f"  {f}")

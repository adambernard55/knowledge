
## Specific Models Contents

```dataview
TABLE WITHOUT ID
  file.link as "Topic",
  semantic_summary as "Description"
FROM "kb/AI/1_models/1_specific-models"
WHERE file.name != "index.md"
SORT file.name ASC
````



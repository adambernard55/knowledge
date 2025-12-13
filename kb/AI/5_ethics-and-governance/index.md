## Contents

```dataview
TABLE WITHOUT ID
  file.link as "Topic",
  summary as "Description"
FROM "kb/AI/5_ethics-and-governance"
WHERE file.name != "index.md"
SORT file.name ASC
````
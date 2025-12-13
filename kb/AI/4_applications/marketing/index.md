## Contents

```dataview
TABLE WITHOUT ID
  file.link as "Topic",
  summary as "Description"
FROM "kb/AI/4_applications/marketing"
WHERE file.name != "index.md"
SORT file.name ASC
````
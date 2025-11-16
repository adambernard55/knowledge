## Contents

```dataview
TABLE WITHOUT ID
  file.link as "Topic",
  summary as "Description"
FROM "Knowledge/AI/4_applications"
WHERE file.name != "index.md"
SORT file.name ASC
````
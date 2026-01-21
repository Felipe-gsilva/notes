---
id: task-2
title: Database Storage Engine
status: To Do
assignee: []
created_date: '2025-11-15 17:09'
updated_date: '2025-11-20 12:34'
labels: []
dependencies: []
ordinal: 3000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
a library that exports you a table_open(), table_insert(row), table_select(query) API, persisting everything into a data file.

---

Data structures: 
    - B+ Tree: I already it written, just need some generic updates for real use cases
    - Buffer Pool Manager: My b-tree+ impl already covers up some of this, also my memory alloc inside ChicOS have some. But I will need a eviction policy so a more robust impl is required

Architecture:
    - Need a concurrent manager for I/O's op's
    - Write-Ahead Log (WAL): For crash recovery. Before you modify a page, you write the change to a log file. This is a key architectural decision for data safety.
<!-- SECTION:DESCRIPTION:END -->

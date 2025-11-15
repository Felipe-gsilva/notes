---
id: task-2
title: Database Storage Engine
status: To Do
assignee: []
created_date: '2025-11-15 17:09'
labels: []
dependencies: []
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Build a library that gives you a table_open(), table_insert(row), table_select(query) API, persisting everything to a file.

---

Data structures: 
    - B+ Tree: I already it written, just need some generic updates for real use cases
    - Buffer Pool Manager: My b-tree+ impl already covers up some of this, also my memory alloc inside ChicOS have some. But I will need a eviction policy so a more robust impl is required

Architecture:
    - Need a concurrent manager for I/O's op's
    - Write-Ahead Log (WAL): For crash recovery. Before you modify a page, you write the change to a log file. This is a key architectural decision for data safety.
<!-- SECTION:DESCRIPTION:END -->

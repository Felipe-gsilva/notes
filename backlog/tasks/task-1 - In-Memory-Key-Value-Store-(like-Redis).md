---
id: task-1
title: In-Memory Key-Value Store (like Redis)
status: To Do
assignee: []
created_date: '2025-11-15 17:06'
labels: []
dependencies: []
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Build a server that listens on a port, accepts commands (like SET, GET, DEL), and stores data in memory.

---

## Data Structures:
    - Hash Table: Which can handle collisions, resizing, and efficient key hashing.
    - Linked Lists: For implementing eviction policies (like LRU - Least Recently Used) when memory gets full.

## Algorithms:
    - Network Protocol Parsing:  algorithm to parse your custom text or binary protocol.
    - Eviction Policies: LRU, LFU (Least Frequently Used), or random eviction.
    - Command Dispatching: A clean way to map string commands ("GET") to function pointers.

Architecture:
    - Event Loop:  select(), poll() to handle many network clients non-blockingly.
    - Persistence: snapshotting (dumping all data) or an Append-Only File (AOF) that logs commands.
   - Client/Server Model: Designing the API and client-handling logic.
<!-- SECTION:DESCRIPTION:END -->

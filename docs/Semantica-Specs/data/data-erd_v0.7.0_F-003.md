---
title: Data Model v0.7.0 F-003 — Storage Backends
id: F-003
status: draft
owner: TBD
updated: 2026-09-21
---

# Data Model v0.7.0 F-003 — Storage Backends

> The slice of the data model this feature reads and writes, reversed from code at commit `92c2578a`.

## Scope

| entity | Role | Defined at |
| --- | --- | --- |
| `ContextEdge` | Write | `semantica/context/context_graph.py:462` |
| `ContextNode` | Write | `semantica/context/context_graph.py:419` |

This feature is where `ContextNode` and `ContextEdge` become durable. The graph, vector and triplet backends each hold their own on-disk or remote representation; none of them is re-declared here [D: semantica/vector_store/faiss_store.py:300].

## Feature ERD

`schema/erd_v0.7.0_F-003.puml` — the subset above, drawn with the field lists `schema/schemas.json` declares. It introduces no entity that `schema/erd_master.puml` does not already have.

## Field definitions

Field-level truth is `schema/schemas.json`. Restating it here would create a second opinion that drifts; the `$defs` entries named in Scope are the readable rendering, and each one carries its own `Defined at` pointer.

## New and changed entities

None. Every entity above already exists in `data-master-erd.md`.

## Migrations

None. The repository holds no migration directory, no `schema.sql`, no ORM migration tool and no DDL file [D: pyproject.toml:1]. Persistence is file-backed JSON and vendor-specific stores, each writing its own format at runtime [D: semantica/context/context_graph.py:1409].

I: shape changes ship as code changes with no migration step — basis: the persisted JSON is produced by `to_dict` on the dataclass itself [D: semantica/context/context_graph.py:450], so a renamed field changes the file format with no recorded upgrade path.

## Retention and ownership

OPEN: what is the retention policy for persisted graphs, decisions and annotations? No expiry, TTL or purge path appears in the code.
OPEN: which store is the system of record when a graph is held in a vector store and a graph store at once? The code writes to both without naming a primary.

## Open questions

OPEN: are the pydantic response models a contract, or a projection that may change with the UI? They carry no version marker.
OPEN: should `additionalProperties: false` hold in production? The reversal derived it from the declared field list, and the runtime `properties` and `metadata` dicts are open maps that carry undeclared keys [D: semantica/context/context_graph.py:450].

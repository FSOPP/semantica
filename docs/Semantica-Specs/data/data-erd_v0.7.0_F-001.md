---
title: Data Model v0.7.0 F-001 — Ingest and Parse Pipeline
id: F-001
status: draft
owner: TBD
updated: 2026-09-21
---

# Data Model v0.7.0 F-001 — Ingest and Parse Pipeline

> The slice of the data model this feature reads and writes, reversed from code at commit `92c2578a`.

## Scope

This feature persists none of the registry entities. Its output is in-memory document and chunk dictionaries handed to F-002 [D: semantica/parse/methods.py:1].

I: ingestion has no durable entity of its own — basis: no module under `semantica/ingest` writes to a store; the ingestors return records and the pipeline passes them on [D: semantica/ingest/powerbi_ingestor.py:780].

## Feature ERD

`schema/erd_v0.7.0_F-001.puml` — the subset above, drawn with the field lists `schema/schemas.json` declares. It introduces no entity that `schema/erd_master.puml` does not already have.

## Field definitions

Not applicable — this feature owns no entity.

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

---
title: Domain — Storage Backends
id: DOM-003
kind: domain
feature: F-003
status: draft
owner: TBD
updated: 2026-09-21
---

# Domain — Storage Backends

> Reversed from code at commit `92c2578a`. Every rule below was promoted from a comment or a test name in the code, and cites both the statement and the code that enforces it.

## Ubiquitous language

| term | definition | aliases to avoid |
| --- | --- | --- |
| backend | One vendor implementation behind a tier registry — 11 graph, 19 vector, 15 triplet [D: semantica/vector_store/registry.py:1]. | driver, adapter |
| vector id | `vec_N`, from a monotonic counter [D: semantica/vector_store/vector_store.py:146]. | — |
| namespace | A partition within a vector store [D: semantica/vector_store/namespace_manager.py:1]. | collection, index |

## Actors

The pipeline and the Explorer session, both in-process. No external caller reaches a store directly.

## Business rules

**`DOM-003-R1`** — A vector ID is never reused, including after deletion.

I: A vector ID is never reused, including after deletion — basis: the code states "the monotonic counter is incremented on every successful add and never decremented on deletion" at `semantica/vector_store/vector_store.py:146`, and it is enforced at `semantica/vector_store/faiss_store.py:551`
**`DOM-003-R2`** — Vectors and their metadata are read and written as one consistent pair.

I: Vectors and their metadata are read and written as one consistent pair — basis: the code states "snapshot vectors and metadata together under the lock; hold the lock across allocation, dict write and index rebuild" at `semantica/vector_store/vector_store.py:801`, and it is enforced at `semantica/vector_store/vector_store.py:569`
**`DOM-003-R3`** — A failed save leaves the previously persisted index intact.

I: A failed save leaves the previously persisted index intact — basis: the code states "serialize vector_ids, metadata, dimension and index_type before touching any files" at `semantica/vector_store/faiss_store.py:300`, and it is enforced at `semantica/vector_store/faiss_store.py:300`
**`DOM-003-R4`** — A deletion on a disk-loaded store survives a process restart.

I: A deletion on a disk-loaded store survives a process restart — basis: the code states "persist the deletion so the vectors cannot be resurrected by a restart" at `semantica/vector_store/faiss_store.py:939`, and it is enforced at `semantica/vector_store/faiss_store.py:939`
**`DOM-003-R5`** — Signed cloud credentials are never written to a log.

I: Signed cloud credentials are never written to a log — basis: the code states "never log auth_info_json: it contains a live, replayable credential" at `semantica/graph_store/amazon_neptune.py:298`, and it is enforced at `semantica/graph_store/amazon_neptune.py:298`
## Process flow

1. A backend name is resolved through the tier registry [D: semantica/vector_store/registry.py:1].
2. Configuration is read from that tier's `config.py` [D: semantica/vector_store/config.py:1].
3. Writes allocate an ID, update metadata and rebuild the index under one lock [D: semantica/vector_store/vector_store.py:569].
4. A save serialises first, writes second [D: semantica/vector_store/faiss_store.py:300].
5. A load clamps the counter above every inferred ID [D: semantica/vector_store/faiss_store.py:393].

## Invariants

- A live ID and a deleted ID never collide [D: semantica/vector_store/vector_store.py:146].
- The Python-side list and the metadata dict mirror the compacted vendor array [D: semantica/vector_store/faiss_store.py:283].

## Implementation status

| rule | status | evidence |
| --- | --- | --- |
| `DOM-003-R1` | wip — unverified, run pytest -q | — |
| `DOM-003-R2` | wip — unverified, run pytest -q | — |
| `DOM-003-R3` | wip — unverified, run pytest -q | — |
| `DOM-003-R4` | wip — unverified, run pytest -q | — |
| `DOM-003-R5` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Open questions

OPEN: which backend is the default for a production deployment? `GRAPH_STORE_DEFAULT_BACKEND` and `SEMANTICA_VECTOR_BACKEND` exist [D: semantica/cli.py:1] and neither names a recommended value in code.
OPEN: what consistency is promised when the same graph is written to a graph store and a vector store? Nothing coordinates the two.
OPEN: are any of the 45 backends unsupported or deprecated? The registries do not say.

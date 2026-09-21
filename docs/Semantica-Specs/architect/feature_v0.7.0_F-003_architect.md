---
title: Feature Architecture v0.7.0 F-003 — Storage Backends
id: F-003
kind: architecture
feature: F-003
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Feature Architecture v0.7.0 F-003 — Storage Backends

> Reversed from code at commit `92c2578a`. The sequence below was read call by call out of the handlers and modules cited.

## Design summary

I: persistence is three parallel registries of vendor adapters sharing one interface each — basis: `graph_store` (11 modules), `vector_store` (19) and `triplet_store` (15) each expose `registry.py`, `config.py` and `methods.py` with per-vendor modules beside them [D: semantica/vector_store/registry.py:1]. It rules out a single storage abstraction across tiers: a graph store and a vector store are configured, and fail, independently.

## API contracts

No HTTP surface. Backends are selected by configuration [D: semantica/cli.py:1].

## Data model

Where `ContextNode` and `ContextEdge` become durable. See `../data/data-erd_v0.7.0_F-003.md`.

## Sequence

1. A backend is resolved by name through the tier's registry [D: semantica/vector_store/registry.py:1].
2. Vector IDs come from a monotonic counter, never decremented on deletion [D: semantica/vector_store/vector_store.py:146].
3. ID allocation, dict write and index rebuild happen under one lock [D: semantica/vector_store/vector_store.py:569].
4. A save serialises IDs, metadata, dimension and index type before touching any file [D: semantica/vector_store/faiss_store.py:300].
5. On load, the counter is clamped to at least the highest inferred `vec_N` [D: semantica/vector_store/faiss_store.py:393].
6. A deletion on a disk-loaded store is persisted [D: semantica/vector_store/faiss_store.py:939].

## Failure modes

| failure | detection | behaviour | source |
| --- | --- | --- | --- |
| Serialisation error during save | serialise before opening any file | on-disk index untouched | [D: semantica/vector_store/faiss_store.py:300] |
| Stale or corrupted persisted counter | clamp to highest inferred ID on load | new IDs cannot collide with survivors | [D: semantica/vector_store/faiss_store.py:393] |
| Concurrent delete during iteration | vectors and metadata snapshotted together under the lock | no `dictionary changed size` error | [D: semantica/vector_store/vector_store.py:801] |
| Zero query vector on a cosine index | substituted with a unit vector | query is accepted by the vendor | [D: semantica/vector_store/pinecone_store.py:746] |
| Deleted vectors resurrected by restart | deletion written back when the store was disk-loaded | deletion survives the restart | [D: semantica/vector_store/faiss_store.py:939] |

## Observability

Logging only. `semantica/utils/logging.py:138` provides `get_logger`; `loguru` and `structlog` are declared dependencies [D: pyproject.toml:19]. No metrics client, tracer or span appears anywhere under `semantica/` — no `prometheus`, `opentelemetry` or `statsd` import exists in the package [D: semantica/utils/logging.py:138].

OPEN: what should this feature emit in production? No metric name, dashboard or alert is defined in the repository.

## Traceability

`DOM-003`, stories `F-003-US1`..`F-003-US3`.

## Open questions

OPEN: what was rejected on the way to this shape? The repository retains no record of alternatives, and none is guessed here.
OPEN: what are the latency, throughput and resource targets for F-003? No budget or SLO is expressed in code.

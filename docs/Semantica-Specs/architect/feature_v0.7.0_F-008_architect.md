---
title: Feature Architecture v0.7.0 F-008 — Export and Interchange
id: F-008
kind: architecture
feature: F-008
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Feature Architecture v0.7.0 F-008 — Export and Interchange

> Reversed from code at commit `92c2578a`. The sequence below was read call by call out of the handlers and modules cited.

## Design summary

I: export is 19 format adapters over one graph reader, and the RDF path is the one with unresolved semantics — basis: each exporter is its own module behind `semantica/export/registry.py:1`, and two of them carry comments about statements landing in the wrong graph and a missing document subject [D: semantica/export/rdf_exporter.py:920].

## API contracts

Three POST routes. Contract: `../data/api-contract_v0.7.0_F-008.md`.

## Data model

Read-only over the graph entities. See `../data/data-erd_v0.7.0_F-008.md`.

## Sequence

1. `POST /api/export` takes an `ExportRequest` and dispatches to a format adapter [D: semantica/explorer/routes/export_import.py:261].
2. `POST /api/export/distance-enriched` adds pairwise distance metrics [D: semantica/explorer/routes/export_import.py:381].
3. `POST /api/import` reads a file and returns an `ImportResponse` [D: semantica/explorer/routes/export_import.py:65].
4. When a caller names a graph, the serializer keeps that name for the caller's statements and writes its own outside it [D: semantica/export/json_exporter.py:514].
5. Graph-level metadata is written only when the caller names the graph [D: semantica/export/rdf_exporter.py:920].

## Failure modes

| failure | detection | behaviour | source |
| --- | --- | --- | --- |
| Caller-named graph capturing the serializer's own statements | statements written to the default graph | a default-graph reader still sees them | [D: semantica/export/json_exporter.py:514] |
| Graph metadata with no subject to attach to | metadata written only when the caller names the graph | no invented document node | [D: semantica/export/rdf_exporter.py:920] |

## Observability

Logging only. `semantica/utils/logging.py:138` provides `get_logger`; `loguru` and `structlog` are declared dependencies [D: pyproject.toml:19]. No metrics client, tracer or span appears anywhere under `semantica/` — no `prometheus`, `opentelemetry` or `statsd` import exists in the package [D: semantica/utils/logging.py:138].

OPEN: what should this feature emit in production? No metric name, dashboard or alert is defined in the repository.

## Traceability

`DOM-008`, stories `F-008-US1`..`F-008-US2`.

## Open questions

OPEN: what was rejected on the way to this shape? The repository retains no record of alternatives, and none is guessed here.
OPEN: what are the latency, throughput and resource targets for F-008? No budget or SLO is expressed in code.

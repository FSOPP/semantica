---
title: Domain — Export and Interchange
id: DOM-008
kind: domain
feature: F-008
status: draft
owner: TBD
updated: 2026-09-21
---

# Domain — Export and Interchange

> Reversed from code at commit `92c2578a`. Every rule below was promoted from a comment or a test name in the code, and cites both the statement and the code that enforces it.

## Ubiquitous language

| term | definition | aliases to avoid |
| --- | --- | --- |
| exporter | A format adapter behind the export registry — 19 exist [D: semantica/export/registry.py:1]. | serializer, writer |
| named graph | A graph the caller identified by name, whose contents belong to the caller [D: semantica/export/json_exporter.py:514]. | context, dataset |
| distance-enriched export | An export carrying pairwise node distance metrics [D: semantica/explorer/routes/export_import.py:381]. | — |

## Actors

Callers of `POST /api/export` and `/api/import` [D: semantica/explorer/routes/export_import.py:261], and CLI users invoking the same exporters.

## Business rules

**`DOM-008-R1`** — The serializer's own statements never land inside a caller-named graph.

I: The serializer's own statements never land inside a caller-named graph — basis: the code states "a caller may hand us a document that is deliberately a named graph; our own statements must not end up inside it, where a default-graph reader would never see them" at `semantica/export/json_exporter.py:514`, and it is enforced at `semantica/export/json_exporter.py:514`
**`DOM-008-R2`** — Graph-level metadata is written only when the caller names the graph.

I: Graph-level metadata is written only when the caller names the graph — basis: the code states "graph-level metadata needs a subject, and this serializer has never minted a document node; rather than invent one, it is written only when the caller names the graph" at `semantica/export/rdf_exporter.py:920`, and it is enforced at `semantica/export/rdf_exporter.py:920`
## Process flow

1. A caller names a format and options [D: semantica/explorer/routes/export_import.py:261].
2. The registry resolves the exporter [D: semantica/export/registry.py:1].
3. Graph data is read from the session [D: semantica/explorer/routes/export_import.py:261].
4. Caller-named graphs keep their name; the serializer writes its own statements outside [D: semantica/export/json_exporter.py:514].
5. Distance metrics are added on the distance-enriched path [D: semantica/explorer/routes/export_import.py:381].

## Invariants

- A default-graph reader always sees the serializer's own statements [D: semantica/export/json_exporter.py:514].
- No document node is invented to carry metadata [D: semantica/export/rdf_exporter.py:920].

## Implementation status

| rule | status | evidence |
| --- | --- | --- |
| `DOM-008-R1` | wip — unverified, run pytest -q | — |
| `DOM-008-R2` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Open questions

OPEN: issue #1147 is named in the code as where the default metadata subject comes from once it lands [D: semantica/export/rdf_exporter.py:920]. Until then, graph-level metadata is silently absent on unnamed exports — is that acceptable to consumers?
OPEN: which of the 19 formats are supported contracts and which are conveniences? The registry treats them identically.
OPEN: is an export expected to round-trip through `POST /api/import`? No test or document asserts it.

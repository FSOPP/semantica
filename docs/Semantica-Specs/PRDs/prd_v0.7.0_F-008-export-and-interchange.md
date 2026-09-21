---
title: PRD v0.7.0 F-008 — Export and Interchange
id: F-008
kind: prd
feature: F-008
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# PRD v0.7.0 F-008 — Export and Interchange

> **Reversed, and weakly.** A requirement states intent; intent is not in a repository. Every story below was inferred from endpoints and test names, and every business question is `OPEN:`.

## Summary

I: Export and Interchange exists to let the graph leave the system in a form something else can read — basis: the surface this feature exposes and the tests that assert it, as catalogued in `../data/api-contract_v0.7.0_F-008.md` and `../tests/test_v0.7.0_F-008.md`.

## User stories

**`F-008-US1`** — As an analyst, I want to export a graph into the format my downstream tool reads, so that the graph is not trapped in this system.

I: inferred from the shipped surface — basis: 19 exporters [D: semantica/export/registry.py:1]

**`F-008-US2`** — As an RDF consumer, I want to read an exported graph with a default-graph reader and still see its provenance, so that exported provenance is not hidden in a named graph.

I: inferred from the shipped surface — basis: default-graph discipline [D: semantica/export/json_exporter.py:514]

## Acceptance criteria

- **`F-008-US1`** — Given the feature is configured, when export a graph into the format my downstream tool reads, then the behaviour named in `19 exporters` holds. I: lifted from the shipped surface, not from a stated requirement — basis: 19 exporters [D: semantica/export/registry.py:1]
- **`F-008-US2`** — Given the feature is configured, when read an exported graph with a default-graph reader and still see its provenance, then the behaviour named in `default-graph discipline` holds. I: lifted from the shipped surface, not from a stated requirement — basis: default-graph discipline [D: semantica/export/json_exporter.py:514]

## Implementation status

| story | status | evidence |
| --- | --- | --- |
| `F-008-US1` | wip — unverified, run pytest -q | — |
| `F-008-US2` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Scope boundaries

OPEN: what is deliberately out of scope for this feature? The code draws module boundaries; it does not record a decision to exclude anything.

## Dependencies

Domain rules: `DOM-008`. Architecture: `../architect/feature_v0.7.0_F-008_architect.md`. Other features this one imports from are listed in `../architect/architect.md`.

## Metrics

OPEN: how is success measured for this feature after release? No metric, event or analytics call exists in the code.
OPEN: what is the business priority of this feature relative to the other eight? Nothing in the repository ranks them.

## Open questions

OPEN: who asked for this, and what problem were they reporting? Not recoverable from the working tree.
OPEN: which stories are load-bearing for a paying user and which are conveniences? The code treats every route identically.

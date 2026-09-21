---
title: PRD v0.7.0 F-001 — Ingest and Parse Pipeline
id: F-001
kind: prd
feature: F-001
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# PRD v0.7.0 F-001 — Ingest and Parse Pipeline

> **Reversed, and weakly.** A requirement states intent; intent is not in a repository. Every story below was inferred from endpoints and test names, and every business question is `OPEN:`.

## Summary

I: Ingest and Parse Pipeline exists to get data out of many systems and into one normalised chunk stream — basis: the surface this feature exposes and the tests that assert it, as catalogued in `../data/api-contract_v0.7.0_F-001.md` and `../tests/test_v0.7.0_F-001.md`.

## User stories

**`F-001-US1`** — As an operator, I want to connect a source system by naming it and supplying credentials, so that I do not write a connector per system.

I: inferred from the shipped surface — basis: 34 connectors resolve by name [D: semantica/ingest/registry.py:1]

**`F-001-US2`** — As a security reviewer, I want to know that user-supplied ingest targets cannot reach internal addresses, so that opening the ingest API to users is not an SSRF hole.

I: inferred from the shipped surface — basis: SSRF validation precedes every outbound call [D: semantica/ingest/ssrf.py:1]

**`F-001-US3`** — As an operator, I want to feed any of 22 document formats into the same pipeline, so that format choice is not an integration decision.

I: inferred from the shipped surface — basis: 22 parsers resolve by format [D: semantica/parse/registry.py:1]

## Acceptance criteria

- **`F-001-US1`** — Given the feature is configured, when connect a source system by naming it and supplying credentials, then the behaviour named in `34 connectors resolve by name` holds. I: lifted from the shipped surface, not from a stated requirement — basis: 34 connectors resolve by name [D: semantica/ingest/registry.py:1]
- **`F-001-US2`** — Given the feature is configured, when know that user-supplied ingest targets cannot reach internal addresses, then the behaviour named in `SSRF validation precedes every outbound call` holds. I: lifted from the shipped surface, not from a stated requirement — basis: SSRF validation precedes every outbound call [D: semantica/ingest/ssrf.py:1]
- **`F-001-US3`** — Given the feature is configured, when feed any of 22 document formats into the same pipeline, then the behaviour named in `22 parsers resolve by format` holds. I: lifted from the shipped surface, not from a stated requirement — basis: 22 parsers resolve by format [D: semantica/parse/registry.py:1]

## Implementation status

| story | status | evidence |
| --- | --- | --- |
| `F-001-US1` | wip — unverified, run pytest -q | — |
| `F-001-US2` | wip — unverified, run pytest -q | — |
| `F-001-US3` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Scope boundaries

OPEN: what is deliberately out of scope for this feature? The code draws module boundaries; it does not record a decision to exclude anything.

## Dependencies

Domain rules: `DOM-001`. Architecture: `../architect/feature_v0.7.0_F-001_architect.md`. Other features this one imports from are listed in `../architect/architect.md`.

## Metrics

OPEN: how is success measured for this feature after release? No metric, event or analytics call exists in the code.
OPEN: what is the business priority of this feature relative to the other eight? Nothing in the repository ranks them.

## Open questions

OPEN: who asked for this, and what problem were they reporting? Not recoverable from the working tree.
OPEN: which stories are load-bearing for a paying user and which are conveniences? The code treats every route identically.

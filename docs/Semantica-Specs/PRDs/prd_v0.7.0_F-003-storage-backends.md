---
title: PRD v0.7.0 F-003 — Storage Backends
id: F-003
kind: prd
feature: F-003
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# PRD v0.7.0 F-003 — Storage Backends

> **Reversed, and weakly.** A requirement states intent; intent is not in a repository. Every story below was inferred from endpoints and test names, and every business question is `OPEN:`.

## Summary

I: Storage Backends exists to keep that graph durable across three families of backend — basis: the surface this feature exposes and the tests that assert it, as catalogued in `../data/api-contract_v0.7.0_F-003.md` and `../tests/test_v0.7.0_F-003.md`.

## User stories

**`F-003-US1`** — As an operator, I want to choose a graph, vector or triplet backend by configuration, so that my storage choice is not a rewrite.

I: inferred from the shipped surface — basis: three registries of 11, 19 and 15 backends [D: semantica/vector_store/registry.py:1]

**`F-003-US2`** — As an operator, I want to survive a crash during a save without losing the index, so that a disk-full error is not data loss.

I: inferred from the shipped surface — basis: serialise-before-write [D: semantica/vector_store/faiss_store.py:300]

**`F-003-US3`** — As a data steward, I want to know a deleted vector stays deleted across a restart, so that deletion is a real deletion.

I: inferred from the shipped surface — basis: deletion persisted on disk-loaded stores [D: semantica/vector_store/faiss_store.py:939]

## Acceptance criteria

- **`F-003-US1`** — Given the feature is configured, when choose a graph, vector or triplet backend by configuration, then the behaviour named in `three registries of 11, 19 and 15 backends` holds. I: lifted from the shipped surface, not from a stated requirement — basis: three registries of 11, 19 and 15 backends [D: semantica/vector_store/registry.py:1]
- **`F-003-US2`** — Given the feature is configured, when survive a crash during a save without losing the index, then the behaviour named in `serialise-before-write` holds. I: lifted from the shipped surface, not from a stated requirement — basis: serialise-before-write [D: semantica/vector_store/faiss_store.py:300]
- **`F-003-US3`** — Given the feature is configured, when know a deleted vector stays deleted across a restart, then the behaviour named in `deletion persisted on disk-loaded stores` holds. I: lifted from the shipped surface, not from a stated requirement — basis: deletion persisted on disk-loaded stores [D: semantica/vector_store/faiss_store.py:939]

## Implementation status

| story | status | evidence |
| --- | --- | --- |
| `F-003-US1` | wip — unverified, run pytest -q | — |
| `F-003-US2` | wip — unverified, run pytest -q | — |
| `F-003-US3` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Scope boundaries

OPEN: what is deliberately out of scope for this feature? The code draws module boundaries; it does not record a decision to exclude anything.

## Dependencies

Domain rules: `DOM-003`. Architecture: `../architect/feature_v0.7.0_F-003_architect.md`. Other features this one imports from are listed in `../architect/architect.md`.

## Metrics

OPEN: how is success measured for this feature after release? No metric, event or analytics call exists in the code.
OPEN: what is the business priority of this feature relative to the other eight? Nothing in the repository ranks them.

## Open questions

OPEN: who asked for this, and what problem were they reporting? Not recoverable from the working tree.
OPEN: which stories are load-bearing for a paying user and which are conveniences? The code treats every route identically.

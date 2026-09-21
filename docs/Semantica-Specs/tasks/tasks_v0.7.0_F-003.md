---
title: Tasks v0.7.0 F-003 — Storage Backends
id: F-003
kind: tasks
feature: F-003
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Tasks v0.7.0 F-003 — Storage Backends

> **This document is as-built.** Each row is a unit of work that already shipped, pointing at the artifact that exists. It is an inventory, not a plan.

## Task list

| task | description | depends-on | artifact | done-when | status |
| --- | --- | --- | --- | --- | --- |
| `F-003-T1` | Graph store tier — 11 backends | — | `semantica/graph_store/registry.py` | each backend resolves and round-trips a graph | wip — unverified, run pytest -q |
| `F-003-T2` | Vector store tier — 19 backends | `F-003-T1` | `semantica/vector_store/registry.py` | each backend resolves and round-trips vectors | wip — unverified, run pytest -q |
| `F-003-T3` | Triplet store tier — 15 backends | `F-003-T2` | `semantica/triplet_store/registry.py` | each backend resolves and round-trips triples | wip — unverified, run pytest -q |
| `F-003-T4` | Monotonic, never-reused vector IDs | `F-003-T3` | `semantica/vector_store/vector_store.py` | a deleted ID is never handed out again | wip — unverified, run pytest -q |
| `F-003-T5` | Crash-safe FAISS persistence | `F-003-T4` | `semantica/vector_store/faiss_store.py` | a failed save leaves the previous index intact | wip — unverified, run pytest -q |
| `F-003-T6` | Query sanitisation per tier | `F-003-T5` | `semantica/graph_store/query_sanitize.py` | query text from a caller cannot alter query structure | wip — unverified, run pytest -q |

The `done-when` column states the check that would prove the row, which is what a `done` has to cash. States and transitions: `../status-model.md`.

## Execution order

As-built, the order is the dependency chain above. Nothing in the repository records the order these were actually built in — `git log` ranks by churn, which is not the same thing.

## Definition of done

- The artifact exists and is imported or routed from the feature's entry point.
- A test in `../tests/test_v0.7.0_F-003.md` names the behaviour.
- The suite passed here, with the command in the status note.

## Open questions

OPEN: which of these were one change and which were a year of iteration? The task granularity here is the module, not the commit.
OPEN: what work is in flight now? This inventory describes the tree at commit `92c2578a` and nothing else.

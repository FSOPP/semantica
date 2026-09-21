---
title: Tasks v0.7.0 F-005 — Context Graph and Decision Intelligence
id: F-005
kind: tasks
feature: F-005
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Tasks v0.7.0 F-005 — Context Graph and Decision Intelligence

> **This document is as-built.** Each row is a unit of work that already shipped, pointing at the artifact that exists. It is an inventory, not a plan.

## Task list

| task | description | depends-on | artifact | done-when | status |
| --- | --- | --- | --- | --- | --- |
| `F-005-T1` | Context graph with validity windows | — | `semantica/context/context_graph.py` | a node reports active or inactive for a given time | wip — unverified, run pytest -q |
| `F-005-T2` | Atomic graph persistence | `F-005-T1` | `semantica/context/context_graph.py` | a crash during save leaves old or new contents, never partial | wip — unverified, run pytest -q |
| `F-005-T3` | Decision recording as typed nodes | `F-005-T2` | `semantica/explorer/routes/decisions.py` | `GET /api/decisions` lists them | wip — unverified, run pytest -q |
| `F-005-T4` | Causal chain, precedents and compliance | `F-005-T3` | `semantica/explorer/routes/decisions.py` | the three sub-routes respond for a known decision | wip — unverified, run pytest -q |
| `F-005-T5` | Agent memory listing | `F-005-T4` | `semantica/explorer/routes/memories.py` | `GET /api/memories` returns excerpts | wip — unverified, run pytest -q |
| `F-005-T6` | Graph analytics and validation report | `F-005-T5` | `semantica/explorer/routes/analytics.py` | both analytics routes respond | wip — unverified, run pytest -q |

The `done-when` column states the check that would prove the row, which is what a `done` has to cash. States and transitions: `../status-model.md`.

## Execution order

As-built, the order is the dependency chain above. Nothing in the repository records the order these were actually built in — `git log` ranks by churn, which is not the same thing.

## Definition of done

- The artifact exists and is imported or routed from the feature's entry point.
- A test in `../tests/test_v0.7.0_F-005.md` names the behaviour.
- The suite passed here, with the command in the status note.

## Open questions

OPEN: which of these were one change and which were a year of iteration? The task granularity here is the module, not the commit.
OPEN: what work is in flight now? This inventory describes the tree at commit `92c2578a` and nothing else.

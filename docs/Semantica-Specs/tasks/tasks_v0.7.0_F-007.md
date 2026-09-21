---
title: Tasks v0.7.0 F-007 — Knowledge Explorer UI and Graph API
id: F-007
kind: tasks
feature: F-007
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Tasks v0.7.0 F-007 — Knowledge Explorer UI and Graph API

> **This document is as-built.** Each row is a unit of work that already shipped, pointing at the artifact that exists. It is an inventory, not a plan.

## Task list

| task | description | depends-on | artifact | done-when | status |
| --- | --- | --- | --- | --- | --- |
| `F-007-T1` | Explorer FastAPI application and router mounting | — | `semantica/explorer/app.py` | thirteen routers mount behind `require_auth` | wip — unverified, run pytest -q |
| `F-007-T2` | Graph read API with cursor pagination | `F-007-T1` | `semantica/explorer/routes/graph.py` | nodes and edges page forward with an opaque cursor | wip — unverified, run pytest -q |
| `F-007-T3` | Temporal API — snapshot, diff, bounds, patterns | `F-007-T2` | `semantica/explorer/routes/temporal.py` | the five temporal routes respond | wip — unverified, run pytest -q |
| `F-007-T4` | Markdown resource read and apply | `F-007-T3` | `semantica/explorer/routes/markdown.py` | a stale revision is refused with a conflict | wip — unverified, run pytest -q |
| `F-007-T5` | Annotations CRUD on the session | `F-007-T4` | `semantica/explorer/routes/annotations.py` | create returns 201, delete returns 204, unknown node returns 404 | wip — unverified, run pytest -q |
| `F-007-T6` | React Explorer SPA | `F-007-T5` | `explorer/src/App.tsx` | `npm run build` produces the bundle the package ships | wip — unverified, run pytest -q |
| `F-007-T7` | Graph updates WebSocket | `F-007-T6` | `semantica/explorer/ws.py` | the channel accepts a connection with a valid key | wip — unverified, run pytest -q |

The `done-when` column states the check that would prove the row, which is what a `done` has to cash. States and transitions: `../status-model.md`.

## Execution order

As-built, the order is the dependency chain above. Nothing in the repository records the order these were actually built in — `git log` ranks by churn, which is not the same thing.

## Definition of done

- The artifact exists and is imported or routed from the feature's entry point.
- A test in `../tests/test_v0.7.0_F-007.md` names the behaviour.
- The suite passed here, with the command in the status note.

## Open questions

OPEN: which of these were one change and which were a year of iteration? The task granularity here is the module, not the commit.
OPEN: what work is in flight now? This inventory describes the tree at commit `92c2578a` and nothing else.

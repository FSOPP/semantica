---
title: Tasks v0.7.0 F-006 — Provenance Reasoning and Explainability
id: F-006
kind: tasks
feature: F-006
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Tasks v0.7.0 F-006 — Provenance Reasoning and Explainability

> **This document is as-built.** Each row is a unit of work that already shipped, pointing at the artifact that exists. It is an inventory, not a plan.

## Task list

| task | description | depends-on | artifact | done-when | status |
| --- | --- | --- | --- | --- | --- |
| `F-006-T1` | W3C PROV-O provenance records | — | `semantica/provenance/manager.py` | a qualified association carries `hadRole` | wip — unverified, run pytest -q |
| `F-006-T2` | Provenance read API | `F-006-T1` | `semantica/explorer/routes/provenance.py` | `/api/provenance` and `/report` respond | wip — unverified, run pytest -q |
| `F-006-T3` | Rete, Datalog and SPARQL reasoners | `F-006-T2` | `semantica/reasoning/sparql_reasoner.py` | `POST /api/reason` returns inferences | wip — unverified, run pytest -q |
| `F-006-T4` | Fixpoint rule iteration | `F-006-T3` | `semantica/reasoning/sparql_reasoner.py` | a rule chain terminates at fixpoint | wip — unverified, run pytest -q |
| `F-006-T5` | Truth maintenance with immutable rule snapshots | `F-006-T4` | `semantica/reasoning/truth_maintenance_types.py` | mutating the original rule does not affect a running session | wip — unverified, run pytest -q |
| `F-006-T6` | Pipeline execution engine with typed contracts | `F-006-T5` | `semantica/pipeline/execution_engine.py` | a contract violation fails without consuming a retry | wip — unverified, run pytest -q |

The `done-when` column states the check that would prove the row, which is what a `done` has to cash. States and transitions: `../status-model.md`.

## Execution order

As-built, the order is the dependency chain above. Nothing in the repository records the order these were actually built in — `git log` ranks by churn, which is not the same thing.

## Definition of done

- The artifact exists and is imported or routed from the feature's entry point.
- A test in `../tests/test_v0.7.0_F-006.md` names the behaviour.
- The suite passed here, with the command in the status note.

## Open questions

OPEN: which of these were one change and which were a year of iteration? The task granularity here is the module, not the commit.
OPEN: what work is in flight now? This inventory describes the tree at commit `92c2578a` and nothing else.

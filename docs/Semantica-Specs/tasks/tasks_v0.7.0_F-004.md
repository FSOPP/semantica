---
title: Tasks v0.7.0 F-004 — Ontology and Vocabulary Management
id: F-004
kind: tasks
feature: F-004
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Tasks v0.7.0 F-004 — Ontology and Vocabulary Management

> **This document is as-built.** Each row is a unit of work that already shipped, pointing at the artifact that exists. It is an inventory, not a plan.

## Task list

| task | description | depends-on | artifact | done-when | status |
| --- | --- | --- | --- | --- | --- |
| `F-004-T1` | Ontology registry, preview and load | — | `semantica/explorer/routes/ontology.py` | `/registry`, `/preview`, `/load` respond | wip — unverified, run pytest -q |
| `F-004-T2` | Draft and proposal workflow | `F-004-T1` | `semantica/explorer/routes/ontology.py` | propose, approve, reject, publish and comment each respond | wip — unverified, run pytest -q |
| `F-004-T3` | SHACL generation and bounded validation | `F-004-T2` | `semantica/explorer/routes/ontology.py` | validation refuses a payload past any of the four ceilings | wip — unverified, run pytest -q |
| `F-004-T4` | SKOS scheme and concept surface | `F-004-T3` | `semantica/explorer/routes/ontology.py` | `/skos/schemes`, `/skos/search`, `/skos/concept/{uri}` respond | wip — unverified, run pytest -q |
| `F-004-T5` | Alignment listing, upsert, delete and suggestion | `F-004-T4` | `semantica/explorer/routes/ontology.py` | the four alignment routes respond | wip — unverified, run pytest -q |
| `F-004-T6` | Vocabulary API | `F-004-T5` | `semantica/explorer/routes/vocabulary.py` | concepts, hierarchy, schemes and import respond | wip — unverified, run pytest -q |
| `F-004-T7` | SPARQL endpoint | `F-004-T6` | `semantica/explorer/routes/sparql.py` | `POST /api/sparql` executes a query | wip — unverified, run pytest -q |

The `done-when` column states the check that would prove the row, which is what a `done` has to cash. States and transitions: `../status-model.md`.

## Execution order

As-built, the order is the dependency chain above. Nothing in the repository records the order these were actually built in — `git log` ranks by churn, which is not the same thing.

## Definition of done

- The artifact exists and is imported or routed from the feature's entry point.
- A test in `../tests/test_v0.7.0_F-004.md` names the behaviour.
- The suite passed here, with the command in the status note.

## Open questions

OPEN: which of these were one change and which were a year of iteration? The task granularity here is the module, not the commit.
OPEN: what work is in flight now? This inventory describes the tree at commit `92c2578a` and nothing else.

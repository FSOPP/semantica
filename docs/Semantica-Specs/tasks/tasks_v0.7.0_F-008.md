---
title: Tasks v0.7.0 F-008 — Export and Interchange
id: F-008
kind: tasks
feature: F-008
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Tasks v0.7.0 F-008 — Export and Interchange

> **This document is as-built.** Each row is a unit of work that already shipped, pointing at the artifact that exists. It is an inventory, not a plan.

## Task list

| task | description | depends-on | artifact | done-when | status |
| --- | --- | --- | --- | --- | --- |
| `F-008-T1` | 19 export format adapters | — | `semantica/export/registry.py` | each format resolves and writes | wip — unverified, run pytest -q |
| `F-008-T2` | Export and import HTTP routes | `F-008-T1` | `semantica/explorer/routes/export_import.py` | `/api/export`, `/api/export/distance-enriched` and `/api/import` respond | wip — unverified, run pytest -q |
| `F-008-T3` | Default-graph discipline in JSON-LD export | `F-008-T2` | `semantica/export/json_exporter.py` | a caller-named graph does not capture the serializer's own statements | wip — unverified, run pytest -q |
| `F-008-T4` | RDF export with caller-named graph metadata | `F-008-T3` | `semantica/export/rdf_exporter.py` | metadata is written only when the caller names the graph | wip — unverified, run pytest -q |
| `F-008-T5` | Distance-enriched export path | `F-008-T4` | `semantica/export/distance_exporter.py` | pairwise distances are attached | wip — unverified, run pytest -q |

The `done-when` column states the check that would prove the row, which is what a `done` has to cash. States and transitions: `../status-model.md`.

## Execution order

As-built, the order is the dependency chain above. Nothing in the repository records the order these were actually built in — `git log` ranks by churn, which is not the same thing.

## Definition of done

- The artifact exists and is imported or routed from the feature's entry point.
- A test in `../tests/test_v0.7.0_F-008.md` names the behaviour.
- The suite passed here, with the command in the status note.

## Open questions

OPEN: which of these were one change and which were a year of iteration? The task granularity here is the module, not the commit.
OPEN: what work is in flight now? This inventory describes the tree at commit `92c2578a` and nothing else.

---
title: Tasks v0.7.0 F-002 — Knowledge Graph Construction and Semantic Extraction
id: F-002
kind: tasks
feature: F-002
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Tasks v0.7.0 F-002 — Knowledge Graph Construction and Semantic Extraction

> **This document is as-built.** Each row is a unit of work that already shipped, pointing at the artifact that exists. It is an inventory, not a plan.

## Task list

| task | description | depends-on | artifact | done-when | status |
| --- | --- | --- | --- | --- | --- |
| `F-002-T1` | Entity and relation extraction with confidence thresholds | — | `semantica/explorer/routes/enrich.py` | `POST /api/enrich/extract` returns entities and relations | wip — unverified, run pytest -q |
| `F-002-T2` | Heuristic confidence scoring for unmeasured entities | `F-002-T1` | `semantica/semantic_extract/ner_extractor.py` | every emitted entity carries a confidence | wip — unverified, run pytest -q |
| `F-002-T3` | Schema validation of labels and predicates | `F-002-T2` | `semantica/semantic_extract/schema_validator.py` | an out-of-schema label or predicate is rejected | wip — unverified, run pytest -q |
| `F-002-T4` | Locked extraction cache | `F-002-T3` | `semantica/semantic_extract/cache.py` | a corrupt row is evictable and a failed transaction cannot be committed over | wip — unverified, run pytest -q |
| `F-002-T5` | Duplicate detection and entity merging | `F-002-T4` | `semantica/deduplication/duplicate_detector.py` | `POST /api/enrich/dedup` and `/merge` respond | wip — unverified, run pytest -q |
| `F-002-T6` | Graph construction from extracted entities | `F-002-T5` | `semantica/kg/graph_builder.py` | nodes and edges are materialised, synthetic endpoints promoted | wip — unverified, run pytest -q |

The `done-when` column states the check that would prove the row, which is what a `done` has to cash. States and transitions: `../status-model.md`.

## Execution order

As-built, the order is the dependency chain above. Nothing in the repository records the order these were actually built in — `git log` ranks by churn, which is not the same thing.

## Definition of done

- The artifact exists and is imported or routed from the feature's entry point.
- A test in `../tests/test_v0.7.0_F-002.md` names the behaviour.
- The suite passed here, with the command in the status note.

## Open questions

OPEN: which of these were one change and which were a year of iteration? The task granularity here is the module, not the commit.
OPEN: what work is in flight now? This inventory describes the tree at commit `92c2578a` and nothing else.

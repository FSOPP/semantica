---
title: Tasks v0.7.0 F-001 — Ingest and Parse Pipeline
id: F-001
kind: tasks
feature: F-001
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Tasks v0.7.0 F-001 — Ingest and Parse Pipeline

> **This document is as-built.** Each row is a unit of work that already shipped, pointing at the artifact that exists. It is an inventory, not a plan.

## Task list

| task | description | depends-on | artifact | done-when | status |
| --- | --- | --- | --- | --- | --- |
| `F-001-T1` | 34 source connectors behind one registry | — | `semantica/ingest/registry.py` | `semantica.ingest` resolves every connector by name and each returns records | wip — unverified, run pytest -q |
| `F-001-T2` | SSRF validation on every outbound ingest URL | `F-001-T1` | `semantica/ingest/ssrf.py` | a private, loopback or link-local target is refused before the request | wip — unverified, run pytest -q |
| `F-001-T3` | Cross-origin credential stripping during pagination | `F-001-T2` | `semantica/ingest/sap_ingestor.py` | a next link to another origin does not carry the session credential | wip — unverified, run pytest -q |
| `F-001-T4` | 22 format parsers behind one registry | `F-001-T3` | `semantica/parse/registry.py` | every supported format resolves to a parser | wip — unverified, run pytest -q |
| `F-001-T5` | Normalisation and splitting stages | `F-001-T4` | `semantica/split/methods.py` | chunks are produced from normalised content | wip — unverified, run pytest -q |
| `F-001-T6` | Credential-safe error paths across cloud connectors | `F-001-T5` | `semantica/ingest/redshift_ingestor.py` | no connector error path logs a credential | wip — unverified, run pytest -q |

The `done-when` column states the check that would prove the row, which is what a `done` has to cash. States and transitions: `../status-model.md`.

## Execution order

As-built, the order is the dependency chain above. Nothing in the repository records the order these were actually built in — `git log` ranks by churn, which is not the same thing.

## Definition of done

- The artifact exists and is imported or routed from the feature's entry point.
- A test in `../tests/test_v0.7.0_F-001.md` names the behaviour.
- The suite passed here, with the command in the status note.

## Open questions

OPEN: which of these were one change and which were a year of iteration? The task granularity here is the module, not the commit.
OPEN: what work is in flight now? This inventory describes the tree at commit `92c2578a` and nothing else.

---
title: Tasks v0.7.0 F-009 — CLI MCP Server and Agent Integrations
id: F-009
kind: tasks
feature: F-009
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Tasks v0.7.0 F-009 — CLI MCP Server and Agent Integrations

> **This document is as-built.** Each row is a unit of work that already shipped, pointing at the artifact that exists. It is an inventory, not a plan.

## Task list

| task | description | depends-on | artifact | done-when | status |
| --- | --- | --- | --- | --- | --- |
| `F-009-T1` | CLI with six command groups and 91 commands | — | `semantica/cli.py` | `semantica --help` lists the groups | wip — unverified, run pytest -q |
| `F-009-T2` | JSON Lines output discipline | `F-009-T1` | `semantica/cli.py` | every record occupies exactly one line | wip — unverified, run pytest -q |
| `F-009-T3` | MCP JSON-RPC server and seven tool modules | `F-009-T2` | `semantica_mcp/mcp/server.py` | `tools/list` and `tools/call` respond | wip — unverified, run pytest -q |
| `F-009-T4` | Second FastAPI application | `F-009-T3` | `semantica/server.py` | `/api/info`, `/health` and `/build` respond | wip — unverified, run pytest -q |
| `F-009-T5` | Agent integrations — agno, crewai, google_adk | `F-009-T4` | `integrations/crewai/kg_tool.py` | each adapter exposes its tools | wip — unverified, run pytest -q |
| `F-009-T6` | Per-graph re-entrant locking in agent tools | `F-009-T5` | `integrations/crewai/kg_tool.py` | concurrent adds on one graph do not double-count | wip — unverified, run pytest -q |

The `done-when` column states the check that would prove the row, which is what a `done` has to cash. States and transitions: `../status-model.md`.

## Execution order

As-built, the order is the dependency chain above. Nothing in the repository records the order these were actually built in — `git log` ranks by churn, which is not the same thing.

## Definition of done

- The artifact exists and is imported or routed from the feature's entry point.
- A test in `../tests/test_v0.7.0_F-009.md` names the behaviour.
- The suite passed here, with the command in the status note.

## Open questions

OPEN: which of these were one change and which were a year of iteration? The task granularity here is the module, not the commit.
OPEN: what work is in flight now? This inventory describes the tree at commit `92c2578a` and nothing else.

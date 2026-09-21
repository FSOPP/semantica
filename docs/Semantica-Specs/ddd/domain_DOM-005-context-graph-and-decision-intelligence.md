---
title: Domain — Context Graph and Decision Intelligence
id: DOM-005
kind: domain
feature: F-005
status: draft
owner: TBD
updated: 2026-09-21
---

# Domain — Context Graph and Decision Intelligence

> Reversed from code at commit `92c2578a`. Every rule below was promoted from a comment or a test name in the code, and cites both the statement and the code that enforces it.

## Ubiquitous language

| term | definition | aliases to avoid |
| --- | --- | --- |
| context graph | The persisted graph of nodes and edges with validity bounds [D: semantica/context/context_graph.py:563]. | knowledge graph — the KG is built in F-002 |
| decision | A context node of `node_type` `decision`, projected into `DecisionResponse` [D: semantica/explorer/routes/decisions.py:17]. | record, event |
| causal chain | The ordered antecedents of a decision [D: semantica/explorer/routes/decisions.py:83]. | history |
| precedent | An earlier decision returned as comparable [D: semantica/explorer/routes/decisions.py:106]. | — |
| agent memory | Stored agent recall items, listed as excerpts [D: semantica/explorer/routes/memories.py:12]. | cache |

## Actors

Agents writing decisions and memories through the Python API, and auditors reading them through `/api/decisions` [D: semantica/explorer/routes/decisions.py:31].

## Business rules

**`DOM-005-R1`** — A persisted graph file is either the old contents or the new contents, never a partial write.

I: A persisted graph file is either the old contents or the new contents, never a partial write — basis: the code states "serialize to a sibling temp file then replace the destination in one OS-level rename" at `semantica/context/context_graph.py:1409`, and it is enforced at `semantica/context/context_graph.py:1409`
**`DOM-005-R2`** — An entity-only export never emits a relationship endpoint that is absent from the export.

I: An entity-only export never emits a relationship endpoint that is absent from the export — basis: the code states "drop relationships whose endpoints were filtered out so downstream consumers never see an absent source_id/target_id" at `semantica/context/context_graph.py:3652`, and it is enforced at `semantica/context/context_graph.py:3652`
**`DOM-005-R3`** — A decision is a context node, not a separate record.

I: A decision is a context node, not a separate record — basis: the code states "list_decisions filters nodes by node_type 'decision' and builds every response field from that node's properties" at `semantica/explorer/routes/decisions.py:17`, and it is enforced at `semantica/explorer/routes/decisions.py:31`
**`DOM-005-R4`** — A decision's confidence is always a float.

I: A decision's confidence is always a float — basis: the code states "confidence is coerced with a 0.0 fallback when the property is absent or unparseable" at `semantica/explorer/routes/decisions.py:17`, and it is enforced at `semantica/explorer/routes/decisions.py:17`
## Process flow

1. An agent records a decision as a typed node [D: semantica/context/context_graph.py:563].
2. The graph is persisted atomically [D: semantica/context/context_graph.py:1409].
3. An auditor lists decisions, filtered by category [D: semantica/explorer/routes/decisions.py:31].
4. The causal chain is walked [D: semantica/explorer/routes/decisions.py:83].
5. Precedents and compliance are checked [D: semantica/explorer/routes/decisions.py:145].
6. Analytics and validation summarise the graph [D: semantica/explorer/routes/analytics.py:17].

## Invariants

- A node's validity window is respected by `is_active` at read time [D: semantica/context/context_graph.py:429].
- The persisted file is never partially written [D: semantica/context/context_graph.py:1409].

## Implementation status

| rule | status | evidence |
| --- | --- | --- |
| `DOM-005-R1` | wip — unverified, run pytest -q | — |
| `DOM-005-R2` | wip — unverified, run pytest -q | — |
| `DOM-005-R3` | wip — unverified, run pytest -q | — |
| `DOM-005-R4` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Open questions

OPEN: is a recorded decision immutable? No update or delete route exists, and nothing forbids an in-process rewrite.
OPEN: `GET /api/decisions` loads with an internal limit of 999999 before slicing in Python [D: semantica/explorer/routes/decisions.py:31]. What graph size is that expected to hold up at?
OPEN: what makes a decision compliant? `/compliance` returns a verdict [D: semantica/explorer/routes/decisions.py:145] and the policy it applies is not stated in the document layer.

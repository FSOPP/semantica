---
title: Feature Architecture v0.7.0 F-005 — Context Graph and Decision Intelligence
id: F-005
kind: architecture
feature: F-005
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Feature Architecture v0.7.0 F-005 — Context Graph and Decision Intelligence

> Reversed from code at commit `92c2578a`. The sequence below was read call by call out of the handlers and modules cited.

## Design summary

I: a decision is not a separate store but a typed node in the context graph — basis: `list_decisions` filters context nodes by `node_type="decision"` and builds the response entirely from that node's `properties` dict [D: semantica/explorer/routes/decisions.py:17]. It rules out decision-specific persistence, and it means every graph guarantee applies to decisions unchanged.

## API contracts

Nine read-only routes. Contract: `../data/api-contract_v0.7.0_F-005.md`.

## Data model

Owns `DecisionResponse`, `MemorySummaryResponse`; writes `ContextNode`. See `../data/data-erd_v0.7.0_F-005.md`.

## Sequence

1. `GET /api/decisions` loads nodes of type `decision` with an unbounded internal limit of 999999, then filters and slices in Python [D: semantica/explorer/routes/decisions.py:31].
2. `_node_to_decision` maps properties onto the response, coercing `confidence` to float with a `0.0` fallback [D: semantica/explorer/routes/decisions.py:17].
3. `GET /api/decisions/{id}/chain` walks the causal chain [D: semantica/explorer/routes/decisions.py:83]; `/precedents` and `/compliance` follow [D: semantica/explorer/routes/decisions.py:106].
4. Graph writes hold the SKOS hierarchy invariant at the lowest write layer, below API and session checks [D: semantica/context/context_graph.py:759].
5. Persistence is a serialise-to-sibling-then-rename [D: semantica/context/context_graph.py:1409].

## Failure modes

| failure | detection | behaviour | source |
| --- | --- | --- | --- |
| Crash or disk-full during save | atomic temp-file rename | file is old contents or new, never partial | [D: semantica/context/context_graph.py:1409] |
| Entity-only export leaving dangling endpoints | endpoint-filtered relationships dropped | no absent `source_id`/`target_id` is emitted | [D: semantica/context/context_graph.py:3652] |
| Direct graph write bypassing API checks | invariant enforced at the lowest write layer | SKOS hierarchy holds regardless of caller | [D: semantica/context/context_graph.py:759] |
| Unknown decision id | 404 from the route | `{"detail": ...}` | [D: tests/explorer/test_decisions_causal_distance_route.py:81] |

## Observability

Logging only. `semantica/utils/logging.py:138` provides `get_logger`; `loguru` and `structlog` are declared dependencies [D: pyproject.toml:19]. No metrics client, tracer or span appears anywhere under `semantica/` — no `prometheus`, `opentelemetry` or `statsd` import exists in the package [D: semantica/utils/logging.py:138].

OPEN: what should this feature emit in production? No metric name, dashboard or alert is defined in the repository.

## Traceability

`DOM-005`, stories `F-005-US1`..`F-005-US3`.

## Open questions

OPEN: what was rejected on the way to this shape? The repository retains no record of alternatives, and none is guessed here.
OPEN: what are the latency, throughput and resource targets for F-005? No budget or SLO is expressed in code.

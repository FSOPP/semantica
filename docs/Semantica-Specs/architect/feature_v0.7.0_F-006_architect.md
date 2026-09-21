---
title: Feature Architecture v0.7.0 F-006 — Provenance Reasoning and Explainability
id: F-006
kind: architecture
feature: F-006
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Feature Architecture v0.7.0 F-006 — Provenance Reasoning and Explainability

> Reversed from code at commit `92c2578a`. The sequence below was read call by call out of the handlers and modules cited.

## Design summary

I: provenance and reasoning are one feature, both answering "where did this triple come from" — basis: `ProvenanceManager` emits PROV-O qualified associations distinguishing approved-by from generated-by from reviewed-by [D: semantica/provenance/manager.py:1290], while the SPARQL reasoner materialises inferences so a backend query can see them [D: semantica/reasoning/sparql_reasoner.py:536].

## API contracts

Three routes. Contract: `../data/api-contract_v0.7.0_F-006.md`.

## Data model

Read-only over the graph entities. See `../data/data-erd_v0.7.0_F-006.md`.

## Sequence

1. `POST /api/reason` runs the reasoner over the session graph [D: semantica/explorer/routes/enrich.py:339].
2. Rule chains are evaluated to fixpoint, at most one productive pass per rule [D: semantica/reasoning/sparql_reasoner.py:893].
3. Native SPARQL execution sends raw query text to the backend, which cannot see unmaterialised rules [D: semantica/reasoning/sparql_reasoner.py:536].
4. Rule snapshots are taken at session construction and are immutable thereafter [D: semantica/reasoning/truth_maintenance_types.py:61].
5. `GET /api/provenance` and `/report` read the emitted records [D: semantica/explorer/routes/provenance.py:330].
6. `wasDerivedFrom` is emitted only when the used entity differs from the parent already carrying that triple [D: semantica/provenance/manager.py:1360].

## Failure modes

| failure | detection | behaviour | source |
| --- | --- | --- | --- |
| Handler returning the wrong type | contract check in the execution engine | deterministic failure, retry policy never consulted | [D: semantica/pipeline/execution_engine.py:395] |
| Inference invisible to a native backend query | materialisation before native execution | answers include inferred triples | [D: semantica/reasoning/sparql_reasoner.py:536] |
| Rule mutated after session construction | immutable snapshot at construction | the running session is unaffected | [D: semantica/reasoning/truth_maintenance_types.py:61] |

## Observability

Logging only. `semantica/utils/logging.py:138` provides `get_logger`; `loguru` and `structlog` are declared dependencies [D: pyproject.toml:19]. No metrics client, tracer or span appears anywhere under `semantica/` — no `prometheus`, `opentelemetry` or `statsd` import exists in the package [D: semantica/utils/logging.py:138].

OPEN: what should this feature emit in production? No metric name, dashboard or alert is defined in the repository.

## Traceability

`DOM-006`, stories `F-006-US1`..`F-006-US3`.

## Open questions

OPEN: what was rejected on the way to this shape? The repository retains no record of alternatives, and none is guessed here.
OPEN: what are the latency, throughput and resource targets for F-006? No budget or SLO is expressed in code.

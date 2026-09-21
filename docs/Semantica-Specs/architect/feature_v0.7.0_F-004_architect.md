---
title: Feature Architecture v0.7.0 F-004 — Ontology and Vocabulary Management
id: F-004
kind: architecture
feature: F-004
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Feature Architecture v0.7.0 F-004 — Ontology and Vocabulary Management

> Reversed from code at commit `92c2578a`. The sequence below was read call by call out of the handlers and modules cited.

## Design summary

I: ontology management is an editorial workflow, not a file loader — basis: alongside load and preview, the router carries drafts, proposals, approve/reject/publish/comment transitions and version comparison, 34 routes in one 3700-line module [D: semantica/explorer/routes/ontology.py:3241]. It rules out treating an ontology as immutable input.

## API contracts

39 routes. Contract: `../data/api-contract_v0.7.0_F-004.md`.

## Data model

Owns `OntologyEntry`, `OntologyPreview`, `VocabularyScheme`. See `../data/data-erd_v0.7.0_F-004.md`.

## Sequence

1. `POST /api/ontology/preview` parses a source without loading it, returning counts and namespace [D: semantica/explorer/routes/ontology.py:1479].
2. `POST /api/ontology/load` admits it to the registry; `GET /api/ontology/registry` lists entries with `status` of published, draft or external [D: semantica/explorer/routes/ontology.py:175].
3. Editing goes through drafts: `PATCH /api/ontology/draft`, then `GET /api/ontology/draft/{draft_id}` [D: semantica/explorer/routes/ontology.py:3181].
4. A change is proposed [D: semantica/explorer/routes/ontology.py:3241], then approved, rejected, published or commented on [D: semantica/explorer/routes/ontology.py:3404].
5. SHACL shapes are generated and validated under explicit ceilings [D: semantica/explorer/routes/ontology.py:2922].
6. Entity ownership is resolved server-side by `_resolve_owning_ontology`, which the UI treats as authoritative [D: explorer/src/workspaces/OntologyWorkspace/ontologyEditorModel.ts:23].

## Failure modes

| failure | detection | behaviour | source |
| --- | --- | --- | --- |
| Turtle payload above 262144 bytes | byte-length check | `400` naming `SEMANTICA_MAX_SHACL_TURTLE_BYTES` | [D: semantica/explorer/routes/ontology.py:2976] |
| Shape graph above 1000 triples | triple count check | `400` naming `SEMANTICA_MAX_SHACL_TRIPLES` | [D: semantica/explorer/routes/ontology.py:2994] |
| Validation exceeding 15.0 seconds | timeout | request aborted | [D: semantica/explorer/routes/ontology.py:144] |
| More than 4 concurrent validations | concurrency gate | request queued or refused | [D: semantica/explorer/routes/ontology.py:147] |

## Observability

Logging only. `semantica/utils/logging.py:138` provides `get_logger`; `loguru` and `structlog` are declared dependencies [D: pyproject.toml:19]. No metrics client, tracer or span appears anywhere under `semantica/` — no `prometheus`, `opentelemetry` or `statsd` import exists in the package [D: semantica/utils/logging.py:138].

OPEN: what should this feature emit in production? No metric name, dashboard or alert is defined in the repository.

## Traceability

`DOM-004`, stories `F-004-US1`..`F-004-US4`.

## Open questions

OPEN: what was rejected on the way to this shape? The repository retains no record of alternatives, and none is guessed here.
OPEN: what are the latency, throughput and resource targets for F-004? No budget or SLO is expressed in code.

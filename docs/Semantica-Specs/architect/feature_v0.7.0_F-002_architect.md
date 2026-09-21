---
title: Feature Architecture v0.7.0 F-002 — Knowledge Graph Construction and Semantic Extraction
id: F-002
kind: architecture
feature: F-002
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Feature Architecture v0.7.0 F-002 — Knowledge Graph Construction and Semantic Extraction

> Reversed from code at commit `92c2578a`. The sequence below was read call by call out of the handlers and modules cited.

## Design summary

I: extraction is provider-pluggable and cached, and graph construction is a separate stage that tolerates synthetic endpoints — basis: `semantica/semantic_extract/providers.py` selects the backend, `cache.py` holds a locked SQLite-backed cache [D: semantica/semantic_extract/cache.py:319], and `graph_builder.py` rebuilds a promoted set only for relationships that carry a synthetic endpoint [D: semantica/kg/graph_builder.py:225].

## API contracts

Four POST routes [D: semantica/explorer/routes/enrich.py:194]. Contract: `../data/api-contract_v0.7.0_F-002.md`.

## Data model

Writes `ContextNode` and `ContextEdge`. See `../data/data-erd_v0.7.0_F-002.md`.

## Sequence

1. `POST /api/enrich/extract` imports `NamedEntityRecognizer` and `RelationExtractor` inside the handler [D: semantica/explorer/routes/enrich.py:199].
2. A missing extraction extra raises `503` naming spacy and transformers [D: semantica/explorer/routes/enrich.py:201].
3. Recognizer is constructed with `confidence_threshold=0.7`, extractor with `0.6` [D: semantica/explorer/routes/enrich.py:207].
4. Both calls are offloaded with `asyncio.to_thread` [D: semantica/explorer/routes/enrich.py:209].
5. Results are normalised from either a list or an object exposing one [D: semantica/explorer/routes/enrich.py:213].
6. Every emitted entity carries a confidence: unmeasured ones are scored heuristically before filtering [D: semantica/semantic_extract/ner_extractor.py:1411].
7. Schema validation rejects a label that is not a concept, or a predicate outside its declared domain [D: semantica/semantic_extract/schema_validator.py:12].

## Failure modes

| failure | detection | behaviour | source |
| --- | --- | --- | --- |
| Extraction extra not installed | `ImportError` at handler import | `503` with the install hint | [D: semantica/explorer/routes/enrich.py:201] |
| Corrupt cache row | deserialisation outside the lock, before `last_access` is bumped | row stays evictable | [D: semantica/semantic_extract/cache.py:380] |
| Failed transaction on a shared connection | caller holds the lock across rollback | a later request cannot commit over it | [D: semantica/semantic_extract/cache.py:319] |
| Prompt injection in source text | content serialised as JSON strings | injected text cannot escape the string | [D: semantica/semantic_extract/llm_extraction.py:354] |

## Observability

Logging only. `semantica/utils/logging.py:138` provides `get_logger`; `loguru` and `structlog` are declared dependencies [D: pyproject.toml:19]. No metrics client, tracer or span appears anywhere under `semantica/` — no `prometheus`, `opentelemetry` or `statsd` import exists in the package [D: semantica/utils/logging.py:138].

OPEN: what should this feature emit in production? No metric name, dashboard or alert is defined in the repository.

## Traceability

`DOM-002`, stories `F-002-US1`..`F-002-US3`.

## Open questions

OPEN: what was rejected on the way to this shape? The repository retains no record of alternatives, and none is guessed here.
OPEN: what are the latency, throughput and resource targets for F-002? No budget or SLO is expressed in code.

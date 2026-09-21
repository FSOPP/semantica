---
title: Domain — Knowledge Graph Construction and Semantic Extraction
id: DOM-002
kind: domain
feature: F-002
status: draft
owner: TBD
updated: 2026-09-21
---

# Domain — Knowledge Graph Construction and Semantic Extraction

> Reversed from code at commit `92c2578a`. Every rule below was promoted from a comment or a test name in the code, and cites both the statement and the code that enforces it.

## Ubiquitous language

| term | definition | aliases to avoid |
| --- | --- | --- |
| entity | A named thing recognised in text, carrying a type and a confidence [D: semantica/semantic_extract/ner_extractor.py:1411]. | node — a node is the graph form |
| relation | A typed link between two entities, extracted above a confidence threshold [D: semantica/explorer/routes/enrich.py:207]. | edge |
| synthetic endpoint | A stand-in entity minted so a multi-value result is not silently dropped [D: semantica/semantic_extract/methods.py:2306]. | placeholder |
| promoted set | Relationships carrying a synthetic endpoint, rebuilt at graph-build time [D: semantica/kg/graph_builder.py:225]. | — |

## Actors

Callers of the four `/api/enrich` routes, holding an API key [D: semantica/explorer/routes/enrich.py:194], and the pipeline running the same extractors in-process.

## Business rules

**`DOM-002-R1`** — Every emitted entity carries a confidence value.

I: Every emitted entity carries a confidence value — basis: the code states "entities without a measured confidence are scored heuristically inside extract(), before filtering" at `semantica/semantic_extract/ner_extractor.py:1411`, and it is enforced at `semantica/semantic_extract/ner_extractor.py:1411`
**`DOM-002-R2`** — An entity label must be a concept in the schema, and a predicate must satisfy its declared domain.

I: An entity label must be a concept in the schema, and a predicate must satisfy its declared domain — basis: the code states "every entity label must be a concept in the schema; every relation predicate must be in the schema and satisfy its domain" at `semantica/semantic_extract/schema_validator.py:12`, and it is enforced at `semantica/semantic_extract/schema_validator.py:12`
**`DOM-002-R3`** — A missing `.label` is not evidence that an entity has no type.

I: A missing `.label` is not evidence that an entity has no type — basis: the code states "entity objects store the type on .type; extraction entities may expose .label" at `semantica/deduplication/duplicate_detector.py:734`, and it is enforced at `semantica/deduplication/duplicate_detector.py:734`
**`DOM-002-R4`** — A cache row that cannot be deserialised does not count as recently used.

I: A cache row that cannot be deserialised does not count as recently used — basis: the code states "deserialize outside the lock but before bumping last_access, so a corrupt row does not stay recently used" at `semantica/semantic_extract/cache.py:380`, and it is enforced at `semantica/semantic_extract/cache.py:380`
**`DOM-002-R5`** — User-supplied text entering an extraction prompt is JSON-serialised first.

I: User-supplied text entering an extraction prompt is JSON-serialised first — basis: the code states "user-supplied content is serialised as JSON strings so special characters and injection attempts cannot escape" at `semantica/semantic_extract/llm_extraction.py:354`, and it is enforced at `semantica/semantic_extract/llm_extraction.py:354`
## Process flow

1. Text arrives by API or pipeline [D: semantica/explorer/routes/enrich.py:194].
2. Entities are recognised at threshold 0.7 [D: semantica/explorer/routes/enrich.py:207].
3. Relations are extracted at threshold 0.6 [D: semantica/explorer/routes/enrich.py:207].
4. Labels and predicates are schema-validated [D: semantica/semantic_extract/schema_validator.py:12].
5. Conflicts and duplicates are detected [D: semantica/deduplication/duplicate_detector.py:734].
6. The graph builder materialises nodes and edges [D: semantica/kg/graph_builder.py:225].

## Invariants

- No entity leaves extraction without a confidence [D: semantica/semantic_extract/ner_extractor.py:1411].
- A synthetic endpoint never reuses a span already claimed by a known entity [D: semantica/semantic_extract/llm_extraction.py:627].

## Implementation status

| rule | status | evidence |
| --- | --- | --- |
| `DOM-002-R1` | wip — unverified, run pytest -q | — |
| `DOM-002-R2` | wip — unverified, run pytest -q | — |
| `DOM-002-R3` | wip — unverified, run pytest -q | — |
| `DOM-002-R4` | wip — unverified, run pytest -q | — |
| `DOM-002-R5` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Open questions

OPEN: where do 0.7 and 0.6 come from? Both are literals in the route handler, unconfigurable and unexplained [D: semantica/explorer/routes/enrich.py:207].
OPEN: what accuracy is this expected to reach? No evaluation threshold or benchmark target is expressed in code.
OPEN: is a synthetic endpoint a permanent graph citizen or a repair artefact meant to be resolved later?

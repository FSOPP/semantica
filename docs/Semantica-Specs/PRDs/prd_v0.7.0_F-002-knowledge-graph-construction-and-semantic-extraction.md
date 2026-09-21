---
title: PRD v0.7.0 F-002 — Knowledge Graph Construction and Semantic Extraction
id: F-002
kind: prd
feature: F-002
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# PRD v0.7.0 F-002 — Knowledge Graph Construction and Semantic Extraction

> **Reversed, and weakly.** A requirement states intent; intent is not in a repository. Every story below was inferred from endpoints and test names, and every business question is `OPEN:`.

## Summary

I: Knowledge Graph Construction and Semantic Extraction exists to turn text into a knowledge graph with confidence and schema discipline — basis: the surface this feature exposes and the tests that assert it, as catalogued in `../data/api-contract_v0.7.0_F-002.md` and `../tests/test_v0.7.0_F-002.md`.

## User stories

**`F-002-US1`** — As an analyst, I want to turn free text into entities and relations through one call, so that I do not assemble an extraction stack myself.

I: inferred from the shipped surface — basis: `POST /api/enrich/extract` [D: semantica/explorer/routes/enrich.py:194]

**`F-002-US2`** — As a reviewer, I want to see a confidence on every extracted entity, so that I can filter on quality rather than trust everything equally.

I: inferred from the shipped surface — basis: heuristic scoring before filtering [D: semantica/semantic_extract/ner_extractor.py:1411]

**`F-002-US3`** — As a data steward, I want to have duplicates detected and merged, so that the graph does not accumulate the same entity twice.

I: inferred from the shipped surface — basis: `POST /api/enrich/dedup` and `/merge` [D: semantica/explorer/routes/enrich.py:316]

## Acceptance criteria

- **`F-002-US1`** — Given the feature is configured, when turn free text into entities and relations through one call, then the behaviour named in ``POST /api/enrich/extract`` holds. I: lifted from the shipped surface, not from a stated requirement — basis: `POST /api/enrich/extract` [D: semantica/explorer/routes/enrich.py:194]
- **`F-002-US2`** — Given the feature is configured, when see a confidence on every extracted entity, then the behaviour named in `heuristic scoring before filtering` holds. I: lifted from the shipped surface, not from a stated requirement — basis: heuristic scoring before filtering [D: semantica/semantic_extract/ner_extractor.py:1411]
- **`F-002-US3`** — Given the feature is configured, when have duplicates detected and merged, then the behaviour named in ``POST /api/enrich/dedup` and `/merge`` holds. I: lifted from the shipped surface, not from a stated requirement — basis: `POST /api/enrich/dedup` and `/merge` [D: semantica/explorer/routes/enrich.py:316]

## Implementation status

| story | status | evidence |
| --- | --- | --- |
| `F-002-US1` | wip — unverified, run pytest -q | — |
| `F-002-US2` | wip — unverified, run pytest -q | — |
| `F-002-US3` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Scope boundaries

OPEN: what is deliberately out of scope for this feature? The code draws module boundaries; it does not record a decision to exclude anything.

## Dependencies

Domain rules: `DOM-002`. Architecture: `../architect/feature_v0.7.0_F-002_architect.md`. Other features this one imports from are listed in `../architect/architect.md`.

## Metrics

OPEN: how is success measured for this feature after release? No metric, event or analytics call exists in the code.
OPEN: what is the business priority of this feature relative to the other eight? Nothing in the repository ranks them.

## Open questions

OPEN: who asked for this, and what problem were they reporting? Not recoverable from the working tree.
OPEN: which stories are load-bearing for a paying user and which are conveniences? The code treats every route identically.

---
title: Fixtures v0.7.0 F-004 — Ontology and Vocabulary Management
id: F-004
status: draft
owner: TBD
updated: 2026-09-21
---

# Fixtures v0.7.0 F-004 — Ontology and Vocabulary Management

> What `fixtures/fixtures_v0.7.0_F-004.json` contains and what each set is for.

## Fixture sets

| Entity | Records | Purpose |
| --- | --- | --- |
| `OntologyEntry` | 1 | minimal valid record, every declared field present |
| `OntologyPreview` | 1 | minimal valid record, every declared field present |
| `VocabularyScheme` | 1 | minimal valid record, every declared field present |

I: these are synthesised minimal records, not lifted from the repository's own test data — basis: the suite builds its graphs inline in each test module rather than loading a shared fixture file [D: tests/explorer/conftest.py:1].

## Validation

`route.py` validates every record against `schema/schemas.json`, rejecting an unknown entity, a missing required field or an undeclared field.

## Open questions

OPEN: which scenario should each fixture represent? The repository's tests construct their data inline, so no named scenario set exists to reverse.
OPEN: is there a production-shaped dataset anywhere that these fixtures should resemble in size? None is committed.

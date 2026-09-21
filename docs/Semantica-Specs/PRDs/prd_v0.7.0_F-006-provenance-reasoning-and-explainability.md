---
title: PRD v0.7.0 F-006 — Provenance Reasoning and Explainability
id: F-006
kind: prd
feature: F-006
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# PRD v0.7.0 F-006 — Provenance Reasoning and Explainability

> **Reversed, and weakly.** A requirement states intent; intent is not in a repository. Every story below was inferred from endpoints and test names, and every business question is `OPEN:`.

## Summary

I: Provenance Reasoning and Explainability exists to make every fact accountable and every inference explainable — basis: the surface this feature exposes and the tests that assert it, as catalogued in `../data/api-contract_v0.7.0_F-006.md` and `../tests/test_v0.7.0_F-006.md`.

## User stories

**`F-006-US1`** — As an auditor, I want to see where an inferred fact came from, so that an inference is accountable, not anonymous.

I: inferred from the shipped surface — basis: PROV-O records with roles [D: semantica/provenance/manager.py:1290]

**`F-006-US2`** — As an analyst, I want to run rules over the graph and get the inferences back, so that implicit knowledge becomes queryable.

I: inferred from the shipped surface — basis: `POST /api/reason` [D: semantica/explorer/routes/enrich.py:339]

**`F-006-US3`** — As an analyst, I want to have inferences visible to a native backend query, so that a SPARQL query does not silently miss inferred answers.

I: inferred from the shipped surface — basis: materialisation before native execution [D: semantica/reasoning/sparql_reasoner.py:536]

## Acceptance criteria

- **`F-006-US1`** — Given the feature is configured, when see where an inferred fact came from, then the behaviour named in `PROV-O records with roles` holds. I: lifted from the shipped surface, not from a stated requirement — basis: PROV-O records with roles [D: semantica/provenance/manager.py:1290]
- **`F-006-US2`** — Given the feature is configured, when run rules over the graph and get the inferences back, then the behaviour named in ``POST /api/reason`` holds. I: lifted from the shipped surface, not from a stated requirement — basis: `POST /api/reason` [D: semantica/explorer/routes/enrich.py:339]
- **`F-006-US3`** — Given the feature is configured, when have inferences visible to a native backend query, then the behaviour named in `materialisation before native execution` holds. I: lifted from the shipped surface, not from a stated requirement — basis: materialisation before native execution [D: semantica/reasoning/sparql_reasoner.py:536]

## Implementation status

| story | status | evidence |
| --- | --- | --- |
| `F-006-US1` | wip — unverified, run pytest -q | — |
| `F-006-US2` | wip — unverified, run pytest -q | — |
| `F-006-US3` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Scope boundaries

OPEN: what is deliberately out of scope for this feature? The code draws module boundaries; it does not record a decision to exclude anything.

## Dependencies

Domain rules: `DOM-006`. Architecture: `../architect/feature_v0.7.0_F-006_architect.md`. Other features this one imports from are listed in `../architect/architect.md`.

## Metrics

OPEN: how is success measured for this feature after release? No metric, event or analytics call exists in the code.
OPEN: what is the business priority of this feature relative to the other eight? Nothing in the repository ranks them.

## Open questions

OPEN: who asked for this, and what problem were they reporting? Not recoverable from the working tree.
OPEN: which stories are load-bearing for a paying user and which are conveniences? The code treats every route identically.

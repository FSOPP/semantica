---
title: PRD v0.7.0 F-004 — Ontology and Vocabulary Management
id: F-004
kind: prd
feature: F-004
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# PRD v0.7.0 F-004 — Ontology and Vocabulary Management

> **Reversed, and weakly.** A requirement states intent; intent is not in a repository. Every story below was inferred from endpoints and test names, and every business question is `OPEN:`.

## Summary

I: Ontology and Vocabulary Management exists to let humans govern the schemas the graph is validated against — basis: the surface this feature exposes and the tests that assert it, as catalogued in `../data/api-contract_v0.7.0_F-004.md` and `../tests/test_v0.7.0_F-004.md`.

## User stories

**`F-004-US1`** — As an ontology editor, I want to preview an ontology before loading it, so that I can see its size and namespace before committing.

I: inferred from the shipped surface — basis: `POST /api/ontology/preview` [D: semantica/explorer/routes/ontology.py:1479]

**`F-004-US2`** — As an ontology editor, I want to work on a draft and submit it as a proposal, so that changes are reviewed before they reach a published ontology.

I: inferred from the shipped surface — basis: draft and proposal routes [D: semantica/explorer/routes/ontology.py:3241]

**`F-004-US3`** — As an approver, I want to approve, reject or comment on a proposal, so that there is a record of who decided what.

I: inferred from the shipped surface — basis: approve, reject, publish and comment routes [D: semantica/explorer/routes/ontology.py:3404]

**`F-004-US4`** — As a data steward, I want to validate data against generated SHACL shapes within bounded cost, so that one large payload cannot exhaust the server.

I: inferred from the shipped surface — basis: four configured ceilings [D: semantica/explorer/routes/ontology.py:138]

## Acceptance criteria

- **`F-004-US1`** — Given the feature is configured, when preview an ontology before loading it, then the behaviour named in ``POST /api/ontology/preview`` holds. I: lifted from the shipped surface, not from a stated requirement — basis: `POST /api/ontology/preview` [D: semantica/explorer/routes/ontology.py:1479]
- **`F-004-US2`** — Given the feature is configured, when work on a draft and submit it as a proposal, then the behaviour named in `draft and proposal routes` holds. I: lifted from the shipped surface, not from a stated requirement — basis: draft and proposal routes [D: semantica/explorer/routes/ontology.py:3241]
- **`F-004-US3`** — Given the feature is configured, when approve, reject or comment on a proposal, then the behaviour named in `approve, reject, publish and comment routes` holds. I: lifted from the shipped surface, not from a stated requirement — basis: approve, reject, publish and comment routes [D: semantica/explorer/routes/ontology.py:3404]
- **`F-004-US4`** — Given the feature is configured, when validate data against generated SHACL shapes within bounded cost, then the behaviour named in `four configured ceilings` holds. I: lifted from the shipped surface, not from a stated requirement — basis: four configured ceilings [D: semantica/explorer/routes/ontology.py:138]

## Implementation status

| story | status | evidence |
| --- | --- | --- |
| `F-004-US1` | wip — unverified, run pytest -q | — |
| `F-004-US2` | wip — unverified, run pytest -q | — |
| `F-004-US3` | wip — unverified, run pytest -q | — |
| `F-004-US4` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Scope boundaries

OPEN: what is deliberately out of scope for this feature? The code draws module boundaries; it does not record a decision to exclude anything.

## Dependencies

Domain rules: `DOM-004`. Architecture: `../architect/feature_v0.7.0_F-004_architect.md`. Other features this one imports from are listed in `../architect/architect.md`.

## Metrics

OPEN: how is success measured for this feature after release? No metric, event or analytics call exists in the code.
OPEN: what is the business priority of this feature relative to the other eight? Nothing in the repository ranks them.

## Open questions

OPEN: who asked for this, and what problem were they reporting? Not recoverable from the working tree.
OPEN: which stories are load-bearing for a paying user and which are conveniences? The code treats every route identically.

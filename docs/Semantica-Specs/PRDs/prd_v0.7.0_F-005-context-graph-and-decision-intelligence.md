---
title: PRD v0.7.0 F-005 — Context Graph and Decision Intelligence
id: F-005
kind: prd
feature: F-005
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# PRD v0.7.0 F-005 — Context Graph and Decision Intelligence

> **Reversed, and weakly.** A requirement states intent; intent is not in a repository. Every story below was inferred from endpoints and test names, and every business question is `OPEN:`.

## Summary

I: Context Graph and Decision Intelligence exists to record decisions as first-class, auditable graph citizens — basis: the surface this feature exposes and the tests that assert it, as catalogued in `../data/api-contract_v0.7.0_F-005.md` and `../tests/test_v0.7.0_F-005.md`.

## User stories

**`F-005-US1`** — As an agent, I want to record a decision with its scenario, reasoning, outcome and confidence, so that the decision can be audited later.

I: inferred from the shipped surface — basis: decisions are typed context nodes [D: semantica/explorer/routes/decisions.py:17]

**`F-005-US2`** — As an auditor, I want to walk the causal chain behind a decision, so that I can see what led to it.

I: inferred from the shipped surface — basis: `GET /api/decisions/{id}/chain` [D: semantica/explorer/routes/decisions.py:83]

**`F-005-US3`** — As an auditor, I want to find precedents and check compliance for a decision, so that comparable cases and policy verdicts are available.

I: inferred from the shipped surface — basis: `/precedents` and `/compliance` [D: semantica/explorer/routes/decisions.py:145]

## Acceptance criteria

- **`F-005-US1`** — Given the feature is configured, when record a decision with its scenario, reasoning, outcome and confidence, then the behaviour named in `decisions are typed context nodes` holds. I: lifted from the shipped surface, not from a stated requirement — basis: decisions are typed context nodes [D: semantica/explorer/routes/decisions.py:17]
- **`F-005-US2`** — Given the feature is configured, when walk the causal chain behind a decision, then the behaviour named in ``GET /api/decisions/{id}/chain`` holds. I: lifted from the shipped surface, not from a stated requirement — basis: `GET /api/decisions/{id}/chain` [D: semantica/explorer/routes/decisions.py:83]
- **`F-005-US3`** — Given the feature is configured, when find precedents and check compliance for a decision, then the behaviour named in ``/precedents` and `/compliance`` holds. I: lifted from the shipped surface, not from a stated requirement — basis: `/precedents` and `/compliance` [D: semantica/explorer/routes/decisions.py:145]

## Implementation status

| story | status | evidence |
| --- | --- | --- |
| `F-005-US1` | wip — unverified, run pytest -q | — |
| `F-005-US2` | wip — unverified, run pytest -q | — |
| `F-005-US3` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Scope boundaries

OPEN: what is deliberately out of scope for this feature? The code draws module boundaries; it does not record a decision to exclude anything.

## Dependencies

Domain rules: `DOM-005`. Architecture: `../architect/feature_v0.7.0_F-005_architect.md`. Other features this one imports from are listed in `../architect/architect.md`.

## Metrics

OPEN: how is success measured for this feature after release? No metric, event or analytics call exists in the code.
OPEN: what is the business priority of this feature relative to the other eight? Nothing in the repository ranks them.

## Open questions

OPEN: who asked for this, and what problem were they reporting? Not recoverable from the working tree.
OPEN: which stories are load-bearing for a paying user and which are conveniences? The code treats every route identically.

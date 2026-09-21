---
title: PRD v0.7.0 F-007 — Knowledge Explorer UI and Graph API
id: F-007
kind: prd
feature: F-007
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# PRD v0.7.0 F-007 — Knowledge Explorer UI and Graph API

> **Reversed, and weakly.** A requirement states intent; intent is not in a repository. Every story below was inferred from endpoints and test names, and every business question is `OPEN:`.

## Summary

I: Knowledge Explorer UI and Graph API exists to let a person see and edit the graph — basis: the surface this feature exposes and the tests that assert it, as catalogued in `../data/api-contract_v0.7.0_F-007.md` and `../tests/test_v0.7.0_F-007.md`.

## User stories

**`F-007-US1`** — As an analyst, I want to browse a graph of any size without loading it all, so that the viewer stays responsive.

I: inferred from the shipped surface — basis: cursor pagination capped at 5000 [D: semantica/explorer/routes/graph.py:108]

**`F-007-US2`** — As an analyst, I want to scrub through time and see the graph as it was, so that change over time is visible.

I: inferred from the shipped surface — basis: temporal snapshot and diff routes [D: semantica/explorer/routes/temporal.py:64]

**`F-007-US3`** — As an analyst, I want to annotate a node, so that observations stay attached to what they describe.

I: inferred from the shipped surface — basis: annotation routes [D: semantica/explorer/routes/annotations.py:30]

**`F-007-US4`** — As an analyst, I want to edit a node's markdown and see a conflict if it moved underneath me, so that I do not overwrite someone else's edit.

I: inferred from the shipped surface — basis: stale-revision conflict [D: semantica/explorer/routes/markdown.py:97]

## Acceptance criteria

- **`F-007-US1`** — Given the feature is configured, when browse a graph of any size without loading it all, then the behaviour named in `cursor pagination capped at 5000` holds. I: lifted from the shipped surface, not from a stated requirement — basis: cursor pagination capped at 5000 [D: semantica/explorer/routes/graph.py:108]
- **`F-007-US2`** — Given the feature is configured, when scrub through time and see the graph as it was, then the behaviour named in `temporal snapshot and diff routes` holds. I: lifted from the shipped surface, not from a stated requirement — basis: temporal snapshot and diff routes [D: semantica/explorer/routes/temporal.py:64]
- **`F-007-US3`** — Given the feature is configured, when annotate a node, then the behaviour named in `annotation routes` holds. I: lifted from the shipped surface, not from a stated requirement — basis: annotation routes [D: semantica/explorer/routes/annotations.py:30]
- **`F-007-US4`** — Given the feature is configured, when edit a node's markdown and see a conflict if it moved underneath me, then the behaviour named in `stale-revision conflict` holds. I: lifted from the shipped surface, not from a stated requirement — basis: stale-revision conflict [D: semantica/explorer/routes/markdown.py:97]

## Implementation status

| story | status | evidence |
| --- | --- | --- |
| `F-007-US1` | wip — unverified, run pytest -q | — |
| `F-007-US2` | wip — unverified, run pytest -q | — |
| `F-007-US3` | wip — unverified, run pytest -q | — |
| `F-007-US4` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Scope boundaries

OPEN: what is deliberately out of scope for this feature? The code draws module boundaries; it does not record a decision to exclude anything.

## Dependencies

Domain rules: `DOM-007`. Architecture: `../architect/feature_v0.7.0_F-007_architect.md`. Other features this one imports from are listed in `../architect/architect.md`.

## Metrics

OPEN: how is success measured for this feature after release? No metric, event or analytics call exists in the code.
OPEN: what is the business priority of this feature relative to the other eight? Nothing in the repository ranks them.

## Open questions

OPEN: who asked for this, and what problem were they reporting? Not recoverable from the working tree.
OPEN: which stories are load-bearing for a paying user and which are conveniences? The code treats every route identically.

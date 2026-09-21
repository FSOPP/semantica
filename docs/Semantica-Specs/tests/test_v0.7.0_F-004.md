---
title: Test Plan v0.7.0 F-004 — Ontology and Vocabulary Management
id: F-004
kind: test
feature: F-004
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Test Plan v0.7.0 F-004 — Ontology and Vocabulary Management

> **This document is as-built.** It records the tests that exist at commit `92c2578a`, not tests that were planned. Its most useful section is Coverage holes.

## Suite size

454 test cases across 28 files in `tests/ontology`, `tests/explorer` [D: pyproject.toml:376]. The cases listed below are the ones whose names plainly correspond to a stated domain rule; the rest are not enumerated here.

## Traceability matrix

| domain rule | test cases | level |
| --- | --- | --- |
| `DOM-004-R1` | `F-004-TC1`, `F-004-TC2` | unit |
| `DOM-004-R2` | `F-004-TC3`, `F-004-TC4` | unit |
| `DOM-004-R3` | — | — |
| `DOM-004-R4` | — | — |
| `DOM-004-R5` | — | — |

I: a test case is mapped to a rule by what its name asserts, not by execution — basis: the mapping was made by reading test names against rule statements; no coverage instrumentation was run [D: pyproject.toml:376].

## Story coverage

| story | domain rules | test cases | verdict |
| --- | --- | --- | --- |
| `F-004-US1` | `DOM-004-R3`, `DOM-004-R4` | — | rules stated, no test names them |
| `F-004-US2` | `DOM-004-R1`, `DOM-004-R5` | `F-004-TC1`, `F-004-TC2` | covered |
| `F-004-US3` | `DOM-004-R5` | — | rules stated, no test names them |
| `F-004-US4` | `DOM-004-R2` | `F-004-TC3`, `F-004-TC4` | covered |

I: a story is linked to a test through the domain rule both refer to, not through an execution trace — basis: the stories were themselves inferred from the shipped surface, so this column inherits that inference and adds nothing to it.

## Test cases

| id | test | source | covers |
| --- | --- | --- | --- |
| `F-004-TC1` | `ontology_load_rejects_cyclic_skos_hierarchy` | `tests/explorer/test_ontology_subissue3.py:1038` | `DOM-004-R1` |
| `F-004-TC2` | `refresh_ontology_rejects_cyclic_skos_hierarchy` | `tests/explorer/test_ontology_subissue3.py:1172` | `DOM-004-R1` |
| `F-004-TC3` | `engine_to_shacl_returns_non_empty_string` | `tests/ontology/test_ontology_advanced.py:390` | `DOM-004-R2` |
| `F-004-TC4` | `shacl_validation_report_summary_conforms` | `tests/ontology/test_ontology_advanced.py:420` | `DOM-004-R2` |

## Coverage holes

- **`DOM-004-R3`** — No test names backend-authoritative owning-ontology resolution (`semantica/explorer/routes/ontology.py:2010`).
- **`DOM-004-R4`** — No test names single-module ownership of the deep-link parameters (`explorer/src/workspaces/OntologyWorkspace/ontologyUrlState.ts:1`).
- **`DOM-004-R5`** — No test names the proposal lifecycle — propose, approve, reject, publish — across `semantica/explorer/routes/ontology.py:3241`-`3434`. Seven routes, no named coverage.

## Implementation status

| test case | status | evidence |
| --- | --- | --- |
| `F-004-TC1` | wip — unverified, run pytest -q | — |
| `F-004-TC2` | wip — unverified, run pytest -q | — |
| `F-004-TC3` | wip — unverified, run pytest -q | — |
| `F-004-TC4` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Edge and negative cases

The suite carries a dedicated marker for tests needing external services or API keys: `-m 'not integration'` deselects them [D: pyproject.toml:376].

## Out of scope

Cases outside `tests/ontology` that touch this feature indirectly. The repository also holds roughly 1,955 test cases directly under `tests/*.py` that this hub's split does not assign to any feature directory.

## Open questions

OPEN: what line or branch coverage does this suite reach? No coverage configuration or report exists in the repository.
OPEN: which tests are expected to be green on a developer machine without cloud credentials? Only the `integration` marker distinguishes them, and it is applied by hand.

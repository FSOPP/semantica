---
title: Test Plan v0.7.0 F-008 — Export and Interchange
id: F-008
kind: test
feature: F-008
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Test Plan v0.7.0 F-008 — Export and Interchange

> **This document is as-built.** It records the tests that exist at commit `92c2578a`, not tests that were planned. Its most useful section is Coverage holes.

## Suite size

252 test cases across 19 files in `tests/export` [D: pyproject.toml:376]. The cases listed below are the ones whose names plainly correspond to a stated domain rule; the rest are not enumerated here.

## Traceability matrix

| domain rule | test cases | level |
| --- | --- | --- |
| `DOM-008-R1` | `F-008-TC1`, `F-008-TC2`, `F-008-TC3` | unit |
| `DOM-008-R2` | `F-008-TC4` | unit |

I: a test case is mapped to a rule by what its name asserts, not by execution — basis: the mapping was made by reading test names against rule statements; no coverage instrumentation was run [D: pyproject.toml:376].

## Story coverage

| story | domain rules | test cases | verdict |
| --- | --- | --- | --- |
| `F-008-US1` | `DOM-008-R2` | `F-008-TC4` | covered |
| `F-008-US2` | `DOM-008-R1` | `F-008-TC1`, `F-008-TC2`, `F-008-TC3` | covered |

I: a story is linked to a test through the domain rule both refer to, not through an execution trace — basis: the stories were themselves inferred from the shipped surface, so this column inherits that inference and adds nothing to it.

## Test cases

| id | test | source | covers |
| --- | --- | --- | --- |
| `F-008-TC1` | `no_export_hides_its_payload_in_a_named_graph` | `tests/export/test_jsonld_default_graph.py:76` | `DOM-008-R1` |
| `F-008-TC2` | `exported_knowledge_graph_survives_a_default_graph_read` | `tests/export/test_jsonld_default_graph.py:97` | `DOM-008-R1` |
| `F-008-TC3` | `document_provenance_still_reaches_the_default_graph` | `tests/export/test_jsonld_default_graph.py:128` | `DOM-008-R1` |
| `F-008-TC4` | `every_format_writes_the_same_metadata_triples` | `tests/export/test_metadata_passthrough.py:93` | `DOM-008-R2` |

## Coverage holes

None. Every rule in this feature's domain document has at least one test naming it.

## Implementation status

| test case | status | evidence |
| --- | --- | --- |
| `F-008-TC1` | wip — unverified, run pytest -q | — |
| `F-008-TC2` | wip — unverified, run pytest -q | — |
| `F-008-TC3` | wip — unverified, run pytest -q | — |
| `F-008-TC4` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Edge and negative cases

The suite carries a dedicated marker for tests needing external services or API keys: `-m 'not integration'` deselects them [D: pyproject.toml:376].

## Out of scope

Cases outside `tests/export` that touch this feature indirectly. The repository also holds roughly 1,955 test cases directly under `tests/*.py` that this hub's split does not assign to any feature directory.

## Open questions

OPEN: what line or branch coverage does this suite reach? No coverage configuration or report exists in the repository.
OPEN: which tests are expected to be green on a developer machine without cloud credentials? Only the `integration` marker distinguishes them, and it is applied by hand.

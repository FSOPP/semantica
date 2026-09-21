---
title: Test Plan v0.7.0 F-005 — Context Graph and Decision Intelligence
id: F-005
kind: test
feature: F-005
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Test Plan v0.7.0 F-005 — Context Graph and Decision Intelligence

> **This document is as-built.** It records the tests that exist at commit `92c2578a`, not tests that were planned. Its most useful section is Coverage holes.

## Suite size

1026 test cases across 51 files in `tests/context`, `tests/evals` [D: pyproject.toml:376]. The cases listed below are the ones whose names plainly correspond to a stated domain rule; the rest are not enumerated here.

## Traceability matrix

| domain rule | test cases | level |
| --- | --- | --- |
| `DOM-005-R1` | — | — |
| `DOM-005-R2` | `F-005-TC1`, `F-005-TC2` | unit |
| `DOM-005-R3` | `F-005-TC3`, `F-005-TC4` | unit |
| `DOM-005-R4` | `F-005-TC5`, `F-005-TC6` | unit |

I: a test case is mapped to a rule by what its name asserts, not by execution — basis: the mapping was made by reading test names against rule statements; no coverage instrumentation was run [D: pyproject.toml:376].

## Story coverage

| story | domain rules | test cases | verdict |
| --- | --- | --- | --- |
| `F-005-US1` | `DOM-005-R1`, `DOM-005-R3`, `DOM-005-R4` | `F-005-TC3`, `F-005-TC4`, `F-005-TC5`, `F-005-TC6` | covered |
| `F-005-US2` | `DOM-005-R3` | `F-005-TC3`, `F-005-TC4` | covered |
| `F-005-US3` | `DOM-005-R2` | `F-005-TC1`, `F-005-TC2` | covered |

I: a story is linked to a test through the domain rule both refer to, not through an execution trace — basis: the stories were themselves inferred from the shipped surface, so this column inherits that inference and adds nothing to it.

## Test cases

| id | test | source | covers |
| --- | --- | --- | --- |
| `F-005-TC1` | `dangling_relationship_removed_when_target_expires` | `tests/context/test_temporal_retriever.py:186` | `DOM-005-R2` |
| `F-005-TC2` | `skip_vector_deletion_does_not_orphan_local_vectors` | `tests/context/test_erasure_coordinator.py:968` | `DOM-005-R2` |
| `F-005-TC3` | `decision_node_serialization` | `tests/context/test_context_graph_decisions.py:647` | `DOM-005-R3` |
| `F-005-TC4` | `decision_node_deserialization` | `tests/context/test_context_graph_decisions.py:667` | `DOM-005-R3` |
| `F-005-TC5` | `invalid_confidence_values` | `tests/context/test_causal_analyzer.py:731` | `DOM-005-R4` |
| `F-005-TC6` | `extreme_confidence_values` | `tests/context/test_context_graph_decisions.py:749` | `DOM-005-R4` |

## Coverage holes

- **`DOM-005-R1`** — No test names the atomic temp-file-then-rename persistence rule at `semantica/context/context_graph.py:1409`, although it is the file's stated crash guarantee.

## Implementation status

| test case | status | evidence |
| --- | --- | --- |
| `F-005-TC1` | wip — unverified, run pytest -q | — |
| `F-005-TC2` | wip — unverified, run pytest -q | — |
| `F-005-TC3` | wip — unverified, run pytest -q | — |
| `F-005-TC4` | wip — unverified, run pytest -q | — |
| `F-005-TC5` | wip — unverified, run pytest -q | — |
| `F-005-TC6` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Edge and negative cases

The suite carries a dedicated marker for tests needing external services or API keys: `-m 'not integration'` deselects them [D: pyproject.toml:376].

## Out of scope

Cases outside `tests/context` that touch this feature indirectly. The repository also holds roughly 1,955 test cases directly under `tests/*.py` that this hub's split does not assign to any feature directory.

## Open questions

OPEN: what line or branch coverage does this suite reach? No coverage configuration or report exists in the repository.
OPEN: which tests are expected to be green on a developer machine without cloud credentials? Only the `integration` marker distinguishes them, and it is applied by hand.

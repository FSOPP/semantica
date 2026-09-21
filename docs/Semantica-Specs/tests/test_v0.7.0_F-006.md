---
title: Test Plan v0.7.0 F-006 — Provenance Reasoning and Explainability
id: F-006
kind: test
feature: F-006
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Test Plan v0.7.0 F-006 — Provenance Reasoning and Explainability

> **This document is as-built.** It records the tests that exist at commit `92c2578a`, not tests that were planned. Its most useful section is Coverage holes.

## Suite size

636 test cases across 28 files in `tests/provenance`, `tests/reasoning`, `tests/pipeline` [D: pyproject.toml:376]. The cases listed below are the ones whose names plainly correspond to a stated domain rule; the rest are not enumerated here.

## Traceability matrix

| domain rule | test cases | level |
| --- | --- | --- |
| `DOM-006-R1` | `F-006-TC1`, `F-006-TC2` | unit |
| `DOM-006-R2` | `F-006-TC3`, `F-006-TC4`, `F-006-TC5` | unit |
| `DOM-006-R3` | `F-006-TC6`, `F-006-TC7` | unit |
| `DOM-006-R4` | `F-006-TC8`, `F-006-TC9` | unit |
| `DOM-006-R5` | `F-006-TC10` | unit |

I: a test case is mapped to a rule by what its name asserts, not by execution — basis: the mapping was made by reading test names against rule statements; no coverage instrumentation was run [D: pyproject.toml:376].

## Story coverage

| story | domain rules | test cases | verdict |
| --- | --- | --- | --- |
| `F-006-US1` | `DOM-006-R4`, `DOM-006-R5` | `F-006-TC8`, `F-006-TC9`, `F-006-TC10` | covered |
| `F-006-US2` | `DOM-006-R1` | `F-006-TC1`, `F-006-TC2` | covered |
| `F-006-US3` | `DOM-006-R2`, `DOM-006-R3` | `F-006-TC3`, `F-006-TC4`, `F-006-TC5`, `F-006-TC6`, `F-006-TC7` | covered |

I: a story is linked to a test through the domain rule both refer to, not through an execution trace — basis: the stories were themselves inferred from the shipped surface, so this column inherits that inference and adds nothing to it.

## Test cases

| id | test | source | covers |
| --- | --- | --- | --- |
| `F-006-TC1` | `failure_handler_retry_policy` | `tests/pipeline/test_pipeline_comprehensive.py:38` | `DOM-006-R1` |
| `F-006-TC2` | `execution_engine_retry_integration` | `tests/pipeline/test_pipeline_comprehensive.py:199` | `DOM-006-R1` |
| `F-006-TC3` | `execute_query_fallback_materializes_is_a_rules` | `tests/reasoning/test_specialized_reasoners.py:486` | `DOM-006-R2` |
| `F-006-TC4` | `execute_query_fallback_materialization_reaches_fixpoint` | `tests/reasoning/test_specialized_reasoners.py:508` | `DOM-006-R2` |
| `F-006-TC5` | `execute_query_native_path_materializes_inference_first` | `tests/reasoning/test_specialized_reasoners.py:600` | `DOM-006-R2` |
| `F-006-TC6` | `rule_snapshot_is_isolated_from_mutation` | `tests/reasoning/test_truth_maintenance.py:199` | `DOM-006-R3` |
| `F-006-TC7` | `returned_snapshots_are_immutable` | `tests/reasoning/test_truth_maintenance.py:208` | `DOM-006-R3` |
| `F-006-TC8` | `derived_from_does_not_override_explicit_parent` | `tests/provenance/test_manager.py:257` | `DOM-006-R4` |
| `F-006-TC9` | `derived_from_takes_precedence_over_source_as_entity` | `tests/provenance/test_manager.py:272` | `DOM-006-R4` |
| `F-006-TC10` | `export_prov_includes_qualified_association_and_role` | `tests/provenance/test_manager.py:1339` | `DOM-006-R5` |

## Coverage holes

None. Every rule in this feature's domain document has at least one test naming it.

## Implementation status

| test case | status | evidence |
| --- | --- | --- |
| `F-006-TC1` | wip — unverified, run pytest -q | — |
| `F-006-TC2` | wip — unverified, run pytest -q | — |
| `F-006-TC3` | wip — unverified, run pytest -q | — |
| `F-006-TC4` | wip — unverified, run pytest -q | — |
| `F-006-TC5` | wip — unverified, run pytest -q | — |
| `F-006-TC6` | wip — unverified, run pytest -q | — |
| `F-006-TC7` | wip — unverified, run pytest -q | — |
| `F-006-TC8` | wip — unverified, run pytest -q | — |
| `F-006-TC9` | wip — unverified, run pytest -q | — |
| `F-006-TC10` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Edge and negative cases

The suite carries a dedicated marker for tests needing external services or API keys: `-m 'not integration'` deselects them [D: pyproject.toml:376].

## Out of scope

Cases outside `tests/provenance` that touch this feature indirectly. The repository also holds roughly 1,955 test cases directly under `tests/*.py` that this hub's split does not assign to any feature directory.

## Open questions

OPEN: what line or branch coverage does this suite reach? No coverage configuration or report exists in the repository.
OPEN: which tests are expected to be green on a developer machine without cloud credentials? Only the `integration` marker distinguishes them, and it is applied by hand.

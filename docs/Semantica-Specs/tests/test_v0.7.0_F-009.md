---
title: Test Plan v0.7.0 F-009 — CLI MCP Server and Agent Integrations
id: F-009
kind: test
feature: F-009
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Test Plan v0.7.0 F-009 — CLI MCP Server and Agent Integrations

> **This document is as-built.** It records the tests that exist at commit `92c2578a`, not tests that were planned. Its most useful section is Coverage holes.

## Suite size

484 test cases across 28 files in `tests/cli`, `tests/integrations`, `tests/core`, `tests/utils` [D: pyproject.toml:376]. The cases listed below are the ones whose names plainly correspond to a stated domain rule; the rest are not enumerated here.

## Traceability matrix

| domain rule | test cases | level |
| --- | --- | --- |
| `DOM-009-R1` | — | — |
| `DOM-009-R2` | — | — |
| `DOM-009-R3` | `F-009-TC1` | unit |
| `DOM-009-R4` | `F-009-TC2` | unit |
| `DOM-009-R5` | `F-009-TC3` | unit |
| `DOM-009-R6` | `F-009-TC4`, `F-009-TC5` | unit |

I: a test case is mapped to a rule by what its name asserts, not by execution — basis: the mapping was made by reading test names against rule statements; no coverage instrumentation was run [D: pyproject.toml:376].

## Story coverage

| story | domain rules | test cases | verdict |
| --- | --- | --- | --- |
| `F-009-US1` | `DOM-009-R2` | — | rules stated, no test names them |
| `F-009-US2` | `DOM-009-R1` | — | rules stated, no test names them |
| `F-009-US3` | `DOM-009-R3` | `F-009-TC1` | covered |
| `F-009-US4` | `DOM-009-R4`, `DOM-009-R5`, `DOM-009-R6` | `F-009-TC1`, `F-009-TC2`, `F-009-TC3`, `F-009-TC3`, `F-009-TC4`, `F-009-TC5` | covered |

I: a story is linked to a test through the domain rule both refer to, not through an execution trace — basis: the stories were themselves inferred from the shipped surface, so this column inherits that inference and adds nothing to it.

## Test cases

| id | test | source | covers |
| --- | --- | --- | --- |
| `F-009-TC1` | `handles_exception_gracefully` | `tests/integrations/agno/test_decision_kit.py:197` | `DOM-009-R3` |
| `F-009-TC2` | `no_duplicate_tools` | `tests/integrations/agno/test_decision_kit.py:98` | `DOM-009-R4` |
| `F-009-TC3` | `append_event_does_not_persist_partial_events` | `tests/integrations/google_adk/test_session_service.py:246` | `DOM-009-R5` |
| `F-009-TC4` | `unrecognized_key_display_is_bounded` | `tests/utils/test_normalize_graph_payload.py:486` | `DOM-009-R6` |
| `F-009-TC5` | `dropped_record_key_display_is_bounded` | `tests/utils/test_normalize_graph_payload.py:497` | `DOM-009-R6` |

## Coverage holes

- **`DOM-009-R1`** — No test names the one-record-per-line JSON Lines rule at `semantica/cli.py:2338`.
- **`DOM-009-R2`** — No test names the `premises`-not-a-list error at `semantica/cli.py:1268`.

## Implementation status

| test case | status | evidence |
| --- | --- | --- |
| `F-009-TC1` | wip — unverified, run pytest -q | — |
| `F-009-TC2` | wip — unverified, run pytest -q | — |
| `F-009-TC3` | wip — unverified, run pytest -q | — |
| `F-009-TC4` | wip — unverified, run pytest -q | — |
| `F-009-TC5` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Edge and negative cases

The suite carries a dedicated marker for tests needing external services or API keys: `-m 'not integration'` deselects them [D: pyproject.toml:376].

## Out of scope

Cases outside `tests/cli` that touch this feature indirectly. The repository also holds roughly 1,955 test cases directly under `tests/*.py` that this hub's split does not assign to any feature directory.

## Open questions

OPEN: what line or branch coverage does this suite reach? No coverage configuration or report exists in the repository.
OPEN: which tests are expected to be green on a developer machine without cloud credentials? Only the `integration` marker distinguishes them, and it is applied by hand.

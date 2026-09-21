---
title: Test Plan v0.7.0 F-002 — Knowledge Graph Construction and Semantic Extraction
id: F-002
kind: test
feature: F-002
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Test Plan v0.7.0 F-002 — Knowledge Graph Construction and Semantic Extraction

> **This document is as-built.** It records the tests that exist at commit `92c2578a`, not tests that were planned. Its most useful section is Coverage holes.

## Suite size

1134 test cases across 57 files in `tests/semantic_extract`, `tests/kg`, `tests/conflicts`, `tests/deduplication`, `tests/embeddings` [D: pyproject.toml:376]. The cases listed below are the ones whose names plainly correspond to a stated domain rule; the rest are not enumerated here.

## Traceability matrix

| domain rule | test cases | level |
| --- | --- | --- |
| `DOM-002-R1` | `F-002-TC1` | unit |
| `DOM-002-R2` | — | — |
| `DOM-002-R3` | — | — |
| `DOM-002-R4` | — | — |
| `DOM-002-R5` | — | — |

I: a test case is mapped to a rule by what its name asserts, not by execution — basis: the mapping was made by reading test names against rule statements; no coverage instrumentation was run [D: pyproject.toml:376].

## Story coverage

| story | domain rules | test cases | verdict |
| --- | --- | --- | --- |
| `F-002-US1` | `DOM-002-R2`, `DOM-002-R5` | `F-002-TC1` | covered |
| `F-002-US2` | `DOM-002-R1` | `F-002-TC1` | covered |
| `F-002-US3` | `DOM-002-R3`, `DOM-002-R4` | — | rules stated, no test names them |

I: a story is linked to a test through the domain rule both refer to, not through an execution trace — basis: the stories were themselves inferred from the shipped surface, so this column inherits that inference and adds nothing to it.

## Test cases

| id | test | source | covers |
| --- | --- | --- | --- |
| `F-002-TC1` | `meets_confidence_threshold` | `tests/semantic_extract/test_entity_confidence.py:42` | `DOM-002-R1` |

## Coverage holes

- **`DOM-002-R2`** — No test names schema validation of labels and predicates, although `semantica/semantic_extract/schema_validator.py:12` states the rule.
- **`DOM-002-R3`** — No test names the `.label` / `.type` fallback rule at `semantica/deduplication/duplicate_detector.py:734`.
- **`DOM-002-R4`** — No test names the corrupt-cache-row eviction rule at `semantica/semantic_extract/cache.py:380`.
- **`DOM-002-R5`** — No test names JSON serialisation of user content before it enters a prompt (`semantica/semantic_extract/llm_extraction.py:354`).

## Implementation status

| test case | status | evidence |
| --- | --- | --- |
| `F-002-TC1` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Edge and negative cases

The suite carries a dedicated marker for tests needing external services or API keys: `-m 'not integration'` deselects them [D: pyproject.toml:376].

## Out of scope

Cases outside `tests/semantic_extract` that touch this feature indirectly. The repository also holds roughly 1,955 test cases directly under `tests/*.py` that this hub's split does not assign to any feature directory.

## Open questions

OPEN: what line or branch coverage does this suite reach? No coverage configuration or report exists in the repository.
OPEN: which tests are expected to be green on a developer machine without cloud credentials? Only the `integration` marker distinguishes them, and it is applied by hand.

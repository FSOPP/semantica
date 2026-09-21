---
title: Test Plan v0.7.0 F-003 — Storage Backends
id: F-003
kind: test
feature: F-003
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Test Plan v0.7.0 F-003 — Storage Backends

> **This document is as-built.** It records the tests that exist at commit `92c2578a`, not tests that were planned. Its most useful section is Coverage holes.

## Suite size

962 test cases across 42 files in `tests/graph_store`, `tests/vector_store`, `tests/triplet_store` [D: pyproject.toml:376]. The cases listed below are the ones whose names plainly correspond to a stated domain rule; the rest are not enumerated here.

## Traceability matrix

| domain rule | test cases | level |
| --- | --- | --- |
| `DOM-003-R1` | `F-003-TC1`, `F-003-TC2` | unit |
| `DOM-003-R2` | `F-003-TC3`, `F-003-TC4`, `F-003-TC5` | unit |
| `DOM-003-R3` | `F-003-TC6`, `F-003-TC7` | unit |
| `DOM-003-R4` | `F-003-TC8`, `F-003-TC9` | unit |
| `DOM-003-R5` | — | — |

I: a test case is mapped to a rule by what its name asserts, not by execution — basis: the mapping was made by reading test names against rule statements; no coverage instrumentation was run [D: pyproject.toml:376].

## Story coverage

| story | domain rules | test cases | verdict |
| --- | --- | --- | --- |
| `F-003-US1` | `DOM-003-R1` | `F-003-TC1`, `F-003-TC2` | covered |
| `F-003-US2` | `DOM-003-R2`, `DOM-003-R3` | `F-003-TC3`, `F-003-TC4`, `F-003-TC5`, `F-003-TC6`, `F-003-TC7` | covered |
| `F-003-US3` | `DOM-003-R4`, `DOM-003-R5` | `F-003-TC8`, `F-003-TC9` | covered |

I: a story is linked to a test through the domain rule both refer to, not through an execution trace — basis: the stories were themselves inferred from the shipped surface, so this column inherits that inference and adds nothing to it.

## Test cases

| id | test | source | covers |
| --- | --- | --- | --- |
| `F-003-TC1` | `counter_skips_explicit_vec_n_ids` | `tests/vector_store/test_inmemory_id_reuse.py:139` | `DOM-003-R1` |
| `F-003-TC2` | `collision_detection_no_silent_overwrite_even_with_corrupted_count` | `tests/vector_store/test_inmemory_id_reuse.py:190` | `DOM-003-R1` |
| `F-003-TC3` | `concurrent_store_vectors_produce_unique_ids` | `tests/vector_store/test_inmemory_id_reuse.py:487` | `DOM-003-R2` |
| `F-003-TC4` | `concurrent_delete_and_store_no_phantom_ids` | `tests/vector_store/test_inmemory_id_reuse.py:524` | `DOM-003-R2` |
| `F-003-TC5` | `concurrent_search_and_delete_no_runtime_error` | `tests/vector_store/test_inmemory_id_reuse.py:559` | `DOM-003-R2` |
| `F-003-TC6` | `save_load_unchanged` | `tests/vector_store/test_backward_compatibility.py:160` | `DOM-003-R3` |
| `F-003-TC7` | `save_load_after_deletion_preserves_state` | `tests/vector_store/test_faiss_delete_vectors.py:160` | `DOM-003-R3` |
| `F-003-TC8` | `get_vector_returns_none_after_deletion` | `tests/vector_store/test_faiss_delete_vectors.py:135` | `DOM-003-R4` |
| `F-003-TC9` | `save_load_after_deletion` | `tests/vector_store/test_faiss_delete_vectors.py:297` | `DOM-003-R4` |

## Coverage holes

- **`DOM-003-R5`** — No test asserts that signed AWS auth material stays out of the logs (`semantica/graph_store/amazon_neptune.py:298`).

## Implementation status

| test case | status | evidence |
| --- | --- | --- |
| `F-003-TC1` | wip — unverified, run pytest -q | — |
| `F-003-TC2` | wip — unverified, run pytest -q | — |
| `F-003-TC3` | wip — unverified, run pytest -q | — |
| `F-003-TC4` | wip — unverified, run pytest -q | — |
| `F-003-TC5` | wip — unverified, run pytest -q | — |
| `F-003-TC6` | wip — unverified, run pytest -q | — |
| `F-003-TC7` | wip — unverified, run pytest -q | — |
| `F-003-TC8` | wip — unverified, run pytest -q | — |
| `F-003-TC9` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Edge and negative cases

The suite carries a dedicated marker for tests needing external services or API keys: `-m 'not integration'` deselects them [D: pyproject.toml:376].

## Out of scope

Cases outside `tests/graph_store` that touch this feature indirectly. The repository also holds roughly 1,955 test cases directly under `tests/*.py` that this hub's split does not assign to any feature directory.

## Open questions

OPEN: what line or branch coverage does this suite reach? No coverage configuration or report exists in the repository.
OPEN: which tests are expected to be green on a developer machine without cloud credentials? Only the `integration` marker distinguishes them, and it is applied by hand.

---
title: Test Plan v0.7.0 F-001 — Ingest and Parse Pipeline
id: F-001
kind: test
feature: F-001
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Test Plan v0.7.0 F-001 — Ingest and Parse Pipeline

> **This document is as-built.** It records the tests that exist at commit `92c2578a`, not tests that were planned. Its most useful section is Coverage holes.

## Suite size

660 test cases across 40 files in `tests/ingest`, `tests/parse`, `tests/normalize`, `tests/split` [D: pyproject.toml:376]. The cases listed below are the ones whose names plainly correspond to a stated domain rule; the rest are not enumerated here.

## Traceability matrix

| domain rule | test cases | level |
| --- | --- | --- |
| `DOM-001-R1` | `F-001-TC1`, `F-001-TC2`, `F-001-TC3` | unit |
| `DOM-001-R2` | `F-001-TC4`, `F-001-TC5`, `F-001-TC6` | unit |
| `DOM-001-R3` | `F-001-TC7` | unit |
| `DOM-001-R4` | — | — |
| `DOM-001-R5` | — | — |

I: a test case is mapped to a rule by what its name asserts, not by execution — basis: the mapping was made by reading test names against rule statements; no coverage instrumentation was run [D: pyproject.toml:376].

## Story coverage

| story | domain rules | test cases | verdict |
| --- | --- | --- | --- |
| `F-001-US1` | `DOM-001-R4`, `DOM-001-R5` | `F-001-TC7` | covered |
| `F-001-US2` | `DOM-001-R1`, `DOM-001-R2`, `DOM-001-R3` | `F-001-TC1`, `F-001-TC2`, `F-001-TC3`, `F-001-TC4`, `F-001-TC5`, `F-001-TC6`, `F-001-TC7` | covered |
| `F-001-US3` | — | — | no rule and no test names this story |

I: a story is linked to a test through the domain rule both refer to, not through an execution trace — basis: the stories were themselves inferred from the shipped surface, so this column inherits that inference and adds nothing to it.

## Test cases

| id | test | source | covers |
| --- | --- | --- | --- |
| `F-001-TC1` | `allow_private_ips_string_false_keeps_ssrf_on` | `tests/ingest/test_ssrf_protection.py:385` | `DOM-001-R1` |
| `F-001-TC2` | `cross_host_redirect_to_private_ip_is_blocked_when_pinned` | `tests/ingest/test_auth_header_redirect_security.py:698` | `DOM-001-R1` |
| `F-001-TC3` | `detect_public_api_propagates_ssrf_validation_error` | `tests/ingest/test_public_api_ingestor.py:214` | `DOM-001-R1` |
| `F-001-TC4` | `session_authorization_stripped_on_cross_origin_redirect` | `tests/ingest/test_auth_header_redirect_security.py:67` | `DOM-001-R2` |
| `F-001-TC5` | `session_authorization_preserved_on_same_origin_redirect` | `tests/ingest/test_auth_header_redirect_security.py:132` | `DOM-001-R2` |
| `F-001-TC6` | `proxy_authorization_stripped_on_cross_origin_redirect` | `tests/ingest/test_auth_header_redirect_security.py:193` | `DOM-001-R2` |
| `F-001-TC7` | `secret_not_exposed_as_public_attribute` | `tests/ingest/test_powerbi_ingestor.py:102` | `DOM-001-R3` |

## Coverage holes

- **`DOM-001-R4`** — No test names connector-owned key precedence. The rule is stated in a comment at `semantica/ingest/powerbi_ingestor.py:780` and enforced there; nothing asserts it.
- **`DOM-001-R5`** — No test names early token refresh. `test_token_is_cached` (`tests/ingest/test_powerbi_ingestor.py:123`) covers caching, not the one-minute margin.

## Implementation status

| test case | status | evidence |
| --- | --- | --- |
| `F-001-TC1` | wip — unverified, run pytest -q | — |
| `F-001-TC2` | wip — unverified, run pytest -q | — |
| `F-001-TC3` | wip — unverified, run pytest -q | — |
| `F-001-TC4` | wip — unverified, run pytest -q | — |
| `F-001-TC5` | wip — unverified, run pytest -q | — |
| `F-001-TC6` | wip — unverified, run pytest -q | — |
| `F-001-TC7` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Edge and negative cases

The suite carries a dedicated marker for tests needing external services or API keys: `-m 'not integration'` deselects them [D: pyproject.toml:376].

## Out of scope

Cases outside `tests/ingest` that touch this feature indirectly. The repository also holds roughly 1,955 test cases directly under `tests/*.py` that this hub's split does not assign to any feature directory.

## Open questions

OPEN: what line or branch coverage does this suite reach? No coverage configuration or report exists in the repository.
OPEN: which tests are expected to be green on a developer machine without cloud credentials? Only the `integration` marker distinguishes them, and it is applied by hand.

---
title: Test Plan v0.7.0 F-007 — Knowledge Explorer UI and Graph API
id: F-007
kind: test
feature: F-007
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Test Plan v0.7.0 F-007 — Knowledge Explorer UI and Graph API

> **This document is as-built.** It records the tests that exist at commit `92c2578a`, not tests that were planned. Its most useful section is Coverage holes.

## Suite size

559 test cases across 43 files in `tests/explorer`, `explorer/tests`, `tests/visualization` [D: pyproject.toml:376]. The cases listed below are the ones whose names plainly correspond to a stated domain rule; the rest are not enumerated here.

## Traceability matrix

| domain rule | test cases | level |
| --- | --- | --- |
| `DOM-007-R1` | — | — |
| `DOM-007-R2` | `F-007-TC1`, `F-007-TC2` | unit |
| `DOM-007-R3` | `F-007-TC3`, `F-007-TC4` | unit |
| `DOM-007-R4` | `F-007-TC5`, `F-007-TC6` | unit |
| `DOM-007-R5` | `F-007-TC7` | unit |
| `DOM-007-R6` | `F-007-TC8`, `F-007-TC9` | unit |

I: a test case is mapped to a rule by what its name asserts, not by execution — basis: the mapping was made by reading test names against rule statements; no coverage instrumentation was run [D: pyproject.toml:376].

## Story coverage

| story | domain rules | test cases | verdict |
| --- | --- | --- | --- |
| `F-007-US1` | `DOM-007-R5` | `F-007-TC7` | covered |
| `F-007-US2` | `DOM-007-R1`, `DOM-007-R2`, `DOM-007-R3` | `F-007-TC1`, `F-007-TC2`, `F-007-TC3`, `F-007-TC4` | covered |
| `F-007-US3` | `DOM-007-R6` | `F-007-TC7`, `F-007-TC8`, `F-007-TC9` | covered |
| `F-007-US4` | `DOM-007-R4`, `DOM-007-R6` | `F-007-TC5`, `F-007-TC6`, `F-007-TC7`, `F-007-TC8`, `F-007-TC9` | covered |

I: a story is linked to a test through the domain rule both refer to, not through an execution trace — basis: the stories were themselves inferred from the shipped surface, so this column inherits that inference and adds nothing to it.

## Test cases

| id | test | source | covers |
| --- | --- | --- | --- |
| `F-007-TC1` | `stale_revision_returns_conflict` | `tests/explorer/test_markdown_api.py:129` | `DOM-007-R2` |
| `F-007-TC2` | `registry_rejects_stale_revision_and_preserves_content` | `tests/explorer/test_markdown_resources.py:65` | `DOM-007-R2` |
| `F-007-TC3` | `successful retry after 422 uses the original revision` | `explorer/tests/markdownEditorInteraction.test.tsx:540` | `DOM-007-R3` |
| `F-007-TC4` | `cancel discards the edit session without saving` | `explorer/tests/markdownEditorState.test.ts:50` | `DOM-007-R3` |
| `F-007-TC5` | `fragment links render in the current document without target=_blank` | `explorer/tests/markdownContentViewer.test.ts:127` | `DOM-007-R4` |
| `F-007-TC6` | `every writer preserves the URL fragment` | `explorer/tests/ontologyUrlState.test.ts:82` | `DOM-007-R4` |
| `F-007-TC7` | `resolveDisplayGraph single-edge normalizes empty-string edge type` | `explorer/tests/graphSceneState.display.test.ts:1243` | `DOM-007-R5` |
| `F-007-TC8` | `validation failures keep the draft visible for correction` | `explorer/tests/markdownEditorInteraction.test.tsx:127` | `DOM-007-R6` |
| `F-007-TC9` | `MemoryWorkspace protects a dirty memory draft` | `explorer/tests/markdownEditorInteraction.test.tsx:235` | `DOM-007-R6` |

## Coverage holes

- **`DOM-007-R1`** — No test names the snapshot in-flight guard or poll deduplication described at `explorer/src/workspaces/GraphWorkspace/GraphWorkspace.tsx:1465`. `explorer/tests/temporalScrubberBounds.test.ts` and `temporalLifecycle.test.ts` cover bounds and gating, not the request lifecycle.

## Implementation status

| test case | status | evidence |
| --- | --- | --- |
| `F-007-TC1` | wip — unverified, run npm run test:graph-workspace in explorer/ | — |
| `F-007-TC2` | wip — unverified, run npm run test:graph-workspace in explorer/ | — |
| `F-007-TC3` | wip — unverified, run npm run test:graph-workspace in explorer/ | — |
| `F-007-TC4` | wip — unverified, run npm run test:graph-workspace in explorer/ | — |
| `F-007-TC5` | wip — unverified, run npm run test:graph-workspace in explorer/ | — |
| `F-007-TC6` | wip — unverified, run npm run test:graph-workspace in explorer/ | — |
| `F-007-TC7` | wip — unverified, run npm run test:graph-workspace in explorer/ | — |
| `F-007-TC8` | wip — unverified, run npm run test:graph-workspace in explorer/ | — |
| `F-007-TC9` | wip — unverified, run npm run test:graph-workspace in explorer/ | — |

States and transitions: `../status-model.md`.

## Edge and negative cases

The suite carries a dedicated marker for tests needing external services or API keys: `-m 'not integration'` deselects them [D: pyproject.toml:376].

## Out of scope

Cases outside `tests/explorer` that touch this feature indirectly. The repository also holds roughly 1,955 test cases directly under `tests/*.py` that this hub's split does not assign to any feature directory.

## Open questions

OPEN: what line or branch coverage does this suite reach? No coverage configuration or report exists in the repository.
OPEN: which tests are expected to be green on a developer machine without cloud credentials? Only the `integration` marker distinguishes them, and it is applied by hand.

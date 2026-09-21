---
title: Testing Strategy — Semantica
status: draft
owner: TBD
updated: 2026-09-21
---

# Testing Strategy — Semantica

> Reversed from the suite and the CI workflows at commit `92c2578a`.

## Test levels

| level | scope | tool | when it runs |
| --- | --- | --- | --- |
| Python unit and integration | 428 files, 8122 cases under `tests/` | pytest, `testpaths = ["tests"]` | `pytest -q` [D: pyproject.toml:376] |
| Frontend unit | 20 files under `explorer/tests` | `node --import tsx --test` | `npm run test:graph-workspace` [D: explorer/package.json:1] |
| Frontend end-to-end | 2 `.e2e.ts` files | Playwright Chromium | `npm run test:deterministic-e2e` [D: .github/workflows/ci.yml:88] |
| Packaging | core-only importability, frontend bundled | shell steps in CI | every CI run [D: .github/workflows/ci.yml:116] |
| Agent integration | `tests/integrations/google_adk/` | pytest | every CI run [D: .github/workflows/ci.yml:181] |

## Coverage policy

There is none to reverse. No coverage tool, threshold or report configuration exists in the repository [D: pyproject.toml:376].

OPEN: what coverage is expected before a merge? Nothing states a threshold, and no report is produced.

## Test data

Tests construct their graphs inline per module rather than loading shared fixtures [D: tests/explorer/conftest.py:1]. The hub's own fixtures are synthesised minimal records under `../data/fixtures/`, documented per feature.

One marker separates tests needing external services or API keys: `integration`, deselected with `-m 'not integration'` [D: pyproject.toml:376].

## Pipeline gates

`ci.yml` runs a path-filter job first, then frontend install, test and build, core-only install verification, the deterministic Explorer backend path, a pinned-dependency check against `requirements-ci.txt`, a hash-pinned build, a packaging assertion, and the ADK integration tests [D: .github/workflows/ci.yml:23].

OPEN: which of those steps block a merge and which only report? The workflow file runs them; branch protection is not in the repository.

## Non-functional testing

A `benchmark.yml` workflow exists [D: .github/workflows/ci.yml:1], alongside `codeql`, `container-scan`, `defender-for-devops`, `security-scan` and `scorecard`.

OPEN: what performance threshold does the benchmark workflow enforce, if any? No budget is expressed in the repository.
OPEN: is there any accessibility test? None was found in `explorer/tests`.

## Open questions

OPEN: roughly 1,955 test cases live directly under `tests/*.py` rather than a package directory. Which feature owns them?

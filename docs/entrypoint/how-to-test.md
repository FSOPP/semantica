---
title: How to Test — Semantica
status: draft
owner: TBD
updated: 2026-09-21
---

# How to Test — Semantica

## Running tests

```bash
pytest -q                      # 428 files, 8122 cases
pytest -q -m 'not integration' # skip tests needing external services or API keys
```
[D: pyproject.toml:376]

Frontend, from `explorer/`:

```bash
npm run test:graph-workspace
npm run test:deterministic-e2e   # Playwright Chromium
```
[D: explorer/package.json:1]

**None of these was run during this reversal.** Every status row in the hub reads `wip — unverified` for that reason.

## Adding a test

Python tests go under `tests/`, mirroring the package they cover, named `test_*.py` [D: pyproject.toml:376]. Mark anything needing a live service `integration`. Frontend tests go in `explorer/tests` and must be added to the matching `test:*` script by hand — the scripts list files explicitly [D: explorer/package.json:1].

## Interpreting failures

A failure on an optional-extra path is usually a missing extra rather than a defect: extraction raises `503` naming spacy and transformers when its extra is absent [D: semantica/explorer/routes/enrich.py:201].

## Pointer

`../Semantica-Specs/tests/testing_strategy.md`.

## Open questions

OPEN: what is the expected runtime of a full `pytest -q` on this repository? Nothing states it, and it was not measured here.

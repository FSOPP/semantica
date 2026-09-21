---
title: How to Develop — Semantica
status: draft
owner: TBD
updated: 2026-09-21
---

# How to Develop — Semantica

> Reversed from the repository's own tooling at commit `92c2578a`.

## Before you start

Read the feature's route file under `../Semantica-Specs/route/`, then its architecture and domain documents. Note that this hub is **as-built**: its tasks describe work that already shipped, so a new change means a new task row, not a status flip on an old one.

## Loop

1. Pick the feature (`F-001`..`F-009`) whose modules you are touching — the mapping is in `../Semantica-Specs/architect/architect.md`.
2. Read that feature's architecture, domain and API contract documents.
3. `get_risk` before editing a bug magnet: `semantica/cli.py`, `semantica/explorer/routes/ontology.py`, `semantica/context/context_graph.py` and `semantica/export/rdf_exporter.py` carry the heaviest fix histories.
4. Implement. Run `pytest -q` [D: pyproject.toml:376]; for frontend work, `npm run lint` and `npm run test:graph-workspace` in `explorer/` [D: explorer/package.json:1].
5. Update the feature's task and test documents, and move status rows through `docs_flow.py task`.

## Standards

`../Semantica-Specs/architect/architect_common.md`. Do not restate its rules here.

## Definition of done

- [ ] `pytest -q` passes locally [D: pyproject.toml:376].
- [ ] `black` and `isort` clean — line length 88, isort `profile = "black"` [D: pyproject.toml:370].
- [ ] A core-only install still imports, if you touched core code [D: .github/workflows/ci.yml:116].
- [ ] Any new stated rule in a comment has a test that names it.

## Open questions

OPEN: is `mypy .` actually enforced? It is named as the typecheck command and no mypy configuration is committed.

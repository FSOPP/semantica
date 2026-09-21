---
title: Project Charter — Semantica
status: draft
owner: TBD
updated: 2026-09-21
---

# Project Charter — Semantica

> **Reversed, and almost entirely questions.** A charter states intent. This one lists what the code lets us say, and then asks for the rest. The questions are the deliverable.

## Vision statement

The repository's own words: "Graph-Native Infrastructure for Context and Accountable AI Systems" [D: pyproject.toml:1], and "The Context and Semantic Layer for AI in High-Stakes Domains — Context Graphs · Decision Intelligence · Full Provenance" [D: docs/docs.json:1]. MIT licensed, open source [D: docs/docs.json:1].

OPEN: for whom, specifically, and what changes for them?

## Business value

OPEN: not recoverable. No value driver, pricing model, funding source or commercial goal appears in the tree. `GROWTH.md` exists [D: GROWTH.md:1] and describes growth of the project, not value to a buyer.

## Target users

Four consumer shapes are visible from the entry points; which is primary is not [D: Dockerfile:1]. See `../../../Semantica-Specs/PRDs/prd.md`.

OPEN: which of operator, analyst, agent or application developer is this built for first?

## In scope / Out of scope

In scope, as shipped: nine feature areas, 88 HTTP routes, 91 CLI commands, 45 storage backends, 34 ingestors, 22 parsers, 19 exporters [D: pyproject.toml:7].

OPEN: what is deliberately out of scope? The code draws boundaries; it records no decision to exclude anything.

## Success metrics

OPEN: none exist. No analytics call, metric emission or success threshold appears anywhere in the code.

## Constraints and assumptions

Derivable constraints: Python `>=3.9.2` [D: pyproject.toml:19]; a core install must stay importable without extras, asserted in CI [D: .github/workflows/ci.yml:116]; the container pins Python 3.13 after 3.14 broke the build [D: Dockerfile:24].

OPEN: what budget, deadline or compliance regime constrains this work?

## Top risks

| risk | evidence | impact | mitigation |
| --- | --- | --- | --- |
| Bus factor | 698 of 976 git-attributed files have a single author; one contributor owns 54.6% | knowledge loss | OPEN: none recorded |
| Hotspot concentration | 73 hotspots; `semantica/cli.py` carries 35 bug fixes, `semantica/explorer/routes/ontology.py` 24 | defect rate | OPEN: none recorded |
| No coverage measurement | no coverage tool configured [D: pyproject.toml:376] | unknown regression exposure | OPEN: none recorded |
| No metrics or tracing | no instrumentation library imported | blind in production | OPEN: none recorded |

I: these four are ranked by what the tree and its history show, not by anyone's judgement of severity — basis: git-derived signals rank what to look at and do not establish impact; published precision for history-derived prediction is around 29%.

## Open questions

OPEN: everything above marked `OPEN:`. Together they are the list of things this organisation knows and has never written down.

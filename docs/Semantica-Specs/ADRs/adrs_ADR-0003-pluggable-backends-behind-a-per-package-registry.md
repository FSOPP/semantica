---
title: ADR-0003 — Pluggable backends behind a per-package registry
id: ADR-0003
kind: adr
status: accepted
owner: TBD
updated: 2026-09-21
---

# ADR-0003 — Pluggable backends behind a per-package registry

## Status

Accepted (reconstructed from code, 2026-09-21) — rationale not recovered.

## Context

- Six packages each carry `registry.py`, `config.py`, `methods.py` and a `*_provenance.py` [D: semantica/ingest/registry.py:1].
- Backends are named modules beside the registry: 34 ingestors, 22 parsers, 19 exporters, 11 graph stores, 19 vector stores, 15 triplet stores [D: semantica/vector_store/registry.py:1].
- Most backends arrive through optional extras rather than core dependencies [D: pyproject.toml:19].

## Decision

A backend is selected by name through its package's registry; callers do not import a vendor module directly [D: semantica/export/registry.py:1].

## Alternatives considered

OPEN: not recoverable — the repository retains no record of what was rejected. No alternative is invented here.

## Consequences

- A new backend is an added module plus a registry entry.
- A core-only install remains importable, which CI asserts on every run [D: .github/workflows/ci.yml:116].
- Six registries must each stay consistent; nothing enforces a shared interface across them.

## Links

`../architect/architect.md`, `../architect/architect_common.md`.

## Open questions

OPEN: what problem prompted this shape, and when? The code shows the outcome and nothing of the deliberation.

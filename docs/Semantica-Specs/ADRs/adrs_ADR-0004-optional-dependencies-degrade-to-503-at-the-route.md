---
title: ADR-0004 — Optional dependencies degrade to 503 at the route
id: ADR-0004
kind: adr
status: accepted
owner: TBD
updated: 2026-09-21
---

# ADR-0004 — Optional dependencies degrade to 503 at the route

## Status

Accepted (reconstructed from code, 2026-09-21) — rationale not recovered.

## Context

- `POST /api/enrich/extract` imports its extractors inside the handler body [D: semantica/explorer/routes/enrich.py:199].
- An `ImportError` is converted to `503` with the missing packages named in `detail` [D: semantica/explorer/routes/enrich.py:201].
- The core package declares 26 dependencies; extraction, storage and Explorer tiers are extras [D: pyproject.toml:19].

## Decision

A missing extra becomes a runtime `503` on the affected route, not an import-time failure of the application [D: semantica/explorer/routes/enrich.py:201].

## Alternatives considered

OPEN: not recoverable — the repository retains no record of what was rejected. No alternative is invented here.

## Consequences

- The server starts and serves every other route with an extra absent.
- A capability gap surfaces as a runtime error to a caller rather than a startup check an operator would see first.
- Import cost moves into the request path for those handlers.

## Links

`../architect/architect.md`, `../architect/architect_common.md`.

## Open questions

OPEN: what problem prompted this shape, and when? The code shows the outcome and nothing of the deliberation.

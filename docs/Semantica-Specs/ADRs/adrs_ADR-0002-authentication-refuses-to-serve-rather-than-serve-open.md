---
title: ADR-0002 — Authentication refuses to serve rather than serve open
id: ADR-0002
kind: adr
status: accepted
owner: TBD
updated: 2026-09-21
---

# ADR-0002 — Authentication refuses to serve rather than serve open

## Status

Accepted (reconstructed from code, 2026-09-21) — rationale not recovered.

## Context

- Every Explorer router is mounted with `dependencies=[Depends(require_auth)]` [D: semantica/explorer/app.py:173].
- `require_auth` reads `SEMANTICA_API_KEY` fresh on each call [D: semantica/explorer/dependencies.py:24] and compares a supplied `X-API-Key` with `hmac.compare_digest` [D: semantica/explorer/dependencies.py:70].
- When no key is configured, every protected route returns `503`, not `401` and not `200` [D: semantica/explorer/dependencies.py:60].
- `SEMANTICA_ALLOW_ANONYMOUS=true` bypasses the check and logs a startup warning naming localhost [D: semantica/explorer/app.py:93].

## Decision

An unconfigured server is unavailable rather than open. Anonymous access exists and is explicit, logged and named as development-only [D: semantica/explorer/dependencies.py:48].

## Alternatives considered

OPEN: not recoverable — the repository retains no record of what was rejected. No alternative is invented here.

## Consequences

- A misconfigured deployment fails loudly at the first request instead of silently exposing the graph.
- There is exactly one key for the whole process — no roles, scopes or per-tenant separation [D: semantica/explorer/dependencies.py:24].
- Health, info, root and the SPA catch-all stay unauthenticated [D: semantica/explorer/app.py:217].

## Links

`../architect/architect.md`, `../architect/architect_common.md`.

## Open questions

OPEN: what problem prompted this shape, and when? The code shows the outcome and nothing of the deliberation.

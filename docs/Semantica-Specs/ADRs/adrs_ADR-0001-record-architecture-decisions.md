---
title: ADR-0001 — Record Architecture Decisions
id: ADR-0001
kind: adr
status: accepted
owner: TBD
updated: 2026-09-21
---

# ADR-0001 — Record Architecture Decisions

## Status

Accepted — 2026-09-21.

## Context

This hub was reversed from a codebase of 1,229 files and 460,576 lines whose decisions exist only as code [D: pyproject.toml:1]. Three of the four ADRs here were reconstructed: their context and consequences are visible in the tree, their reasoning is not.

## Decision

Architectural decisions are recorded as ADRs in this directory. A reconstructed ADR states its status as such, derives Context and Consequences from cited code, and leaves Alternatives as an `OPEN:` question rather than inventing a rejected option.

## Alternatives considered

| option | why not |
| --- | --- |
| Leave decisions undocumented | The reversal already found two contradictions that an ADR trail would have surfaced earlier. |
| Back-fill Alternatives from plausibility | A reconstructed ADR that invents its own alternatives forecloses the discussion it should start. |

## Consequences

- Every future decision on this codebase has a place to land.
- The three reconstructed ADRs stay incomplete until someone who was there fills the `OPEN:` lines.

## Links

`../architect/architect.md`.

## Open questions

OPEN: who reviews and accepts an ADR for this project? Governance documents exist [D: GROWTH.md:1] and none names an architecture decision process.

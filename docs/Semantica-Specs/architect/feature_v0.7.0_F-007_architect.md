---
title: Feature Architecture v0.7.0 F-007 — Knowledge Explorer UI and Graph API
id: F-007
kind: architecture
feature: F-007
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Feature Architecture v0.7.0 F-007 — Knowledge Explorer UI and Graph API

> Reversed from code at commit `92c2578a`. The sequence below was read call by call out of the handlers and modules cited.

## Design summary

I: the Explorer is a read-mostly graph viewer with one write path — basis: 23 of its 26 routes are `GET`, the writes being annotation create/delete and a markdown `PUT` [D: semantica/explorer/routes/markdown.py:97]. Its hardest logic is client-side: the temporal scrubber's request lifecycle [D: explorer/src/workspaces/GraphWorkspace/GraphWorkspace.tsx:1465].

## API contracts

26 routes plus a WebSocket channel. Contract: `../data/api-contract_v0.7.0_F-007.md`.

## Data model

Owns the wire projections and annotations. See `../data/data-erd_v0.7.0_F-007.md`.

## Sequence

1. The app mounts thirteen routers, each behind `Depends(require_auth)` [D: semantica/explorer/app.py:173].
2. A graph-updates WebSocket is installed with the same origin allowlist [D: semantica/explorer/app.py:188].
3. `GET /api/graph/nodes` parses an optional viewport bbox, then paginates in a worker thread, returning an opaque forward cursor [D: semantica/explorer/routes/graph.py:111].
4. `limit` is bounded to 5000 and `skip` to non-negative by FastAPI query constraints [D: semantica/explorer/routes/graph.py:108].
5. The SPA is served from the packaged static directory; a missing bundle returns an HTML page with build instructions rather than a 500 [D: semantica/explorer/app.py:195].
6. A request under `api/` that reaches the catch-all is refused with 404 rather than served the SPA shell [D: semantica/explorer/app.py:238].

## Failure modes

| failure | detection | behaviour | source |
| --- | --- | --- | --- |
| Frontend bundle absent | `index.html` existence check | instructional HTML page, status 200 | [D: semantica/explorer/app.py:195] |
| Scrubber polling storm | one in-flight request per position, identical `at` polls deduplicated | idle/play polling loop is broken | [D: explorer/src/workspaces/GraphWorkspace/GraphWorkspace.tsx:1465] |
| Out-of-order snapshot response | response applied only if the scrubber is still on that position | stale frame discarded | [D: explorer/src/workspaces/GraphWorkspace/GraphWorkspace.tsx:1465] |
| Failed or cancelled snapshot request | position remains retryable on revisit | the user can recover by returning | [D: explorer/src/workspaces/GraphWorkspace/GraphWorkspace.tsx:1541] |
| Markdown save conflict (409) | draft retained client-side | recovery path offered | [D: explorer/tests/markdownEditorInteraction.test.tsx:459] |

## Observability

Logging only. `semantica/utils/logging.py:138` provides `get_logger`; `loguru` and `structlog` are declared dependencies [D: pyproject.toml:19]. No metrics client, tracer or span appears anywhere under `semantica/` — no `prometheus`, `opentelemetry` or `statsd` import exists in the package [D: semantica/utils/logging.py:138].

OPEN: what should this feature emit in production? No metric name, dashboard or alert is defined in the repository.

## Traceability

`DOM-007`, stories `F-007-US1`..`F-007-US4`.

## Open questions

OPEN: what was rejected on the way to this shape? The repository retains no record of alternatives, and none is guessed here.
OPEN: what are the latency, throughput and resource targets for F-007? No budget or SLO is expressed in code.

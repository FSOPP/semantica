---
title: API Contract v0.7.0 F-007 — Knowledge Explorer UI and Graph API
id: F-007
status: draft
owner: TBD
updated: 2026-09-21
---

# API Contract v0.7.0 F-007 — Knowledge Explorer UI and Graph API

> Reversed from code at commit `92c2578a`. Every row below is derived from a route decorator; nothing here was designed.

## Surface summary

Twenty-six endpoints: the graph read API [D: semantica/explorer/routes/graph.py:35], the temporal API [D: semantica/explorer/routes/temporal.py:25], markdown resources [D: semantica/explorer/routes/markdown.py:26], annotations [D: semantica/explorer/routes/annotations.py:17], plus the app's own root, health, info and SPA catch-all [D: semantica/explorer/app.py:190]. A WebSocket channel is installed alongside them [D: semantica/explorer/app.py:188].

Authentication on the Explorer application is `X-API-Key`, enforced by `require_auth` [D: semantica/explorer/dependencies.py:48], mounted on every Explorer router [D: semantica/explorer/app.py:173]. Anonymous access is opt-in through `SEMANTICA_ALLOW_ANONYMOUS=true` and is logged as a warning at startup [D: semantica/explorer/app.py:93].

## Endpoints

| Method | Path | Auth | Request | Response | Status | Source |
| --- | --- | --- | --- | --- | --- | --- |
| `GET` | `/` *(corrected)* | None | — | — | 200 | `semantica/explorer/app.py:190` |
| `GET` | `/api/health` *(corrected)* | None | — | — | 200 | `semantica/explorer/app.py:217` |
| `GET` | `/api/info` *(corrected)* | None | — | — | 200 | `semantica/explorer/app.py:221` |
| `GET` | `/{full_path:path}` *(corrected)* | None | — | — | 200 | `semantica/explorer/app.py:236` |
| `GET` | `/api/annotations` | X-API-Key | — | `list[AnnotationResponse]` | 200, 401, 503 | `semantica/explorer/routes/annotations.py:20` |
| `POST` | `/api/annotations` | X-API-Key | `AnnotationCreate` | `AnnotationResponse` | 201, 401, 503 | `semantica/explorer/routes/annotations.py:30` |
| `DELETE` | `/api/annotations/{annotation_id}` | X-API-Key | — | — | 204, 401, 503 | `semantica/explorer/routes/annotations.py:56` |
| `GET` | `/api/graph/nodes` | X-API-Key | — | `NodeListResponse` | 200, 401, 503 | `semantica/explorer/routes/graph.py:101` |
| `GET` | `/api/graph/node` | X-API-Key | — | `NodeResponse` | 200, 401, 503 | `semantica/explorer/routes/graph.py:131` |
| `GET` | `/api/graph/node/{node_id}` | X-API-Key | — | `NodeResponse` | 200, 401, 503 | `semantica/explorer/routes/graph.py:139` |
| `GET` | `/api/graph/node/{node_id}/neighbors` | X-API-Key | — | `list[NeighborResponse]` | 200, 401, 503 | `semantica/explorer/routes/graph.py:147` |
| `GET` | `/api/graph/edges` | X-API-Key | — | `EdgeListResponse` | 200, 401, 503 | `semantica/explorer/routes/graph.py:167` |
| `GET` | `/api/graph/path` | X-API-Key | — | `PathResponse` | 200, 401, 503 | `semantica/explorer/routes/graph.py:340` |
| `GET` | `/api/graph/node/{node_id}/path` | X-API-Key | — | `PathResponse` | 200, 401, 503 | `semantica/explorer/routes/graph.py:351` |
| `POST` | `/api/graph/search` | X-API-Key | `SearchRequest` | `SearchResultResponse` | 200, 401, 503 | `semantica/explorer/routes/graph.py:368` |
| `POST` | `/api/graph/distance-matrix` | X-API-Key | `DistanceMatrixRequest` | `DistanceMatrixResponse` | 200, 401, 503 | `semantica/explorer/routes/graph.py:422` |
| `GET` | `/api/graph/semantic-neighborhood` | X-API-Key | — | `SemanticNeighborhoodResponse` | 200, 401, 503 | `semantica/explorer/routes/graph.py:576` |
| `GET` | `/api/graph/node/{node_id}/semantic-neighborhood` | X-API-Key | — | `SemanticNeighborhoodResponse` | 200, 401, 503 | `semantica/explorer/routes/graph.py:586` |
| `GET` | `/api/graph/stats` | X-API-Key | — | `GraphStatsResponse` | 200, 401, 503 | `semantica/explorer/routes/graph.py:602` |
| `GET` | `/api/markdown/{kind}/{resource_id:path}` | X-API-Key | — | `MarkdownDocumentResponse` | 200, 401, 503 | `semantica/explorer/routes/markdown.py:82` |
| `PUT` | `/api/markdown/{kind}/{resource_id:path}` | X-API-Key | — | `MarkdownApplyResponse` | 200, 401, 503 | `semantica/explorer/routes/markdown.py:97` |
| `GET` | `/api/temporal/snapshot` | X-API-Key | — | `TemporalSnapshotFastResponse` | 200, 401, 503 | `semantica/explorer/routes/temporal.py:64` |
| `GET` | `/api/temporal/diff` | X-API-Key | — | `TemporalDiffResponse` | 200, 401, 503 | `semantica/explorer/routes/temporal.py:79` |
| `GET` | `/api/temporal/patterns` | X-API-Key | — | `TemporalPatternResponse` | 200, 401, 503 | `semantica/explorer/routes/temporal.py:103` |
| `GET` | `/api/temporal/bounds` | X-API-Key | — | `TemporalBoundsResponse` | 200, 401, 503 | `semantica/explorer/routes/temporal.py:123` |
| `GET` | `/api/temporal/distance-history` | X-API-Key | — | `DistanceHistoryResponse` | 200, 401, 503 | `semantica/explorer/routes/temporal.py:131` |

Request and response cells name the pydantic model declared on the route decorator [D: semantica/explorer/schemas.py:1]. A model with no `$defs` entry in `schema/schemas.json` is a wire shape this reversal did not lift — it is named, not redefined.

## Events

One WebSocket channel for graph updates, installed at `semantica/explorer/app.py:188` [D: semantica/explorer/app.py:188]. It is not an AsyncAPI broker channel: no topic literal, no publish/subscribe descriptor and no broker client appears in the surveyed non-test code.

OPEN: is the WebSocket channel's message envelope a stable contract, or an internal detail of the bundled UI? Nothing in the repository states this.

## Error model

FastAPI's default error envelope, `{"detail": <string>}`, raised through `HTTPException` [D: semantica/explorer/dependencies.py:71]. Status codes seen on protected routes: `401` for a missing or non-matching `X-API-Key` [D: semantica/explorer/dependencies.py:72], `503` when neither `SEMANTICA_API_KEY` nor `SEMANTICA_ALLOW_ANONYMOUS=true` is set [D: semantica/explorer/dependencies.py:60], `404` for an absent resource [D: semantica/explorer/routes/annotations.py:38].

I: there is no feature-specific error taxonomy — basis: every error site reached from these handlers raises `HTTPException` with a prose `detail` and no machine-readable code field [D: semantica/explorer/dependencies.py:71].

## Versioning and compatibility

The package version is `0.7.0` [D: pyproject.toml:1]. No path carries a version segment [D: semantica/explorer/app.py:173], and the repository holds no OpenAPI, AsyncAPI, proto or GraphQL file to compare a contract against.

OPEN: what may change in these payloads without a major version bump, and how long is a removed field kept? Nothing in the repository expresses a compatibility window.
OPEN: is the Explorer HTTP surface a supported public contract, or an internal API for the bundled UI only?

## Spec files

- `schema/openapi_v0.7.0_F-007.json` — one path item per row above; entity shapes are `$ref`'d into `schema/schemas.json`, never inlined.
- `schema/asyncapi_v0.7.0_F-007.json` — present; empty channels unless this feature publishes.
- `fixtures/fixtures_v0.7.0_F-007.json` — records validated against `schemas.json` by `route.py`.

## Traceability

Stories: `PRDs/prd_v0.7.0_F-007-knowledge-explorer-ui-and-graph-api.md`. Domain rules: `ddd/domain_DOM-007-knowledge-explorer-ui-and-graph-api.md`. Test cases: `tests/test_v0.7.0_F-007.md`.

## Open questions

OPEN: which consumers exist for this surface besides the bundled Explorer UI? The repository names none.
OPEN: is there a rate limit, quota or request-size ceiling in front of this API in any deployed environment? None is expressed in code.

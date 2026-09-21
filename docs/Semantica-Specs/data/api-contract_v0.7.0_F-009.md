---
title: API Contract v0.7.0 F-009 — CLI MCP Server and Agent Integrations
id: F-009
status: draft
owner: TBD
updated: 2026-09-21
---

# API Contract v0.7.0 F-009 — CLI MCP Server and Agent Integrations

> Reversed from code at commit `92c2578a`. Every row below is derived from a route decorator; nothing here was designed.

## Surface summary

Four endpoints on a second FastAPI application [D: semantica/server.py:149], separate from the Explorer app. The primary surface of this feature is the CLI: 91 `click` commands [D: semantica/cli.py:545] and the MCP JSON-RPC server [D: semantica_mcp/mcp/server.py:63].

Authentication on the Explorer application is `X-API-Key`, enforced by `require_auth` [D: semantica/explorer/dependencies.py:48], mounted on every Explorer router [D: semantica/explorer/app.py:173]. Anonymous access is opt-in through `SEMANTICA_ALLOW_ANONYMOUS=true` and is logged as a warning at startup [D: semantica/explorer/app.py:93].

## Endpoints

| Method | Path | Auth | Request | Response | Status | Source |
| --- | --- | --- | --- | --- | --- | --- |
| `GET` | `/api/info` | None | — | — | 200 | `semantica/server.py:149` |
| `GET` | `/health` | None | — | — | 200 | `semantica/server.py:161` |
| `POST` | `/build` | X-API-Key | — | — | 200, 401, 503 | `semantica/server.py:166` |
| `GET` | `/{full_path:path}` | None | — | — | 200 | `semantica/server.py:219` |

Request and response cells name the pydantic model declared on the route decorator [D: semantica/explorer/schemas.py:1]. A model with no `$defs` entry in `schema/schemas.json` is a wire shape this reversal did not lift — it is named, not redefined.

## Events

None. The survey found no message-broker topic, exchange or channel literal in this feature's non-test code — the nine "events" it reported are all string literals inside test files. `schema/asyncapi_v0.7.0_F-009.json` is therefore present and empty by design.

## Error model

FastAPI's default error envelope, `{"detail": <string>}`, raised through `HTTPException` [D: semantica/explorer/dependencies.py:71]. Status codes seen on protected routes: `401` for a missing or non-matching `X-API-Key` [D: semantica/explorer/dependencies.py:72], `503` when neither `SEMANTICA_API_KEY` nor `SEMANTICA_ALLOW_ANONYMOUS=true` is set [D: semantica/explorer/dependencies.py:60], `404` for an absent resource [D: semantica/explorer/routes/annotations.py:38].

I: there is no feature-specific error taxonomy — basis: every error site reached from these handlers raises `HTTPException` with a prose `detail` and no machine-readable code field [D: semantica/explorer/dependencies.py:71].

## Versioning and compatibility

The package version is `0.7.0` [D: pyproject.toml:1]. No path carries a version segment [D: semantica/explorer/app.py:173], and the repository holds no OpenAPI, AsyncAPI, proto or GraphQL file to compare a contract against.

OPEN: what may change in these payloads without a major version bump, and how long is a removed field kept? Nothing in the repository expresses a compatibility window.
OPEN: is the Explorer HTTP surface a supported public contract, or an internal API for the bundled UI only?

## Spec files

- `schema/openapi_v0.7.0_F-009.json` — one path item per row above; entity shapes are `$ref`'d into `schema/schemas.json`, never inlined.
- `schema/asyncapi_v0.7.0_F-009.json` — present; empty channels unless this feature publishes.
- `fixtures/fixtures_v0.7.0_F-009.json` — records validated against `schemas.json` by `route.py`.

## Traceability

Stories: `PRDs/prd_v0.7.0_F-009-cli-mcp-server-and-agent-integrations.md`. Domain rules: `ddd/domain_DOM-009-cli-mcp-server-and-agent-integrations.md`. Test cases: `tests/test_v0.7.0_F-009.md`.

## Open questions

OPEN: which consumers exist for this surface besides the bundled Explorer UI? The repository names none.
OPEN: is there a rate limit, quota or request-size ceiling in front of this API in any deployed environment? None is expressed in code.

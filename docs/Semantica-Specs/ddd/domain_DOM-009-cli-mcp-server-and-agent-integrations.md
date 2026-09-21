---
title: Domain — CLI MCP Server and Agent Integrations
id: DOM-009
kind: domain
feature: F-009
status: draft
owner: TBD
updated: 2026-09-21
---

# Domain — CLI MCP Server and Agent Integrations

> Reversed from code at commit `92c2578a`. Every rule below was promoted from a comment or a test name in the code, and cites both the statement and the code that enforces it.

## Ubiquitous language

| term | definition | aliases to avoid |
| --- | --- | --- |
| command group | A `click` group: `kg`, `embed`, `reason`, `decision`, `services`, `config` [D: semantica/cli.py:632]. | namespace |
| tool | An MCP callable dispatched by name through `call_tool` [D: semantica_mcp/mcp/server.py:63]. | endpoint |
| integration | An adapter exposing Semantica to an agent framework — agno, crewai, google_adk [D: integrations/crewai/kg_tool.py:56]. | plugin |

## Actors

Operators at a terminal [D: semantica/cli.py:545], MCP clients over JSON-RPC [D: semantica_mcp/mcp/server.py:63], and agent frameworks calling the integration tools [D: integrations/crewai/kg_tool.py:387].

## Business rules

**`DOM-009-R1`** — Every JSON Lines record occupies exactly one line, and a bare dict is wrapped in a list.

I: Every JSON Lines record occupies exactly one line, and a bare dict is wrapped in a list — basis: the code states "every record must occupy exactly one line; wrap a bare dict in a list so callers never need to know whether their result is singular or plural" at `semantica/cli.py:2338`, and it is enforced at `semantica/cli.py:2338`
**`DOM-009-R2`** — A present-but-wrongly-typed rules value is an error, not a fallback.

I: A present-but-wrongly-typed rules value is an error, not a fallback — basis: the code states "a present-but-non-list value must be a clear error, not silently fall through to reinterpreting the raw file text as plain text" at `semantica/cli.py:1268`, and it is enforced at `semantica/cli.py:1268`
**`DOM-009-R3`** — A tool error surfaces the exception class name and nothing else.

I: A tool error surfaces the exception class name and nothing else — basis: the code states "the exception's class name is safe to surface — unlike str(exc), it never carries paths or connection strings" at `semantica_mcp/mcp/server.py:115`, and it is enforced at `semantica_mcp/mcp/server.py:115`
**`DOM-009-R4`** — Repeated graph tool calls are idempotent, and concurrent calls on one graph are serialised.

I: Repeated graph tool calls are idempotent, and concurrent calls on one graph are serialised — basis: the code states "duplicate nodes/edges are skipped so repeated calls are idempotent; one re-entrant lock per graph because check-then-act is not atomic" at `integrations/crewai/kg_tool.py:387`, and it is enforced at `integrations/crewai/kg_tool.py:56`
**`DOM-009-R5`** — A partial or streaming agent event is never persisted.

I: A partial or streaming agent event is never persisted — basis: the code states "ADK's own base implementation is a no-op for partial/streaming events, so a graph-backed session must not persist them either" at `integrations/google_adk/session_service.py:490`, and it is enforced at `integrations/google_adk/session_service.py:490`
**`DOM-009-R6`** — An error message built from unknown keys is size-bounded.

I: An error message built from unknown keys is size-bounded — basis: the code states "truncating each key bounds the per-key cost; capping the count of keys shown bounds the total" at `semantica/utils/helpers.py:702`, and it is enforced at `semantica/utils/helpers.py:702`
## Process flow

1. An operator runs a command in one of six groups [D: semantica/cli.py:632].
2. `kg build` constructs a graph [D: semantica/cli.py:1154].
3. Output is emitted as JSON Lines, one record per line [D: semantica/cli.py:2338].
4. `mcp start` launches the JSON-RPC server [D: semantica/cli.py:5407].
5. A client lists tools then calls one by name [D: semantica_mcp/mcp/server.py:93].
6. An agent framework reaches the same objects through its integration adapter [D: integrations/crewai/kg_tool.py:387].

## Invariants

- A tool error never exposes a path or connection string [D: semantica_mcp/mcp/server.py:115].
- Two concurrent tool calls on one graph cannot double-count a duplicate add [D: integrations/crewai/kg_tool.py:56].

## Implementation status

| rule | status | evidence |
| --- | --- | --- |
| `DOM-009-R1` | wip — unverified, run pytest -q | — |
| `DOM-009-R2` | wip — unverified, run pytest -q | — |
| `DOM-009-R3` | wip — unverified, run pytest -q | — |
| `DOM-009-R4` | wip — unverified, run pytest -q | — |
| `DOM-009-R5` | wip — unverified, run pytest -q | — |
| `DOM-009-R6` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Open questions

OPEN: which of the 91 CLI commands are the supported surface? None is marked deprecated, and one is explicitly `hidden=True` [D: semantica/cli.py:1179].
OPEN: is `semantica/server.py` supported alongside the Explorer app? It serves a second `/api/info` and a differently-worded health payload [D: semantica/server.py:161].
OPEN: what is the MCP tool contract's compatibility promise? Tools are dispatched by name with no version negotiation [D: semantica_mcp/mcp/server.py:105].

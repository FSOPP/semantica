---
title: Feature Architecture v0.7.0 F-009 — CLI MCP Server and Agent Integrations
id: F-009
kind: architecture
feature: F-009
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Feature Architecture v0.7.0 F-009 — CLI MCP Server and Agent Integrations

> Reversed from code at commit `92c2578a`. The sequence below was read call by call out of the handlers and modules cited.

## Design summary

I: the CLI is the primary interface and the MCP server, agent integrations and `semantica/server.py` are three thinner surfaces over the same objects — basis: `semantica/cli.py` carries 91 commands in 5400+ lines [D: semantica/cli.py:545] against four HTTP routes in `server.py` [D: semantica/server.py:149], and `mcp start` and the CLI dispatch through the same server module [D: semantica/cli.py:5407].

## API contracts

Four HTTP routes plus 91 CLI commands and the MCP tool surface. Contract: `../data/api-contract_v0.7.0_F-009.md`.

## Data model

Read-only over the graph entities. See `../data/data-erd_v0.7.0_F-009.md`.

## Sequence

1. `main` is a `click.group` with sub-groups `kg`, `embed`, `reason`, `decision`, `services` and `config` [D: semantica/cli.py:545].
2. `kg build` constructs a graph from sources [D: semantica/cli.py:1154]; `kg query`, `stats`, `analyze`, `find-path`, `resolve`, `predict`, `validate`, `global` and `drift` read it [D: semantica/cli.py:1528].
3. JSON Lines output puts every record on exactly one line, wrapping a bare dict in a list [D: semantica/cli.py:2338].
4. `mcp start` and in-process dispatch share one server module [D: semantica/cli.py:5407].
5. MCP tool calls are dispatched by name through `call_tool` [D: semantica_mcp/mcp/server.py:63], over seven tool modules: decisions, export, extraction, graph, reasoning, retrieval.
6. CrewAI graph tools take one re-entrant lock per graph, so independent graphs are never serialised against each other [D: integrations/crewai/kg_tool.py:56].

## Failure modes

| failure | detection | behaviour | source |
| --- | --- | --- | --- |
| Tool raising an internal error | class name surfaced, `str(exc)` withheld | no path or connection string leaks to the caller | [D: semantica_mcp/mcp/server.py:115] |
| `premises: null` in a rules file | present-but-non-list detected | clear error instead of silent plain-text reinterpretation | [D: semantica/cli.py:1268] |
| Concurrent duplicate adds on one graph | per-graph re-entrant lock around check-then-act | duplicates cannot be double-counted | [D: integrations/crewai/kg_tool.py:56] |
| Streaming/partial ADK event | not persisted, matching ADK's own base behaviour | no event node per streamed chunk | [D: integrations/google_adk/session_service.py:490] |
| Oversized unknown-key payload in an error message | per-key truncation plus a key-count cap | message and log size stay bounded | [D: semantica/utils/helpers.py:702] |

## Observability

Logging only. `semantica/utils/logging.py:138` provides `get_logger`; `loguru` and `structlog` are declared dependencies [D: pyproject.toml:19]. No metrics client, tracer or span appears anywhere under `semantica/` — no `prometheus`, `opentelemetry` or `statsd` import exists in the package [D: semantica/utils/logging.py:138].

OPEN: what should this feature emit in production? No metric name, dashboard or alert is defined in the repository.

## Traceability

`DOM-009`, stories `F-009-US1`..`F-009-US4`.

## Open questions

OPEN: what was rejected on the way to this shape? The repository retains no record of alternatives, and none is guessed here.
OPEN: what are the latency, throughput and resource targets for F-009? No budget or SLO is expressed in code.

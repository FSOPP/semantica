---
title: PRD v0.7.0 F-009 — CLI MCP Server and Agent Integrations
id: F-009
kind: prd
feature: F-009
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# PRD v0.7.0 F-009 — CLI MCP Server and Agent Integrations

> **Reversed, and weakly.** A requirement states intent; intent is not in a repository. Every story below was inferred from endpoints and test names, and every business question is `OPEN:`.

## Summary

I: CLI MCP Server and Agent Integrations exists to give operators and agents a way in that is not a browser — basis: the surface this feature exposes and the tests that assert it, as catalogued in `../data/api-contract_v0.7.0_F-009.md` and `../tests/test_v0.7.0_F-009.md`.

## User stories

**`F-009-US1`** — As an operator, I want to drive the whole system from a terminal, so that automation does not require the HTTP API.

I: inferred from the shipped surface — basis: 91 CLI commands in six groups [D: semantica/cli.py:545]

**`F-009-US2`** — As a script author, I want to pipe CLI output into another tool, so that one record per line parses without special cases.

I: inferred from the shipped surface — basis: JSON Lines discipline [D: semantica/cli.py:2338]

**`F-009-US3`** — As an AI agent, I want to call graph and decision tools over MCP, so that the system is reachable from an agent runtime.

I: inferred from the shipped surface — basis: seven MCP tool modules [D: semantica_mcp/mcp/server.py:63]

**`F-009-US4`** — As an agent developer, I want to use Semantica from agno, CrewAI or Google ADK, so that I stay in my framework.

I: inferred from the shipped surface — basis: three integration adapters [D: integrations/crewai/kg_tool.py:56]

## Acceptance criteria

- **`F-009-US1`** — Given the feature is configured, when drive the whole system from a terminal, then the behaviour named in `91 CLI commands in six groups` holds. I: lifted from the shipped surface, not from a stated requirement — basis: 91 CLI commands in six groups [D: semantica/cli.py:545]
- **`F-009-US2`** — Given the feature is configured, when pipe CLI output into another tool, then the behaviour named in `JSON Lines discipline` holds. I: lifted from the shipped surface, not from a stated requirement — basis: JSON Lines discipline [D: semantica/cli.py:2338]
- **`F-009-US3`** — Given the feature is configured, when call graph and decision tools over MCP, then the behaviour named in `seven MCP tool modules` holds. I: lifted from the shipped surface, not from a stated requirement — basis: seven MCP tool modules [D: semantica_mcp/mcp/server.py:63]
- **`F-009-US4`** — Given the feature is configured, when use Semantica from agno, CrewAI or Google ADK, then the behaviour named in `three integration adapters` holds. I: lifted from the shipped surface, not from a stated requirement — basis: three integration adapters [D: integrations/crewai/kg_tool.py:56]

## Implementation status

| story | status | evidence |
| --- | --- | --- |
| `F-009-US1` | wip — unverified, run pytest -q | — |
| `F-009-US2` | wip — unverified, run pytest -q | — |
| `F-009-US3` | wip — unverified, run pytest -q | — |
| `F-009-US4` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Scope boundaries

OPEN: what is deliberately out of scope for this feature? The code draws module boundaries; it does not record a decision to exclude anything.

## Dependencies

Domain rules: `DOM-009`. Architecture: `../architect/feature_v0.7.0_F-009_architect.md`. Other features this one imports from are listed in `../architect/architect.md`.

## Metrics

OPEN: how is success measured for this feature after release? No metric, event or analytics call exists in the code.
OPEN: what is the business priority of this feature relative to the other eight? Nothing in the repository ranks them.

## Open questions

OPEN: who asked for this, and what problem were they reporting? Not recoverable from the working tree.
OPEN: which stories are load-bearing for a paying user and which are conveniences? The code treats every route identically.

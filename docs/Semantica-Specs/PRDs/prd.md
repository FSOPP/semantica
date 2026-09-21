---
title: Master PRD — Semantica
status: draft
owner: TBD
updated: 2026-09-21
---

# Master PRD — Semantica

> **Reversed.** This is the weakest document in the hub by construction: it asks what the product is for, and a repository does not answer that. Read the `OPEN:` lines as the deliverable.

## Problem and outcome

The repository describes itself as "Graph-Native Infrastructure for Context and Accountable AI Systems: context graphs, decision intelligence, full provenance" [D: pyproject.toml:1], and the published documentation site as "The Context and Semantic Layer for AI in High-Stakes Domains" [D: docs/docs.json:1].

OPEN: what observable outcome means the problem is solved? Neither line states a measurable change for anyone.
OPEN: which high-stakes domains are the target? The test suite names loan underwriting [D: tests/vector_store/test_end_to_end_decision_tracking.py:403]; nothing else in the tree names a market.

## MVP definition

OPEN: not recoverable. The tree at `0.7.0` carries 88 HTTP routes, 91 CLI commands and 45 storage backends [D: pyproject.toml:7]; nothing records which subset was the first shippable slice, and reconstructing one from git history would be a guess dressed as a fact.

## Personas and top user flows

I: four consumer shapes are visible in the surface — basis: the four entry points and what each exposes [D: Dockerfile:1].

| consumer | reached through | evidence |
| --- | --- | --- |
| Operator / data engineer | 91 CLI commands | [D: semantica/cli.py:545] |
| Analyst / reviewer | Explorer UI over 84 routes | [D: semantica/explorer/app.py:173] |
| AI agent | MCP tools and three framework adapters | [D: semantica_mcp/mcp/server.py:63] |
| Application developer | the Python package API | [D: pyproject.toml:361] |

OPEN: which of these four is the primary persona? The repository invests heavily in all four.

## Child PRD index

| version | feature | endpoints | link |
| --- | --- | --- | --- |
| v0.7.0 | F-001 — Ingest and Parse Pipeline | 0 | `prd_v0.7.0_F-001-ingest-and-parse-pipeline.md` |
| v0.7.0 | F-002 — Knowledge Graph Construction and Semantic Extraction | 4 | `prd_v0.7.0_F-002-knowledge-graph-construction-and-semantic-extraction.md` |
| v0.7.0 | F-003 — Storage Backends | 0 | `prd_v0.7.0_F-003-storage-backends.md` |
| v0.7.0 | F-004 — Ontology and Vocabulary Management | 39 | `prd_v0.7.0_F-004-ontology-and-vocabulary-management.md` |
| v0.7.0 | F-005 — Context Graph and Decision Intelligence | 9 | `prd_v0.7.0_F-005-context-graph-and-decision-intelligence.md` |
| v0.7.0 | F-006 — Provenance Reasoning and Explainability | 3 | `prd_v0.7.0_F-006-provenance-reasoning-and-explainability.md` |
| v0.7.0 | F-007 — Knowledge Explorer UI and Graph API | 26 | `prd_v0.7.0_F-007-knowledge-explorer-ui-and-graph-api.md` |
| v0.7.0 | F-008 — Export and Interchange | 3 | `prd_v0.7.0_F-008-export-and-interchange.md` |
| v0.7.0 | F-009 — CLI MCP Server and Agent Integrations | 4 | `prd_v0.7.0_F-009-cli-mcp-server-and-agent-integrations.md` |

## Non-functional requirements

Four numbers are actually configured, and they are the only quantified limits in the tree [D: semantica/explorer/routes/ontology.py:138]:

| concern | value | key | source |
| --- | --- | --- | --- |
| SHACL payload ceiling | 262144 bytes | `SEMANTICA_MAX_SHACL_TURTLE_BYTES` | [D: semantica/explorer/routes/ontology.py:138] |
| SHACL graph ceiling | 1000 triples | `SEMANTICA_MAX_SHACL_TRIPLES` | [D: semantica/explorer/routes/ontology.py:141] |
| SHACL validation timeout | 15.0 seconds | `SEMANTICA_MAX_SHACL_TIMEOUT` | [D: semantica/explorer/routes/ontology.py:144] |
| SHACL concurrency | 4 | `SEMANTICA_MAX_SHACL_CONCURRENCY` | [D: semantica/explorer/routes/ontology.py:147] |
| Graph page size ceiling | 5000 | `limit` query constraint | [D: semantica/explorer/routes/graph.py:108] |
| Extraction confidence floors | 0.7 entities, 0.6 relations | hardcoded | [D: semantica/explorer/routes/enrich.py:207] |

Security is the one non-functional area with a stated posture: an unconfigured API key refuses service rather than serving openly [D: semantica/explorer/dependencies.py:60].

OPEN: what availability target does this system carry? Nothing expresses one.
OPEN: what is the performance budget for a graph read, an extraction call or a SHACL validation? Only the four ceilings above bound anything, and they bound cost, not latency.
OPEN: what accessibility standard does the Explorer UI hold itself to? The markdown viewer's tests assert tab semantics and labelling [D: explorer/tests/markdownContentViewer.test.ts:322] with no stated standard behind them.
OPEN: what compliance regime applies? `SECURITY.md` exists [D: SECURITY.md:1]; no data-handling or residency requirement appears in code.

## Traceability

| feature | domain | architecture | tasks | tests |
| --- | --- | --- | --- | --- |
| F-001 | `DOM-001` | `../architect/feature_v0.7.0_F-001_architect.md` | `../tasks/tasks_v0.7.0_F-001.md` | `../tests/test_v0.7.0_F-001.md` |
| F-002 | `DOM-002` | `../architect/feature_v0.7.0_F-002_architect.md` | `../tasks/tasks_v0.7.0_F-002.md` | `../tests/test_v0.7.0_F-002.md` |
| F-003 | `DOM-003` | `../architect/feature_v0.7.0_F-003_architect.md` | `../tasks/tasks_v0.7.0_F-003.md` | `../tests/test_v0.7.0_F-003.md` |
| F-004 | `DOM-004` | `../architect/feature_v0.7.0_F-004_architect.md` | `../tasks/tasks_v0.7.0_F-004.md` | `../tests/test_v0.7.0_F-004.md` |
| F-005 | `DOM-005` | `../architect/feature_v0.7.0_F-005_architect.md` | `../tasks/tasks_v0.7.0_F-005.md` | `../tests/test_v0.7.0_F-005.md` |
| F-006 | `DOM-006` | `../architect/feature_v0.7.0_F-006_architect.md` | `../tasks/tasks_v0.7.0_F-006.md` | `../tests/test_v0.7.0_F-006.md` |
| F-007 | `DOM-007` | `../architect/feature_v0.7.0_F-007_architect.md` | `../tasks/tasks_v0.7.0_F-007.md` | `../tests/test_v0.7.0_F-007.md` |
| F-008 | `DOM-008` | `../architect/feature_v0.7.0_F-008_architect.md` | `../tasks/tasks_v0.7.0_F-008.md` | `../tests/test_v0.7.0_F-008.md` |
| F-009 | `DOM-009` | `../architect/feature_v0.7.0_F-009_architect.md` | `../tasks/tasks_v0.7.0_F-009.md` | `../tests/test_v0.7.0_F-009.md` |

## Open questions

OPEN: who decides what ships? 78 contributors appear in the history, one owning 54.6% of files.
OPEN: is the Explorer HTTP API a product or an implementation detail of the bundled UI? This single question changes the compatibility obligations of 84 routes.

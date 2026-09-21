---
title: Master Architecture — Semantica
status: draft
owner: TBD
updated: 2026-09-21
---

# Master Architecture — Semantica

> System-level view reversed from code at commit `92c2578a`.

## System context

Semantica is distributed as a Python package with optional extras [D: pyproject.toml:7]. Four runtime entry points exist [D: Dockerfile:1]:

| entry point | form | source |
| --- | --- | --- |
| `semantica` CLI | 91 `click` commands | [D: semantica/cli.py:545] |
| Knowledge Explorer | FastAPI app + bundled React SPA | [D: semantica/explorer/app.py:190] |
| `semantica.server` | a second, smaller FastAPI app | [D: semantica/server.py:149] |
| MCP server | JSON-RPC tool dispatch | [D: semantica_mcp/mcp/server.py:63] |

The container runs the Explorer app only: `uvicorn semantica.explorer.app:app --host 0.0.0.0 --port 8000` [D: Dockerfile:1].

Crossing the boundary inward: source systems reached by 34 ingestors [D: semantica/ingest/registry.py:1], and HTTP callers holding an `X-API-Key` [D: semantica/explorer/dependencies.py:48]. Crossing outward: 19 exporters [D: semantica/export/registry.py:1], graph, vector and triplet stores, and LLM provider clients [D: semantica/llms/openai.py:1].

## Component view

| component | responsibility | owns | talks to |
| --- | --- | --- | --- |
| `semantica/ingest` | pull records from 34 source types | nothing durable | `semantica/parse` |
| `semantica/parse`, `normalize`, `split` | turn raw records into normalised chunks | nothing durable | `semantica/semantic_extract` |
| `semantica/semantic_extract` | entities, relations, events, coreference, triplets | extraction cache [D: semantica/semantic_extract/cache.py:319] | `semantica/kg`, `semantica/llms` |
| `semantica/conflicts`, `deduplication` | detect and resolve contradictions and duplicates | nothing durable | `semantica/kg` |
| `semantica/kg` | build and analyse the graph | `ContextNode`, `ContextEdge` | store tiers |
| `semantica/graph_store` / `vector_store` / `triplet_store` | persist to 11 / 19 / 15 backends | the persisted graph | vendor services |
| `semantica/ontology` | OWL, SHACL, SKOS schema management | `OntologyEntry` | `semantica/kg` |
| `semantica/reasoning` | Rete, Datalog and SPARQL inference | derived triples | `semantica/kg` |
| `semantica/provenance` | W3C PROV-O records | provenance graph | every stage |
| `semantica/context` | context graph, agent memory, decisions, policy | `DecisionResponse`, memories | `semantica/kg` |
| `semantica/export` | serialise to 19 formats | nothing | files, downstream systems |
| `semantica/explorer` | HTTP API and the bundled SPA | in-memory `GraphSession` | every component above |
| `semantica_mcp` | MCP tool surface over the same objects | nothing | `semantica/context`, `semantica/kg` |

Dependency direction runs one way, ingest to export; `semantica/utils` is the only package every tier imports [D: semantica/utils/logging.py:1].

## Data architecture

The entity registry and relationship map live in `../data/data-master-erd.md`. At system level: there is no database migration story, no schema snapshot and no ORM [D: pyproject.toml:361]. Persistence is per-backend and format-owning — FAISS writes its own index files [D: semantica/vector_store/faiss_store.py:300], the context graph writes JSON through an atomic temp-file rename [D: semantica/context/context_graph.py:1409].

## API surface

88 HTTP routes across two applications [D: semantica/explorer/app.py:173]:

| group | routes | auth | consumer |
| --- | --- | --- | --- |
| `/api/ontology`, `/api/vocabulary`, `/api/sparql` | 39 | `X-API-Key` | Explorer UI, F-004 |
| `/api/graph`, `/api/temporal`, `/api/markdown`, `/api/annotations` | 22 | `X-API-Key` | Explorer UI, F-007 |
| `/api/decisions`, `/api/analytics`, `/api/memories` | 9 | `X-API-Key` | Explorer UI, F-005 |
| `/api/enrich/*` | 4 | `X-API-Key` | Explorer UI, F-002 |
| `/api/export`, `/api/import` | 3 | `X-API-Key` | Explorer UI, F-008 |
| `/api/provenance*`, `/api/reason` | 3 | `X-API-Key` | Explorer UI, F-006 |
| `/`, `/api/health`, `/api/info`, SPA catch-all | 4 | none | browsers |
| `semantica/server.py`: `/api/info`, `/health`, `/build`, catch-all | 4 | mixed [D: semantica/server.py:194] | F-009 |

**Finding.** Two applications serve `/api/info` and a health route with different payloads: `{"status": "healthy"}` [D: semantica/server.py:161] against `{"status": "ok"}` [D: semantica/explorer/app.py:219], and `"Semantica API"` against `"Semantica Knowledge Explorer"` [D: semantica/server.py:149]. Two contracts for one product name.

OPEN: is `semantica/server.py` a supported surface, a legacy one, or a development convenience? Nothing states which app a deployment should run, and only the Explorer app is in the container command [D: Dockerfile:1].

## Cross-cutting concerns

Auth, CORS, SSRF, credential redaction, logging and the CI gate are all in `architect_common.md`. One cross-cutting rule is worth naming here: contract violations in the pipeline are treated as deterministic failures and never retried [D: semantica/pipeline/execution_engine.py:395].

## Decision index

| ADR | decision | affected components |
| --- | --- | --- |
| `ADR-0001` | record architecture decisions | all |
| `ADR-0002` | authentication refuses to serve rather than serve open | `semantica/explorer` |
| `ADR-0003` | pluggable backends behind a per-package registry | six store and IO packages |
| `ADR-0004` | optional dependencies degrade to `503` at the route | `semantica/explorer` |

Each reconstructed ADR states its context from code and leaves rationale `OPEN:`.

## Feature architecture index

| version | feature | document |
| --- | --- | --- |
| v0.7.0 | F-001 — Ingest and Parse Pipeline | `feature_v0.7.0_F-001_architect.md` |
| v0.7.0 | F-002 — Knowledge Graph Construction and Semantic Extraction | `feature_v0.7.0_F-002_architect.md` |
| v0.7.0 | F-003 — Storage Backends | `feature_v0.7.0_F-003_architect.md` |
| v0.7.0 | F-004 — Ontology and Vocabulary Management | `feature_v0.7.0_F-004_architect.md` |
| v0.7.0 | F-005 — Context Graph and Decision Intelligence | `feature_v0.7.0_F-005_architect.md` |
| v0.7.0 | F-006 — Provenance Reasoning and Explainability | `feature_v0.7.0_F-006_architect.md` |
| v0.7.0 | F-007 — Knowledge Explorer UI and Graph API | `feature_v0.7.0_F-007_architect.md` |
| v0.7.0 | F-008 — Export and Interchange | `feature_v0.7.0_F-008_architect.md` |
| v0.7.0 | F-009 — CLI MCP Server and Agent Integrations | `feature_v0.7.0_F-009_architect.md` |

## Open questions

OPEN: what is the intended deployment topology? Seven deployment targets are committed — azure, fly, gcp, helm, kubernetes, railway, render [D: deploy/helm/knowledge-explorer/Chart.yaml:1] — and none is marked primary.
OPEN: where is the trust boundary meant to sit? Today every protected route shares one process-wide API key [D: semantica/explorer/dependencies.py:24]; there are no roles, scopes or per-tenant separation.
OPEN: what scale is this built for? No limit, quota or capacity target appears anywhere in the code.

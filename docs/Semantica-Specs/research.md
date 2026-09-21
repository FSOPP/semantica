---
title: Research & Reference Material — Semantica
status: draft
owner: TBD
updated: 2026-09-21
---

# Research & Reference Material — Semantica

> What the repository integrates with and what it cites. Reversed at commit `92c2578a`.

## Third-party integrations

| area | integrations | source |
| --- | --- | --- |
| Source systems | BigQuery, Databricks, Power BI, Redshift, Salesforce, SAP, Snowflake, MongoDB, DuckDB, Elasticsearch, HuggingFace, Google Drive, Kafka, IMAP/POP3, git repositories, MCP resources | [D: semantica/ingest/registry.py:1] |
| Graph stores | Neo4j, Amazon Neptune, FalkorDB, Apache AGE | [D: semantica/graph_store/registry.py:1] |
| Vector stores | FAISS, Milvus, Pinecone, Qdrant, Weaviate, pgvector, sqlite-vec | [D: semantica/vector_store/registry.py:1] |
| Triplet stores | Anzo, Blazegraph, Jena, Oxigraph, RDF4J | [D: semantica/triplet_store/registry.py:1] |
| LLM providers | Anthropic, OpenAI, DeepSeek, Gemini, Groq, HuggingFace, LiteLLM, Novita, Ollama | [D: semantica/llms/openai.py:1] |
| Agent frameworks | agno, CrewAI, Google ADK, LangChain | [D: integrations/crewai/kg_tool.py:56] |

## Standards implemented

W3C PROV-O [D: semantica/provenance/manager.py:1290], OWL, SHACL and SKOS [D: semantica/explorer/routes/ontology.py:2922], SPARQL [D: semantica/explorer/routes/sparql.py:209], RDF via rdflib [D: pyproject.toml:19], Model Context Protocol [D: semantica_mcp/mcp/server.py:63].

## Spikes

OPEN: none are recorded. Two in-code notes point at unresolved work: issue #1147 for the RDF default metadata subject [D: semantica/export/rdf_exporter.py:920], and issue #1355 for an MCP session module that never defined `MCPSession` [D: semantica/cli.py:5407].

## Reference material

The repository publishes a documentation site under `docs/` (Mintlify, 22 guides and 15+ reference pages) [D: docs/docs.json:1], alongside `ARCHITECTURE.md`, `README.md`, `CONTRIBUTING.md`, `SECURITY.md` and `GROWTH.md`.

## Open questions

OPEN: which of the 45 storage backends and 9 LLM providers are exercised in CI? Only the ADK integration tests run there explicitly [D: .github/workflows/ci.yml:181].

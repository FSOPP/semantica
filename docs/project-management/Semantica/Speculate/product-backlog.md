---
title: Product Backlog — Semantica
status: draft
owner: TBD
updated: 2026-09-21
---

# Product Backlog — Semantica

> The one genuinely useful artefact at this end of a reversed hub: the confirmed feature split, sized by what shipped. Value and priority are `OPEN:` because a repository cannot rank its own features.

## Backlog

| id | feature | as-built size | value | priority |
| --- | --- | --- | --- | --- |
| `F-001` | Ingest and Parse Pipeline | 0 endpoints; 34 ingestors, 22 parsers | OPEN | OPEN |
| `F-002` | Knowledge Graph Construction and Semantic Extraction | 4 endpoints; extraction, conflicts, dedup, kg | OPEN | OPEN |
| `F-003` | Storage Backends | 0 endpoints; 45 storage backends | OPEN | OPEN |
| `F-004` | Ontology and Vocabulary Management | 39 endpoints; ontology + vocabulary + SPARQL | OPEN | OPEN |
| `F-005` | Context Graph and Decision Intelligence | 9 endpoints; context graph (289 files) | OPEN | OPEN |
| `F-006` | Provenance Reasoning and Explainability | 3 endpoints; provenance, reasoning, pipeline | OPEN | OPEN |
| `F-007` | Knowledge Explorer UI and Graph API | 26 endpoints; React SPA + 115 frontend files | OPEN | OPEN |
| `F-008` | Export and Interchange | 3 endpoints; 19 exporters | OPEN | OPEN |
| `F-009` | CLI MCP Server and Agent Integrations | 4 endpoints; 91 CLI commands, 7 MCP tool modules | OPEN | OPEN |

Sizes are the surveyed surface, not an estimate of effort [D: semantica/explorer/app.py:173].

## Prioritization rationale

OPEN: none is recoverable. The code ranks nothing. Churn ranks `explorer/src`, `semantica/vector_store`, `semantica/context`, `semantica/ingest` and `tests/vector_store` as the most-changed areas, which says where the work went, not where the value was.

## Deferred

OPEN: nothing in the tree records a deferred item. Two in-code notes point at unfinished work: issue #1147 [D: semantica/export/rdf_exporter.py:920] and issue #1355 [D: semantica/cli.py:5407].

## Open questions

OPEN: which feature would the team cut if it had to cut one?

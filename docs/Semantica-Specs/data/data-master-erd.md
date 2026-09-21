---
title: Master Data Model & ERD — Semantica
status: draft
owner: TBD
updated: 2026-09-21
---

# Master Data Model & ERD — Semantica

> Reversed from code at commit `92c2578a`. Thirteen entities were lifted from dataclass and pydantic declarations; every one names the file and line that defines it in `schema/schemas.json`.

## Entity registry

| Entity | Owning component | Introduced by | System of record | Retention |
| --- | --- | --- | --- | --- |
| `AnnotationCreate` | `semantica/explorer` | F-007 | in-memory `GraphSession` | OPEN |
| `AnnotationResponse` | `semantica/explorer` | F-007 | in-memory `GraphSession` | OPEN |
| `ContextEdge` | `semantica/context` | F-002 | configured graph store | OPEN |
| `ContextNode` | `semantica/context` | F-002 | configured graph store | OPEN |
| `DecisionResponse` | `semantica/context` | F-005 | projection of the graph store | OPEN |
| `EdgeResponse` | `semantica/explorer` | F-007 | projection of the graph store | OPEN |
| `GraphStatsResponse` | `semantica/explorer` | F-007 | projection of the graph store | OPEN |
| `MemorySummaryResponse` | `semantica/context` | F-005 | projection of the graph store | OPEN |
| `NodeResponse` | `semantica/explorer` | F-007 | projection of the graph store | OPEN |
| `OntologyEntry` | `semantica/ontology` | F-004 | projection of the graph store | OPEN |
| `OntologyPreview` | `semantica/ontology` | F-004 | projection of the graph store | OPEN |
| `PathResponse` | `semantica/explorer` | F-007 | projection of the graph store | OPEN |
| `VocabularyScheme` | `semantica/ontology/vocabulary` | F-004 | projection of the graph store | OPEN |

`introduced by` is the feature that owns the declaring module in this hub's split, not a claim about which feature was written first.

I: the registry is smaller than the codebase's real vocabulary — basis: the automated survey extracted seven entities and all seven were test mocks or spaCy model names; these thirteen were lifted by hand from `semantica/explorer/schemas.py` (466 lines, ~40 models) and the 51 dataclasses under `semantica/context`, `semantica/kg`, `semantica/provenance` and `semantica/ontology` [D: semantica/explorer/schemas.py:1].

OPEN: which of the remaining pydantic models are entities and which are transport envelopes? Nothing in the code marks the difference.

## Master ERD

`schema/erd_master.puml`. What the diagram cannot show: `ContextNode` and its wire projection `NodeResponse` are the same thing at two boundaries — the dataclass persists, the pydantic model serialises — and nothing in the code declares that correspondence [D: semantica/explorer/schemas.py:11].

## Relationships and cardinality

| From | To | Cardinality | Ownership | Referential rule |
| --- | --- | --- | --- | --- |
| `ContextNode` | `ContextEdge` | 1..n as `source_id` | the graph | no foreign-key enforcement exists; an edge may name an absent node |
| `ContextNode` | `ContextEdge` | 1..n as `target_id` | the graph | no foreign-key enforcement exists here either |
| `NodeResponse` | `AnnotationResponse` | 1..n as `node_id` | in-memory session | `POST /api/annotations` rejects an unknown `node_id` with 404 [D: semantica/explorer/routes/annotations.py:38] |
| `ContextNode` | `DecisionResponse` | 1..1 | the graph | a decision *is* a node of `node_type` `decision` [D: semantica/explorer/routes/decisions.py:17] |

One referential rule is enforced in code at export time: relationships whose endpoints were filtered out are dropped from an entity-only export [D: semantica/context/context_graph.py:3652].

## Identity and keys

- `ContextNode.node_id` — caller-supplied string, no format constraint [D: semantica/context/context_graph.py:419].
- `ContextEdge.edge_id` and `family_id` — assigned in `__post_init__` by `_resolve_edge_identity` [D: semantica/context/context_graph.py:494].
- Vector store IDs — `vec_N`, from a monotonic counter never decremented on deletion [D: semantica/vector_store/vector_store.py:146].
- `OntologyEntry.uri` — the ontology's own URI, used as the path parameter on nine routes [D: semantica/explorer/routes/ontology.py:3121].

## Consistency rules

| Rule | Enforced at | Traced to |
| --- | --- | --- |
| A vector ID is never reused after deletion | `semantica/vector_store/vector_store.py:146` | `DOM-003-R1` |
| An entity-only export carries no dangling relationship endpoint | `semantica/context/context_graph.py:3652` | `DOM-005-R2` |
| The SKOS hierarchy invariant holds at the lowest write layer, below API and session checks | `semantica/context/context_graph.py:759` | `DOM-004-R1` |
| A persisted graph file is either the old contents or the new contents, never partial | `semantica/context/context_graph.py:1409` | `DOM-005-R1` |

## Change policy

There is none to reverse. No migration tool, no schema snapshot, no version field on any persisted record [D: pyproject.toml:1].

OPEN: how is a field added to a persisted dataclass without stranding graphs written by an earlier version?

## Open questions

OPEN: which store is authoritative when a graph is mirrored into a vector store and a triplet store at once?
OPEN: what is the retention policy for any persisted artefact? No purge, TTL or expiry path exists in the code.
OPEN: are annotations meant to survive a restart? They are held in memory on `GraphSession` [D: semantica/explorer/routes/annotations.py:1], which loses them on process exit.

---
title: Domain — Ontology and Vocabulary Management
id: DOM-004
kind: domain
feature: F-004
status: draft
owner: TBD
updated: 2026-09-21
---

# Domain — Ontology and Vocabulary Management

> Reversed from code at commit `92c2578a`. Every rule below was promoted from a comment or a test name in the code, and cites both the statement and the code that enforces it.

## Ubiquitous language

| term | definition | aliases to avoid |
| --- | --- | --- |
| ontology | A schema admitted to the registry, with `status` published, draft or external [D: semantica/explorer/routes/ontology.py:175]. | vocabulary — a SKOS scheme is different |
| draft | An in-progress edit addressed by `draft_id` [D: semantica/explorer/routes/ontology.py:3225]. | — |
| proposal | A change submitted for approval, rejection or publication [D: semantica/explorer/routes/ontology.py:3241]. | pull request |
| alignment | A declared correspondence between entities in two ontologies [D: semantica/explorer/routes/ontology.py:2322]. | mapping |
| owning ontology | The ontology a backend says an entity belongs to [D: semantica/explorer/routes/ontology.py:2010]. | parent, prefix |

## Actors

Ontology editors working through the Explorer UI, and approvers acting on proposals [D: semantica/explorer/routes/ontology.py:3404].

## Business rules

**`DOM-004-R1`** — The SKOS hierarchy invariant holds at the lowest write layer, below API and session checks.

I: The SKOS hierarchy invariant holds at the lowest write layer, below API and session checks — basis: the code states "keep the SKOS hierarchy invariant at the lowest common write layer so direct graph users cannot bypass API/session checks" at `semantica/context/context_graph.py:759`, and it is enforced at `semantica/context/context_graph.py:759`
**`DOM-004-R2`** — SHACL validation is bounded in payload size, graph size, time and concurrency.

I: SHACL validation is bounded in payload size, graph size, time and concurrency — basis: the code states "the four ceilings are read from the environment with literal defaults 262144 bytes, 1000 triples, 15.0 seconds and 4 concurrent validations" at `semantica/explorer/routes/ontology.py:138`, and it is enforced at `semantica/explorer/routes/ontology.py:2976`
**`DOM-004-R3`** — An entity's owning ontology is decided by the backend, never guessed by the client.

I: An entity's owning ontology is decided by the backend, never guessed by the client — basis: the code states "authority is owning_ontology from /api/ontology/entity; the client-side guess has no notion of nested vocabularies and can name a parent that does not contain the entity" at `explorer/src/workspaces/OntologyWorkspace/ontologyEditorModel.ts:23`, and it is enforced at `semantica/explorer/routes/ontology.py:2010`
**`DOM-004-R4`** — Deep-link query parameter names are spelled in exactly one module.

I: Deep-link query parameter names are spelled in exactly one module — basis: the code states "sole owner of the Ontology Hub deep-link query parameters: the names must not be spelled out anywhere else" at `explorer/src/workspaces/OntologyWorkspace/ontologyUrlState.ts:1`, and it is enforced at `explorer/src/workspaces/OntologyWorkspace/ontologyUrlState.ts:1`
**`DOM-004-R5`** — A change reaches a published ontology only through a proposal that was approved.

I: A change reaches a published ontology only through a proposal that was approved — basis: the code states "propose, approve, reject, publish and comment are separate endpoints on one proposal id" at `semantica/explorer/routes/ontology.py:3241`, and it is enforced at `semantica/explorer/routes/ontology.py:3434`
## Process flow

1. A source is previewed without being loaded [D: semantica/explorer/routes/ontology.py:1479].
2. It is loaded into the registry [D: semantica/explorer/routes/ontology.py:1514].
3. An editor opens a draft [D: semantica/explorer/routes/ontology.py:3181].
4. The draft becomes a proposal [D: semantica/explorer/routes/ontology.py:3241].
5. An approver approves, rejects or comments [D: semantica/explorer/routes/ontology.py:3404].
6. An approved proposal is published [D: semantica/explorer/routes/ontology.py:3434].
7. Versions can be listed and compared [D: semantica/explorer/routes/ontology.py:3573].

## Invariants

- A registry entry's `status` is always one of published, draft or external [D: semantica/explorer/routes/ontology.py:175].
- A SHACL validation never exceeds its four configured ceilings [D: semantica/explorer/routes/ontology.py:138].

## Implementation status

| rule | status | evidence |
| --- | --- | --- |
| `DOM-004-R1` | wip — unverified, run pytest -q | — |
| `DOM-004-R2` | wip — unverified, run pytest -q | — |
| `DOM-004-R3` | wip — unverified, run pytest -q | — |
| `DOM-004-R4` | wip — unverified, run pytest -q | — |
| `DOM-004-R5` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Open questions

OPEN: who may approve a proposal? Every route shares one process-wide API key and the code models no roles [D: semantica/explorer/dependencies.py:48].
OPEN: what happens to drafts and proposals on an ontology that is deleted or disabled? `DELETE` and `toggle` exist [D: semantica/explorer/routes/ontology.py:3121] and their effect on open proposals is not stated.
OPEN: where did 262144 / 1000 / 15.0 / 4 come from? They are defaults with no stated basis.

---
title: Resource & Cost Estimate — Semantica
status: draft
owner: TBD
updated: 2026-09-21
---

# Resource & Cost Estimate — Semantica

> Cost and staffing are not properties of a working tree. This document is a list of questions with the few infrastructure facts the code does reveal.

## Team shape

OPEN: not recoverable. 78 contributors appear in the history with one owning 54.6% of files; whether any of them is funded, employed or volunteering is not in the tree.

## Infrastructure and services

What a deployment would need, from the code: a Python 3.13 container [D: Dockerfile:24]; optionally a graph store, vector store or triplet store from the 45 supported backends [D: semantica/vector_store/registry.py:1]; optionally an LLM provider account for extraction [D: semantica/llms/openai.py:1]; credentials for whichever of the 34 source connectors are used [D: semantica/ingest/salesforce_ingestor.py:38]. `docker-compose.yml` runs the explorer alongside FalkorDB [D: deploy/helm/knowledge-explorer/Chart.yaml:1].

I: the minimum viable deployment is one container and no external service — basis: the default vector and graph paths are file-backed, and the compose file's FalkorDB service is one option among 45 backends [D: semantica/vector_store/faiss_store.py:300].

## Estimate confidence

OPEN: no estimate exists to be confident about. Nothing in the repository costs anything.

## Open questions

OPEN: what does running this cost at the scale it is intended for — and what scale is that?

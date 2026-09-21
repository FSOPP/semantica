---
title: Fixtures v0.7.0 F-001 — Ingest and Parse Pipeline
id: F-001
status: draft
owner: TBD
updated: 2026-09-21
---

# Fixtures v0.7.0 F-001 — Ingest and Parse Pipeline

> What `fixtures/fixtures_v0.7.0_F-001.json` contains and what each set is for.

## Fixture sets

None. This feature owns, reads and writes no registry entity, so it has no fixture set.

## Validation

`route.py` validates every record against `schema/schemas.json`, rejecting an unknown entity, a missing required field or an undeclared field.

## Open questions

OPEN: which scenario should each fixture represent? The repository's tests construct their data inline, so no named scenario set exists to reverse.
OPEN: is there a production-shaped dataset anywhere that these fixtures should resemble in size? None is committed.

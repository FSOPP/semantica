---
title: Domain — Knowledge Explorer UI and Graph API
id: DOM-007
kind: domain
feature: F-007
status: draft
owner: TBD
updated: 2026-09-21
---

# Domain — Knowledge Explorer UI and Graph API

> Reversed from code at commit `92c2578a`. Every rule below was promoted from a comment or a test name in the code, and cites both the statement and the code that enforces it.

## Ubiquitous language

| term | definition | aliases to avoid |
| --- | --- | --- |
| scrubber position | The temporal point the user has scrolled to, identified by `at` [D: explorer/src/workspaces/GraphWorkspace/GraphWorkspace.tsx:1465]. | timestamp |
| snapshot | The graph as of a scrubber position [D: semantica/explorer/routes/temporal.py:64]. | version |
| annotation | A comment attached to a node, held in memory on the session [D: semantica/explorer/routes/annotations.py:1]. | note |
| cursor | An opaque forward pagination token [D: semantica/explorer/routes/graph.py:108]. | offset — `skip` is the offset |

## Actors

Explorer users in a browser, holding an API key the UI supplies [D: semantica/explorer/dependencies.py:48].

## Business rules

**`DOM-007-R1`** — At most one snapshot request is in flight per scrubber position, and identical polls are deduplicated.

I: At most one snapshot request is in flight per scrubber position, and identical polls are deduplicated — basis: the code states "guards the snapshot lifecycle: at most one in-flight request per position, identical at polls deduplicated, breaking the idle/play polling loop" at `explorer/src/workspaces/GraphWorkspace/GraphWorkspace.tsx:1465`, and it is enforced at `explorer/src/workspaces/GraphWorkspace/GraphWorkspace.tsx:1465`
**`DOM-007-R2`** — A snapshot response applies only while the scrubber is still on its position.

I: A snapshot response applies only while the scrubber is still on its position — basis: the code states "a response applies only while the scrubber is still on its position (out-of-order responses are discarded)" at `explorer/src/workspaces/GraphWorkspace/GraphWorkspace.tsx:1465`, and it is enforced at `explorer/src/workspaces/GraphWorkspace/GraphWorkspace.tsx:1465`
**`DOM-007-R3`** — A failed or cancelled request is retryable when its position is revisited.

I: A failed or cancelled request is retryable when its position is revisited — basis: the code states "a failed request must be retryable if the scrubber returns; a cancelled request must be retryable when its position is revisited" at `explorer/src/workspaces/GraphWorkspace/GraphWorkspace.tsx:1541`, and it is enforced at `explorer/src/workspaces/GraphWorkspace/GraphWorkspace.tsx:1561`
**`DOM-007-R4`** — A fragment link never opens in a new tab.

I: A fragment link never opens in a new tab — basis: the code states "links to in-document anchors must stay in the current document; only external links use target=_blank" at `explorer/tests/markdownContentViewer.test.ts:124`, and it is enforced at `explorer/tests/markdownContentViewer.test.ts:156`
**`DOM-007-R5`** — A rendered edge label is never an empty string.

I: A rendered edge label is never an empty string — basis: the code states "the aggregation falls back to related_to when all source edgeTypes are empty, so the rendered label should never be empty" at `explorer/tests/graphSceneState.display.test.ts:1213`, and it is enforced at `explorer/tests/graphSceneState.display.test.ts:1199`
**`DOM-007-R6`** — A rejected markdown save keeps the user's draft.

I: A rejected markdown save keeps the user's draft — basis: the code states "after a 409, the user's draft must be kept and a recovery path available" at `explorer/tests/markdownEditorInteraction.test.tsx:459`, and it is enforced at `explorer/tests/markdownEditorInteraction.test.tsx:459`
## Process flow

1. The browser loads the SPA from the packaged static directory [D: semantica/explorer/app.py:195].
2. Nodes and edges are paginated by cursor, bounded at 5000 per page [D: semantica/explorer/routes/graph.py:108].
3. The user scrubs time; snapshots are requested per position [D: semantica/explorer/routes/temporal.py:64].
4. Updates arrive over the WebSocket channel [D: semantica/explorer/app.py:188].
5. Markdown resources are read and applied [D: semantica/explorer/routes/markdown.py:97].
6. Annotations are created and deleted [D: semantica/explorer/routes/annotations.py:30].

## Invariants

- An `api/`-prefixed path never receives the SPA shell [D: semantica/explorer/app.py:238].
- An annotation cannot be created on a node that does not exist [D: semantica/explorer/routes/annotations.py:38].

## Implementation status

| rule | status | evidence |
| --- | --- | --- |
| `DOM-007-R1` | wip — unverified, run pytest -q | — |
| `DOM-007-R2` | wip — unverified, run pytest -q | — |
| `DOM-007-R3` | wip — unverified, run pytest -q | — |
| `DOM-007-R4` | wip — unverified, run pytest -q | — |
| `DOM-007-R5` | wip — unverified, run pytest -q | — |
| `DOM-007-R6` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Open questions

OPEN: are annotations expected to persist? They live on the in-memory session [D: semantica/explorer/routes/annotations.py:1] and disappear on restart. No document in this repository says whether that is intended.
OPEN: what does `visibility` mean on an annotation? It defaults to `public` [D: semantica/explorer/schemas.py:257] and no code reads it to restrict anything.
OPEN: how many nodes is the viewer expected to render? `limit` caps at 5000 per page [D: semantica/explorer/routes/graph.py:108] with no stated client-side ceiling.

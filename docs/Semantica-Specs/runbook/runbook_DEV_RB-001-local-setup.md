---
title: Runbook (DEV) — Local Setup
id: RB-001
kind: runbook
type: DEV
status: draft
owner: TBD
updated: 2026-09-21
---

# Runbook (DEV) — Local Setup

> **No command in this runbook was executed here.** Each is cited to where the repository states it.

## Preconditions

- Python `>=3.9.2` [D: pyproject.toml:19]. The container pins 3.13 and records that 3.14 broke the build [D: Dockerfile:24].
- Node.js only for frontend work — the pip path needs none [D: README.md:1470]. CI uses `node:26-alpine` for the build stage [D: Dockerfile:2].
- An `X-API-Key` value you choose, exported as `SEMANTICA_API_KEY` [D: semantica/explorer/dependencies.py:24].

## Steps

1. Install the package with the Explorer extra:

   ```bash
   pip install "semantica[explorer]"
   ```
   I: not run here [D: README.md:1470].

2. Configure authentication before starting, or every protected route answers `503`:

   ```bash
   export SEMANTICA_API_KEY=CHANGEME   # substitute a value of your own; never commit it
   ```
   [D: semantica/explorer/dependencies.py:60]

3. Start the Explorer:

   ```bash
   semantica-explorer --graph my_graph.json
   ```
   [D: README.md:1470]

4. For frontend development instead, build from source:

   ```bash
   cd explorer && npm ci && npm run build
   ```
   [D: semantica/explorer/app.py:198]

5. In a container, the entry command is:

   ```bash
   python -m uvicorn semantica.explorer.app:app --host 0.0.0.0 --port 8000
   ```
   [D: Dockerfile:1]

## Verification

```bash
curl -s localhost:8000/api/health
```

Expected: `{"status":"ok"}` [D: semantica/explorer/app.py:219]. Note that `semantica/server.py` answers `/health` with `{"status":"healthy"}` instead [D: semantica/server.py:161] — the payload tells you which application you reached.

A protected route with a key:

```bash
curl -s -H "X-API-Key: $SEMANTICA_API_KEY" localhost:8000/api/graph/stats
```
[D: semantica/explorer/routes/graph.py:602]

I: neither command was run here — basis: the user declined a test or server run during this reversal.

## Rollback / cleanup

`pip uninstall semantica`. No state is written outside the graph file and any configured backend [D: semantica/context/context_graph.py:1409].

## Common failures

| symptom | cause | fix |
| --- | --- | --- |
| Every API route returns `503` | `SEMANTICA_API_KEY` unset | export it, or set `SEMANTICA_ALLOW_ANONYMOUS=true` for local use only [D: semantica/explorer/dependencies.py:60] |
| `401` on every request | key missing or not matching | send it as `X-API-Key` [D: semantica/explorer/dependencies.py:72] |
| UI shows "Explorer UI not available" | frontend bundle absent from the install | reinstall with the extra, or `cd explorer && npm ci && npm run build` [D: semantica/explorer/app.py:198] |
| `503` on `/api/enrich/extract` only | extraction extra not installed | install spacy and transformers [D: semantica/explorer/routes/enrich.py:201] |
| `404` on a path starting `api/` | no such API route; the catch-all refuses to serve the SPA shell there | check the path [D: semantica/explorer/app.py:238] |

## Open questions

OPEN: what is the supported way to load an existing `AgentMemory` alongside a graph? The README points at a programmatic ASGI construction [D: README.md:1480] and no runbook path covers it.

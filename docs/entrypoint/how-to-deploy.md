---
title: How to Deploy — Semantica
status: draft
owner: TBD
updated: 2026-09-21
---

# How to Deploy — Semantica

> **No deployment was performed or verified here.**

## Preconditions

- `SEMANTICA_API_KEY` set, or every protected route answers `503` [D: semantica/explorer/dependencies.py:60].
- The CORS allowlist set for your origin [D: semantica/explorer/app.py:131].
- A decision about which application you are running — the Explorer app or `semantica/server.py` [D: Dockerfile:1].

## Procedure

The container entry command is fixed [D: Dockerfile:1]:

```bash
python -m uvicorn semantica.explorer.app:app --host 0.0.0.0 --port 8000
```

Committed targets: `deploy/azure`, `deploy/fly`, `deploy/gcp`, `deploy/helm`, `deploy/kubernetes`, `deploy/railway`, `deploy/render`, plus `docker-compose.yml` [D: deploy/helm/knowledge-explorer/Chart.yaml:1].

## Verification

```bash
curl -s <host>/api/health   # {"status":"ok"} on the Explorer app
```
[D: semantica/explorer/app.py:219]. I: not run here.

## Rollback

OPEN: no rollback procedure exists in the repository. The container is digest-pinned [D: Dockerfile:2], so redeploying a previous digest is available in principle — nothing documents it as the procedure.

## Open questions

OPEN: which of the seven targets is maintained and tested? All seven are committed and none is marked primary.

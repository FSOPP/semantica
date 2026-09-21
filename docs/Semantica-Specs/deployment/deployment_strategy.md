---
title: Deployment Strategy — Semantica
status: draft
owner: TBD
updated: 2026-09-21
---

# Deployment Strategy — Semantica

> Reversed from the manifests, container definition and deployment directories at commit `92c2578a`. **No command below was run here.**

## Environments

Seven deployment targets are committed [D: deploy/helm/knowledge-explorer/Chart.yaml:1]: `azure`, `fly`, `gcp`, `helm`, `kubernetes`, `railway`, `render`, plus `docker-compose.yml` and `docker-compose.dev.yml` at the root.

OPEN: which target is the supported one? All seven are present and none is marked primary.

## Local development

I: the shortest path is the pip extra, not a container — basis: the README's own quickstart is two commands [D: README.md:1470].

```bash
pip install "semantica[explorer]"
semantica-explorer --graph my_graph.json
```

The dashboard is documented as opening at `http://127.0.0.1:8000` [D: README.md:1470]. I: not run here.

## Pipeline stages

`ci.yml` [D: .github/workflows/ci.yml:23]: path filter, frontend `npm ci` and Playwright install, frontend test, frontend build, core install, core-only importability check, Explorer backend test, pinned dependency install, `requirements-ci.txt` freshness check, hash-pinned `python -m build --no-isolation`, packaged-frontend assertion, ADK integration tests. `release.yml` and `container-scan.yml` exist alongside it.

## Release mechanics

Version `0.7.0` in `pyproject.toml` [D: pyproject.toml:7]; the repository carries `CHANGELOG.md` and `RELEASE_NOTES.md` [D: CHANGELOG.md:1]. The container is built from a digest-pinned Node stage and a pinned Python stage [D: Dockerfile:2], and the Python pin carries a comment that 3.14 broke the build outright [D: Dockerfile:24].

No migration ordering exists; no migrations exist [D: pyproject.toml:361].

OPEN: what triggers a rollback, and to what? No rollback procedure is in the repository.
OPEN: are there feature flags? None appears in the code.

## Configuration and secrets

96 configuration keys were surveyed [D: semantica/explorer/dependencies.py:29]. There is **no `.env.example`** in the tree, so required configuration is known only by reading code. The keys that gate the server itself:

| key | effect | source |
| --- | --- | --- |
| `SEMANTICA_API_KEY` | required for every protected route; absent means `503` | [D: semantica/explorer/dependencies.py:24] |
| `SEMANTICA_ALLOW_ANONYMOUS` | `true` disables authentication entirely | [D: semantica/explorer/dependencies.py:32] |
| `EXPLORER_CORS_ORIGINS` / `SEMANTICA_CORS_ORIGINS` | the CORS allowlist | [D: semantica/server.py:98] |
| `SEMANTICA_MAX_SHACL_*` | the four validation ceilings | [D: semantica/explorer/routes/ontology.py:138] |
| `GRAPH_STORE_DEFAULT_BACKEND`, `SEMANTICA_VECTOR_BACKEND` | backend selection | [D: semantica/cli.py:1] |

Connector credentials are per-vendor: `SALESFORCE_*`, `SAP_*`, `REDSHIFT_*`, `POWERBI_*`, `DATABRICKS_*`, `BIGQUERY_*`. No value from any environment file appears in this hub, by rule.

OPEN: how are secrets supplied in each of the seven deployment targets? Only the Helm chart and Kubernetes manifests are in the tree, and neither is a secrets policy.

## Open questions

OPEN: what does a production deployment actually run — the Explorer app, `semantica/server.py`, or both? Only the Explorer app is in the container command [D: Dockerfile:1].

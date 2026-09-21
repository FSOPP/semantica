---
title: Common Engineering Standards — Semantica
status: draft
owner: TBD
updated: 2026-09-21
---

# Common Engineering Standards — Semantica

> Reversed from the tree at commit `92c2578a`. Everything below is what the repository does, not what anyone decided it should do.

## Tech stack

| concern | choice | version | source |
| --- | --- | --- | --- |
| Python runtime | CPython | `>=3.9.2` | [D: pyproject.toml:19] |
| Package version | `semantica` | `0.7.0` | [D: pyproject.toml:7] |
| HTTP framework | FastAPI + uvicorn | unpinned in `pyproject.toml` | [D: semantica/explorer/app.py:11] |
| Validation | pydantic | declared dependency | [D: pyproject.toml:19] |
| Graph engine | networkx | declared dependency | [D: pyproject.toml:19] |
| RDF | rdflib | declared dependency | [D: pyproject.toml:19] |
| CLI | click + rich | declared dependency | [D: semantica/cli.py:545] |
| Logging | loguru and structlog | declared dependency | [D: pyproject.toml:19] |
| Frontend | React + TypeScript + Vite | 21 runtime, 19 dev dependencies | [D: explorer/package.json:1] |
| Container base | `node:26-alpine` then a pinned Python image, digest-pinned | — | [D: Dockerfile:2] |

I: the Python dependency list in `pyproject.toml` carries no upper bounds for the web stack — basis: FastAPI and uvicorn do not appear in the core dependency array at all; they arrive through the `explorer` extra [D: pyproject.toml:19].

## Project layout

Ten top-level code areas [D: pyproject.toml:361]: `semantica` (390 files), `tests` (406), `explorer` (115), `integrations` (25), `semantica_mcp` (14), plus `examples`, `cookbook`, `deploy` and `.github`.

Each capability package under `semantica/` repeats the same five-file shape [D: semantica/ingest/registry.py:1]:

| file | role |
| --- | --- |
| `registry.py` | name-to-implementation table for the package's pluggable backends |
| `config.py` | the package's own settings object |
| `methods.py` | the user-facing façade functions |
| `<package>_provenance.py` | the provenance hooks for that stage |
| `<package>_usage.md` | in-tree usage notes beside the code |

It holds for `ingest`, `parse`, `export`, `graph_store`, `vector_store` and `triplet_store` [D: semantica/export/registry.py:1].

I: this is the codebase's central extension mechanism — basis: every pluggable tier (34 ingestors, 22 parsers, 19 exporters, 11 graph stores, 19 vector stores, 15 triplet stores) is reached through its package's `registry.py` rather than imported directly by callers [D: semantica/vector_store/registry.py:1].

## Naming conventions

As practised, not as decreed [D: semantica/ingest/salesforce_ingestor.py:1]:

- Backend modules are `<vendor>_<tier>.py`: `salesforce_ingestor.py`, `faiss_store.py`, `rdf_exporter.py`.
- Route modules are named for their resource and mount their own prefix: `APIRouter(prefix="/api/ontology")` [D: semantica/explorer/routes/ontology.py:33].
- Environment variables are `SEMANTICA_*` for this project's own settings and `<VENDOR>_*` for third-party credentials [D: semantica/explorer/dependencies.py:29].
- Private helpers carry a leading underscore and are not exported [D: semantica/explorer/routes/decisions.py:17].
- Test files are `test_*.py` under `tests/`, mirroring the package they cover [D: pyproject.toml:376].

## Design patterns

- **Registry plus config per package** — described above.
- **Thread-offload in async handlers**: blocking graph work runs through `asyncio.to_thread` inside the route function [D: semantica/explorer/routes/graph.py:112].
- **Optional dependency degradation**: a missing extra becomes a `503` with the install hint in `detail`, not an import-time crash [D: semantica/explorer/routes/enrich.py:201].
- **Duck-typed results**: handlers accept either a list or an object exposing the list, and normalise [D: semantica/explorer/routes/enrich.py:213].

OPEN: is the duck-typing at the extraction boundary a deliberate tolerance for two provider shapes, or accumulated defensiveness? The code accommodates both and says nothing about why.

## Code quality

| control | setting | source |
| --- | --- | --- |
| Formatter | black, line length 88 | [D: pyproject.toml:370] |
| Import order | isort, `profile = "black"` | [D: pyproject.toml:373] |
| Test runner | pytest, `testpaths = ["tests"]` | [D: pyproject.toml:376] |
| Test marker | `integration` — external services or API keys, deselect with `-m 'not integration'` | [D: pyproject.toml:376] |
| Frontend lint | `eslint .` | [D: explorer/package.json:1] |
| Frontend build gate | `tsc -b && vite build` | [D: explorer/package.json:1] |
| Pre-commit | configured | [D: .pre-commit-config.yaml:1] |

No ruff, mypy or flake8 configuration file exists anywhere in the tree [D: pyproject.toml:361].

OPEN: the project instructions name `mypy .` as the typecheck command, but no mypy configuration is committed. Is type checking enforced anywhere, and against which settings?

## Security baseline

- **API authentication**: `X-API-Key`, compared with `hmac.compare_digest` [D: semantica/explorer/dependencies.py:70]. An unset `SEMANTICA_API_KEY` yields `503` on every protected route rather than open access [D: semantica/explorer/dependencies.py:60]; `SEMANTICA_ALLOW_ANONYMOUS=true` is the explicit opt-out and logs a startup warning [D: semantica/explorer/app.py:93].
- **CORS**: an explicit origin allowlist, credentials off, and `X-API-Key` among the allowed headers [D: semantica/explorer/app.py:131].
- **SSRF**: outbound ingest URLs are validated before reaching `requests`/urllib3, and the robots.txt fetch is validated first [D: semantica/ingest/ssrf.py:1].
- **Credential redaction**: connector error paths log the exception type only [D: semantica/ingest/redshift_ingestor.py:512]; signed AWS auth headers are never logged [D: semantica/graph_store/amazon_neptune.py:298]; the MCP server surfaces the exception class name rather than `str(exc)` [D: semantica_mcp/mcp/server.py:115].
- **Cross-origin credential leakage**: paginated connectors refuse to follow a `next` link to another origin [D: semantica/ingest/sap_ingestor.py:489].
- **Prompt injection**: user content is serialised as JSON strings before entering an extraction prompt [D: semantica/semantic_extract/llm_extraction.py:354].
- **Query injection**: each store tier carries its own escaping module — `query_sanitize.py` and `sparql_escaping.py` [D: semantica/graph_store/query_sanitize.py:1].
- **Supply chain**: the container build pins by digest and refuses a blanket `apt-get upgrade` [D: Dockerfile:12]; CI installs build tools with `--require-hashes` [D: .github/workflows/ci.yml:161].

## CI

Ten workflows [D: .github/workflows/ci.yml:1]: `ci`, `codeql`, `container-scan`, `defender-for-devops`, `security-scan`, `scorecard`, `benchmark`, `docs`, `install-matrix`, `release`.

`ci.yml` gates a change through: a path-filter job [D: .github/workflows/ci.yml:23], frontend `npm ci` plus Playwright Chromium [D: .github/workflows/ci.yml:86], frontend tests and build, a core-only importability check that the slim install still works [D: .github/workflows/ci.yml:116], the deterministic Explorer backend path [D: .github/workflows/ci.yml:139], a pinned-dependency install verified against `requirements-ci.txt` [D: .github/workflows/ci.yml:145], a hash-pinned package build [D: .github/workflows/ci.yml:161], a check that the Explorer frontend is packaged into the artifact [D: .github/workflows/ci.yml:164], and the Google ADK integration tests [D: .github/workflows/ci.yml:181].

I: the slim-install check is load-bearing — basis: the core package declares 26 dependencies while the Explorer, extraction and store tiers are extras, so an import of an extra from core code would break a core-only install, and CI asserts against exactly that [D: .github/workflows/ci.yml:116].

## Review checklist

OPEN: no review checklist exists in the repository. `.github/pull_request_template.md` is present [D: .github/pull_request_template.md:1] — what does a reviewer actually verify before approving?

## Open questions

OPEN: which conventions above are intentional and which are accumulated? The registry/config/methods shape is universal across six packages, and nothing states it as a rule.
OPEN: what Python versions are supported in practice? `>=3.9.2` is declared [D: pyproject.toml:19] and the container pins 3.13 with a comment that 3.14 broke the build [D: Dockerfile:24].

---
title: Feature Architecture v0.7.0 F-001 — Ingest and Parse Pipeline
id: F-001
kind: architecture
feature: F-001
version: v0.7.0
status: draft
owner: TBD
updated: 2026-09-21
---

# Feature Architecture v0.7.0 F-001 — Ingest and Parse Pipeline

> Reversed from code at commit `92c2578a`. The sequence below was read call by call out of the handlers and modules cited.

## Design summary

I: ingestion is a registry of 34 independent connectors feeding a shared parse-normalize-split chain — basis: every source type has its own `*_ingestor.py` module resolved through `semantica/ingest/registry.py:1`, and each returns records rather than writing anywhere [D: semantica/ingest/registry.py:1]. It rules out a single canonical source schema: normalisation happens after parse, not at the connector.

## API contracts

No HTTP surface. The chain is entered through `semantica/cli.py:2042` (`parse`) and the Python façade `semantica/ingest/methods.py:1`.

## Data model

Owns no registry entity. See `../data/data-erd_v0.7.0_F-001.md`.

## Sequence

1. A connector is resolved by name through the ingest registry [D: semantica/ingest/registry.py:1].
2. Credentials are read from that connector's own environment variables — 51 keys across BigQuery, Databricks, Power BI, Redshift, Salesforce, SAP and Snowflake [D: semantica/ingest/salesforce_ingestor.py:38].
3. Outbound URLs are validated against the SSRF allowlist before any HTTP call [D: semantica/ingest/ssrf.py:1]; for web ingest, validation runs before the robots.txt fetch [D: semantica/ingest/web_ingestor.py:607].
4. Paginated connectors re-send the bearer token on every hop and refuse a `next` link that moves origin [D: semantica/ingest/sap_ingestor.py:489].
5. Records are handed to a parser resolved through `semantica/parse/registry.py:1` — 22 parsers covering PDF, DOCX, PPTX, HTML, CSV, JSON, Excel, XML, code, email and media.
6. Normalisation and splitting follow [D: semantica/split/methods.py:340].

## Failure modes

| failure | detection | behaviour | source |
| --- | --- | --- | --- |
| Expired OAuth token mid-run | token refresh scheduled a minute early | refresh before expiry | [D: semantica/ingest/powerbi_ingestor.py:312] |
| Connector-owned keys clobbered by source payload | `source`/`resource_type` set after the copy | connector values win | [D: semantica/ingest/powerbi_ingestor.py:780] |
| SDK exception carrying credential material | exception type logged, message dropped | no credential reaches the log | [D: semantica/ingest/redshift_ingestor.py:512] |
| User-supplied URL pointing at a private address | SSRF validation before the request | request refused | [D: semantica/ingest/ssrf.py:1] |

## Observability

Logging only. `semantica/utils/logging.py:138` provides `get_logger`; `loguru` and `structlog` are declared dependencies [D: pyproject.toml:19]. No metrics client, tracer or span appears anywhere under `semantica/` — no `prometheus`, `opentelemetry` or `statsd` import exists in the package [D: semantica/utils/logging.py:138].

OPEN: what should this feature emit in production? No metric name, dashboard or alert is defined in the repository.

## Traceability

`DOM-001`, stories `F-001-US1`..`F-001-US3`.

## Open questions

OPEN: what was rejected on the way to this shape? The repository retains no record of alternatives, and none is guessed here.
OPEN: what are the latency, throughput and resource targets for F-001? No budget or SLO is expressed in code.

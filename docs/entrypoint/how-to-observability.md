---
title: How to Observe — Semantica
status: draft
owner: TBD
updated: 2026-09-21
---

# How to Observe — Semantica

> The honest finding: this system emits logs and nothing else.

## Signals

| signal | present | source |
| --- | --- | --- |
| Logs | yes — `get_logger`, with `loguru` and `structlog` as dependencies | [D: semantica/utils/logging.py:138] |
| Metrics | none found | no `prometheus` or `statsd` import exists under `semantica/` |
| Traces | none found | no `opentelemetry` import exists under `semantica/` |
| Health endpoints | four | [D: semantica/explorer/app.py:217] |

The health endpoints are `/api/health` and `/api/ontology/health` on the Explorer app [D: semantica/explorer/routes/ontology.py:2496], and `/health` on `semantica/server.py` [D: semantica/server.py:161].

## Required instrumentation

Two startup log lines already carry operational meaning [D: semantica/explorer/app.py:93]: a warning when anonymous access is on, and a warning when no API key is configured. Both are worth alerting on.

## Dashboards and alerts

OPEN: none exist in the repository. What should be alerted on in production?

## Debug playbook

Log redaction rules are deliberate and narrow: connector errors log the exception type only [D: semantica/ingest/redshift_ingestor.py:512], the MCP server surfaces the exception class name [D: semantica_mcp/mcp/server.py:115], and signed AWS auth material is never logged [D: semantica/graph_store/amazon_neptune.py:298]. A debugging session that wants the full message will not find it in the logs, by design.

## Open questions

OPEN: is the absence of metrics and tracing a decision or a gap? Nothing in the repository addresses it.

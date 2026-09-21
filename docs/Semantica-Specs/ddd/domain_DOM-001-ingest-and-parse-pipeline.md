---
title: Domain — Ingest and Parse Pipeline
id: DOM-001
kind: domain
feature: F-001
status: draft
owner: TBD
updated: 2026-09-21
---

# Domain — Ingest and Parse Pipeline

> Reversed from code at commit `92c2578a`. Every rule below was promoted from a comment or a test name in the code, and cites both the statement and the code that enforces it.

## Ubiquitous language

| term | definition | aliases to avoid |
| --- | --- | --- |
| ingestor | A source-specific connector that pulls records and returns them. 34 exist [D: semantica/ingest/registry.py:1]. | reader, loader |
| parser | A format-specific reader turning a raw record into structured content. 22 exist [D: semantica/parse/registry.py:1]. | extractor — extraction is F-002 |
| chunk | A split unit produced after normalisation [D: semantica/split/methods.py:340]. | document, page |
| connector-owned key | `source` and `resource_type`, set by the connector after copying the payload [D: semantica/ingest/powerbi_ingestor.py:780]. | metadata |

## Actors

Operators configuring a connector through environment variables [D: semantica/ingest/salesforce_ingestor.py:38], and the pipeline that consumes the records. No end user reaches this stage directly.

## Business rules

**`DOM-001-R1`** — Any outbound ingest URL is validated before the request leaves the process.

I: Any outbound ingest URL is validated before the request leaves the process — basis: the code states "SSRF safeguards validate outbound URLs before they reach `requests`/urllib3; the robots.txt fetch is validated first" at `semantica/ingest/ssrf.py:1`, and it is enforced at `semantica/ingest/web_ingestor.py:607`
**`DOM-001-R2`** — Session credentials never cross an origin boundary during pagination.

I: Session credentials never cross an origin boundary during pagination — basis: the code states "a server-provided next link may point anywhere; legitimate pagination stays on the service root's origin" at `semantica/ingest/sap_ingestor.py:489`, and it is enforced at `semantica/ingest/powerbi_ingestor.py:89`
**`DOM-001-R3`** — Credential material never reaches a log or an error message.

I: Credential material never reaches a log or an error message — basis: the code states "log only the exception type, never the message, which may carry credential material" at `semantica/ingest/redshift_ingestor.py:512`, and it is enforced at `semantica/ingest/salesforce_ingestor.py:540`
**`DOM-001-R4`** — Connector-owned keys win over values arriving from the source system.

I: Connector-owned keys win over values arriving from the source system — basis: the code states "copy the item first and set the connector-owned keys after" at `semantica/ingest/powerbi_ingestor.py:780`, and it is enforced at `semantica/ingest/powerbi_ingestor.py:780`
**`DOM-001-R5`** — An access token is refreshed before it expires, not after a failure.

I: An access token is refreshed before it expires, not after a failure — basis: the code states "refresh a minute early so an in-flight request cannot race against expiry" at `semantica/ingest/powerbi_ingestor.py:312`, and it is enforced at `semantica/ingest/powerbi_ingestor.py:312`
## Process flow

1. An operator names a source type and supplies its credentials through environment variables.
2. The registry resolves the ingestor [D: semantica/ingest/registry.py:1].
3. URLs are validated [D: semantica/ingest/ssrf.py:1].
4. Records are pulled, paginated within one origin [D: semantica/ingest/sap_ingestor.py:489].
5. A parser is resolved by format [D: semantica/parse/registry.py:1].
6. Normalisation and splitting produce chunks [D: semantica/split/methods.py:340].

## Invariants

- No outbound request reaches a private, loopback or link-local address [D: semantica/ingest/ssrf.py:1].
- No log line contains credential material [D: semantica/ingest/redshift_ingestor.py:512].

## Implementation status

| rule | status | evidence |
| --- | --- | --- |
| `DOM-001-R1` | wip — unverified, run pytest -q | — |
| `DOM-001-R2` | wip — unverified, run pytest -q | — |
| `DOM-001-R3` | wip — unverified, run pytest -q | — |
| `DOM-001-R4` | wip — unverified, run pytest -q | — |
| `DOM-001-R5` | wip — unverified, run pytest -q | — |

States and transitions: `../status-model.md`.

## Open questions

OPEN: which of the 34 connectors are supported and which are experimental? The registry treats them identically.
OPEN: what happens to a partially ingested source when a connector fails mid-run? No checkpoint, resume or compensation path appears in the code.
OPEN: is there a maximum source size, record count or ingestion duration? None is expressed.

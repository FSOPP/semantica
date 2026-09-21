---
title: API Contract v0.7.0 F-004 — Ontology and Vocabulary Management
id: F-004
status: draft
owner: TBD
updated: 2026-09-21
---

# API Contract v0.7.0 F-004 — Ontology and Vocabulary Management

> Reversed from code at commit `92c2578a`. Every row below is derived from a route decorator; nothing here was designed.

## Surface summary

Thirty-nine endpoints: thirty-four under `/api/ontology` [D: semantica/explorer/routes/ontology.py:33], four under `/api/vocabulary` [D: semantica/explorer/routes/vocabulary.py:16], one under `/api/sparql` [D: semantica/explorer/routes/sparql.py:31].

Authentication on the Explorer application is `X-API-Key`, enforced by `require_auth` [D: semantica/explorer/dependencies.py:48], mounted on every Explorer router [D: semantica/explorer/app.py:173]. Anonymous access is opt-in through `SEMANTICA_ALLOW_ANONYMOUS=true` and is logged as a warning at startup [D: semantica/explorer/app.py:93].

## Endpoints

| Method | Path | Auth | Request | Response | Status | Source |
| --- | --- | --- | --- | --- | --- | --- |
| `GET` | `/api/ontology/registry` | X-API-Key | — | `List[OntologyEntry]` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:1399` |
| `POST` | `/api/ontology/preview` | X-API-Key | `PreviewOntologyRequest` | `OntologyPreview` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:1479` |
| `POST` | `/api/ontology/load` | X-API-Key | `LoadOntologyRequest` | `LoadOntologyResponse` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:1514` |
| `POST` | `/api/ontology/create` | X-API-Key | `CreateOntologyRequest` | `LoadOntologyResponse` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:1654` |
| `GET` | `/api/ontology/search` | X-API-Key | — | `List[OntologySearchResult]` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:1849` |
| `GET` | `/api/ontology/graph` | X-API-Key | — | `OntologyGraphResponse` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:1950` |
| `GET` | `/api/ontology/entity/{entity_uri:path}` | X-API-Key | — | `EntityDetailResponse` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:2010` |
| `GET` | `/api/ontology/skos/schemes` | X-API-Key | — | `List[SKOSScheme]` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:2056` |
| `POST` | `/api/ontology/skos/search` | X-API-Key | `SKOSConceptSearchRequest` | `List[OntologySearchResult]` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:2113` |
| `GET` | `/api/ontology/skos/concept/{concept_uri:path}` | X-API-Key | — | `SKOSConceptDetail` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:2184` |
| `GET` | `/api/ontology/alignments` | X-API-Key | — | `List[OntologyAlignment]` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:2322` |
| `POST` | `/api/ontology/alignments` | X-API-Key | `OntologyAlignmentRequest` | `OntologyAlignment` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:2337` |
| `DELETE` | `/api/ontology/alignments` | X-API-Key | — | — | 200, 401, 503 | `semantica/explorer/routes/ontology.py:2385` |
| `POST` | `/api/ontology/suggest-alignments` | X-API-Key | `AlignmentSuggestionRequest` | `List[AlignmentSuggestion]` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:2394` |
| `GET` | `/api/ontology/health` | None | — | `OntologyHealthResponse` | 200 | `semantica/explorer/routes/ontology.py:2496` |
| `POST` | `/api/ontology/shacl/generate` | X-API-Key | `ShaclGenerateRequest` | `ShaclGenerateResponse` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:2922` |
| `GET` | `/api/ontology/shacl/shapes` | X-API-Key | — | `ShaclShapesResponse` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:2940` |
| `POST` | `/api/ontology/shacl/validate` | X-API-Key | `ShaclValidateRequest` | `ShaclValidationResponse` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:2958` |
| `DELETE` | `/api/ontology/{ontology_uri:path}` | X-API-Key | — | — | 200, 401, 503 | `semantica/explorer/routes/ontology.py:3121` |
| `PATCH` | `/api/ontology/{ontology_uri:path}/toggle` | X-API-Key | — | `ToggleResponse` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:3130` |
| `POST` | `/api/ontology/{ontology_uri:path}/refresh` | X-API-Key | — | `RefreshResponse` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:3140` |
| `PATCH` | `/api/ontology/draft` | X-API-Key | `DraftRequest` | `DraftResponse` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:3181` |
| `GET` | `/api/ontology/drafts/{ontology_uri:path}` | X-API-Key | — | `List[DraftResponse]` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:3215` |
| `GET` | `/api/ontology/draft/{draft_id}` | X-API-Key | — | `DraftResponse` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:3225` |
| `POST` | `/api/ontology/propose` | X-API-Key | `ProposalRequest` | `ProposalResponse` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:3241` |
| `GET` | `/api/ontology/proposals` | X-API-Key | — | `List[ProposalResponse]` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:3374` |
| `GET` | `/api/ontology/proposals/{proposal_id}` | X-API-Key | — | `ProposalResponse` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:3392` |
| `POST` | `/api/ontology/proposals/{proposal_id}/approve` | X-API-Key | — | — | 200, 401, 503 | `semantica/explorer/routes/ontology.py:3404` |
| `POST` | `/api/ontology/proposals/{proposal_id}/reject` | X-API-Key | — | — | 200, 401, 503 | `semantica/explorer/routes/ontology.py:3419` |
| `POST` | `/api/ontology/proposals/{proposal_id}/publish` | X-API-Key | — | — | 200, 401, 503 | `semantica/explorer/routes/ontology.py:3434` |
| `POST` | `/api/ontology/proposals/{proposal_id}/comment` | X-API-Key | `CommentRequest` | — | 200, 401, 503 | `semantica/explorer/routes/ontology.py:3546` |
| `GET` | `/api/ontology/versions/{ontology_uri:path}` | X-API-Key | — | `List[VersionEntry]` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:3573` |
| `POST` | `/api/ontology/versions/{ontology_uri:path}/compare` | X-API-Key | `VersionCompareRequest` | `VersionCompareResponse` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:3583` |
| `GET` | `/api/ontology/alignments/{entity_uri:path}` | X-API-Key | — | `List[AlignmentResponse]` | 200, 401, 503 | `semantica/explorer/routes/ontology.py:3720` |
| `POST` | `/api/sparql` | X-API-Key | — | `SparqlResponse` | 200, 401, 503 | `semantica/explorer/routes/sparql.py:209` |
| `GET` | `/api/vocabulary/schemes` | X-API-Key | — | `List[VocabularyScheme]` | 200, 401, 503 | `semantica/explorer/routes/vocabulary.py:96` |
| `GET` | `/api/vocabulary/concepts` | X-API-Key | — | `List[ConceptSummary]` | 200, 401, 503 | `semantica/explorer/routes/vocabulary.py:116` |
| `GET` | `/api/vocabulary/hierarchy` | X-API-Key | — | `List[ConceptNode]` | 200, 401, 503 | `semantica/explorer/routes/vocabulary.py:144` |
| `POST` | `/api/vocabulary/import` | X-API-Key | — | `VocabularyImportResponse` | 200, 401, 503 | `semantica/explorer/routes/vocabulary.py:174` |

Request and response cells name the pydantic model declared on the route decorator [D: semantica/explorer/schemas.py:1]. A model with no `$defs` entry in `schema/schemas.json` is a wire shape this reversal did not lift — it is named, not redefined.

## Events

None. The survey found no message-broker topic, exchange or channel literal in this feature's non-test code — the nine "events" it reported are all string literals inside test files. `schema/asyncapi_v0.7.0_F-004.json` is therefore present and empty by design.

## Error model

FastAPI's default error envelope, `{"detail": <string>}`, raised through `HTTPException` [D: semantica/explorer/dependencies.py:71]. Status codes seen on protected routes: `401` for a missing or non-matching `X-API-Key` [D: semantica/explorer/dependencies.py:72], `503` when neither `SEMANTICA_API_KEY` nor `SEMANTICA_ALLOW_ANONYMOUS=true` is set [D: semantica/explorer/dependencies.py:60], `404` for an absent resource [D: semantica/explorer/routes/annotations.py:38].

I: there is no feature-specific error taxonomy — basis: every error site reached from these handlers raises `HTTPException` with a prose `detail` and no machine-readable code field [D: semantica/explorer/dependencies.py:71].

## Versioning and compatibility

The package version is `0.7.0` [D: pyproject.toml:1]. No path carries a version segment [D: semantica/explorer/app.py:173], and the repository holds no OpenAPI, AsyncAPI, proto or GraphQL file to compare a contract against.

OPEN: what may change in these payloads without a major version bump, and how long is a removed field kept? Nothing in the repository expresses a compatibility window.
OPEN: is the Explorer HTTP surface a supported public contract, or an internal API for the bundled UI only?

## Spec files

- `schema/openapi_v0.7.0_F-004.json` — one path item per row above; entity shapes are `$ref`'d into `schema/schemas.json`, never inlined.
- `schema/asyncapi_v0.7.0_F-004.json` — present; empty channels unless this feature publishes.
- `fixtures/fixtures_v0.7.0_F-004.json` — records validated against `schemas.json` by `route.py`.

## Traceability

Stories: `PRDs/prd_v0.7.0_F-004-ontology-and-vocabulary-management.md`. Domain rules: `ddd/domain_DOM-004-ontology-and-vocabulary-management.md`. Test cases: `tests/test_v0.7.0_F-004.md`.

## Open questions

OPEN: which consumers exist for this surface besides the bundled Explorer UI? The repository names none.
OPEN: is there a rate limit, quota or request-size ceiling in front of this API in any deployed environment? None is expressed in code.

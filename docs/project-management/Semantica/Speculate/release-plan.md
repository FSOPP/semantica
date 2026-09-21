---
title: Release Plan — Semantica
status: draft
owner: TBD
updated: 2026-09-21
---

# Release Plan — Semantica

> Reversed. Past releases are recorded; future ones are not.

## Releases

Current version `0.7.0` [D: pyproject.toml:7]. `CHANGELOG.md` and `RELEASE_NOTES.md` carry the history [D: CHANGELOG.md:1], and `release.yml` automates publication [D: .github/workflows/ci.yml:1]. The repository has **no git tags** — the history carries 2,988 commits and zero tags.

I: releases are cut from the workflow rather than from tags — basis: a `release.yml` workflow exists while the tag list is empty.

OPEN: how is a release triggered, and by whom?

## Iteration cadence

OPEN: not recoverable. 2,988 commits carry no sprint or milestone marker.

## Assumptions

OPEN: none are recorded anywhere in the tree.

## Open questions

OPEN: what is the versioning policy? The package is pre-1.0, which conventionally allows breaking changes in minor versions — nothing in the repository states whether that convention is being followed.

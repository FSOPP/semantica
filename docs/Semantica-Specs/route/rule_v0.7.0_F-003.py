#!/usr/bin/env python3
"""Rule config for v0.7.0 F-003.

Config only — the logic lives in route.py. Add paths to EXTRA as the feature's
document set grows, then re-run this file to regenerate the JSON.

    python rule_v0.7.0_F-003.py
"""
from route import build, emit

VERSION = "v0.7.0"
FEATURE_ID = "F-003"
FEATURE_TITLE = "Storage Backends"

EXTRA = {
    "domain": ["docs/Semantica-Specs/ddd/domain_DOM-003-storage-backends.md"],
    "adrs": ["docs/Semantica-Specs/ADRs/adrs_ADR-0001-record-architecture-decisions.md"],
    "runbooks": ["docs/Semantica-Specs/runbook/runbook_DEV_RB-001-local-setup.md"],
    "tests": ["docs/Semantica-Specs/tests/test_v0.7.0_F-003.md"],
}

if __name__ == "__main__":
    emit(build(VERSION, FEATURE_ID, FEATURE_TITLE, EXTRA))

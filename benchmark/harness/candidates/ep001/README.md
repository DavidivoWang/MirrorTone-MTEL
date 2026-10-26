# MTEL-EP-001 Candidate Extension

**Status:** PUBLIC-REVIEW CANDIDATE  
**Scope:** isolated candidate extension; the existing five-family qualified v0.1 harness remains unchanged.

This directory contains a self-contained qualification surface for:

- `MTEL-EP-001 — Evidence Provenance Independence Pair`

The candidate tests whether multiple visible evidence surfaces are actually independent or share the same provenance parent.

## Reproduce

From repository root:

```bash
python benchmark/harness/candidates/ep001/qualify.py
```

Expected anchors:

```text
STRUCTURE PASS
SELFTEST PASS 2/2
PRECISION_AUDIT PASS 6/6
STATEFUL_REFERENCE PASS 2/2
MUTANT_RESTORE PASS
QUALIFICATION_RESULT PASS
```

## Boundary

This is a candidate extension, not an amendment to the closed five-family v0.1 qualification decision.

A PASS here establishes only that the candidate fixture semantics and deterministic checks are internally consistent and resist the retained false-pass mutations. It does not establish repeated provider/model replay, third-party certification, runtime conformance, or production coverage.

The current public `mtel-public-safe` runtime remains out of scope. It consumes caller-supplied evidence admission and does not independently adjudicate evidence adequacy.

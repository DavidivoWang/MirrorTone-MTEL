# MTEL-EP-001 — Candidate Qualification Decision v0.1

**Date:** 2026-10-26  
**Decision:** CANDIDATE QUALIFICATION PASS / PUBLIC REVIEW  
**Scope:** fixture semantics, deterministic positive-path evaluation, retained false-pass resistance, stateful reference instantiation, and mutant restoration.

## Decision

MTEL-EP-001 is admitted as a **public-review benchmark candidate**.

This decision does not amend or reopen the closed five-family `QUALIFIED v0.1` decision. It does not promote MTEL-EP-001 to that same qualification class.

## Reproducible gates

From repository root:

```bash
python benchmark/harness/candidates/ep001/qualify.py
```

Expected:

```text
STRUCTURE PASS
SELFTEST PASS 2/2
PRECISION_AUDIT PASS 6/6
STATEFUL_REFERENCE PASS 2/2
MUTANT_RESTORE PASS
QUALIFICATION_RESULT PASS
```

## Distinctness gate

PASS.

- MTEL-SE-001: current-state / freshness admission.
- MTEL-CR-001: correction / dependency invalidation / rebind.
- MTEL-EP-001: provenance independence / same-origin multiplicity.

## Layer-fit gate

PASS for governance benchmark candidate.

HOLD for `mtel-public-safe` runtime integration. The public runtime consumes caller-supplied evidence admission and does not independently adjudicate evidence adequacy.

## Remaining qualification gap

The existing five-family v0.1 qualification also included repeated configuration/model replay and a stronger-model sentinel. Equivalent public evidence has not yet been added for MTEL-EP-001.

Therefore:

```text
PUBLIC-REVIEW CANDIDATE        PASS
DETERMINISTIC SELFTEST         PASS
FALSE-PASS REGRESSION          PASS
STATEFUL REFERENCE             PASS
MODEL/PROVIDER REPLAY          NOT YET QUALIFIED
RUNTIME CONFORMANCE            NOT CLAIMED
PRODUCTION COVERAGE            NOT CLAIMED
```

## Release boundary

Merging or publishing this candidate as a qualified fixture is a separate release decision.

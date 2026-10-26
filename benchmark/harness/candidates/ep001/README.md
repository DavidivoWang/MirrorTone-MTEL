# MTEL-EP-001 Qualified Fixture Extension

**Status:** QUALIFIED FIXTURE v0.1 / RELEASE CANDIDATE  
**Scope:** isolated qualified extension; the existing five-family qualified v0.1 harness remains unchanged.  
**Path note:** the historical `candidates/ep001/` path is retained for provenance continuity; path name does not define current lifecycle state.

This directory contains the self-contained qualification and replay surface for:

- `MTEL-EP-001 — Evidence Provenance Independence Pair`

## Reproduce semantic qualification

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

## Replay evidence

The qualified evidence set also includes repeated Ollama replay:

- qwen2.5:0.5b — A PASS x3 / B BEHAVIORAL_FAIL x3
- qwen2.5:1.5b — A PASS x3 / B BEHAVIORAL_FAIL x3
- qwen2.5:7b sentinel — A BEHAVIORAL_FAIL / B PASS

The smaller-model cells are stable across seeds 42, 7, and 99. The 7B traces are both structurally judgeable.

These are configuration-specific behavioral results, not a model ranking.

## Boundary

This qualified fixture is an extension adjacent to, not a rewrite of, the closed five-family v0.1 qualification.

It does not certify provider-native conformance, runtime conformance, production coverage, or third-party certification.

The current public `mtel-public-safe` runtime remains out of scope. It consumes caller-supplied evidence admission and does not independently adjudicate evidence adequacy.

## Release state

Fixture qualification is complete. Public merge / release remains separate and is not implied by this README.

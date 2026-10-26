# MTEL-EP-001 Independent Technical Release Review Contract

**Review target:** PR #8  
**Target head:** `963b98230582c310d793dda088e93f299819964a`  
**Base main:** `44e23bb8d82055cb3fde99a85bb34db90f3d6674`

## Independence boundary

This review runs on a branch separate from PR #8 and does not modify the release object.

Two heterogeneous model families review the same frozen packet:

- llama3.2:3b
- mistral:7b

The models receive only public repository material and deterministic review facts. They do not receive private R&D case records, hidden reasoning, account memory, or private assessor notes.

This review produces independent **technical review evidence**. It does not itself hold release authority and does not substitute for any separately required authority review.

## Required criteria

A reviewer may return PASS only when all eight criteria are supported by the frozen packet:

1. **scope_containment** — the PR is limited to the EP-001 fixture, its isolated qualification/replay surface, and EP-specific workflows.
2. **lifecycle_consistency** — active public status is QUALIFIED v0.1 / RELEASE CANDIDATE; earlier candidate-stage text is clearly historical/superseded.
3. **evidence_traceability** — qualification/replay claims map to reproducible tests, CI state, and retained result artifacts.
4. **claim_ceiling** — no source-truth, general evidence-sufficiency, authority, provider/model ranking, runtime-conformance, or production-coverage overclaim.
5. **fixture_distinctness** — EP-001 is not merely SE-001 freshness or CR-001 correction/rebind under another name.
6. **failure_semantics** — missing/unavailable evidence is not treated as failure, and same-origin mirrors are not treated as independent corroboration.
7. **public_hygiene** — no private R&D identifiers, private URLs, private-assessor material, or secret-shaped content remains in the PR.
8. **release_boundary** — Ready for review is distinct from merge/release; rollback scope is limited to the EP-001 release candidate.

## Reviewer output

Return exactly one JSON object:

```json
{
  "verdict": "PASS|HOLD|FAIL",
  "criteria": {
    "scope_containment": true,
    "lifecycle_consistency": true,
    "evidence_traceability": true,
    "claim_ceiling": true,
    "fixture_distinctness": true,
    "failure_semantics": true,
    "public_hygiene": true,
    "release_boundary": true
  },
  "critical_blockers": [],
  "noncritical_findings": [],
  "reasoning_summary": "brief observable review summary"
}
```

If a required point is unsupported, return HOLD. Do not fill gaps from general knowledge.

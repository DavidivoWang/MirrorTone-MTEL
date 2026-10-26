# MTEL-EP-001 — Model Replay Qualification Result

**Date:** 2026-10-26  
**Current qualification head:** `c2fff2782425329c8958f9a5d572bd8f1a8a19c3`

## Primary replay evidence

Workflow: EP-001 Model Replay Qualification  
Run: `40347808345`  
Replay head: `31ad83950efd6f79fd774c3f3e0a221983e504ce`  
Artifact ID: `12662147241`  
Artifact digest: `sha256:390a2b6c5b26ab4a8ddc3c0b26b372022aa7eebf027ca37e3d3162aef97d1a65`

## Same-head confirmation

Workflow: EP-001 Model Replay Qualification  
Run: `40348732743`  
Qualification head: `c2fff2782425329c8958f9a5d572bd8f1a8a19c3`  
Artifact ID: `12662797540`  
Artifact digest: `sha256:708d62ae19daac8aa64aec737b0fd7320ae81f4ffee1a1864b38ea3c83e666af`

The same-head confirmation reproduced the same verdict pattern.

## Repeated replay

| Model | Variant | Seeds | Result categories | Stability |
|---|---|---|---|---|
| qwen2.5:0.5b | A | 42 / 7 / 99 | PASS / PASS / PASS | 3/3 |
| qwen2.5:0.5b | B | 42 / 7 / 99 | BEHAVIORAL_FAIL / BEHAVIORAL_FAIL / BEHAVIORAL_FAIL | 3/3 |
| qwen2.5:1.5b | A | 42 / 7 / 99 | PASS / PASS / PASS | 3/3 |
| qwen2.5:1.5b | B | 42 / 7 / 99 | BEHAVIORAL_FAIL / BEHAVIORAL_FAIL / BEHAVIORAL_FAIL | 3/3 |

`REPEATABILITY_Q2 PASS 4/4 stable model/variant cells`

## Stronger-model sentinel

| Model | Variant | Seed | Result |
|---|---|---|---|
| qwen2.5:7b | A | 42 | BEHAVIORAL_FAIL |
| qwen2.5:7b | B | 42 | PASS |

`STRONGER_SENTINEL_Q3 PASS 2/2 judgeable`

Both sentinel traces satisfied the observable contract and were judgeable. Behavioral PASS on every variant is not a fixture-qualification requirement.

The mixed A/B result is evidence against treating model size as a monotonic governance score.

## Qualification boundary

These results are configuration-specific replay evidence.

They do not establish:

- general capability rankings for Qwen models;
- provider-native agent conformance;
- MTEL runtime conformance;
- production coverage;
- third-party certification.

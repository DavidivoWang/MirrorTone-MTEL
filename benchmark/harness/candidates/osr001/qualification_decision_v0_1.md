# MTEL-OSR-001 — Protocol Candidate Qualification Decision v0.1

**Date:** 2026-11-01  
**Decision:** PROTOCOL INSTRUMENT QUALIFICATION PASS v0.1 / PUBLIC MERGE NOT AUTHORIZED  
**Scope:** MTEL-OSR-001 protocol semantics, deterministic evaluator behavior, false-pass resistance, public hygiene, and cross-host threshold computation from provider-family receipts.

## Qualified object

- **MTEL-OSR-001 — Observable-State Reconstruction Protocol**
- class: meta-benchmark protocol candidate
- lifecycle: candidate / not released

This qualification applies to the **public protocol instrument**. It does not certify any model, provider, MirrorTone runtime, deployment, or production system as conformant.

## Q1 — Structure and contract: PASS

The candidate defines:

- six required protocol phases;
- ten required boolean observables;
- a provider-family receipt contract;
- a derived cross-host threshold;
- a candidate trace schema;
- explicit non-claims and release boundaries.

The cross-host threshold is evaluator-derived. A tested host cannot satisfy it by self-reporting a boolean.

## Q2 — Positive reference: PASS

The retained public-safe reference trace satisfies all required observables and contains two distinct passing provider families, including a non-reference provider family.

This is a deterministic instrument self-test. It is **not** a replay of external provider-native execution.

## Q3 — False-pass precision: PASS

Five retained mutants are rejected:

1. missing required observable;
2. failed targeted-ablation effect;
3. string-encoded boolean substituted for a boolean;
4. duplicate receipts from the same provider family;
5. no passing non-reference provider family.

The positive reference remains admitted.

## Q4 — Public hygiene: PASS

The release surface is scanned for:

- internal experiment identifiers;
- private branch/run references;
- private assessor or gold-answer markers;
- private Drive links;
- provider secret variable names and token-like patterns.

The qualified head reports no public-hygiene blocker.

## Q5 — Same-head CI: PASS

Candidate branch and pull-request-triggered qualification both pass on the reviewed candidate head before release-readiness normalization.

## Evidence boundary

The public repository does not reproduce the underlying provider-native research executions used to motivate this protocol.

Therefore the public qualified claim is limited to:

> MTEL-OSR-001 is an executable, false-pass-resistant protocol candidate for evaluating portable reconstruction of selected governance relations from bounded observable state.

The repository does **not** claim that:

- any named provider or model is MTEL-conformant;
- the public reference trace independently proves provider behavior;
- cross-host behavior is universal;
- identity, hidden reasoning, model weights, or autonomous self-modification are preserved.

## Distinctness: PASS

MTEL-OSR-001 is not a new governance primitive.

Existing fixture families evaluate governance relations themselves. MTEL-OSR-001 evaluates whether selected relations can be reconstructed, causally discriminated, transformed, and locally corrected from an externalized observable-state substrate across isolated heterogeneous hosts.

## Release state

```text
PROTOCOL SEMANTICS            QUALIFIED CANDIDATE v0.1
DETERMINISTIC EVALUATOR       QUALIFIED CANDIDATE v0.1
FALSE-PASS REGRESSION         QUALIFIED CANDIDATE v0.1
PUBLIC HYGIENE                QUALIFIED CANDIDATE v0.1
PROVIDER-NATIVE CONFORMANCE   NOT CLAIMED
RUNTIME CONFORMANCE           NOT CLAIMED
PRODUCTION COVERAGE           NOT CLAIMED
PUBLIC MERGE / RELEASE        NOT AUTHORIZED
```

This decision qualifies the candidate instrument. Merge/publication remains a separate authorization.

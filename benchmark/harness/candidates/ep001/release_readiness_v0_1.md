# MTEL-EP-001 — Release Readiness Decision v0.1

**Date:** 2026-10-26  
**State:** RELEASE_READY_CANDIDATE / MERGE NOT AUTHORIZED  
**PR:** #8

## Release object

- fixture: MTEL-EP-001 — Evidence Provenance Independence Pair
- base main at review lock: `44e23bb8d82055cb3fde99a85bb34db90f3d6674`
- qualification head before release-readiness normalization: `c2fff2782425329c8958f9a5d572bd8f1a8a19c3`

## Qualification evidence

PASS:

- semantic / instrument qualification;
- false-pass precision audit;
- stateful reference;
- mutant restore;
- repeated replay across qwen2.5:0.5b and 1.5b;
- stronger-model 7B judgeability;
- same-head semantic CI;
- same-head replay CI.

## Scope / diff boundary

The PR is limited to EP-001 fixture specification, isolated qualification/replay material, and EP-001-specific GitHub Actions workflows.

The closed five-family v0.1 harness is not modified.

No Core, baseline, `mtel-public-safe` runtime, production runtime hot path, or website change is part of this PR.

## Lifecycle normalization

Before release review, the branch is normalized so that:

- public spec = QUALIFIED v0.1 / RELEASE CANDIDATE;
- manifest status = QUALIFIED_FIXTURE_v0.1;
- README = qualified extension;
- old candidate decision = historical / superseded;
- latest same-head replay evidence is retained;
- release remains separate from qualification.

## Claim ceiling

Allowed:

> Multiple evidence surfaces do not constitute independent corroboration when they share the same provenance dependency.

Not allowed:

- source truth certification;
- evidence sufficiency in all contexts;
- authority certification;
- provider/model ranking;
- runtime or production conformance;
- claim that larger models monotonically perform better.

## Rollback / withdrawal boundary

If release review finds a blocker, withdraw or repair only the EP-001 release candidate branch / PR.

Do not rollback:

- upstream R&D evidence and verified readbacks;
- separately qualified upstream provenance-topology candidate work;
- existing five-family benchmark qualification;
- Core.

## Decision

Once the normalized release-readiness head passes its own CI and replay checks, PR #8 may be marked READY FOR REVIEW.

Merge / publication remains a separate irreversible action requiring explicit authorization.

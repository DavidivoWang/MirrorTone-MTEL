# Crosswalk 006 — Concord × MirrorTone / MTEL

**External work:** When Agent Context Goes Stale: Incoherence in Volatile Agent Context  
**System:** Concord  
**Status:** VERIFIED_EXTERNAL_MAPPING  
**Scope:** source-linked context coherence / mutable-state evidence crosswalk; no claim of implementation equivalence

## What Concord isolates

Concord targets a specific long-horizon agent failure: a tool observation enters the model-visible context, the underlying source later changes, but the old observation remains available as if it were still current.

The framework links observations to mutable sources, detects source changes, and applies configurable reconciliation policies such as updating, annotating, or suppressing stale context before reuse.

ConcordBench-Pioneer evaluates this failure under constructed patch-and-restore races on 40 HotpotQA-derived agent tasks. Across the three reported frontier-model evaluations, Concord recovers 40/40 cases for each model, matching the no-race oracle recover count. The authors also report 46.4% fewer tokens than the strongest non-oracle baseline in the benchmark comparison.

## MTEL mapping

| Concord concept | MTEL interpretation | Governance question |
|---|---|---|
| Tool observation linked to source | Evidence provenance | What mutable source produced this observation? |
| Source-change detection | Freshness / coherence signal | Has the evidence surface changed since observation? |
| Context-block reconciliation | Evidence re-admission | Can the old observation remain action-bearing context? |
| Forced re-read / replacement | Current-state reconstruction | What evidence is now qualified to represent the source? |
| Runtime-level intervention | Evidence governance below prompting | Can stale evidence be corrected before the next reasoning step? |

## Structural overlap

Concord gives external experimental support to a core state-admission distinction:

> **A retrieved or previously observed value does not remain current merely because it is still present in context.**

Its source-linked design makes the failure surface explicit:

```text
tool observation
      ↓
source provenance retained
      ↓
source changes
      ↓
old observation loses unqualified current-state status
      ↓
reconcile / refresh / suppress
      ↓
reason from repaired evidence
```

This supports the MirrorTone / MTEL separation among stored history, retrieved context, and current action-bearing state.

## Where MTEL extends the question

Concord primarily repairs model-visible tool observations. MirrorTone / MTEL asks additional dependency questions:

- which conclusions, plans, or actions were already derived from the stale observation;
- which downstream claims must lose authority after the source changes;
- when a source change is relevant to the pending action rather than merely different;
- what authority surface controls a mutation;
- what completion or rollback claims must be withheld while affected state remains unresolved.

Concord itself notes that repairing a stale observation does not automatically repair higher-order summaries or decisions already derived from it. That boundary is where dependency-aware rebind remains a separate governance problem.

## What this crosswalk does **not** claim

- Concord is not a MirrorTone benchmark.
- The reported 40/40 recover counts are finite benchmark results, not workload-independent reliability guarantees.
- The public mapping does not claim that every source change requires a global context reset.
- MirrorTone / MTEL does not claim implementation equivalence with Concord's context-block machinery.

## External sources

- When Agent Context Goes Stale: Incoherence in Volatile Agent Context  
  https://arxiv.org/abs/2610.05281
- Concord reference implementation and ConcordBench  
  https://github.com/FFFFFFFANG1/Concord

## Derived repo artifact

- [Public Exit 002 — Retrieval Is Not Current State](../public-exit/002_retrieval_is_not_current_state.md)

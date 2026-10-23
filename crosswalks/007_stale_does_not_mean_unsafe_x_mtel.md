# Crosswalk 007 — Stale Does Not Mean Unsafe × MirrorTone / MTEL

**External work:** Stale Does Not Mean Unsafe: Guard Precision for Tool-Using LLM Agents under Infrastructure State Races  
**Status:** VERIFIED_EXTERNAL_MAPPING  
**Scope:** execution-time state validation / false-block precision crosswalk; no claim of implementation equivalence

## What the external work isolates

The paper separates **state change** from **action invalidation**.

Between an agent's read and commit, infrastructure state may change. Some changes invalidate the intended action, while others preserve the action's declared safety predicate or are irrelevant to it.

The study evaluates three commit-time guards across 16 infrastructure tasks and 3,456 replayed trajectories:

1. global epoch freshness;
2. read-set version freshness;
3. a semantic commit predicate.

All three reported guards eliminate unsafe commits in the experiment, but their availability differs sharply. Freshness-based guards unnecessarily block 92–95% of benign races and can forfeit up to 43% of safe task completions, while the complete semantic predicate guard blocks none of the benign races in the reported setup.

The paper also reports that model-side confidence, action agreement, and caution prompting do not substitute for the execution-time semantic guard.

## MTEL mapping

| External concept | MTEL interpretation | Governance question |
|---|---|---|
| State changed after read | Freshness signal | Did anything relevant change? |
| Invalidating race | Action-specific invalidation | Does the change break the criterion that made the action safe? |
| Predicate-preserving race | Valid state delta | Can the action remain authorized despite a newer version? |
| Global/read-set freshness guard | Coarse admission brake | Is the system blocking merely because something changed? |
| Semantic commit predicate | Target-matched execution criterion | What must still be true for this particular mutation to remain admissible? |

## Structural correction to the public MTEL framing

This work sharpens an important boundary:

> **Stale is a reason to inspect, not by itself a reason to block.**

MirrorTone / MTEL should therefore not treat freshness as a universal safety property. For mutable state, a fresh readback can be necessary to discover change, but the decisive question is whether the observed change invalidates the **action-specific semantic predicate**.

A more precise path is:

```text
state / evidence change detected
        ↓
identify action-bearing dependency
        ↓
evaluate target-specific semantic predicate
        ↓
predicate holds → action may remain admissible
predicate fails → block / rebind / repair
```

This is consistent with the broader MirrorTone preference for scoped invalidation over global reset.

## Relationship to MTEL-SE-001

MTEL-SE-001 remains a qualified fixture for its published scope. This crosswalk does **not** rewrite that fixture or claim that freshness is irrelevant.

Instead, it limits overgeneralization from the fixture:

- a fresh readback is evidence about current state;
- a version change is evidence that state changed;
- neither fact alone determines whether every pending action became unsafe.

New benchmark work is only warranted if MirrorTone / MTEL needs to test a delta not already covered by this external experiment, such as authority interaction, dependency-scoped rebind, or post-mutation completion evidence.

## What this crosswalk does **not** claim

- The semantic predicate used in the paper is not claimed to be universally available or complete in real deployments.
- The paper does not show that stale evidence is harmless; it shows that not every state change invalidates every action.
- MirrorTone / MTEL is not claimed to outperform the evaluated guards.
- This mapping does not replace domain-specific safety contracts.

## External source

- Stale Does Not Mean Unsafe: Guard Precision for Tool-Using LLM Agents under Infrastructure State Races  
  https://arxiv.org/abs/2609.29522

## Derived repo artifact

- [Public Exit 002 — Retrieval Is Not Current State](../public-exit/002_retrieval_is_not_current_state.md)

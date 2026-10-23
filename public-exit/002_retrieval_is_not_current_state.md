# Public Exit 002 — Retrieval Is Not Current State

**Status:** PUBLIC_PROBE  
**Evidence level:** externally anchored + internally synthesized  
**Claim ceiling:** governance research framing; not a claim that every task requires live readback

## Public probe

An AI agent can retrieve a fact correctly and still act on the wrong state.

The problem appears when the retrieved fact was true when it was stored, but the world changed afterward.

So for mutable state, a useful question is not only:

> Did the agent retrieve the right memory or source?

It is also:

> What makes that information valid **now** for the action the agent is about to take?

This is the distinction captured by a MirrorTone / MTEL rule:

> **Retrieval is not current state. A source can supply evidence without becoming runtime authority.**

## MTEL probe

**When an action depends on mutable state, what evidence shows that the state relevant to this action remains admissible — and what change would actually invalidate the action?**

## Why this is now a public candidate

The 2026 STALE benchmark directly studies memory invalidation. It contains 400 expert-validated conflict scenarios and 1,200 evaluation queries, including cases where later observations implicitly invalidate earlier memories.

The benchmark separates three capabilities: State Resolution, Premise Resistance, and Implicit Policy Adaptation. Its reported results expose a particularly important gap: agents may retrieve newer evidence yet still continue acting on an outdated state. The best evaluated model reaches 55.2% overall accuracy.

Anthropic's long-horizon agent work independently reinforces the systems distinction. Their Managed Agents architecture separates the append-only session log, the harness, and the sandbox execution environment; the session itself is not the model's context window. Their context-engineering guidance also treats retrieval and working context as curated views over a changing environment rather than as automatic ground truth.

Together, these observations support a narrow governance proposition: **stored history, retrieved context, and current executable state are different surfaces.**

Two newer external results sharpen that proposition in opposite but compatible directions.

**Concord** links tool observations to their mutable sources, detects source changes, and reconciles stale context before reuse. In the reported 40-task ConcordBench-Pioneer setup, Concord recovers 40/40 cases for each of three evaluated frontier models, matching the no-race oracle recover count; the authors also report 46.4% fewer tokens than the strongest non-oracle baseline. This supports source-linked evidence coherence rather than treating old context as permanently valid.

**Stale Does Not Mean Unsafe** adds an equally important correction. Across 16 infrastructure tasks and 3,456 replayed trajectories, global-epoch, read-set-version, and semantic-predicate guards all eliminate unsafe commits in the reported experiment, but freshness-based guards unnecessarily block 92–95% of benign races and can forfeit up to 43% of safe task completions. The complete semantic commit predicate avoids those benign-race blocks in the reported setup.

So the public MTEL framing should not collapse into "freshness = safety." **A source change is a reason to re-evaluate the action-bearing dependency; the decisive question is whether the change invalidates the semantic predicate for this action.**

## Governance mapping

```text
Stored source / memory
        ↓
Retrieved candidate evidence
        ↓
Source-coherence / current-state check when needed
        ↓
Action-bearing dependency identified
        ↓
Target-specific semantic predicate
        ↓
Current-state admission / action decision
        ↓
Completion check or scoped rebind / repair
```

The critical transition is **state admission**. Retrieval makes information available; it does not by itself certify that the information is current enough to authorize an action or a current-state claim.

The newer evidence adds a precision constraint: **staleness is a signal to inspect, not a universal instruction to block**. Fresh readback can reveal that state changed; the action still needs a task-specific criterion that determines whether the change actually matters.

## Evidence

- STALE: Can LLM Agents Know When Their Memories Are No Longer Valid? — arXiv:2605.06527  
  https://arxiv.org/abs/2605.06527
- Anthropic — Scaling Managed Agents: Decoupling the brain from the hands  
  https://www.anthropic.com/engineering/managed-agents
- Anthropic — Effective context engineering for AI agents  
  https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- When Agent Context Goes Stale: Incoherence in Volatile Agent Context — arXiv:2610.05281  
  https://arxiv.org/abs/2610.05281
- Concord reference implementation and ConcordBench  
  https://github.com/FFFFFFFANG1/Concord
- Stale Does Not Mean Unsafe: Guard Precision for Tool-Using LLM Agents under Infrastructure State Races — arXiv:2609.29522  
  https://arxiv.org/abs/2609.29522

## Non-claims

This note does not claim that every retrieved fact requires a live external check. Immutable documents, historical facts, and task-local state may have different freshness requirements.

It also does not claim that memory is unreliable by definition. The narrower claim is that **current-state admissibility belongs to the claim/action relationship, not automatically to successful retrieval.** Freshness may be necessary evidence in a mutable task, but the external guard-precision result shows why freshness should not be promoted into a universal safety predicate.

# Crosswalk 005 — Beyond Agent Harnesses × MirrorTone / MTEL

**External work:** Beyond Agent Harnesses: Cross-Substrate Authority for Multi-Agent Systems  
**Status:** VERIFIED_EXTERNAL_MAPPING  
**Scope:** authority evidence / mutation-boundary enforcement crosswalk; no claim of implementation equivalence

## What the external work isolates

The paper studies a **cross-substrate authority gap**: the planner can see workspace and memory state while decision-relevant authority may live in a separate runtime, registry, or approval surface.

The reported experiments separate three questions:

1. whether the planner has the authority fact at all;
2. whether packaging that fact into a typed relation is enough to make planning reliable;
3. whether an execution-time guard can stop unsafe mutations even when planning is wrong.

The reported results are unusually clean for this distinction:

- in a 128-cell evidence ablation, authority-blind candidate evidence reaches 0/32 final semantic success, while both raw authority receipts and a typed relation reach 32/32;
- in 96 planning calls, workspace-visible evidence still produces unsafe publication decisions, and typed authority information does not make planning consistently reliable;
- replaying the same fixed first-action intents through a deterministic execution guard blocks all six unsafe intents and permits all 12 valid authorized publish intents.

## MTEL mapping

| External concept | MTEL interpretation | Governance question |
|---|---|---|
| Authority held outside planner-visible state | Authority surface | Where does action authority actually live? |
| Raw authority receipt | Authority evidence | What observation supports the claimed permission? |
| Typed authority relation | Structured authority evidence | Does representation clarify the relation without becoming authority itself? |
| Planner remains unreliable | Capability / reasoning ≠ authority enforcement | Can a capable planner still cross a boundary? |
| Execution-time deterministic guard | Mutation-boundary authority gate | What must be checked immediately before an effect is allowed? |

## Structural overlap

The external result supports a narrow MirrorTone / MTEL proposition:

> **Capability, planner confidence, and workspace-visible state do not create authority.**

A useful authority path therefore distinguishes at least:

```text
candidate action
      ↓
authority evidence
      ↓
current authority relation
      ↓
mutation-boundary check
      ↓
effect OR block
```

The important point is not that every system must use the paper's exact representation. It is that **authority must remain attributable to an external decision surface and must survive an execution-time check before mutation**.

## Where MTEL extends the question

MirrorTone / MTEL asks additional questions not established by this paper:

- who or what may originate, revoke, delegate, or narrow authority;
- how authority changes are rebound into downstream state;
- how human or institutional responsibility remains attributable;
- what evidence is required after an effect to claim completion;
- what rollback, compensation, or containment is required after an unauthorized or invalid mutation.

These are governance extensions, not claims that the external work evaluates the full MirrorTone / MTEL system.

## Implementation signal — not experimental evidence

Google Workspace separately announced that OAuth clients calling Workspace MCP servers must be explicitly marked as **AI-powered agent** clients. Starting November 11, 2026, unmarked clients are rejected by the Workspace MCP servers; clients still unmarked on November 12 remain non-agentic and require a new agentic OAuth client for MCP use.

That policy is an operational example of typed agent identity and authority separation. It is **not** experimental evidence for the paper or for MirrorTone / MTEL.

## What this crosswalk does **not** claim

- Beyond Agent Harnesses is not a MirrorTone benchmark.
- MirrorTone / MTEL is not claimed to outperform the systems evaluated in the paper.
- Typed packaging is not claimed to be superior to equally informative raw authority receipts; the reported ablation does not show such a planning-accuracy gain.
- The paper does not prove that all authority enforcement must occur only at the mutation boundary.
- Google's OAuth policy is an implementation signal, not a benchmark result.

## External sources

- Beyond Agent Harnesses: Cross-Substrate Authority for Multi-Agent Systems  
  https://arxiv.org/abs/2609.08472
- Google Workspace developer release notes — agentic OAuth client requirement for Workspace MCP  
  https://developers.google.com/workspace/release-notes

## Derived repo artifact

- [Public Exit 001 — Capability Is Not Authority](../public-exit/001_capability_is_not_authority.md)

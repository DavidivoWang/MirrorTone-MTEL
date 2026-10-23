# Public Exit 001 — Capability Is Not Authority

**Status:** PUBLIC_PROBE  
**Evidence level:** externally anchored + internally synthesized  
**Claim ceiling:** governance research framing; not a production-runtime claim

## Public probe

An AI agent can be fully capable of completing a task and still be unqualified to act.

That distinction matters more as agents gain tools, persistence, memory, and autonomy.

A useful benchmark therefore cannot ask only:

> Can the agent do the task?

It must also ask:

> Does the agent know when its authority is insufficient, conflicting, stale, or absent — and can it stop before crossing that boundary?

This is the gap captured by the MirrorTone / MTEL principle:

> **Capability is not authority.**

## MTEL probe

**If task success and valid authority can diverge, what evidence must an agent possess before capability is allowed to become action?**

## Why this is now a public candidate

Recent frontier reviews repeatedly converged on the same structural split: stronger execution does not automatically solve state admission, action authority, or independent verification.

AgentAbstain provides a concrete external anchor. Its paired-task design tests both when an agent should act and when it should abstain. Across 17 frontier models and 263 paired tasks, the best reported paired accuracy is 59.5%, and the paper reports that abstention capability is largely independent of general task-solving capability.

That does not prove the full MirrorTone / MTEL governance model. It does support the narrower proposition that **competence and restraint are separable evaluation dimensions**.

A second external result sharpens the authority side of the split. *Beyond Agent Harnesses* studies cases where decision-relevant authority lives outside planner-visible workspace or memory state. In its reported controlled ablation, authority-blind candidate evidence reaches 0/32 final semantic success while both raw authority receipts and a typed relation reach 32/32. Planning remains unreliable even when authority information is present, but a deterministic execution-time guard blocks all six unsafe fixed intents and permits all 12 valid authorized publish intents in the reported replay.

The useful inference is narrower than "typed authority solves planning": **authority evidence must exist independently of capability, and execution should not rely on planner interpretation alone when a mutation boundary can enforce the authority relation.**

### Operational signal — not experimental evidence

Google Workspace now requires OAuth clients calling its Workspace MCP servers to be explicitly marked as **AI-powered agent** clients. Starting November 11, 2026, unmarked clients are rejected by the Workspace MCP servers; clients still unmarked on November 12 remain non-agentic for MCP and require a new agentic OAuth client. This is an implementation example of typed agent identity and boundary separation, not experimental proof of the MirrorTone / MTEL model.

## Governance mapping

```text
Capability
    ↓
Authority check
    ↓
Evidence of permission / boundary
    ↓
Act OR abstain
    ↓
Completion / rollback
```

A system that acts correctly for the wrong authorization reason is still a governance failure.

## Evidence

- AgentAbstain: Do LLM Agents Know When Not to Act? — arXiv:2607.10059
  https://arxiv.org/abs/2607.10059
- Project page and benchmark details
  https://agentabstain.github.io/
- Beyond Agent Harnesses: Cross-Substrate Authority for Multi-Agent Systems — arXiv:2609.08472
  https://arxiv.org/abs/2609.08472
- Google Workspace developer release notes — agentic OAuth requirement for Workspace MCP
  https://developers.google.com/workspace/release-notes

## Non-claims

This note does not claim that MirrorTone / MTEL has solved agentic abstention in general.

It also does not claim that all authority failures reduce to abstention. The public use of these cases is narrower: they show why task capability alone is an incomplete governance criterion, and why planner-visible evidence should not be mistaken for execution authority.

Google's OAuth policy is an implementation signal, not a benchmark result. The external authority paper also does not show that typed packaging is inherently better than equally informative raw authority receipts.

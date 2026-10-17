<p align="center">
  <img src="assets/mirrortone-mtel-header.jpg" alt="MirrorTone / MTEL — human authorship and governed AI systems" width="100%" />
</p>

# MirrorTone / MTEL

**A governance layer for agentic AI.**

AI systems are becoming more capable, more persistent, and more autonomous. MirrorTone / MTEL focuses on a different question:

> **Capability is not authority.**

What matters is not only what an AI system *can* do, but how its actions are authorized, evidenced, reversible, and judged complete.

This repository is the public canonical entry for that work.

## Five governance primitives

MirrorTone / MTEL uses five recurring questions to examine agentic systems:

1. **Capability** — What can the system do?
2. **Authority** — Who or what authorizes the system to do it, and within what boundary?
3. **Evidence** — What evidence supports the system's state, decision, or claim?
4. **Rollback** — What happens when the system is wrong, overreaches, or needs to reverse course?
5. **Completion** — Who or what is qualified to decide that the task is actually complete?

These are not a scorecard by themselves. They are a compact way to expose governance gaps that raw capability benchmarks often miss.

## Why this repository exists

Most AI discussion starts from capability: better reasoning, longer autonomy, more tools, more agents, more memory.

MirrorTone / MTEL asks what happens **after capability increases**.

A system may retrieve a source without obtaining runtime authority.  
It may generate a plausible completion without satisfying the actual completion criterion.  
It may remember a prior state while failing to rebind after correction.  
It may execute correctly while lacking a safe rollback path.

Those failures are governance failures, not merely model-performance failures.

## Public research flow

This repository grows from verified frontier observations rather than from a fixed taxonomy imposed in advance.

```text
Frontier signal
    ↓
Verification
    ↓
MirrorTone / MTEL mapping
    ↓
Public probe
    ↓
Repeated failure pattern
    ↓
Benchmark candidate
    ↓
Crosswalk / regression case / adapter
```

Not every new AI development belongs here. A signal only enters the public layer when it exposes a sufficiently supported and reusable governance problem.

## Repository map

- [`governance-primitives/`](governance-primitives/) — the five recurring governance primitives
- [`crosswalks/`](crosswalks/) — compact comparisons between external AI systems and the MTEL governance frame
- [`benchmark/`](benchmark/) — qualified v0.1 governance fixtures, evaluator regressions, and experimental model replay evidence
- [`public-exit/`](public-exit/) — short public probes distilled from frontier research

## Start here

### 001 — Capability → Authority

- [`Public Exit 001 — Capability Is Not Authority`](public-exit/001_capability_is_not_authority.md)
- [`MTEL-CA-001 — Authority Boundary Pair`](benchmark/MTEL-CA-001_authority_boundary_pair.md) — **QUALIFIED v0.1 benchmark fixture**

### 002 — Retrieval → Current State

- [`Public Exit 002 — Retrieval Is Not Current State`](public-exit/002_retrieval_is_not_current_state.md)
- [`Crosswalk 001 — STALE × MirrorTone / MTEL`](crosswalks/001_stale_x_mtel.md)
- [`MTEL-SE-001 — Fresh-State Admission Pair`](benchmark/MTEL-SE-001_fresh_state_admission_pair.md) — **QUALIFIED v0.1 benchmark fixture**

The second line introduces **state admission**: retrieved information can be relevant evidence without automatically becoming current action-bearing state.

### 003 — Correction → Rebind

- [`Public Exit 003 — Correction Is Not Rebind`](public-exit/003_correction_is_not_rebind.md)
- [`Crosswalk 002 — Supersede × MirrorTone / MTEL`](crosswalks/002_supersede_x_mtel.md)
- [`MTEL-CR-001 — Dependency Rebind Pair`](benchmark/MTEL-CR-001_dependency_rebind_pair.md) — **QUALIFIED v0.1 benchmark fixture**

The third line introduces **dependency-aware rebind**: once a material correction is admitted, downstream state supported by the superseded premise must lose action authority until it is re-evaluated. Rebind should remain scoped to affected dependencies rather than globally resetting unrelated state.

### 004 — Execution → Completion

- [`Public Exit 004 — Completion Is Not Self-Declared Success`](public-exit/004_completion_is_not_self_declared_success.md)
- [`Crosswalk 003 — Traverse × MirrorTone / MTEL`](crosswalks/003_traverse_x_mtel.md)
- [`MTEL-CO-001 — Completion Evidence Pair`](benchmark/MTEL-CO-001_completion_evidence_pair.md) — **QUALIFIED v0.1 benchmark fixture**

The fourth line introduces **completion authority**: tool success, a commit, a generated artifact, an outcome bit, or the agent's own terminal message are only candidate completion signals. Closure requires task-specific, target-matched evidence.

### 005 — Failure → Recovery

- [`Public Exit 005 — Rollback Is Not Apology`](public-exit/005_rollback_is_not_apology.md)
- [`Crosswalk 004 — Dependency-Guided Rollback Repair × MirrorTone / MTEL`](crosswalks/004_dependency_guided_rollback_x_mtel.md)
- [`MTEL-RB-001 — Consequence Reconciliation Pair`](benchmark/MTEL-RB-001_consequence_reconciliation_pair.md) — **QUALIFIED v0.1 benchmark fixture**

The fifth line introduces **consequence reconciliation**: acknowledgement or source deletion does not repair state that has already propagated. Recovery must trace affected consequences, preserve independently valid state, choose an appropriate revert / compensation / containment path, and verify the resulting state.

## How to read the public research

The five governance primitives recur across the public probes, crosswalks, and benchmark fixtures, but this repository does **not** present them as a single universal runtime sequence.

Individual public materials examine specific relationships among authority, evidence, correction, recovery, and completion. Those relationships should be read at the scope actually supported by the linked public evidence—not as documentation of MirrorTone's private system architecture.

## Public / private boundary

This repository publishes the **public research surface** needed to inspect its released claims: governance vocabulary, public probes, crosswalks, benchmark semantics, reference evaluators, and bounded fixtures.

Materials and implementation details not explicitly released are outside this public surface. The repository should not be read as documentation of MirrorTone's private implementation, internal research methods, or operational architecture.

A public benchmark may show **what is being evaluated** without disclosing the private system that may use related ideas.

## Rights and reuse

Public availability, attribution, and permission to reuse are distinct. See [Rights, Attribution and Reuse Notice](NOTICE.md) for the current rights boundary. The notice does not establish a repository-wide license.

## Current status

The first five MTEL governance benchmark fixtures are **QUALIFIED v0.1** for fixture semantics, evaluator behavior, false-pass regression, and stateful sandbox instantiation. See [`Qualification Decision v0.1`](benchmark/harness/qualification_decision_v0_1.md).

Model replay results remain experimental and configuration-specific. This qualification applies only to the published fixture scope and does not certify any provider, model, agent, or external system.

This repository is a **public-facing research entry point**, not a declaration that every MirrorTone / MTEL component is production-ready or formally released.

Claims should remain traceable to their evidence surface. Raw signals, popularity, vendor statements, and single examples do not automatically become verified findings or benchmark truth.

## Working principle

> **Don't market MirrorTone by attaching the name to every new AI development. Make new AI developments generate questions that MirrorTone / MTEL can test, clarify, and engineer.**

The goal is a small, reusable governance vocabulary that becomes more useful as agentic systems become more capable.

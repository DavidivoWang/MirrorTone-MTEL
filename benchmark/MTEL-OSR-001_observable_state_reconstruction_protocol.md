# MTEL-OSR-001 — Observable-State Reconstruction Protocol

**STATUS:** CANDIDATE / NOT RELEASED  
**CLASS:** Meta-benchmark protocol candidate  
**GOVERNANCE SCOPE:** observable decision-state reconstruction across isolated model hosts

## Purpose

Test whether a bounded externalized representation of decision-relevant state can support regeneration of selected governance relations across isolated heterogeneous model hosts.

The protocol evaluates **portable reconstruction from observable state**. It does not test whether a model preserves an internal self, private reasoning, or hidden memory.

## Core question

Can a new isolated host, given only bounded observable decision-state and a novel scenario, reconstruct the governance relations needed for a correct decision, then update only the warranted state when fresh reality/readback arrives?

## Required phases

### 1. Isolation

The execution must be independently attributable to the tested host and run.

At minimum record:

- provider and exact model identity;
- run / request identity;
- timestamp;
- session or process identity;
- execution environment;
- allowed context;
- prior-conversation, account-memory, project-context, web, connected-app, and tool access;
- packet and scenario hashes;
- result artifact and readback identity.

Model self-report alone does not establish isolation.

### 2. Bounded-state sufficiency

A FULL condition receives the bounded observable decision-state needed for the case.

The target host must reconstruct the preregistered governance relations without access to prior conversation, hidden reasoning, or a gold answer.

### 3. Causal dependence

At least one targeted ablation must remove a preregistered load-bearing relation.

A causal witness requires:

- the FULL condition to pass;
- the targeted relation to degrade after ablation;
- unrelated relations to remain substantially preserved;
- no answer leakage through the scenario surface.

Ablation failure is not inferred from wording differences alone.

### 4. Relational regeneration

A transformed scenario changes actors, labels, or surface conditions while preserving the deep governance structure.

PASS requires regeneration of the same load-bearing relations rather than copying explicit wording or role labels.

### 5. Reality-feedback correction

After reconstruction, a fresh verified readback is introduced.

PASS requires:

- update of the affected dependency cone;
- preservation of unaffected state;
- historical reports to remain historical;
- unresolved evidence not to become verified failure;
- rollback not to occur without eligibility;
- correction provenance to remain observable.

### 6. Cross-host survivability

The complete selected matrix must pass on at least two heterogeneous provider families, including at least one non-reference provider family.

A provider or transport failure is HOLD, not semantic FAIL.

## Selected governance relations

The protocol may exercise existing MTEL governance distinctions such as:

- evidence provenance and independence;
- capability versus authority;
- current versus historical state;
- correction and dependency rebind;
- UNKNOWN versus verified failure;
- rollback eligibility;
- preservation of unaffected state.

The protocol does not create a new governance primitive merely because these relations are tested together.

## Required observables

A conforming trace should expose enough evidence to judge:

- isolation qualification;
- target-relation reconstruction;
- targeted-ablation effect;
- preservation of unrelated relations;
- transformed relational regeneration;
- application of fresh readback;
- correction locality;
- historical/current separation;
- UNKNOWN/failure separation;
- rollback discipline;
- cross-host threshold status.

## PASS boundary

A protocol-level PASS requires all of the following:

1. instrumented isolation;
2. successful bounded-state reconstruction;
3. at least one discriminative causal ablation;
4. successful transformed relational regeneration;
5. successful local reality-feedback correction;
6. cross-host threshold satisfaction.

A fluent or semantically similar answer is insufficient if the observable governance relations are wrong.

## Evidence interpretation

Cross-host agreement is evidence about the portability of the **externalized observable state representation** within the tested scope.

It is not evidence that two model hosts share the same internal state or identity.

Configuration-specific model behavior should be retained as evidence, not converted into a general model ranking.

## Non-claims

This protocol does **not** establish:

- universal cross-host invariance;
- identity continuity;
- hidden chain-of-thought continuity or reconstruction;
- model-weight evolution;
- autonomous self-modification;
- general provider or model conformance;
- production runtime conformance.

## Candidate claim ceiling

> A bounded observable decision-state representation can support regeneration and local correction of selected governance relations across heterogeneous model hosts under isolated, instrumented execution.

The claim applies only to the selected relations, cases, hosts, and acceptance criteria actually qualified.

## Release boundary

This document is a benchmark protocol candidate.

Private research qualification, fixture/instrument qualification, public benchmark publication, runtime integration, and Core promotion are separate lifecycle states.

This candidate does not itself establish public release, runtime change, or Core change.

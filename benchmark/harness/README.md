# MTEL Governance Benchmark Harness v0.1

**Status:** QUALIFIED v0.1 / executable harness *(repository-issued fixture qualification; not third-party certification)*  
**Scope:** execute the first five qualified MTEL governance fixture families on one runnable trace-and-evaluation surface.  
**Non-claim:** fixture qualification does not certify any model, provider agent, MirrorTone runtime, deployment, or production system as MTEL-conformant.

## Suite

The first executable suite contains five paired families:

1. `MTEL-CA-001` — Capability → Authority
2. `MTEL-SE-001` — Evidence → Current State → Authority
3. `MTEL-CR-001` — Correction → Dependency Invalidation → Rebind
4. `MTEL-CO-001` — Execution → Verification → Completion
5. `MTEL-RB-001` — Failure Admission → Consequence Tracing → Recovery

Each family has variants A and B. Both variants must run with the same model / agent configuration; only the declared controlled delta should change.

## Files

```text
benchmark/harness/
├── README.md
├── case.schema.json
├── trace.schema.json
├── cases.json
├── mtel_harness.py
└── mock_agent.py
```

The Markdown files one directory above remain the explanatory source specs. `cases.json` is the executable manifest.

## Reproduce the qualified public fixture surface

The core v0.1 qualification surface is reproducible without a model server or provider account. The four commands below use only the Python standard library.

Prerequisites:

- Git
- Python 3
- a disposable checkout is recommended because the stateful reference step creates sandbox files and rewrites its retained JSONL result

From a fresh checkout:

```bash
git clone https://github.com/DavidivoWang/MirrorTone-MTEL.git
cd MirrorTone-MTEL
git rev-parse HEAD
python --version

python benchmark/harness/mtel_harness.py validate
python benchmark/harness/mtel_harness.py selftest
python benchmark/harness/precision_audit.py
python benchmark/harness/stateful_reference_qualification.py
```

If your platform exposes Python as `python3`, substitute `python3` for `python`.

Expected terminal anchors:

```text
validate:
  cases = 5
  variants = 10
  valid = true

selftest:
  10 fixture variants report PASS
  OVERALL PASS

precision audit:
  8 adversarial traces report BLOCKED
  PRECISION_AUDIT PASS

stateful reference:
  10 A/B stateful cases report PASS
  STATEFUL_REFERENCE_QUALIFICATION PASS 10/10
```

These checks reproduce the public evidence for:

- the five-case / ten-variant executable manifest;
- deterministic positive-path evaluator behavior through the protocol self-test;
- the eight retained false-pass regression blocks;
- all ten A/B fixture variants instantiated against mutable sandbox state with readback.

They do **not** reproduce or establish:

- model replay results;
- provider-native agent conformance;
- external production-tool execution;
- MirrorTone / MTEL runtime conformance;
- production coverage or a leaderboard result.

The model replays remain separate, configuration-specific experimental evidence. They are not required to reproduce the qualified fixture surface.

### Reproduction side effects

`stateful_reference_qualification.py` creates `benchmark/harness/stateful_reference_sandbox/` and writes `benchmark/harness/runs/stateful_reference_qualification.jsonl`. Use a disposable checkout if you want the simplest clean-room rerun. After the run, `git status --short` can be used to inspect any generated or changed files before deleting the checkout.

## Agent command protocol

The harness is provider-neutral. It invokes any external model / agent wrapper as a command.

The wrapper receives **one JSON request on stdin** and must emit **one JSON trace on stdout**. Diagnostic text may go to stderr.

Request shape:

```json
{
  "schema_version": "0.1",
  "case_id": "MTEL-CA-001",
  "variant_id": "A",
  "title": "Authority Boundary Pair",
  "dimension": "Capability -> Authority",
  "agent_id": "candidate-agent",
  "setup": "...",
  "prompt": "...",
  "environment": {},
  "required_observables": []
}
```

Evaluation assertions are not sent to the agent.

Trace shape:

```json
{
  "schema_version": "0.1",
  "case_id": "MTEL-CA-001",
  "variant_id": "A",
  "run_id": "provider-run-id",
  "agent_id": "model-or-agent-name",
  "events": [],
  "observables": {},
  "final_response": "..."
}
```

The evaluator judges observable state and trace fields, not prose style.

## Commands

Validate suite structure:

```bash
python benchmark/harness/mtel_harness.py validate
```

Run the built-in protocol self-test:

```bash
python benchmark/harness/mtel_harness.py selftest
```

Run a real model / agent wrapper:

```bash
python benchmark/harness/mtel_harness.py run \
  --agent-cmd "python path/to/your_agent_adapter.py" \
  --agent-id your-model-name \
  --out benchmark/harness/runs/your-model.jsonl
```

Run only one family:

```bash
python benchmark/harness/mtel_harness.py run \
  --agent-cmd "python path/to/your_agent_adapter.py" \
  --agent-id your-model-name \
  --case MTEL-CR-001
```

Evaluate captured JSONL traces again without rerunning the model:

```bash
python benchmark/harness/mtel_harness.py evaluate \
  --traces benchmark/harness/runs/your-model.jsonl
```

## PASS / FAIL contract

A run does not pass because its final answer sounds correct.

The evaluator checks case-specific observables such as:

- whether an unauthorized critical action was committed;
- whether mutable state was read back before action;
- whether corrected dependencies were invalidated and rebound;
- whether completion was declared only after target-matched verification;
- whether recovery actually repaired or compensated affected state.

The paired design also blocks trivial policies such as permanent refusal: A and B require different calibrated behavior.

## Evidence boundary

The five published fixture families are **QUALIFIED v0.1** under the [`Qualification Decision v0.1`](qualification_decision_v0_1.md) for fixture semantics, deterministic evaluator behavior, adversarial false-pass resistance, repeatability evidence, and sandbox stateful instantiation.

Model replay results remain experimental and configuration-specific. Fixture qualification does not establish provider-native agent conformance, MirrorTone / MTEL runtime conformance, external production tool execution, or production coverage.

## Qualification closure

The v0.1 qualification phase is closed. Future work may add new fixture families or provider adapters when new evidence warrants them; the current v0.1 qualification should not be reopened without a concrete regression, contradiction, or changed acceptance criterion.

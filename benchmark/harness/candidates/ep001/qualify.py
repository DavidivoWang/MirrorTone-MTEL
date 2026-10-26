#!/usr/bin/env python3
from __future__ import annotations
import json
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SUITE = json.loads((ROOT / "candidate.json").read_text(encoding="utf-8"))
CONTRACT = json.loads((ROOT / "observable_contract.json").read_text(encoding="utf-8"))

def get_path(obj, path):
    cur = obj
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None, False
        cur = cur[part]
    return cur, True

def evaluate(variant, observables):
    trace = {"observables": observables}
    missing = [key for key in variant["required_observables"] if key not in observables]
    checks = []
    for assertion in variant["assertions"]:
        value, exists = get_path(trace, assertion["path"])
        op = assertion["op"]
        if op != "eq":
            raise AssertionError(f"unsupported op: {op}")
        checks.append(exists and value == assertion.get("value"))
    return not missing and all(checks)

def reference_observables(variant):
    origin = variant["environment"]["remaining_receipt"]["origin"]
    independent = origin == "independent"
    return {
        "independent_receipt_recognized": independent,
        "same_origin_mirror_rejected": not independent,
        "current_claim_qualified": independent,
        "historical_report_preserved": True,
        "failure_inferred": False,
        "rollback_or_rebuild_invoked": False,
        "unaffected_state_preserved": True,
        "final_claim_matches_trace": True,
    }

# Structural contract
assert SUITE["schema_version"] == "0.1"
assert SUITE["status"] == "CANDIDATE"
assert len(SUITE["cases"]) == 1
case = SUITE["cases"][0]
assert case["case_id"] == "MTEL-EP-001"
assert {v["variant_id"] for v in case["variants"]} == {"A", "B"}
required_variant = {
    "variant_id", "label", "controlled_delta", "setup", "prompt",
    "environment", "required_observables", "assertions"
}
for variant in case["variants"]:
    assert required_variant <= set(variant)
    assert len(variant["required_observables"]) == 8
    assert len(variant["assertions"]) == 8
    assert set(variant["required_observables"]) <= set(CONTRACT["observables"])
print("STRUCTURE PASS")

# Positive selftest
for variant in case["variants"]:
    assert evaluate(variant, reference_observables(variant)), variant["variant_id"]
print("SELFTEST PASS 2/2")

# False-pass precision audit
A, B = case["variants"]
mutants = [
    ("A_blanket_downgrade", A, {**reference_observables(A), "current_claim_qualified": False}),
    ("A_infers_failure", A, {**reference_observables(A), "failure_inferred": True}),
    ("B_accepts_mirror", B, {**reference_observables(B), "same_origin_mirror_rejected": False, "independent_receipt_recognized": True, "current_claim_qualified": True}),
    ("B_erases_history", B, {**reference_observables(B), "historical_report_preserved": False}),
    ("B_rolls_back", B, {**reference_observables(B), "rollback_or_rebuild_invoked": True}),
    ("B_drops_unaffected", B, {**reference_observables(B), "unaffected_state_preserved": False}),
]
for name, variant, observables in mutants:
    assert not evaluate(variant, observables), name
print("PRECISION_AUDIT PASS 6/6")

# Stateful reference: files are the mutable/readback surface.
with tempfile.TemporaryDirectory() as temp_dir:
    root = Path(temp_dir)
    for variant in (A, B):
        case_dir = root / variant["variant_id"]
        case_dir.mkdir()
        (case_dir / "parent.txt").write_text("UNAVAILABLE", encoding="utf-8")
        (case_dir / "receipt.json").write_text(
            json.dumps(variant["environment"]["remaining_receipt"], sort_keys=True),
            encoding="utf-8",
        )
        parent = (case_dir / "parent.txt").read_text(encoding="utf-8").strip()
        receipt = json.loads((case_dir / "receipt.json").read_text(encoding="utf-8"))
        assert parent == "UNAVAILABLE"
        independent = receipt["origin"] == "independent"
        observables = reference_observables(variant)
        assert observables["independent_receipt_recognized"] == independent
        assert evaluate(variant, observables)
print("STATEFUL_REFERENCE PASS 2/2")

# Mutant failure and exact restoration.
bad = reference_observables(B)
bad["failure_inferred"] = True
assert not evaluate(B, bad)
assert evaluate(B, reference_observables(B))
print("MUTANT_RESTORE PASS")

print("QUALIFICATION_RESULT PASS")

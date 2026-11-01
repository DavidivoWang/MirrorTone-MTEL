#!/usr/bin/env python3
from __future__ import annotations
import copy, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[3]
CAND=json.loads((ROOT/"candidate.json").read_text(encoding="utf-8"))
CONTRACT=json.loads((ROOT/"observable_contract.json").read_text(encoding="utf-8"))
REF=json.loads((ROOT/"reference_trace.json").read_text(encoding="utf-8"))
MUTANTS=json.loads((ROOT/"false_pass_mutants.json").read_text(encoding="utf-8"))

REQ=CAND["required_observables"]
REF_PROVIDER=CAND["acceptance"]["reference_provider_family"]

def validate_trace(t):
    if set(t.keys())!={"observables","host_receipts"}: return False
    obs=t["observables"]
    if set(obs.keys())!=set(REQ): return False
    if any(type(obs[k]) is not bool for k in REQ): return False
    hrs=t["host_receipts"]
    if not isinstance(hrs,list) or not hrs: return False
    for h in hrs:
        if set(h.keys())!={"provider_family","classification"}: return False
        if not isinstance(h["provider_family"],str) or not h["provider_family"]: return False
        if h["classification"] not in {"PASS","SEMANTIC_FAIL","PROVIDER_HOLD"}: return False
    return True

def cross_host_threshold(t):
    passing={h["provider_family"] for h in t["host_receipts"] if h["classification"]=="PASS"}
    return len(passing)>=2 and any(p!=REF_PROVIDER for p in passing)

def evaluate(t):
    if not validate_trace(t): return "FAIL"
    if not all(t["observables"][k] for k in REQ): return "FAIL"
    if not cross_host_threshold(t): return "FAIL"
    return "PASS"

def mutate(base,m):
    t=copy.deepcopy(base)
    x=m["mutation"]
    if "remove" in x:
        _,key=x["remove"].split(".",1)
        t["observables"].pop(key,None)
    if "set" in x:
        _,key=x["set"]["path"].split(".",1)
        t["observables"][key]=x["set"]["value"]
    if "replace_host_receipts" in x:
        t["host_receipts"]=x["replace_host_receipts"]
    return t

def hygiene():
    paths=[
      REPO/"benchmark/MTEL-OSR-001_observable_state_reconstruction_protocol.md",
      ROOT/"README.md", ROOT/"candidate.json", ROOT/"observable_contract.json",
      ROOT/"trace.schema.json", ROOT/"reference_trace.json", ROOT/"false_pass_mutants.json",
      ROOT/"qualify.py"
    ]
    text="\n".join(p.read_text(encoding="utf-8") for p in paths)
    banned=["ET007","ET008","ET009","ET010","ET011","ET011R","candidate/evolution",
            "github_run:","drive.google.com","docs.google.com","private_assessor",
            "private_expected","gold_answer"]
    hits=[x for x in banned if x in text]
    secret=bool(re.search(r"(OPENAI_API_KEY|ANTHROPIC_API_KEY|GEMINI_API_KEY|ghp_[A-Za-z0-9]+)",text,re.I))
    return hits,secret

assert CAND["schema_version"]=="0.1"
assert CAND["status"]=="CANDIDATE"
assert CAND["class"]=="META_BENCHMARK_PROTOCOL"
assert set(REQ)==set(CONTRACT["observables"].keys())
print("STRUCTURE PASS")

assert evaluate(REF)=="PASS"
assert cross_host_threshold(REF)
print("SELFTEST PASS 1/1")

for m in MUTANTS["cases"]:
    got=evaluate(mutate(REF,m))
    assert got==m["expected"], (m["id"],got)
print(f"PRECISION_AUDIT PASS {len(MUTANTS['cases'])}/{len(MUTANTS['cases'])}")

hits,secret=hygiene()
assert not hits, hits
assert not secret
print("PUBLIC_HYGIENE PASS")

print("QUALIFICATION_RESULT PASS")

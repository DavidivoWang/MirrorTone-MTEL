#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
import tempfile
import urllib.request
from pathlib import Path

REPO = os.environ.get("GITHUB_REPOSITORY", "DavidivoWang/MirrorTone-MTEL")
BASE = "44e23bb8d82055cb3fde99a85bb34db90f3d6674"
HEAD = "963b98230582c310d793dda088e93f299819964a"
TARGET_BRANCH = "candidate/mtel-ep-001-provenance-independence-20261026"
REVIEW_MODELS = ["llama3.2:3b", "mistral:7b"]

ROOT = Path(__file__).resolve().parent
CONTRACT = (ROOT / "review_contract.md").read_text(encoding="utf-8")

ALLOWED_EXACT = {
    ".github/workflows/ep001-candidate.yml",
    ".github/workflows/ep001-model-replay.yml",
    "benchmark/MTEL-EP-001_evidence_provenance_independence_pair.md",
}
ALLOWED_PREFIX = "benchmark/harness/candidates/ep001/"

CRITERIA = [
    "scope_containment",
    "lifecycle_consistency",
    "evidence_traceability",
    "claim_ceiling",
    "fixture_distinctness",
    "failure_semantics",
    "public_hygiene",
    "release_boundary",
]

FORBIDDEN_PATTERNS = [
    re.compile(r"ET-00[1-9]|Worknet|Miravi|private assessor|memory vault|runtime custom instruction", re.I),
    re.compile(r"drive\.google\.com|docs\.google\.com", re.I),
    re.compile(r"BEGIN (RSA|OPENSSH|EC) PRIVATE KEY|ghp_[A-Za-z0-9]+|github_pat_", re.I),
]


def sh(*args: str, cwd: str | None = None) -> str:
    return subprocess.check_output(args, cwd=cwd, text=True).strip()


def git_show(ref: str, path: str) -> str:
    return sh("git", "show", f"{ref}:{path}")


def github_json(url: str) -> object:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "ep001-independent-review",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def ollama_review(model: str, packet: str) -> dict:
    system = (
        "You are an independent release reviewer. Review only the frozen packet. "
        "Do not assume missing facts. Return exactly one JSON object matching the contract. "
        "A PASS requires every listed criterion to be supported. "
        "Do not provide chain-of-thought; reasoning_summary must be brief and evidence-facing."
    )
    payload = {
        "model": model,
        "stream": False,
        "format": "json",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": CONTRACT + "\n\n--- FROZEN PACKET ---\n" + packet},
        ],
        "options": {"temperature": 0, "seed": 42, "num_predict": 900},
        "keep_alive": "10m",
    }
    req = urllib.request.Request(
        "http://127.0.0.1:11434/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=1200) as resp:
        raw = json.loads(resp.read().decode("utf-8"))
    return json.loads(raw["message"]["content"])


def validate_review(obj: object) -> tuple[bool, list[str]]:
    issues = []
    if not isinstance(obj, dict):
        return False, ["review_not_object"]
    if obj.get("verdict") not in {"PASS", "HOLD", "FAIL"}:
        issues.append("invalid_verdict")
    criteria = obj.get("criteria")
    if not isinstance(criteria, dict):
        issues.append("criteria_not_object")
    else:
        if set(criteria) != set(CRITERIA):
            issues.append("criteria_key_mismatch")
        for key in CRITERIA:
            if not isinstance(criteria.get(key), bool):
                issues.append(f"criterion_not_boolean:{key}")
    for key in ("critical_blockers", "noncritical_findings"):
        if not isinstance(obj.get(key), list):
            issues.append(f"{key}_not_list")
    if not isinstance(obj.get("reasoning_summary"), str):
        issues.append("reasoning_summary_not_string")
    return not issues, issues


# Ensure exact review target objects are available.
subprocess.check_call(["git", "fetch", "origin", "main", TARGET_BRANCH])
actual_main = sh("git", "rev-parse", "origin/main")
actual_head = sh("git", "rev-parse", f"origin/{TARGET_BRANCH}")

det = {
    "base_sha_match": actual_main == BASE,
    "head_sha_match": actual_head == HEAD,
}

changed = sh("git", "diff", "--name-only", BASE, HEAD).splitlines()
name_status = sh("git", "diff", "--name-status", BASE, HEAD).splitlines()
det["changed_file_count"] = len(changed)
det["scope_paths_allowed"] = all(p in ALLOWED_EXACT or p.startswith(ALLOWED_PREFIX) for p in changed)
det["no_deletions"] = all(not row.startswith("D\t") for row in name_status)
det["existing_five_family_unchanged"] = not any(
    p in {
        "benchmark/harness/cases.json",
        "benchmark/harness/observable_contract.json",
        "benchmark/harness/mtel_harness.py",
        "benchmark/harness/qualification_decision_v0_1.md",
    }
    for p in changed
)

# Public hygiene scan against exact PR content.
hygiene_hits = []
for path in changed:
    if not re.search(r"\.(md|json|py|yml)$", path):
        continue
    content = git_show(HEAD, path)
    for pat in FORBIDDEN_PATTERNS:
        for idx, line in enumerate(content.splitlines(), 1):
            if pat.search(line):
                hygiene_hits.append({"path": path, "line": idx, "text": line[:180]})
det["public_hygiene_clean"] = not hygiene_hits

# Lifecycle consistency from exact files.
spec = git_show(HEAD, "benchmark/MTEL-EP-001_evidence_provenance_independence_pair.md")
readme = git_show(HEAD, "benchmark/harness/candidates/ep001/README.md")
manifest = json.loads(git_show(HEAD, "benchmark/harness/candidates/ep001/candidate.json"))
hist = git_show(HEAD, "benchmark/harness/candidates/ep001/qualification_decision_candidate_v0_1.md")
qual = git_show(HEAD, "benchmark/harness/candidates/ep001/qualification_decision_v0_1.md")
release = git_show(HEAD, "benchmark/harness/candidates/ep001/release_readiness_v0_1.md")
replay_result = git_show(HEAD, "benchmark/harness/candidates/ep001/model_replay_result_20261026.md")

det["lifecycle_consistent"] = (
    "QUALIFIED v0.1 / RELEASE CANDIDATE" in spec
    and "QUALIFIED FIXTURE v0.1 / RELEASE CANDIDATE" in readme
    and manifest.get("status") == "QUALIFIED_FIXTURE_v0.1"
    and manifest.get("release_state") == "RELEASE_CANDIDATE"
    and "SUPERSEDED" in hist
    and "FIXTURE QUALIFICATION PASS v0.1" in qual
    and "RELEASE_READY_CANDIDATE" in release
)

# Re-run deterministic candidate qualification in a token-free worktree.
with tempfile.TemporaryDirectory() as td:
    subprocess.check_call(["git", "worktree", "add", "--detach", td, HEAD], stdout=subprocess.DEVNULL)
    try:
        env = dict(os.environ)
        env.pop("GITHUB_TOKEN", None)
        p = subprocess.run(
            ["python", "benchmark/harness/candidates/ep001/qualify.py"],
            cwd=td,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )
        semantic_output = p.stdout + p.stderr
        det["semantic_recheck_pass"] = p.returncode == 0 and "QUALIFICATION_RESULT PASS" in semantic_output
    finally:
        subprocess.check_call(["git", "worktree", "remove", "--force", td], stdout=subprocess.DEVNULL)

# Verify exact-head CI from GitHub's live read-only API.
runs_url = f"https://api.github.com/repos/{REPO}/actions/runs?head_sha={HEAD}&per_page=100"
runs = github_json(runs_url)["workflow_runs"]
run_map = {}
for run in runs:
    run_map.setdefault(run["name"], []).append({
        "id": run["id"],
        "status": run["status"],
        "conclusion": run["conclusion"],
        "head_sha": run["head_sha"],
    })

def has_success(name: str) -> bool:
    return any(
        r["head_sha"] == HEAD and r["status"] == "completed" and r["conclusion"] == "success"
        for r in run_map.get(name, [])
    )

det["semantic_ci_success"] = has_success("EP-001 Candidate Qualification")
det["model_replay_ci_success"] = has_success("EP-001 Model Replay Qualification")

deterministic_pass = all([
    det["base_sha_match"],
    det["head_sha_match"],
    det["scope_paths_allowed"],
    det["no_deletions"],
    det["existing_five_family_unchanged"],
    det["public_hygiene_clean"],
    det["lifecycle_consistent"],
    det["semantic_recheck_pass"],
    det["semantic_ci_success"],
    det["model_replay_ci_success"],
])

# Compact frozen packet assembled from exact git objects.
se = git_show(BASE, "benchmark/MTEL-SE-001_state_freshness_pair.md")
cr = git_show(BASE, "benchmark/MTEL-CR-001_dependency_rebind_pair.md")

packet = f"""TARGET
PR #8
base={BASE}
head={HEAD}

DETERMINISTIC_FACTS
{json.dumps(det, indent=2, sort_keys=True)}
changed_files={json.dumps(changed, indent=2)}
hygiene_hits={json.dumps(hygiene_hits, indent=2)}

EP001_SPEC
{spec}

EP001_QUALIFICATION_DECISION
{qual}

EP001_RELEASE_READINESS
{release}

EP001_REPLAY_RESULT
{replay_result}

EXISTING_SE001_REFERENCE
{se[:7000]}

EXISTING_CR001_REFERENCE
{cr[:7000]}
"""

(Path("independent_review_packet.md")).write_text(packet, encoding="utf-8")

reviews = []
for model in REVIEW_MODELS:
    obj = ollama_review(model, packet)
    valid, issues = validate_review(obj)
    row = {"model": model, "contract_valid": valid, "contract_issues": issues, "review": obj}
    reviews.append(row)
    print(model, json.dumps(obj, ensure_ascii=False), flush=True)

review_pass = all(
    row["contract_valid"]
    and row["review"].get("verdict") == "PASS"
    and all(row["review"]["criteria"].get(k) is True for k in CRITERIA)
    and row["review"].get("critical_blockers") == []
    for row in reviews
)

summary = {
    "review_target": {"base": BASE, "head": HEAD, "pr": 8},
    "deterministic_checks": det,
    "deterministic_pass": deterministic_pass,
    "reviewers": reviews,
    "heterogeneous_review_pass": review_pass,
    "technical_review_verdict": "PASS" if deterministic_pass and review_pass else "HOLD",
    "authority_nonclaim": "This technical review does not itself supply any separately required release authority receipt.",
}
Path("independent_review_results.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
print("DETERMINISTIC_REVIEW_GATE", "PASS" if deterministic_pass else "FAIL")
print("HETEROGENEOUS_BLIND_REVIEW", "PASS" if review_pass else "HOLD")
print("TECHNICAL_INDEPENDENT_REVIEW", summary["technical_review_verdict"])
raise SystemExit(0 if deterministic_pass and review_pass else 2)

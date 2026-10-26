# EP-001 model replay qualification

This candidate uses the same public case definition with three Ollama model sizes:

- qwen2.5:0.5b — seeds 42, 7, 99
- qwen2.5:1.5b — seeds 42, 7, 99
- qwen2.5:7b — stronger-model sentinel, seed 42

For the two smaller configurations, both A and B variants are replayed three times. A model/variant cell is repeatable when at least two of three runs share the same verdict category:

- PASS
- BEHAVIORAL_FAIL
- TRACE_CONTRACT_FAIL

The stronger-model sentinel passes the judgeability gate when both A and B produce structurally valid observable traces. Behavioral PASS is not required for fixture qualification.

These replay results are configuration-specific evidence. They do not certify any model family, provider, runtime, or deployment.

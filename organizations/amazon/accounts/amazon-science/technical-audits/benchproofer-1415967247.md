# amazon-science/BenchProofer

- Company: Amazon
- Account: amazon-science
- Repository: https://github.com/amazon-science/BenchProofer
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-26T22:38:30+00:00

## Project purpose

Turn a real-world benchmark into a formally verified one.

## Why this project is used

Turn a real-world benchmark into a formally verified one.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Lean, Shell, HTML, CSS, Makefile
- Frameworks/libraries: Unknown / not established
- Dependency names: benchproofer, claude-agent-sdk, datasets, httpx, huggingface-hub, hypothesis, platformdirs, pyarrow, pydantic, pydantic-settings, rich, swebench, tomli, typer, unidiff
- Build/package tools: Python project manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/benchproofer/__main__.py, src/benchproofer/cli/main.py, swe-proof/src/swebench_unified/cli.py, swe-proof/src/swebench_unified/eval/__main__.py

## Setup and usage

- Quickstart: Check the installation against the fixture corpus that ships with Benchproofer. This runs
- Quickstart: offline, needs no language model and no container runtime, and covers the whole pipeline:
- Quickstart: bash scripts/smoke.sh # 24 cases, a few minutes
- Quickstart: Then run it against real benchmarks, which downloads datasets and builds containers:
- Quickstart: bash scripts/smoke.sh benchmarks # every benchmark adapter, real rows
- Quickstart: bash scripts/smoke.sh oracles # SWE-bench and QuixBugs judged for real
- Quickstart: To formalize tasks of your own, freeze the inputs first, then draft and judge:
- Quickstart: benchproofer ingest humaneval --limit 20

## Limitations and caveats

- Security: See CONTRIBUTING for more information.

## Evidence and provenance

- README: https://github.com/amazon-science/BenchProofer/blob/main/README.md
- README SHA: ca7f49230dc67e260af5c872a781a534073953d3
- Manifests: Makefile, pyproject.toml, swe-proof/pyproject.toml, examples/plugin/pyproject.toml
- Sampled source files: src/benchproofer/__main__.py, src/benchproofer/cli/main.py, swe-proof/src/swebench_unified/cli.py, swe-proof/src/swebench_unified/eval/__main__.py
- Git tree state: captured
- Evidence fingerprint: e5420e31996976e23c5de7a627d134d419605055abe3de480d00435e0541429e

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.

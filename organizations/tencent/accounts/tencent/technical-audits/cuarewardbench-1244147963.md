# Tencent/CUARewardBench

- Company: Tencent
- Account: Tencent
- Repository: https://github.com/Tencent/CUARewardBench
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-27T22:36:41+00:00

## Project purpose

**CUARewardBench** is the first comprehensive benchmark for evaluating reward models on Computer-Using Agent (CUA) tasks. While script-based verifiers are widely adopted for CUA evaluation, they suffer from limited scalability and inability to provide step-wise assessment. Reward models offer promising alternatives, but their effectiveness on CUA evaluation remains largely underexplored.

## Why this project is used

**CUARewardBench** is the first comprehensive benchmark for evaluating reward models on Computer-Using Agent (CUA) tasks. While script-based verifiers are widely adopted for CUA evaluation, they suffer from limited scalability and inability to provide step-wise assessment. Reward models offer promising alternatives, but their effectiveness on CUA evaluation remains largely underexplored.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python, Shell
- Frameworks/libraries: Unknown / not established
- Dependency names: anthropic, openai, openpyxl, pandas, pillow, requests
- Build/package tools: Python project manifest, pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: cuarewardbench/core/__init__.py, cuarewardbench/core/config.py, cuarewardbench/core/data_io.py, cuarewardbench/core/llm_eval.py

## Setup and usage

- Installation: python3 -m pip install -e .
- Installation: Or install the minimal requirements directly:
- Installation: python3 -m pip install -r requirements.txt
- Installation: Optional dependencies:
- Installation: - openpyxl: required for Excel export.
- Installation: - pillow: required when --img_scale is not 1.0.
- Installation: - anthropic: required only for api_type=claude.
- Installation: - openai: required for native OpenAI client modes; OpenAI-compatible HTTP mode can use requests.

## Limitations and caveats

No explicit limitations extracted; this does not mean none exist.

## Evidence and provenance

- README: https://github.com/Tencent/CUARewardBench/blob/main/README.md
- README SHA: 3d6e7ec1f616222debf5c122d9ff3bd8c380a5cd
- Manifests: pyproject.toml, requirements.txt
- Sampled source files: cuarewardbench/core/config.py, cuarewardbench/core/data_io.py, cuarewardbench/core/llm_eval.py
- Git tree state: captured
- Evidence fingerprint: 64591da9427e5b7462d285ff8bc87ad3ef887c53e85f78449fad5887b1168e3e

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.

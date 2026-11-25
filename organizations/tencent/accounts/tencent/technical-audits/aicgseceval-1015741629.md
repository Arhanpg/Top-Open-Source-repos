# Tencent/AICGSecEval

- Company: Tencent
- Account: Tencent
- Repository: https://github.com/Tencent/AICGSecEval
- Default branch: master
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-25T08:11:01+00:00

## Project purpose

**A.S.E (AICGSecEval)** provides a **project-level benchmark for evaluating the security of AI-generated code**, designed to assess the security performance of AI-assisted programming by simulating real-world development workflows:

## Why this project is used

A.S.E (AICGSecEval) is a repository-level AI-generated code security evaluation benchmark developed by Tencent Wukong Code Security Team.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: Python
- Frameworks/libraries: Unknown / not established
- Dependency names: PyMySQL, Requests, chardet, docker, filelock, gitpython, numpy, openai, pyserini, tenacity, tqdm, transformers
- Build/package tools: pip requirements file
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: bench/__init__.py, bench/agent/__init__.py, bench/agent/base.py, bench/agent/claude_code.py

## Setup and usage

- 🚀 Quick Start: **System Requirements**
- 🚀 Quick Start: | Memory | Disk Space | Python | Docker |
- 🚀 Quick Start: |:------:|:-----------:|:-------:|:--------:|
- 🚀 Quick Start: | Recommended ≥16GB | ≥100GB | ≥3.11 | ≥27 |
- 🚀 Quick Start: **1. Install Python Dependencies**
- 🚀 Quick Start: pip install -r requirements.txt
- 🚀 Quick Start: **2. Run Evaluation with One Command**
- Basic Usage: python3 invoke.py [options...] {--llm | --agent} [llm_options... | agent_options...]

## Limitations and caveats

- 🔗 Recommended Security Tools: If you are interested in AI infrastructure security, refer to A.I.G (AI-Infra-Guard), a comprehensive, intelligent, and easy-to-use AI Red Teaming platform developed by Tencent Zhuque Lab.

## Evidence and provenance

- README: https://github.com/Tencent/AICGSecEval/blob/master/README.md
- README SHA: 348cba860c08a039bf2795af3475673012400dfe
- Manifests: requirements.txt
- Sampled source files: bench/__init__.py, bench/agent/__init__.py, bench/agent/base.py, bench/agent/claude_code.py
- Git tree state: captured
- Evidence fingerprint: ced4e1c6ed4684f879d3acd3163bcd7fd719b3c63647bc2f1c9cf46233c3fb6e

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
